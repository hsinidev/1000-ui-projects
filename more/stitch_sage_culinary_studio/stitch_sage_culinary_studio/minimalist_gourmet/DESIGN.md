---
name: Minimalist Gourmet
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
  on-surface-variant: '#46483c'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f2f1ee'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#56642b'
  primary: '#56642b'
  on-primary: '#ffffff'
  primary-container: '#8a9a5b'
  on-primary-container: '#253000'
  inverse-primary: '#bdce89'
  secondary: '#5e604d'
  on-secondary: '#ffffff'
  secondary-container: '#e1e1c9'
  on-secondary-container: '#636451'
  tertiary: '#51606b'
  on-tertiary: '#ffffff'
  tertiary-container: '#8595a1'
  on-tertiary-container: '#1f2e37'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d9eaa3'
  primary-fixed-dim: '#bdce89'
  on-primary-fixed: '#161f00'
  on-primary-fixed-variant: '#3e4c16'
  secondary-fixed: '#e4e4cc'
  secondary-fixed-dim: '#c8c8b0'
  on-secondary-fixed: '#1b1d0e'
  on-secondary-fixed-variant: '#474836'
  tertiary-fixed: '#d5e5f1'
  tertiary-fixed-dim: '#b9c9d5'
  on-tertiary-fixed: '#0e1d26'
  on-tertiary-fixed-variant: '#3a4953'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e3e2e0'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
  section-gap: 80px
---

## Brand & Style

This design system targets an epicurean audience that values precision, clarity, and the art of cooking. The brand personality is that of a "quiet authority"—sophisticated, intentional, and serene. It evokes the feeling of a sun-drenched, high-end kitchen where every tool has its place.

The design style is **Minimalism** with a focus on editorial composition. It prioritizes the visual impact of high-quality food photography by treating the UI as a gallery frame rather than a distraction. Key attributes include:
- **Airy Composition:** Massive internal margins within components to allow the content to breathe.
- **Sophisticated Restraint:** A rejection of loud micro-interactions in favor of smooth, meaningful transitions.
- **Editorial Precision:** Using typography and whitespace to create a clear hierarchy that guides the user through complex culinary instructions without cognitive load.

## Colors

The palette is derived from natural, organic elements found in a gourmet kitchen. 

- **Primary (Sage Green):** Used for primary actions, success states, and subtle accents that signify growth and freshness.
- **Secondary (Cream):** The foundational surface color. It provides a warmer, more premium feel than pure white, reducing eye strain during long reading sessions.
- **Tertiary (Charcoal):** Reserved for high-contrast typography and structural elements where definition is required.
- **Neutral (Off-White/Linen):** A step between Cream and pure white to create subtle tonal shifts in background depth.

Use Sage Green sparingly to maintain its impact. The Charcoal should never be pure black, ensuring the "soft-premium" feel is maintained across all text blocks.

## Typography

The typography strategy pairs the timeless elegance of **Noto Serif** with the functional clarity of **Work Sans**. 

- **Noto Serif** handles the narrative: recipe titles, storytelling, and section headers. Its flared serifs provide a literary quality.
- **Work Sans** handles the utility: ingredients list, nutritional data, and step-by-step instructions. Its neutral, open apertures ensure legibility even at smaller sizes or on mobile devices.
- **Nutritional Data:** Use the `data-mono` style for calorie counts and measurements to ensure vertical alignment in lists.
- **Editorial Labels:** Use the `label-caps` style for category tags (e.g., "VEGAN", "30 MINS") to create a distinct visual break from body text.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for desktop to maintain the "editorial" look of a physical cookbook. 

- **The Grid:** A 12-column grid with generous 24px gutters. Elements should often span 6 or 8 columns to create off-center, asymmetrical layouts that feel modern and curated.
- **Vertical Rhythm:** A strict 8px baseline is used. However, "Macro-spacing" (section gaps) should be intentionally oversized (80px+) to separate different phases of the cooking journey.
- **Information Density:** Low. Every recipe step or ingredient group should have significant padding to prevent the user from feeling overwhelmed while cooking.

## Elevation & Depth

To maintain a minimalist and "airy" aesthetic, this design system avoids traditional shadows. Instead, depth is communicated through:

- **Tonal Layering:** Using the Cream (#F5F5DC) and Off-White (#FAF9F6) to create subtle distinction between the page background and card elements.
- **Subtle Borders:** 1px solid lines using a low-opacity Charcoal (10-15% alpha) or a darker shade of Cream. This creates structure without adding visual weight.
- **Image Overlays:** Ingredients or text may slightly overlap high-quality photography using a "Negative Margin" technique to create a layered, three-dimensional effect without needing drop shadows.

## Shapes

The shape language is **Soft**. It avoids the clinical feel of sharp 90-degree corners but stops short of being "bubbly" or overly playful. 

- **Standard Radius:** 4px (0.25rem) for input fields and small buttons.
- **Component Radius:** 8px (0.5rem) for cards and recipe imagery.
- **Large Radius:** 12px (0.75rem) for major containers or modal overlays.

The goal is to mirror the soft edges of organic ingredients while maintaining a structural, architectural integrity.

## Components

- **Buttons:** Primary buttons use a solid Sage Green background with white text. Secondary buttons use a Charcoal border with no fill. Always use generous horizontal padding (min 32px).
- **Cards:** Use a "Frame" style. Instead of a background fill, use a 1px subtle border. Images within cards should have a 1:1 or 4:5 aspect ratio to feel like professional photography prints.
- **Chips/Tags:** Small, pill-shaped elements using a Sage Green tint (10% opacity) with Sage Green text for dietary markers.
- **Input Fields:** Bottom-border only or very light 1px Charcoal borders. Labels should use the `label-caps` typography style.
- **Step Indicators:** Use large, low-opacity Noto Serif numerals (e.g., 01, 02) to mark recipe steps, acting as a background element behind the instruction text.
- **Ingredient Lists:** Include a subtle horizontal divider between items. Checkboxes should be minimal—a simple square that fills with Sage Green when selected.
- **Measurement Toggle:** A custom component to switch between Metric and Imperial, using a soft-toggle design with Sage Green as the active state.