"use client";
import * as React from "react";
import { useState } from "react";

function FunkyStory() {
  const [plantName, setPlantName] = useState("");
  const [plantType, setPlantType] = useState("");
  const [plantDetails, setPlantDetails] = useState("");
  const [storyLength, setStoryLength] = useState("100");
  const [story, setStory] = useState("Story here...");
  const [loading, setLoading] = useState(false);

  async function handleGenerateStory() {
    setLoading(true);
    try {
      const response = await fetch("/api/funky-story", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          plant_type: plantType,
          plant_name: plantName,
          plant_details: plantDetails,
          story_length: storyLength,
        }),
      });
      const data = await response.json();
      setStory(data.story);
    } catch (error) {
      console.error("Error:", error);
      setStory("Failed to fetch story.");
    }
    setLoading(false);
  }

  return (
    <main className="min-h-screen bg-[#f0edf2] flex flex-col items-center justify-start px-4 relative overflow-hidden">
      {/* Background bubble */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-[70%] w-[125vw] h-[50vw] bg-[#7c9ea3] rounded-full px-4 text-white text-center text-4xl font-bold flex items-center justify-center z-0" />

      {/* Title */}
      <div className="relative z-10 flex items-center justify-center text-[#f0edf2] text-6xl font-bold gap-2 mt-[12vh]">
        <img
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/4dae54090e1f6ef2fb3e3008b2a1d3d0e7713ad3"
          className="h-[80px] w-[80px] max-sm:w-12 max-sm:h-12"
          alt="Watering Plant Left"
        />
        <span>Funky Story Generator</span>
        <img
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/75e5c9bfea7e2cbde94f9c25fb12e63940c7962e"
          className="h-[80px] w-[80px] max-sm:w-12 max-sm:h-12"
          alt="Watering Plant Right"
        />
      </div>

      {/* Chat Interface */}
      <div className="flex items-center justify-center gap-20 mt-40 w-full max-w-6xl">
        {/* Left side: plant icon + Ask box */}
        <div className="flex flex-col items-center gap-4">
          <input
            type="text"
            placeholder="Plant name"
            className="p-2 rounded-xl text-xl bg-white text-black border border-gray-300 shadow-sm w-72"
            value={plantName}
            onChange={(e) => setPlantName(e.target.value)}
          />
          <input
            type="text"
            placeholder="Plant type"
            className="p-2 rounded-xl text-xl bg-white text-black border border-gray-300 shadow-sm w-72"
            value={plantType}
            onChange={(e) => setPlantType(e.target.value)}
          />
          <input
            type="text"
            placeholder="Plant details"
            className="p-2 rounded-xl text-xl bg-white text-black border border-gray-300 shadow-sm w-72"
            value={plantDetails}
            onChange={(e) => setPlantDetails(e.target.value)}
          />
          <input
            type="number"
            placeholder="Story length (words)"
            className="p-2 rounded-xl text-xl bg-white text-black border border-gray-300 shadow-sm w-72"
            value={storyLength}
            onChange={(e) => setStoryLength(e.target.value)}
          />
          <button
            onClick={handleGenerateStory}
            className="mt-2 bg-green-500 text-white px-4 py-2 rounded-xl text-xl"
            disabled={loading}
          >
            {loading ? "Generating..." : "Generate Story"}
          </button>
        </div>

        {/* Right side: Response box + plant icon */}
        <div className="flex items-center gap-4">
          <div
            role="textbox"
            tabIndex={0}
            aria-label="Chat response area"
            className="flex-1 shrink p-9 w-[500px] min-h-[309px] bg-zinc-400 rounded-2xl text-lg text-white overflow-y-auto"
          >
            {story}
          </div>
          <img
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/41385efda9563a0a206d237dcdc21cf13c026a41?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
            alt="Chat response icon"
            className="object-contain w-[60px]"
          />
        </div>
      </div>
    </main>
  );
}

export default FunkyStory;


