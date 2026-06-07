---
name: Aeronaut
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#3f484c'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#6f787d'
  outline-variant: '#bfc8cd'
  surface-tint: '#0c6780'
  primary: '#0c6780'
  on-primary: '#ffffff'
  primary-container: '#87ceeb'
  on-primary-container: '#005870'
  inverse-primary: '#89d0ed'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e2'
  on-secondary-container: '#636465'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#c3c4c4'
  on-tertiary-container: '#4f5151'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#baeaff'
  primary-fixed-dim: '#89d0ed'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#004d62'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 80px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-gap: 160px
---

## Brand & Style

The brand personality of this design system is one of liberation, precision, and breathtaking clarity. It targets thrill-seekers and professionals who find peace in high-altitude environments. The UI must evoke a feeling of weightlessness—as if the interface itself is suspended in the stratosphere.

The chosen style is **Minimalism** with a heavy emphasis on **High-Contrast** and **Thin-Line** aesthetics. By utilizing vast amounts of whitespace (representing the sky) and hairline strokes (representing technical precision and gear), the design system creates a sense of openness and verticality. Navigation and content should feel unburdened, avoiding heavy blocks or dark fills in favor of light, ethereal compositions.

## Colors

The color palette is strictly limited to mimic the atmosphere at 10,000 feet. **Sky Blue (#87CEEB)** serves as the primary action color, used sparingly for critical interactive elements and highlights to maintain its impact. **White (#FFFFFF)** is the dominant surface color, ensuring the interface feels expansive. **Cloud Grey (#D3D3D3)** provides the necessary depth for borders, secondary text, and subtle structural divisions.

To ensure accessibility and the "High-Contrast" requirement, a deep charcoal/black (#1A1A1A) is used for primary typography against the white background. This stark contrast ensures readability even in high-glare, outdoor environments typical of aerial sports.

## Typography

This design system utilizes **Space Grotesk** for headlines to lean into a technical, futuristic, and geometric aesthetic that mirrors aeronautical instrumentation. Headlines should be set with tight tracking and light weights to maintain a sophisticated, "thin-line" feel.

For body text and functional labels, **Lexend** is employed. Its design was specifically optimized for readability and has an athletic, clear cadence that fits the "extreme sports" context. Large-scale display text should use a "Light" weight (300) to emphasize the airy nature of the system, while uppercase labels with increased letter spacing are used for navigational headers and metadata to provide a sense of technical organization.

## Layout & Spacing

The layout philosophy is a **Fixed Grid** with extreme internal padding. A 12-column grid is used for desktop, but the "airy" feel is achieved through unusually large vertical gaps (`section-gap`) between content blocks, preventing the UI from ever feeling cluttered.

Margins are generous (64px+) to create a frame that pushes content toward the center, mimicking a view through a cockpit or goggles. Elements should never feel "packed"; if in doubt, double the whitespace. Alignment should be precise and predominantly left-aligned or centered to maintain a clean, architectural vertical axis.

## Elevation & Depth

To maintain the sense of altitude without sacrificing minimalism, this design system rejects heavy shadows. Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**.

Depth is communicated through:
1.  **Hairline Strokes:** 1px borders in Cloud Grey (#D3D3D3) or a semi-transparent Sky Blue to define boundaries.
2.  **Layered White:** Using subtle shifts between White (#FFFFFF) and a very faint version of Cloud Grey to distinguish between the background and elevated surfaces (like cards).
3.  **Translucency:** Occasional use of background blurs (frosted glass) on navigation bars to suggest the presence of clouds or atmosphere behind the UI.

## Shapes

The shape language is strictly **Sharp (0)**. To evoke the precision of aeronautical engineering and the "edge" of extreme sports, all containers, buttons, and input fields utilize 90-degree corners. 

Any visual softness should come from the color palette and whitespace, not the geometry. Rectilinear shapes provide a high-contrast, modern structure that feels intentional and professional. Thin 1px lines should be the primary method for defining these shapes.

## Components

**Buttons:**
Primary buttons are transparent with a 1px Sky Blue border and Sky Blue text. On hover, they transition to a solid Sky Blue fill with White text. Secondary buttons use the Cloud Grey for borders. All buttons are rectangular with no corner radius.

**Input Fields:**
Inputs are defined by a single bottom border (1px Cloud Grey). When focused, the border transitions to Sky Blue. Labels sit above the line in the "label-caps" typographic style.

**Cards:**
Cards do not have shadows. They are defined by a 1px Cloud Grey border or a slightly off-white background fill. Content within cards must maintain at least 40px of internal padding to preserve the "airy" aesthetic.

**Chips/Tags:**
Used for sport categories (e.g., "Skydiving", "Base Jumping"). These are small, uppercase text elements surrounded by a thin 1px Cloud Grey border.

**Progress Indicators:**
For "altitude" or "skill levels," use thin horizontal lines. The background line is Cloud Grey, and the progress fill is Sky Blue.

**Additional Components:**
- **Vertical Rule:** Use long, thin vertical lines to separate columns of text, reinforcing the sense of "altitude" and downward movement.
- **Iconography:** Icons must be "Stroked" (outline only) with a consistent 1px weight to match the typography and border system. Avoid solid-fill icons.