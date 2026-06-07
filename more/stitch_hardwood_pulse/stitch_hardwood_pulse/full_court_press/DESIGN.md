---
name: Full-Court Press
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#46362e'
  surface-container-lowest: '#170b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362720'
  surface-container-highest: '#41312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#989999'
  on-tertiary-container: '#2f3132'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#41312a'
typography:
  display-xl:
    fontFamily: Lexend
    fontSize: 84px
    fontWeight: '800'
    lineHeight: 90%
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 100%
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 110%
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 160%
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 150%
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 100%
    letterSpacing: 0.05em
spacing:
  base: 8px
  container-max: 1440px
  gutter: 24px
  margin-x: 40px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is engineered to capture the kinetic energy and high-stakes atmosphere of professional basketball. The aesthetic is rooted in **High-Contrast / Bold** design, leveraging the aggression of sports broadcasting with the precision of modern digital interfaces. 

The personality is intense, authoritative, and fast-paced. It targets an audience that craves real-time data, immersive highlights, and an "on-court" feel. The UI evokes a sense of momentum through the use of sharp angles, heavy directional shadows, and "bouncy" micro-interactions that mimic the elasticity of a basketball. Visual depth is not subtle; it is achieved through extreme layering and hard-edged silhouettes to ensure every stat and video frame feels monumental.

## Colors

The palette is dominated by a deep matte black (`#1A1A1A`) to provide a high-performance, dark-mode foundation that makes media content pop. Vibrant basketball orange (`#FF6B00`) serves as the primary action color, used for critical UI cues, active states, and branding accents. 

Crisp white is reserved for high-readability text and primary icons, ensuring maximum contrast against the dark background. A limited set of high-saturation status colors (Success/Error) are used sparingly to maintain the "arena" atmosphere without distracting from the core team colors.

## Typography

Typography in this design system is split between "Performance" and "Information." 

**Lexend** is utilized for all headlines and labels. Its bold, geometric construction mimics the numbers on athletic jerseys. To achieve the "condensed" athletic look, large display headers use heavy weights with negative letter-spacing and uppercase transformations.

**Inter** is used for body copy and data-heavy tables. It provides a systematic, neutral counterpoint to the aggressive headers, ensuring that long-form articles and player bios remain legible during high-speed browsing.

## Layout & Spacing

The layout utilizes a **fixed-width 12-column grid** for desktop, centered within the viewport to maintain a premium, editorial feel. Gutter widths are generous (24px) to allow for the heavy shadows and "explosive" hover states that expand beyond the container boundaries.

Vertical rhythm is governed by an 8px baseline grid. Components like the **Vertical Schedule Sidebar** occupy a dedicated 3-column span on the right, while the **Video-first Gallery** utilizes a fluid 9-column span that breaks into a masonry layout to emphasize different content weights.

## Elevation & Depth

Depth is conveyed through **Hard-Edged Shadows** and **Tonal Layering**. Unlike soft, ambient shadows, this design system uses high-opacity, offset shadows (e.g., `8px 8px 0px rgba(0,0,0,0.5)`) that give elements a physical, "stacked" appearance.

1.  **Base:** The matte black background (#1A1A1A).
2.  **Surface:** Dark grey cards (#262626) with 1px solid borders in #333333.
3.  **Raised:** Elements that hover or active cards use a secondary orange shadow to create a "glow" or "lift" effect.
4.  **Interactive:** When clicked, elements should visually "depress" by reducing the shadow offset, simulating a physical button press.

## Shapes

The shape language is strictly **Sharp (0px)**. No rounded corners are permitted. This reinforces the aggressive, high-energy nature of the sport. Every button, card, input field, and video container features 90-degree angles. To add visual interest, specific decorative elements or "call-out" badges may feature 45-degree diagonal "clipped" corners to mimic jersey typography and court markings.

## Components

### Interactive Spider-Web (Radar) Charts
Used for player stats comparisons. The web lines are rendered in thin white strokes (20% opacity) with the filled area using a 50% transparent orange. Points on the web should "pulse" when hovered.

### Vertical Schedule Sidebar
A persistent component featuring high-contrast blocks. Game-day entries use the primary orange for "Live" status, with a white vertical bar indicating the current selection. Transitioning between days should feel "snappy" with a slight overshoot (elastic) animation.

### Buttons & Inputs
- **Primary Button:** Solid #FF6B00 background, black uppercase text, 0px radius. On hover, it grows by 4% in scale with a "bouncy" spring transition.
- **Inputs:** Matte black background with a 2px white bottom-border only. The border turns orange and thickens on focus.

### Video-First Gallery
Thumbnails utilize an aspect ratio of 16:9 or 9:16 (shorts). Every thumbnail features a heavy "Play" icon overlay in white. On hover, the video begins a silent auto-preview while the card "jumps" forward using the established elevation shadows.

### Chips & Badges
Rectangular, sharp-edged tags. Use "Live" badges with a flickering red dot to create urgency. All badges use the **label-bold** typography spec.