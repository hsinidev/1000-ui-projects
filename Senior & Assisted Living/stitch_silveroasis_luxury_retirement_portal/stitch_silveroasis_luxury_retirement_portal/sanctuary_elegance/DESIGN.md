---
name: Sanctuary Elegance
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#4d463a'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#7e7668'
  outline-variant: '#d0c5b5'
  surface-tint: '#725b29'
  primary: '#715a28'
  on-primary: '#ffffff'
  primary-container: '#8c733e'
  on-primary-container: '#ffffff'
  inverse-primary: '#e1c386'
  secondary: '#506353'
  on-secondary: '#ffffff'
  secondary-container: '#d2e8d4'
  on-secondary-container: '#566959'
  tertiary: '#5e5d59'
  on-tertiary: '#ffffff'
  tertiary-container: '#777671'
  on-tertiary-container: '#ffffff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdf9f'
  primary-fixed-dim: '#e1c386'
  on-primary-fixed: '#261a00'
  on-primary-fixed-variant: '#584413'
  secondary-fixed: '#d2e8d4'
  secondary-fixed-dim: '#b7ccb8'
  on-secondary-fixed: '#0d1f13'
  on-secondary-fixed-variant: '#384b3c'
  tertiary-fixed: '#e5e2dc'
  tertiary-fixed-dim: '#c9c6c1'
  on-tertiary-fixed: '#1c1c18'
  on-tertiary-fixed-variant: '#474743'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 60px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 44px
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Work Sans
    fontSize: 22px
    fontWeight: '400'
    lineHeight: 36px
  body-md:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  label-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: 0.05em
  label-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 32px
  margin: 40px
  target-min: 56px
---

## Brand & Style

The design system is rooted in the philosophy of "Quiet Luxury." It bridges the gap between high-end hospitality and radical accessibility, ensuring that the interface feels like a premium concierge service rather than a medical or utility app. The brand personality is serene, dependable, and sophisticated, targeting an affluent demographic that values both aesthetic beauty and functional ease.

The style leans into **Minimalism** with subtle **Tactile** accents. By using generous whitespace, we reduce cognitive load, while high-contrast borders and large interactive surfaces ensure ease of use for those with low-vision or motor-control challenges. The visual language avoids trendy "noise," opting instead for a timeless, editorial-inspired layout that evokes the feeling of a physical luxury brochure.

## Colors

The palette is anchored in high-contrast natural tones to meet WCAG AAA standards where possible, ensuring maximum legibility for low-vision users. 

- **Primary (Warm Gold):** Used for key calls-to-action and brand accents. It is darkened slightly to #8C733E to maintain a 4.5:1 ratio against light backgrounds.
- **Secondary (Soft Sage):** A calming, restorative green used for success states, secondary buttons, and decorative icons.
- **Tertiary (Cream):** The primary canvas color. It provides a softer, more luxurious alternative to pure white, reducing eye strain.
- **Neutral (Deep Charcoal):** Used for body text and primary headers to ensure the sharpest possible contrast against the Cream background.

## Typography

This design system prioritizes readability through high-contrast serif headlines and highly legible sans-serif body text. 

- **Headlines:** Noto Serif provides an authoritative, editorial feel. Its distinct letterforms assist in quick scanning.
- **Body & Labels:** Work Sans was selected for its open apertures and generous x-height, which are essential for users with declining visual acuity. 
- **Scale:** All font sizes are intentionally oversized. The "Body-md" starts at 18px to ensure comfortable reading without the need for manual zooming. Paragraphs utilize generous line heights to prevent "line swimming."

## Layout & Spacing

The layout utilizes a **Fixed Grid** model to provide a consistent, predictable experience. On desktop, content is centered within a maximum-width container to minimize ocular movement requirements. 

A rigid 8px spacing system is used, but with a "Large-Scale" philosophy. The minimum interactive hit area is set to 56px (target-min) to accommodate motor-skill variations. Vertical rhythm is emphasized with large gutters (32px) and margins (40px) to ensure no two elements feel "cluttered," which is a primary pain point for low-vision users.

## Elevation & Depth

To maintain a premium hospitality feel, the design system avoids heavy shadows, which can muddy the interface for low-vision users. Instead, it employs **Tonal Layers** and **Low-Contrast Outlines**.

- **Surface Tiers:** Depth is created by placing Cream containers on slightly darker Off-White backgrounds.
- **Borders:** Instead of shadows, interactive elements use 2px solid borders in Warm Gold or Soft Sage to define boundaries clearly.
- **Focus States:** High-visibility focus rings (3px width) in Deep Charcoal are mandatory for all keyboard and screen-reader navigation.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding provides a welcoming, human feel while maintaining the structural integrity of a "Luxury Resort." 

Large-scale components like cards use `rounded-lg` (0.5rem), providing enough curvature to feel modern without appearing overly "bubbly" or juvenile. This balance preserves the sophisticated brand image while ensuring that corners do not feel aggressively sharp.

## Components

- **Buttons:** Primary buttons use a solid Gold background with Charcoal text. They must have a minimum height of 56px. Secondary buttons use a 2px Sage border.
- **Cards:** Cards feature a 1px Sage border or a subtle tonal shift. They should always have a clear "primary action" button to avoid ambiguity.
- **Input Fields:** Fields must have permanent labels (no floating placeholders) and high-contrast 2px borders. The tap target for the entire field area should be large.
- **Chips:** Used for filtering resort amenities (e.g., "Spa," "Dining"). Chips use a thick stroke when selected to provide clear visual feedback.
- **Lists:** High-density lists are avoided. List items must have at least 16px of vertical padding and a divider line with at least a 3:1 contrast ratio against the background.
- **Navigation:** A simplified top-tier navigation bar with large, legible icons accompanied by text labels. Icon-only buttons are strictly prohibited to ensure clarity.