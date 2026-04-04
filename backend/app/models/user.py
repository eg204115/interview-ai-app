from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
import uuid

from backend.app.core.enums import SenderType

class User(BaseModel):
    userId: str = str(uuid.uuid4())
    email: EmailStr
    firstName: str
    lastName: str
    createdAt: datetime = datetime.utcnow()
    lastLogin: Optional[datetime] = None
    userType: SenderType