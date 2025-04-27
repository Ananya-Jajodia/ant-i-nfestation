import React from "react";

function ChatResponse() {
  return (
    <div className="flex flex-wrap grow gap-9 text-6xl text-zinc-300 max-md:mt-10 max-md:text-4xl">
      <div className="grow shrink-0 basis-0 min-h-[419px] w-fit max-md:max-w-full max-md:text-4xl">
        <div
          role="textbox"
          tabIndex={0}
          aria-label="Chat response area"
          className="flex-1 shrink gap-10 self-stretch p-9 w-full rounded-2xl basis-0 bg-zinc-400 max-md:px-5 max-md:max-w-full max-md:text-4xl"
        >
          Responses here...
        </div>
      </div>
      <img
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/41385efda9563a0a206d237dcdc21cf13c026a41?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
        alt="Chat response icon"
        className="object-contain shrink-0 mt-10 aspect-[0.95] w-[82px] max-md:mt-5"
      />
    </div>
  );
}

export default ChatResponse;
