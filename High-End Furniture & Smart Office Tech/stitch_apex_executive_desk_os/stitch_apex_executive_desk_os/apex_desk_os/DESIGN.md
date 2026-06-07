---
name: Apex-Desk OS
colors:
  surface: '#121317'
  surface-dim: '#121317'
  surface-bright: '#38393d'
  surface-container-lowest: '#0c0e12'
  surface-container-low: '#1a1c1f'
  surface-container: '#1e2023'
  surface-container-high: '#282a2e'
  surface-container-highest: '#333539'
  on-surface: '#e2e2e7'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e2e2e7'
  inverse-on-surface: '#2f3034'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6cb'
  on-secondary: '#2f3034'
  secondary-container: '#46464b'
  on-secondary-container: '#b5b4ba'
  tertiary: '#adc6ff'
  on-tertiary: '#002e69'
  tertiary-container: '#00112f'
  on-tertiary-container: '#0079fc'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46464b'
  tertiary-fixed: '#d8e2ff'
  tertiary-fixed-dim: '#adc6ff'
  on-tertiary-fixed: '#001a41'
  on-tertiary-fixed-variant: '#004493'
  background: '#121317'
  on-background: '#e2e2e7'
  surface-variant: '#333539'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-xs:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  panel-padding: 24px
  control-gap: 8px
---

## Brand & Style

This design system is engineered for the executive environment, blending high-performance computing aesthetics with premium furniture craftsmanship. The personality is authoritative, precise, and unobtrusive. It targets high-level professionals who demand a workspace that functions as a sophisticated instrument rather than a consumer gadget.

The visual style is **Minimalist-Technical**. It utilizes a dark, low-glare foundation to reduce eye strain in modern office lighting, paired with metallic textures that mirror physical desk hardware. The emotional response is one of absolute control and stability, achieved through a "hardware-first" UI approach where every digital element feels like a tactile, machined component.

## Colors

The palette is strictly controlled to maintain a focused, executive atmosphere.

*   **Matte Black (#121212):** The primary surface color, providing a deep, non-reflective base that allows hardware-style controls to pop.
*   **Brushed Steel (#8E8E93 / #D1D1D6):** Used for structural elements, borders, and secondary text to simulate high-grade aluminum or steel.
*   **Sky Blue (#007AFF):** Reserved exclusively for interactive states, active data streams, and critical system feedback.
*   **Success/Warning/Danger:** Use high-saturation variants of Green (#30D158) and Red (#FF453A) but only in thin, 1px strokes or micro-indicators to maintain the minimalist aesthetic.

## Typography

This design system utilizes **Inter** for all primary interface elements to ensure maximum legibility at high speeds and varying viewing distances. For technical readouts, height coordinates, and telemetry data, **JetBrains Mono** is employed to provide a precise, instrument-panel feel.

Headlines should be tight and impactful. Body text is prioritized for clarity. Labels use heavy-weight, uppercase styling to mimic the engraved labels found on professional machinery.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy, organizing the interface into rigid, functional zones that correspond to physical ergonomic reaches. A 12-column grid is used for the primary dashboard, while side-docked controls use fixed-pixel widths (80px for icons, 320px for expanded menus).

Spacing is governed by a 4px base unit, ensuring all components align with mathematical precision. High-density layouts are preferred for data visualization, while "Executive Views" utilize generous 32px margins to emphasize focus on a single metric, such as current desk height or calorie burn.

## Elevation & Depth

Depth is achieved through **Tonal Layers** and subtle physical metaphors rather than traditional shadows.

1.  **Base Layer:** The Matte Black (#121212) floor.
2.  **Inset Surfaces:** Components like input fields and inactive sliders use "pressed" effects—1px inner strokes with a slightly darker fill (#0A0A0A) to look like they are milled into the surface.
3.  **Raised Surfaces:** Interactive panels use a subtle vertical gradient (from #1E1E1E to #121212) and a 1px top-edge highlight in Brushed Steel (#8E8E93) to simulate a beveled edge.
4.  **Interactive Glow:** Active components do not use shadows; instead, they emit a soft Sky Blue (#007AFF) outer glow (blur: 12px, opacity: 0.2) to indicate system engagement.

## Shapes

The shape language is "Soft-Industrial." Corners are not sharp (which feels aggressive) nor overly rounded (which feels consumer-grade). A consistent **0.25rem (4px)** radius is applied to all primary controls, mimicking the slight edge-rounding of CNC-machined metal.

Large containers and dashboard panels should maintain this 4px radius. Circular elements are used exclusively for toggle switches and status indicators to differentiate them from actionable rectangular buttons.

## Components

*   **Buttons:** Rectangular with a 1px Brushed Steel border. In their default state, they are ghost-styled. On hover, the border glows Sky Blue. On "active" or "pressed" states, the fill becomes Sky Blue with Matte Black text.
*   **Height Sliders:** Large-scale vertical or horizontal tracks. The track is inset (darker than background), and the "handle" is a Brushed Steel block with a Sky Blue LED-style indicator line in the center.
*   **Data Readouts:** Use JetBrains Mono for numbers. Large metrics should be high-contrast (Brushed Steel on Matte Black) with a secondary Sky Blue sparkline graph for historical context.
*   **Switches:** Low-profile toggle sliders. The "Off" state is Matte Black; the "On" state fills the track with Sky Blue.
*   **Status Chips:** Small, rectangular labels with a subtle Brushed Steel border and mono-spaced text. They should appear like physical stickers or engraved plates.
*   **Segmented Controls:** Used for preset heights (e.g., "Sit", "Stand", "Focus"). These should look like a single piece of milled aluminum with divider lines, where the selected segment is illuminated from beneath with a Blue highlight.
*   **Dials:** For fine-tuning height or lighting, use a "Knurled" texture effect—a series of thin vertical lines within a circular component to suggest tactile grip.