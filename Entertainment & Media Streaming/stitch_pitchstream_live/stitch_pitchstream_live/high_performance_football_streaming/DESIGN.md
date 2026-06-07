---
name: High-Performance Football Streaming
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#909096'
  outline-variant: '#46464c'
  surface-tint: '#c3c6d7'
  primary: '#c3c6d7'
  on-primary: '#2c303d'
  primary-container: '#0a0e1a'
  on-primary-container: '#777b8a'
  inverse-primary: '#5a5e6d'
  secondary: '#d7ffc5'
  on-secondary: '#053900'
  secondary-container: '#2ff801'
  on-secondary-container: '#0f6d00'
  tertiary: '#bfc6df'
  on-tertiary: '#293044'
  tertiary-container: '#070e20'
  on-tertiary-container: '#747b92'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2f3'
  primary-fixed-dim: '#c3c6d7'
  on-primary-fixed: '#171b28'
  on-primary-fixed-variant: '#434654'
  secondary-fixed: '#79ff5b'
  secondary-fixed-dim: '#2ae500'
  on-secondary-fixed: '#022100'
  on-secondary-fixed-variant: '#095300'
  tertiary-fixed: '#dbe2fc'
  tertiary-fixed-dim: '#bfc6df'
  on-tertiary-fixed: '#141b2e'
  on-tertiary-fixed-variant: '#3f465b'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
  stats-number:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 20px
  margin: 32px
---

## Brand & Style

This design system is engineered to capture the electrifying atmosphere of a night match under stadium floodlights. The brand personality is aggressive, elite, and instantaneous, catering to die-hard football fans who demand zero latency and high-fidelity visuals. 

The aesthetic leverages a **High-Contrast Cinematic** style. By pairing a void-like deep navy with a piercing radioactive green, the UI creates a sense of depth and urgency. **Glassmorphism** is utilized strategically to ensure that interface elements feel like heads-up displays (HUDs) floating over live action, maintaining a continuous connection to the pitch without obstructing the view. The overall emotional response is one of adrenaline and technical precision.

## Colors

The palette is anchored by **Deep Navy (#0A0E1A)**, which serves as the canvas for all live content, providing maximum contrast for video streams. **Neon Pitch-Green (#39FF14)** is the high-energy pulse of the system, reserved exclusively for "Live" indicators, primary action buttons, and active state highlights to draw the eye instantly.

A secondary navy tier (#1B2235) is used for surface elevations and card backgrounds to distinguish them from the base layout. Functional neutrals range from pure white for maximum legibility to muted slate tones for metadata and secondary information, ensuring the hierarchy remains clear during fast-paced gameplay.

## Typography

Typography in this design system prioritizes impact and readability under pressure. **Space Grotesk** is used for headlines and score displays; its geometric, technical structure evokes a high-performance, futuristic feel. For body copy and player statistics, **Lexend** provides exceptional clarity and an athletic, motivating tone.

Headlines should utilize tight letter-spacing to feel dense and powerful. Numerical data—especially scores and clock timers—must be rendered in bold weights to ensure they remain legible even when scaled down on mobile devices or in peripheral vision during a broadcast.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for edge-to-edge cinematic immersion. On desktop, a 12-column grid is used with generous gutters to separate data-heavy sidebars from the primary stream. On mobile, the system collapses into a single-column view where the video remains pinned to the top (aspect ratio 16:9).

Spacing is built on a 4px baseline, but utilizes larger jumps (16px to 24px) for major component grouping to maintain "sharp, clean lines." High-energy content areas should utilize condensed vertical spacing to keep more information above the fold, while premium marketing sections should use expanded padding to feel more editorial.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and tonal layering rather than traditional drop shadows. This ensures the interface feels integrated with the live video feed.

1.  **The Pitch (Level 0):** The primary background or live stream video.
2.  **Surface Containers (Level 1):** Solid Deep Navy (#0A0E1A) with subtle 1px borders in a lighter navy shade.
3.  **Glass Overlays (Level 2):** Semi-transparent surfaces (20% opacity) with a 20px backdrop blur and a 1px "ice" border (white at 10% opacity). This is used for scoreboards, player stats, and menu overlays.
4.  **Active Focus (Level 3):** Elements that require immediate attention use a subtle outer glow of Neon Pitch-Green to simulate the effect of a lit stadium sign.

## Shapes

In alignment with the "sharp, clean lines" requirement, this design system utilizes a **Level 0 (Sharp)** roundedness philosophy. Rectilinear containers emphasize precision and technical performance. 

Borders are strictly 90-degree angles for all cards, input fields, and buttons. To prevent the UI from feeling dated, use thin 1px strokes for borders and intentional negative space. The only exception to the sharp-edge rule is for purely circular elements like user avatars or "Live" recording dots, which provide a necessary organic contrast to the rigid structural grid.

## Components

**Buttons:** Primary CTAs are solid Neon Pitch-Green with black text for maximum punch. Secondary buttons are "Ghost" style—transparent with a 1px white or green border and sharp corners.

**Live Indicators:** A dedicated component featuring a pulsing green dot and the text "LIVE" in Space Grotesk Bold. This component always sits on a glassmorphic background to remain visible against varying pitch colors.

**Cards:** Match cards use the Level 1 Navy surface. They should feature high-resolution player photography that subtly "breaks" the top border of the card to create a 3D effect. 

**Input Fields:** Deep navy backgrounds with 1px borders that glow green upon focus. All corners remain sharp.

**Data Visualizations:** Match stats (possession, shots) should use high-contrast bars in green vs. slate, avoiding rounded caps on the bars to maintain the sharp aesthetic.

**Scoreboard Overlay:** A persistent, semi-transparent glass bar at the top or bottom of the screen, utilizing a monospaced variant of the font for the match clock to prevent "jitter" as numbers change.