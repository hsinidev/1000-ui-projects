---
name: Cyber-Shield Design System
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
  on-surface-variant: '#b9ccb2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#84967e'
  outline-variant: '#3b4b37'
  surface-tint: '#00e639'
  primary: '#ebffe2'
  on-primary: '#003907'
  primary-container: '#00ff41'
  on-primary-container: '#007117'
  inverse-primary: '#006e16'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#fcf8f8'
  on-tertiary: '#313030'
  tertiary-container: '#dfdcdb'
  on-tertiary-container: '#626060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#72ff70'
  primary-fixed-dim: '#00e639'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#00530e'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: metropolis
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: metropolis
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-mono:
    fontFamily: jetbrainsMono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  caption-sm:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-edge: 40px
  section-gap: 80px
---

## Brand & Style

The design system is engineered to evoke an atmosphere of absolute digital sovereignty. Targeting High-Net-Worth Individuals (HNWIs), the aesthetic prioritizes "discreet power"—a blend of high-end luxury and military-grade technical precision. 

The visual style is a fusion of **Minimalism** and **Glassmorphism**. It utilizes expansive dark space to represent the "void" of the digital landscape, where the UI acts as a precise, illuminated command center. Every element must feel intentional, expensive, and impenetrable. The emotional goal is to move the user from a state of digital anxiety to one of calm, overseen security.

## Colors

The palette is strictly constrained to reinforce authority. 

- **Deep Space Black (#050505):** The foundation. It is not a true neutral black, but a deep, pressurized dark that provides the canvas for high-contrast elements.
- **Neon Green (#00FF41):** Used exclusively for "System Health," "Active Protection," and critical action accents. It should never be used for large surfaces, only for thin lines, indicators, and subtle outer glows.
- **Pure White (#FFFFFF):** Reserved for primary typography and essential iconography to ensure maximum legibility against the dark background.
- **Secondary Grays:** Used for secondary text and subtle borders to maintain hierarchy without cluttering the visual field.

## Typography

This design system utilizes a tiered typographic approach to balance luxury with technical utility.

- **Headlines (Metropolis):** Geometric and structured. Used to convey stability and modern sophistication.
- **Body Text (Inter):** Highly legible and neutral, ensuring that complex security reports remain easy to scan.
- **Technical Data (JetBrains Mono):** Used for status codes, IP addresses, timestamps, and small labels. This monospaced font signals the "tech-forward" nature of the firm.
- **Hierarchy:** High contrast in size and weight is essential. Use uppercase JetBrains Mono for all eyebrow titles and status indicators.

## Layout & Spacing

The layout follows a **Fixed Grid** model within a centered container for desktop, ensuring an organized, balanced presentation. 

- **Grid:** A 12-column grid with generous 24px gutters.
- **Rhythm:** All spacing must be multiples of 8px. 
- **Density:** High-HNWI interfaces require "breathing room." Avoid dense clusters of information. Use wide margins and significant vertical gaps (section-gap) to separate distinct security modules.
- **Alignment:** Strict adherence to the grid. Elements should feel "locked" into place, suggesting a disciplined and secure architecture.

## Elevation & Depth

Depth is created through **Glassmorphism** and light-based hierarchy rather than traditional shadows.

- **Glass Surfaces:** Cards use a semi-transparent fill (`rgba(18, 18, 18, 0.7)`) with a high-intensity background blur (20px-40px). 
- **Luminous Borders:** Instead of shadows, use 1px solid borders. For active or "protected" states, these borders transition from a neutral gray to a subtle Neon Green glow.
- **Z-Axis:** Higher elevation is represented by increased transparency (lighter fills) and sharper background blurs, making the element appear closer to the user's "HUD."
- **Internal Glows:** Apply a very subtle inner shadow (0px 1px 2px) in white at 10% opacity to the top edge of cards to simulate a light source from above.

## Shapes

To reinforce the feeling of a "Shield" and a "Fortress," the design system utilizes **Sharp (0px)** corners for all primary structural elements.

- **Containers:** Square corners suggest rigidity and unyielding protection.
- **Buttons:** Sharp edges with 1px borders.
- **Exceptions:** Very small UI indicators (like status pips or radio toggles) may use circular shapes to distinguish them from structural layout elements.

## Components

- **Buttons:** Primary buttons feature a 1px Neon Green border and Pure White text. On hover, they gain a subtle Neon Green outer glow (`0px 0px 12px rgba(0, 255, 65, 0.4)`). Secondary buttons are Ghost-style with 1px White borders.
- **Glass Cards:** The signature component. Used for data visualization and profile summaries. Must include the `backdrop-filter: blur()` property and a 1px border.
- **Status Indicators:** Use a pulse animation for the Neon Green "Active" state. This provides a tactile "heartbeat" to the UI, signaling the firm is constantly monitoring.
- **Input Fields:** Minimalist under-line inputs or full-box outlines with JetBrains Mono for placeholder text. The cursor should be a solid Neon Green block.
- **Security Shields (Custom Component):** Large-scale SVG icons representing the protection status of specific assets (e.g., Home, Yacht, Digital Assets), using thin 0.5pt to 1pt stroke weights.
- **Data Visualization:** Charts should use thin Neon Green lines with a gradient fill that fades into the Deep Space Black background. No grid lines, only essential data points.