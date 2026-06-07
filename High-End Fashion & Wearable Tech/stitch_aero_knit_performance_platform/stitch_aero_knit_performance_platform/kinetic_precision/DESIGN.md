---
name: Kinetic Precision
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#c7c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#cac6c3'
  on-tertiary: '#32302f'
  tertiary-container: '#0b0a09'
  on-tertiary-container: '#7c7977'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c7c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e6e1df'
  tertiary-fixed-dim: '#cac6c3'
  on-tertiary-fixed: '#1d1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  data-point:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.01em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system embodies the intersection of elite human performance and advanced textile engineering. The aesthetic is defined as **Kinetic & Technical**, prioritizing a high-velocity user experience that feels both hyper-functional and premium. 

The visual style utilizes a "Liquid-Structured" approach: layouts are governed by a rigid technical grid, while interactive elements and data visualizations flow with organic, fluid motion. We leverage **Glassmorphism** to create a sense of depth and layered intelligence, suggesting that the interface is a heads-up display for the athlete's body. The emotional response should be one of focused intensity, precision, and futuristic empowerment.

## Colors

The palette is anchored in **Carbon Black**, providing a high-contrast foundation that eliminates distractions. **Neon Mint** is the exclusive catalyst for action, reserved for primary CTAs, performance peaks, and active states. **Silver** functions as the technical bridge, used for secondary information, borders, and structural details.

- **Primary (Carbon Black):** The void. Used for all main backgrounds to ensure the hardware and apparel imagery "pop."
- **Accent (Neon Mint):** High-visibility energy. Used sparingly to guide the eye to critical data points and mission-critical buttons.
- **Secondary (Silver):** The metallic structural element. Used for labels, icons, and non-interactive technical data.
- **Surface:** A slightly elevated grey-black used for cards and containers to create hierarchy against the deep background.

## Typography

Typography must feel engineered. We use **Space Grotesk** for headlines and data visualizations to provide a technical, geometric edge. **Inter** serves as the workhorse for body copy, ensuring maximum readability during high-activity scenarios. 

**JetBrains Mono** is introduced for labels and technical metadata, reinforcing the "smart" aspect of the brand. Headlines should utilize tight tracking and bold weights to convey strength, while labels should be generously tracked and all-caps for a navigational, instrumentation-inspired feel.

## Layout & Spacing

This design system utilizes a **12-column fluid grid** built on an 8px base unit. The layout is strictly structured but allows for "kinetic" overflows—imagery and background elements may break the grid to suggest movement.

A subtle 32px square grid pattern should be overlaid on the background (opacity 0.03) to serve as a visual anchor for the technical aesthetic. Gutters are kept wide (24px) to ensure breathing room between dense data sets, and margins are significant (32px+) to focus the user's attention on the center-stage content.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and tonal layering rather than traditional shadows. Surfaces do not "cast" light; they "refract" it.

1.  **Base Layer:** Solid Carbon Black.
2.  **Mid Layer (Containers):** Semi-transparent (40-60%) Carbon with a 20px background blur and a 1px Silver stroke at 12% opacity.
3.  **Top Layer (Overlays/Modals):** Lighter translucency with 40px background blur, creating a "frosted" technical look.

Interactive elements should use a "Glow-Depth" approach: instead of rising on the Z-axis, they emit a subtle Neon Mint outer glow when active or hovered, suggesting high energy.

## Shapes

The shape language is primarily **Soft (0.25rem)** to maintain a technical, "machined" appearance. While the content is "liquid," the containers must remain disciplined. 

- **Standard Elements:** 4px radius for a sharp, precise look.
- **Action Elements (Buttons):** 8px radius for better touch targets and visual distinction.
- **Data Containers:** 0px (sharp) corners on the inner side of a grouping to imply they are part of a larger mechanical unit.
- **Circular Elements:** Reserved exclusively for user avatars or specific performance rings (heart rate, progress).

## Components

### Buttons
- **Primary:** Solid Neon Mint background with Carbon Black text. No border. On hover, a slight "pulse" animation.
- **Secondary:** Transparent background with a 1px Silver stroke and Silver text.
- **Ghost:** Transparent with Silver text; becomes Neon Mint on hover.

### Cards & Glass Containers
Cards should appear as "modules." Use the mid-layer glassmorphism settings (20px blur, 1px Silver stroke). Headers within cards should be separated by a 1px Silver line at 5% opacity.

### Data Visualizations
Charts must feel alive. Use Neon Mint for the primary data line and Silver for the grid/axis. Avoid solid fills; use gradients that bleed from Neon Mint into transparency (the "liquid" effect).

### Inputs
Text fields are "Ghost" style: a single 1px Silver bottom border. Upon focus, the border transitions to Neon Mint and a very subtle vertical glow expands upward.

### Chips & Tags
Small, 4px rounded rectangles. Background is 10% Silver (semi-transparent) with JetBrains Mono labels. When a tag represents a "Live" state, it should include a small pulsing Neon Mint dot.