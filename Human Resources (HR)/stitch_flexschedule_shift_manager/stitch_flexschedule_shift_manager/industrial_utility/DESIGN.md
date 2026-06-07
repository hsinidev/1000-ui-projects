---
name: Industrial Utility
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#f9f5f5'
  on-tertiary: '#313030'
  tertiary-container: '#dcd9d9'
  on-tertiary-container: '#605f5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  numeral-xl:
    fontFamily: Space Grotesk
    fontSize: 56px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.04em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 20px
  touch-target-min: 48px
---

## Brand & Style

This design system is built for the high-stakes environment of workforce management, where clarity and speed of interaction are paramount. The brand personality is authoritative, reliable, and "heavy-duty." It avoids decorative flourishes in favor of a **High-Contrast / Industrial** aesthetic that draws inspiration from physical signage and machinery interfaces.

The target audience consists of operations managers and shift workers who require a "glanceable" UI that functions flawlessly under various lighting conditions and on mobile devices. The emotional response is one of confidence and structural integrity; the UI feels like a tool rather than just software.

## Colors

The palette is anchored in a high-visibility **Industrial Yellow** (#FFD700) set against a **Matte Black** (#1A1A1A) foundation. This combination creates an immediate hierarchy and signals "action" and "utility."

- **Primary:** Industrial Yellow is reserved for primary actions, active shift states, and critical notifications.
- **Surface:** Matte Black provides the base layer, reducing eye strain for night-shift workers.
- **Accents:** Pure White is used for high-readability text and secondary icons.
- **Semantic:** Specific shift types (e.g., Overtime, On-Call, Holiday) should utilize high-saturation status colors to distinguish between block types on a dense calendar view.

## Typography

The typography system prioritizes technical precision. **Space Grotesk** is used for headlines, numerals, and UI labels to provide a geometric, futuristic, and industrial feel. Its unique letterforms ensure that numbers—critical for shift times and durations—are instantly recognizable.

**Inter** is utilized for body copy and dense data tables to ensure maximum legibility and a neutral tone. Large scale numerals (`numeral-xl`) should be used for clock-in displays and remaining hours to ensure they are readable from a distance.

## Layout & Spacing

This design system utilizes a **Fixed Grid** for desktop (12-column) and a **Fluid Grid** for mobile. The rhythm is strictly based on a **4px baseline**, ensuring all elements align to a technical modularity.

Margins are generous to prevent accidental taps, especially on mobile devices where workers may be wearing gloves or moving quickly. Every interactive element must adhere to a minimum touch target of 48px. Layouts should prioritize vertical scanning, with clear horizontal dividers to separate shift entries.

## Elevation & Depth

To maintain the rugged, industrial aesthetic, this design system avoids soft shadows and "fuzzy" depth. Instead, it employs **Tonal Layers** and **Hard Borders**.

- **Level 0 (Base):** Matte Black (#1A1A1A).
- **Level 1 (Cards/Surface):** Dark Grey (#2A2A2A) with a 1px solid border (#3A3A3A).
- **Level 2 (Popovers/Modals):** Dark Grey (#2A2A2A) with a 2px solid Industrial Yellow border.
- **Active State:** Elements appear "pressed" by shifting 2px down and right, mimicking a physical mechanical button. 

Depth is communicated through color contrast and border weight rather than atmospheric shadows.

## Shapes

The shape language is **Sharp (0)**. There are no rounded corners in this design system. Every container, button, and input field uses 90-degree angles to reinforce the industrial, structural theme. This creates a "precision-tooled" look that distinguishes the platform from softer, consumer-grade applications.

## Components

- **Buttons:** Rectangular with no radius. Primary buttons use an Industrial Yellow background with Black text in bold caps. Secondary buttons use a white border with no fill.
- **Shift Blocks:** Rectangular blocks on the calendar grid. Use high-contrast left-border accents to denote shift types (e.g., Red for Urgent, Green for Confirmed).
- **Inputs:** Underlined or fully boxed with a thick 2px border. On focus, the border changes to Industrial Yellow. Labels sit above the input in `label-caps`.
- **Chips:** Small, rectangular tags with monochromatic fills and high-contrast text. No rounded corners.
- **Cards:** Used for shift summaries. They feature a "header bar" in a contrasting gray to separate metadata from the main content.
- **Status Indicators:** Large, geometric icons (Square or Diamond) instead of circles, maintaining the sharp-edged motif.
- **Time Picker:** A large-scale, high-contrast grid of numbers for rapid selection on mobile.