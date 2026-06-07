---
name: Cinematic Velocity
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '900'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  display-md:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.03em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin-mobile: 16px
  margin-landscape: 48px
---

## Brand & Style

This design system is engineered for a high-octane, premium sports streaming experience. The brand personality is aggressive, precise, and cinematic, mirroring the intensity of a live 4K broadcast. It targets a passionate audience that demands speed and visual fidelity.

The UI style utilizes **Glassmorphism** to create depth and hierarchy without sacrificing the immersive quality of full-bleed sports imagery. Translucent layers with high-contrast borders evoke a sophisticated "Command Center" feel. The experience is optimized for high-energy interaction, using motion and vibrant accents to signal urgency and live action.

## Colors

The palette is strictly high-contrast to ensure maximum readability during fast-paced viewing. 

- **Primary (Neon Red):** Reserved for "LIVE" indicators, critical calls to action, and active progress bars. It represents the energy of the stadium.
- **Secondary (Crisp White):** Used for primary typography and high-frequency iconography to ensure a clean, sharp look against dark backgrounds.
- **Background (Deep Black):** The foundation of the interface, providing a true cinematic canvas that makes 4K video content pop.
- **Overlays (Translucent Greys):** Used for glass surfaces, providing structure while maintaining a visual connection to the content behind them.

## Typography

This design system uses a dual-font strategy. **Inter** is utilized for headlines and labels, leveraging its tight tracking and bold weights to mimic professional broadcast graphics. All labels should be set in uppercase to reinforce the authoritative, athletic tone. 

**Lexend** is the choice for body text and player statistics. Its specific design for readability ensures that even dense sporting data remains clear on mobile screens and at a distance in landscape orientation. Headlines should prioritize "Extra Bold" or "Black" weights for a commanding presence.

## Layout & Spacing

The layout follows a **Fluid Grid** model with an 8px rhythmic scale. For mobile-first delivery, the system prioritizes vertical scrolling for discovery and a seamless transition to a 12-column grid in landscape orientation for the viewing experience.

In landscape mode, "safe areas" are strictly enforced to prevent UI overlap with critical broadcast graphics (scoreboards, tickers). Gutters are kept tight at 16px to maximize the "edge-to-edge" cinematic feel, while margins expand significantly in landscape to center the focus on the primary stream.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism** and layering rather than traditional drop shadows.

1.  **Base Layer:** Pure #000000 or full-bleed video content.
2.  **Surface Layer:** 20% opacity white tint with a 12px background blur. Used for persistent navigation and content cards.
3.  **Accent Layer:** High-contrast 1px solid borders (#FFFFFF at 15% opacity) define the edges of surfaces, ensuring they remain visible against varying video backgrounds.
4.  **Active Layer:** Elements currently in focus or "Live" use a 1px Neon Red (#FF0000) border and a subtle red outer glow (5px blur) to simulate a light-emitting broadcast signal.

## Shapes

The design system utilizes **Rounded** corners to balance the aggressive typography with a premium, modern tech aesthetic. A standard radius of 0.5rem (8px) is applied to all primary cards and buttons. 

Larger containers like modal sheets or player overlays use a 1.5rem (24px) radius on top corners to create a "nested" feel within the viewport. Live indicators and small tags (like "4K" or "HDR") use a full pill shape to distinguish them from interactive buttons.

## Components

- **Buttons:** Primary buttons are solid Neon Red with white Inter-Bold uppercase text. Secondary buttons use a glass background with a 1px white border.
- **Live Indicators:** A pill-shaped component with a pulsing Neon Red dot and "LIVE" in white text.
- **Glass Cards:** Used for game previews. They feature a 20% transparent black fill and a 12px background blur to ensure text readability over hero imagery.
- **Score Tickers:** High-contrast, monochromatic strips that use condensed typography for rapid data consumption.
- **Player Controls:** Oversized, translucent icons with a 24px background blur to allow content to peek through while providing a large touch target for mobile users.
- **Stat Overlays:** High-energy data visualizations using Neon Red for positive metrics and White for neutral data, framed in high-contrast glass panels.