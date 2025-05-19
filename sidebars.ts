import type { SidebarsConfig } from '@docusaurus/plugin-content-docs';

const sidebars: SidebarsConfig = {
  tutorialSidebar: [
    {
      type: 'doc',
      id: 'intro', // MUST match the frontmatter ID in docs/intro.md
    },
  ],
};

export default sidebars;
