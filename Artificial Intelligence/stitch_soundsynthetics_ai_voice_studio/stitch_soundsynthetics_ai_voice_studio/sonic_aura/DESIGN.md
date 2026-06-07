---
name: Sonic Aura
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d4c5ab'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9c8f78'
  outline-variant: '#504532'
  surface-tint: '#fbbc00'
  primary: '#ffe2ab'
  on-primary: '#402d00'
  primary-container: '#ffbf00'
  on-primary-container: '#6d5000'
  inverse-primary: '#795900'
  secondary: '#fff9ef'
  on-secondary: '#3a3000'
  secondary-container: '#ffdb3c'
  on-secondary-container: '#725f00'
  tertiary: '#e6e5e5'
  on-tertiary: '#303031'
  tertiary-container: '#cac9c9'
  on-tertiary-container: '#545454'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdfa0'
  primary-fixed-dim: '#fbbc00'
  on-primary-fixed: '#261a00'
  on-primary-fixed-variant: '#5c4300'
  secondary-fixed: '#ffe16d'
  secondary-fixed-dim: '#e9c400'
  on-secondary-fixed: '#221b00'
  on-secondary-fixed-variant: '#544600'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
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
    lineHeight: '1.5'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-technical:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style

The design system is engineered to evoke the precision of a high-end recording studio blended with the ethereal nature of synthesized sound. The brand personality is professional, authoritative, and sophisticated, targeting audio engineers and creative directors who require clinical accuracy within an immersive environment.

The style is **Auditory-Atmospheric**, a bespoke hybrid of **Minimalism** and **Glassmorphism**. It utilizes deep tonal layering and subtle radial gradients to simulate the movement of sound waves and the glow of vacuum tubes. The UI should feel less like a website and more like a premium hardware instrument—tactile, responsive, and deeply focused.

## Colors

The palette is anchored in a deep **Charcoal (#121212)** base to provide a void-like canvas that minimizes eye strain during long production sessions. **Smoke (#757575)** serves as the secondary structural color, used for borders and inactive states to maintain low visual noise.

**Gold (#FFBF00)** and **Warm Amber (#FFD700)** act as the "active" filaments of the interface, reserved for playback indicators, primary actions, and critical data points. These highlights should be applied with restraint, often accompanied by a soft outer glow (bloom) to suggest light-emitting hardware components.

## Typography

This design system utilizes **Space Grotesk** for headlines and technical data to reinforce a futuristic, engineering-driven aesthetic. Its geometric construction mirrors the mathematical nature of frequency and synthesis. 

**Inter** is employed for all body copy and functional UI elements to ensure maximum legibility against dark backgrounds. For metadata, timecodes, and hardware-style labels, use the `label-caps` or `mono-technical` tokens. Line heights are generous to prevent text "vibration" in high-contrast dark mode scenarios.

## Layout & Spacing

The layout follows a **Fixed-Grid** model for the central workspace to ensure audio tools remain in predictable locations, while peripheral panels can adapt to the screen width. A 12-column grid is used for the primary dashboard, with a 24px gutter to provide breathing room between complex visualizers.

Spacing follows a strict 8px rhythmic scale. Vertical margins between sections should be expansive (40px+) to maintain an "Atmospheric" feel, preventing the tool-heavy interface from feeling cluttered or overwhelming.

## Elevation & Depth

Depth is established through **Tonal Layering** and **Glassmorphism** rather than traditional drop shadows. 
1.  **Level 0 (Base):** The Charcoal (#121212) canvas.
2.  **Level 1 (Panels):** Surfaces slightly lighter than the base with a subtle 1px Smoke (#757575) stroke at 20% opacity.
3.  **Level 2 (Overlays):** Translucent panels using a 12px backdrop blur and a faint Amber inner-glow to suggest active focus.

Use radial gradients peaking in the corners of panels to mimic the way light falls across a physical mixing console.

## Shapes

The design system adopts a **Soft (1)** roundedness profile (0.25rem). This maintains a professional, "precision instrument" feel, avoiding the playfulness of larger border radii. 

Interactive elements like play buttons or toggles use the `rounded-lg` (0.5rem) token to subtly distinguish them from structural containers. Audio waveform containers and data visualizations should remain sharp or use minimal rounding to emphasize technical accuracy.

## Components

### Buttons
- **Primary:** Solid Gold (#FFBF00) with black text. On hover, apply a 10px amber outer glow (bloom).
- **Secondary:** Transparent with a 1px Smoke border. Text turns Gold on hover.
- **Ghost:** Text only, used for utility actions (e.g., "Reset").

### Input Fields & Controls
- **Text Inputs:** Deep Charcoal fill with a bottom-only Smoke border. Focus state turns the border Gold.
- **Faders/Sliders:** Horizontal tracks in Smoke, with a Gold circular handle. The "active" portion of the track should glow.
- **Knobs:** Circular indicators with a single Gold needle point, mimicking analog studio gear.

### Cards & Modules
- Use the "Level 1" elevation style. Headers within cards should use `label-caps` for a technical, organized appearance.

### Specialized Audio Components
- **Waveform Display:** Use a semi-transparent Gold fill for the wave, with a bright Amber vertical line for the playhead.
- **VU Meters:** Segmented bars transitioning from Smoke (low) to Gold (peak).