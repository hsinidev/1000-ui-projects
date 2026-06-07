---
name: Bio-Fence Tactical System
colors:
  surface: '#0d141b'
  surface-dim: '#0d141b'
  surface-bright: '#333a42'
  surface-container-lowest: '#080f16'
  surface-container-low: '#151c24'
  surface-container: '#192028'
  surface-container-high: '#242b33'
  surface-container-highest: '#2e353e'
  on-surface: '#dce3ee'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#dce3ee'
  inverse-on-surface: '#2a3139'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c1c8ca'
  on-secondary: '#2b3234'
  secondary-container: '#434a4c'
  on-secondary-container: '#b2babc'
  tertiary: '#bfc6db'
  on-tertiary: '#293041'
  tertiary-container: '#9199ad'
  on-tertiary-container: '#2a3142'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#dde4e6'
  secondary-fixed-dim: '#c1c8ca'
  on-secondary-fixed: '#161d1f'
  on-secondary-fixed-variant: '#41484a'
  tertiary-fixed: '#dbe2f8'
  tertiary-fixed-dim: '#bfc6db'
  on-tertiary-fixed: '#141c2b'
  on-tertiary-fixed-variant: '#3f4758'
  background: '#0d141b'
  on-background: '#dce3ee'
  surface-variant: '#2e353e'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-xs:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1440px
  card-padding: 24px
---

## Brand & Style

The design system is engineered to project absolute reliability, technical precision, and high-security authority. It serves a dual purpose: providing peace of mind to pet owners through robust invisible fencing and delivering deep, actionable insights through pet activity tracking.

The visual style is **High-Contrast Dark Mode**, blending elements of **Corporate Modern** with **Technical Industrialism**. The aesthetic is defined by "Tactile Precision"—where every element feels intentional and mission-critical. Key visual identifiers include glowing vector lines that represent GPS boundaries, semi-transparent overlays for telemetry data, and a sense of "physical robustness" conveyed through thick borders and deliberate structural weights. The user should feel like they are operating a professional-grade security terminal rather than a consumer app.

## Colors

The palette for this design system is rooted in high-visibility safety and deep-space technicality.

*   **Midnight Blue (#0A1221):** The foundation. Used for primary backgrounds to minimize eye strain and provide a canvas where "glowing" elements can pop.
*   **Safety Orange (#FF6B00):** The primary driver for action and awareness. This is used for critical alerts, GPS boundary lines, primary buttons, and active state indicators.
*   **Graphite (#2D3436):** Used for structural elements, secondary cards, and surface backgrounds to create depth without losing the dark-mode aesthetic.
*   **Technical Accents:** Neutral tones are pushed toward cooler grays to maintain the "security" feel, while high-alert states may utilize a secondary pulse of the primary orange.

## Typography

Typography in this design system prioritizes data density and rapid legibility. 

**Space Grotesk** is utilized for headlines and primary UI anchors, providing a geometric, futuristic character that reinforces the technical nature of the product. **Geist** is employed for body copy, system labels, and data visualization; its monospaced-adjacent metrics make it ideal for displaying GPS coordinates, battery percentages, and time stamps. 

Text is often presented in high contrast against the Midnight Blue background, with labels frequently utilizing uppercase styling and increased letter spacing to mimic aerospace instrumentation.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for desktop and tablet, conforming to a 12-column structure to ensure data alignment across dense dashboards. On mobile, it shifts to a fluid 4-column layout with generous 24px side margins to accommodate one-handed operation during outdoor tracking.

The spacing rhythm is based on a 4px base unit. Visual groups are separated by clear 24px gutters to prevent information overload. Data-heavy sections (like activity logs) utilize a tighter vertical rhythm to maximize visible information, while safety-critical controls (like "Deactivate Fence") are given significant clear space to prevent accidental triggers.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layers** and **Vector Glows** rather than traditional soft shadows.

1.  **Base Layer:** Midnight Blue (#0A1221).
2.  **Surface Layer:** Graphite (#1C1F26), used for primary cards and containers.
3.  **Interactive Layer:** Semi-transparent Graphite with a 1px inner stroke to define edges.
4.  **Critical Layer:** Elements that require immediate attention (like an active breach alert) utilize a 2px Safety Orange border with a subtle outer "glow" (a high-blur, low-opacity drop shadow in the same orange) to simulate an illuminated physical warning light.

Semi-transparent overlays (blurs of 12px to 20px) are used for mobile navigation and modal backgrounds to maintain the technical "glass" feel of a high-tech HUD.

## Shapes

The shape language combines "Robust Softness." While the primary UI cards use a **Level 2 (0.5rem)** roundedness to feel modern and accessible, this is often contrasted by **sharp 90-degree internal angles** in data visualizations and decorative vector "corner brackets" that frame the UI.

This juxtaposition creates a "ruggedized" feel—similar to hardware designed for the field. Buttons and interactive chips follow the standard roundedness, while status indicators and "Danger Zone" alerts use thicker, 3px borders to emphasize their weight and importance.

## Components

### Buttons & CTAs
Primary buttons are solid Safety Orange with black text for maximum contrast. Secondary buttons are outlined in Graphite with a subtle hover-glow. All buttons feature a minimum height of 48px to ensure tactile reliability in outdoor conditions.

### Alert Cards
Alert cards are the cornerstone of the system. In a breach state, these cards transition from Graphite to having a 3px Safety Orange border. They utilize the "Display" typography for immediate recognition of the status (e.g., "BREACH DETECTED").

### GPS Mapping Interface
The map is a customized dark-mode vector tile set. "Invisible Fence" lines are rendered as glowing Safety Orange vectors. Pet icons are high-contrast white circles with a persistent "pulse" animation when active tracking is engaged.

### Activity Chips
Small, Graphite-filled pills with monospaced Geist labels. These categorize pet movements (e.g., "RESTING," "RUNNING," "STRAYING").

### Input Fields
Inputs are deep-inset Graphite boxes with 1px Graphite borders that transition to Safety Orange when focused. They utilize a monospace-leaning font for numerical data entry (coordinates, radius distance).

### Telemetry Lists
Lists of activity history use alternating tonal rows (Midnight Blue vs. a slightly lighter Graphite tint) to maintain readability across long data sets without the need for horizontal divider lines.