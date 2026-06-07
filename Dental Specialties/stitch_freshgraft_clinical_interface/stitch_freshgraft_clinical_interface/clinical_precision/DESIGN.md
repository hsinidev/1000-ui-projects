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
  on-surface-variant: '#434653'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#737784'
  outline-variant: '#c3c6d5'
  surface-tint: '#2559bd'
  primary: '#00327d'
  on-primary: '#ffffff'
  primary-container: '#0047ab'
  on-primary-container: '#a5bdff'
  inverse-primary: '#b1c5ff'
  secondary: '#00677e'
  on-secondary: '#ffffff'
  secondary-container: '#00d2fd'
  on-secondary-container: '#005669'
  tertiary: '#303743'
  on-tertiary: '#ffffff'
  tertiary-container: '#474e5b'
  on-tertiary-container: '#b8bfcf'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2ff'
  primary-fixed-dim: '#b1c5ff'
  on-primary-fixed: '#001946'
  on-primary-fixed-variant: '#00419e'
  secondary-fixed: '#b4ebff'
  secondary-fixed-dim: '#3cd7ff'
  on-secondary-fixed: '#001f27'
  on-secondary-fixed-variant: '#004e5f'
  tertiary-fixed: '#dce2f3'
  tertiary-fixed-dim: '#c0c7d6'
  on-tertiary-fixed: '#151c27'
  on-tertiary-fixed-variant: '#404754'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
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
  technical-sm:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-bold:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.08em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin-mobile: 20px
  max-width: 1280px
---

## Brand & Style

The design system is engineered to evoke the atmosphere of a high-end medical laboratory: sterile, reliable, and technologically advanced. It serves a dual purpose: providing a clear, high-contrast interface for medical professionals while utilizing biomorphic background elements to visualize the biological nature of tissue and bone regeneration.

The visual style is a hybrid of **Minimalism** and **Modern Corporate**, emphasizing functional clarity over decorative flourish. The UI acts as a digital instrument—a surgical tool designed for accuracy. While the functional components remain strictly geometric and sharp, the background utilizes organic, fluid shapes to represent cellular structures, creating a sophisticated tension between the "observer" (the UI) and the "subject" (the biological matter).

## Colors

The palette is anchored by **Laboratory Blue (#0047AB)**, a color associated with clinical authority and scientific depth. This is set against a **Clinical White** background to maintain a sterile, high-light environment. 

- **Primary (Laboratory Blue):** Used for primary actions, critical data highlights, and branding.
- **Secondary (Cyan/Serum):** Used sparingly for data visualization and "active" state indicators.
- **Neutral (Slate/Gray):** Used for secondary text and structural borders, ensuring the interface doesn't feel overly "heavy."
- **Background:** Strictly white or extremely light gray to maximize readability and simulate a clean-room environment.

## Typography

This design system utilizes a tiered typography strategy to balance technical sophistication with maximum legibility. 

**Space Grotesk** is used for headlines and technical data points. Its geometric nature reflects scientific innovation and futuristic precision. 

**Inter** is the primary workhorse for body copy and UI labels. It provides a neutral, systematic clarity that is essential for reading medical data and complex instructions. To enhance the "scientific" feel, labels often utilize all-caps with increased letter spacing, mimicking the markings found on medical equipment.

## Layout & Spacing

The design system employs a **Fixed Grid** model for desktop and a single-column **Fluid Grid** for mobile devices. All spacing is based on a strict 4px/8px increments to ensure mathematical precision across the UI.

On mobile, the focus is on a singular vertical flow to prevent cognitive overload. Desktop layouts utilize a 12-column grid with generous 24px gutters to allow the "biomorphic" background elements to breathe without interfering with data-heavy components. Content density should be kept moderate to maintain a "clean" feel, using whitespace as a separator rather than decorative lines wherever possible.

## Elevation & Depth

To maintain the "high-precision instrument" aesthetic, this design system avoids soft, ambient shadows. Instead, it uses **Tonal Layers** and **Low-contrast outlines**.

- **Depth:** Surfaces are defined by thin (1px) borders in a light gray or muted blue, rather than drop shadows. 
- **Active States:** Depth is communicated through color shifts (e.g., a button becoming a deeper blue) or technical inner-glows that suggest a "backlit" instrument panel.
- **Glassmorphism:** Occasionally used for overlays or modal backgrounds with high-diffusion blur (30px+) to simulate looking through a microscope lens or a glass petri dish, allowing the organic background shapes to remain visible but non-distracting.

## Shapes

The shape language follows a "Surgical Sharpness" principle. All UI components—including buttons, input fields, and cards—utilize **0px (Sharp) corners**. This reinforces the feeling of precision, reliability, and technical rigor.

The only exceptions are the **Biomorphic Background Shapes**. These are soft, rounded, and organic, created using SVG blobs or blurred gradients. They represent the "soft" tissue being treated by the "sharp" precision of the FreshGraft technology. This contrast ensures that the interactive elements are clearly distinguished from the illustrative background.

## Components

### Buttons
Primary buttons are solid Laboratory Blue with white, all-caps text. They have sharp corners and no gradients. Secondary buttons use a 1px border of the same blue with a transparent background.

### Input Fields
Fields are represented by a bottom-border only or a very thin 1px full border. Labels sit above the field in a small, spaced-out caps font (Inter). Focus states should be indicated by a 2px Laboratory Blue underline.

### Cards
Cards are containers with a white background and a subtle light-gray border. They should not have shadows. Content within cards is divided by thin horizontal rules to maintain the appearance of a technical report.

### Chips & Tags
Used for status indicators (e.g., "In Vitro," "Clinical Phase"). These are rectangular with no rounding, using a light blue background and dark blue text to signify "read-only" data labels.

### Data Visualization
Charts should use "Scientific Blue" and "Serum Cyan" for data lines. Grid lines on charts should be visible but very faint, mimicking graph paper or oscilloscope displays.

### Biomorphic Backgrounds
Incorporate large, low-opacity (5-10%) organic SVG paths behind content sections. These shapes should appear to "flow" or "grow" as the user scrolls, providing a sense of biological life beneath the technical interface.