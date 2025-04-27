import React from "react";

function Header() {
  return (
    <header className="flex gap-10 items-end pt-20 w-full font-bold tracking-tighter text-center text-gray-100 rounded-full bg-slate-400 leading-[86px] text-[length:var(--sds-typography-title-hero-size)] max-md:max-w-full">
      <img
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/4db0851930728d8be9907bb0029ce1669d821a30?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
        alt="Plant decoration left"
        className="object-contain shrink-0 mt-24 max-w-full aspect-[0.92] w-[161px] max-md:mt-10"
      />
      <img
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/9e76e02156a14a25bf171c095fdbb0debc9b0475?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
        alt="Plant decoration"
        className="object-contain shrink-0 self-start max-w-full aspect-square w-[125px]"
      />
      <h1 className="grow shrink mt-10 w-[309px] max-md:text-4xl max-md:leading-[53px]">
        Plant Care <br />
        Chatbot
      </h1>
      <img
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/5278bedea1272ad48cf68406a4a494bd65ea38d4?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
        alt="Plant decoration"
        className="object-contain shrink-0 self-start max-w-full aspect-square w-[125px]"
      />
      <img
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/a887b8fa85815fa6c167bb29238836559625cef8?placeholderIfAbsent=true&apiKey=1c3858503713423d98bf7a76ad7001c7"
        alt="Plant decoration right"
        className="object-contain shrink-0 mt-24 max-w-full aspect-[0.89] w-[156px] max-md:mt-10"
      />
    </header>
  );
}

export default Header;

