---
name: Midnight Gala
colors:
  surface: '#041521'
  surface-dim: '#041521'
  surface-bright: '#2b3b49'
  surface-container-lowest: '#010f1c'
  surface-container-low: '#0d1d2a'
  surface-container: '#11212e'
  surface-container-high: '#1c2b39'
  surface-container-highest: '#273644'
  on-surface: '#d4e4f6'
  on-surface-variant: '#c6c6ce'
  inverse-surface: '#d4e4f6'
  inverse-on-surface: '#223240'
  outline: '#909098'
  outline-variant: '#46464d'
  surface-tint: '#bfc5e4'
  primary: '#bfc5e4'
  on-primary: '#292f48'
  primary-container: '#0a1128'
  on-primary-container: '#767c99'
  inverse-primary: '#575d78'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#111313'
  on-tertiary-container: '#7d7e7e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#bfc5e4'
  on-primary-fixed: '#141a32'
  on-primary-fixed-variant: '#3f465f'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#041521'
  on-background: '#d4e4f6'
  surface-variant: '#273644'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
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
  label-lg:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 80px
  section-gap: 160px
---

## Brand & Style
The brand personality is authoritative yet ethereal, catering to a high-end clientele seeking prestige and exclusivity in bridal and formal wear. The UI must evoke a sense of "The Blue Hour"—that quiet, cinematic moment of anticipation before a grand event. 

The design style is **Minimalist-Luxury with Glassmorphism**. It prioritizes immersive, full-bleed imagery and deep tonal layering. By using high contrast between the dark "Midnight" background and the "Gold" interactive elements, the system creates a focused, spotlight effect on the couture. The emotional response should be one of awe, sophistication, and effortless grace.

## Colors
This design system utilizes a dark-mode-first palette to achieve a cinematic atmosphere. 

- **Primary (Midnight Blue):** Used for the core canvas and deep immersive backgrounds. It provides the "void" that makes photography pop.
- **Secondary (Gold):** Reserved for high-intent actions, accents, and premium signifiers. It should be used sparingly to maintain its value.
- **Tertiary (Smoke White):** Applied to primary typography and subtle borders to ensure legibility against the dark base.
- **Neutral (Slate Smoke):** Used for secondary text, disabled states, and atmospheric depth within UI containers.

## Typography
The typography strategy relies on the tension between the classic, editorial feel of **Noto Serif** and the modern, technical precision of **Manrope**.

- **Headlines:** Must always use Noto Serif. Large display sizes should use tighter letter spacing to feel like a high-fashion magazine masthead.
- **Body:** Manrope provides a clean, neutral contrast that ensures readability for long descriptions of fabrics and services.
- **Labels:** Uppercase labels with generous letter spacing should be used for categories, breadcrumbs, and small UI hints to reinforce the luxury aesthetic.

## Layout & Spacing
The layout follows a **Fixed Grid** model for desktop to maintain editorial control over whitespace, transitioning to a fluid model for mobile.

The philosophy is "Generous and Airy." We prioritize vertical breathing room (Section Gaps) to prevent the high-contrast colors from feeling claustrophobic. Use a 12-column grid with wide gutters (32px) to allow content to feel "decoupled" from the edges. Margins are intentionally large (64px+) to create a frame-like effect around the content, mimicking a gallery wall.

## Elevation & Depth
Depth is created through **Glassmorphism and Tonal Layering** rather than traditional shadows.

1.  **Base Layer:** Solid Midnight Blue.
2.  **Surface Layer:** Midnight Blue with a slight lightness increase (approx 5%) to define cards and containers.
3.  **Glass Layer:** For navigation bars and floating overlays, use a 15% opacity Smoke White with a heavy (20px-40px) background blur.
4.  **Accents:** Gold is used as a "light source." Use subtle gold outer glows (5-10% opacity) for active states to simulate a physical shimmer. 
Avoid heavy black shadows; instead, use thin, 1px Smoke White borders at 10% opacity to define edges.

## Shapes
This design system utilizes **Sharp (0px)** corners. The absence of rounding reinforces the "architectural" and "formal" nature of the brand. Rectilinear shapes convey stability, precision, and the sharp lines of high-end tailoring. 

Interactive elements like buttons and input fields should remain strictly rectangular. The only exception is for circular icon-buttons (e.g., gallery navigation arrows), which should be perfect circles to act as focal points.

## Components

- **Buttons:** Primary buttons are Gold with Midnight Blue text, no border. Secondary buttons are transparent with a 1px Gold border. All buttons use the Label-LG typography style (uppercase).
- **Sophisticated Forms:** Input fields use "Underline Only" styling—a 1px Smoke border on the bottom. Labels float above in Manrope. Focused states turn the underline Gold.
- **Swipeable Galleries:** Full-screen or large-format containers. Use "Ghost" navigation arrows (thin circles) that appear on hover. Progress is indicated by a slim Gold line at the bottom of the viewport.
- **Elegant Calendars:** Used for booking consultations. The grid is minimalist with no internal borders. Selected dates are highlighted with a solid Gold square; available dates are Smoke White; unavailable dates are 20% opacity.
- **Chips:** Small rectangular boxes with a 1px Smoke border, used for size selection or fabric types.
- **Cards:** No shadows. Defined by a subtle background color shift and high-quality imagery that bleeds to the top and sides. Content is centered or left-aligned with significant internal padding (32px+).