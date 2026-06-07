---
name: Audiophile Precision
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c7c6ca'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#919094'
  outline-variant: '#46464a'
  surface-tint: '#c8c6c7'
  primary: '#c8c6c7'
  on-primary: '#313031'
  primary-container: '#0f0f10'
  on-primary-container: '#7d7b7c'
  inverse-primary: '#5f5e5f'
  secondary: '#c6c6cb'
  on-secondary: '#2f3034'
  secondary-container: '#48494d'
  on-secondary-container: '#b8b8bd'
  tertiary: '#c6c6cb'
  on-tertiary: '#2e3034'
  tertiary-container: '#0d0f13'
  on-tertiary-container: '#7a7b80'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e3'
  primary-fixed-dim: '#c8c6c7'
  on-primary-fixed: '#1c1b1c'
  on-primary-fixed-variant: '#474647'
  secondary-fixed: '#e3e2e7'
  secondary-fixed-dim: '#c6c6cb'
  on-secondary-fixed: '#1a1b1f'
  on-secondary-fixed-variant: '#46474b'
  tertiary-fixed: '#e2e2e7'
  tertiary-fixed-dim: '#c6c6cb'
  on-tertiary-fixed: '#1a1c1f'
  on-tertiary-fixed-variant: '#45474b'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
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
  margin-edge: 40px
  panel-padding: 32px
  control-gap: 16px
---

## Brand & Style

The brand identity of this design system is rooted in the high-fidelity world of professional audio engineering and luxury consumer electronics. It targets a sophisticated audience that values precision, durability, and the tactile satisfaction of premium hardware. 

The UI style is a hybrid of **Modern Minimalism** and **Tactile Skeuomorphism**. It leverages the clarity of a minimalist layout—prioritizing function and whitespace—while imbuing interactive elements with the physical characteristics of "milled" metal and "weighted" analog controls. The atmosphere is quiet and authoritative, designed to feel like a high-performance instrument rather than a mere software application. Every interaction should evoke the sensation of operating a finely tuned piece of rack-mounted hardware.

## Colors

The palette is strictly curated to reflect industrial materials. The foundation is a deep matte black (`#0F0F10`), providing a non-reflective surface that minimizes visual noise. Secondary tones are derived from brushed steel and aluminum, using a range of cool grays to define edges and surfaces. 

Highlights are rendered in silver and pure white to ensure maximum legibility against the dark background. A singular "Signal Blue" accent is used sparingly for active states or critical playback information, mimicking the precision LEDs found on high-end amplifiers. Gradients should be linear and subtle, simulating the way light hits a machined metal surface rather than creating a "glossy" appearance.

## Typography

The typography system balances technical rigor with modern elegance. **Space Grotesk** is used for primary headlines and branding elements; its geometric construction mirrors the "high-performance" feel of modern audio equipment. 

For all functional text, body copy, and interface labels, **Inter** is utilized for its exceptional legibility and neutral, systematic character. To maintain the professional aesthetic, labels for controls (like "GAIN" or "DB") should be set in small caps with increased letter spacing, mimicking the screen-printed text on a physical console. Numerical data, such as decibel levels or sample rates, should be treated with a semi-bold weight to ensure they are readable at a glance in low-light environments.

## Layout & Spacing

This design system employs a **Fixed Grid** model to simulate the modular nature of pro-audio hardware racks. The layout is organized into distinct "panels" or "modules" that house specific control groups (e.g., EQ, Multi-room zones, Playback). 

The rhythm is governed by an 8px base unit. Generous margins (`40px`) surround the main interface to give the UI a premium, uncrowded feel. Within control modules, a tighter `16px` gap is used between related knobs and faders to imply a physical connection. Panels should be grouped logically, with consistent vertical gutters of `24px` to maintain a clear visual hierarchy across different screen sizes.

## Elevation & Depth

Depth is the primary tool for conveying the "Audiophile-Sleek" aesthetic. It is achieved through three specific techniques:

1.  **Recessed Surfaces:** Control areas and input fields are "carved" into the matte black background using subtle inner shadows and a 1px darker top-border. This creates a "well" that components sit within.
2.  **Raised Components:** Knobs, faders, and buttons use a "brushed metal" gradient. They feature a thin, 1px light highlight on the top-left edge and a soft, directional drop shadow on the bottom-right to simulate physical protrusion from the surface.
3.  **Light Scopes:** Interactive states (like a turned knob) should feature a subtle "glow" or light-bleed effect around the base, as if backlit by a high-quality LED.

Avoid standard "box-shadows" that float elements; instead, focus on making elements feel like they are mechanically attached to the chassis.

## Shapes

The shape language is disciplined and architectural. A **Soft (0.25rem)** roundedness is applied to major containers and panels, mimicking the precision-milled radius of an aluminum faceplate. 

Interactive elements like buttons and fader-caps use this same minimal radius to maintain a professional, industrial look. Circular shapes are reserved exclusively for rotational controls (knobs) and status indicators, providing a clear visual distinction between "pressable" and "turnable" interface elements. Sharp corners are avoided to prevent the UI from feeling "digital" or aggressive, but overly rounded "pill" shapes are also avoided to maintain the technical tone.

## Components

**Buttons & Switches**
Buttons should appear as milled aluminum blocks. In their default state, they have a subtle vertical gradient. When "pressed," the gradient reverses and a 1px inner shadow is applied to simulate physical travel.

**Knobs & Faders**
Knobs are the centerpiece of the system. They feature a circular brushed-metal texture (radial gradient) with a physical "indicator notch" highlighted in silver. Faders move within a recessed track; the track itself should have a dark, grooved inner-shadow.

**VU Meters & Visualizers**
Use high-contrast bar segments. Inactive segments are deep gray; active segments transition from cool white to silver. For "clipping" or peak indicators, use a sharp, saturated red.

**Lists & Zone Selection**
Zone cards should be separated by thin, low-opacity "etched" lines rather than heavy borders. Each list item should feel like a discrete module in a rack.

**Checkboxes & Radios**
These are replaced with "Toggle Switches" or "LED indicators." An active state is indicated by a "lit" glow effect rather than a simple checkmark, maintaining the hardware metaphor.