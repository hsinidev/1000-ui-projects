---
name: Haute Optique
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
  on-surface-variant: '#4c4546'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#6b5c4c'
  on-secondary: '#ffffff'
  secondary-container: '#f4dfcb'
  on-secondary-container: '#716252'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#f4dfcb'
  secondary-fixed-dim: '#d7c3b0'
  on-secondary-fixed: '#241a0e'
  on-secondary-fixed-variant: '#524436'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 80px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  nav-link:
    fontFamily: Epilogue
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.15em
  body-lg:
    fontFamily: Epilogue
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Epilogue
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Epilogue
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.2em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

This design system is engineered for a premium clinical environment that doubles as a luxury fashion boutique. The brand personality is authoritative yet avant-garde, blending the precision of optometry with the high-stakes aesthetics of a runway editorial. It evokes a sense of curated exclusivity, targeting a clientele that views eyewear as a primary fashion investment.

The design style is **Minimalist** with a focus on **Editorial High-Contrast**. It relies on aggressive whitespace to frame high-end photography, creating a gallery-like experience. Every interface element is treated as a structural component, using sharp lines and intentional voids to direct the eye toward the product—the frames—and the expertise of the practitioners.

## Colors

The palette is anchored in a monochromatic foundation to ensure that product photography remains the focal point. 

- **Deep Black (#000000):** Used for primary typography, structural borders, and high-impact UI elements. It represents the "Ink" of a high-fashion magazine.
- **Crisp White (#FFFFFF):** The primary canvas color. It provides the "Generous Whitespace" required to keep the interface feeling airy and expensive.
- **Muted Champagne (#D9C5B2):** A sophisticated accent used sparingly for highlights, secondary call-to-actions, and subtle background shifts to indicate premium surfaces.
- **Off-White/Neutral (#F7F7F7):** Used for subtle section breaks or background fills behind product carousels to add depth without introducing a new hue.

## Typography

This design system utilizes a stark typographic hierarchy to achieve an editorial feel. 

**Noto Serif** is the voice of the clinic. It is used for all major headlines and display text. Its high-contrast strokes and elegant serifs provide the necessary gravitas and luxury "Vogue-esque" aesthetic.

**Epilogue** serves as the modern, wide-set counterpoint. By increasing the letter spacing (tracking) on navigation and labels, it creates a clean, technical feel that balances the traditional serif. This sans-serif is used for all functional UI elements, body copy, and technical eyeglass specifications to ensure readability and a contemporary edge.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop and a fluid model on mobile, emphasizing "The Rule of Thirds" often found in photography. 

- **Grid:** A 12-column grid with wide 32px gutters to prevent content crowding.
- **Margins:** Oversized 64px margins on the viewport edges to frame the content like a printed page.
- **Rhythm:** Vertical spacing is intentionally loose. Section gaps of 128px are standard to allow each frame or service to "breathe" and stand alone.
- **Asymmetry:** Occasional intentional misalignment (e.g., text blocks overlapping image edges) should be used to break the digital monotony and lean into the fashion-forward aesthetic.

## Elevation & Depth

Visual hierarchy is established through high-contrast layering and **Sharp Shadows**. 

- **Shadows:** Unlike soft, organic shadows, this design system uses crisp, offset shadows with very low blur (e.g., 4px - 8px blur) and high opacity (15-20%) to create a "cut-out" or "collaged" effect. This mimics the hard lighting often used in high-fashion studio photography.
- **Tonal Layers:** Elevation is also conveyed by placing Champagne elements over White surfaces. 
- **Imagery as Depth:** Full-bleed images act as the lowest layer, with typography and UI components "floating" on top with high-contrast backgrounds to ensure legibility.

## Shapes

The shape language is strictly **Sharp (0)**. 

To maintain the sophisticated, high-end look, all buttons, input fields, image containers, and cards feature 90-degree corners. Rounded corners are perceived as friendly and casual; sharp corners are perceived as precise, professional, and architectural. Thin 1px black borders are the primary container method for cards and inputs, reinforcing the "clean lines" aesthetic.

## Components

- **Buttons:** Primary buttons are solid Black with White uppercase text. Hover states shift to the Champagne accent. All buttons are rectangular with no corner radius.
- **Inputs:** Minimalist bottom-border only or full 1px black outline. Labels sit inside the field in the `label-caps` style and move above on focus.
- **Product Cards:** No borders or shadows by default. The image occupies 90% of the card area. Text (Brand & Price) appears in a clean, wide-set sans-serif underneath. On hover, a sharp shadow appears to "lift" the card.
- **Navigation:** A sticky top-bar with a transparent background that transitions to White on scroll. Links use high letter-spacing and a subtle underline on hover.
- **Appointment CTA:** A persistent, floating "Book Exam" button that utilizes the Champagne accent color to distinguish it from the black-and-white fashion content.
- **Image Carousels:** Use large-scale imagery with "progress bars" instead of dots to maintain the architectural feel.