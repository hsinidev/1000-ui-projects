---
name: Aura-NFT Cyber-Chic
colors:
  surface: '#0d1515'
  surface-dim: '#0d1515'
  surface-bright: '#333b3b'
  surface-container-lowest: '#080f10'
  surface-container-low: '#151d1e'
  surface-container: '#192122'
  surface-container-high: '#232b2c'
  surface-container-highest: '#2e3637'
  on-surface: '#dce4e4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dce4e4'
  inverse-on-surface: '#2a3232'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c1c6da'
  on-secondary: '#2b3040'
  secondary-container: '#414657'
  on-secondary-container: '#b0b4c9'
  tertiary: '#fff6e4'
  on-tertiary: '#3b2f00'
  tertiary-container: '#fed83a'
  on-tertiary-container: '#725e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#dee2f7'
  secondary-fixed-dim: '#c1c6da'
  on-secondary-fixed: '#161b2a'
  on-secondary-fixed-variant: '#414657'
  tertiary-fixed: '#ffe173'
  tertiary-fixed-dim: '#e8c423'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#0d1515'
  on-background: '#dce4e4'
  surface-variant: '#2e3637'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
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
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-viz:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 48px
  container-max: 1440px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The design system embodies a "Cyber-Chic" aesthetic, merging high-fashion curation with futuristic digital landscapes. It targets a sophisticated audience of generative art collectors and tech-forward creators. The emotional response is one of exclusivity, digital permanence, and high-tech precision.

The style is defined by **Glassmorphism** and **Luminescence**. UI elements are treated as physical panes of high-clarity synthetic glass, floating within a deep, infinite void. Depth is created through optical refraction, backdrop blurs, and localized neon light sources that cast atmospheric glows on surrounding surfaces. The result is a premium, immersive environment that frames generative art as a luxury commodity.

## Colors
This design system utilizes a deep-space dark mode to allow generative art colors to pop. 

- **Primary Background:** Midnight Blue (#0A0E1A) provides the "void" foundation.
- **Primary Accent:** Electric Cyan (#00F2FF) is used exclusively for interactive elements, data highlights, and light-emitting sources.
- **Secondary Surfaces:** Deep charcoal tones are used to create structural hierarchy, providing a matte contrast to the glass elements.
- **Functional Colors:** Success states utilize a vivid emerald neon, while errors use a high-saturation magenta, maintaining the cybernetic palette.

## Typography
The typography strategy balances technical precision with modern editorial flair. 

**Space Grotesk** is the voice of the system, used for large headlines to emphasize the futuristic, geometric nature of the brand. **Inter** provides high legibility for secondary content and long-form descriptions. **JetBrains Mono** (monospaced) is used for technical metadata, NFT IDs, and "hacker-chic" labels, reinforcing the generative/code-based nature of the artwork. All text should maintain high contrast against the dark backgrounds, primarily using pure white or very light cyan tints.

## Layout & Spacing
The layout follows a **Fixed Grid** model for desktop to maintain a curated, gallery-like feel. 

A 12-column grid is used with wide 24px gutters to allow the glass components "room to breathe." Margins are generous (48px+) to create a premium sense of whitespace. Layouts should be asymmetrical where possible to mimic modern art galleries, with large hero sections that utilize the full viewport height. Alignment should be crisp and mathematical, contrasting with the soft glows of the components.

## Elevation & Depth
Depth is achieved through a multi-layered glass metaphor rather than traditional drop shadows.

1.  **Base Layer:** The Midnight Blue void.
2.  **Surface Layer:** Deep Charcoal with 0% blur, used for sidebars and background panels.
3.  **Glass Layer:** 60% opacity backgrounds with a 20px - 40px backdrop blur. These layers feature a 1px inner border (white at 12% opacity) to simulate the edge of a glass pane.
4.  **Floating Glow:** High-priority elements (like active NFT cards or primary buttons) use an `outer-glow` effect. This is a Cyan-tinted shadow with a 20px spread and very low opacity (15-20%), creating the illusion of a light-emitting component.

## Shapes
The shape language is "Soft-Tech." While the overall vibe is sharp and precise, a subtle 4px (0.25rem) corner radius is applied to all glass panes and buttons to prevent the UI from feeling overly aggressive or dated. Larger containers like gallery cards may use 8px (0.5rem) to feel more substantial. Interactive indicators (radio buttons, active states) use 0px sharp corners to maintain a "technical instrument" aesthetic.

## Components

### Buttons
- **Primary:** Electric Cyan background, black text. No shadow, but a 15px Cyan outer glow on hover.
- **Secondary (Glass):** Transparent background with 20px blur, 1px white border (20% opacity). Cyan text.
- **Ghost:** No background, white text, Cyan underline on hover.

### Cards (The "Gallery" Pane)
The central component. Features a 40px backdrop blur and a thin light-cyan top-border to catch "overhead light." The content within the card uses monospaced labels for price and mint numbers. Images within cards should have no rounded corners to respect the artwork's integrity.

### Input Fields
Darker charcoal backgrounds with "inset" shadows. The focus state triggers a full 1px Electric Cyan border and a subtle cyan glow.

### Technical Data Visualizations
Charts and graphs utilize thin 1px lines in Electric Cyan. Data points are small glowing circles. No fills are used in charts, only stroked lines to maintain the "holographic" aesthetic.

### Navigation
Top-bar navigation is a fixed glass pane with a heavy blur (60px). Active links are indicated by a cyan "glitch" line or a simple high-contrast glow beneath the text.