---
name: EarthMind Apothecary
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
  on-surface-variant: '#45483c'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#52652a'
  primary: '#33450d'
  on-primary: '#ffffff'
  primary-container: '#4a5d23'
  on-primary-container: '#bed58e'
  inverse-primary: '#b8cf88'
  secondary: '#974806'
  on-secondary: '#ffffff'
  secondary-container: '#fd9754'
  on-secondary-container: '#6f3200'
  tertiary: '#44402d'
  on-tertiary: '#ffffff'
  tertiary-container: '#5c5742'
  on-tertiary-container: '#d5cdb3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4eca2'
  primary-fixed-dim: '#b8cf88'
  on-primary-fixed: '#141f00'
  on-primary-fixed-variant: '#3b4d14'
  secondary-fixed: '#ffdbc8'
  secondary-fixed-dim: '#ffb68a'
  on-secondary-fixed: '#321300'
  on-secondary-fixed-variant: '#743500'
  tertiary-fixed: '#ebe2c8'
  tertiary-fixed-dim: '#cec6ad'
  on-tertiary-fixed: '#1f1c0b'
  on-tertiary-fixed-variant: '#4c4733'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  headline-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Newsreader
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.03em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1140px
---

## Brand & Style

This design system is built upon the intersection of ancestral wisdom and modern clinical expertise. The aesthetic is **Tactile and Minimalist**, leaning heavily into the "Foraged & Rustic" narrative. It avoids the synthetic smoothness of modern tech in favor of grit, fiber, and organic imperfection.

The brand personality is authoritative and grounded. The UI should feel like a high-end botanical field guide or a professional apothecary’s ledger—highly organized and scientific, yet deeply connected to the earth. The emotional response should be one of trust, serenity, and a sense of returning to foundational truths. Visual interest is driven by texture rather than motion, utilizing subtle linen overlays and grainy gradients to create a physical presence on a digital screen.

## Colors

The palette is derived directly from the forest floor and historical herbals. 

*   **Moss Green (#4A5D23):** Used for primary actions, navigation headers, and signifying growth and health.
*   **Burnt Orange (#B35D1E):** Reserved for highlights, notifications, and secondary accents that require attention without breaking the organic harmony.
*   **Parchment (#F4EBD0):** The primary surface color. It acts as the canvas, providing a warm, low-strain background that feels like aged paper.
*   **Ink (#2D2926):** A deep, slightly warm charcoal used for all primary text to ensure high legibility and a "printed" feel.

Color application should favor large washes of Parchment with Moss Green as the dominant structural color. Avoid pure white or pure black; every color must feel "dyed" or "organic."

## Typography

Typography in this design system is "Serif-heavy" to reinforce authority and the literary heritage of herbalism. **Newsreader** is the cornerstone, used for both headlines and body copy to create a scholarly, editorial feel. Its variable optical sizing allows for sharp, elegant headers and highly readable long-form text.

To balance the traditional serif, **Work Sans** is used for utility elements, such as labels, metadata, and buttons. This adds a "clinical" layer to the design, suggesting modern scientific rigor behind the ancestral knowledge. Use generous line heights to evoke the airy feel of a premium textbook.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to maintain an editorial, book-like structure. On desktop, content is centered within a 12-column grid with wide margins to create a sense of "prestige" and focus. 

The spacing rhythm is based on a 4px baseline, but defaults to larger increments (16px, 24px, 40px) to prevent the UI from feeling "cramped" or "app-like." White space is treated as "the silence between the plants"—it is essential for clarity and the professional, clinical tone. Layouts should be symmetrical where possible, reflecting the balance of nature.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Tactile Textures** rather than traditional drop shadows. 

1.  **Base Layer:** The Parchment (#F4EBD0) surface, featuring a subtle grain or linen texture overlay at 5-10% opacity.
2.  **Inset Depth:** Form inputs and interactive containers use subtle inner shadows or 1px strokes in a darker Parchment tint to appear "pressed" or "debossed" into the paper.
3.  **Floating Elements:** When an element must sit above the content (like a modal), use a very soft, wide, Burnt Orange-tinted shadow at 5% opacity to maintain the warm, organic atmosphere. 

Avoid "material" style elevations. The goal is to make the interface feel like a flat physical surface with layered paper and ink.

## Shapes

The shape language is **Soft (0.25rem)**. While the overall vibe is organic, the clinical aspect of the brand requires professional structure. Sharp corners feel too aggressive, while pill-shapes feel too "tech-startup." 

Slightly softened corners mimic hand-cut paper or vintage apothecary labels. Use "Organic Shapes"—such as irregular botanical frames or hand-drawn ink circles—sparingly as background decorative elements behind product shots or botanical illustrations to break the rigid grid and reinforce the "Foraged" aesthetic.

## Components

*   **Buttons:** Rectangular with a 4px radius. Primary buttons are solid Moss Green with Parchment text. Secondary buttons are outlined with a 1px Moss Green stroke. High-priority "Caution" or "Specialty" buttons use Burnt Orange.
*   **Cards:** Use a slightly lighter or darker tint of Parchment than the background. Borders should be a very fine (0.5pt) ink-colored stroke. Use subtle linen textures within the card body.
*   **Input Fields:** Minimalist design with only a bottom border or a very faint debossed effect. Use Work Sans for placeholder text to maintain the clinical look.
*   **Chips/Tags:** Small, rectangular tags using the Burnt Orange or Moss Green palette with uppercase Work Sans labels. These should look like labeled specimens.
*   **Botanical Illustrations:** Use fine-line, monochrome (Ink or Moss Green) illustrations of herbs and plants. These are not just decorative; they should be treated as functional iconography.
*   **Checkboxes/Radios:** Custom-styled to look like hand-inked marks (a simple "X" for checkboxes or a solid dot for radios), reinforcing the "Ancestral Ledger" theme.