---
name: Audiophile-Industrial
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#bacbbc'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#849587'
  outline-variant: '#3b4a3f'
  surface-tint: '#00e38c'
  primary: '#fafff8'
  on-primary: '#00391f'
  primary-container: '#3dffa3'
  on-primary-container: '#007244'
  inverse-primary: '#006d40'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#fafeff'
  on-tertiary: '#313030'
  tertiary-container: '#e3e0df'
  on-tertiary-container: '#646363'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#55ffa8'
  primary-fixed-dim: '#00e38c'
  on-primary-fixed: '#002110'
  on-primary-fixed-variant: '#00522f'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-lg:
    fontFamily: spaceGrotesk
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-sm:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0.1em
  label-caps:
    fontFamily: spaceGrotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  panel-gap: 2px
  container-padding: 12px
---

## Brand & Style

This design system is engineered for professional audio engineers and high-end video creators. The personality is clinical, authoritative, and rugged, drawing inspiration from high-fidelity rack-mounted hardware and industrial precision tools. It avoids decorative softness in favor of functional density and technical clarity.

The visual style is a hybrid of **Minimalism** and **Brutalism**, filtered through a high-end dark-mode lens. It utilizes a "Utility-First" philosophy where every pixel serves a data-driven purpose. Atmospheric depth is achieved not through shadows, but through subtle metallic textures and tonal layering that mimics brushed aluminum and matte polycarbonate surfaces. The emotional goal is to instill a sense of absolute control and surgical accuracy.

## Colors

The palette is anchored in a "Void" aesthetic, utilizing **Matte Black (#0A0A0A)** for the deepest background layers to maximize contrast with active elements. **Charcoal (#121212)** serves as the primary surface color for containers and panels, creating a subtle distinction from the base.

**Neon Mint (#3DFFA3)** is the sole high-energy accent. It is used exclusively for interactive states, critical data visualizations (like active waveforms), and "On" indicators. For data-heavy layouts, use varying opacities of Neon Mint (e.g., 10%, 40%) to create visual hierarchy without introducing new hues. Functional status colors should be muted: a desaturated red for clipping/error and a cold amber for warnings, ensuring they do not compete with the primary Neon Mint signature.

## Typography

The typography strategy distinguishes between **Operational UI** and **Technical Data**. **Inter** is used for interface elements like menus, settings, and descriptive text to ensure maximum legibility and a neutral professional tone.

**Space Grotesk** is utilized for all numerical readouts, labels, and metadata. Its geometric and technical structure mimics digital readouts found on professional hardware. For data visualizations, such as decibel meters and timestamps, use the Mono-spaced features of the font to prevent layout shifting during real-time value updates. Large headlines should be tight and impactful, while small labels must always be uppercase with generous letter spacing to maintain legibility against dark backgrounds.

## Layout & Spacing

This design system employs a **Fixed Grid** model for the primary workspace to simulate a hardware console. The layout is divided into modular "Racks" or panels. Use a strict 4px baseline grid to ensure all technical elements—like sliders and level meters—align perfectly.

Panels should be separated by minimal **2px gaps**, creating a "joined-chassis" look rather than floating cards. Content density is high; margins are kept tight (24px) to maximize the "screen estate" for waveforms and multi-track timelines. Use vertical rhythm to group related controls, mimicking the physical grouping of knobs and switches on an outboard audio processor.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Bold Borders** rather than traditional drop shadows. Surfaces do not "float"; they are "etched" or "mounted."

1.  **Level 0 (Base):** Matte Black (#0A0A0A) - used for the primary application background.
2.  **Level 1 (Panels):** Charcoal (#121212) - used for the main workspace modules.
3.  **Level 2 (Active Elements):** A 1px solid border of #2A2A2A defines the perimeter of internal sections.
4.  **Level 3 (Interaction):** Inner glows or "inset" shadows are used on buttons and input fields to simulate physical depression into a metal surface.

To add texture, apply a subtle noise grain (2% opacity) or a fine vertical brushed-metal CSS gradient to Level 1 surfaces.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. This reinforces the industrial, precision-tooled aesthetic. All buttons, input fields, panels, and data bars must have 90-degree corners. 

Waveforms and graphic elements should follow this "stepped" logic—avoiding smooth splines in favor of high-frequency, jagged peaks that represent raw audio data. Progress bars and meters should be segmented into blocks rather than continuous fills, referencing classic LED VU meters.

## Components

**Buttons:** Solid Matte Black backgrounds with a 1px border. In the default state, the border is #333. In the hover or active state, the border and text transition to Neon Mint (#3DFFA3). No rounded corners.

**Input Fields:** Recessed appearance using an internal 1px shadow. Text is always Space Grotesk. Labels are placed above the field in `label-caps` style.

**Meters & Gauges:** Horizontal or vertical bars composed of segmented blocks. The "Peak" of the meter should use Neon Mint, while the "Floor" uses a dimmed version (#1A4D36).

**Cards/Panels:** These are "Modules." They feature a header bar with a subtle metallic gradient and the module name in `label-caps`. 

**Waveform Display:** The background is Matte Black with a faint #121212 grid overlay. The waveform itself is rendered in Neon Mint with a 1px stroke.

**Knobs/Dials:** Use a circular vector with a single "indicator notch" in Neon Mint. Interaction should be vertical drag, mimicking the tactile feel of high-end pots.