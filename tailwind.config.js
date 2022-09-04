const { fontFamily } = require('tailwindcss/defaultTheme');

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./pages/**/*.js', './components/**/*.js', './slices/**/*.js'],
  theme: {
    fontFamily: {
      sans: 'Argent, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "Noto Sans", sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol", "Noto Color Emoji"',
      serif:
        'Brandon, ui-serif, Georgia, Cambria, "Times New Roman", Times, serif',
    },
    extend: {
      fontFamily: {
        primary: ['Argent', ...fontFamily.sans],
        secondary: ['Brandon', ...fontFamily.serif],
        argent: ['Argent', ...fontFamily.sans],
        brandon: ['Brandon', ...fontFamily.serif],
      },
    },
  },
  plugins: [require('@tailwindcss/aspect-ratio')],
};
