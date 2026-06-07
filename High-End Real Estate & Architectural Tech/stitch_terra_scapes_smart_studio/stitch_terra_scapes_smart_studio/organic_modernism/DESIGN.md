---
name: Organic Modernism
colors:
  surface: '#fff8f6'
  surface-dim: '#e7d7d2'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1ed'
  surface-container: '#fceae5'
  surface-container-high: '#f6e5e0'
  surface-container-highest: '#f0dfda'
  on-surface: '#221a17'
  on-surface-variant: '#55433d'
  inverse-surface: '#382e2b'
  inverse-on-surface: '#feede8'
  outline: '#88726c'
  outline-variant: '#dbc1b9'
  surface-tint: '#97472b'
  primary: '#944428'
  on-primary: '#ffffff'
  primary-container: '#b35c3e'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb59d'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#006764'
  on-tertiary: '#ffffff'
  tertiary-container: '#00827f'
  on-tertiary-container: '#f1fffd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#ffb59d'
  on-primary-fixed: '#390c00'
  on-primary-fixed-variant: '#793016'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#92f3ef'
  tertiary-fixed-dim: '#75d6d2'
  on-tertiary-fixed: '#00201f'
  on-tertiary-fixed-variant: '#00504e'
  background: '#fff8f6'
  on-background: '#221a17'
  surface-variant: '#f0dfda'
typography:
  display:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h1:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h2:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  h3:
    fontFamily: Montserrat
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
  label-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  xs: 0.25rem
  sm: 0.5rem
  md: 1rem
  lg: 1.5rem
  xl: 2.5rem
  xxl: 4rem
  gutter: 1.5rem
  margin: 2rem
---

## Brand & Style

This design system establishes a high-end visual language for the intersection of luxury landscaping and advanced outdoor technology. The brand personality is rooted in "Organic Modernism"—a philosophy that balances the raw, tactile beauty of the natural world with the precision and reliability of modern engineering.

The UI avoids the harshness of traditional tech interfaces, opting instead for a Soft-UI (Neumorphic) aesthetic. This approach creates a "tactile digital" experience where elements appear to be molded from the physical surface of the screen. The emotional response should be one of serenity, sophistication, and trust. Visuals are characterized by high-quality nature-inspired textures (such as subtle stone grain or leaf vein patterns), flowing organic shapes, and a professional, uncluttered layout.

## Colors

The palette is anchored by **Earthy Terracotta**, a primary hue that evokes sun-baked clay and natural warmth. This is paired with **Slate Gray** for secondary accents and functional elements, providing a grounded, professional contrast. 

The background is a crisp **Off-White**, specifically tuned with a hint of warmth to prevent the "sterile" feel of pure white and to complement the terracotta tones. For the neumorphic effects, we utilize two specific shadow tones: a pure white for high-side highlights and a muted, warm-tinted gray for the low-side shadows, ensuring the "soft" extrusion looks integrated into the surface rather than floating above it.

## Typography

This design system utilizes **Montserrat** for headings to convey a bold, urban, and geometric confidence. Headings should be used with tight tracking in larger sizes to maintain a high-end editorial feel. 

**Manrope** is selected for body text and labels due to its refined, modern, and balanced proportions. Its generous x-height ensures readability across mobile and desktop applications. Typography should be used sparingly, allowing the generous whitespace to frame the text as a core design element rather than just information.

## Layout & Spacing

The layout philosophy follows a **fixed grid** model for desktop and tablet views, centering content within a maximum width to maintain a sense of containment and luxury. A 12-column system is used with generous gutters to provide "breathing room."

Spacing is aggressive; margins between sections should lean towards the `xxl` (64px) or larger scale. This deliberate use of whitespace signals that the brand is not rushed, prioritizing clarity and premium presentation over information density. All spatial relationships follow an 8px base rhythm to ensure mathematical harmony.

## Elevation & Depth

Depth in this design system is achieved through **Soft-UI Neumorphism**. Instead of traditional drop shadows that imply an object floating at different heights, elements appear to be part of the background material itself.

1.  **Raised Elements:** Use a dual-shadow approach. A light highlight (White, 100% opacity, 10px-20px blur) on the top-left and a soft dark shadow (Slate/Terracotta mix, 15% opacity, 10px-20px blur) on the bottom-right.
2.  **Sunken Elements:** Used for active states and input fields. Use inner shadows with the same dual-directional light logic.
3.  **Tonal Layers:** For complex dashboards, use extremely subtle shifts in background color (within the off-white range) to define zones without breaking the "extruded surface" illusion.

## Shapes

The shape language is primarily **Rounded**, moving away from clinical sharp corners toward more natural, organic radii. While the default `rounded-md` is 8px, large interactive cards should utilize `rounded-xl` (24px) or custom asymmetrical organic blobs to mimic stones or foliage. 

All buttons should have significant rounding to feel comfortable and "touchable." Continuous curves (squiurcles) are preferred over standard border-radius where the technology allows, enhancing the organic-modern aesthetic.

## Components

### Buttons
Buttons are the primary expression of the Soft-UI style.
*   **Primary:** Raised terracotta surface with white Montserrat text.
*   **Secondary:** Raised off-white surface with slate gray text.
*   **Interactive State:** Upon hover, the shadow softens; upon click, the button transitions to an "inset" (sunken) shadow state to simulate a physical press.

### Cards & Containers
Cards should be treated as soft extrusions from the background. For high-end product showcases, apply a very subtle grain texture overlay (2% opacity) to the card surface to simulate natural stone or premium matte plastic.

### Selection Cards
Used for landscape packages or tech options. These use organic, non-uniform shapes (slightly "blobby" but professional) rather than perfect rectangles. 

### Input Fields
Inputs are always "sunken" into the UI. Use a soft inner shadow to create a well-defined area for data entry, maintaining the earthy terracotta for the cursor and focus outlines.

### Chips & Tags
Small, pill-shaped elements using the secondary slate gray with high transparency. They should appear "etched" into the surface rather than raised.

### Specialized Components
*   **Weather/Status Tiles:** Neumorphic squares with blurred glass icons representing outdoor conditions.
*   **Botanical Lists:** List items separated by generous whitespace and subtle, organic dividers (e.g., a line that looks like a hand-drawn stroke rather than a digital vector).