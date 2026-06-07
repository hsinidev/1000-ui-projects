---
name: Zenith-Auction
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
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
  secondary: '#ffb4a8'
  on-secondary: '#690000'
  secondary-container: '#e60000'
  on-secondary-container: '#fff6f5'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#080a0a'
  on-tertiary-container: '#78797a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c9c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a8'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#930100'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Oswald
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Oswald
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  headline-md:
    fontFamily: Oswald
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
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
  data-display:
    fontFamily: JetBrains Mono
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for the high-stakes world of elite horology auctions. It targets a demographic of sophisticated collectors who value precision, speed, and exclusivity. The aesthetic is defined as **High-Contrast Minimalism**—a style that strips away all distractions to focus on the movement of the clock and the value of the asset.

The emotional response should be one of "controlled urgency." By combining a deep matte dark mode with aggressive red accents, the UI mimics the cockpit of a racing machine or a high-frequency trading terminal. Every interaction must feel instantaneous and definitive, reflecting the finality of a gavel strike.

## Colors

This design system utilizes a restricted, high-impact palette to ensure maximum legibility and focus. 

- **Matte Black (#0A0A0A):** The foundation. Used for the primary background to eliminate glare and create depth.
- **Racing Red (#E60000):** The signal. Reserved strictly for high-energy actions, critical countdowns, and active bid indicators.
- **Pure White (#FFFFFF):** The data. Used for primary typography and essential UI borders to ensure sharp contrast against the matte base.
- **Surface Gray (#1A1A1A):** The separator. Used for secondary containers and card backgrounds to create subtle layering without breaking the dark-mode immersion.

## Typography

The typography strategy emphasizes technical precision. 

- **Headers:** **Oswald** provides a bold, condensed, and industrial feel. It should be used in uppercase for all major headings to command attention.
- **Body:** **Inter** is used for descriptions and long-form content to ensure readability amidst the high-contrast environment.
- **Data & Labels:** **JetBrains Mono** is utilized for prices, serial numbers, and live timers. Its monospaced nature ensures that ticking numbers do not cause layout shifts, maintaining a "digital instrument" feel.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop and a fluid model for mobile. A 12-column grid is used with narrow gutters (16px) to maximize the screen real estate for high-resolution watch photography.

Spacing follows a strict 4px base unit. In the "Fast" aesthetic, padding should be compact to keep as much critical information "above the fold" as possible. Use generous margins (32px+) only for the outer viewport to frame the content like a luxury display case, while keeping internal component spacing tight and efficient.

## Elevation & Depth

To maintain the "Minimalist but Aggressive" style, this design system avoids soft ambient shadows. Instead, it uses **Bold Borders** and **Tonal Layers** to convey hierarchy.

- **Level 0 (Background):** #0A0A0A.
- **Level 1 (Cards/Panels):** #1A1A1A with a 1px solid #FFFFFF (10% opacity) border.
- **Level 2 (Active/Hover):** #1A1A1A with a 1px solid #E60000 border.
- **Interactions:** When an item is selected or a bid is placed, the element should glow slightly using a sharp, 0-blur outer stroke of Racing Red rather than a soft shadow.

## Shapes

The shape language is strictly **Sharp (0)**. Every button, input field, and container must have 0px corner radii. This reinforces the technical, precise, and aggressive nature of the brand. There are no "soft" elements in high-stakes bidding; the architecture should reflect the hard edges of industrial watchmaking and engineering.

## Components

### Buttons
- **Primary (Bid):** Solid #E60000 background, #FFFFFF uppercase text (Oswald). No rounding. On hover, background shifts to #B30000.
- **Secondary:** Transparent background with a 2px solid #FFFFFF border. White text.

### Input Fields
- **Bidding Input:** #0A0A0A background, 1px #FFFFFF border. Text is JetBrains Mono for numeric precision. Focus state triggers a 1px #E60000 border.

### Cards
- **Product Card:** #1A1A1A background. Full-bleed imagery. Information footer uses a 1px top border of #FFFFFF at 10% opacity.

### Chips & Status
- **Live Status:** A solid #E60000 rectangle with white monospaced text. 
- **Time Remaining:** Must use JetBrains Mono. When under 60 seconds, the text color flips from White to Racing Red and triggers a subtle pulse animation.

### Lists
- **Bid History:** Alternating zebra stripes of #0A0A0A and #141414. High-contrast white text for the price, muted gray for the timestamp.

### Additional Components
- **The "Gavel" Pulse:** A full-screen 100ms red border flash when a new "Highest Bid" is recorded, providing immediate sensory feedback to the user.