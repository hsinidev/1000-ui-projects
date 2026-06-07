---
name: Nomad tactical
colors:
  surface: '#121416'
  surface-dim: '#121416'
  surface-bright: '#37393b'
  surface-container-lowest: '#0c0e10'
  surface-container-low: '#1a1c1e'
  surface-container: '#1e2022'
  surface-container-high: '#282a2c'
  surface-container-highest: '#333537'
  on-surface: '#e2e2e5'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#e2e2e5'
  inverse-on-surface: '#2f3133'
  outline: '#8f9097'
  outline-variant: '#45474c'
  surface-tint: '#bfc6db'
  primary: '#bfc6db'
  on-primary: '#293041'
  primary-container: '#0a1221'
  on-primary-container: '#767d90'
  inverse-primary: '#575e70'
  secondary: '#ffb693'
  on-secondary: '#561f00'
  secondary-container: '#fe6b00'
  on-secondary-container: '#572000'
  tertiary: '#bcc7dd'
  on-tertiary: '#263142'
  tertiary-container: '#071222'
  on-tertiary-container: '#737e92'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe2f8'
  primary-fixed-dim: '#bfc6db'
  on-primary-fixed: '#141c2b'
  on-primary-fixed-variant: '#3f4758'
  secondary-fixed: '#ffdbcc'
  secondary-fixed-dim: '#ffb693'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#7a3000'
  tertiary-fixed: '#d8e3fa'
  tertiary-fixed-dim: '#bcc7dd'
  on-tertiary-fixed: '#111c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#121416'
  on-background: '#e2e2e5'
  surface-variant: '#333537'
typography:
  display-alert:
    fontFamily: Anton
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Anton
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.4'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.2'
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '800'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  container-padding: 24px
---

## Brand & Style
The design system is engineered for the high-stakes environment of executive protection and armored logistics. The brand personality is **authoritative, vigilant, and indestructible**. It targets high-net-worth individuals and security operatives who require instant cognitive processing of vehicle telemetry, threat assessments, and environmental data.

The visual style is a fusion of **Tactile Brutalism** and **High-Contrast Command-Center** aesthetics. It rejects soft aesthetics in favor of rigid structures, heavy-duty containers, and technical precision. The emotional response is one of absolute security and operational control; every pixel serves a functional purpose, mirroring the physical reinforcement of the armored fleet.

## Colors
The palette is dominated by **Midnight Blue**, utilized for deep-space backgrounds and primary structural elements to establish an authoritative, night-vision-compatible environment. 

**Safety Orange** is reserved strictly for interactive calls to action, high-priority alerts, and SOS indicators, ensuring immediate visual acquisition. **Graphite** serves as the metallic, rugged mid-tone for borders, dividers, and secondary surfaces. Status indicators utilize high-intensity "glow" colors—saturated greens and reds—to communicate vehicle health and threat levels against the dark canvas.

## Typography
The typography strategy prioritizes rapid legibility under stress. This design system utilizes **Anton** for primary headers and critical alerts, providing a high-impact, condensed verticality that signals urgency. 

**Inter** provides a neutral, systematic foundation for body copy and general interface text, ensuring clarity in descriptive content. For telemetry and technical readouts, **JetBrains Mono** is used to maintain character alignment and a "machine-readable" aesthetic. Heavy use of uppercase and tracking is applied to labels to distinguish them from dynamic data.

## Layout & Spacing
The layout follows a **Fixed-Grid System** built on a 4px baseline to maintain technical alignment. Content is housed in modular "Tactical Blocks" that occupy a 12-column grid on desktop and a 4-column grid on mobile. 

Margins and gutters are kept tight (16px) to maximize the information density required for a command-center interface. Strategic use of "Dead Space" (pure black or midnight blue voids) is used to separate high-priority weapon or navigation modules from secondary environmental controls. Components should reflow vertically on mobile, with the most critical "Panic/SOS" functions pinned to the bottom of the viewport.

## Elevation & Depth
In this design system, depth is not achieved through shadows, but through **Tonal Stacking** and **Translucency**. 

1.  **Base Layer:** Midnight Blue (Solid).
2.  **Module Layer:** Graphite or semi-transparent Midnight Blue (80% opacity) with a 1px solid Graphite border.
3.  **Active Overlay:** 10% Safety Orange tint over the module with a glowing inner stroke.

Visual hierarchy is reinforced by "Heavy-Duty" containers that use chamfered corners or visible "bolt" accents in the borders. Status indicators should appear to "emit light" via subtle outer glows (dropshadows with 0 spread and high blur) in the status color (e.g., Green or Orange).

## Shapes
The shape language of this design system is **unapologetically sharp**. A roundedness of 0 is applied to all primary containers, buttons, and input fields to reinforce the "rugged/armored" aesthetic. 

Small accents, such as status pips, may use a 45-degree chamfer rather than a radius. Interactive elements like buttons should feature a "clipped corner" effect on the top-right to suggest a custom-machined interface.

## Components
- **Buttons:** Sharp-edged, solid Safety Orange for primary actions. Text is always uppercase bold JetBrains Mono. Secondary buttons are outlined in Graphite with a "Tactile Hover" effect (filling with 10% white).
- **Status Indicators:** Small, circular "LED" pips with a 4px blur radius to simulate a hardware glow.
- **Data Cards:** Containers with a 1px Graphite border, a subtle gradient from top to bottom (Midnight Blue to Black), and a header bar with a contrasting background color.
- **Input Fields:** Recessed appearance with a 1px Graphite bottom-border and monospaced placeholder text. Active state triggers a Safety Orange 1px border.
- **Heavy-Duty Progress Bars:** Thick, segmented bars (stepped) rather than smooth fills, suggesting mechanical increments.
- **HUD Overlays:** Semi-transparent Graphite panels (60% opacity) with "corner-only" borders to frame critical live video or map data.