---
name: Quantum-Phone OS
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cfc2d9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#988ca2'
  outline-variant: '#4d4356'
  surface-tint: '#dab9ff'
  primary: '#dab9ff'
  on-primary: '#470083'
  primary-container: '#8f00ff'
  on-primary-container: '#efddff'
  inverse-primary: '#8600ef'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#646565'
  on-tertiary-container: '#e3e3e3'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#efdbff'
  primary-fixed-dim: '#dab9ff'
  on-primary-fixed: '#2b0053'
  on-primary-fixed-variant: '#6500b8'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Sora
    fontSize: 72px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Sora
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Sora
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
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
  unit: 8px
  container-margin: 24px
  gutter: 16px
  section-gap: 48px
  fluid-multiplier: '1.5'
---

## Brand & Style

This design system embodies the intersection of physical precision and digital fluidity. It is crafted for an elite audience that values technological mystery and high-performance luxury. The aesthetic is defined by **Ultra-Modern Futurism**, blending deep, infinite blacks with high-energy "Electric Violet" accents.

The visual language leverages **Glassmorphism** to create a sense of depth and lightness, making the UI feel like it is floating within the device's hardware. Motion is not just an afterthought but a core pillar; "Liquid" transitions ensure that every interaction feels organic, viscous, and responsive. The overall experience should evoke a feeling of "controlled power"—sophisticated, silent, and effortlessly fast.

## Colors

The palette is anchored in **Midnight Black (#000000)** to maximize the OLED display's capabilities and provide a canvas for high-contrast elements. **Electric Violet (#8F00FF)** serves as the primary action color, used sparingly for critical focal points and interactive states.

**Glass Materials** are used to define the spatial hierarchy. Surfaces are never fully opaque; they utilize backdrop blurs to allow background content and 3D elements to bleed through subtly. Neutral grays are avoided in favor of varying transparencies and deep, desaturated purples to maintain the "liquid night" atmosphere. High-energy gradients are permitted only when transitioning between Violet and deep void-blacks.

## Typography

This design system utilizes a tiered typographic approach to reinforce its futuristic character. **Sora** is the primary display face, chosen for its geometric precision and tech-forward curves. It should be used for large headlines with tight tracking to create a "locked-in" editorial look.

**Hanken Grotesk** handles functional UI elements and body text, providing a sharp, contemporary readability that doesn't distract from the visual depth of the system. For technical metadata, battery percentages, and system status, **JetBrains Mono** is used in all-caps to provide a laboratory-precise, engineered feel. 

Hierarchy is established through weight and scale rather than color. Important headers should be exceptionally bold, while secondary information uses lower opacity white rather than gray.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with significant negative space. To maintain a premium feel, margins are wider than standard smartphone interfaces (24px minimum), pushing content toward the center to create a "floating" effect.

Spacing is based on an 8px base unit. However, the system encourages "Airy" layouts—vertical gaps between sections should feel expansive (section-gap). On desktop and tablet views, the grid expands to 12 columns, while mobile uses a 4-column system. Elements often "break the grid" with 3D assets or liquid-simulated blobs that overflow the container edges, creating a dynamic, non-static experience.

## Elevation & Depth

Depth is conveyed through **Optical Stacked Layers** and refraction rather than traditional drop shadows. This design system uses three primary methods for elevation:

1.  **Backdrop Refraction:** Elements closer to the user have a stronger backdrop blur (up to 40px) and a lighter translucent background.
2.  **Electric Glows:** Interactive or "active" elements emit an inner glow of Electric Violet, simulating a light source behind the glass.
3.  **Z-Axis Scaling:** Upon interaction, components don't just change color; they subtly scale toward the user, increasing their translucency to simulate physical distance from the "Midnight Black" background.
4.  **Outer Strokes:** Use 1px "light-leak" borders on the top and left sides of glass elements to simulate a subtle physical edge.

## Shapes

The shape language is defined by **Continuous Curvature**. Standard containers use a 1rem (16px) radius, but the system leans heavily into "Squircle" geometry to mimic hardware silhouettes. 

Buttons and high-level navigation items use pill shapes to contrast against the more structured rectangular glass panels. All shapes must feel "molded" rather than "cut"—meaning corners are smooth and transitions between straight edges and curves are mathematically eased to prevent visual tension.

## Components

### Interactive Elements
*   **Buttons:** Primary buttons are solid Electric Violet with a slight liquid-gradient shimmer. Secondary buttons are "Glass Link" style: no fill, 1px translucent border, and a heavy backdrop blur.
*   **Inputs:** Minimalist bottom-border only in the default state. Upon focus, the field expands into a glass container with a violet inner glow.

### Data & Content
*   **Glass Cards:** The workhorse of the UI. Must have `backdrop-filter: blur(20px)` and a subtle 1px border. No hard shadows; use a very soft, large-radius violet ambient glow for high-priority cards.
*   **Chips:** Pill-shaped, using JetBrains Mono for text. Used for system status or technical tags.

### Motion & Feedback
*   **Liquid Transitions:** When navigating, panels should appear to "flow" from the touch point, using elastic easing functions.
*   **3D Assets:** Hero sections should feature high-fidelity, matte-textured 3D models that rotate slightly based on the device's gyroscope.

### Navigation
*   **The Void Dock:** A floating pill-shaped navigation bar at the bottom, using maximum glass refraction. Icons should use thin 1.5pt strokes that "fill" with Electric Violet when active.