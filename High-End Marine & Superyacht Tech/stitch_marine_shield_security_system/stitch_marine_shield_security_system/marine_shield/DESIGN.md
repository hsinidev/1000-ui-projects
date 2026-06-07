---
name: Marine-Shield
colors:
  surface: '#0d141a'
  surface-dim: '#0d141a'
  surface-bright: '#333a41'
  surface-container-lowest: '#080f15'
  surface-container-low: '#151c23'
  surface-container: '#192027'
  surface-container-high: '#242b31'
  surface-container-highest: '#2f353c'
  on-surface: '#dce3ec'
  on-surface-variant: '#e4bfb1'
  inverse-surface: '#dce3ec'
  inverse-on-surface: '#2a3138'
  outline: '#ab8a7d'
  outline-variant: '#5b4137'
  surface-tint: '#ffb599'
  primary: '#ffb599'
  on-primary: '#5a1c00'
  primary-container: '#ff5f00'
  on-primary-container: '#531a00'
  inverse-primary: '#a63b00'
  secondary: '#c6c6c9'
  on-secondary: '#2f3133'
  secondary-container: '#454749'
  on-secondary-container: '#b4b5b7'
  tertiary: '#c0c7cf'
  on-tertiary: '#2a3137'
  tertiary-container: '#8e959c'
  on-tertiary-container: '#272e34'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbce'
  primary-fixed-dim: '#ffb599'
  on-primary-fixed: '#370e00'
  on-primary-fixed-variant: '#7f2b00'
  secondary-fixed: '#e2e2e5'
  secondary-fixed-dim: '#c6c6c9'
  on-secondary-fixed: '#1a1c1e'
  on-secondary-fixed-variant: '#454749'
  tertiary-fixed: '#dce3eb'
  tertiary-fixed-dim: '#c0c7cf'
  on-tertiary-fixed: '#151c22'
  on-tertiary-fixed-variant: '#41484e'
  background: '#0d141a'
  on-background: '#dce3ec'
  surface-variant: '#2f353c'
typography:
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  status-num:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1'
    letterSpacing: -0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  panel-gap: 8px
  container-padding: 20px
---

## Brand & Style

This design system is engineered for the high-stakes environment of maritime security. The brand personality is authoritative, uncompromising, and hyper-functional. It evokes a sense of "Tactical-Elite" readiness, mimicking the sophisticated interfaces found in naval command centers and aerospace cockpits. The target audience—security officers and yacht captains—requires immediate data legibility under intense operational stress.

The visual style is a hybrid of **Industrial Minimalism** and **Tactical Glassmorphism**. It utilizes heavy, structural elements balanced by semi-transparent data overlays. Every pixel serves a functional purpose; there is no decorative flourish that does not contribute to situational awareness. High-contrast transitions and subtle internal glows create a "HUD" (Heads-Up Display) effect, ensuring the interface feels like an integrated piece of hardware rather than a standard software application.

## Colors

The palette is rooted in a deep, nocturnal spectrum to preserve night vision on the bridge while highlighting critical data.

- **Slate Grey (Primary Backgrounds):** The foundation of the UI, providing a low-light base that reduces eye strain.
- **Graphite (Secondary Surfaces):** Used for elevated panels, card containers, and inset areas to create structural depth.
- **Safety Orange (Primary Action/Alert):** Reserved strictly for interactive elements, active states, and high-priority warnings. This color must maintain maximum saturation to pierce through the dark UI.
- **Tactical Overlays:** A range of semi-transparent greys (10% to 40% opacity) used for glass panels and HUD-style readouts.
- **Status Indicators:** 
    - *Secure:* A muted, technical Cyan-Blue.
    - *Caution:* Deep Amber.
    - *Breach:* Pure Safety Orange.

## Typography

This design system utilizes a dual-font strategy to balance technical precision with rapid legibility.

**JetBrains Mono** is the primary technical font. Its monospaced nature ensures that coordinates, timestamps, and sensor data remain perfectly aligned in shifting data grids. It is used for all headlines, status labels, and numerical readouts.

**Hanken Grotesk** serves as the body font. Its sharp, contemporary sans-serif letterforms provide excellent readability for logs, incident reports, and system descriptions.

All labels should default to uppercase with increased letter spacing to mimic military-grade hardware labeling. In high-stress scenarios, typography size should be prioritized over density; never drop below 14px for critical telemetry.

## Layout & Spacing

The layout philosophy follows a **Fixed-Modular Grid**. Content is organized into rigid, interlocking "modules" that suggest a physical control console. 

- **Grid:** A 12-column grid system is used for desktop, collapsing to 1 column for mobile. 
- **Rhythm:** A strict 4px base unit governs all spacing. Vertical rhythm is tight to maximize information density.
- **Adaptation:** On mobile devices, the dashboard pivots to a "Single-Metric View," focusing on the highest-priority alert. On large bridge displays, the layout expands to show multi-angle perimeter camera feeds and radar overlays simultaneously.
- **Safe Areas:** Generous 24px outer margins ensure the UI is not clipped by physical bezel housings or marine-grade enclosures.

## Elevation & Depth

Hierarchy is established through **Tonal Stacking** and **Tactical Glassmorphism** rather than traditional shadows.

1.  **Floor:** Slate Grey (Base).
2.  **Raised Panels:** Graphite surfaces with 1px interior borders (0.5px stroke width) in a lighter grey to simulate chamfered edges.
3.  **Active Overlays:** Semi-transparent Graphite (80% opacity) with a `20px` backdrop blur to separate transient data from the background map or camera feed.
4.  **Interaction Depth:** Buttons and toggles use "inset" styling (negative elevation) when active, suggesting a physical mechanical click.
5.  **Glow:** Safety Orange elements (text and icons) feature a subtle `0 0 8px` outer glow in high-alert states to mimic the luminance of a radar screen.

## Shapes

The shape language is strictly **Geometric and Sharp**. 

- **Corners:** 0px radius across all components. This reinforces the industrial, rugged nature of the system. 
- **Accents:** 45-degree clipped corners (dog-ears) are used for high-level navigation tabs and primary alert headers to provide a distinct "military-spec" silhouette.
- **Dividers:** Horizontal and vertical rules are 1px thick, utilizing a dashed pattern for secondary containers and solid lines for primary structural boundaries.

## Components

- **Buttons:** Primary buttons are solid Safety Orange with black text. Secondary buttons are outlined with 1px Slate Grey. All buttons feature a "hover" state where the corners appear to be braced by L-shaped brackets.
- **Alert Headers:** These span the full width of the interface. When active, they use a pulsing Safety Orange background with black, bold "JetBrains Mono" text.
- **Inputs:** Field backgrounds are Graphite with a bottom-only 2px border. Focus state changes the border to Safety Orange and adds a faint orange glow to the text.
- **Status Chips:** Small, rectangular indicators. "Active" chips should feature a small blinking "recording" dot icon.
- **Data Cards:** Containers for sensor data. They include a small "ID tag" in the top left corner (e.g., [SN-042]) to reinforce the industrial aesthetic.
- **Tactical Map Overlays:** Semi-transparent circles and vectors with coordinate labels that follow the cursor or target, rendered in the status-indicator colors.
- **Toggle Switches:** Rectangular sliders that "snap" into place with high-contrast color shifts rather than smooth animations.