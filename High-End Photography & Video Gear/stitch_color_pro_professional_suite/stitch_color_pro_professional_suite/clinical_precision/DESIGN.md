---
name: Clinical Precision
colors:
  surface: '#fbf9fc'
  surface-dim: '#dbd9dd'
  surface-bright: '#fbf9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f6'
  surface-container: '#efedf0'
  surface-container-high: '#e9e7eb'
  surface-container-highest: '#e3e2e5'
  on-surface: '#1b1b1e'
  on-surface-variant: '#414754'
  inverse-surface: '#303033'
  inverse-on-surface: '#f2f0f3'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc0'
  primary: '#0059bb'
  on-primary: '#ffffff'
  primary-container: '#0070ea'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc7ff'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e2'
  on-secondary-container: '#646464'
  tertiary: '#5a5c60'
  on-tertiary: '#ffffff'
  tertiary-container: '#737479'
  on-tertiary-container: '#fdfcff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc7ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e7'
  tertiary-fixed-dim: '#c6c6cb'
  on-tertiary-fixed: '#1a1c1f'
  on-tertiary-fixed-variant: '#45474b'
  background: '#fbf9fc'
  on-background: '#1b1b1e'
  surface-variant: '#e3e2e5'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
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
  label-mono:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  data-point:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  bento-gap: 1px
  container-max: 1440px
---

## Brand & Style
The brand personality of Color-Pro is defined by absolute technical authority and surgical precision. The target audience consists of colorists, cinematographers, and digital imaging technicians who require a zero-compromise environment. The UI must evoke a sense of professional reliability, appearing more like a scientific instrument than a consumer application.

This design system utilizes a **Clinical Minimalism** style. It leverages heavy white space to reduce cognitive load and high-contrast elements to ensure critical data is immediately legible. The aesthetic avoids decorative flourishes, focusing instead on the beauty of high-resolution product photography and the structural integrity of the "Bento-box" layout—a modular system that mirrors the physical hardware controls of professional color-grading suites.

## Colors
The palette is rooted in a "Sterile White" foundation (#FFFFFF) to provide a neutral canvas for color-accurate work. **Medical Blue** is the primary driver for interactivity, chosen for its association with cleanliness and professional trust.

A secondary "Calibration Palette" (RGB/CMY) is used exclusively for technical data visualization and status indicators. These colors must remain pure and vibrant, representing the full spectrum of color-grading capabilities. Neutral tones are kept strictly within the grayscale to prevent any "color cast" from influencing the user's perception of the content being graded.

## Typography
The typography strategy balances the utilitarian nature of **Inter** for long-form technical reading with the geometric, technical edge of **Space Grotesk** for headlines and data labels. 

Space Grotesk provides a "computer-calculated" feel that aligns with the medical/scientific aesthetic. All labels for technical specs (e.g., Delta-E, Nits, Gamut coverage) should use the `label-mono` style to emphasize precision. Line heights are kept tight in technical readouts but generous in editorial sections to maintain a premium, high-end editorial feel.

## Layout & Spacing
The layout follows a **Bento-box** philosophy, where information is partitioned into distinct, high-precision modules. The system uses a strict 4px grid. 

Technical specifications are displayed in a series of interlocking tiles with a minimal 1px "hairline" gap to simulate the high-tolerance assembly of professional hardware. Content is centered within a fixed 1440px container for marketing pages, while technical dashboard views utilize a full-width fluid grid to maximize the visibility of scopes and monitors. High-resolution product photography should be treated as a primary layout element, often occupying entire "tiles" within the grid.

## Elevation & Depth
This design system rejects traditional shadows in favor of **Low-contrast Outlines** and **Tonal Layering**. Depth is achieved through the stacking of pure white on light gray (#F2F2F7) backgrounds.

To maintain the "Clinical-Chic" aesthetic, UI elements appear to be precision-milled from the same surface. Borders are thin (1px) and use a subtle neutral tone (#E5E5EA) to define boundaries without adding visual noise. When an element requires focus (e.g., a modal), a backdrop blur is used to create a sterile, glass-like separation rather than a dark shadow.

## Shapes
Sharpness equals precision. This design system utilizes a **Sharp (0px)** roundedness level for all primary UI components, including buttons, input fields, and bento-tiles. 

This lack of curvature mirrors the industrial design of high-end reference monitors and rack-mounted hardware. Exceptions are made only for very small utility chips or circular status LEDs, which represent physical hardware indicators. The overall visual impression should be one of rigid structural integrity.

## Components
- **Buttons:** Primary buttons are solid Medical Blue with white uppercase text. Secondary buttons are outlined in 1px black or blue. Hover states involve a slight color shift (darker blue) without any change in size or elevation.
- **Bento Tiles:** These are the core structural units. Each tile should have a 1px border and contain a single data point or product feature. Labels are placed in the top-left using `label-mono`.
- **Technical Inputs:** Input fields feature monospaced numerical values. When a value is changed, the border flashes the corresponding calibration accent color (e.g., Green for "Success/Calibrated").
- **Status Indicators:** Small, circular "LED" icons that use the Accent Palette (RGB/CMY) to indicate signal status, color space, and power.
- **Product Cards:** Minimalist frames that prioritize high-key, sterile-lit photography. Product names are set in `headline-md` Space Grotesk.
- **Lists:** Data-heavy lists use alternating row colors (White and #F9F9F9) with no vertical dividers, maintaining a clean "clinical" spreadsheet appearance.