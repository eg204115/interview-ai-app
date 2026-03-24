

"use client";
import { useRouter } from "next/navigation";

export default function Home() {
  const router = useRouter();

  return (
    <div style={{ padding: 20 }}>
      <h1>Interview Practice AI</h1>
      <button onClick={() => router.push("/interview")}>
        Start Interview
      </button>
    </div>
  );
}