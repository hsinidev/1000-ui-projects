---
name: Dark Tech UI
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#303031'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c9c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#faf6fc'
  on-tertiary: '#303034'
  tertiary-container: '#dddae0'
  on-tertiary-container: '#605f64'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c9c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e4e1e7'
  tertiary-fixed-dim: '#c8c5cb'
  on-tertiary-fixed: '#1b1b1f'
  on-tertiary-fixed-variant: '#47464b'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.03em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
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
  margin: 40px
  container-max: 1440px
---

## Brand & Style

This design system is engineered to project an aura of high-performance intelligence, absolute security, and futuristic innovation. Targeted at enterprise IT decision-makers, the aesthetic balances the raw power of "Dark Tech" with the sophisticated clarity of modern B2B software. 

The style utilizes a blend of **Minimalism** and **Glassmorphism**. It relies on high-contrast interactions against deep, void-like backgrounds to focus the user's attention on critical data and technical precision. The emotional response is one of calm control in a high-stakes digital environment—stable, cutting-edge, and elite.

## Colors

The palette is anchored in an "Obsidian" depth, using `#050505` for base layers and `#0a0a0a` for primary containers. The signature "Electric Cyan" (`#00f2ff`) is used sparingly but impactfully to denote interactivity, progress, and critical system status.

Secondary surfaces use a "Charcoal" gradient to establish hierarchy. Data visualizations should leverage the primary cyan alongside a supporting palette of cool grays and deep blues to maintain a monochromatic technical feel, avoiding warmer tones that would disrupt the cold, futuristic atmosphere.

## Typography

Typography in this design system emphasizes structural geometry and legibility. **Space Grotesk** is the primary driver for headlines and labels, providing a technical, monospaced-adjacent feel that suggests precision engineering. All headers should utilize generous letter spacing to enhance the "sleek" futuristic aesthetic.

**Inter** handles the heavy lifting for body copy and data tables. Its neutral, utilitarian character ensures that complex IT documentation and system logs remain highly readable. Use uppercase styling for labels and small navigational elements to reinforce the technical dashboard feel.

## Layout & Spacing

The layout philosophy follows a rigid 12-column fixed grid for main content areas, ensuring a "designed by machine" level of alignment and predictability. A strictly enforced 8px base unit governs all padding and margins.

Components should favor generous internal whitespace to prevent the dark interface from feeling cramped or claustrophobic. Use wide margins (40px+) on container edges to allow the glassmorphic edges to "breathe" against the obsidian background.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional shadows. Layers are defined by their backdrop blur intensity and the opacity of their frosted surface.

1.  **Base Level:** Obsidian black (`#050505`).
2.  **Mid Level (Cards/Containers):** Semi-transparent charcoal (`rgba(20, 20, 20, 0.7)`) with a 12px to 20px backdrop-blur.
3.  **High Level (Modals/Popovers):** Higher transparency with a more intense blur and a 1px solid white border at 10% opacity.

Interactive elements should feature a subtle "inner glow" using the primary cyan color to simulate light emitting from within the technical interface.

## Shapes

The shape language is "Soft-Technical." By using a consistent `0.25rem` (4px) corner radius, the UI maintains a sharp, precise look without the aggressive nature of perfectly square corners. 

Buttons and input fields should strictly follow this radius. Only decorative elements or large "hero" glass containers should ever use the `rounded-lg` (8px) variant. This restraint ensures the design feels like a piece of high-end hardware.

## Components

### Buttons
Primary buttons are solid `#00f2ff` with black text. On hover, they trigger a cyan outer glow (`drop-shadow`). Secondary buttons are "ghost" style: 1px borders with cyan text and no fill.

### Input Fields
Inputs feature a dark, semi-transparent background with a subtle bottom-only border or a very thin 1px perimeter. Upon focus, the border and label should glow in the primary cyan.

### Glass Cards
The core container for the design system. These must have a `1px` border using a white-to-transparent linear gradient (top-left to bottom-right) at low opacity (10-15%) to catch the "light" and define the edges of the frosted glass.

### Data Visualizations
Charts should utilize thin stroke widths (1px - 1.5px). Data points should be represented by small, glowing cyan pips. Use gradient fills under line charts that fade from 20% cyan to 0% transparency.

### Technical Accents
Incorporate "Status Pips" (small glowing dots) to indicate system health. Use ultra-thin divider lines (0.5px) to separate content sections without adding visual bulk.