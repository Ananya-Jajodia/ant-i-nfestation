import React from "react";

function ChatInput() {
  return (
    <div className="max-md:mt-10 max-md:max-w-full">
      <div className="flex gap-5 max-md:flex-col">
        <div className="w-[15%] max-md:ml-0 max-md:w-full">
          <img
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/eab58d5df972b8ee7e290806ed41ac6ecc295416?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
            alt="Chat input icon"
            className="object-contain shrink-0 mt-20 aspect-[1.07] w-[92px] max-md:mt-10"
          />
        </div>
        <div className="ml-5 w-[85%] max-md:ml-0 max-md:w-full">
          <div className="w-full text-6xl min-h-[209px] text-zinc-300 max-md:mt-3.5 max-md:max-w-full max-md:text-4xl">
            <div
              role="textbox"
              tabIndex={0}
              aria-label="Chat input area"
              className="flex-1 shrink gap-10 self-stretch p-9 w-full bg-white rounded-2xl basis-0 max-md:px-5 max-md:max-w-full max-md:text-4xl"
            >
              Ask questions here...
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ChatInput;
