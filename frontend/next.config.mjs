/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/funky-story',
        destination: 'http://localhost:5000/api/funky-story', // Flask backend
      },
    ];
  },
};

export default nextConfig;
