---
name: ClimateResilient Style
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#42483f'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#73796f'
  outline-variant: '#c2c8bc'
  surface-tint: '#43673d'
  primary: '#34562e'
  on-primary: '#ffffff'
  primary-container: '#4b6f44'
  on-primary-container: '#c7f0bb'
  inverse-primary: '#a9d19e'
  secondary: '#555f70'
  on-secondary: '#ffffff'
  secondary-container: '#d6e0f4'
  on-secondary-container: '#596374'
  tertiary: '#005479'
  on-tertiary: '#ffffff'
  tertiary-container: '#006d9c'
  on-tertiary-container: '#cee9ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c4eeb8'
  primary-fixed-dim: '#a9d19e'
  on-primary-fixed: '#012202'
  on-primary-fixed-variant: '#2c4f27'
  secondary-fixed: '#d9e3f7'
  secondary-fixed-dim: '#bdc7db'
  on-secondary-fixed: '#121c2a'
  on-secondary-fixed-variant: '#3d4757'
  tertiary-fixed: '#c9e6ff'
  tertiary-fixed-dim: '#89ceff'
  on-tertiary-fixed: '#001e2f'
  on-tertiary-fixed-variant: '#004c6e'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is anchored in the intersection of environmental stewardship and high-precision financial technology. It evokes a sense of unwavering reliability and proactive protection. The brand personality is authoritative yet accessible, positioning the platform as a sophisticated tool for managing planetary risks.

The visual style follows a **Modern Corporate** aesthetic with subtle **Glassmorphism** accents. This approach uses clean, structured layouts to convey professionalism, while translucent layers and soft depth effects represent the fluid, ever-changing nature of weather data. The interface prioritizes clarity and high-performance density, ensuring that complex parametric triggers and global catastrophe data remain legible and actionable for insurance professionals and agricultural stakeholders.

## Colors

The palette is derived from the natural world but refined for a digital, data-heavy environment.

- **Moss Green (Primary):** Used for primary actions, success states, and growth indicators. It reinforces the connection to agriculture and ecological resilience.
- **Storm Grey (Secondary/Neutral):** The foundation of the UI. It provides the professional "weight" required for a financial platform, used for text, borders, and structural elements.
- **Sky Blue (Accent/Data):** Reserved for atmospheric data points, weather event highlights, and interactive data visualizations. It provides a sharp contrast to the earthy primary tones.
- **Backgrounds:** A clean, slightly cool-tinted neutral base ensures high contrast for data visualization.

## Typography

The design system employs a dual-font strategy to balance character with utility. **Manrope** is used for headlines to provide a modern, refined, and trustworthy feel. **Inter** is used for all functional UI elements, body text, and data displays due to its exceptional legibility at small sizes and its systematic, neutral tone.

For data-heavy dashboards, a "Data Mono" style (Inter with specific tracking) is used to ensure numerical values are easy to scan and compare. Hierarchy is established through weight and purposeful use of Storm Grey to distinguish between primary information and metadata.

## Layout & Spacing

The design system utilizes a **12-column fluid grid** for desktop and a single-column fluid stack for mobile devices. The layout philosophy centers on "Data Densification"—maximizing information without cluttering the viewport.

Spacing follows an 8px rhythmic scale. Gutters are kept wide (24px) to provide visual breathing room between complex data cards. On mobile, margins are reduced to 16px to maximize the screen real estate for real-time charts and maps. Components should use generous internal padding (MD scale) to maintain the professional, high-end feel.

## Elevation & Depth

Depth is conveyed through **Ambient Shadows** and **Tonal Layers**. Instead of harsh black shadows, this design system uses soft, diffused shadows tinted with Storm Grey to create a natural, atmospheric lift.

1.  **Level 0 (Base):** The main canvas, using the lightest neutral tint.
2.  **Level 1 (Cards):** White surfaces with a subtle 1px border and a low-opacity, wide-spread shadow.
3.  **Level 2 (Overlays/Modals):** Increased shadow spread and a backdrop blur (glassmorphism) to maintain context of the underlying weather data.
4.  **Level 3 (Interactive):** Active states on buttons or cards use a subtle "glow" effect using the Primary Moss Green or Sky Blue to indicate focus.

## Shapes

The design system uses a **Rounded** shape language to soften the technical nature of the data. Standard UI components like buttons and input fields use a 0.5rem (8px) corner radius. 

Larger containers and dashboard cards utilize the `rounded-lg` (16px) or `rounded-xl` (24px) settings to create a friendly, accessible silhouette. This roundedness is contrasted by the precise, linear nature of the data charts, creating a balance between organic resilience and technical accuracy.

## Components

### Buttons & Inputs
Buttons feature solid fills for primary actions (Moss Green) and ghost styles for secondary actions. Inputs use Storm Grey for borders with a high-contrast focus state in Sky Blue. All touch targets on mobile must maintain a minimum height of 48px.

### Cards & Data Visualization
Cards are the primary container for parametric data. They should include header areas for weather-related icons (isobar lines, sunbursts, leaf icons). Data visualizations—line charts, heatmaps, and radial gauges—should utilize the Sky Blue for "Current Data" and Moss Green for "Target/Safe Zones."

### Chips & Status Indicators
Status chips use low-saturation backgrounds with high-saturation text. For example, a "Resilient" status uses a light Moss Green tint with dark Moss Green text. Weather alerts use Sky Blue to differentiate from standard error/success states.

### Weather Icons
Icons must be custom-drawn with a consistent 2px stroke weight. They should focus on agricultural motifs (crops, soil moisture) and meteorological symbols (pressure systems, precipitation types), avoiding overly playful or rounded "app-store" styles in favor of technical precision.