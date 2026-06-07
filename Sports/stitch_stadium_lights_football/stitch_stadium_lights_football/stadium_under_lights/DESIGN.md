---
name: Stadium Under Lights
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bbcbbb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#869486'
  outline-variant: '#3d4a3e'
  surface-tint: '#4ae183'
  primary: '#54e98a'
  on-primary: '#003919'
  primary-container: '#2ecc71'
  on-primary-container: '#005027'
  inverse-primary: '#006d37'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#00ed7b'
  on-tertiary: '#003919'
  tertiary-container: '#00ce6a'
  on-tertiary-container: '#005126'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6bfe9c'
  primary-fixed-dim: '#4ae183'
  on-primary-fixed: '#00210c'
  on-primary-fixed-variant: '#005228'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#61ff97'
  tertiary-fixed-dim: '#00e476'
  on-tertiary-fixed: '#00210c'
  on-tertiary-fixed-variant: '#005227'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-display:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-table:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 20px
  margin: 24px
  container-max: 1280px
  score-card-gap: 12px
---

## Brand & Style

This design system captures the high-octane atmosphere of a night match under floodlights. The brand personality is intense, authoritative, and energetic, designed for the dedicated football fan who demands real-time data and premium editorial content. 

The visual style is a fusion of **High-Contrast / Bold** and **Glassmorphism**. It utilizes deep, atmospheric layering to simulate the depth of a stadium bowl, while using "light-leak" gradients and glowing neon accents to mimic the glare of stadium towers. The emotional response is one of anticipation and "big-match" prestige, maintaining a premium sports broadcast feel through sharp execution and high-energy color pops.

## Colors

The palette is built on a "Pitch Black" foundation to maximize contrast and focus.

- **Primary:** Pitch Green (#2ecc71), used for primary actions, live score indicators, and key highlights. It represents the vibrant grass of the field.
- **Secondary:** Charcoal (#1a1a1a), used for card backgrounds and elevated surfaces to create depth without losing the dark aesthetic.
- **Tertiary:** Hyper Green (#00ff85), a more luminous variant used sparingly for "Live" badges and glowing hover states to simulate stadium light intensity.
- **Neutral:** Pure Black (#0a0a0a) and Floodlight White (#f8f9fa). Surface colors should use deep charcoals to allow for "glow" effects to be visible.

Apply subtle noise textures to dark backgrounds to simulate the grain of concrete or stadium turf.

## Typography

This design system utilizes two distinct typefaces to balance athletic energy with data density. 

**Lexend** is the engine for headlines and labels. Its wide, geometric, and clear-cut nature provides an "athletic" feel that remains highly readable at large scales. Use it in Bold and Extra Bold weights for scoreboards and section headers.

**Work Sans** serves all long-form news and statistical data tables. It is chosen for its exceptional legibility in dark mode, preventing eye strain during heavy data consumption. Data points in tables should utilize the SemiBold weight to pop against the dark backgrounds.

## Layout & Spacing

The layout employs a **Fixed Grid** model (12 columns) for desktop editorial content, transitioning to a fluid stack for mobile scores. 

A tight, 4px-based rhythmic scale ensures high information density. For "Match Day" views, use a horizontal-scroll "Score Strip" at the top of the viewport with minimal padding to maximize the number of visible fixtures. News feeds should use a masonry-style or structured 3-column grid to maintain scannability. Vertical rhythm is prioritized to ensure that data-heavy tables remain easy to track line-by-line.

## Elevation & Depth

Depth is created through **Tonal Layers** and **Light-Source Logic**. 

1. **The Pitch (Base):** Deepest black (#0a0a0a).
2. **The Stands (Cards):** Dark Charcoal (#1a1a1a) with a subtle 1px border (#2ecc71 at 10% opacity).
3. **The Floodlights (Interaction):** High-elevation elements (like active score cards or modals) feature a "bloom" effect—a soft, green outer glow (`box-shadow: 0 0 20px rgba(46, 204, 113, 0.2)`).

Use backdrop blurs (Glassmorphism) behind navigation bars to simulate looking through stadium glass suites. This maintains context while ensuring the active content remains the focus.

## Shapes

The design system uses a **Soft (1)** shape language. The subtle 0.25rem radius on cards and buttons provides a modern, "tech-sport" feel without the playfulness of fully rounded corners. 

Buttons and badges should feel "cut" and precise. For specific UI elements like "Live" indicators, use a 0px (Sharp) radius to evoke a more aggressive, broadcast-ticker aesthetic.

## Components

- **Buttons:** Primary buttons use a solid Pitch Green background with black text for maximum contrast. Secondary buttons use a transparent background with a green 1px stroke.
- **Score Cards:** Utilize a dark background with a high-contrast white for team names and the Pitch Green for the live clock/score. Use "neon" green pips for live status.
- **News Cards:** Use a vertical gradient overlay (Bottom: Black, Top: Transparent) over imagery to ensure headline legibility.
- **Data Tables:** Striped rows are prohibited; instead, use thin 1px charcoal dividers. Highlight the "Home Team" or "Player" using a vertical green bar on the left edge of the cell.
- **Chips/Badges:** Small, caps-lock Lexend labels with high-contrast backgrounds for "Breaking News" or "Transfer" categories.
- **Input Fields:** Dark backgrounds with a bottom-only border that glows Green on focus.
- **The "Live" Ticker:** A persistent, high-contrast horizontal bar with scrolling text, utilizing a slight blur background to separate it from the main feed.