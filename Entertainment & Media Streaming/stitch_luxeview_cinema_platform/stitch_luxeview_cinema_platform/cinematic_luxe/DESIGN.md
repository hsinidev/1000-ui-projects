---
name: Cinematic Luxe
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c9c6c5'
  primary: '#c9c6c5'
  on-primary: '#313030'
  primary-container: '#0a0a0a'
  on-primary-container: '#7b7979'
  inverse-primary: '#5f5e5e'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#ffb4aa'
  on-tertiary: '#690003'
  tertiary-container: '#200000'
  on-tertiary-container: '#f0181b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ffdad5'
  tertiary-fixed-dim: '#ffb4aa'
  on-tertiary-fixed: '#410001'
  on-tertiary-fixed-variant: '#930007'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-xl:
    fontFamily: Be Vietnam Pro
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.03em
  headline-md:
    fontFamily: Be Vietnam Pro
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.02em
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
  label-sm:
    fontFamily: Inter
    fontSize: 12px
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
  container-max: 1440px
  gutter: 24px
  margin-edge: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 64px
---

## Brand & Style

This design system is built to evoke the exclusivity of a private screening room. The personality is sophisticated, authoritative, and deeply immersive. By prioritizing high-resolution visual assets and a dark, moody environment, the interface recedes to let the content lead. 

The style utilizes **Glassmorphism** to create a sense of physical depth, where navigation and overlays appear as polished obsidian sheets floating over the cinematic background. The target audience expects a premium, frictionless experience that feels more like an editorial gallery than a software application.

## Colors

The palette is anchored by **Midnight Onyx (#0A0A0A)**, providing a deep, true-black foundation that maximizes the contrast of OLED displays. **Gold Leaf (#D4AF37)** is used sparingly for premium indicators, such as "Top 10," "4K HDR" badges, and VIP membership statuses. 

**Vibrant Crimson (#E50914)** is reserved strictly for high-priority calls to action, such as "Watch Now" or "Subscribe," ensuring they stand out against the dark environment. Gradients should transition from transparent to Midnight Onyx to create seamless blends between poster art and the UI.

## Typography

The typographic system utilizes **Be Vietnam Pro** for headlines to provide a contemporary, editorial feel. Headers feature wide tracking (letter-spacing) to enhance the sense of luxury and breathability. **Inter** is used for body copy and metadata for its exceptional legibility at smaller sizes on television and mobile screens. All labels and overlines should utilize uppercase styling with increased letter spacing to differentiate metadata from narrative text.

## Layout & Spacing

This design system employs a **fixed grid** approach for desktop and tablet to maintain a cinematic aspect ratio, while utilizing a fluid model for mobile. A 12-column grid provides the structure, with generous margins (48px) to prevent content from feeling crowded. 

Spacing follows an 8px rhythmic scale. Horizontal scrolling carousels should allow the "next" item to peek from the edge, signaling further content. Large vertical gaps (64px+) between genres or categories are used to create distinct "chapters" in the browsing experience.

## Elevation & Depth

Depth is achieved through **Glassmorphism** and layering rather than traditional drop shadows.
- **Level 1 (Base):** Full-screen cinematic imagery with a 40% black vignette.
- **Level 2 (Surface):** Semi-transparent Midnight Onyx panels with a 20px backdrop-blur. These are used for navigation bars and secondary info cards.
- **Level 3 (Interactive):** Elevated cards featuring a subtle 1px inner border (white at 10% opacity) to simulate the edge of a glass pane.
- **Level 4 (Overlay):** Full-screen modals with a 40px backdrop-blur, effectively isolating the user from the background content.

## Shapes

The shape language is sophisticated and precise. A **Soft (0.25rem)** base radius is applied to movie posters and standard buttons to maintain a sleek, modern look without feeling overly "bubbly." Larger components like modal containers and prominent "Hero" cards use a **rounded-lg (0.5rem)** radius. The interaction between sharp edges and soft corners reinforces the "Luxe" aesthetic.

## Components

- **Buttons:** Primary buttons are solid Vibrant Crimson. Secondary buttons use a glass-morphic fill (white at 10% opacity) with a white 1px border. All buttons use Be Vietnam Pro Medium.
- **Movie Cards:** High-resolution vertical posters. Upon hover, cards scale up by 5% and reveal a Gold Leaf progress bar at the bottom for "Continue Watching" items.
- **Navigation Bar:** Fixed at the top, utilizing a heavy backdrop-blur and a 1px bottom stroke in Gold Leaf (20% opacity).
- **Chips:** Used for genres or technical specs (e.g., "4K"). These feature a pill shape, no fill, and a thin grey border.
- **Playhead/Progress Bar:** A thin line where the elapsed time is represented in Gold Leaf and the remaining time in 20% opacity white.
- **Modals:** Centered overlays with a frosted glass background. The close button is always in the top right, utilizing a simple thin-line icon.