"use client";
import React from "react";

const UploadSection = () => {
  return (
    <section className="flex absolute left-2/4 justify-center items-center -translate-x-2/4 h-[419px] top-[200px] w-[800px]">
      <button className="p-9 text-6xl text-center bg-green-600 rounded-2xl border-solid border-[4.525px] border-zinc-300 text-zinc-300 max-md:text-5xl max-sm:p-6 max-sm:text-4xl">
        Upload an image of your plant
      </button>
    </section>
  );
};

export default UploadSection;