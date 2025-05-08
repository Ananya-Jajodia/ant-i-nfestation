/** @type {import('next').NextConfig} */
const nextConfig = {
  async rewrites() {
    return [
      {
        source: '/api/funky-story',
        destination: 'http://localhost:5050/api/funky-story', // Flask backend
      },
      {
        source: '/api/plant-chat',
        destination: 'http://localhost:5050/api/plant-chat',
      },
    ];
  },
};

export default nextConfig;
