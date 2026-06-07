---
name: Corporate-Stealth PE System
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#b8c8da'
  on-secondary: '#223240'
  secondary-container: '#394857'
  on-secondary-container: '#a7b7c8'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#18191a'
  on-tertiary-container: '#818282'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 20px
  margin-desktop: 40px
  container-max: 1280px
---

## Brand & Style

The design system is engineered for the high-stakes world of private equity and cross-border asset relocation. It adopts a **Corporate-Stealth** aesthetic: a visual language that communicates power through restraint, security through precision, and intelligence through clarity. The brand personality is authoritative yet invisible, functioning like a high-end security vault—utilitarian, impenetrable, and impeccably organized.

The style is a hybrid of **Minimalism** and **Technical Modernism**. It avoids unnecessary ornamentation, favoring sharp edges, structural grids, and high-density information displays. The emotional response is one of total confidence; users should feel they are interacting with an elite, encrypted terminal where every pixel serves a functional purpose in managing global wealth.

## Colors

The design system utilizes a deep, "low-observable" palette designed for high-focus environments. The foundation is **Midnight Blue (#0A192F)**, used for primary backgrounds to minimize eye strain and evoke a sense of deep-space security. **Slate (#708090)** serves as the secondary structural color for borders and secondary text, while **Silver (#C0C0C0)** provides high-contrast legibility for primary content.

To emphasize the "High-Tech" requirement, the system employs a neon-adjacent **Accent (#00FFC2)** exclusively for real-time data pulses and active security states. This creates a "glow-in-the-dark" hierarchy where critical information pierces through the stealth background. Status indicators use extreme contrast—vivid reds and greens—against the dark base to ensure zero ambiguity during asset movement.

## Typography

This design system relies on **Inter** for its neutral, systematic, and highly legible characteristics. It provides the "Institutional" weight required for private equity. Headlines are tightly tracked and bold to command authority.

For technical precision and real-time data—such as asset coordinates, transaction IDs, and timestamps—the system introduces **JetBrains Mono**. This monospaced secondary font reinforces the "high-tech" and "secure" nature of the product, ensuring that numerical data is perfectly aligned and easily scannable. All labels for data fields are rendered in uppercase with increased letter spacing to mimic military-grade instrumentation.

## Layout & Spacing

The layout philosophy follows a **Fixed-Grid System** on a 4px base unit. This ensures rhythmic precision across all device sizes. For mobile-first implementation, the design system utilizes a 4-column grid with generous 20px side margins to prevent "edge-bleed" of sensitive data. On desktop, this scales to a 12-column grid.

Spacing is intentionally dense to allow for high information density, reflecting a professional "Dashboard" environment. However, structural sections are separated by distinct "Dead Zones" (larger margins) to prevent cognitive overload during rapid data updates. Alignment is strictly flush-left to maintain a fast, vertical scanning path for the eye.

## Elevation & Depth

To maintain the "Stealth" aesthetic, this design system rejects traditional soft shadows. Instead, depth is conveyed through **Tonal Layers** and **Subtle Gradients**. 

Higher-elevation elements (like modal dialogs or active cards) are indicated by a slightly lighter fill color (Slate-variant) and a crisp **1px Silver border** with low opacity. Backgrounds may feature extremely subtle radial gradients—moving from #0A192F to a slightly lighter navy—to draw the eye toward the center of the viewport. Interactive surfaces use a "recessed" look, achieved with inner borders rather than outer glows, simulating a physical control panel carved from a single block of material.

## Shapes

The design system utilizes **Sharp (0px)** roundedness for all primary UI components. This choice reinforces the "Precise" and "Authoritative" brand pillars. Right angles suggest a lack of compromise and an architectural rigidity suited for high-finance and relocation logistics.

While the primary buttons and containers are strictly rectangular, small circular elements are permitted exclusively for status "pips" or connectivity indicators to make them stand out as dynamic, real-time objects against the static, angular grid of the UI.

## Components

### Buttons & Controls
Buttons are rectangular with 1px solid borders. Primary actions use a "Silver" fill with "Midnight Blue" text for maximum contrast. Secondary actions are "Ghost" style (transparent fill, Slate border). The hover state is not a color change, but a "glitch-fast" inversion of colors or a subtle inner glow.

### Status Indicators
These are the most prominent visual elements. For real-time asset tracking, indicators use a "Pulse" animation. A "Secure" status is a solid Silver icon; a "Moving" status is a flashing Accent Green; a "Breached" status is a high-contrast Red alert box that occupies the top-tier elevation level.

### Input Fields
Inputs are minimalist, consisting of a bottom-border only or a very faint 1px Slate outline. Upon focus, the border color shifts to Silver, and the label transforms into a smaller "Data-Mono" style above the field.

### Data Cards
Cards for asset relocation details are flat with high-contrast headers. Use 1px Silver borders to separate distinct data sets. Content within cards is heavily structured using the monospaced font for numerical values to ensure column alignment across different rows.

### Security Overlays
Given the focus on security, the system includes "Biometric Verification" and "Encrypted Feed" components. These use scan-line textures (subtle 1px horizontal patterns) and monospaced "Processing" logs to provide visual feedback of the system's background security operations.