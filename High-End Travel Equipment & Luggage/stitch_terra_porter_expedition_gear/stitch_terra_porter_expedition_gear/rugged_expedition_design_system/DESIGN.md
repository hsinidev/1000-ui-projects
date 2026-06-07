---
name: Rugged Expedition Design System
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#dec0ba'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#a68b85'
  outline-variant: '#57423e'
  surface-tint: '#ffb4a6'
  primary: '#ffb4a6'
  on-primary: '#650901'
  primary-container: '#c24e3a'
  on-primary-container: '#fff9f8'
  inverse-primary: '#a63a28'
  secondary: '#bbc7da'
  on-secondary: '#25313f'
  secondary-container: '#3c4857'
  on-secondary-container: '#aab6c8'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#747373'
  on-tertiary-container: '#fdfaf9'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a6'
  on-primary-fixed: '#3f0300'
  on-primary-fixed-variant: '#862213'
  secondary-fixed: '#d7e3f6'
  secondary-fixed-dim: '#bbc7da'
  on-secondary-fixed: '#101c2a'
  on-secondary-fixed-variant: '#3c4857'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  h2:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h3:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 48px
  container-max: 1440px
  modular-gap: 1px
---

## Brand & Style

This design system establishes a **Rugged-Luxe** aesthetic, balancing the raw durability of expedition hardware with the refined precision of high-end engineering. The brand personality is authoritative, resilient, and elite—designed for individuals who require gear that performs in extreme conditions without sacrificing aesthetic sophistication.

The visual style is **Tactile and High-Contrast**. It moves away from the "flatness" of modern SaaS, embracing the physical weight of industrial materials. Expect to see weathered textures, brushed metal surfaces, and "battle-tested" imperfections that suggest longevity. The interface should feel like a piece of high-performance equipment—an overbuilt tool that is as much at home in a mountain range as it is in a luxury showroom.

## Colors

The palette is anchored in environmental grit and industrial utility. This design system utilizes a dark-mode default to emphasize high-contrast visibility and to reduce glare in outdoor expedition environments.

- **Earthy Terracotta (#C24E3A):** The primary action color, signifying warmth, safety, and high-visibility markers found on rescue equipment.
- **Slate (#3E4A59):** A secondary functional color used for interactive surfaces and weather-related data visualization.
- **Industrial Grey (#2D2D2D):** The structural foundation, representing the titanium and carbon fiber materials of the gear.
- **Surface Accents:** Use subtle distressing and noise overlays on grey surfaces to mimic the look of powder-coated metal.

## Typography

The typography leverages a high-contrast pairing of technical geometry and utilitarian clarity. 

**Space Grotesk** is utilized for headers and data labels. Its geometric construction and idiosyncratic "tech" apertures provide a cutting-edge feel that mirrors navigation equipment. For headers, use heavy weights and tight tracking to simulate the impact of stamped serial numbers on metal.

**Inter** provides the utilitarian backbone for body copy, chosen for its exceptional legibility at small sizes and its neutral, systematic appearance. Use the "label-caps" style for all technical specifications and gauge readouts to maintain a disciplined, military-spec hierarchy.

## Layout & Spacing

This design system employs a **Fixed Grid** model with a heavy emphasis on modularity. The layout should mimic the organization of a field-kit or a ruggedized equipment case, where every component has a designated, reinforced slot.

- **Modular Grid:** Use a 12-column grid for primary content, but utilize "hard" dividers (1px borders) between sections to emphasize the modular construction.
- **Rhythm:** All spacing must be multiples of 4px. Use generous margins (48px+) to allow the "luxe" aspect of the brand to breathe, but keep internal component padding tight and efficient.
- **Industrial Gaps:** For technical dashboards and gauge clusters, use a 1px gap between elements to create a "panelized" effect.

## Elevation & Depth

Elevation in this design system is achieved through **Tonal Layering and Materiality** rather than traditional soft shadows.

- **Physical Stacking:** Depth is conveyed by overlapping elements with high-contrast borders. A "raised" element should appear as a bolted-on plate rather than a floating card.
- **Weathered Edges:** Use subtle inner shadows and 1px "light-leak" top borders on containers to simulate the beveled edge of a machined metal part.
- **Brushed Textures:** Use subtle SVG noise textures on the background of container tiers to differentiate between "base" surfaces and "interactive" surfaces.
- **Hard Shadows:** When shadows are necessary for legibility, use "hard" 90-degree shadows with 100% opacity, offset by 2px-4px, to reinforce the brutalist, industrial aesthetic.

## Shapes

The shape language is strictly **Sharp (0px)**. 

To maintain the rugged, "overbuilt" feel, all UI elements—including buttons, input fields, and containers—must feature 90-degree corners. This evokes the geometry of hard-shell equipment cases and industrial machinery. 

**Exceptions:** 
- Small chamfered corners (45-degree angled cuts) may be used on the corners of high-level containers or "Expedition" badges to signify reinforced structural points. 
- Circular elements are reserved exclusively for functional gauges (weather gauges, compasses, or performance dials).

## Components

Components must look "battle-tested" and mechanical.

- **Buttons:** Use the primary Terracotta (#C24E3A) for main actions. Buttons should have a 2px solid border in a darker shade of the background color and use "label-caps" typography. Add a subtle "scratched" texture overlay on hover.
- **Weather-Resistance Gauges:** Circular dials featuring thin, high-contrast Slate (#3E4A59) strokes. Use Space Grotesk for real-time numerical data. Gauges should look like physical analog-digital hybrids.
- **Video Containers:** High-performance containers must feature "technical brackets" on the corners and an active "REC" or "LIVE" status indicator in the top right.
- **Input Fields:** Styled as "recessed" panels. Use a darker tertiary background with a 1px border. Focus states should trigger a high-contrast Terracotta glow on the border only.
- **Industrial Metal Accents:** Use 1px vertical or horizontal lines with a metallic gradient to separate technical data points.
- **Chips/Status Tags:** Styled as ruggedized fabric patches or stamped metal plates, using "label-caps" text and high-contrast backgrounds.