---
name: Nomad-Secure Command
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1c'
  surface-container: '#1f1f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353536'
  on-surface: '#e4e2e3'
  on-surface-variant: '#c5c6cc'
  inverse-surface: '#e4e2e3'
  inverse-on-surface: '#303031'
  outline: '#8f9096'
  outline-variant: '#45474c'
  surface-tint: '#bfc7d8'
  primary: '#bfc7d8'
  on-primary: '#29313e'
  primary-container: '#0a121e'
  on-primary-container: '#767d8d'
  inverse-primary: '#575f6d'
  secondary: '#c3c6d1'
  on-secondary: '#2c3039'
  secondary-container: '#454952'
  on-secondary-container: '#b5b8c2'
  tertiary: '#ffb693'
  on-tertiary: '#561f00'
  tertiary-container: '#250900'
  on-tertiary-container: '#d25700'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe3f4'
  primary-fixed-dim: '#bfc7d8'
  on-primary-fixed: '#141c28'
  on-primary-fixed-variant: '#3f4755'
  secondary-fixed: '#dfe2ed'
  secondary-fixed-dim: '#c3c6d1'
  on-secondary-fixed: '#181c23'
  on-secondary-fixed-variant: '#43474f'
  tertiary-fixed: '#ffdbcc'
  tertiary-fixed-dim: '#ffb693'
  on-tertiary-fixed: '#351000'
  on-tertiary-fixed-variant: '#7a3000'
  background: '#131314'
  on-background: '#e4e2e3'
  surface-variant: '#353536'
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
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  telemetry-num:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  component-padding-x: 12px
  component-padding-y: 8px
---

## Brand & Style

This design system is engineered for high-stakes executive transport and armored logistics coordination. The visual language balances extreme robustness with sophisticated technical precision, evoking the feeling of a specialized tactical operations center (TOC). It is designed for operators who require immediate data density, absolute clarity, and a sense of "armored" reliability.

The aesthetic combines **Modern Tactical** with **Subtle Glassmorphism**. Elements appear as though they are projected onto reinforced glass displays inside an armored vehicle. The interface utilizes dark-mode primary surfaces to reduce light pollution in low-light environments, accented by neon-glow indicators that signify live data streams and system readiness.

## Colors

The palette is anchored in **Midnight Blue** (#0A121E), providing a deep, high-contrast base that minimizes eye strain. **Graphite** (#282C34) serves as the primary surface color, creating a layered, structural feel.

**Safety Orange** (#FF6B00) is reserved strictly for critical actions, alerts, and primary command buttons to ensure instant visibility against the dark background. A secondary **Cyan Accent** (#00F0FF) is utilized for "active" state glows and telemetry data, signaling that a system is online and functioning correctly. Backgrounds should utilize subtle gradients of Midnight Blue to Graphite to imply depth and hardware-integration.

## Typography

The typography system uses a hybrid approach to maximize technical legibility. **JetBrains Mono** is used for all headers, labels, and data points to emphasize the "command center" feel and ensure numerical clarity. **Inter** is used for body text and descriptive content to provide high-speed readability and a modern, professional polish.

Headers should be bold and high-visibility. Small labels always use uppercase with increased tracking (letter-spacing) to mimic industrial hardware labeling. Telemetry data (coordinates, timestamps, speeds) must always use monospaced fonts to prevent visual shifting during real-time updates.

## Layout & Spacing

This design system uses a **Tight Tactical Grid** based on a 4px base unit. In high-stress environments, information density is prioritized over whitespace. 

- **Grid:** A 12-column fluid grid for desktop; 4-column for mobile.
- **Density:** Elements are packed closely to allow more data on-screen, but separated by high-contrast Graphite borders to prevent "visual bleed."
- **Margins:** Tight margins (16px/32px) ensure the interface feels expansive and "edge-to-edge," like a built-in vehicle display.
- **Adaptive Rules:** On mobile, secondary telemetry sidebars collapse into a bottom-anchored "Command Bar." Desktop views prioritize a "Main Map/Feed" center with modular widgets flanking the sides.

## Elevation & Depth

Hierarchy is established through **Tonal Stacking** and **Glassmorphism** rather than traditional shadows. 

1. **Base Level:** Midnight Blue (The "Deep Space").
2. **Container Level:** Graphite surfaces with 85% opacity and a 16px backdrop blur, creating a glass-on-hardware effect.
3. **Active Level:** Elements in focus use a 1px solid Graphite border and a subtle internal "Safety Orange" or "Cyan" glow (2-4px spread) to indicate selection.
4. **Overlay Level:** Critical alerts use full-opacity Safety Orange backgrounds with black text to "jump" to the foreground of the user's attention.

Shadows, if used, should be narrow, dark, and sharp (0% blur) to maintain the "hard-surface" tactical feel.

## Shapes

The shape language is **Sharp and Industrial**. To convey a sense of armored strength and precision, the default roundedness is set to 0px. 

All buttons, input fields, and containers utilize hard 90-degree corners. Where a visual "break" is needed, use 45-degree chamfered corners (clipped corners) on the top-right or bottom-left of containers to reinforce the "military-spec" hardware aesthetic. Decorative elements should follow a hexagonal or octagonal geometry.

## Components

- **Command Buttons:** Rectangular with no radius. Primary actions are Safety Orange with black text. Secondary actions are Graphite with a 1px Cyan border. Active states feature a subtle outer glow.
- **Status Indicators:** Small circular or diamond-shaped icons with a "breathing" glow effect (Cyan for Active/Secure, Orange for Alert/Insecure).
- **Data Cards:** Semi-transparent Graphite containers with a subtle 1px top-border highlight. Titles are always in JetBrains Mono (Label-Caps).
- **Inputs:** Darker than the surface level, using a 1px bottom border that glows Cyan when focused. Text entry uses JetBrains Mono.
- **HUD Overlays:** Information displayed directly over maps or video feeds should have a 40% black tint background and sharp Cyan text for maximum contrast.
- **Tactical Chips:** Small, high-contrast tags used for status (e.g., "ARMORED," "EN ROUTE," "LOCKED"). These use the Label-Caps typography.
- **Telemetry Feeds:** Scrolling vertical lists of monospaced data with no dividers, using only indentation and color-coding for hierarchy.