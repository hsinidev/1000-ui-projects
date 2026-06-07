---
name: Zen-Pet Wellness
colors:
  surface: '#faf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e3e2e0'
  on-surface: '#1a1c1a'
  on-surface-variant: '#444841'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f2f1ee'
  outline: '#757870'
  outline-variant: '#c4c8bf'
  surface-tint: '#54624e'
  primary: '#52604c'
  on-primary: '#ffffff'
  primary-container: '#6a7964'
  on-primary-container: '#f8fff0'
  inverse-primary: '#bbcbb3'
  secondary: '#6b5c4c'
  on-secondary: '#ffffff'
  secondary-container: '#f4dfcb'
  on-secondary-container: '#716252'
  tertiary: '#615b54'
  on-tertiary: '#ffffff'
  tertiary-container: '#7a736c'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e7ce'
  primary-fixed-dim: '#bbcbb3'
  on-primary-fixed: '#121f0f'
  on-primary-fixed-variant: '#3d4b38'
  secondary-fixed: '#f4dfcb'
  secondary-fixed-dim: '#d7c3b0'
  on-secondary-fixed: '#241a0e'
  on-secondary-fixed-variant: '#524436'
  tertiary-fixed: '#ebe1d8'
  tertiary-fixed-dim: '#cec5bc'
  on-tertiary-fixed: '#1f1b16'
  on-tertiary-fixed-variant: '#4c463f'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2e0'
typography:
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  h3:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Newsreader
    fontSize: 17px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: Newsreader
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

This design system is built to evoke a sense of restorative calm, professional expertise, and deep compassion. The brand personality is "The Gentle Healer"—sophisticated yet deeply approachable. It targets discerning pet owners seeking holistic care and rehabilitation services that prioritize the emotional and physical well-being of their animals.

The UI style is a blend of **Soft Minimalism** and **Tactile Organicism**. It leverages generous whitespace to reduce cognitive load and uses "natural" textures and colors to create a high-end, boutique atmosphere. The emotional response should be one of immediate relief and quiet confidence, steering away from the clinical coldness of traditional veterinary medicine toward a warm, sanctuary-like digital experience.

## Colors

The palette is derived from nature to ground the digital experience in the physical world of wellness and rehabilitation.

*   **Primary (Sage Green):** A muted, earthy green used for primary actions, success states, and brand emphasis. It symbolizes growth and healing.
*   **Secondary (Pale Wood/Ash):** A warm taupe-tan used for structural accents, Dividers, and subtle backgrounds to evoke the tactile quality of light oak.
*   **Tertiary (Soft Sand):** A very light, warm beige used for card backgrounds and secondary containers to soften the interface.
*   **Neutral (Soft White):** The primary canvas color. It is a warm, "off-white" that prevents the eye strain associated with pure white (#FFFFFF), maintaining the serene atmosphere.

## Typography

This design system utilizes a high-contrast typographic pairing to balance modern accessibility with traditional trust.

*   **Headlines & UI Labels:** *Plus Jakarta Sans* provides a friendly, geometric clarity. The soft curves of the letterforms mirror the organic shapes used throughout the UI.
*   **Body Text:** *Newsreader* is used for all long-form content. Its literary quality evokes the authority of a medical professional while its soft serifs maintain a human, compassionate touch.
*   **Hierarchy:** Use generous line heights (1.6x) for body text to ensure a relaxed reading pace. Headlines should remain tight and elegant.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop to maintain a "contained" and curated feel, while transitioning to a fluid model for mobile devices. 

*   **The Rhythm:** Use an 8px-based scale, but prioritize larger "breathing room" (LG and XL increments) between major sections to prevent the UI from feeling cluttered.
*   **Margins:** Maintain wide outer margins (minimum 24px on mobile, up to 80px on desktop) to center the content as a focal point of calm.
*   **Alignment:** Use centered layouts for marketing or landing sections to enhance the "Zen" feel, while using left-aligned layouts for functional rehabilitation dashboards.

## Elevation & Depth

Depth in this design system is achieved through **Ambient Shadows** and **Tonal Layering** rather than harsh borders.

*   **Shadows:** Use extremely soft, diffused shadows with a slight "Sage Green" tint (#7D8C76 at 5-10% opacity). This creates an "airy" feel where components appear to float gently above the surface.
*   **Layering:** Backgrounds should utilize the Neutral Soft White, while interactive cards use either the Tertiary Sand or a pure White to create a subtle stack.
*   **Gradients:** Use very soft, linear gradients (e.g., Sage Green to a slightly lighter tint) on primary buttons and progress bars to suggest dimension without looking "glossy."

## Shapes

The shape language is strictly **Pill-shaped and Organic**. There are no sharp corners in this design system.

*   **Corner Radii:** Buttons and tags use a full "pill" radius. Cards and containers use a minimum of 24px (rounded-lg) or 48px (rounded-xl) to feel soft and approachable.
*   **Organic Containers:** Use "squircle" or slightly irregular organic blobs for image masks and decorative background elements to reinforce the holistic, natural theme.

## Components

*   **Buttons:** Fully pill-shaped. Primary buttons use a soft Sage Green gradient. Secondary buttons use a Thin Sage stroke or a wood-toned background.
*   **Cards:** Use `rounded-xl` corners with the ambient sage-tinted shadow. Content within cards should have internal padding of at least 32px.
*   **Calm Progress Bars:** Thicker than standard bars (approx. 12px height) with fully rounded caps. Use a soft Sage Green for the fill and a Pale Wood for the track.
*   **Inputs:** Minimalist fields with a soft Tertiary background and no border until focused. On focus, use a 2px Sage Green bottom border or soft outer glow.
*   **Chips/Tags:** Small pill-shaped containers with *Plus Jakarta Sans* in uppercase/letter-spaced labels for high legibility.
*   **Wellness Timeline:** A vertical rehabilitation tracker using soft circles and dotted lines in Pale Wood to show a pet's journey through recovery.