---
name: Structural-Sense
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
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#c7c6c6'
  on-tertiary: '#303031'
  tertiary-container: '#999999'
  on-tertiary-container: '#303131'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: IBM Plex Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.02em
  h2:
    fontFamily: IBM Plex Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '700'
    lineHeight: 24px
    letterSpacing: 0.02em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  code-xs:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '400'
    lineHeight: 14px
    letterSpacing: 0.05em
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 12px
  margin: 16px
---

## Brand & Style
The design system is engineered for structural integrity monitoring, where precision is paramount and data density is a requirement rather than a choice. The brand personality is **authoritative, industrial, and hyper-vigilant**. It evokes the feeling of a mission-control center for civil engineering—utilitarian, reliable, and strictly functional.

The aesthetic follows a **Technical-Brutalist** approach. It rejects unnecessary decoration in favor of structural clarity, using heavy contrast to separate critical alerts from baseline telemetry. It mimics the physical instrumentation found in heavy industry, utilizing sharp edges, high-contrast indicators, and a rigorous adherence to a technical grid.

## Colors
The palette is rooted in a **Matte Black** base to reduce visual fatigue in low-light environments and to provide a "void" where data can emerge with high clarity.

- **Primary (Safety Orange):** Reserved strictly for interactive elements, critical data points, and active alerts. It is the color of urgency and human-infrastructure interaction.
- **Neutrals & Greys:** A tiered system of cool greys defines the hierarchy. Darker greys are used for card backgrounds and surfaces, while lighter greys are reserved for borders and secondary metadata.
- **Semantic Accents:** While Safety Orange is the primary accent, a limited "Matrix Green" is used for nominal status and a "Pure Red" for terminal failure states, ensuring immediate cognitive recognition of safety levels.

## Typography
The typography system prioritizes legibility under duress.

- **IBM Plex Sans** is used for structural headings, providing a systematic, engineered feel.
- **Inter** handles standard body text for maximum clarity and accessibility.
- **JetBrains Mono** is the workhorse for all data visualizations, sensor readings, and timestamps. Its monospaced nature ensures that fluctuating numbers do not cause layout shifts and align perfectly in dense tables.

All data labels are set in uppercase to mimic industrial nameplates and emphasize the "official" nature of the telemetry.

## Layout & Spacing
This design system utilizes a **Dense Fluid Grid** optimized for mobile-first structural reporting. The base unit is a strict 4px rhythm, allowing for tight grouping of sensor data.

Layouts should maximize "data-per-inch." Padding is kept to the functional minimum required to maintain touch targets on mobile (44px min). Components are structured in a "Stacked Instrumentation" layout, where cards represent specific sensor clusters or structural segments. On larger displays, these cards tile into a multi-column dashboard without increasing whitespace, maintaining the high-density technical aesthetic.

## Elevation & Depth
Elevation is expressed through **Tonal Layering and Sharp Outlines** rather than shadows. In an industrial context, shadows create visual "mush."

- **Level 0 (Background):** Pure Matte Black (#000000).
- **Level 1 (Card/Surface):** Deep Grey (#0D0D0D) with a 1px solid border (#262626).
- **Level 2 (Interaction/Pop-over):** Mid Grey (#1A1A1A) with a Safety Orange border for focus.

Visual depth is achieved by increasing border contrast rather than adding blur. Inactive states are dimmed via opacity (60%), while active or critical states are brought to the foreground through full-saturation Safety Orange.

## Shapes
The shape language is **Strictly Geometric and Sharp**. 

All components—buttons, cards, and input fields—feature 0px border radii. This reinforces the industrial, non-consumer nature of the application. The only exceptions are status "pips" (indicators), which may be circular to represent physical LED hardware. All other structural elements follow a hard-edged, rectangular philosophy to maximize screen real estate and align with the grid.

## Components
- **Industrial Cards:** Use a 1px border (#262626) with a title bar featuring a monospaced ID tag (e.g., [SNSR-041]). Backgrounds are slightly lighter than the page background to distinguish the container.
- **Buttons:**
  - *Primary:* Solid Safety Orange with Black text. Bold, all-caps.
  - *Secondary:* Ghost style with Grey border and Orange text.
- **Data Visualizations:** Line charts should use 1px stroke widths with no smoothing (linear interpolation). Critical thresholds are marked with dashed Safety Orange lines.
- **Status Indicators:** Small 8px square "LEDs." Green (Steady), Orange (Blinking/Pulsing for active alerts), Red (Rapid Flash for critical).
- **Inputs:** Underlined or fully boxed with 1px borders. Focus states must trigger a 2px Safety Orange border.
- **Mobile Navigation:** A bottom-docked persistent bar with high-contrast icons and monospaced labels, prioritizing the "Alerts" and "Live Feed" views.
- **Urgent Notifications:** Full-width banners in Safety Orange with black monospaced text, occupying the top of the viewport and pushing content down.