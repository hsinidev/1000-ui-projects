---
name: Obsidian Manga System
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
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#cac6c3'
  on-tertiary: '#32302f'
  tertiary-container: '#131211'
  on-tertiary-container: '#807d7b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e6e1df'
  tertiary-fixed-dim: '#cac6c3'
  on-tertiary-fixed: '#1c1b1a'
  on-tertiary-fixed-variant: '#484645'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-hero:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
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
    fontWeight: '600'
    lineHeight: '1.0'
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
  margin-mobile: 16px
  margin-desktop: 48px
  section-gap: 64px
---

## Brand & Style

The design system focuses on a "Theater Mode" philosophy, where the interface recedes to ensure the manga artwork remains the focal point. The brand personality is sophisticated, immersive, and cinematic. It targets a discerning audience that values high-quality curation and a premium reading experience.

The visual style is a blend of **Minimalism** and **Glassmorphism**. By using deep blacks and charcols, we create a sense of infinite depth. Glassmorphism is applied selectively to overlays and navigation elements to maintain context without obstructing the vibrant cover art or panels. This approach evokes an emotional response of focus and calm, transforming the act of reading into a prestige event.

## Colors

The palette is anchored in a dual-tone dark foundation. **True Black (#000000)** is reserved for the background of the manga reader and primary canvases to maximize contrast with white pages. **Deep Charcoal (#121212)** is used for UI containers, sidebars, and navigation to provide subtle separation.

This design system utilizes a **Dynamic Accent System**. While the default interactive state uses a neutral silver or white, the interface adopts genre-specific accents when a user enters a series-specific view:
- **Action:** Electric Blue for energy and precision.
- **Romance:** Soft Pink for warmth and emotion.
- **Horror:** Blood Red for tension and visceral impact.
- **Fantasy:** Deep Purple for mystery and magic.

Surface colors should use high-transparency overlays to maintain the glassmorphic aesthetic.

## Typography

The typography strategy relies on the contrast between functional utility and editorial elegance. 

**Noto Serif** is the voice of the content. It is used for series titles, chapter headings, and large display quotes. Its high-contrast strokes provide a premium, literary feel that elevates manga from "comics" to "graphic literature."

**Inter** handles the functional UI. It is selected for its exceptional legibility at small sizes and its neutral character. It stays out of the way, providing clarity for metadata (author names, dates, tags) and navigation items. All labels should be crisp, with slightly increased letter spacing for uppercase variants to ensure they remain legible against dark backgrounds.

## Layout & Spacing

The layout utilizes a **Fixed Grid** for content discovery and a **Fluid Core** for the reading experience. For browsing, a 12-column grid is employed with generous 48px margins on desktop to create a sense of exclusivity and "breathable" luxury. 

Whitespace is treated as a functional element, not a void. Large vertical gaps (64px+) separate content sections (e.g., "Trending" vs "Recently Updated") to prevent visual clutter. The "Manga Reader" view should ignore standard margins to provide an edge-to-edge immersive experience, with UI controls appearing only on hover or tap via translucent glass overlays.

## Elevation & Depth

This design system avoids traditional drop shadows in favor of **Tonal Layers** and **Glassmorphism**. Depth is communicated through luminosity:
- **Level 0 (Background):** True Black (#000000).
- **Level 1 (Surface):** Deep Charcoal (#121212).
- **Level 2 (Overlays/Modals):** A semi-transparent blur (Backdrop Filter: blur(20px)) with a 10% white border to simulate the edge of a glass pane.

The "Review & Reaction" drawer should emerge from the right side of the screen using a high-index glass layer, allowing the manga content to be partially visible beneath it, maintaining the user's place in the story.

## Shapes

The shape language is "Soft-Minimalist." We use subtle rounding to take the edge off the dark theme without making the UI feel "bubbly" or juvenile. 

Standard components like buttons and input fields use a **4px (0.25rem)** radius. Large "Series Cards" use a **8px (0.5rem)** radius to better frame the artwork. The sharp edges are reserved for the manga panels themselves within the reader to respect the original artist's intent.

## Components

### Series Cards
The primary discovery unit. These should be large, vertical aspect ratio (2:3) cards with minimal metadata. Title and rating should appear as a gradient overlay at the bottom of the card only.

### Buttons
Primary buttons use the dynamic genre accent color with white text. Secondary buttons are "Ghost" style, featuring a thin 1px border and no fill.

### Review & Reaction Drawer
A signature component that slides in from the right. It features a blurred backdrop, a vertical list of user reactions with emoji support, and a threaded comment system. The header of the drawer must display the current chapter and page being discussed.

### Sleek Navigation
A top-docked or side-docked navigation bar that is almost entirely transparent. It should feature icon-only labels for a cleaner look, with tooltips for accessibility.

### Genre Chips
Small, low-contrast capsules that take on the dynamic accent color as a subtle 20% opacity background tint and a 100% opacity text color.