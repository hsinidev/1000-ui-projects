---
name: CyberLitigate
colors:
  surface: '#121317'
  surface-dim: '#121317'
  surface-bright: '#38393d'
  surface-container-lowest: '#0d0e12'
  surface-container-low: '#1a1b1f'
  surface-container: '#1e1f23'
  surface-container-high: '#292a2e'
  surface-container-highest: '#343539'
  on-surface: '#e3e2e7'
  on-surface-variant: '#c7c6ca'
  inverse-surface: '#e3e2e7'
  inverse-on-surface: '#2f3034'
  outline: '#919094'
  outline-variant: '#46464a'
  surface-tint: '#c8c6c7'
  primary: '#c8c6c7'
  on-primary: '#313031'
  primary-container: '#0a0a0b'
  on-primary-container: '#7a797a'
  inverse-primary: '#5f5e5f'
  secondary: '#c8c6c8'
  on-secondary: '#303032'
  secondary-container: '#474649'
  on-secondary-container: '#b7b4b7'
  tertiary: '#00dbe9'
  on-tertiary: '#00363a'
  tertiary-container: '#000c0e'
  on-tertiary-container: '#00868f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e3'
  primary-fixed-dim: '#c8c6c7'
  on-primary-fixed: '#1c1b1c'
  on-primary-fixed-variant: '#474647'
  secondary-fixed: '#e4e2e4'
  secondary-fixed-dim: '#c8c6c8'
  on-secondary-fixed: '#1b1b1d'
  on-secondary-fixed-variant: '#474649'
  tertiary-fixed: '#7df4ff'
  tertiary-fixed-dim: '#00dbe9'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#121317'
  on-background: '#e3e2e7'
  surface-variant: '#343539'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  code-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  unit: 4px
  gutter: 24px
  margin: 48px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is built to project an image of digital invulnerability and legal precision. The brand personality is authoritative, impenetrable, and technologically superior, catering to a clientele that requires high-stakes defense in the digital realm.

The visual style is a fusion of **Minimalism** and **Glassmorphism**, executed within a strict high-contrast dark environment. It utilizes thin, luminous boundaries and sharp geometric forms to evoke the feeling of a high-end security terminal. Every interface element should feel like a piece of critical data protected behind a layer of reinforced glass. The aesthetic prioritizes "Defensive Design"—where layouts feel structured, orderly, and fortified.

## Colors

The palette is anchored in deep, "Matte Black" depths to ensure maximum focus on content. "Graphite" is employed for elevated surfaces and containers, providing a subtle tonal shift that maintains a monochromatic foundation. 

"Neon Cyan" is the surgical instrument of this design system; it is used sparingly for critical actions, active states, and data visualizations. It should often be accompanied by a soft outer glow (0-4px) to simulate a light-emitting interface. High-contrast white is reserved for primary text to ensure legibility against the dark backgrounds.

## Typography

This design system utilizes a dual-font strategy to balance corporate professionalism with technical precision. **Space Grotesk** is used for headlines, labels, and data points; its geometric construction provides a "monospaced-adjacent" feel that suggests data-heavy accuracy.

**Inter** is the workhorse for body copy and long-form legal text. It is chosen for its exceptional readability in dark mode and its neutral, systematic character. All labels should be set in Space Grotesk with increased letter spacing to enhance the technical aesthetic.

## Layout & Spacing

The layout follows a **Fixed Grid** model to ensure a sense of structural rigidity and "defensive" alignment. A 12-column grid is used for desktop layouts, with generous 48px margins to provide visual breathing room and emphasize the high-end nature of the brand.

Content containers should adhere strictly to a 4px baseline grid. Spacing is used to create clear groupings of data; tighter spacing (stack-sm) for related meta-data and wider spacing (stack-lg) for section breaks. Grid lines may be visually rendered as faint, 1px graphite lines in the background to reinforce the technical theme.

## Elevation & Depth

Depth is communicated through **Glassmorphism** and **Tonal Layering** rather than traditional drop shadows. Surfaces are stacked to create hierarchy:
1.  **Base Layer:** Matte Black (#0A0A0B).
2.  **Surface Layer:** Semi-transparent Graphite with a backdrop blur (20px) and a subtle 1px border (#FFFFFF 10% opacity).
3.  **Active/Hover Layer:** Surfaces may gain a thin, luminous Neon Cyan top-border or a subtle inner glow.

Shadows, when used, are strictly ambient and neutral, meant only to separate overlapping glass cards. The "Data-Grid Pattern"—a series of faint dots or lines—should sit just above the base layer to provide a sense of architectural depth.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. Every UI element—from buttons and input fields to cards and modal windows—must feature 90-degree corners. This evokes a sense of digital precision, cutting-edge technology, and uncompromising law. 

Avoid circles where possible; use octagons or diamond shapes for iconography or avatars to maintain the geometric theme. Thin lines (1px) are the primary decorative element, used to "frame" content and lead the eye across the terminal-like interface.

## Components

### Buttons
Primary buttons are solid Graphite with a Neon Cyan 1px border. On hover, the border glow intensifies and text may transition to Neon Cyan. Secondary buttons are ghost-style with subtle 1px white borders. All buttons are rectangular with no corner radius.

### Cards
Cards use the glassmorphic style: semi-transparent background with a heavy backdrop blur. They must feature a 1px border on all sides, or a "header accent" which is a 2px Neon Cyan line at the very top.

### Input Fields
Inputs are minimalist, consisting of a bottom-border only or a fully encased 1px Graphite box. The cursor and focus state must utilize Neon Cyan. Placeholder text should be set in a dimmed Graphite to maintain high contrast only for active data.

### Data Chips & Tags
Small, rectangular tags used for case status or privacy levels. These should use Space Grotesk for the font and may include a tiny "status LED" dot (Neon Cyan for active, Red for alert, Grey for inactive).

### Navigation
The sidebar or top-nav should be integrated into the grid, using thin vertical/horizontal lines to separate sections. Active links are indicated by a Neon Cyan vertical bar and a slight glow on the text.

### Technical Elements
Include "Scanning" animations, "Data-Stream" progress bars (using a segmented block style), and "Encrypted" text transitions to reinforce the cyber-law narrative.