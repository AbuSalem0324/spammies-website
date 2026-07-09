// @ts-check
import { defineConfig } from 'astro/config';

import tailwindcss from '@tailwindcss/vite';

// https://astro.build/config
export default defineConfig({
  // Used for absolute OG/Twitter image URLs. Override via SITE env if needed.
  site: process.env.SITE || "https://spammies-website.vercel.app",
  vite: {
    plugins: [tailwindcss()],
  },
});
