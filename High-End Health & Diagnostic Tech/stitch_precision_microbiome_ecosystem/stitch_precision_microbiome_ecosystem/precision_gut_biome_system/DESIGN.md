---
name: Precision Gut-Biome System
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#45483c'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#52652a'
  primary: '#33450d'
  on-primary: '#ffffff'
  primary-container: '#4a5d23'
  on-primary-container: '#bed58e'
  inverse-primary: '#b8cf88'
  secondary: '#725a39'
  on-secondary: '#ffffff'
  secondary-container: '#fbdbb0'
  on-secondary-container: '#765f3d'
  tertiary: '#3e403c'
  on-tertiary: '#ffffff'
  tertiary-container: '#555753'
  on-tertiary-container: '#ccccc8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4eca2'
  primary-fixed-dim: '#b8cf88'
  on-primary-fixed: '#141f00'
  on-primary-fixed-variant: '#3b4d14'
  secondary-fixed: '#feddb3'
  secondary-fixed-dim: '#e1c299'
  on-secondary-fixed: '#281801'
  on-secondary-fixed-variant: '#584324'
  tertiary-fixed: '#e3e3de'
  tertiary-fixed-dim: '#c6c7c2'
  on-tertiary-fixed: '#1a1c19'
  on-tertiary-fixed-variant: '#454744'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
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
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system establishes a visual language at the intersection of biological vitality and laboratory precision. The brand personality is authoritative yet empathetic—positioning advanced microbiome science as an accessible, high-end wellness experience. 

The aesthetic strategy employs a sophisticated **Soft-UI Neumorphism** approach. Unlike traditional flat medical interfaces, this system uses subtle light and shadow to create a tactile, "living" interface that mimics the soft, organic structures of the human body. This is balanced by a **Technical Minimalism** layout, ensuring that complex digestive data remains legible, structured, and clinically reliable. The emotional response is one of calm confidence, scientific rigor, and natural harmony.

## Colors

The palette is rooted in an "Organic-Tech" spectrum. **Moss Green (#4A5D23)** serves as the primary action color, representing growth and biological health. **Sand (#D2B48C)** provides a warm, humanizing secondary tone used for softer accents and grounding elements. 

The interface relies heavily on a background base of slightly desaturated Sand (#F0EDE4) to facilitate the neumorphic effect. Pure **White (#FFFFFF)** is reserved for light-source highlights on extruded elements and high-contrast surfaces. Typography and technical data points utilize a deep charcoal neutral to maintain surgical legibility without the harshness of pure black.

## Typography

The typographic hierarchy reinforces the "Organic & Technical" duality. **Space Grotesk** is used for headlines and data points, providing a geometric, futuristic character that suggests precision and innovation. 

**Manrope** is the workhorse for body copy and UI labels. Its balanced, modern proportions ensure maximum readability for medical descriptions and user instructions. By pairing the slightly eccentric terminals of Space Grotesk with the refined stability of Manrope, the design system achieves a high-end editorial feel suitable for a premium medical-tech product.

## Layout & Spacing

The design system utilizes a **Fixed Grid** model within a flexible container. A 12-column system is used for desktop views to organize technical data visualizations, while a simplified 4-column grid handles mobile layouts. 

Spacing is generous to evoke a sense of clinical "air" and premium quality. The rhythm is based on an 8px scale, but emphasizes larger "macro-spaces" (48px+) between distinct biological data sections to prevent cognitive overload. Organic shapes often break the grid slightly—such as background "blobs" that bleed off the edges—to maintain the soft, biological narrative.

## Elevation & Depth

Depth in this design system is achieved through **Soft-UI Neumorphism**. Surfaces are not layered with traditional drop shadows; instead, they appear to be pushed out from or pressed into the background material.

- **Extruded Elements (Cards/Buttons):** These feature a dual-shadow technique. A light shadow (White) on the top-left and a soft, muted Sand-tinted shadow on the bottom-right.
- **Inverted Elements (Inputs/Selected States):** These use internal shadows to create a "pressed" effect, suggesting a physical interaction with the interface.
- **Micro-shadows:** For technical charts, very thin, low-opacity Moss Green shadows are used to lift active data points without breaking the soft aesthetic.

## Shapes

The shape language is defined by "Organic Precision." While the layout follows a structured grid, the containers themselves use a **Rounded (Level 2)** profile. 

Primary UI containers use a 1rem (16px) corner radius to feel approachable. Interactive elements like pill-buttons utilize a fully rounded 3rem radius. To further the gut-biome narrative, the design system incorporates "Super-ellipses" and non-perfect "blob" shapes for background decorative elements and image masks, mimicking the microscopic view of cellular life.

## Components

### Buttons
Buttons appear as extruded "Soft-UI" surfaces. The primary button uses Moss Green text on a Sand-colored extruded surface. On hover, the extrusion "compresses" slightly. The active/pressed state uses an inset shadow to appear physically pushed into the UI.

### Cards & Containers
Cards should have the same background color as the main canvas (#F0EDE4) to allow the neumorphic light and dark shadows to create the illusion of depth. They are the primary vehicle for grouping health metrics.

### Input Fields
Inputs are styled as "inset" wells. The background is slightly darker than the surface, with a subtle inner shadow on the top and left edges, suggesting a carved space for user data.

### Progress & Health Gauges
These utilize organic, "liquid" fills in Moss Green. Unlike standard rectangular bars, progress indicators should have rounded, bulbous ends to maintain the biological theme.

### Chips & Tags
Technical tags for microbiome species or digestive markers use a Moss Green stroke with a transparent background, utilizing a technical monospaced-style weight from Space Grotesk.

### Data Visualizations
Charts avoid sharp angles. Line graphs use smoothed Bezier curves. Bar charts feature heavily rounded caps. The Moss Green and Sand colors are used to denote healthy vs. neutral ranges, with high-contrast charcoal for the axis labels.