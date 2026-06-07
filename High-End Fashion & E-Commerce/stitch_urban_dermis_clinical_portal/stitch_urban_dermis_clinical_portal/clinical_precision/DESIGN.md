---
name: Clinical Precision
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
  on-surface-variant: '#424750'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#727781'
  outline-variant: '#c2c6d1'
  surface-tint: '#27609d'
  primary: '#003461'
  on-primary: '#ffffff'
  primary-container: '#004b87'
  on-primary-container: '#8abcff'
  inverse-primary: '#a3c9ff'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#003942'
  on-tertiary: '#ffffff'
  tertiary-container: '#00525d'
  on-tertiary-container: '#2fcbe3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e4ff'
  primary-fixed-dim: '#a3c9ff'
  on-primary-fixed: '#001c38'
  on-primary-fixed-variant: '#004882'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#a1efff'
  tertiary-fixed-dim: '#44d8f1'
  on-tertiary-fixed: '#001f25'
  on-tertiary-fixed-variant: '#004e59'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 48px
  gutter: 32px
  section-gap: 80px
  element-gap: 16px
---

## Brand & Style

This design system centers on a "Sterile-Chic" aesthetic, merging the authoritative rigor of clinical dermatology with the ethereal elegance of high-end luxury skincare. The visual language is defined by a sense of hyper-cleanliness, scientific transparency, and tactile softness.

The primary style is a sophisticated hybrid of **Neumorphism** and **Glassmorphism**. Neumorphic patterns provide a soft, "squishy" physical presence that feels organic and skin-like, while glassmorphism layers introduce a sense of clinical transparency and high-tech filtration. The overall emotional response should be one of profound trust, calm, and professional excellence.

## Colors

The palette is rooted in medical purity. The primary "Clinical Blue" is deep and authoritative, used sparingly for critical actions and branding. "Pure White" serves as the foundational surface color to maintain a sterile atmosphere. 

"Glass-Cyan" acts as a functional accent, representing hydration and advanced technology through translucent overlays. The background utilizes a very subtle off-white to allow the neumorphic light and dark shadows to create the necessary extrusions and indentations. Contrast is kept high for text readability but soft for structural elements to maintain the "Soft-UI" signature.

## Typography

This design system utilizes **Manrope** for its balanced, modern, and clinical geometry. The typography is scaled to ensure high readability and an editorial feel. 

Headlines are set with tighter letter-spacing to feel precise and impactful. Body text utilizes generous line-height to reinforce the "airy" feel requested in the design narrative. Small labels and metadata should be set in uppercase with increased tracking to mimic the labeling found on professional medical packaging.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to ensure a curated, premium experience that doesn't feel stretched or diluted. A 12-column system is used with wide gutters to provide maximum whitespace.

Margins are intentionally oversized to evoke the feeling of a luxury gallery or a high-end medical clinic. Information density is kept low; every element is given room to "breathe," reducing cognitive load and emphasizing the "sterile" aesthetic.

## Elevation & Depth

Hierarchy is achieved through a combination of neumorphic extrusions and glassmorphic layers. 

1.  **Neumorphic Bases:** Primary cards and containers use dual shadows. A light shadow (#FFFFFF) is applied to the top-left, and a soft dark shadow (#D1D9E6) is applied to the bottom-right. This creates a soft, tactile surface that appears to be molded from the background.
2.  **Glassmorphism Overlays:** Modals, navigation bars, and dropdowns use a "Glass-Cyan" tint with a heavy backdrop-blur (20px-30px). This suggests depth and transparency without breaking the sterile aesthetic.
3.  **Active States:** Interactive elements like buttons should appear "pressed" or "sunken" using inset shadows when engaged, providing a physical sense of feedback.

## Shapes

The design system employs **Rounded** corners (0.5rem base) to soften the clinical edge, making the interface feel approachable and human. While the lines are clean and precise, the avoidance of sharp 90-degree angles ensures the UI feels "Soft."

Larger containers like primary neumorphic cards use the `rounded-xl` (1.5rem) setting to emphasize their tactile, sculptural quality. Buttons and input fields follow the `rounded-lg` (1rem) standard for a modern, high-end feel.

## Components

### Buttons
Primary buttons are neumorphic extrusions with Clinical Blue text. Ghost buttons use a subtle Cyan border. All buttons transition to an "inset" shadow state on click to simulate a physical press.

### Cards
Cards are the centerpiece of this design system. They must be the same color as the background, distinguished only by their dual light/dark shadows. They should never have borders. Content inside cards should be padded generously.

### Inputs
Search bars and form fields use an "inset" neumorphic shadow, making them appear carved into the surface. The focus state is indicated by a soft, glowing Cyan outer shadow.

### Chips & Tags
Chips are rendered with a glassmorphic background—semi-transparent with a 1px white border—to look like small pieces of clinical equipment or lenses.

### Progress Indicators
Step indicators and progress bars use a "liquid" cyan fill, suggesting serum or hydration levels, contained within an indented neumorphic track.

### Modals
Modals should always use the glassmorphism style, blurring the clinical content behind them to maintain focus while preserving the sense of environment.