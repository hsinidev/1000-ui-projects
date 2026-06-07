---
name: Zenith Orbital
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#f9f5f5'
  on-tertiary: '#313030'
  tertiary-container: '#dcd9d8'
  on-tertiary-container: '#605e5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
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
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-technical:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.05em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for the elite traveler—individuals who require uncompromising connectivity in the world’s most remote frontiers. The brand personality is **Technical, Authoritative, and Infinite**. It evokes the sensation of looking through a high-precision telescope or operating a spacecraft’s glass cockpit.

The visual style is a fusion of **High-Contrast Minimalism** and **Tech-Forward Glassmorphism**. We lean into a "Dark Mode by Default" philosophy to represent the void of space, using light only where it signifies data or action. The UI should feel like a premium instrument: sharp, precise, and responsive. Visual interest is driven by "scanning" cues—subtle horizontal line animations and glowing pulse points—that suggest active satellite tracking and real-time data flow.

## Colors

The palette is anchored in **Deep Space Black (#050505)**, providing a high-density foundation that allows interactive elements to vibrate with clarity. **Neon Cyan (#00F0FF)** is the primary action color, used exclusively for data-rich visuals, active states, and connectivity indicators. 

**Stark White (#FFFFFF)** is reserved for high-priority typography and critical icons to ensure maximum legibility against the dark void. For depth, we employ a scale of cool, desaturated grays (#1A1A1A, #333333) to define container boundaries and inactive states without breaking the immersion of the dark environment.

## Typography

This design system utilizes **Space Grotesk** for all headlines and technical labels to impart a geometric, futuristic character. Its open apertures and technical structure mirror the precision of satellite hardware.

For sustained reading and complex data sets, **Inter** is utilized for body copy. Its neutral, utilitarian design provides the necessary balance to the more aggressive headlines, ensuring the interface remains readable even in low-light environments. All labels and secondary data points should be set in uppercase Space Grotesk with increased letter spacing to simulate a digital readout or telemetry display.

## Layout & Spacing

The layout follows a **Fixed 12-Column Grid** for desktop and a **Fluid 4-Column Grid** for mobile, emphasizing structural alignment and "hard" edges. The spacing rhythm is strictly based on a **4px baseline**, creating a dense, information-rich environment typical of technical interfaces.

Margins are generous at the edges (32px+) to focus the user's eye on the central "HUD" (Heads-Up Display) area. Content modules should be separated by clear, consistent gutters (24px). Elements should appear modular, as if they could be snapped into place within a physical rack-mount system.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Luminous Accents** rather than traditional shadows. Surfaces are defined by their background tint:
- **Base Level:** Deep Space Black (#050505).
- **Raised Containers:** Semi-transparent Glassmorphism (Background: Black at 60% opacity with a 12px backdrop blur).
- **Borders:** 1px solid lines in #1A1A1A, which "activate" into Neon Cyan (#00F0FF) when focused or active.

Interactive depth is achieved through **Glow Effects**. A soft, Neon Cyan outer glow (4px-8px blur) should be applied to primary buttons and active status indicators to simulate light emitting from the screen.

## Shapes

To maintain a "High-End Technical" aesthetic, the design system utilizes **Sharp (0px)** corners for all primary UI elements. This reinforces a sense of precision and military-grade durability. 

Subtle 45-degree "clipped" corners (dog-ears) may be used on cards or buttons to enhance the futuristic, aerospace-inspired look. Large decorative elements or "scanning" frames should use thin, high-contrast strokes rather than filled shapes to maintain visual lightness.

## Components

### Buttons
Primary buttons feature a Stark White background with Deep Space Black text. On hover, they transition to a Neon Cyan glow with a 1px Cyan border. Ghost buttons use a 1px Cyan border and transparent background, reflecting the "technical readout" style.

### Input Fields
Inputs are underlined or fully boxed with a 1px gray stroke. Upon focus, the stroke pulses into Neon Cyan and a subtle "scanning" line animates across the top of the input area. Labels are always small-caps Space Grotesk.

### Chips & Status Indicators
Status indicators (e.g., "Connected," "Searching") use a pulse animation. "Connected" states utilize a solid Neon Cyan dot with a concentric ring animation to symbolize signal transmission.

### Cards
Cards are treated as "Modules." They use the glassmorphic style with a 1px border. Technical metadata (lat/long, signal strength) should be pinned to the corners of the card in a monospace-style font.

### Progress & Scanning
Progress bars are thin (2px) and feature a "running light" effect where a high-intensity Cyan segment moves across a dim Cyan track. This reinforces the "Scanning" visual cue central to the brand.