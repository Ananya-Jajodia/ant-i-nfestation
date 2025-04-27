import { Card } from "./Card";
import Link from 'next/link';

export function GridSection() {
  return (
    <section className="relative p-5 mx-auto my-0 max-w-[1200px]">
      {/* <img
        src="https://cdn.builder.io/api/v1/image/assets%2F1c3858503713423d98bf7a76ad7001c7%2Fdfc011d0c539449c8ad45f50ad7d34bc"
        className="right-0 box-border object-cover overflow-hidden shrink-0 mt-5 w-full aspect-square grow-0 max-w-48 min-h-5 min-w-5"
      /> */}
      {/* Flower Buttons */}
      <div className="relative w-full max-w-md mt-[30vh]">
        {/* Center circle */}
        <div className="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2 w-12 h-12 bg-[#fff9db] rounded-full border border-gray-400 z-10"></div>

        {/* Bottom Left */}
        <Link href="/plantcare_chatbot">
          <button className="absolute left-0 bottom-0 w-80 h-40 bg-[#b5c6a8] text-[#f0edf2] font-semibold rounded-[25px_80px_25px_25px] shadow-md hover:scale-105 transition-transform">
            Plant Care <br />Chatbot
          </button>
        </Link>

        {/* Bottom Right */}
        <Link href="/identifier">
          <button className="absolute right-0 bottom-0 w-80 h-40 bg-[#b898c6] text-[#f0edf2] font-semibold rounded-[80px_25px_25px_25px] shadow-md hover:scale-105 transition-transform">
            Identify A<br />Plant
          </button>
        </Link>

        {/* Top Right */}
        <Link href="/suggestor">
          <button className="absolute right-0 top-0 w-80 h-40 bg-[#9c83aa] text-[#f0edf2] font-semibold rounded-[25px_25px_25px_80px] shadow-md hover:scale-105 transition-transform">
            Plant<br />Suggestor
          </button>
        </Link>

        {/* Top Left */}
        <Link href="/funky_story">
          <button className="absolute left-0 top-0 w-80 h-40 bg-[#96c1b2] text-[#f0edf2] font-semibold rounded-[25px_25px_80px_25px] shadow-md hover:scale-105 transition-transform">
            Funky Story<br />Generator
          </button>
        </Link>
      </div>
    </section >
  );
}
