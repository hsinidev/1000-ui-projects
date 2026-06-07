---
name: FleetMaster Industrial Technical
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
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#9a9999'
  on-tertiary-container: '#313131'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  ui-bold:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0em
  ui-reg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0em
  data-lg:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mid:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.02em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 12px
  margin-mobile: 16px
---

## Brand & Style
The brand personality is authoritative, resilient, and unapologetically functional. It targets fleet managers and commercial drivers who operate in high-stakes environments where precision is not a luxury, but a safety requirement. 

This design system utilizes a **Modern Brutalist** style filtered through an industrial lens. It avoids decorative "fluff" in favor of structural integrity. The UI should evoke the feeling of a high-end diagnostic tool or a cockpit interface: rugged enough for the road, yet precise enough for complex logistics data. Visual hierarchy is established through rigid grid structures and high-contrast signaling rather than soft shadows or organic shapes.

## Colors
This design system utilizes a high-contrast dark mode foundation to reduce eye strain for drivers in various lighting conditions and to emphasize the "Industrial-Technical" aesthetic.

- **Graphite (#2B2B2B):** Used for primary surfaces and container backgrounds.
- **Safety Orange (#FF6B00):** Reserved for primary actions, critical alerts, and active states. It acts as the "hazard light" of the UI.
- **Silver (#C0C0C0):** Used for borders, secondary text, and iconography to provide a metallic, high-tech finish.
- **Pure Black (#000000) & Deep Charcoal (#1A1A1A):** Used for background depth and card nesting to maintain high density without visual clutter.

## Typography
The typography strategy differentiates between **Instructional UI** and **Technical Data**.

- **Inter (Sans-Serif):** Used for all navigational elements, buttons, and instructional text. It provides the necessary legibility and "robust" feel required for a professional tool. Use heavier weights (600+) for headlines to ground the layout.
- **Space Grotesk (Monospace/Technical):** Used for all telematics, timestamps, coordinates, and metrics. This font reinforces the "high-tech" precision of the brand. All numerical data must be rendered in Space Grotesk to ensure alignment and rapid scanning.

## Layout & Spacing
This design system utilizes a **High-Density Fluid Grid** optimized for mobile dashboard viewing. 

- **Rhythm:** A strict 4px baseline grid ensures all elements align with engineering precision.
- **Density:** Information density is high. Use 12px gutters to pack data points closely while maintaining touch-target integrity for drivers (minimum 44px height for interactive zones).
- **Subtle Grids:** Use 1px Silver (#C0C0C0) lines at 10% opacity as background overlays in data-heavy sections to simulate a blueprint or technical schematic.

## Elevation & Depth
In alignment with the "Industrial" aesthetic, this design system eschews soft shadows in favor of **Structural Layering** and **Bold Borders**.

- **Level 0 (Background):** Pure Black (#000000).
- **Level 1 (Card/Container):** Graphite (#2B2B2B) with a 1px solid Silver (#C0C0C0) border.
- **Level 2 (Popovers/Modals):** Graphite (#2B2B2B) with a 2px Safety Orange (#FF6B00) accent border on the top or left edge.
- **Visual Depth:** Depth is created through "Technical Borders"—internal 1px lines that divide sections within a card, rather than using drop shadows.

## Shapes
The shape language is strictly **Sharp (0px)**. 

To evoke a sense of machinery and hardware, all buttons, cards, and input fields must feature hard 90-degree angles. To add a "High-Tech" flourish, certain large containers or primary buttons may use a "chamfered" corner (a 45-degree clip) of 8px on the top-right or bottom-left corner to simulate military-grade equipment.

## Components

- **Buttons:** Primary buttons use a solid Safety Orange (#FF6B00) fill with black text. Secondary buttons use a transparent fill with a 2px Silver border and Silver text.
- **Data Cards:** Containers for telematics should feature a "header bar" in a slightly lighter shade of Graphite with the metric label in Space Grotesk.
- **Status Indicators:** Use small, square-shaped pips (not circles) for status. Optimal status is "Electric Green" (#00FF41); Critical is "Flash Red" (#FF0000).
- **Technical Inputs:** Input fields should have a 1px Silver border that turns Safety Orange on focus. Use "Space Grotesk" for the input text to maintain the technical feel.
- **Gauges & Progress:** Use segmented bars rather than smooth fills to represent percentages (e.g., fuel levels, risk scores), mimicking LED hardware displays.
- **Dividers:** Use dashed or dotted 1px Silver lines to separate data points within a single view.