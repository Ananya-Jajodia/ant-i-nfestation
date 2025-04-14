export function Header() {
  return (
    <header className="flex relative justify-center items-center rounded-none bg-slate-400 h-[331px] max-sm:h-[250px]">
      <h1 className="text-7xl font-bold tracking-tighter text-center text-gray-100 max-md:text-6xl max-sm:text-4xl">
        Potted Pet Land
      </h1>
      <img
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/4dae54090e1f6ef2fb3e3008b2a1d3d0e7713ad3"
        className="absolute h-[125px] top-[82px] w-[125px] max-sm:w-20 max-sm:h-20 max-sm:top-[60px]"
        alt="Watering Plant"
      />
      <img
        src="https://cdn.builder.io/api/v1/image/assets/TEMP/75e5c9bfea7e2cbde94f9c25fb12e63940c7962e"
        className="absolute h-[125px] top-[82px] w-[125px] max-sm:w-20 max-sm:h-20 max-sm:top-[60px]"
        alt="Watering Plant"
      />
    </header>
  );
}
