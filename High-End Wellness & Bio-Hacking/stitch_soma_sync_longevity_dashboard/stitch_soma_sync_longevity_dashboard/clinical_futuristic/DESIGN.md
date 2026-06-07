---
name: Clinical-Futuristic
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#434654'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737685'
  outline-variant: '#c3c6d6'
  surface-tint: '#0c56d0'
  primary: '#003d9b'
  on-primary: '#ffffff'
  primary-container: '#0052cc'
  on-primary-container: '#c4d2ff'
  inverse-primary: '#b2c5ff'
  secondary: '#285ab9'
  on-secondary: '#ffffff'
  secondary-container: '#709bfe'
  on-secondary-container: '#003179'
  tertiary: '#374559'
  on-tertiary: '#ffffff'
  tertiary-container: '#4e5c71'
  on-tertiary-container: '#c6d4ed'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b2c5ff'
  on-primary-fixed: '#001848'
  on-primary-fixed-variant: '#0040a2'
  secondary-fixed: '#d9e2ff'
  secondary-fixed-dim: '#b1c6ff'
  on-secondary-fixed: '#001946'
  on-secondary-fixed-variant: '#00419d'
  tertiary-fixed: '#d5e3fd'
  tertiary-fixed-dim: '#b9c7e0'
  on-tertiary-fixed: '#0d1c2f'
  on-tertiary-fixed-variant: '#3a485c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Space Grotesk
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  data-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-value:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 32px
  max_width: 1440px
---

## Brand & Style
The design system embodies a "Clinical-Futuristic" aesthetic, positioning the platform as a high-precision medical instrument for longevity science. It targets a sophisticated audience of biohackers and health-conscious professionals who value data-driven insights over emotional marketing.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. It utilizes ultra-clean, high-density layouts reminiscent of laboratory equipment interfaces. Surfaces are treated with frosted-glass effects to imply depth and transparency, while rigid alignment and microscopic precision in UI elements evoke a sense of professional reliability and scientific rigor.

## Colors
This design system utilizes a restricted, high-signal palette to maintain a sterile, laboratory-grade environment. 

- **Primary & Secondary:** Laboratory Blues are used exclusively for interactive states, primary actions, and data-critical highlights.
- **Surface:** Sterile White (#F8FAFC) serves as the base canvas, providing a crisp, non-distracting background.
- **Accents:** Deep Slate (#334155) is used for high-contrast typography and structural borders to ground the lighter elements.
- **Functional:** Status colors (Red/Green) are highly desaturated until active, ensuring they do not break the sterile aesthetic unless immediate attention is required.

## Typography
The typography strategy leverages three distinct typefaces to separate hierarchy and intent:
1. **Headlines (Space Grotesk):** A technical, geometric sans-serif used for branding and major section headings to reinforce the futuristic tone.
2. **Body (Inter):** A neutral, highly legible sans-serif for all instructional text and clinical descriptions, ensuring no fatigue during long reading sessions.
3. **Data & Labels (JetBrains Mono):** A monospaced font used for precise metrics, timestamps, and laboratory values to imply mathematical accuracy. 

All text should be rendered with high contrast against the background, using Slate for maximum legibility.

## Layout & Spacing
The design system employs a **fixed-grid** system optimized for high-density information. 

- **Grid:** A 12-column grid with narrow 16px gutters to maximize horizontal real estate for complex data tables and charts.
- **Rhythm:** A strict 4px baseline grid governs all vertical spacing, ensuring that even dense displays feel intentional and structured.
- **Density:** Information density is high. Use padding sparingly within cards to allow as much data "above the fold" as possible, while maintaining external margins to prevent visual clutter at the screen edges.

## Elevation & Depth
Depth is communicated through material properties rather than traditional shadows.

1. **Base:** The primary background is the solid Sterile White.
2. **Glass Layers:** All cards and panels use a "Frosted Glass" effect: `backdrop-filter: blur(20px)` with a background opacity of 70-80%. 
3. **Borders:** Instead of shadows, use "Ghost Borders"—1px solid outlines in a very light Slate or Blue with 10-15% opacity. This defines the container without adding visual weight.
4. **Active Elevation:** When an element is focused or hovered, increase the border opacity and apply a very soft, subtle Primary Blue outer glow (`box-shadow`) to simulate a powered-on state.

## Shapes
The shape language is "Soft-Technical." Elements use a very small corner radius (4px) to retain a crisp, clinical feel while avoiding the harshness of true sharp corners. 

- **Standard Elements:** 4px radius for buttons, input fields, and small cards.
- **Large Containers:** 8px radius for main dashboard modules.
- **Data Points:** Circles for chart nodes and status indicators to provide a soft contrast to the otherwise rectangular grid.

## Components

### Interactive Health Charts & Gauges
- **Charts:** Use thin, 1.5pt strokes for line graphs. Grid lines should be faint (5% opacity Slate). Data points should glow slightly when hovered.
- **Gauges:** Circular "High-Fidelity" gauges with dual-rings. The inner ring represents the baseline; the outer ring represents the current biometric delta.

### High-Density Data Tables
- **Styling:** No row backgrounds; use 1px horizontal dividers only. 
- **Typography:** Use the `data-label` and `data-value` tokens. 
- **Alignment:** Numbers must be right-aligned and tabular-lining to allow for easy vertical scanning of metrics.

### Glass Buttons
- **Primary:** Solid Laboratory Blue with white text. No gradient.
- **Secondary:** Ghost style—1px Primary Blue border, transparent background, Primary Blue text.
- **Action Feedback:** On click, a momentary "pulse" effect using a light blue overlay.

### Input Fields
- **Design:** Bottom-border only or very light four-sided border. Labels use `data-label` style and are positioned above the field. Focused fields transition the border to a 2px Laboratory Blue line.

### Health Chips
- **Usage:** For tagging biomarkers (e.g., "Glucose," "Cortisol").
- **Style:** Small, `rounded-xl`, with a light Blue tint background (10% opacity) and Primary Blue text.