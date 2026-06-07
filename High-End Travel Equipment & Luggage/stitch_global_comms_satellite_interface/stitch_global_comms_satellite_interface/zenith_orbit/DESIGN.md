---
name: Zenith Orbit
colors:
  surface: '#0d1515'
  surface-dim: '#0d1515'
  surface-bright: '#333b3b'
  surface-container-lowest: '#080f10'
  surface-container-low: '#151d1e'
  surface-container: '#192122'
  surface-container-high: '#232b2c'
  surface-container-highest: '#2e3637'
  on-surface: '#dce4e4'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dce4e4'
  inverse-on-surface: '#2a3232'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c5c6cb'
  on-secondary: '#2e3134'
  secondary-container: '#44474b'
  on-secondary-container: '#b3b5ba'
  tertiary: '#f7f8f8'
  on-tertiary: '#2f3131'
  tertiary-container: '#dbdbdb'
  on-tertiary-container: '#5e6060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e1e2e7'
  secondary-fixed-dim: '#c5c6cb'
  on-secondary-fixed: '#191c1f'
  on-secondary-fixed-variant: '#44474b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0d1515'
  on-background: '#dce4e4'
  surface-variant: '#2e3637'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for the elite traveler, bridging the gap between high-performance aerospace instrumentation and luxury consumer electronics. The brand personality is authoritative yet ethereal, evoking the silence of deep space and the precision of satellite telemetry. 

The aesthetic is a sophisticated blend of **Glassmorphism** and **Futuristic Minimalism**. It utilizes translucent layering to suggest depth in the void, punctuated by high-energy neon accents that signify active connectivity and data flow. The UI should feel like a high-end digital cockpit—utilitarian in its clarity but premium in its execution, providing users with a sense of absolute control over their global reach.

## Colors

The palette is strictly limited to maintain a high-contrast, premium atmosphere. 

- **Deep Space Black (#05070A):** The foundation of the interface, providing a void-like depth that makes foreground elements pop.
- **Neon Cyan (#00F2FF):** The primary action and signal color. It represents "active" states, data transmission, and the glowing core of the technology.
- **Crisp White (#FFFFFF):** Used exclusively for high-priority typography and iconography to ensure legibility against the dark void.
- **Functional Grays:** Translucent variants of white (10%, 20%, 40% opacity) are used for borders, secondary text, and glass surfaces.

## Typography

This design system utilizes **Space Grotesk** for headlines and labels to provide a geometric, technical feel that aligns with aerospace aesthetics. **Inter** is used for body copy to ensure maximum readability during travel. 

Headlines should occasionally use uppercase styling with increased letter spacing to mimic instrument panels. For telemetry and signal metrics, the "data-mono" style provides a structured, rhythmic appearance for numerical values.

## Layout & Spacing

The design system employs a **Fixed Grid** approach for desktop (12 columns) and a fluid approach for mobile. The layout philosophy is "Centric and Focused"—critical data visualizations are often centered, surrounded by generous whitespace (the "void") to emphasize premium quality.

Spacing follows a strict 8px base unit. Margins are wide to prevent the UI from feeling cluttered, maintaining the minimalist, high-end aesthetic. Elements should be grouped into functional clusters with distinct glass backgrounds to separate data streams clearly.

## Elevation & Depth

Depth is not communicated through shadows, but through **Glassmorphism and Luminance**. 

1.  **Base Layer:** The Deep Space Black background.
2.  **Mid Layer:** Translucent glass panels (Backdrop blur: 12px-20px) with 1px borders in low-opacity Cyan or White.
3.  **Top Layer:** Interactive elements with outer glows (Neon Cyan) that appear to cast light onto the glass surfaces beneath them.

Interactive states should trigger a "scanning" line animation—a thin, high-intensity Cyan horizontal line that scrolls vertically across the component to indicate data processing or focus.

## Shapes

The shape language is "Technical Precision." This design system uses **Soft (0.25rem)** roundedness for most UI components. This subtle rounding suggests a refined, machined edge—similar to high-end aerospace hardware—rather than the overly bubbly shapes found in consumer apps. 

Circular elements are reserved specifically for data visualizations, such as signal strength rings and orbital trackers, creating a distinct visual contrast between structural containers (rectilinear) and live data (circular).

## Components

### Buttons
Primary buttons feature a solid Neon Cyan fill with Deep Space Black text. On hover, they emit a 15px Cyan outer glow. Secondary buttons use a "ghost" style with a 1px Neon Cyan border and a subtle interior gradient that animates on hover.

### Cards & Containers
Containers must use glassmorphism: a 10% opacity white background with a heavy backdrop blur. Borders should be 1px wide, using a 20% white-to-cyan linear gradient to suggest light reflecting off a glass edge.

### Inputs & Selection
Input fields are underlined rather than boxed, utilizing a Cyan "scanning" animation when focused. Checkboxes and radio buttons are minimalist geometric shapes (squares/circles) that "fill" with a neon glow when selected.

### Data Visualizations
The system's signature component is the **Circular Signal Metric**. This uses concentric rings of varying thickness. Active segments pulse with Cyan light, while inactive segments remain at 5% white opacity.

### Scanning Line
A decorative yet functional element: a 1px horizontal line with a `box-shadow` of `0 0 8px #00F2FF` that moves vertically across cards or the entire viewport during loading or data refresh states.