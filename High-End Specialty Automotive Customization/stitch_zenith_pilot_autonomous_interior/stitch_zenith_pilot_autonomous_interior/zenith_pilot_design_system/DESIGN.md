---
name: Zenith-Pilot Design System
colors:
  surface: '#041424'
  surface-dim: '#041424'
  surface-bright: '#2b3b4b'
  surface-container-lowest: '#000f1e'
  surface-container-low: '#0c1d2c'
  surface-container: '#102130'
  surface-container-high: '#1b2b3b'
  surface-container-highest: '#263647'
  on-surface: '#d3e4fa'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#d3e4fa'
  inverse-on-surface: '#223242'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#c5c7c8'
  on-secondary: '#2e3132'
  secondary-container: '#494c4d'
  on-secondary-container: '#babcbd'
  tertiary: '#00daf3'
  on-tertiary: '#00363d'
  tertiary-container: '#002328'
  on-tertiary-container: '#0094a6'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e1e3e4'
  secondary-fixed-dim: '#c5c7c8'
  on-secondary-fixed: '#191c1d'
  on-secondary-fixed-variant: '#454748'
  tertiary-fixed: '#9cf0ff'
  tertiary-fixed-dim: '#00daf3'
  on-tertiary-fixed: '#001f24'
  on-tertiary-fixed-variant: '#004f58'
  background: '#041424'
  on-background: '#d3e4fa'
  surface-variant: '#263647'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: 0.1em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.2em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  margin-page: 4rem
  gutter-grid: 2rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
  stack-lg: 3rem
---

## Brand & Style

This design system facilitates a "Level 3 Autonomous Lifestyle," where the boundary between driving and living is blurred. The brand personality is **Elite, Serene, and Intelligent**. It targets high-net-worth individuals who value time as their greatest luxury.

The aesthetic follows a **Minimalist-Luxe** movement, blending the stark clarity of high-end galleries with the immersive tech of future-forward interfaces. The style is defined by:
- **Sophisticated Airiness:** Excessive negative space to reduce cognitive load during transit.
- **Social-First Ergonomics:** UI patterns borrowed from mobile social feeds (vertical scrolling, story-style progress bars, and high-impact imagery) to make the vehicle feel like a personal digital hub.
- **Glassmorphic Accents:** Strategic use of "Glass-Cyan" to indicate interactive, data-driven layers that float above the physical interior environment.

## Colors

The palette is engineered for a high-contrast, premium "night-mode" feel, even during daylight hours.

- **Deep Navy (#001F3F):** The foundation. Used for the primary "Canvas" of the interior displays to minimize glare and maximize depth.
- **Silk White (#F8F9FA):** The primary content color. Used for high-priority typography and iconography to ensure razor-sharp legibility.
- **Glass-Cyan (#00E5FF):** The "Pulse." This color is reserved strictly for interactive elements, status indicators, and glassmorphic overlays.
- **Functional Neutrals:** A range of desaturated navies are used for secondary containers to maintain a monochromatic luxury feel without using standard grays.

## Typography

This design system utilizes a dual-font strategy to balance character with utility. 

**Montserrat** is used for display and headline roles. It is set with wide tracking (letter-spacing) to evoke a sense of architectural luxury and breathing room. Weights should remain light to medium to avoid a "heavy" feel.

**Inter** is the workhorse for body copy and system labels. It provides the necessary legibility for glancing at data at 70mph. 

**Key Rule:** All labels and short descriptors must be set in uppercase with at least 15-20% letter spacing to maintain the "digital-first luxury" signature.

## Layout & Spacing

The layout philosophy centers on **Wide Margins and Social-First Hierarchies**. 

- **The Grid:** A 12-column fluid grid for ultra-wide vehicle displays, transitioning to a single-column "Story" feed for passenger handheld devices. 
- **The "Zen" Margin:** A mandatory 4rem (64px) safe area around all primary displays to prevent content from feeling "trapped" by the physical bezels of the car’s interior.
- **Verticality:** Primary interactions are designed for vertical thumb-swipe gestures, mirroring modern social media patterns. This allows the passenger to navigate lifestyle features (dining, entertainment, climate) with minimal effort.

## Elevation & Depth

Depth in this design system is achieved through **Optical Translucency** rather than traditional shadows.

1.  **Base Layer:** The Deep Navy (#001F3F) solid foundation.
2.  **Muted Layer:** Secondary containers use a slight opacity (10-15%) of Silk White to create a "tinted glass" look.
3.  **Active Glass (Glassmorphism):** The Glass-Cyan (#00E5FF) is used with a 20px - 40px backdrop blur. This is reserved for "floating" elements like notification toasts, active play-bars, or navigation prompts.
4.  **High-Contrast Outlines:** Instead of shadows, use 1px "Silk White" borders at 10% opacity to define the edges of containers against the dark background.

## Shapes

The shape language is **Refined and Geometric**.

A `roundedness` level of **2** (0.5rem base) is used for standard components to maintain a clean, modern edge. However, large container cards and "lifestyle blocks" should utilize `rounded-xl` (1.5rem) to feel more like high-end furniture and less like industrial software. 

Interactive triggers (buttons) are often presented as "pill-shaped" to differentiate them clearly from informational containers.

## Components

- **Buttons:** Primary buttons use a Glass-Cyan fill with a heavy backdrop blur and Deep Navy text. Secondary buttons are "Ghost" style with a Silk White outline.
- **Lifestyle Cards:** High-aspect-ratio cards (9:16) for media and social integration. These use "Silk White" typography overlaid on immersive imagery with a subtle bottom-to-top Navy gradient.
- **Glass-Cyan Sliders:** Used for volume, climate, and lighting. The track is a faint Navy stroke, while the thumb is a glowing Glass-Cyan orb.
- **Input Fields:** Minimalist underlines rather than boxes. On focus, the underline glows with a Cyan outer-glow (neon effect).
- **Status Chips:** Small, pill-shaped indicators with 5% Cyan background and 100% Cyan text for "Autonomous Mode" or "Connected" states.
- **Social Feed List:** A vertically scrolling list of "Suggested Stops" or "Social Notifications" using wide-tracking headlines and generous padding between items.