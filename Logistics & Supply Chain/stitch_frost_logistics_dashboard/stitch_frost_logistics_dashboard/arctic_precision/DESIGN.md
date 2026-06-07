---
name: Arctic Precision
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#3f4852'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#6f7883'
  outline-variant: '#bec7d4'
  surface-tint: '#00629d'
  primary: '#00629d'
  on-primary: '#ffffff'
  primary-container: '#00a3ff'
  on-primary-container: '#00375a'
  inverse-primary: '#98cbff'
  secondary: '#516072'
  on-secondary: '#ffffff'
  secondary-container: '#d2e1f7'
  on-secondary-container: '#556477'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#9a9d9f'
  on-tertiary-container: '#313536'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cfe5ff'
  primary-fixed-dim: '#98cbff'
  on-primary-fixed: '#001d33'
  on-primary-fixed-variant: '#004a77'
  secondary-fixed: '#d4e4fa'
  secondary-fixed-dim: '#b9c8de'
  on-secondary-fixed: '#0d1c2d'
  on-secondary-fixed-variant: '#39485a'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 24px
  gutter: 16px
---

## Brand & Style
The brand personality of the design system is clinical, reliable, and technologically advanced. It is built for logistics professionals who require absolute certainty in temperature-sensitive environments. The aesthetic prioritizes "visual cooling"—using a palette and material system that mimics ice, glass, and surgical steel to evoke a sense of preserved integrity.

The design style is a refined **Glassmorphism**, referred to as 'Frost'. Unlike decorative glassmorphism, this implementation focuses on legibility and data hierarchy. It utilizes semi-transparency to maintain spatial awareness of complex logistics maps and data streams, while using high-definition blurs to ensure text remains legible against dynamic backgrounds.

## Colors
The palette is restricted to a high-utility spectrum of Ice Blue, Silver, and White. 
- **Ice Blue (Primary):** Used for primary actions, active states, and data points within the "safe" temperature range.
- **Silver (Secondary):** Employed for structural elements, borders, and secondary metadata to mimic metallic industrial surfaces.
- **White (Tertiary/Background):** The base for the frosted panels, providing the "clean" surgical feel necessary for trust.
- **Semantic Colors:** Critical alerts break the cold palette with a sharp Red, while optimal status indicators use a cool Emerald Green to ensure immediate recognition in data-heavy views.

## Typography
The typography system uses a dual-font approach to balance technical precision with extreme legibility. 
- **Space Grotesk** is reserved for headlines and critical data readouts (like temperature and GPS coordinates). Its geometric, slightly futuristic construction reinforces the "tech-forward" nature of the design system.
- **Inter** handles all functional UI text and body copy. It is chosen for its neutral, systematic performance in data-dense tables and logistics logs.
- All labels for sensor data utilize an uppercase style with increased letter spacing to differentiate headers from live values.

## Layout & Spacing
The layout follows a **Fixed Grid** model for desktop dashboards and a **Fluid Grid** for mobile tracking interfaces. 
- A strict 4px baseline grid ensures that all glass panels and data cells align perfectly, conveying a sense of order and precision.
- **Gaps:** High-density views use 8px (sm) spacing, while spacious overview dashboards utilize 24px (lg) margins to allow the glassmorphic effects "room to breathe" without visual clutter.
- Content should be grouped into logical "modules" (cards) that span 3, 6, or 12 columns depending on the data priority.

## Elevation & Depth
Depth in the design system is communicated through "Frost" layers rather than traditional shadows.
- **Surface 1 (Base):** A clean, solid off-white or light silver background.
- **Surface 2 (The Frost Layer):** Semi-transparent white (#FFFFFF at 60-70% opacity) with a 20px - 40px backdrop blur. This is used for primary content cards.
- **Surface 3 (High Focus):** For modals or tooltips, use a higher transparency (#FFFFFF at 85%) with a subtle 1px inner stroke in pure white to simulate a "beveled glass" edge.
- **Borders:** All panels must have a 1px solid border in a very light silver (#E2E8F0) with low opacity to define the shape against the blurred background.

## Shapes
The shape language is "Soft" (0.25rem - 0.75rem) to maintain a professional, architectural feel. 
- Sharp corners are avoided to prevent a "harsh" industrial look, but overly pill-shaped elements are also excluded to maintain a serious, enterprise-grade tone.
- **Standard Cards:** Use 0.5rem (rounded-lg).
- **Buttons and Inputs:** Use 0.25rem (base roundedness) for a crisp, precise appearance.
- **Status Indicators:** Small 4px circles or squares with rounded corners provide high-visibility signals without distracting from numerical data.

## Components
- **Glassmorphic Cards:** The core container. Features a 1px white inner-border and a subtle outer-glow rather than a drop shadow. Backgrounds must be blurred to 20px minimum.
- **Status Indicators:** Use a "Glow" effect. An optimal temperature status should feature a green dot with a soft green outer pulse, suggesting "active monitoring."
- **Data Visualization:** Line charts should use "Ice Blue" for the primary metric. Shaded areas under the line should use a very faint blue-to-transparent gradient.
- **Buttons:** 
  - *Primary:* Solid Ice Blue with white text. No glass effect for maximum clickability.
  - *Secondary:* Ghost style with a silver border and frosted background on hover.
- **Inputs:** Semi-transparent with a 1px silver border that turns Ice Blue on focus.
- **Temperature Badges:** High-contrast capsules using Space Grotesk for the numerical value, ensuring visibility from a distance in warehouse settings.