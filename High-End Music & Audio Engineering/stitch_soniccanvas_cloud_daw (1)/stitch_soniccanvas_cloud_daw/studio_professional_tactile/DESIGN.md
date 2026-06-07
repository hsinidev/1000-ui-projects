---
name: Studio Professional Tactile
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
  on-surface-variant: '#bacbbc'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
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
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#fafeff'
  on-tertiary: '#303030'
  tertiary-container: '#e3e0e0'
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
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  mono-label:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  technical-readout:
    fontFamily: Space Grotesk
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 12px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 1px
  track-height: 48px
---

## Brand & Style
The design system is engineered for elite audio engineering and precision music production. It evokes a sense of focused isolation—the "studio late-night" vibe—where the tool disappears into the workflow. The brand personality is analytical, high-performance, and reliable.

The UI style merges **Minimalism** with **Tactile Skeuomorphism**. While the overall environment is flat and unobtrusive to reduce cognitive load, critical interactive elements like faders, knobs, and switches utilize subtle gradients and inner shadows to mimic physical outboard gear. This provides the user with an immediate "affordance" of touch, essential for a creative environment that translates physical gestures into digital sound.

## Colors
The palette is centered on a "void" aesthetic to make audio data the focal point. 
- **Matte Black (#0A0A0A):** The foundation of the workspace, used for the primary application background and timeline "gutters."
- **Charcoal (#1A1A1A):** Used for functional surfaces, channel strips, and inspector panels to create subtle separation from the background.
- **Neon Mint (#3DFFA3):** The high-visibility accent. Reserved strictly for active states, playheads, current selections, and peak audio indicators. 
- **Functional Grays:** A spectrum of grays between #262626 and #A1A1A1 is used for iconography and inactive text to maintain hierarchy without visual clutter.

## Typography
Typography is split into two functional roles: **System Navigation** and **Technical Performance.**

1.  **Inter** is utilized for the primary interface, settings, and navigation. It is chosen for its exceptional legibility at small sizes, ensuring that complex menus remain scannable.
2.  **Space Grotesk** is used for all technical readouts, timecodes, and parameter values. Its geometric, monospaced-adjacent qualities provide the "scientific instrument" feel necessary for a high-end DAW.

All text utilizes high-contrast ratios against the charcoal surfaces, with technical readouts often appearing in a dimmed gray (#808080) until hovered or modified, at which point they transition to the Neon Mint accent.

## Layout & Spacing
The layout follows a **Strict Modular Grid** based on an 8px unit. The DAW interface is divided into functional zones: the Header (transport controls), the Sidebar (browser/inspector), the Main Stage (timeline/sequencer), and the Footer (mixer/properties).

- **Fluidity:** The Timeline and Mixer are fluid, expanding to fill available screen real estate while maintaining fixed-width Sidebar panels.
- **Micro-Spacing:** A 1px "technical gutter" is used between adjacent channel strips to simulate the assembly of physical hardware components. 
- **Density:** High information density is prioritized. Vertical spacing is compressed to maximize the number of visible tracks on a single screen.

## Elevation & Depth
This design system utilizes **Tonal Layering** combined with **Inner Shadows** to create a functional sense of depth.

- **Recessed Areas:** Audio tracks and MIDI clips are placed in "wells" created by subtle inner shadows on the Matte Black background. This makes the content feel nested within the machine.
- **Elevated Interactive Elements:** Knobs and Fader caps utilize a subtle top-down lighting gradient. A 1px highlight on the top edge and a soft 4px drop shadow give these elements a tactile, "clickable" presence.
- **Glass Overlays:** Floating plugin windows and context menus use a 20px backdrop blur with a 60% opacity Charcoal fill to maintain focus on the modal without losing the context of the arrangement underneath.

## Shapes
The shape language is primarily **Industrial and Rectilinear.** 

A "Soft" (4px) corner radius is applied to buttons, input fields, and track headers to prevent the UI from feeling sharp or aggressive, while maintaining a professional, boxy silhouette. 

- **Fader Caps:** Utilize a 2px radius for a more metallic, machined appearance.
- **Knobs:** Perfectly circular with a 2px "indicator dot" in Neon Mint.
- **Clip Regions:** Use a 4px radius on the top corners and 0px on the bottom to visually "anchor" them to the track lane.

## Components
### Buttons & Controls
- **Transport Controls:** Large, flat icons. The 'Record' button uses a pulsing dim red, while 'Play' and 'Active' states use Neon Mint glows.
- **Faders:** The track is a recessed line (#0A0A0A); the handle is a charcoal block with a centered Neon Mint horizontal line.

### Level Meters (VU)
- **Visuals:** Segmented bars. Low levels are dark gray, active levels are Neon Mint.
- **Peak Indicators:** A single-pixel persistent line at the highest reached decibel, turning pure white (#FFFFFF) during clipping.

### Knobs
- **Interaction:** Vertical drag to increase value.
- **Visuals:** A 360-degree track that fills with Neon Mint as the value increases, utilizing a "glow" effect for the filled portion to simulate LED-ringed hardware.

### Inputs & Labels
- **Parameter Inputs:** Minimalist boxes with no borders, only a bottom stroke that turns Neon Mint on focus.
- **Chips/Tags:** Used for plugin inserts—low profile, dark charcoal background, with a 1px Neon Mint left-border if the plugin is active.

### Tracks
- **Selection:** Selected tracks are indicated by a Neon Mint vertical bar on the extreme left edge of the track header.