---
name: ArchiView
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c9ac'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9379'
  outline-variant: '#444933'
  surface-tint: '#abd600'
  primary: '#ffffff'
  on-primary: '#283500'
  primary-container: '#c3f400'
  on-primary-container: '#556d00'
  inverse-primary: '#506600'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c3f400'
  primary-fixed-dim: '#abd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
  label-mono-lg:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-mono-sm:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  base: 4px
  unit-1: 4px
  unit-2: 8px
  unit-4: 16px
  unit-6: 24px
  unit-8: 32px
  unit-12: 48px
  unit-16: 64px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 40px
---

## Brand & Style
The design system is engineered for precision, professional-grade architectural visualization, and real-time spatial data. It targets architects, real estate developers, and construction managers who require high-utility interfaces that feel like an extension of their technical tools.

The aesthetic follows a **Blueprint-Tech** movement—a fusion of **Industrial Brutalism** and **Modern Glassmorphism**. It evokes the feeling of a Head-Up Display (HUD) projected onto a physical job site. Key visual motifs include technical wireframes, coordinate system markings, and scanning line overlays that imply real-time environmental processing. The emotional response should be one of total control, surgical accuracy, and cutting-edge technological capability.

## Colors
This design system utilizes a high-contrast, dark-mode-first palette to maximize legibility in varying lighting conditions (on-site outdoors vs. indoor offices). 

- **Matte Black (#121212):** Used as the primary canvas to reduce eye strain and provide a deep "void" for AR elements to pop against.
- **Electric Lime (#CCFF00):** The high-visibility action color. Reserved for interactive states, primary data points, and "active scanning" indicators.
- **Silver (#C0C0C0):** Used for structural elements, secondary labels, and wireframe patterns to mimic industrial materials.
- **Translucency:** For AR overlays, colors are applied to surfaces with 60–80% opacity to maintain environmental awareness.

## Typography
The typography strategy prioritizes "data-dense" readability. **Space Grotesk** is used for headlines and technical labels to provide a geometric, futuristic feel that aligns with architectural drafting. **Inter** is utilized for body copy and descriptions to ensure maximum legibility at smaller scales.

All technical data, coordinates, and measurements must use the label-mono styles. Uppercase styling is preferred for all UI headers and buttons to reinforce the industrial, "stenciled" aesthetic.

## Layout & Spacing
The layout uses a **Rigid Technical Grid** based on 4px increments. For web and tablet interfaces, a 12-column fluid grid is standard. In the AR viewport, a "Safe Zone" margin of 48px is maintained to prevent UI elements from bleeding into the user's peripheral vision.

Spacing should feel deliberate and "engineered." Avoid organic or uneven spacing. Use strict alignment to the grid to mimic blueprint layouts. Components should be spaced using `unit-4` (16px) or `unit-6` (24px) to ensure touch targets are sufficient for field use.

## Elevation & Depth
In this design system, depth is achieved through **Tonal Layering** and **Glassmorphism** rather than traditional drop shadows.

1.  **Floor (Level 0):** Matte Black (#121212) - The base canvas.
2.  **Raised (Level 1):** Dark Grey (#1E1E1E) with a 1px Silver (#C0C0C0) border at 10% opacity.
3.  **Overlay (Level 2):** Frosted glass effect (Backdrop Blur: 12px) with a semi-transparent black fill.
4.  **Active/Focus (Level 3):** Elements gain an outer glow using the Primary Electric Lime at low opacity (15%) to simulate light emission from a screen or projector.

Scanning lines and wireframe patterns are placed at Level 0.5 (between base and raised) to provide texture without interfering with content.

## Shapes
This design system uses **Sharp (0px)** roundedness. All containers, buttons, and input fields must have hard 90-degree corners to reflect the precision of architectural blueprints and industrial hardware. 

Corners may occasionally feature "chamfered" edges (45-degree cuts) for specialized "HUD" elements or primary action buttons to further the military/industrial tech aesthetic. Decorative borders should use 1px stroke weights to maintain a "fine-liner" drafting feel.

## Components
- **Buttons:** Hard-edged, solid Electric Lime for primary actions with black text. Secondary buttons are Ghost-style with a 1px Silver border.
- **Technical Chips:** Used for coordinate data and status tags. These feature a "tag" aesthetic with the label-mono-sm typeface.
- **Input Fields:** Bottom-border only or full 1px Silver border. Focus state turns the border Electric Lime with a subtle scanning-line animation inside the field.
- **Cards:** Transparent backgrounds with 1px Silver borders. Headers of cards should have a "bracket" visual at the corners.
- **Scanning Bar:** A horizontal Electric Lime line with a soft glow that travels vertically across AR viewports to indicate active environment processing.
- **Crosshairs:** Interactive reticles used for point-selection in 3D space, utilizing the Silver color palette with a 50% opacity.
- **Glass Overlays:** Used for side panels in the AR view, featuring high blur and low-opacity fills to ensure the physical environment remains visible behind the UI.