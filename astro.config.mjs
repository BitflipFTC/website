// @ts-check
import { defineConfig } from 'astro/config';
import cloudflare from '@astrojs/cloudflare';

// https://astro.build/config
// export default defineConfig({});

import rehypeExternalLinks from 'rehype-external-links';

// adds target="_blank" to md links
export default defineConfig({
  output: 'server',

  adapter: cloudflare({

  }),
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
