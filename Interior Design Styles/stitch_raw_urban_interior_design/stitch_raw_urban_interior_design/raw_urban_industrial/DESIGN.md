---
name: Raw Urban Industrial
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d9c2b9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a18c85'
  outline-variant: '#53433d'
  surface-tint: '#ffb598'
  primary: '#ffb598'
  on-primary: '#562005'
  primary-container: '#a45c3d'
  on-primary-container: '#fff1ec'
  inverse-primary: '#904c2e'
  secondary: '#c0c8cd'
  on-secondary: '#2a3136'
  secondary-container: '#424a4f'
  on-secondary-container: '#b2b9bf'
  tertiary: '#e9c349'
  on-tertiary: '#3c2f00'
  tertiary-container: '#cca72f'
  on-tertiary-container: '#4e3d00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb598'
  on-primary-fixed: '#360f00'
  on-primary-fixed-variant: '#723519'
  secondary-fixed: '#dce4e9'
  secondary-fixed-dim: '#c0c8cd'
  on-secondary-fixed: '#151d21'
  on-secondary-fixed-variant: '#40484c'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
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
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-tech:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 20px
  margin-desktop: 64px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style
The design system is rooted in the "Raw Urban" aesthetic, channeling the atmosphere of a converted industrial loft. It targets an audience that appreciates the intersection of gritty reality and high-end sophistication—architects, urban explorers, and curators of luxury industrial goods. 

The visual style is a blend of **Tactile Brutalism** and **Modern Architectural** design. It emphasizes structural honesty, utilizing high-fidelity textures like weathered steel, textured concrete, and supple leather to create a sense of physical weight. The emotional response is one of authority, permanence, and uncompromising quality. Every element should feel engineered rather than merely "designed," prioritizing a mobile-first experience that leverages high-contrast photography to break through the utilitarian framework.

## Colors
The palette is dominated by "Charcoal" and "Concrete Grey," providing a dark, industrial foundation. The primary accent is "Warm Leather" (#A45C3D), used to provide a human, organic touch against the coldness of "Weathered Steel" (#71797E). 

The design system operates exclusively in a dark-mode-first environment. High-contrast white is reserved for critical information and calls to action, while muted brass or gold tones serve as tertiary accents for premium detailing. Use subtle noise overlays on background surfaces to mimic the texture of cast concrete and brushed metal.

## Typography
This design system utilizes a "Serif-heavy" hierarchy to command authority. **Newsreader** is the voice of the system, used for all headlines to evoke a literary, editorial, and sophisticated feel. Its slightly traditional forms contrast sharply with the industrial environment.

**Work Sans** provides a grounded, neutral base for body copy, ensuring high readability against dark, textured backgrounds. For technical data, metadata, and navigational labels, **Space Grotesk** is used to introduce a geometric, "engineered" quality that reinforces the architectural theme. Always use all-caps for labels to mimic blueprint annotations.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy with a rigid 8px baseline rhythm. For mobile-first delivery, the system uses a 4-column grid with generous 20px side margins to ensure content feels framed like a gallery piece. 

In desktop views, the system shifts to a 12-column grid. Spacing is intentionally "airy" in some areas to provide a sense of loft-style scale, while technical components are tightly packed into "control clusters." Use heavy vertical borders (2px+) in Charcoal or Weathered Steel to separate sections, rather than relying solely on whitespace, to maintain the architectural structure.

## Elevation & Depth
Depth is achieved through **Tonal Layers** and **Tactile Textures** rather than traditional shadows. Surfaces do not "float"; they are "stacked" or "inset."

1.  **Base:** The lowest level, representing the raw concrete shell (deepest charcoal).
2.  **Raised Plinths:** Secondary surfaces (Concrete Grey) use subtle 1px inner borders to appear as if they are slabs laid on top of the base.
3.  **Insets:** Input fields and secondary containers use "inner shadows" to appear carved into the surface.
4.  **Glass overlays:** For mobile navigation, a heavy backdrop blur (30px+) with a 10% white tint mimics the look of frosted industrial glass or reinforced partitions.

## Shapes
The shape language is strictly **Sharp (0px)**. To maintain the architectural and "Raw" integrity, rounded corners are avoided entirely. All buttons, cards, and input fields must have 90-degree angles to mimic the cut of steel beams and stone slabs. 

The only exception is for circular iconography or user avatars, which should be framed in square containers whenever possible to maintain the rigid structural grid.

## Components
-   **Buttons:** Rectangular and heavy. Primary buttons use the "Warm Leather" fill with "Charcoal" Serif text. Secondary buttons use a 2px "Weathered Steel" stroke with no fill.
-   **Cards:** Non-rounded slabs with a 1px solid border. Use high-contrast architectural imagery as the header, with a subtle grainy texture overlay.
-   **Inputs:** Underlined or fully enclosed in a 1px steel border. Labels should use the "Space Grotesk" label-caps style positioned above the field.
-   **Chips/Tags:** Monospaced (Space Grotesk) text inside a solid Steel-colored box. No radius.
-   **Selection Controls:** Checkboxes and Radios are strictly square. When active, they fill with the "Warm Leather" primary color.
-   **Lists:** Separated by 1px horizontal rules that span the full width of the container, mimicking floor-to-ceiling industrial shelving.
-   **Progress Bars:** Thin, high-contrast lines. Use the "Weathered Steel" for the track and the "Warm Leather" or "White" for the indicator.