---
name: Experience-Driven Luxury
colors:
  surface: '#fff8f5'
  surface-dim: '#e1d8d4'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2ed'
  surface-container: '#f5ece7'
  surface-container-high: '#efe6e2'
  surface-container-highest: '#e9e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#41474d'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#72787e'
  outline-variant: '#c1c7ce'
  surface-tint: '#356382'
  primary: '#003650'
  on-primary: '#ffffff'
  primary-container: '#1b4d6b'
  on-primary-container: '#90bde0'
  inverse-primary: '#9fccef'
  secondary: '#9d4225'
  on-secondary: '#ffffff'
  secondary-container: '#fe8c69'
  on-secondary-container: '#742409'
  tertiary: '#393124'
  on-tertiary: '#ffffff'
  tertiary-container: '#514739'
  on-tertiary-container: '#c3b6a4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9fccef'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#184b69'
  secondary-fixed: '#ffdbd1'
  secondary-fixed-dim: '#ffb59f'
  on-secondary-fixed: '#3a0a00'
  on-secondary-fixed-variant: '#7e2b10'
  tertiary-fixed: '#efe0cd'
  tertiary-fixed-dim: '#d2c4b2'
  on-tertiary-fixed: '#221a0f'
  on-tertiary-fixed-variant: '#4f4538'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  headline-display:
    fontFamily: Noto Serif
    fontSize: 80px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.03em
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 160px
---

## Brand & Style

The design system is anchored in the concept of "Experiential Serenity." It targets a discerning global traveler who seeks more than just a room; they seek a curated emotional journey. The brand personality is authoritative yet welcoming, blending the timeless elegance of traditional hospitality with a modern, minimalist digital approach.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. We utilize expansive layouts and high-quality photography to immerse the user in the physical environment of the hotels, while using delicate, translucent interface layers to provide utility without disrupting the visual narrative. Every interaction is designed to feel deliberate, quiet, and premium, evoking a sense of exclusive tranquility.

## Colors

The color palette for this design system is inspired by natural coastal landscapes, creating a grounded yet sophisticated atmosphere.

*   **Sand (#F5E6D3):** Functions as the primary canvas. It is used for large background areas and surfaces to provide a warmer, more tactile feeling than pure white.
*   **Ocean Blue (#1B4D6B):** Used for primary actions, navigation elements, and authoritative text. It represents depth and stability.
*   **Terracotta (#C05C3D):** Reserved for accent moments, interactive highlights, and call-to-action elements that require an organic, human warmth.
*   **Deep Charcoal (#2D2926):** Our neutral, used for body text and subtle borders to ensure high legibility against the Sand background.

## Typography

Typography in this design system creates a dialogue between heritage and modernity. 

We use **Noto Serif** for all headings. Its high-contrast strokes and elegant serifs provide the "authoritative" voice required for a luxury brand. Headlines should be set with tight tracking to emphasize their editorial quality.

For body copy and functional UI elements, we use **Plus Jakarta Sans**. This typeface is modern and highly legible. To achieve the "wide-tracked" look requested, body text should always feature a positive letter-spacing (0.02em to 0.03em), creating a sense of breathability and lightness in the reading experience.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for content, centered within the viewport, while allowing imagery and background elements to bleed full-width to the edges. 

The layout relies on a 12-column grid with generous 32px gutters. A hallmark of this system is the use of "Extreme Whitespace." Sections are separated by large vertical gaps (160px+) to ensure the user never feels overwhelmed. Content should often be offset—spanning 6 or 8 columns rather than the full 12—to create an asymmetrical, editorial feel that mimics high-end travel magazines.

## Elevation & Depth

To maintain a serene and immersive feeling, this design system avoids heavy, traditional drop shadows. Instead, we use **Glassmorphism** and **Tonal Layering** to create depth.

*   **Glassmorphism:** Navigation bars and foreground overlays use a background blur (20px) with a 60% opacity white or Sand tint. This allows the immersive photography to remain visible while ensuring UI legibility.
*   **Low-Contrast Outlines:** Interactive containers use a 1px border in a slightly darker shade of Sand or a very low-opacity Ocean Blue. 
*   **Ambient Depth:** When a shadow is strictly necessary for a floating element (like a modal), use a very large, ultra-diffused shadow with a 5% opacity tint of Ocean Blue, creating an "ambient glow" rather than a hard shadow.

## Shapes

The shape language of this design system is **Soft (Level 1)**. 

While the layout is structured and grid-based, we introduce 0.25rem (4px) corner radii to buttons, input fields, and cards. This subtle rounding softens the clinical precision of the grid, making the interface feel more approachable and organic, echoing the soft edges of a sandy coastline. Media elements (images and videos) may remain sharp (0px) to maintain a high-fashion, editorial aesthetic.

## Components

*   **Buttons:** Primary buttons are solid Ocean Blue with Sand text, using the `label-caps` typography. They feature generous internal padding (16px 32px). Secondary buttons use a transparent background with a 1px Ocean Blue border.
*   **Navigation:** The primary navigation is a transparent sticky bar. Upon scroll, it transitions to a glassmorphic state (Sand tint with background blur). Links use the `label-caps` style.
*   **Input Fields:** Clean, bottom-border-only design to minimize visual clutter. Labels float above the line in `label-caps` style when the field is active.
*   **Cards:** Cards are used for "Experiences." They feature full-bleed imagery with a subtle gradient overlay at the bottom to house white typography. They do not have shadows; they rely on spacing and the Sand background for definition.
*   **Immersive Hero:** A full-viewport component featuring auto-playing silent video or high-resolution imagery, with a centered Display Headline and a single Terracotta call-to-action.
*   **Personalized Concierge Widget:** A small, persistent floating element in the bottom right, styled with a glassmorphic circle and a Terracotta icon, representing the "Personalized Service" aspect of the brand.