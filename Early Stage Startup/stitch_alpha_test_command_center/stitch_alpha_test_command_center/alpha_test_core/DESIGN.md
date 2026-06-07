---
name: ALPHA-TEST CORE
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#494949'
  on-secondary-container: '#b9b8b8'
  tertiary: '#fff7e9'
  on-tertiary: '#3b2f00'
  tertiary-container: '#ffd93d'
  on-tertiary-container: '#725e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#e4e2e2'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#ffe173'
  tertiary-fixed-dim: '#e8c426'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.05em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  technical-data:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  body-base:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
---

## Brand & Style

The design system is engineered for high-stakes beta management, where clarity and technical precision are paramount. The aesthetic is **Brutalist-Technical**, drawing inspiration from kernel debuggers, terminal interfaces, and industrial command centers. 

The visual language rejects modern softness in favor of raw, high-contrast utility. It is designed to evoke a sense of "system-level" access, positioning the user as an operator rather than a consumer. The emotional response should be one of focus, authority, and analytical rigor.

**Key Visual Principles:**
- **Zero-Softness:** Absolute rejection of border radii.
- **High Information Density:** Maximum data visibility with minimal decorative padding.
- **Active Illumination:** Using "glow" and high-chroma accents to denote system activity and focus.
- **Synthetic Texture:** Subtle scanline overlays to reinforce the hardware-interface metaphor.

## Colors

The palette is strictly functional, utilizing a deep matte foundation to allow technical data to "pop" with phosphor-like intensity.

- **Primary (Cyber-Cyan):** Reserved for critical actions, active states, and primary data points. It represents the "powered-on" state of the system.
- **Background (Matte Black):** A non-reflective base that minimizes eye strain during long debugging sessions and maximizes contrast.
- **Surface & Borders (Slate Grey):** Two tiers of grey are used to define the structural grid. `#2E2E2E` is for inactive structural containers, while `#4A4A4A` is used for interactive boundaries and secondary data.
- **Functional Accents:** While not in the primary palette, standard status colors (Red for 'Critical', Amber for 'Warning') should be used sparingly but with maximum saturation.

## Typography

This design system utilizes a dual-font strategy to balance character with readability.

1.  **Technical/Header Layer:** Uses **Space Grotesk** for its geometric, engineered feel. For raw data outputs and terminal-style logs, a standard **Monospace** stack (JetBrains Mono, Fira Code, or system monospace) must be used to ensure character alignment and a "codebase" aesthetic.
2.  **Interface Layer:** Uses **Inter** for all body copy and descriptive text. Its neutral, utilitarian design ensures that high volumes of documentation remain legible against the high-contrast background.

All headers should be set with tight letter-spacing to feel "compacted," while labels should be uppercase with wide tracking to mimic industrial equipment marking.

## Layout & Spacing

The layout is governed by a **Rigid Grid System**. Everything aligns to a 4px baseline to maintain mathematical consistency.

- **Grid:** A 12-column fluid grid is used for primary page structures. 
- **Gutters:** Tight 16px gutters reinforce the "dense" debugger feel.
- **Borders as Spacing:** In this design system, borders are not just decorative; they are structural. Use 1px solid lines to separate all logical sections.
- **Density:** Favor "Compact" spacing. Information density is a feature, not a bug. Padding within cards and containers should be kept to the minimum required for legibility (usually 16px or 20px).

## Elevation & Depth

Standard shadows are prohibited. Depth in this design system is achieved through **Illumination and Layering**, not gravity.

- **Level 0 (Floor):** Matte Black (#121212). The base system state.
- **Level 1 (Panels):** Defined by a 1px Slate Grey (#2E2E2E) border. No change in background color.
- **Active State (Glow):** When an element is focused or active, it receives a "Cyber-Cyan" border and a subtle outer glow (0px blur, or very tight 2-4px spread) to simulate a cathode-ray tube (CRT) effect.
- **Overlays:** Modals and tooltips should have a solid Matte Black background with a high-contrast Slate Grey (#4A4A4A) border.
- **Texture:** Apply a global, low-opacity (2-3%) scanline overlay (horizontal 2px stripes) across the entire UI to provide a tactile, hardware feel.

## Shapes

The shape language is **Strictly Orthogonal**. 

- **Corner Radius:** 0px across all elements (Buttons, Cards, Inputs, Modals).
- **Icons:** Use stroke-based icons with sharp angles. Avoid rounded terminals on icon paths.
- **Dividers:** Use 1px vertical or horizontal lines. 
- **Visual Accents:** Use 45-degree "clipped corners" (achieved via CSS clip-path or linear-gradients) for decorative elements or primary button edges to evoke a "military-spec" appearance.

## Components

### Buttons
- **Primary:** Solid Cyber-Cyan background with Matte Black text. No rounding. Hover state adds a cyan outer glow.
- **Secondary:** Transparent background, 1px Slate Grey border. Text in Slate Grey. Hover turns border to Cyber-Cyan.
- **Ghost:** Monospace text with a `[ ]` bracket prefix and suffix.

### Input Fields
- **Default:** Transparent background with a bottom-only 1px border in Slate Grey. 
- **Focus:** Border shifts to Cyber-Cyan with a solid vertical "block cursor" blinking at the end of the text string.
- **Labels:** Always displayed above the input in `label-caps` typography.

### Cards / Modules
- **Container:** 1px Slate Grey (#2E2E2E) border. 
- **Header:** A dedicated top bar within the card, separated by a 1px line, containing the module title in `label-caps`.
- **Active:** If the card is a selectable item, the border glows Cyber-Cyan when active.

### Feedback & Status
- **Scanlines:** Active loading states should feature a "moving" scanline highlight that travels vertically across the component.
- **Progress Bars:** Block-based (segmented) rather than a smooth continuous fill, resembling vintage loading sequences.

### Specialized Components
- **Terminal Output:** A dedicated component for log data using a slightly darker background (#0A0A0A) and Monospace font.
- **Status Pills:** Rectangular blocks with high-contrast text. No rounded ends.