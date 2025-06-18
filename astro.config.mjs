// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
// export default defineConfig({});

import rehypeExternalLinks from 'rehype-external-links';

// adds target="_blank" to md links
export default defineConfig({
  markdown: {
    rehypePlugins: [
      [
        rehypeExternalLinks,
        {
          target: '_blank',
          // Optional: Add rel="noopener noreferrer" for security
          rel: ['noopener', 'noreferrer'],
        },
      ],
    ],
  },
});
