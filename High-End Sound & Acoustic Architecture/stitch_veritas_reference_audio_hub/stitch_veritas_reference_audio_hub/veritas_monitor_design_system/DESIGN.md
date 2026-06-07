---
name: Veritas-Monitor Design System
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
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#f9f9f9'
  on-tertiary: '#2f3131'
  tertiary-container: '#dcdddd'
  on-tertiary-container: '#5f6161'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#72ff70'
  primary-fixed-dim: '#00e639'
  on-primary-fixed: '#002203'
  on-primary-fixed-variant: '#00530e'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: IBM Plex Sans
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: IBM Plex Sans
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: IBM Plex Sans
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: IBM Plex Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 1rem
    letterSpacing: 0.08em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  grid-columns: '12'
---

## Brand & Style

This design system is engineered for professional-grade monitoring environments where data integrity and visual precision are paramount. The aesthetic merges the clinical rigor of laboratory equipment with the refined tactility of high-end audio hardware. 

The brand personality is authoritative, transparent, and hyper-functional. It avoids decorative elements in favor of "Engineering-Grade" utility. The visual language is rooted in **Modern Minimalism** and **Technical Glassmorphism**, utilizing high-contrast layouts to ensure critical information is never obscured. Every pixel serves a diagnostic purpose, evoking the reliability of a physical rack-mounted oscilloscope or a calibrated studio monitor.

## Colors

The palette is strictly functional, optimized for low-fatigue monitoring in dark environments. 

- **Matte Black (#1A1A1A):** The primary surface color, providing a deep, non-reflective base that minimizes eye strain.
- **Pure White (#FFFFFF):** Reserved for primary data readouts and essential high-contrast labels.
- **Metallic Silver (#C0C0C0):** Used for structural elements, borders, and inactive states to simulate brushed aluminum hardware components.
- **Oscilloscope Green (#00FF41):** The sole functional accent. It represents "Active," "Normal," or "Signal." It should be used sparingly for data visualizations, status indicators, and primary action highlights.

The color system relies on high contrast ratios to maintain WCAG AAA standards for legibility in critical technical workflows.

## Typography

This design system utilizes **IBM Plex Sans** for its engineered, neutral character and excellent legibility in dense interfaces. **JetBrains Mono** is introduced for data readouts, status labels, and telemetry to reinforce the technical, "Engineering-Grade" aesthetic.

Typography is prioritized by data density. Headlines are restrained, while small-scale labels use uppercase tracking and monospaced digits to ensure that fluctuating numerical values do not cause layout shifts. All data-driven text should use tabular figures.

## Layout & Spacing

The layout follows a **Strict Fixed Grid** system based on a 4px base unit. 

- **Desktop:** 12-column grid with 16px gutters and 32px outer margins. Content modules are housed in rigid containers that align to the grid, mirroring the look of modular hardware.
- **Mobile:** 4-column grid with 16px margins.
- **Philosophy:** Whitespace is used as a functional separator rather than an aesthetic luxury. Alignment is always flush-left or flush-right; centered elements are avoided to maintain the technical "blueprint" feel.

Layouts should prioritize "Above the Fold" information density, minimizing scrolling in favor of dashboard-style visibility.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Technical Glassmorphism** rather than traditional shadows.

1.  **Base (Level 0):** Matte Black (#1A1A1A).
2.  **Raised Modules (Level 1):** Slight contrast shift or 1px Silver (#C0C0C0) border. No shadow.
3.  **Interactive Overlays (Level 2):** Semi-transparent glassmorphism. Use a backdrop blur (12px to 20px) with a 10% opacity white fill and a crisp 1px pure white border. This represents a "HUD" or "Glass Console" layer that sits above the primary diagnostic data.

Shadows are omitted entirely to maintain a flat, industrial look, ensuring that "light" never feels artificial or inconsistent with hardware expectations.

## Shapes

The shape language is strictly **Sharp (0px)**. 

Every component—from buttons to input fields to container cards—must feature 90-degree angles. This reinforces the "Clinical-Precision" aesthetic and allows for seamless tiling of complex data modules. Rounded corners are perceived as "consumer-friendly" and are therefore excluded to maintain a professional, industrial-grade tone.

## Components

### Buttons
- **Primary:** Oscilloscope Green background, Matte Black text, sharp edges. No gradients.
- **Secondary:** Transparent background, 1px Silver border, Silver text.
- **State:** On hover, primary buttons should flicker or "glow" (0.5 opacity green outer glow), simulating a backlit physical switch.

### Input Fields
- **Style:** Underline only or 1px Silver border on all sides. 
- **Typography:** JetBrains Mono for all user input to ensure character clarity (e.g., distinguishing 0 from O).
- **Active State:** Border transitions to Oscilloscope Green.

### Data Displays (Specialized Component)
- **Telemetry Cards:** High-contrast modules with a 1px Silver border. Use JetBrains Mono for large numerical values.
- **Status Indicators:** Small, sharp squares (4px x 4px). Green for "Sync," Grey for "Standby," and a high-contrast Red (#FF0000) for "Warning."

### Overlays & Menus
- Use the Glassmorphism style described in Elevation. High backdrop-blur ensures readability over dense underlying data grids.
- Selection indicators in menus must use a solid block of Oscilloscope Green behind the text.

### Progress Bars & Meters
- Segmented blocks (reminiscent of LED VU meters) instead of smooth continuous fills. Each segment represents a specific decibel or percentage threshold.