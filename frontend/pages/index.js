import { GridSection } from "./components/GridSection";
import { FooterGallery } from "./components/FooterGallery";
import Head from 'next/head';

export default function Home() {
  return (
    <>
      <main className="min-h-screen bg-[#f0edf2] flex flex-col flexitems-center justify-start px-4 relative overflow-hidden">


        <div className="absolute top-0 left-1/2 -translate-x-1/2 -translate-y-[70%] w-[125vw] h-[50vw] bg-[#7c9ea3] rounded-full px-4 text-white text-center text-4xl font-bold flex items-center justify-center z-0" />

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
