"use client";
import * as React from "react";
import { useState } from "react";

function TalkyPage() {
  const [query, setQuery] = useState("");
  const [response, setResponse] = useState("Responses here...");
  const [loading, setLoading] = useState(false);

  async function handleAsk() {
    setLoading(true);
    try {
      const res = await fetch("/api/plant-chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ query }),
      });

      const data = await res.json();
      setResponse(data.response || "No response received.");
    } catch (err) {
      console.error("Error:", err);
      setResponse("Failed to fetch response.");
    }
    setLoading(false);
  }

  return (
    <main className="min-h-screen bg-[#f0edf2] flex flex-col items-center justify-start px-4 relative overflow-hidden">
      {/* Background bubble */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-[70%] w-[125vw] h-[50vw] bg-[#7c9ea3] rounded-full px-4 text-white text-center text-4xl font-bold flex items-center justify-center z-0" />

      {/* Title */}
      <div className="relative z-10 flex items-center justify-center text-[#f0edf2] text-6xl font-bold gap-2 mt-[12vh]">
        <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/4dae54090e1f6ef2fb3e3008b2a1d3d0e7713ad3" className="h-[80px] w-[80px]" alt="Watering Plant Left" />
        <span>Plant Care Chatbot</span>
        <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/75e5c9bfea7e2cbde94f9c25fb12e63940c7962e" className="h-[80px] w-[80px]" alt="Watering Plant Right" />
      </div>

      {/* Chat Interface */}
      <div className="flex items-center justify-center gap-20 mt-26 w-full max-w-6xl">
        <div className="flex flex-col items-center gap-4">
          <input
            type="text"
            placeholder="Ask questions here..."
            className="p-2 rounded-xl text-xl bg-white text-black border border-gray-300 shadow-sm w-72"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
          />
          <button
            onClick={handleAsk}
            className="mt-2 bg-green-500 text-white px-4 py-2 rounded-xl text-xl"
            disabled={loading}
          >
            {loading ? "Asking..." : "Ask"}
          </button>
        </div>

        <div className="flex items-center gap-4">
          <div className="flex-1 shrink p-9 w-[700px] min-h-[309px] bg-zinc-400 rounded-2xl text-lg text-white overflow-y-auto">
            {response}
          </div>
          <img src="https://cdn.builder.io/api/v1/image/assets/TEMP/41385efda9563a0a206d237dcdc21cf13c026a41" className="object-contain w-[60px]" alt="Chat response icon" />
        </div>
      </div>
    </main>
  );
}

export default TalkyPage;


