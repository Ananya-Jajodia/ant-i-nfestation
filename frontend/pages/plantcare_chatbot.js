// "use client";
// import * as React from "react";
// import ChatbotHeader from "./components/ChatbotHeader";
// import ChatInterface from "./components/ChatInterface";
// import ChatInput from "./components/ChatInput";
// import ChatResponse from "./components/ChatResponse";

// function TalkyPage() {
//   return (
//     <main className="min-h-screen bg-[#f0edf2] flex flex-col flexitems-center justify-start px-4 relative overflow-hidden">


//       <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-[70%] w-[125vw] h-[50vw] bg-[#7c9ea3] rounded-full px-4 text-white text-center text-4xl font-bold flex items-center justify-center z-0" />

//       <div className="relative z-10 flex items-center justify-center text-[#f0edf2] text-6xl font-bold gap-2 mt-[12vh]">

//         <img
//           src="https://cdn.builder.io/api/v1/image/assets/TEMP/4dae54090e1f6ef2fb3e3008b2a1d3d0e7713ad3"
//           className="h-[80px] w-[80px] max-sm:w-12 max-sm:h-12"
//           alt="Watering Plant Left"
//         />
//         <span>Plant Care Chatbot</span>
//         <img
//           src="https://cdn.builder.io/api/v1/image/assets/TEMP/75e5c9bfea7e2cbde94f9c25fb12e63940c7962e"
//           className="h-[80px] w-[80px] max-sm:w-12 max-sm:h-12"
//           alt="Watering Plant Right"
//         />
//       </div>
//       <div className="flex items-end justify-center gap-10 mt-16 w-full max-w-6xl">
//         <ChatInput />
//         <ChatResponse />
//       </div>
//       {/* <ChatInterface /> */}
//     </main>
//   );
// }

// export default TalkyPage;

"use client";
import * as React from "react";

function TalkyPage() {
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
        <span>Plant Care Chatbot</span>
        <img
          src="https://cdn.builder.io/api/v1/image/assets/TEMP/75e5c9bfea7e2cbde94f9c25fb12e63940c7962e"
          className="h-[80px] w-[80px] max-sm:w-12 max-sm:h-12"
          alt="Watering Plant Right"
        />
      </div>

      {/* Chat Interface */}
      <div className="flex items-center justify-center gap-20 mt-16 w-full max-w-6xl">

        {/* Left side: plant icon + Ask box */}
        <div className="flex items-center gap-4">
          <img
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/eab58d5df972b8ee7e290806ed41ac6ecc295416?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
            alt="Chat input icon"
            className="object-contain w-[60px]"
          />
          <div
            role="textbox"
            tabIndex={0}
            aria-label="Chat input area"
            className="flex-1 shrink p-9 w-[300px] min-h-[09px] bg-white rounded-2xl text-4xl text-zinc-300"
          >
            Ask questions here...
          </div>
        </div>

        {/* Right side: Response box + plant icon */}
        <div className="flex items-center gap-4">
          <div
            role="textbox"
            tabIndex={0}
            aria-label="Chat response area"
            className="flex-1 shrink p-9 w-[300px] min-h-[109px] bg-zinc-400 rounded-2xl text-4xl text-zinc-300"
          >
            Responses here...
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

export default TalkyPage;

