---
name: Botanical Vitality
colors:
  surface: '#fef8f5'
  surface-dim: '#ded9d6'
  surface-bright: '#fef8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8f3ef'
  surface-container: '#f2edea'
  surface-container-high: '#ece7e4'
  surface-container-highest: '#e6e1de'
  on-surface: '#1d1b1a'
  on-surface-variant: '#42493e'
  inverse-surface: '#32302e'
  inverse-on-surface: '#f5f0ec'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#a03f30'
  on-secondary: '#ffffff'
  secondary-container: '#fe8672'
  on-secondary-container: '#741f13'
  tertiary: '#393937'
  on-tertiary: '#ffffff'
  tertiary-container: '#50504d'
  on-tertiary-container: '#c4c2bf'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#ffdad4'
  secondary-fixed-dim: '#ffb4a7'
  on-secondary-fixed: '#400200'
  on-secondary-fixed-variant: '#80281b'
  tertiary-fixed: '#e4e2de'
  tertiary-fixed-dim: '#c8c6c3'
  on-tertiary-fixed: '#1b1c1a'
  on-tertiary-fixed-variant: '#474744'
  background: '#fef8f5'
  on-background: '#1d1b1a'
  surface-variant: '#e6e1de'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
  h3:
    fontFamily: Newsreader
    fontSize: 28px
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
    lineHeight: '1'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

This design system is built upon the philosophy of "Clinical Serenity"—a fusion of high-end editorial aesthetics and professional healthcare reliability. It targets an audience seeking holistic wellness through nature-backed science, requiring a UI that feels both organic and deeply organized.

The visual style utilizes **Modern Minimalism** with **Tactile** influences. By prioritizing whitespace and purposeful botanical imagery, the interface avoids the cluttered feel of traditional medical portals, instead evoking the atmosphere of a high-end apothecary or a tranquil botanical garden. The user experience is designed to reduce cognitive load and heart rate, using soft transitions and clear information architecture to foster a sense of being "in good hands."

## Colors

The palette is rooted in the natural world, specifically the grounding qualities of earth and flora. 

*   **Primary (Forest Green):** Used for primary actions, navigation, and core brand elements to represent growth and medicinal authority.
*   **Secondary (Terracotta):** Used as a warmth-inducing accent for secondary CTAs, alerts, and highlighting key wellness benefits.
*   **Tertiary/Background (Cream):** Replaces clinical white to provide a softer, more premium foundation that reduces eye strain.
*   **Neutral:** A warm charcoal-grey is used for body text to ensure high legibility without the harshness of pure black.

Use subtle tints of Forest Green (90% lightness) for background sections to create soft rhythmic transitions across long-form content.

## Typography

This design system leverages a high-contrast typographic pairing to balance tradition and modernity. 

**Newsreader** provides a classic, literary authority to headings, echoing the trust of botanical encyclopedias and medical journals. It should be used with tighter tracking in larger sizes to maintain a sophisticated, editorial look.

**Manrope** serves as the functional workhorse. Its geometric yet friendly construction ensures that patient data, ingredient lists, and instructional text remain highly readable and contemporary. Use `label-caps` for eyebrows and small UI metadata to create a structured hierarchy.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for desktop and a fluid system for mobile. A 12-column grid provides the structural backbone, but the layout philosophy encourages "breaking the grid" with organic botanical illustrations that bleed off-edge or overlap containers.

Generous vertical spacing (section gaps) is mandatory to maintain the "calm" brand pillar. Elements should never feel crowded; if a screen feels dense, increase the whitespace between sections rather than shrinking the components. Align text-heavy content to a central 8-column span to optimize readability.

## Elevation & Depth

To maintain a natural and soft aesthetic, this design system avoids harsh shadows and high-contrast depth. Instead, it uses **Tonal Layers** and **Ambient Shadows**.

1.  **Surface Tiers:** Use a slightly darker cream or a very pale green tint to lift containers off the base background.
2.  **Shadow Character:** When elevation is necessary (e.g., for floating cards or dropdowns), use a "Botanical Blur"—a very soft, diffused shadow with a hint of Forest Green in the tint (#2D5A27 at 4% opacity) rather than grey.
3.  **Flat Depth:** Prefer thin, 1px borders in a muted Terracotta or Forest Green over shadows for interactive elements like input fields.

## Shapes

The shape language is defined by **Soft Roundedness**, mimicking the smoothed edges of river stones or organic leaves. 

Avoid sharp 90-degree corners entirely. Use the standard 0.5rem (8px) radius for most UI components (cards, buttons, inputs). For imagery, consider using "organic masks"—subtle, non-uniform rounded shapes—to frame botanical photography, reinforcing the natural medicine theme.

## Components

*   **Buttons:** Primary buttons use a solid Forest Green fill with white Manrope text. Secondary buttons use a Terracotta outline with a 1.5px stroke. Hover states should involve a gentle shift in saturation rather than a dramatic color change.
*   **Cards:** Use a "Surface" approach—Cream containers on a slightly tinted background with a soft 1px border. Do not use heavy shadows.
*   **Inputs:** Clean, bottom-border only or fully enclosed with soft corners. Labels should use the `label-caps` style for clarity.
*   **Chips/Tags:** Used for filtering herbal categories or health benefits. These should use a pill-shape (radius-xl) and soft, earth-toned backgrounds (e.g., a pale sage or muted clay).
*   **Botanical Accents:** Use thin-line botanical sketches (Illustrations) as decorative elements that interact with the borders of components, sometimes peeking from behind cards to add depth and brand personality.
*   **Progress Indicators:** Use soft, rounded bars in Forest Green to track wellness journeys or form completion, ensuring the "clinical" aspect feels supportive rather than cold.