import { Card } from "./Card";

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
        <button className="absolute left-0 bottom-0 w-80 h-40 bg-[#b5c6a8] text-[#f0edf2] font-semibold rounded-[25px_80px_25px_25px] shadow-md hover:scale-105 transition-transform">
          talk to me<br />bby
        </button>

        {/* Bottom Right */}
        <button className="absolute right-0 bottom-0 w-80 h-40 bg-[#b898c6] text-[#f0edf2] font-semibold rounded-[80px_25px_25px_25px] shadow-md hover:scale-105 transition-transform">
          who am i<br />mommy
        </button>

        {/* Top Right */}
        <button className="absolute right-0 top-0 w-80 h-40 bg-[#9c83aa] text-[#f0edf2] font-semibold rounded-[25px_25px_25px_80px] shadow-md hover:scale-105 transition-transform">
          gimme mo<br />plant
        </button>

        {/* Top Left */}
        <button className="absolute left-0 top-0 w-80 h-40 bg-[#96c1b2] text-[#f0edf2] font-semibold rounded-[25px_25px_80px_25px] shadow-md hover:scale-105 transition-transform">
          where did i<br />come from
        </button>
      </div>
    </section>
  );
}
