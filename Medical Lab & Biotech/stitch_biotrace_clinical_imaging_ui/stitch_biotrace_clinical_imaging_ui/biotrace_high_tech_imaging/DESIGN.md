---
name: BioTrace High-Tech Imaging
colors:
  surface: '#13121b'
  surface-dim: '#13121b'
  surface-bright: '#393842'
  surface-container-lowest: '#0e0d16'
  surface-container-low: '#1b1b24'
  surface-container: '#1f1f28'
  surface-container-high: '#2a2933'
  surface-container-highest: '#35343e'
  on-surface: '#e4e1ee'
  on-surface-variant: '#c7c4d8'
  inverse-surface: '#e4e1ee'
  inverse-on-surface: '#302f39'
  outline: '#918fa1'
  outline-variant: '#464555'
  surface-tint: '#c3c0ff'
  primary: '#c3c0ff'
  on-primary: '#1d00a5'
  primary-container: '#4f46e5'
  on-primary-container: '#dad7ff'
  inverse-primary: '#4d44e3'
  secondary: '#b3c8e9'
  on-secondary: '#1c314b'
  secondary-container: '#364a65'
  on-secondary-container: '#a5bada'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#5f6060'
  on-tertiary-container: '#dbdbdb'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2dfff'
  primary-fixed-dim: '#c3c0ff'
  on-primary-fixed: '#0f0069'
  on-primary-fixed-variant: '#3323cc'
  secondary-fixed: '#d3e3ff'
  secondary-fixed-dim: '#b3c8e9'
  on-secondary-fixed: '#041c35'
  on-secondary-fixed-variant: '#344863'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#13121b'
  on-background: '#e4e1ee'
  surface-variant: '#35343e'
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
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
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
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  container-max: 1440px
  gutter: 24px
---

## Brand & Style

This design system centers on the concept of "Illuminated Precision." It is engineered for a clinical diagnostic environment where clarity, speed of interpretation, and technical authority are paramount. The brand personality is clinical yet visionary, balancing the cold reliability of medical instrumentation with the high-energy pulse of digital innovation.

The aesthetic merges **High-Contrast Modernism** with **Technical Glassmorphism**. Dark, immersive backgrounds provide the "void" necessary for medical imagery to stand out, while Electric Indigo accents act as data conduits, guiding the eye to critical information. The style utilizes crisp, hairline borders and subtle luminescence to mimic the interface of high-end diagnostic hardware.

## Colors

The palette is anchored in a "Deep Dark" mode to minimize eye strain during long diagnostic sessions and to maximize the dynamic range of imaging results.

- **Midnight Blue (#001730):** The primary structural color. Used for sidebars, containers, and deep backgrounds to provide a stable, professional foundation.
- **Electric Indigo (#4F46E5):** The "Action" color. It represents energy and data flow. Use this for primary interactions, active states, and critical data highlights.
- **Silver (#C0C0C0):** The "Instrumental" color. Used for secondary text, icons, and borders to provide a metallic, high-tech feel.
- **Base Background (#000B18):** A darker variant of Midnight Blue used for the lowest canvas layer to create depth.

## Typography

The typography strategy focuses on the intersection of technical geometry and legibility.

- **Space Grotesk** is used for headlines. Its geometric construction evokes a futuristic, scientific feel.
- **Inter** is utilized for all functional text. Its neutral, systematic nature ensures that complex patient data remains highly readable across various screen sizes.
- **Monospaced Data:** For coordinates, timestamps, and diagnostic values, a monospaced font is used to ensure vertical alignment of digits, facilitating quick comparison.

## Layout & Spacing

This design system uses a strict **8px grid system** to maintain mathematical rigor. The layout follows a **Fixed-Fluid Hybrid** model:
- **Sidebars & Control Panels:** Fixed width (280px - 320px) to ensure diagnostic tools are always in the same position.
- **Imaging Viewport:** Fluid, expanding to utilize all remaining screen real estate.
- **Gutters:** Standardized at 24px to provide enough breathing room between high-density data panels.
- **Margins:** 32px or 40px at the screen edges to frame the content like a premium piece of medical equipment.

## Elevation & Depth

Depth in this design system is created through **Luminosity and Translucency** rather than traditional drop shadows.

- **The Canvas:** The lowest layer is the Midnight Blue background.
- **Glass Panels:** Content areas use a "Glassmorphism" effect: a semi-transparent surface (Midnight Blue at 60% opacity) with a `20px` backdrop blur and a `1px` border of Silver at 15% opacity.
- **Active Elevation:** When an element is focused or elevated, it gains an "Inner Glow" (Electric Indigo) and the border opacity increases.
- **Illumination:** Critical alerts or primary buttons use a soft outer glow (`box-shadow: 0 0 15px rgba(79, 70, 229, 0.4)`) to simulate a backlit LED display.

## Shapes

The shape language is "Soft-Technical." Elements use small corner radii to feel modern and engineered without becoming overly organic or "friendly."

- **Standard Elements:** 4px radius (`rounded-sm`). Used for inputs, buttons, and small cards.
- **Main Containers:** 8px radius (`rounded-md`). Used for primary diagnostic modules.
- **Inner Accents:** 0px (Sharp). Used for data bars, progress fills, and separators to maintain a "scientific" look.

## Components

### Buttons
- **Primary:** Electric Indigo background, white text, 4px radius. On hover, apply a 10px Electric Indigo outer glow.
- **Secondary:** Transparent background, 1px Silver border. Text is Silver.
- **Ghost:** No background or border. Text is Silver, turns Electric Indigo on hover.

### Input Fields
- Dark Midnight Blue background with a 1px Silver border (20% opacity).
- On focus, the border turns Electric Indigo and an inner 2px glow is applied.
- Labels are always positioned above the field in `label-caps` style.

### Cards & Modules
- Use the Glassmorphism specification from the Elevation section.
- Headers within cards should have a 1px Silver bottom border at 10% opacity.

### Diagnostic Specifics
- **Status Chips:** High-contrast pills (e.g., "Critical" in red, "Stable" in green) with a subtle background tint and 100% saturated text.
- **Data Tables:** Zebra-striping is avoided. Instead, use 1px horizontal Silver separators at 5% opacity.
- **Crosshair/Markers:** 1px Electric Indigo lines for marking coordinates on scans, ensuring they are visible against grayscale medical images.