---
name: Executive Stealth
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
  on-surface-variant: '#cfc5b8'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3031'
  outline: '#989084'
  outline-variant: '#4c463c'
  surface-tint: '#d9c49e'
  primary: '#f8e2ba'
  on-primary: '#3b2f14'
  primary-container: '#dbc6a0'
  on-primary-container: '#615234'
  inverse-primary: '#6c5c3d'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#e7e4e3'
  on-tertiary: '#313030'
  tertiary-container: '#cbc8c7'
  on-tertiary-container: '#555453'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f6e0b8'
  primary-fixed-dim: '#d9c49e'
  on-primary-fixed: '#251a03'
  on-primary-fixed-variant: '#534528'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  display:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
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
  container-max: 1440px
  gutter: 24px
  margin-edge: 64px
  section-gap: 120px
---

## Brand & Style
The design system embodies the "Executive Stealth" philosophy: a silent, powerful presence that prioritizes privacy, precision, and high-tier luxury. The brand personality is one of an elite concierge—confident, understated, and impeccably organized. The UI should evoke an emotional response of being "above the clouds," utilizing a dark, cinematic aesthetic that reduces cognitive load while emphasizing exclusivity.

This design system utilizes a fusion of **Minimalism** and **Glassmorphism**. By stripping away unnecessary decorative elements and focusing on material depth and transparency, the interface feels like a high-tech flight deck filtered through a luxury lounge lens. Generous whitespace is treated as a premium commodity, ensuring every piece of data is presented with significant breathing room.

## Colors
The palette is built on a foundation of deep, layered blacks to create a sense of infinite depth. 

- **Primary (Champagne Gold):** Used exclusively for high-priority actions, luxury accents, and active states. It should feel metallic and luminous, never flat.
- **Secondary (Deep Charcoal):** The main surface color for large UI containers, providing a softer contrast than pure black.
- **Tertiary (Matte Black):** Reserved for structural scaffolding, sidebars, and background foundations to anchor the layout.
- **Accents:** Use semi-transparent white (10-15% opacity) for glassmorphic borders and separator lines to maintain the "stealth" appearance without losing definition.

## Typography
The typography strategy contrasts the heritage of aviation with the modernization of fleet management. 

**Noto Serif** is utilized for headings to communicate authority, tradition, and bespoke service. It should be used sparingly for editorial moments and section titles. **Manrope** provides a clean, technical counterpoint for all functional UI elements, ensuring maximum legibility during rapid data scanning. Wide letter-spacing is applied to labels to enhance the sophisticated, "spaced-out" aesthetic.

## Layout & Spacing
The layout follows a **Fixed Grid** model centered within the viewport, emphasizing a controlled, editorial experience rather than a sprawling web app. A 12-column system is used for primary content, while margins are intentionally oversized (64px+) to frame the content like a luxury magazine.

Spacing follows a strict 8px rhythmic scale. However, the design system encourages "Visual Pauses"—purposeful gaps between sections (up to 120px) to prevent the user from feeling overwhelmed by technical fleet data.

## Elevation & Depth
Depth is created through **Glassmorphism** and tonal layering rather than traditional drop shadows. 

1.  **Base Layer:** Solid Matte Black (#0D0D0D).
2.  **Mid Layer (Containers):** Deep Charcoal (#1A1A1A) with a subtle 1px inner border of 10% white.
3.  **Top Layer (Overlays/Modals):** Translucent charcoal with a `backdrop-filter: blur(20px)`. This creates the "frosted cockpit" effect.
4.  **Interactive Depth:** When an element is hovered, it should not lift with a shadow; instead, its gold border-intensity should increase, or the background blur should become more opaque.

## Shapes
The shape language is "Architectural Soft." Corners are not sharp (which feels aggressive) nor overly round (which feels consumer-grade). 

A `0.25rem` (4px) base radius is applied to all standard components like input fields and buttons. This provides a precision-engineered feel reminiscent of luxury watchmaking or aerospace components. Larger cards may use `0.5rem` to distinguish them from smaller UI widgets.

## Components
- **Buttons:** Primary buttons use a solid Champagne Gold fill with black text. Secondary buttons are "Ghost" style with a thin 1px gold border and no fill.
- **Cards:** Glassmorphic backgrounds with a 1px top-down linear gradient border (white at 15% to white at 5%). 
- **Inputs:** Minimalist bottom-border-only design or very subtle charcoal fills. Focus states transition the bottom border to Champagne Gold.
- **Chips/Status:** Use a "Stealth Dot" system—small circular indicators in Gold (Active), Grey (Idle), or Muted Red (Alert) rather than large colorful labels.
- **Data Visualization:** Line charts should use thin gold strokes with a subtle glow (bloom) effect. Background grids in charts should be barely visible matte black.
- **Flight Trackers:** Custom map styles should be strictly "Dark Mode Blue/Grey" with Champagne Gold flight paths to maintain the executive aesthetic.