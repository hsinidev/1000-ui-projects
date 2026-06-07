---
name: Obsidian Nexus
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1d'
  surface-container: '#1e2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333536'
  on-surface: '#e2e2e3'
  on-surface-variant: '#bacac7'
  inverse-surface: '#e2e2e3'
  inverse-on-surface: '#2e3132'
  outline: '#859491'
  outline-variant: '#3c4948'
  surface-tint: '#3cdcd1'
  primary: '#ffffff'
  on-primary: '#003734'
  primary-container: '#62f9ee'
  on-primary-container: '#00716b'
  inverse-primary: '#006a64'
  secondary: '#7bd6d1'
  on-secondary: '#003735'
  secondary-container: '#007774'
  on-secondary-container: '#a1fcf7'
  tertiary: '#ffffff'
  on-tertiary: '#28313c'
  tertiary-container: '#dae3f2'
  on-tertiary-container: '#5c6572'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#62f9ee'
  primary-fixed-dim: '#3cdcd1'
  on-primary-fixed: '#00201e'
  on-primary-fixed-variant: '#00504b'
  secondary-fixed: '#98f2ed'
  secondary-fixed-dim: '#7bd6d1'
  on-secondary-fixed: '#00201f'
  on-secondary-fixed-variant: '#00504d'
  tertiary-fixed: '#dae3f2'
  tertiary-fixed-dim: '#bec7d6'
  on-tertiary-fixed: '#131c27'
  on-tertiary-fixed-variant: '#3e4753'
  background: '#111415'
  on-background: '#e2e2e3'
  surface-variant: '#333536'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
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
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  grid-gutter: 24px
  grid-margin: 40px
---

## Brand & Style

This design system targets high-level IT decision-makers and enterprise technical architects. The brand personality is authoritative, precise, and forward-looking, evoking the feeling of a mission-control interface or a secure digital vault.

The visual style is defined by **Glassmorphism** and **High-Contrast Neon** accents. It relies on deep layers of transparency to suggest depth and complexity, while glowing elements represent live data and active systems. The emotional response is one of absolute technical reliability and futuristic sophistication.

## Colors

The palette is anchored in a dark-mode-only architecture. 
- **Base Surfaces:** Use `#0B0C10` for the deepest background layers and `#1F2833` for secondary containers.
- **Accents:** `#66FCF1` (Electric Cyan) is reserved for primary calls to action and critical status indicators. `#45A29E` serves as a muted variant for hover states and secondary active elements.
- **Typography:** `#C5C6C7` provides high-readability contrast against the obsidian backgrounds without the harshness of pure white.

## Typography

The typographic system utilizes **Space Grotesk** for headlines to achieve a technical, geometric edge reminiscent of sci-fi interfaces. For long-form data and body text, **Inter** provides the necessary utilitarian clarity required for B2B IT documentation. 

Headlines should utilize tight tracking and aggressive line heights. Label styles must be used for metadata and system statuses, often paired with all-caps styling to reinforce the "instrument panel" aesthetic.

## Layout & Spacing

This design system uses a **fixed grid** approach for desktop dashboards to maintain structural integrity across complex data visualizations. A 12-column grid is standard, with 24px gutters.

The spacing rhythm follows a strict 4px base unit. Layouts should emphasize "Information Density"—minimize excessive whitespace in favor of logical grouping via thin, high-contrast borders and grid overlays. Subtle background patterns (0.05 opacity) of a 20px dot or square grid should be visible in the base background layer.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and luminosity rather than traditional shadows. 
- **Level 1:** Base background (#0B0C10).
- **Level 2:** Floating panels with `backdrop-filter: blur(12px)` and a background of `rgba(31, 40, 51, 0.7)`.
- **Level 3:** Active overlays or modals with a 1px solid border of `#45A29E` at 30% opacity.

Instead of shadows, use "Glows." Elements of importance should emit a soft outer pulse using the primary accent color with a high blur radius and low opacity.

## Shapes

The shape language is **Sharp**. To maintain a high-tech, engineered feel, all UI elements—including buttons, cards, and input fields—utilize 0px border-radii. 

For decorative elements, use 45-degree chamfered corners (clipped corners) to reinforce the futuristic aeronautic aesthetic. Lines must be kept thin (1px) to suggest precision.

## Components

**Buttons:** Primary buttons are solid `#66FCF1` with black text. Secondary buttons are "Ghost" style with a 1px neon border and a subtle `box-shadow: 0 0 10px` glow on hover.

**Cards:** Must feature a frosted glass effect. Borders should be 1px wide, using a linear gradient (top-left to bottom-right) from `#45A29E` to transparent.

**Inputs:** Field backgrounds should be darker than the container surface. Focus states must trigger a full-border glow and a subtle increase in the backdrop-blur intensity.

**Data Visualization:** Use high-contrast lines. Area charts should use semi-transparent neon fills with a vertical gradient fading to zero.

**System HUD:** Include specialized "Status Chips" that use a small glowing dot icon next to technical labels to indicate system health (e.g., Pulse Green, Warning Amber, Critical Cyan).