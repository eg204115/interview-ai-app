from database.mongodb import interviews_collection
from services.gemini_service import generate_questions, generate_closing
from bson import ObjectId


def start_interview(role, difficulty):
    questions = generate_questions(role, difficulty)

    interview = {
        "role": role,
        "difficulty": difficulty,
        "questions": questions,
        "answers": [],
        "current_index": 0,
        "completed": False
    }

    result = interviews_collection.insert_one(interview)

    return str(result.inserted_id), questions[0]


def submit_answer(interview_id, answer):
    interview = interviews_collection.find_one({"_id": ObjectId(interview_id)})

    if not interview or interview["completed"]:
        return {"message": "Interview not found or already completed"}

    index = interview["current_index"]
    questions = interview["questions"]

    # Save answer
    interviews_collection.update_one(
        {"_id": ObjectId(interview_id)},
        {"$push": {"answers": answer}}
    )

    # Move to next question
    index += 1

    if index >= len(questions):
        # End interview
        interviews_collection.update_one(
            {"_id": ObjectId(interview_id)},
            {
                "$set": {
                    "completed": True,
                    "current_index": index
                }
            }
        )

        return {
            "completed": True,
            "message": generate_closing()
        }

    # Update index
    interviews_collection.update_one(
        {"_id": ObjectId(interview_id)},
        {"$set": {"current_index": index}}
    )

    return {
        "completed": False,
        "next_question": questions[index]
    }