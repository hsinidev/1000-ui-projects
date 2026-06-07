---
name: Heritage Frontier
colors:
  surface: '#fbfbe2'
  surface-dim: '#dbdcc3'
  surface-bright: '#fbfbe2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f5dc'
  surface-container: '#efefd7'
  surface-container-high: '#eaead1'
  surface-container-highest: '#e4e4cc'
  on-surface: '#1b1d0e'
  on-surface-variant: '#504441'
  inverse-surface: '#303221'
  inverse-on-surface: '#f2f2d9'
  outline: '#827470'
  outline-variant: '#d4c3be'
  surface-tint: '#77574d'
  primary: '#442a22'
  on-primary: '#ffffff'
  primary-container: '#5d4037'
  on-primary-container: '#d4ada1'
  inverse-primary: '#e7bdb1'
  secondary: '#1b6d24'
  on-secondary: '#ffffff'
  secondary-container: '#a0f399'
  on-secondary-container: '#217128'
  tertiary: '#432b22'
  on-tertiary: '#ffffff'
  tertiary-container: '#5b4137'
  on-tertiary-container: '#d2aea1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#e7bdb1'
  on-primary-fixed: '#2c160e'
  on-primary-fixed-variant: '#5d4037'
  secondary-fixed: '#a3f69c'
  secondary-fixed-dim: '#88d982'
  on-secondary-fixed: '#002204'
  on-secondary-fixed-variant: '#005312'
  tertiary-fixed: '#ffdbce'
  tertiary-fixed-dim: '#e4beb2'
  on-tertiary-fixed: '#2b160f'
  on-tertiary-fixed-variant: '#5b4137'
  background: '#fbfbe2'
  on-background: '#1b1d0e'
  surface-variant: '#e4e4cc'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-table:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  container-max: 1280px
---

## Brand & Style

This design system is built to evoke a sense of generational trust and rugged permanence. It targets high-net-worth land investors and families seeking legacy properties. The aesthetic is a hybrid of **Tactile / Skeuomorphic** textures and **Corporate** precision. 

The visual language avoids trendy ephemera in favor of an "established" feel. It utilizes the physical metaphors of a well-worn leather saddle and high-quality stationery. UI elements should feel heavy and intentional, utilizing subtle grain textures on backgrounds and crisp, defined borders to suggest a craftsman’s attention to detail. The emotional response is one of reliability, heritage, and the quiet authority of the outdoors.

## Colors

The color palette is anchored in natural, earth-toned hues that reflect the ranching lifestyle.
- **Primary (Leather Brown):** Used for navigation, headers, and primary actions to signify strength and stability.
- **Secondary (Forest Green):** Reserved for growth-oriented call-to-actions, map markers, and success states, connecting the user to the land.
- **Background (Parchment):** This textured neutral replaces sterile whites to provide a warmer, more traditional reading experience.
- **Neutral Accents:** Soft browns and taupes are used for borders and dividers to maintain a low-contrast, sophisticated hierarchy.

## Typography

Typography in this design system balances authoritative storytelling with technical clarity.
- **Headings:** Use **Newsreader** for all editorial and structural titles. It provides a literary, established feel that suggests history and prestige. 
- **Interface & Data:** Use **Work Sans** for all functional UI elements, property specifications, and data-heavy acreage tables. Its grounded, neutral character ensures maximum legibility when displaying complex surveying or financial data.
- **Hierarchy:** Maintain a clear distinction by using Newsreader for property names and Work Sans for technical specs (e.g., price per acre, soil types).

## Layout & Spacing

This design system employs a **Fixed Grid** model to reinforce a sense of structure and traditional order. 
- **Grid:** A 12-column grid with generous 24px gutters.
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Negative Space:** Whitespace (or "Parchment space") should be used liberally to mimic the layout of high-end architectural or sporting magazines. Elements should never feel crowded; the layout should breathe like the open landscapes it represents.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Bold Borders** rather than modern floating shadows. 
- **Surfaces:** Use slightly darker shades of the Parchment background or thin Leather-Brown borders to define containers.
- **Shadows:** When necessary, use very tight, high-opacity shadows that mimic the look of embossed paper or a physical stamp (0px 2px 4px rgba(93, 64, 55, 0.15)).
- **Photography:** Images are treated as physical artifacts, often contained within a 1px solid border (#D7CCC8) with a generous internal margin to create a "matted frame" effect.

## Shapes

The shape language is **Soft (0.25rem)**, suggesting hand-crafted quality. Completely sharp corners feel too aggressive or "digital," while pill-shapes feel too playful. A subtle 4px radius on buttons, cards, and input fields provides a "finished" look without compromising the professional, traditional tone of this design system.

## Components

- **Buttons:** Primary buttons use a solid Leather-Brown fill with centered Work Sans caps. Hover states should darken the fill slightly or introduce a subtle inner-glow to mimic a pressed leather texture.
- **Cards:** Property cards feature a "matted" photo container at the top, followed by a Newsreader title. Secondary data (acreage, price) is displayed in a structured Work Sans grid at the bottom.
- **Inputs:** Form fields should use a 1px solid border in a muted brown. When focused, the border thickens or shifts to Forest Green. Backgrounds should be a shade lighter than the page background to indicate interactivity.
- **Photography Containers:** Always use a 4:3 or 16:9 aspect ratio. Large hero sections should incorporate a subtle grain overlay to soften the digital crispness and align with the tactile brand.
- **Interactive Maps:** Custom map styles should utilize the design system's green and brown palette, avoiding standard "digital blue" water in favor of more muted, natural tones.