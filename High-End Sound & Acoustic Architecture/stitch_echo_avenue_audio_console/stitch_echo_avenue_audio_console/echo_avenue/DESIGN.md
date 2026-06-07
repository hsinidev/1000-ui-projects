---
name: Echo-Avenue
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d1c1d9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9a8ca2'
  outline-variant: '#4e4356'
  surface-tint: '#dfb7ff'
  primary: '#dfb7ff'
  on-primary: '#4b007e'
  primary-container: '#9d00ff'
  on-primary-container: '#f7e5ff'
  inverse-primary: '#8c00e5'
  secondary: '#c8c6c5'
  on-secondary: '#303030'
  secondary-container: '#474746'
  on-secondary-container: '#b6b5b4'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#696a6a'
  on-tertiary-container: '#ebebeb'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f1daff'
  primary-fixed-dim: '#dfb7ff'
  on-primary-fixed: '#2d004f'
  on-primary-fixed-variant: '#6b00b0'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: 80px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  metric-lg:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
    letterSpacing: -0.01em
  metric-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 1.5rem
  margin-mobile: 1rem
  margin-desktop: 2.5rem
  container-max: 1440px
---

## Brand & Style

The brand identity centers on "Sonic Precision." This design system reflects the high-stakes environment of live performance technology—where latency is zero and performance is absolute. The aesthetic is a fusion of **High-Contrast Bold** and **Glassmorphism**, designed to feel like a high-end audio console in a darkened stadium.

The UI must evoke a sense of controlled energy. By utilizing deep blacks and vibrant violet highlights, we create a hierarchy that directs the user's attention to critical data and performance metrics. The tone is uncompromisingly professional and technical, prioritizing legibility and rapid information processing over decorative flourishes. Visual interest is driven by vector-line graphics—abstract representations of frequencies and sound waves—that provide a sense of motion without distracting from the task at hand.

## Colors

This design system is built on a "Vantablack" foundation. **Carbon Black (#121212)** serves as the primary canvas, ensuring maximum contrast for technical readouts. **Graphite (#2A2A2A)** is used for structural surfaces, containers, and secondary layers to provide subtle depth.

**Neon Violet (#9D00FF)** is the "Active" state. It is used sparingly but aggressively for primary actions, focus states, and data peaks. High-visibility status colors (Success/Error) are dialed to maximum saturation to ensure they pierce through the dark interface during live events. All overlays and modal windows utilize a glassmorphic blur to maintain a sense of environmental awareness within the software.

## Typography

The typography strategy is bifurcated between expressive geometry and technical utility. 

1.  **Space Grotesk** is used for headlines and large display moments. Its geometric construction feels modern and high-performance.
2.  **Geist** handles all standard UI text and body copy. Its clean, neutral characteristics ensure clarity in complex dashboard environments.
3.  **JetBrains Mono** is reserved for all numeric data, metrics, and labels. The monospaced nature allows for "tabular figures," meaning numbers won't jump or shift when values update rapidly during a live performance.

Large display type should utilize tight letter spacing, while small technical labels should be tracked out for better legibility on high-resolution displays.

## Layout & Spacing

The design system utilizes a **12-column fixed grid** for desktop environments, ensuring that dense technical data remains organized and predictable. A strict **8px spatial system** governs all padding and margins.

- **Desktop:** 12 columns, 24px gutters. Content is centered with a max-width of 1440px.
- **Tablet:** 8 columns, 16px gutters.
- **Mobile:** 4 columns, 16px margins.

The layout philosophy is "Data-First." Spacing is intentionally tight to maximize information density, allowing operators to see more of the signal chain without scrolling. Negative space is used primarily to separate distinct functional modules rather than for aesthetic "breathability."

## Elevation & Depth

In this dark-mode-default environment, depth is communicated through **Tonal Layering** and **Glassmorphism** rather than traditional drop shadows.

1.  **Base Layer:** Carbon Black (#121212).
2.  **Surface Level:** Graphite (#2A2A2A) containers with a 1px solid stroke in a slightly lighter grey (#3A3A3A) to define boundaries.
3.  **Overlay Level:** Semi-transparent panels (60-80% opacity) with a `backdrop-filter: blur(20px)`. This is used for menus, modals, and tooltips, creating a "glass" effect that allows the underlying waveforms to remain visible.
4.  **Luminescence:** Critical elements (active buttons, live indicators) use a **Neon Violet Glow**. This is achieved with an outer bloom effect (shadow spread) to simulate the look of LED hardware.

## Shapes

The shape language is strictly **Sharp (0px)**. To reinforce the technical, high-precision nature of the company, we avoid rounded corners. Every component—from buttons to cards to input fields—must feature hard 90-degree angles.

This geometric rigidity mimics the rack-mounted hardware used in professional audio environments. Sharp corners facilitate a tighter grid alignment and a more aggressive, high-performance visual profile. Vector lines representing frequencies should use consistent 2px stroke weights with "butt" caps (square ends) to maintain this geometric consistency.

## Components

### Buttons
Primary buttons are solid Neon Violet with white or black text. They feature no border-radius. On hover, they emit a violet outer glow. Secondary buttons use a Graphite background with a 1px violet stroke.

### Input Fields
Inputs are Carbon Black with a 1px Graphite border. Upon focus, the border transitions to Neon Violet, accompanied by a subtle inner glow. Labels always use JetBrains Mono in uppercase.

### Cards & Modules
Modules are Graphite panels with a 1px stroke. Header areas of cards should be distinguished by a subtle 5% white tint or a different background shade to separate control groups from data displays.

### Sound Wave Graphics
Dynamic vector lines used for decoration or data visualization should be rendered in Neon Violet. Use varying opacities to create a sense of depth and "signal ghosting."

### Checkboxes & Radios
Custom-built square components. Checkboxes use a simple "X" or solid fill in Neon Violet when active, maintaining the sharp-edge aesthetic.

### Performance Meters
Vertical or horizontal bars. Use a segmented "LED" look (blocks of color) rather than a smooth gradient fill to emphasize technical precision.