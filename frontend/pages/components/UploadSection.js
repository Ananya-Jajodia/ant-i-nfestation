"use client";
import React, { useRef, useState } from "react";

const UploadSection = () => {
  const fileInputRef = useRef(null);
  const [result, setResult] = useState(null);

  const handleButtonClick = () => {
    fileInputRef.current.click();
  };

  const handleFileChange = async (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const formData = new FormData();
    formData.append("image", file);

    const res = await fetch("/api/identify-plant", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data.plantName || "Unknown");
  };

  return (
    <section className="flex flex-col absolute left-2/4 justify-center items-center -translate-x-2/4 h-[419px] top-[200px] w-[800px]">
      <button
        className="p-9 text-6xl text-center bg-green-600 rounded-2xl border-solid border-[4.525px] border-zinc-300 text-zinc-300 max-md:text-5xl max-sm:p-6 max-sm:text-4xl"
        onClick={handleButtonClick}
      >
        Upload an image of your plant
      </button>

      <input
        type="file"
        accept="image/*"
        ref={fileInputRef}
        onChange={handleFileChange}
        style={{ display: "none" }}
      />

      {result && (
        <p className="mt-6 text-4xl text-green-700 font-bold text-center">
          Plant Name: {result}
        </p>
      )}
    </section>
  );
};

export default UploadSection;

// "use client";
// import React from "react";

// const UploadSection = () => {
//   return (
//     <section className="flex absolute left-2/4 justify-center items-center -translate-x-2/4 h-[419px] top-[200px] w-[800px]">
//       <button className="p-9 text-6xl text-center bg-green-600 rounded-2xl border-solid border-[4.525px] border-zinc-300 text-zinc-300 max-md:text-5xl max-sm:p-6 max-sm:text-4xl">
//         Upload an image of your plant
//       </button>
//     </section>
//   );
// };

// export default UploadSection;
