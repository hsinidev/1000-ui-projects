---
name: Optic-Draft
colors:
  surface: '#0f131f'
  surface-dim: '#0f131f'
  surface-bright: '#353946'
  surface-container-lowest: '#0a0e1a'
  surface-container-low: '#171b28'
  surface-container: '#1b1f2c'
  surface-container-high: '#262a37'
  surface-container-highest: '#313442'
  on-surface: '#dfe2f3'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#dfe2f3'
  inverse-on-surface: '#2c303d'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#f7f6ff'
  on-tertiary: '#283044'
  tertiary-container: '#d3daf4'
  on-tertiary-container: '#575f75'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#dae2fc'
  tertiary-fixed-dim: '#bec6df'
  on-tertiary-fixed: '#131b2e'
  on-tertiary-fixed-variant: '#3f465b'
  background: '#0f131f'
  on-background: '#dfe2f3'
  surface-variant: '#313442'
typography:
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.02em
spacing:
  unit: 4px
  container-padding: 24px
  gutter: 12px
  panel-gap: 8px
---

## Brand & Style

The design system is engineered for high-precision eyewear diagnostics and bespoke craftsmanship. It evokes the feeling of a professional optical laboratory merged with a high-performance Heads-Up Display (HUD). The brand personality is clinical, futuristic, and meticulously accurate. 

The visual language is defined by a "Technical Glass" aesthetic. It utilizes a dark-mode-first approach to minimize eye strain during digital lens measurements and to allow the Cyan Glow accents to simulate light-emitting diagnostic tools. Users should feel like they are operating a sophisticated piece of optical instrumentation where every pixel serves a functional, data-driven purpose.

## Colors

The palette is rooted in a deep, nocturnal foundation to provide maximum contrast for technical readouts.

- **Primary (Cyan Glow):** Used exclusively for active states, data highlights, and "laser" diagnostic lines. It represents the "optical beam."
- **Secondary (Pure White):** Reserved for high-priority typography and crisp borders.
- **Tertiary (Atmospheric Blue):** A mid-tone used for subtle borders and container backgrounds to prevent pure black "crushing."
- **Neutral (Deep Indigo):** The primary canvas color, providing a sense of depth and specialized environment.

Functional status colors (Success/Warning/Error) should be tinted with the Primary Cyan to maintain palette cohesion, using subtle shifts in hue rather than traditional traffic-light colors where possible.

## Typography

This design system utilizes **JetBrains Mono** across all interfaces to reinforce the technical, monospaced nature of lens prescription data and geometric drafting. 

- **Headlines:** Should be high-contrast (White on Deep Indigo) and often accompanied by a small technical prefix (e.g., "01 // FRAME SELECT").
- **Labels:** Use `label-caps` for all navigational and diagnostic metadata to simulate HUD telemetry.
- **Data Readouts:** Numerical values in diagnostics should use `mono-data` to ensure character alignment in tabular layouts.
- **Hierachy:** Impact is created through weight and case changes rather than large jumps in font size, maintaining a "tight" instrument panel feel.

## Layout & Spacing

The layout philosophy is a **Modular Grid System** inspired by technical blueprints. Information is packed tightly to maximize the visibility of diagnostic data without requiring extensive scrolling.

- **Grid:** A 12-column fluid grid for desktop, collapsing to a 4-column grid for mobile.
- **Tight Rhythm:** Uses a strict 4px baseline. Components are spaced closely (8px or 12px) to feel like integrated parts of a single machine.
- **Margins:** Exterior page margins are kept consistent at 24px, but internal panel padding is reduced to 16px to maintain the "efficient" aesthetic.
- **Responsive Behavior:** On mobile, technical overlays may switch to a vertical "stack" but must retain their thin-border framing to keep the HUD feel.

## Elevation & Depth

Depth in this design system is achieved through light and transparency rather than shadows. 

1. **Glassmorphism:** Panels use a semi-transparent Deep Indigo fill with a high-strength backdrop blur (20px+). This allows "scan-lines" or background diagnostic maps to peek through.
2. **Technical Overlays:** Elements are "stacked" using varying border opacities. A 1px solid border at 20% White represents a background panel, while a 1px border at 100% Cyan represents an active instrument.
3. **Inner Glow:** Instead of drop shadows, active elements utilize a subtle inner glow or a faint outer "bloom" of Cyan Glow (#00F2FF) to suggest an illuminated display screen.
4. **Scan-line Texture:** A global, low-opacity (2-4%) horizontal pattern is applied over the base layer to simulate a cathode-ray or digital sensor feed.

## Shapes

The shape language is **Sharp and Geometric**. To reflect the precision of lens cutting and optical engineering, the design system avoids rounded corners in favor of 90-degree angles.

- **Primary Shapes:** Rectangular panels with hard edges.
- **Diagnostic Elements:** Perfect circles are used exclusively for lens-related diagnostics, focal point indicators, and "eye-tracking" UI elements.
- **Accents:** Use 45-degree clipped corners (chamfers) for buttons or status tags to reinforce the "industrial drafting" style.

## Components

### Buttons & Controls
Buttons are rectangular with 1px borders. The `Primary` state features a full Cyan Glow fill with Black text. The `Ghost` state uses a White border that glows Cyan on hover. Interaction should feel "digital"—instantaneous color shifts without heavy transitions.

### Glass Panels
The foundational container. Must include a 1px border (White at 10% opacity) and a backdrop blur. For high-importance data, a "scan-line" texture should be visible within the panel fill.

### Circular Diagnostics
Specialized components for lens visualization. These include "crosshair" overlays, degree markers (0-360°), and concentric rings that animate slightly to indicate active "scanning" or "calculation" states.

### Input Fields
Inputs are underlined or fully boxed with 1px lines. Labels always sit above the field in `label-caps`. Focus states trigger a "flicker" animation where the border glows Cyan.

### Lists & Tables
Data-heavy lists use alternating background opacities (zebras) at very low levels (3-5%). Vertical dividers are avoided; horizontal rules are thin and extended to the panel edges to mimic blueprint lines.

### Technical Overlays
Small floating tags that provide "telemetry" for specific UI elements (e.g., coordinates, zoom levels, or frame dimensions). These should use the `mono-data` type and be connected to their parent element by a 1px diagonal leader line.