import React from "react";
import ChatInput from "./ChatInput";
import ChatResponse from "./ChatResponse";

function ChatInterface() {
  return (
    <section className="w-full flex justify-between items-end p-5 mt-auto mb-[-20px] max-sm:flex-wrap max-sm:gap-5 max-sm:justify-center bg-[#f0edf2]">
      <div className="flex gap-5 max-md:flex-col">
        <div className="w-6/12 max-md:ml-0 max-md:w-full">
          <ChatInput />
        </div>
        <div className="ml-5 w-6/12 max-md:ml-0 max-md:w-full">
          <ChatResponse />
        </div>
      </div>
    </section>
  );
}

export default ChatInterface;
