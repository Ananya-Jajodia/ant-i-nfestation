export function Card({ children }) {
  return (
    <article className="p-8 text-5xl font-bold tracking-tighter text-gray-100 rounded border border-black border-solid h-[245px] leading-[60px] shadow-[0_4px_4px_rgba(0,0,0,0.25)] max-md:text-4xl max-md:h-[200px] max-sm:p-5 max-sm:text-3xl max-sm:h-[150px]">
      {children}
    </article>
  );
}
