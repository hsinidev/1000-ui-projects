---
name: Kinetic Juris
colors:
  surface: '#fbf8ff'
  surface-dim: '#d9d9e7'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f2ff'
  surface-container: '#ededfb'
  surface-container-high: '#e7e7f5'
  surface-container-highest: '#e1e1ef'
  on-surface: '#191b25'
  on-surface-variant: '#434656'
  inverse-surface: '#2e303a'
  inverse-on-surface: '#f0effe'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004ced'
  primary: '#003ec7'
  on-primary: '#ffffff'
  primary-container: '#0052ff'
  on-primary-container: '#dfe3ff'
  inverse-primary: '#b7c4ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#464e64'
  on-tertiary: '#ffffff'
  tertiary-container: '#5e667d'
  on-tertiary-container: '#dde4ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b7c4ff'
  on-primary-fixed: '#001452'
  on-primary-fixed-variant: '#0038b6'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#dae2fd'
  tertiary-fixed-dim: '#bec6e0'
  on-tertiary-fixed: '#131b2e'
  on-tertiary-fixed-variant: '#3f465c'
  background: '#fbf8ff'
  on-background: '#191b25'
  surface-variant: '#e1e1ef'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Space Grotesk
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  grid-gutter: 20px
  grid-margin: 32px
---

## Brand & Style

This design system is built for the high-velocity world of venture capital and startup law. It rejects the stuffy, wood-paneled aesthetic of traditional firms in favor of a **Modern & Agile** philosophy. The brand personality is "Elite Technical Partner"—blending the rigorous precision of law with the rapid deployment cycles of a tech company.

The visual direction utilizes a hybrid of **Minimalism** and **Glassmorphism**. By leaning into heavy white space and a restricted palette, the system communicates clarity and lack of friction. The "Bento-box" modularity reflects the organized complexity of legal term sheets and cap tables, presenting information in bite-sized, digestible, and high-energy modules.

## Colors

The palette is centered on **Electric Blue**, a high-vibrancy primary color that signals energy and digital fluency. This is offset by **Slate Grey** for typography to provide deep contrast without the harshness of pure black, maintaining a sophisticated "tech-corporate" feel.

- **Primary (Electric Blue):** Used for primary actions, active states, and brand-critical highlights.
- **Secondary (Slate Grey):** Used for secondary text, icons, and borders.
- **Tertiary (Deep Slate):** Reserved for high-level headings and dark-mode-style surface accents.
- **Neutral (White/Off-white):** The canvas. Use pure white for backgrounds to maintain a "clean-room" professional environment.

## Typography

This design system uses a dual-type approach to balance character with utility. **Space Grotesk** is the voice of the firm—it is used for headlines to provide a geometric, slightly technical edge that resonates with engineering-minded founders. **Inter** is the functional workhorse, utilized for all body copy, data tables, and legal fine print to ensure maximum readability across all screen densities.

Use `label-caps` for eyebrows and small metadata to reinforce the geometric grid. Maintain tight tracking on headlines and generous line-height on body text to facilitate the reading of dense legal documentation.

## Layout & Spacing

The layout is governed by a **Fixed Grid** philosophy optimized for the "Bento-box" pattern. The system utilizes a 12-column grid for desktop with 20px gutters. Elements should be grouped into cards of varying column spans (e.g., 3-column, 6-column, and 9-column blocks) to create a modular dashboard feel even on static content pages.

Horizontal and vertical rhythm follows a strict 4px/8px baseline. Large internal padding (minimum 24px) within bento containers is required to maintain the "Minimalist" brand value.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and **Low-contrast outlines** rather than heavy shadows. This design system treats the UI as a series of translucent glass layers floating over a clean white void.

- **Surface Tiers:** Use a 1px solid border (#E2E8F0) for all containers. 
- **Backdrop Blur:** For modals and floating navigation, apply a 12px to 20px backdrop blur with a white fill at 70% opacity.
- **Shadows:** Use a single "Ambient Blue" shadow for primary call-to-actions: `0px 10px 30px rgba(0, 82, 255, 0.1)`. This gives a subtle lift without feeling heavy or dated.

## Shapes

The shape language is **Rounded**, using a 0.5rem (8px) base radius. This softens the technical nature of the typography and the rigidity of the bento-grid, making the firm feel approachable. 

- **Cards:** Use `rounded-lg` (16px) to define distinct modules.
- **Buttons/Inputs:** Use the base 8px radius.
- **Decorative Elements:** Occasional use of "Pill-shaped" tags for status indicators (e.g., "Active," "Pending") is encouraged to provide visual variety against the rectangular grid.

## Components

### Buttons
Primary buttons use the **Electric Blue** fill with white text. Hover states should transition to a slightly darker shade with a subtle scale-up effect (1.02x). Secondary buttons use a transparent background with a 1px Slate Grey border.

### Bento Cards
The core container of the system. Every card must have a 1px border and an 8px or 16px corner radius. Headlines within cards should be `h2` or smaller. Use white backgrounds for content cards and very light grey (#F8FAFC) for "background" or "inactive" modules.

### Inputs & Forms
Input fields should be minimalist: 1px borders that turn Electric Blue on focus. Use **Inter** for input text. Labels should use `label-caps` for a professional, structured appearance.

### Chips & Badges
Small, pill-shaped components used for categorization (e.g., "Series A", "Fintech"). These should use low-saturation background tints of the primary color to avoid distracting from the main action.

### Glass Navigation
The top navigation bar should always utilize the glassmorphism effect—blurring the content underneath as the user scrolls, maintaining a sense of depth and modern tech aesthetics.