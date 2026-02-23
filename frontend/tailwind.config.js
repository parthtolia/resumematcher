/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#0D384D",   // deep navy like professional sites
        accent: "#0056B3",    // bright accent for buttons, links
        text: "#1F2937",
      },
    },
  },
  plugins: [],
}