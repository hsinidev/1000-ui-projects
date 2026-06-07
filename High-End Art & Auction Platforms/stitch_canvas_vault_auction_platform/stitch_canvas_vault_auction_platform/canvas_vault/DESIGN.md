---
name: Canvas-Vault
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Bodoni Moda
    fontSize: 80px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '400'
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
    lineHeight: '1.6'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-x: 64px
  section-padding: 128px
---

## Brand & Style
This design system centers on a **Minimalist-Galleria** aesthetic, positioning the product as an elite, archival-grade platform for high-value fine art. The brand personality is silent, authoritative, and sophisticated, acting as a neutral vessel that allows the artwork to remain the primary focus. 

The visual style is a blend of **Minimalism** and **High-Contrast Editorial**. It utilizes expansive whitespace to create a sense of exclusivity and "breathing room" found in physical blue-chip galleries. The emotional response should be one of absolute trust, permanence, and clinical precision. Every interaction must feel intentional, reinforcing a UX focus on elite security and high-fidelity detail.

## Colors
The palette is strictly limited to three core tones to maintain an archival feel. 

- **Matte Black (#121212):** Used for primary typography, structural borders, and high-emphasis UI elements. It provides the "weight" and authority of the system.
- **Stark White (#FFFFFF):** The primary background color. It should be used generously to simulate gallery walls.
- **Slate (#708090):** Reserved for secondary information, metadata, disabled states, and subtle UI accents that require less visual prominence than the primary black.

Avoid gradients or soft shadows. Contrast is the primary tool for hierarchy.

## Typography
The typographic system relies on extreme contrast between the serif display face and the sans-serif functional face.

- **Headings:** **Bodoni Moda** is used for all editorial and high-level headings. It should be set with high contrast; large sizes emphasize its elegant hairlines.
- **Body & UI:** **Inter** provides a clinical, legible counterpoint. It is used for all descriptions, bid inputs, and security details.
- **Labels:** Small labels (e.g., "Lot Number", "Status") should be set in Inter, uppercase, with generous letter spacing to evoke the feeling of museum placard captions.

## Layout & Spacing
The layout follows a **Fixed Grid** model with an emphasis on oversized margins and dramatic vertical spacing.

- **Grid:** A 12-column grid with wide 32px gutters.
- **Rhythm:** Use a strict 8px base unit. Section-to-section transitions should use 128px or more of vertical whitespace to maintain the premium, "un-crowded" feel.
- **Imagery:** Artworks should span at least 6-8 columns, often breaking the standard vertical rhythm to allow for full-height, high-fidelity crops.
- **Information Density:** Intentionally low. Information is revealed progressively to ensure the user is never overwhelmed by data, focusing instead on the aesthetic value of the piece.

## Elevation & Depth
This design system rejects shadows and blurs in favor of **Bold Borders** and **Tonal Layering**.

- **Structure:** Depth is communicated through 1px Matte Black borders. Surfaces do not "float"; they are contained within sharp, defined compartments.
- **Layering:** Use Slate (#708090) at very low opacities (e.g., 5-10%) for subtle background differentiation in "vault" or "secure" areas.
- **Interactions:** Hover states should involve color inversions (White to Black) or subtle weight shifts rather than elevation changes.

## Shapes
The shape language is strictly **Sharp**. 

Every UI element—including buttons, input fields, images, and cards—must have a 0px border radius. This reinforces the "archival" and "architectural" nature of the product, moving away from consumer-grade software aesthetics and toward a high-end professional tool for collectors and institutions.

## Components
- **Buttons:** Primary buttons are solid Matte Black with White text. Secondary buttons are 1px Matte Black outlines. All buttons use sharp corners and uppercase Inter typography.
- **Input Fields:** Minimalist 1px bottom-border only, or a full 1px Matte Black box. Focus states should be denoted by a thickness increase to 2px.
- **Cards:** Used sparingly. Cards are defined by a 1px Matte Black border with no shadow. The artwork image within the card should be the dominant element.
- **High-Fidelity Viewer:** A custom component for art inspection. It should include a Matte Black "Secure" header, a magnifying glass cursor, and technical metadata (provenance, dimensions) in the Slate color.
- **Status Indicators:** Use small, sharp rectangular "chips" for "Bidding Open" or "Sold." These should use Slate for neutral states and Matte Black for active states.
- **Security Badges:** Discreet, 1px bordered icons that signify "Vault Verified" or "Blockchain Provenance," using the Slate color to remain present but unobtrusive.