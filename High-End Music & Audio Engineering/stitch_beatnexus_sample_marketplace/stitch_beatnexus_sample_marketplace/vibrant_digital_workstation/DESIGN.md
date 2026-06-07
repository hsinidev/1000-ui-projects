---
name: Vibrant Digital Workstation
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e5bcc4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#ac878f'
  outline-variant: '#5c3f45'
  surface-tint: '#ffb1c3'
  primary: '#ffb1c3'
  on-primary: '#66002c'
  primary-container: '#ff4b89'
  on-primary-container: '#590026'
  inverse-primary: '#bb0058'
  secondary: '#bdf4ff'
  on-secondary: '#00363d'
  secondary-container: '#00e3fd'
  on-secondary-container: '#00616d'
  tertiary: '#d1bcff'
  on-tertiary: '#3c0090'
  tertiary-container: '#a178ff'
  on-tertiary-container: '#34007f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffd9e0'
  primary-fixed-dim: '#ffb1c3'
  on-primary-fixed: '#3f0019'
  on-primary-fixed-variant: '#8f0041'
  secondary-fixed: '#9cf0ff'
  secondary-fixed-dim: '#00daf3'
  on-secondary-fixed: '#001f24'
  on-secondary-fixed-variant: '#004f58'
  tertiary-fixed: '#e9ddff'
  tertiary-fixed-dim: '#d1bcff'
  on-tertiary-fixed: '#23005b'
  on-tertiary-fixed-variant: '#5700c9'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 80px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.0'
spacing:
  unit: 8px
  gutter: 24px
  margin: 48px
  container-max: 1440px
---

## Brand & Style

This design system establishes a high-energy, premium digital environment tailored for professional music producers. The brand personality is aggressive, innovative, and precise. It draws heavily from **Vaporwave-infused Brutalism** and **Glassmorphism**, merging the raw edge of a technical workstation with the vibrant pulse of modern electronic music culture.

The UI must evoke the feeling of a "Night Mode" studio—intense, focused, and high-contrast. Key visual signatures include:
- **Overlapping Elements:** Breaking the standard grid with "floating" modules that suggest depth and fluidity.
- **Glowing Accents:** Thin, high-intensity neon strokes that guide the user's eye toward critical actions.
- **Matte Texture:** Using deep blacks with zero-reflectivity to allow the neon primaries to "pop" with digital intensity.

## Colors

The palette is anchored in **Matte Black (#0A0A0A)** to provide a professional, low-fatigue background for long studio sessions. 

- **Primary (Hot Pink):** Used for critical calls to action, active states, and primary brand markers.
- **Secondary (Electric Blue):** Used for technical data, secondary interactive elements, and audio waveforms.
- **Tertiary (Cyber Purple):** Used for specialized categories, rare sample packs, and depth gradients.
- **Glow Logic:** Accents should utilize these colors with a 15-20px Gaussian blur behind 1px strokes to simulate a neon-lit interface.

## Typography

The typography strategy balances technical precision with editorial impact. **Space Grotesk** is used for all headlines and UI labels to provide a futuristic, geometric feel reminiscent of high-end hardware synthesizers. For long-form descriptions and metadata, **Inter** provides maximum legibility within the dark-mode environment.

Large headlines should use tight tracking and occasional overlapping with background elements to reinforce the "Vibrant-Digital" aesthetic. "Label-caps" are reserved for technical specs (BPM, Key, File Size).

## Layout & Spacing

This design system utilizes a **12-column fixed grid** for desktop, centered within a 1440px container. However, individual modules and "feature cards" are encouraged to break the grid using negative margins to create the "overlapping" aesthetic.

The spacing rhythm follows a strict 8px base unit. 
- **Internal Padding:** Use tight 16px or 24px increments for a "compact workstation" feel.
- **Section Spacing:** Use large 80px+ gaps to allow the vibrant elements room to breathe.
- **Layering:** Overlap elements by exactly 24px or 48px to maintain mathematical harmony while appearing chaotic.

## Elevation & Depth

Depth is conveyed through **Glassmorphism and Tonal Layering** rather than traditional shadows.

1.  **The Floor:** Matte Black (#0A0A0A) solid base.
2.  **The Rack:** Surface levels are created using subtle 1px borders (#FFFFFF at 10% opacity) and background blurs (20px).
3.  **Active Focus:** Elements "glow" into the foreground using a drop shadow with 0px offset, 15px blur, and the primary/secondary color at 40% opacity.
4.  **Intersections:** Where two modules overlap, a "glowing accent line" (1px solid primary color) marks the boundary of the top-most element.

## Shapes

To maintain the professional "Hardware/Workstation" feel, this design system uses **Sharp (0px)** corners for all structural components, including cards, inputs, and containers.

Small decorative elements or tags may use a **Pill-shape** to provide a visual break from the rigid grid, but the primary architecture remains strictly rectangular. This reinforces the "Brutalist" influence and aligns with the aesthetic of digital audio workstations (DAWs).

## Components

- **Buttons:** Primary buttons are solid Matte Black with a 1px Hot Pink border and a perpetual Pink glow. Hover states invert the colors. Text is always uppercase Space Grotesk.
- **Audio Cards:** Large, rectangular blocks with background blurs. The waveform should be rendered in Electric Blue. Metadata is displayed in "mono-data" typography at the bottom.
- **Inputs:** Simple bottom-border only (1px #333). When focused, the border transitions to Electric Blue with a subtle upwards glow.
- **Glowing Accent Lines:** Horizontal or vertical 1px dividers that use a linear gradient (Transparent -> Primary/Secondary -> Transparent).
- **Transport Controls:** Oversized, geometric icons (Play, Pause, Stop) using high-contrast strokes.
- **Sample Tags:** Small, pill-shaped chips with a secondary color outline and no background fill.
- **The "Rack" List:** A list of samples organized like a hardware rack, where each row has a subtle 1px top-border to separate items.