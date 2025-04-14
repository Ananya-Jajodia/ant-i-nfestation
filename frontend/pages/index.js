// "use client";
// import * as React from "react";
// import { Header } from "./Header";
import { GridSection } from "./GridSection";
import { FooterGallery } from "./FooterGallery";

// function PottedPetLand() {
//   return (
//     <>
//       <link
//         href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap"
//         rel="stylesheet"
//       />
//       <main className="overflow-hidden relative mx-auto w-full max-w-none min-h-screen bg-gray-100 max-md:max-w-[991px] max-sm:max-w-screen-sm">
//         <Header />
//         <GridSection />
//         <FooterGallery />
//       </main>
//     </>
//   );
// }

// export default PottedPetLand;

// pages/index.js
import Head from 'next/head';

export default function Home() {
  return (
    <>
      {/* <Head>
        <title>Potted Pet Land</title>
        <meta name="description" content="Cute flower nav layout" />
        <link rel="icon" href="/favicon.ico" />
      </Head> */}

      <main className="min-h-screen bg-[#f0edf2] flex flex-col flexitems-center justify-start px-4 relative overflow-hidden">
        {/* Header */}
        {/* <div className="w-full h-[40vh] bg-[#7c9ea3] px-4 text-white text-center text-4xl font-bold flex items-center justify-center relative overflow-hidden">
          <div className="absolute left-6 top-4">🌱</div>
          <span>Potted Pet Land</span>
          <div className="absolute right-6 top-4">🌱</div>
          <div className="absolute bottom-[-40%] left-1/2 -translate-x-1/2 w-[200%] h-[200%] bg-[#f5f5fa] rounded-full z-0"></div>
        </div> */}


        <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-[70%] w-[125vw] h-[50vw] bg-[#7c9ea3] rounded-full px-4 text-white text-center text-4xl font-bold flex items-center justify-center z-0" />

        {/* Title */}
        <div className="relative z-10 flex items-center justify-center text-[#f0edf2] text-6xl font-bold gap-2 mt-[12vh]">

          <img
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/4dae54090e1f6ef2fb3e3008b2a1d3d0e7713ad3"
            className="h-[80px] w-[80px] max-sm:w-12 max-sm:h-12"
            alt="Watering Plant Left"
          />
          <span>Potted Pet Land</span>
          <img
            src="https://cdn.builder.io/api/v1/image/assets/TEMP/75e5c9bfea7e2cbde94f9c25fb12e63940c7962e"
            className="h-[80px] w-[80px] max-sm:w-12 max-sm:h-12"
            alt="Watering Plant Right"
          />
        </div>

        <GridSection />
        <FooterGallery />
      </main>
    </>
  );
}
