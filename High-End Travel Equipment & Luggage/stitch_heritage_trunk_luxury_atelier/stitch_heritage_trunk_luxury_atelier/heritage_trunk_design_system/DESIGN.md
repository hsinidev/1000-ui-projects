---
name: Heritage Trunk Design System
colors:
  surface: '#fff8f7'
  surface-dim: '#f1d3d1'
  surface-bright: '#fff8f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff0ef'
  surface-container: '#ffe9e7'
  surface-container-high: '#ffe1df'
  surface-container-highest: '#f9dcd9'
  on-surface: '#271717'
  on-surface-variant: '#504443'
  inverse-surface: '#3e2c2b'
  inverse-on-surface: '#ffedeb'
  outline: '#827472'
  outline-variant: '#d4c3c1'
  surface-tint: '#795553'
  primary: '#321716'
  on-primary: '#ffffff'
  primary-container: '#4a2c2a'
  on-primary-container: '#bd928f'
  inverse-primary: '#eabcb8'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#231f0e'
  on-tertiary: '#ffffff'
  tertiary-container: '#383422'
  on-tertiary-container: '#a39c84'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#eabcb8'
  on-primary-fixed: '#2e1413'
  on-primary-fixed-variant: '#5f3e3c'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ebe2c8'
  tertiary-fixed-dim: '#cec6ad'
  on-tertiary-fixed: '#1f1c0b'
  on-tertiary-fixed-variant: '#4c4733'
  background: '#fff8f7'
  on-background: '#271717'
  surface-variant: '#f9dcd9'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Noto Serif
    fontSize: 20px
    fontWeight: '500'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
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
  container-padding: 24px
  gutter: 16px
  section-gap: 64px
---

## Brand & Style

The design system is anchored in the concepts of legacy, tactile craftsmanship, and bespoke exclusivity. It evokes the sensory experience of a private atelier: the scent of tanned leather, the weight of brass hardware, and the texture of fine stationary. The target audience consists of high-net-worth individuals who value provenance over trends.

The visual style is **Tactile / Skeuomorphic** refined through a lens of modern luxury. This is achieved by using subtle textures that mimic parchment and leather, paired with crisp, high-contrast photography. The UI should feel less like a digital interface and more like a physical catalog or a leather-bound ledger.

## Colors

The palette is derived from traditional trunk-making materials. **Deep Mahogany** serves as the primary structural color, used for typography and heavy accents to provide a sense of grounded permanence. **Parchment** acts as the primary canvas, replacing stark whites with a warmer, more aged surface that reduces eye strain and feels premium. 

**Gold** is reserved strictly for high-value interactions and delicate decorative elements, such as dividers and iconography. Neutral tones are used for depth, specifically a darker shade of mahogany for shadows and "ink" blacks for legibility on lighter surfaces.

## Typography

This design system utilizes **Noto Serif** for all editorial and heading elements to establish an authoritative, literary tone. Headings should utilize tighter tracking and generous line heights to allow the letterforms to breathe. 

**Manrope** is used for body text and functional labels to provide a contemporary counter-balance. Its clean, geometric nature ensures readability on mobile devices. For navigation and small metadata, an all-caps treatment of Manrope is preferred to mimic the look of embossed metal plates or stamped leather.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model on desktop and a high-margin fluid model on mobile. To maintain an air of exclusivity, the design system utilizes generous whitespace (negative space) to draw focus to the high-contrast photography. 

A strict 8px rhythmic grid governs all components. Vertical rhythm is prioritized to maintain the "page-like" feel of the parchment cards. Section gaps are intentionally large to create a slow, deliberate scrolling experience, discouraging the "flick-scroll" behavior of mass-market apps.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and subtle physical metaphors rather than heavy shadows. 

1.  **Base Layer:** The Parchment background (#F4EBD0).
2.  **Surface Layer:** UI Cards use a slightly lighter, "cleaner" parchment tint with a very fine 1px inner stroke in a muted Gold to simulate the edge of a thick cardstock.
3.  **Interactive Layer:** Buttons and active states utilize Deep Mahogany.
4.  **Engraving:** For secondary buttons or dividers, a "letterpress" effect is used—a 1px dark top shadow and 1px light bottom highlight—to make the element appear stamped into the surface.

## Shapes

The shape language reflects the structural integrity of a trunk. Corners are generally **Soft (4px)** to prevent the UI from feeling dangerously sharp, while still maintaining the architectural strength of a bespoke object. 

Avoid large, pill-shaped buttons or overly circular elements, as they contradict the brand's traditionalist roots. Containers should resemble hand-cut leather patches or heavy cardstock.

## Components

### Buttons
Primary buttons are solid **Deep Mahogany** with **Gold** or **Parchment** text, utilizing a sharp rectangular profile with minimal rounding. The hover/active state should introduce a subtle grain texture overlay. Secondary buttons are outlined in Gold with all-caps Manrope typography.

### Parchment Cards
Cards are the primary container for content. They must feature a subtle paper texture and a 1px border that is slightly darker than the card fill. On mobile, cards should span the full width or be inset with significant margins to maintain the "editorial" look.

### Gold Dividers
Horizontal rules are never a simple gray line. They are 1px **Gold** lines, often featuring a small diamond or flourish in the center to denote a break in the narrative.

### Input Fields
Inputs are styled as "Signature Lines." Instead of a full box, use a bottom border only in Deep Mahogany, with the label positioned in Manrope Caps above the line, mimicking a formal document.

### Additional Components
- **The "Monogram" Badge:** A circular or diamond-shaped gold element used for limited editions or bespoke options.
- **Textured Overlays:** A subtle noise or leather grain texture applied to image placeholders and primary call-to-action sections.