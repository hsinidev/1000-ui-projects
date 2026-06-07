---
name: Quiet Compassion
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#424845'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#727875'
  outline-variant: '#c2c8c4'
  surface-tint: '#4e635a'
  primary: '#4e635a'
  on-primary: '#ffffff'
  primary-container: '#8da399'
  on-primary-container: '#263932'
  inverse-primary: '#b5ccc1'
  secondary: '#5c5f5e'
  on-secondary: '#ffffff'
  secondary-container: '#dee0df'
  on-secondary-container: '#606363'
  tertiary: '#5c5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#9c9e9e'
  on-tertiary-container: '#333636'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d1e8dd'
  primary-fixed-dim: '#b5ccc1'
  on-primary-fixed: '#0b1f18'
  on-primary-fixed-variant: '#374b43'
  secondary-fixed: '#e1e3e2'
  secondary-fixed-dim: '#c5c7c6'
  on-secondary-fixed: '#191c1c'
  on-secondary-fixed-variant: '#444747'
  tertiary-fixed: '#e1e3e3'
  tertiary-fixed-dim: '#c5c7c7'
  on-tertiary-fixed: '#191c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: Manrope
    fontSize: 12px
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
  unit: 8px
  container-max: 1040px
  gutter: 32px
  margin-page: 64px
  section-gap: 120px
---

## Brand & Style

The brand identity centers on the "Quiet Design" philosophy, prioritizing emotional safety and stability for users navigating grief. The personality is empathetic, steady, and unobtrusive—acting as a supportive presence rather than a demanding interface.

The design style is a blend of **Minimalism** and **Soft Tonal Layering**. It avoids the anxiety of modern "attention-economy" patterns. Instead of high-energy interactions, this design system utilizes vast whitespace, slow transitions, and a reduced cognitive load to provide a sense of "room to breathe." The aesthetic goal is to create a digital sanctuary that feels as permanent and calm as a physical library or a quiet garden.

## Colors

The palette is anchored in organic, desaturated tones to prevent visual fatigue. 

*   **Primary (Soft Sage):** Used sparingly for meaningful actions and active states. It represents growth and tranquility.
*   **Secondary (Muted Grey):** Provides soft structure for borders and secondary backgrounds, ensuring the UI doesn't feel stark.
*   **Surface (White/Off-white):** The dominant color. Large expanses of white space are mandatory to maintain the "Quiet Design" principle.
*   **Text (Charcoal Grey):** A softened black (#4A4A4A) is used for body text to reduce the harsh contrast of pure black on white, making long-form reading more comfortable.

## Typography

This design system uses a pairing of **Noto Serif** (substituting for Lora) and **Manrope**.

*   **Serif Headers:** Noto Serif brings a literary, timeless quality. Headers should use "Sentence case" to feel more conversational and less like a corporate shout.
*   **Sans-Serif Body:** Manrope provides a balanced, modern clarity. It is highly readable at smaller sizes and feels grounded.
*   **Hierarchy:** Maintain generous vertical spacing between headings and body text. Avoid bold weights where a medium weight or a larger font size can suffice; the goal is an elegant, lightweight appearance.

## Layout & Spacing

The layout follows a **Fixed Grid** model centered on the screen, creating a sense of containment and focus. 

*   **Rhythm:** Use an 8px base unit. However, the defining characteristic of this system is the "extra" space—padding should always lean towards the larger side of the scale.
*   **Section Gaps:** Use significant vertical breathing room (120px+) between major content blocks to prevent the user from feeling overwhelmed by information.
*   **Margins:** Generous side margins ensure content never feels "trapped" against the edges of the viewport.

## Elevation & Depth

To maintain a "stable and unintrusive" feel, this design system avoids heavy shadows or complex 3D effects. 

*   **Tonal Layering:** Depth is primarily communicated through subtle shifts in background color (e.g., a light sage card on a white background).
*   **Low-Contrast Outlines:** Use soft, 1px borders in Muted Grey (#E5E7E6) to define areas without creating hard visual breaks.
*   **Ambient Shadows:** If an element must float (like a supportive modal), use an extremely diffused, low-opacity shadow (e.g., 5% opacity) with a slight Sage tint to keep it integrated with the color story.

## Shapes

The shape language is **Rounded**, avoiding sharp corners which can feel aggressive or clinical. 

*   **Standard Radius:** 8px for cards and containers to provide a gentle, approachable structure.
*   **Large Radius:** 16px or 24px for larger layout elements or featured content sections to emphasize the "soft" brand personality.
*   **Consistency:** Every interactive element must share these rounded properties to reinforce the feeling of a safe, "softened" environment.

## Components

*   **Buttons:** Primary buttons use the Soft Sage background with white text. Secondary buttons are outlined in Muted Grey. Avoid high-contrast "hover" states; use a gentle opacity shift instead. No "Buy Now" style urgency.
*   **Cards:** Use a simple #F9FAFA background with an 8px radius and a 1px border. Do not use heavy hover lifts.
*   **Input Fields:** Minimalist design with only a bottom border or a very light grey fill. Focus states use a Soft Sage glow rather than a thick black line.
*   **Chips/Tags:** Used for categorization. These should be pill-shaped with very light sage backgrounds and dark sage text.
*   **Lists:** High line-height (1.8x) for readability. Use soft bullet points (dots or small sage icons) rather than numbers where possible to reduce the feeling of a "checklist."
*   **Reflection/Journaling Areas:** Large, open text areas with a paper-like feel, utilizing the Noto Serif font to encourage expressive thought.
*   **Progress Indicators:** Use soft, horizontal bars that fill slowly. Avoid circular "loading" icons that feel frantic; prefer a gentle pulse or a fading transition.