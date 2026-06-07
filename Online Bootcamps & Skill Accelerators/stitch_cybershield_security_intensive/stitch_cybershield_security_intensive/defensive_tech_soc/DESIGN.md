---
name: Defensive-Tech SOC
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
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#c8c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b6b5b4'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: spaceGrotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  terminal-data:
    fontFamily: spaceGrotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.02em
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is engineered to evoke the high-stakes environment of an elite Security Operations Center (SOC). The brand personality is clinical, authoritative, and resilient—built for users who operate in the "trenches" of digital defense. The aesthetic shifts away from friendly consumer-grade UI toward a "Defensive Brutalism" style. It prioritizes information density and technical precision over decorative whitespace.

The target audience consists of aspiring and professional security analysts who value efficiency and professional-grade tooling. Every interface element should feel like a piece of mission-critical equipment. The emotional response is one of controlled intensity: the UI does not hold the user's hand; it provides the raw power and data needed to execute complex defensive maneuvers.

## Colors

The palette is anchored in deep blacks and tactical greys to minimize eye strain during long-duration monitoring.

- **Matte Black (#0D0D0D):** The primary canvas color, used for the base background.
- **Laser Red (#FF0000):** Reserved strictly for interactive accents, critical alerts, and successful "breach" notifications. It serves as the "warning light" within the dark environment.
- **Slate Greys (#1A1A1A, #2E2E2E):** Used for structural layering, distinguishing between containers, sidebars, and inactive UI elements.

All secondary signals (Success, Warning, Info) should utilize highly desaturated versions of their standard hues to maintain the "gritty" professional atmosphere, ensuring the Laser Red remains the dominant visual priority.

## Typography

The typography system creates a hierarchy between "Executive Intent" and "Technical Data."

- **Space Grotesk** is utilized for headlines, labels, and data points. Its geometric, technical construction provides the "terminal-style" aesthetic required for headers while maintaining high legibility. All labels should be set in uppercase with increased letter spacing to mimic hardware engraving.
- **Inter** handles all long-form body text and instructional content. Its utilitarian design ensures high readability for complex technical documentation and procedures.

To achieve the "glowing" terminal effect, use a subtle text-shadow on Space Grotesk elements when they appear in Laser Red or High-Contrast White.

## Layout & Spacing

This design system utilizes a **fixed 12-column grid** with a philosophy of high-density information architecture. 

- **Grid:** Use a 16px gutter. Layouts should be tight, maximizing screen real estate for data visualizations and code blocks.
- **Rhythm:** A 4px baseline grid governs all spacing. Vertical stacks should favor 8px (sm) or 16px (md) increments to maintain a compact, "instrument panel" feel.
- **Structure:** Content is organized into modular "blades" or panes. Use visible 1px borders to define these zones rather than relying on whitespace, reinforcing the gritty, structural nature of the SOC interface.

## Elevation & Depth

Depth is communicated through **Tonal Layering** and **Luminescence** rather than traditional shadows.

1.  **Floor (#0D0D0D):** The base application background.
2.  **Surface-Low (#1A1A1A):** Standard containers and inactive cards.
3.  **Surface-High (#2E2E2E):** Hover states, active panels, or floating tooltips.

**The Glow Effect:** Interactive elements do not lift off the page; they "power on." Use a subtle `0px 0px 8px` outer glow in Laser Red for primary active states and a faint Slate Grey glow for secondary interactive elements. This reinforces the hardware-interface metaphor. Avoid soft, ambient shadows; depth should feel flat and stacked, like a series of physical monitors.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. 

All buttons, input fields, containers, and badges must feature 90-degree corners. This uncompromising geometry communicates a sense of military-grade precision and "no-nonsense" professional utility. Rounded corners are perceived as friendly or soft, which contradicts the "Defensive-Tech" aesthetic. 

Structural lines should be thin (1px) and crisp. In specific data-heavy views, use diagonal "clipped corner" accents on large containers to further the high-end technical feel.

## Components

- **Buttons:** Sharp 1px borders. Primary buttons use a solid Matte Black fill with Laser Red text and a red border; on hover, they transition to a solid Laser Red fill with a subtle glow.
- **Input Fields:** Styled as "Command Prompts." Use a dark #1A1A1A background with a 1px #2E2E2E border that turns Laser Red when focused. Include a static `>` or `$` prefix for text inputs to reinforce the terminal aesthetic.
- **Cards/Panels:** Backgrounds use #1A1A1A. Headers for cards should be separated by a 1px line and feature a label in Space Grotesk caps.
- **Chips/Status Badges:** Small, sharp rectangles. Use Laser Red for "Critical" and desaturated Slates for "System."
- **Data Visualizations:** Line charts and graphs must use thin strokes with "Scanline" pattern overlays. Data points should have a glowing focal point.
- **Lists:** High-density, monospaced data rows with alternating #1A1A1A and #0D0D0D backgrounds.
- **Additional Suggestion:** Include a "Global System Status" ticker at the top or bottom of the UI, displaying scrolling hex codes or system logs to ground the experience in a live SOC environment.