---
name: Zen-Precision
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#45483c'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#52652a'
  primary: '#33450d'
  on-primary: '#ffffff'
  primary-container: '#4a5d23'
  on-primary-container: '#bed58e'
  inverse-primary: '#b8cf88'
  secondary: '#835425'
  on-secondary: '#ffffff'
  secondary-container: '#ffbf87'
  on-secondary-container: '#7a4b1e'
  tertiary: '#3f412f'
  on-tertiary: '#ffffff'
  tertiary-container: '#565845'
  on-tertiary-container: '#cdceb6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4eca2'
  primary-fixed-dim: '#b8cf88'
  on-primary-fixed: '#141f00'
  on-primary-fixed-variant: '#3b4d14'
  secondary-fixed: '#ffdcc1'
  secondary-fixed-dim: '#f9ba82'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#683d0f'
  tertiary-fixed: '#e4e4cc'
  tertiary-fixed-dim: '#c8c8b0'
  on-tertiary-fixed: '#1b1d0e'
  on-tertiary-fixed-variant: '#474836'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
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
    lineHeight: '1.6'
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-page: 64px
  section-gap: 128px
  container-max: 1200px
---

## Brand & Style

The design system is anchored in the concept of "The Focused Path." It balances the quiet, meditative discipline of archery with the rigorous technical precision of high-end craftsmanship. The target audience is the discerning archer who values the heritage of the sport as much as the quality of the equipment. 

The visual style is a blend of **Minimalism** and **Tactile** influences. It utilizes heavy whitespace to evoke the silence of a range, paired with subtle organic textures that hint at natural materials like wood and leather. The UI should feel deliberate, removing any unnecessary noise to allow the user to focus on the product or the practice. Every element is designed to feel "hand-crafted," emphasizing quality over quantity.

## Colors

The palette is derived from the archery range and the bowyer’s workshop. **Moss Green** serves as the primary action color, representing the outdoor environment and providing a steady, calming focal point. **Natural Wood** is used for secondary accents, adding warmth and a sense of traditional material.

**Sand** acts as the primary background surface, creating a softer, more premium feel than pure white. **Charcoal** provides the necessary weight for typography and structural borders, ensuring that the minimalist layout remains grounded and legible. High-contrast pairings (Charcoal on Sand or Sand on Moss Green) should be used to guide the eye to primary conversion points.

## Typography

The typography in this design system creates a dialogue between tradition and modernity. **Noto Serif** is utilized for headlines to convey authority, heritage, and the "sophisticated" aspect of the brand. It should be used with generous leading and occasional italicization for emphasis.

**Manrope** provides the functional counterpart. As a clean, modern sans-serif, it handles all UI elements, body copy, and technical specifications. This ensures that while the brand feels historic, the shopping and booking experience remains efficient and clear. All labels and buttons should use Manrope in uppercase with slight letter-spacing to evoke the feel of engraved technical markings.

## Layout & Spacing

The layout follows a **Fixed Grid** model to mirror the precision of a target. A 12-column grid is centered within the viewport, using wide page margins to create a "frame" around the content. This framing technique focuses the user's attention on the center, much like a sight-picture through a bow.

Spacing is generous. Section gaps are intentionally large to provide "breathing room," reinforcing the Zen philosophy of the brand. Grids should use a base-8 rhythm for internal spacing, but the overarching layout should prioritize asymmetrical balance and large areas of "Sand" whitespace.

## Elevation & Depth

This design system avoids aggressive shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**. Depth is communicated through subtle shifts in background color—for example, a Sand surface may sit atop a slightly darker Natural Wood or Moss Green container.

When depth must be emphasized, use "Ghost Borders"—1px solid lines in Charcoal at 15% opacity. This maintains a flat, architectural look. For high-end product showcases, a very soft, diffused ambient shadow (0px 10px 30px rgba(0,0,0,0.05)) may be used to make premium items appear as if they are resting physically on the Sand-colored surface.

## Shapes

The shape language is primarily **Soft (Level 1)**. This subtle 4px corner radius strikes a balance between the organic curves of a traditional longbow and the sharp, mathematical precision of an arrow's flight. 

Buttons and input fields should maintain this consistent Soft radius. Circular shapes are reserved exclusively for elements that mimic physical targets or specialized equipment components (like bow sights or fletching details). Avoid pill-shaped buttons; they are too "casual" for the high-end, disciplined nature of this design system.

## Components

### Buttons
Primary buttons use a solid Moss Green fill with Sand text, utilizing uppercase Manrope for the label. Secondary buttons use a 1px Charcoal border with no fill. The interaction state should be a subtle shift to Natural Wood on hover, suggesting a tactile, physical change.

### Input Fields
Inputs are defined by a bottom-border only (Charcoal, 1px) or a very light Sand-filled box with a 4px radius. This keeps the forms looking light and unencumbered. Labels should sit above the input in Manrope Bold at a small size.

### Cards
Product and range cards should be minimalist. Use a 1px ghost border and rely on high-quality photography to do the heavy lifting. Content should be center-aligned within the card to reinforce the "target" metaphor.

### Chips & Tags
Used for equipment categories (e.g., "Recurve," "Carbon Fiber"). These should be Charcoal text on a Natural Wood background at low opacity, or Moss Green outlines.

### Specialized Components
*   **The Progress Tracker:** For range bookings or training modules, use a thin, horizontal line (like an arrow shaft) with small circular nodes representing progress points.
*   **Technical Spec Lists:** Use Charcoal dividers and Manrope typography for equipment specifications, emphasizing the "Precision" aspect of the brand.