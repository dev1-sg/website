// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  // title: '',
  // tagline: '',
  favicon: 'img/favicon.ico',

  // Corrected the URL to reflect the actual deployment location
  url: 'http://dev1-sg.github.io',
  // Adjusted baseUrl to ensure it ends with a slash for correct path resolution
  baseUrl: '/website/',

  // organizationName: 'dev1-sg', // Ensure this is your actual organization/user name
  // projectName: 'website', // Ensure this is your actual repo name

  onBrokenLinks: 'ignore', // Or 'warn' or 'ignore'
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Ensure docs are served from the baseUrl directly
          routeBasePath: '/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    // // Consider updating or adding a custom social card image relevant to your project
    // image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: '',
      logo: {
        // alt: '',
        src: 'img/logo.png',
        href: '/website/Getting-Started',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Documents',
        },
        {
          // Update this URL to point to your actual GitLab repository
          href: 'https://github.com/dev1-sg/website',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Community',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/dev1-sg',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} dev1.sg, Inc. Built with ❤️`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
