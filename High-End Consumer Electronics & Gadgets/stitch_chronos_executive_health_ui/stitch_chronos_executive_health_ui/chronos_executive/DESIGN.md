---
name: Chronos Executive
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#1f1f1f'
  on-tertiary-container: '#888686'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Montserrat
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-numeric:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '300'
    lineHeight: '1.0'
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin-mobile: 20px
  margin-desktop: 64px
---

## Brand & Style

The design system is engineered for the high-stakes environment of the modern executive. It balances the precision of high-performance horology with the seamless intelligence of advanced wearable technology. The visual language is one of quiet confidence—avoiding loud trends in favor of a timeless, premium aesthetic.

The core style is **Refined Glassmorphism**. This approach utilizes deep, layered translucency to create a sense of physical depth within the interface. By combining frosted textures with razor-sharp gold accents, the UI mimics the look of high-end watch crystals and precision-machined hardware. The emotional response is one of exclusivity, intelligence, and absolute reliability.

## Colors

The color strategy centers on a "Midnight & Metal" philosophy. **Deep Navy** functions as the expansive canvas, providing a softer, more sophisticated alternative to pure black. **Matte Black** is used strategically to define containers and internal depth, creating a structural "chassis" for the data.

**Champagne Gold** is the primary signal color. It is used sparingly but impactfully for critical information, borders, and interactive states. It should always feel like a metallic inlay rather than a flat color fill. 

For data visualizations, utilize high-contrast pairings against the navy background:
- **Primary Data:** Champagne Gold
- **Success/Positive:** Emerald Tint (#50C878)
- **Warning/High Energy:** Ruby Tint (#E0115F)

## Typography

Typography in this design system emphasizes clarity and structural hierarchy. **Montserrat** provides a geometric, architectural feel for headlines, echoing the circular motifs of wearable hardware. **Inter** is used for body text to ensure maximum legibility at various viewing distances and lighting conditions.

For technical data and metrics, **Geist** provides a monospaced-adjacent precision that feels "engineered." All labels should utilize the `label-caps` style to differentiate metadata from primary content. Champagne Gold should be reserved for `display-lg` and key `data-numeric` points to draw the eye immediately to the most vital executive metrics.

## Layout & Spacing

The layout philosophy follows a **Contextual Fluidity** model. For a wearable-focused system, the grid relies heavily on safe margins and center-aligned focus areas. 

- **Vertical Rhythm:** A strict 4px baseline grid ensures alignment across dense data sets.
- **The Golden Ratio:** Use a 1.618 ratio to determine the relationship between primary glass cards and secondary information panels.
- **Safe Zones:** On circular displays, keep all interactive elements within a 15% inner-inset margin to prevent touch-target clipping at the bezel.
- **Desktop/Dashboard:** When viewed on a management console, transition to a 12-column grid with generous 40px margins to maintain an airy, premium feel.

## Elevation & Depth

Depth is achieved through **Optical Layering** rather than traditional shadows.
1.  **Level 0 (Base):** Deep Navy background with a subtle radial gradient (center #002B56 to edges #001F3F).
2.  **Level 1 (Surface):** Matte Black containers with 80% opacity, used for secondary background elements.
3.  **Level 2 (Active Glass):** Glassmorphic cards using a `backdrop-filter: blur(20px)` and a 1px border. The border is a linear gradient: `Champagne Gold (top-left)` to `Transparent (bottom-right)`.
4.  **Level 3 (Interactive):** Elements that are currently being touched or focused gain a subtle outer glow using the Champagne Gold color with a 15% opacity and 20px spread.

Avoid drop shadows; use "inner glows" on borders to simulate the refraction of light through a sapphire crystal watch face.

## Shapes

The shape language is defined by **Precision Geometry**. All primary containers use the `rounded-lg` (16px/1rem) setting to mimic the ergonomic curves of premium tech hardware. 

Buttons and high-level navigation items use a **Pill-shaped** profile to maximize the touch target area and provide a distinct silhouette against the rectangular data cards. Icons should be encased in circular frames or placed on a clear 45-degree angled grid to maintain the technical, "instrument cluster" feel.

## Components

### Buttons
Primary buttons are solid Champagne Gold with Matte Black text. Secondary buttons are "Ghost" style, featuring a 1px Gold border and the glassmorphic blur effect. 

### Glass Cards
The signature component. Use a semi-transparent white fill (5%) with a heavy backdrop blur. The 1px border must be a gold gradient to create a "beveled edge" illusion. Cards should be used to group related executive metrics (e.g., Heart Rate Variability + Stress Score).

### Data Visualizations
Charts should avoid filled areas. Use thin, high-contrast strokes. "Ring" charts (donuts) are preferred for progress metrics, utilizing a 270-degree arc rather than a full circle to imply a more sophisticated, gauge-like aesthetic.

### Input Fields
Inputs are bottom-border only when inactive, turning into a fully encased Matte Black glass container when focused. Use Champagne Gold for the blinking cursor and label transition.

### Lists
List items are separated by a subtle 1px "Dividing Beam"—a line that is Champagne Gold at 20% opacity, tapering off to transparent at both ends.