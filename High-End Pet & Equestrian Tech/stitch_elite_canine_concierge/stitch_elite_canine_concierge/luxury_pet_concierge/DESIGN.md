---
name: Luxury Pet Concierge
colors:
  surface: '#f9f9ff'
  surface-dim: '#d9d9e0'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3fa'
  surface-container: '#ededf4'
  surface-container-high: '#e7e8ee'
  surface-container-highest: '#e2e2e9'
  on-surface: '#191c20'
  on-surface-variant: '#4b463d'
  inverse-surface: '#2e3036'
  inverse-on-surface: '#f0f0f7'
  outline: '#7d766c'
  outline-variant: '#cec5ba'
  surface-tint: '#685d4a'
  primary: '#685d4a'
  on-primary: '#ffffff'
  primary-container: '#f7e7ce'
  on-primary-container: '#726753'
  inverse-primary: '#d3c5ad'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#6b5c44'
  on-tertiary: '#ffffff'
  tertiary-container: '#fbe6c7'
  on-tertiary-container: '#75664e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f0e0c8'
  primary-fixed-dim: '#d3c5ad'
  on-primary-fixed: '#221b0b'
  on-primary-fixed-variant: '#4f4533'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#f4e0c1'
  tertiary-fixed-dim: '#d7c4a6'
  on-tertiary-fixed: '#241a07'
  on-tertiary-fixed-variant: '#52452e'
  background: '#f9f9ff'
  on-background: '#191c20'
  surface-variant: '#e2e2e9'
typography:
  headline-xl:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
  headline-lg:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: EB Garamond
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
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  gutter: 24px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built for an elite pet concierge and health service, targeting high-net-worth individuals who view their pets as family members deserving of the highest care. The brand personality is poised, nurturing, and exceptionally refined. 

The aesthetic leans heavily into **Soft-UI Neumorphism**, utilizing the physics of light to create a tactile, interface-as-sculpture feel. By blending Minimalism with subtle skeuomorphic depth, the design avoids the clinical coldness of traditional health apps, opting instead for an "airy" atmosphere that feels like a high-end spa or a private club. The goal is to evoke a sense of calm and total reliability, ensuring every interaction feels premium and deliberate.

## Colors

The palette is anchored by **Silk White (#F8F8FF)**, which serves as the canvas for the neumorphic shadows. **Soft Champagne (#F7E7CE)** is used for primary actions and highlights, providing a warm, prestigious glow. **Slate (#708090)** acts as the anchor for typography and iconography, offering enough contrast for accessibility without breaking the sophisticated, low-contrast harmony.

To achieve the soft-UI effect, this design system utilizes variations of the Silk White base: 
- **Light Shadow:** #FFFFFF (Pure White) at 100% opacity.
- **Dark Shadow:** #E0E0EB (A cool-toned shadow) at 40-60% opacity.
- **Surface Gradients:** Subtle transitions from #F8F8FF to #F2F2F9 to enhance the 3D curvature.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage with modernity. **EB Garamond** provides an authoritative and literary tone for headings, suggesting a legacy of excellence and bespoke service. It should be used with generous leading and occasional italics for emphasis.

**Manrope** is used for all functional text. Its geometric yet friendly proportions ensure maximum readability for health data and concierge schedules. All body text should maintain a generous line height (1.6) to support the "airy" visual direction. Labels use an increased font weight and slight letter spacing to maintain hierarchy against the soft UI elements.

## Layout & Spacing

The layout philosophy follows a **fixed-width, centered grid** for desktop to mimic the feel of a luxury editorial magazine, and a fluid, high-margin grid for mobile. We utilize a 12-column system with wide 24px gutters.

Spacing is intentionally expansive. This design system avoids information density in favor of "breathable" layouts. Content blocks are separated by significant vertical margins (stack-lg) to allow the neumorphic shadows of each card to exist without visual interference. Interior padding within cards should never fall below 32px to maintain a premium feel.

## Elevation & Depth

Hierarchy is established through **extrusion and recession** rather than color or traditional drop shadows. Elements exist on three primary planes:

1.  **The Base:** Silk White (#F8F8FF) background.
2.  **Elevated (Extruded):** Primary cards and buttons. These use two shadows: a "light" shadow (top-left, -8px -8px, 16px blur, white) and a "dark" shadow (bottom-right, 8px 8px, 16px blur, #E0E0EB).
3.  **Recessed (Inset):** Input fields and search bars. These use inset shadows to appear carved into the interface, creating a tactile "well" for user data.

Gradients should be used subtly (top-left to bottom-right) on elevated surfaces to reinforce the direction of the light source, moving from a lighter tint of the surface color to the base color.

## Shapes

The shape language is defined by extreme softness. A minimum corner radius of **24px** is applied to all standard cards, while buttons and chips utilize a **full-pill (maximum)** radius. 

The use of "soft" shapes is critical to the brand’s psychological profile—removing sharp edges communicates safety, friendliness, and the organic nature of pet care. Even internal elements like progress bars or image containers must adhere to high-radius standards (minimum 16px) to remain consistent with the outer containers.

## Components

### Buttons
Buttons are pill-shaped and elevated. The "Primary" button uses the Champagne color with a subtle inner glow. The "Secondary" button is Silk White, distinguished from the background only by its neumorphic extrusion. Hover states should "flatten" slightly (reducing shadow distance) to simulate a physical press.

### Cards
Cards are the primary container for all pet health data and concierge options. They feature a 32px corner radius. To maintain the "airy" feel, cards should not have borders; depth alone should define their boundaries.

### Input Fields
Inputs are recessed (inset shadow) with a 24px corner radius. The text cursor and active focus state use the Slate color for clarity.

### Chips & Tags
Used for pet categories or service types. These should be flat with a 1px Slate border at 10% opacity, or slightly recessed for a "toggled" feel.

### Additional Components
- **Health Chronology:** A vertical timeline using soft-blobs as nodes.
- **Concierge Booking Slider:** A tactile, neumorphic thumb-slider for selecting appointment times.
- **Pet Profiles:** Circular avatars with a "carved" frame effect.