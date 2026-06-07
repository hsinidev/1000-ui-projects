---
name: Terra-Equestrian Design System
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
  on-surface-variant: '#4f453f'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#81756e'
  outline-variant: '#d2c4bc'
  surface-tint: '#705a4c'
  primary: '#26170c'
  on-primary: '#ffffff'
  primary-container: '#3d2b1f'
  on-primary-container: '#ac9181'
  inverse-primary: '#dec1af'
  secondary: '#545f72'
  on-secondary: '#ffffff'
  secondary-container: '#d5e0f7'
  on-secondary-container: '#586377'
  tertiary: '#1c1a15'
  on-tertiary: '#ffffff'
  tertiary-container: '#322e29'
  on-tertiary-container: '#9b958e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#fbddca'
  primary-fixed-dim: '#dec1af'
  on-primary-fixed: '#28180d'
  on-primary-fixed-variant: '#574335'
  secondary-fixed: '#d8e3fa'
  secondary-fixed-dim: '#bcc7dd'
  on-secondary-fixed: '#111c2c'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#e9e1d9'
  tertiary-fixed-dim: '#ccc5be'
  on-tertiary-fixed: '#1e1b16'
  on-tertiary-fixed-variant: '#4a4640'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  base: 8px
  gutter: 24px
  margin-desktop: 80px
  margin-mobile: 24px
  section-gap: 120px
---

## Brand & Style

The brand personality of this design system is defined by "Quiet Luxury"—an aesthetic that prioritizes heritage, permanence, and architectural precision over transient trends. It is designed for an elite audience that values discretion and craftsmanship. The emotional response should be one of stability and exclusivity, evoking the atmosphere of a private estate library or a prestigious polo pavilion.

The design style is **Minimalism** with an **Editorial** influence. It utilizes heavy whitespace to allow high-resolution, full-bleed imagery to serve as the primary narrative driver. Layouts are strictly governed by structural grids, mirroring the intentionality of landscape architecture. The interface acts as a silent gallery, framing the properties without competing for attention.

## Colors

This design system utilizes a palette rooted in the natural world, specifically the textures of leather, stone, and earth. 

*   **Primary (Earthy Brown):** A deep, saturated umber used for primary typography and structural accents, representing the "Terra" or grounded aspect of the brand.
*   **Secondary (Slate Gray):** A cool, architectural gray used for secondary details, borders, and UI iconography to provide a sophisticated contrast to the warm browns.
*   **Tertiary (Stone/Clay):** A muted, warm neutral used for surface backgrounds and subtle container fills.
*   **Neutral (Crisp White):** The primary canvas color, used generously to create the "High-end Editorial" feel and provide maximum contrast for imagery.

Color application should be conservative. Use the Earthy Brown for primary CTAs and the Slate Gray for functional elements. Whitespace is not just a gap; it is a primary "color" in this system.

## Typography

The typography strategy balances tradition with modernity. 

**Noto Serif** is used for all headings and display text. It conveys the heritage of equestrian culture and the literary quality of high-end real estate catalogs. Large-scale headings should use the "display-lg" style with slightly tighter letter spacing to create an architectural, "locked-in" appearance.

**Manrope** serves as the functional workhorse for body copy and UI labels. Its balanced, refined geometry ensures legibility at smaller sizes while maintaining a modern edge. For navigation and technical labels, the "label-caps" style should be used to provide a crisp, organized hierarchy that feels meticulously planned.

## Layout & Spacing

This design system employs a **Fixed Grid** model on desktop to maintain an architectural sense of order. The layout is built on a 12-column grid with a wide 80px outer margin to frame the content like a premium coffee-table book.

The spacing rhythm is expansive. Standard vertical gaps between sections should be 120px, allowing users to breathe between content blocks. Imagery should alternate between contained (aligned to the grid) and full-bleed (edge-to-edge) to create a dynamic, editorial pace. Gutters are kept tight at 24px to emphasize the relationship between text and the imagery it describes.

## Elevation & Depth

To maintain its architectural and grounded aesthetic, this design system avoids traditional shadows and floating elements. Depth is communicated through **Tonal Layers** and **Low-Contrast Outlines**.

1.  **Structural Hairlines:** Use 1px borders in Slate Gray (at 20-30% opacity) to define zones without adding visual weight.
2.  **Inset Depth:** Rather than lifting elements up, depth is created by layering content over full-bleed imagery or using subtle shifts in background color (e.g., placing a Crisp White card over a Stone background).
3.  **Flat Stacking:** Elements should feel like they are placed firmly on a solid surface. If an overlay is required (e.g., a navigation menu), use a solid Crisp White background or a high-opacity Slate Gray—never a soft blur or drop shadow.

## Shapes

The shape language of this design system is strictly **Sharp (0px)**. 

Every UI element—from buttons and input fields to image containers and cards—must feature 90-degree corners. This decision reinforces the architectural and "grounded" brand pillars, mimicking the structural lines of high-end estate floor plans and the precision of formal polo grounds. Rounding is only permitted for iconography that naturally requires it (e.g., a circle for a user avatar).

## Components

### Buttons
Buttons are rectangular and sharp. Primary buttons use the Earthy Brown background with Crisp White text. Secondary buttons are "ghost" style with a 1px Slate Gray border. Label text is always in the `label-caps` style for a refined, professional look.

### Cards
Real estate listing cards should emphasize the image first. Use a "borderless" approach where the typography sits directly on the white canvas below a full-width image. Text should be left-aligned with ample padding to maintain the editorial feel.

### Input Fields
Inputs are simple 1px underlines or full-box outlines in Slate Gray. Use `manrope` for placeholder text. The focus state is indicated by the line weight increasing to 2px or the color shifting to Earthy Brown.

### Navigation
The navigation bar should be minimalist and high-contrast. Links are `label-caps` with a 2px Earthy Brown underline appearing on hover.

### Chips/Tags
Used for property features (e.g., "6 Stalls," "Olympic Arena"). These should be styled as simple Slate Gray outlines with `label-caps` text. No filled backgrounds.

### Additional Components: Property Specifications
A dedicated "Spec Grid" component is required for estate details. This uses hairline Slate Gray dividers and a two-column layout, pairing `label-caps` for the attribute name with `body-md` for the value.