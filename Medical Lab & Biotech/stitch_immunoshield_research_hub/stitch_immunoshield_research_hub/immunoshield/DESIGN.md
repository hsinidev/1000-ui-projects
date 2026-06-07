---
name: ImmunoShield
colors:
  surface: '#f4fafa'
  surface-dim: '#d5dbdb'
  surface-bright: '#f4fafa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff5f5'
  surface-container: '#e9efef'
  surface-container-high: '#e3e9e9'
  surface-container-highest: '#dde4e4'
  on-surface: '#161d1d'
  on-surface-variant: '#3f4947'
  inverse-surface: '#2b3232'
  inverse-on-surface: '#ecf2f2'
  outline: '#6f7977'
  outline-variant: '#bec9c7'
  surface-tint: '#136964'
  primary: '#136964'
  on-primary: '#ffffff'
  primary-container: '#80cbc4'
  on-primary-container: '#005652'
  inverse-primary: '#89d4cd'
  secondary: '#516161'
  on-secondary: '#ffffff'
  secondary-container: '#d4e6e5'
  on-secondary-container: '#576867'
  tertiary: '#ba1a20'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffa79f'
  on-tertiary-container: '#9e0012'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#a4f0e9'
  primary-fixed-dim: '#89d4cd'
  on-primary-fixed: '#00201e'
  on-primary-fixed-variant: '#00504b'
  secondary-fixed: '#d4e6e5'
  secondary-fixed-dim: '#b8cac9'
  on-secondary-fixed: '#0e1e1e'
  on-secondary-fixed-variant: '#3a4a49'
  tertiary-fixed: '#ffdad6'
  tertiary-fixed-dim: '#ffb3ac'
  on-tertiary-fixed: '#410003'
  on-tertiary-fixed-variant: '#930010'
  background: '#f4fafa'
  on-background: '#161d1d'
  surface-variant: '#dde4e4'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  code-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  xxl: 48px
  cytoplasmic-margin: 64px
---

## Brand & Style

The design system is centered on the concept of "Biological Precision." It aims to bridge the gap between sterile clinical data and the fluid, organic nature of immunology. The brand personality is authoritative yet approachable, evoking a sense of microscopic exploration and defensive resilience.

The UI style utilizes a sophisticated blend of **Minimalism** and **Glassmorphism**. By employing translucent layers and frosted effects, the interface mimics biological membranes, creating a sense of depth and interconnectedness. This approach ensures that complex scientific data feels lightweight and navigable rather than overwhelming. The emotional response is one of calm, professional trust, and technological advancement.

## Colors

The palette is designed to maintain a high level of clinical cleanliness while acknowledging the biological subject matter. 

- **Primary Backgrounds:** Use the Soft Teal (#E0F2F1) as the base foundation for the application. It provides a calming, non-white sterile environment that reduces eye strain.
- **Action & Accent:** The deeper Teal (#80CBC4) serves as the primary action color for buttons, active states, and structural accents.
- **Clinical Surfaces:** Pure White (#FFFFFF) is reserved exclusively for data cards and primary surfaces to ensure maximum contrast for legibility.
- **Critical Alerts:** Blood-Red (#D32F2F) is used sparingly but impactfully. It is strictly reserved for critical data points, high-risk immunological alerts, and destructive actions to ensure immediate user attention.

## Typography

The design system utilizes **Inter** for all typographic needs to ensure maximum scannability of dense clinical datasets. The typeface choice emphasizes functional, systematic clarity.

Headlines should use tighter letter spacing and heavier weights to create a strong visual anchor on the page. For body text, generous line heights are implemented to assist in the reading of long-form laboratory reports and patient histories. Labels and metadata should utilize a slightly increased letter spacing and uppercase styling to distinguish them from actionable data.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model to accommodate various data densities and screen sizes used in clinical environments. A 12-column system is standard, with 24px gutters.

Spacing is defined by a "Cytoplasmic Rhythm," where core content is surrounded by generous margins to prevent the UI from feeling claustrophobic. Elements should be grouped into logical "clusters" (mimicking cellular organelles) using consistent padding. Use larger spacing increments (xl and xxl) between major content sections to maintain the organic, airy aesthetic.

## Elevation & Depth

This design system uses **Glassmorphism** and **Ambient Shadows** to create a multi-layered biological hierarchy. 

Depth is achieved through backdrop blurs (ranging from 10px to 20px) on translucent surfaces. Shadows are never pure black; they are tinted with the primary teal color (e.g., #80CBC4 at 10% opacity) and feature large blur radii with minimal offsets. This creates a soft, diffused "glow" rather than a hard drop shadow, making components appear as if they are suspended in a fluid medium. High-priority cards should feature a subtle 1px semi-transparent white border to simulate a cell membrane catching light.

## Shapes

The shape language is strictly **Biomorphic**. To reflect the organic nature of immunology, the design system avoids sharp 90-degree angles entirely.

A base roundedness of 0.5rem (8px) is used for small components like inputs and chips. Primary cards and containers use 1rem (16px), while large "membrane" sections use 1.5rem (24px). For decorative elements or specialized iconography, asymmetric "blob" shapes may be used to enhance the cellular aesthetic, provided they do not interfere with the alignment of critical data.

## Components

- **Buttons:** Primary buttons feature a solid #80CBC4 fill with high rounded corners. Secondary buttons use a glassmorphic style with a translucent teal background and a 1px white border.
- **Cards:** The core data container. Cards must have a White (#FFFFFF) background with a 16px corner radius and a soft, teal-tinted ambient shadow.
- **Chips:** Used for "Cell Markers" or "Status Indicators." These should be pill-shaped with a soft teal or light-red tint depending on the data severity.
- **Input Fields:** Minimalist design with a Soft Teal background and a subtle bottom border that expands upon focus.
- **Lists:** Data lists should be separated by whitespace rather than hard lines, using subtle tonal changes in the background to define rows.
- **Bio-Visualizers:** Custom components that display cellular data should use the Blood-Red for critical outliers and shades of Teal for healthy ranges.
- **Translucent Overlays:** Modals and side panels must use a high-blur backdrop filter to maintain context of the underlying data while providing focus.