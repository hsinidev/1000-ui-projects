---
name: Aero-Closet Identity
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#444748'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#747878'
  outline-variant: '#c4c7c7'
  surface-tint: '#5f5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1c1b1b'
  on-primary-container: '#858383'
  inverse-primary: '#c8c6c5'
  secondary: '#7b5647'
  on-secondary: '#ffffff'
  secondary-container: '#feccba'
  on-secondary-container: '#7a5546'
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
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ecbcaa'
  on-secondary-fixed: '#2e140a'
  on-secondary-fixed-variant: '#603f31'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Bodoni Moda
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  display-md:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Bodoni Moda
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-ui:
    fontFamily: Metropolis
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 20px
  section-gap: 120px
---

## Brand & Style

This design system embodies the intersection of high-fashion editorial aesthetics and precision robotic engineering. It is designed for an elite clientele who views their wardrobe as a curated gallery. The brand personality is authoritative, sophisticated, and whisper-quiet—suggesting a service that operates with seamless, automated perfection.

The visual style is **High-End Minimalism**. It prioritizes extreme legibility, vast "negative space" to allow garment photography to breathe, and a rigid adherence to a grid that mirrors the architectural precision of the automated hardware. The emotional response should be one of calm, effortless luxury, where the interface acts as a silent digital concierge.

## Colors

The palette is rooted in a high-contrast editorial foundation. 

*   **Primary (Deep Charcoal):** Used for all primary typography, structural icons, and heavy lifting. It provides the "ink" on the page, grounding the design with authority.
*   **Secondary (Rose Gold):** Reserved exclusively for accents, interactive states, and "precision" indicators. It should be applied sparingly to maintain its value as a luxury signal.
*   **Background (Crisp White):** The primary canvas. It must remain uncluttered to simulate the feeling of a spacious, high-end boutique.
*   **Surface (Soft Grey):** Used for subtle dividers and secondary containers to provide structure without breaking the minimalist flow.

Interactive elements should utilize a linear gradient of the Rose Gold to simulate the metallic sheen of the physical automation rails.

## Typography

The typographic hierarchy is a study in contrast. 

**Headlines** utilize *Bodoni Moda*, a high-contrast serif that evokes the timeless elegance of premium fashion periodicals. These should be set with generous leading and occasional italicization for emphasis on "Collection" or "Designer" names.

**UI & Data** utilize *Metropolis*, a clean, geometric sans-serif. This font represents the "Aero" aspect of the brand—technical, precise, and modern. Use uppercase styling for labels and technical data points (e.g., fabric type, temperature, storage duration) to enhance the "engineered" feel of the system.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** system inspired by editorial spreads. Content is centered within a maximum width container to ensure consistency on ultra-wide displays.

*   **Desktop:** A 12-column grid with wide 80px outer margins. This creates a "frame" around the content, emphasizing its value.
*   **Tablet:** An 8-column grid with 40px margins.
*   **Mobile:** A 4-column grid with 20px margins.

Vertical rhythm is governed by a 4px base unit, but the defining characteristic is the **Section Gap**. Large modules (e.g., "The Evening Collection" vs "Daily Wear") should be separated by significant whitespace (120px+) to ensure a curated, non-cluttered user experience.

## Elevation & Depth

To maintain a minimalist aesthetic, this design system rejects heavy drop shadows in favor of **Low-Contrast Outlines** and **Tonal Layering**.

Depth is communicated through:
1.  **Hairline Borders:** Use 0.5pt to 1pt borders in Deep Charcoal (at 10-15% opacity) to define cards and containers.
2.  **Layered Surfaces:** Primary content sits on pure white (#FFFFFF). Overlays or secondary drawers should use a very subtle off-white or the softest grey to indicate they are "above" the main plane.
3.  **Active Depth:** When an item is selected, instead of a shadow, apply a subtle Rose Gold inner-stroke. This mimics the precision lighting found inside high-end cabinetry.

## Shapes

The shape language is strictly **Sharp (0px)**. 

In luxury and high-fashion, sharp corners signify architectural intent and bespoke craftsmanship. Every button, image container, and input field must feature crisp 90-degree angles. The only exceptions are icons or specific garment-related graphics. This rigidity reinforces the "precision-engineered" nature of the automated wardrobe system.

## Components

### Buttons
Primary actions are rendered as sharp-edged blocks with a Deep Charcoal background and White text. Secondary actions use a "Ghost" style—a 1px Charcoal border with no fill. For "Elite" or "Automated" actions (e.g., "Retrieve Garment"), use a subtle Rose Gold gradient border.

### Input Fields
To maintain minimalism, input fields should use only a bottom-border (1px Charcoal). Labels sit above the field in uppercase *Metropolis* (Label-MD). Focus states are indicated by the bottom border transitioning to a Rose Gold gradient.

### Cards
Cards for garment display should have zero elevation. They are defined by high-contrast photography and a thin, 0.5px border. Information like "Designer" and "Last Worn" should be tucked into the corners using the `data-ui` type scale.

### The "Aero" Progress Bar
When the system is retrieving an item, use a specialized progress bar: a hairline horizontal track with a 2px Rose Gold "shuttle" that moves with high easing (slow-fast-slow) to mimic the mechanical movement of the wardrobe's retrieval arm.

### Chips & Tags
Used for "Fabric" or "Season." These should be sharp rectangles with a light charcoal background and white text, set in uppercase. Avoid rounded capsules.