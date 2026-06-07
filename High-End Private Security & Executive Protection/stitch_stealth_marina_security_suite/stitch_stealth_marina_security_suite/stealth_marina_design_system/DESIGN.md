---
name: Stealth-Marina Design System
colors:
  surface: '#111316'
  surface-dim: '#111316'
  surface-bright: '#37393d'
  surface-container-lowest: '#0c0e11'
  surface-container-low: '#1a1c1f'
  surface-container: '#1e2023'
  surface-container-high: '#282a2d'
  surface-container-highest: '#333538'
  on-surface: '#e2e2e6'
  on-surface-variant: '#bac9c9'
  inverse-surface: '#e2e2e6'
  inverse-on-surface: '#2f3034'
  outline: '#859493'
  outline-variant: '#3b4949'
  surface-tint: '#2ddbde'
  primary: '#47eaed'
  on-primary: '#003738'
  primary-container: '#00ced1'
  on-primary-container: '#005354'
  inverse-primary: '#00696b'
  secondary: '#bec8cd'
  on-secondary: '#293236'
  secondary-container: '#414a4f'
  on-secondary-container: '#b0babf'
  tertiary: '#d5d5d5'
  on-tertiary: '#2f3131'
  tertiary-container: '#b9b9b9'
  on-tertiary-container: '#484a4a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#5af8fb'
  primary-fixed-dim: '#2ddbde'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f51'
  secondary-fixed: '#dbe4e9'
  secondary-fixed-dim: '#bec8cd'
  on-secondary-fixed: '#141d21'
  on-secondary-fixed-variant: '#3f484c'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#111316'
  on-background: '#e2e2e6'
  surface-variant: '#333538'
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
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  data-point:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
---

## Brand & Style

This design system embodies the intersection of elite maritime engineering and mission-critical tactical software. The brand personality is authoritative, precise, and uncompromising, designed to evoke the feeling of a high-tech command center on a modern vessel.

The visual style is **Nautical-Industrial Glassmorphism**. It combines the raw, structural integrity of brushed steel and gunmetal with the sophisticated transparency of modern tactical displays. High-contrast interfaces ensure that information is legible under the harsh glare of the midday sun or the pitch-black conditions of a midnight watch. The aesthetic relies on technical precision—thin lines, data-dense layouts, and subtle "radar" motifs—to communicate professional-grade security and luxury.

## Colors

The palette is optimized for low-light environments and high-stress visibility.

*   **Primary (Teal):** Used for "Active" states, data pings, and critical action buttons. It represents the interface's digital pulse and ensures high-visibility against dark backgrounds.
*   **Secondary (Gunmetal):** The foundation of the system. Used for structural elements, sidebars, and "milled metal" surfaces. It provides a heavy, industrial weight to the UI.
*   **Neutral (Deep Charcoal/Black):** Used for the primary canvas to minimize screen glare and maximize the depth of glassmorphic layers.
*   **Functional White:** Reserved for primary text and high-priority status indicators to ensure maximum legibility.

## Typography

Typography in this design system is treated as a technical instrument. 

**Space Grotesk** is utilized for headlines, providing a geometric, futuristic tone that feels engineered. **Geist** serves as the primary body face, selected for its exceptional clarity and "developer-spec" aesthetic which fits the industrial theme. **JetBrains Mono** is reserved for labels, coordinates, and system readouts, reinforcing the tactical, mission-critical nature of the service. All caps are used sparingly for labels to denote authority and urgency.

## Layout & Spacing

The layout utilizes a **Technical Fixed Grid**. A 12-column system is used for dashboard views, while a 4-column system is applied to mobile tactical units. 

The spacing rhythm is tight and disciplined, built on a 4px base unit to allow for high data density. Visual interest is created through the use of "Safe Zones"—generous outer margins (40px) that frame the dense, technical information in the center, much like a nautical chart or a specialized radar screen. Visible grid lines (0.5px thickness in Gunmetal) may be used to separate major UI sections, emphasizing the industrial construction.

## Elevation & Depth

Depth is not conveyed through traditional shadows, but through **Tonal Layering and Glassmorphism**. 

1.  **Level 0 (Floor):** Deepest Gunmetal/Neutral, representing the physical hull.
2.  **Level 1 (Panels):** Slightly lighter Gunmetal with a subtle brushed metal texture (low-opacity overlay).
3.  **Level 2 (Active Overlays):** Glassmorphic surfaces with a 20px backdrop-blur and 10% white opacity. These represent floating HUD elements.
4.  **Borders:** Instead of shadows, use 1px "milled" borders. Inner borders use a subtle highlight (Crisp White at 10% opacity) on the top and left edges to simulate light hitting a metal edge.

## Shapes

The shape language is rigid and structural. We use a **Soft Industrial** approach (roundedness: 1), where the default 4px radius mimics the slightly chamfered edges of precision-machined hardware. 

Avoid large, organic curves. Octagonal corner-cuts (clipped corners) are encouraged for primary action buttons and status badges to enhance the "tactical gear" aesthetic. Progress bars and sliders should remain sharp-edged or use the minimum 4px radius to maintain a professional, non-consumer appearance.

## Components

*   **Tactical Buttons:** Heavy, Gunmetal backgrounds with Teal top-borders (2px). Hover states should trigger a subtle Teal outer glow (simulating an LED backlight).
*   **Glass Cards:** Used for secondary data. Feature a 1px Crisp White border at 15% opacity and a heavy backdrop blur.
*   **Status Chips:** Monospaced text inside clipped-corner boxes. High-contrast Teal for "Secure," Warning Orange for "Alert," and Crisp White for "Neutral."
*   **Data Grids:** Radar-style circular grids used as background elements for location data. Lines should be 0.5px wide in Teal at 20% opacity.
*   **Input Fields:** Ghost-style inputs with only a bottom border (1px Gunmetal). On focus, the border turns Teal and a faint scanline animation triggers briefly.
*   **Vertical Lists:** Separated by 0.5px Gunmetal dividers with "lat/long" coordinates occasionally used as decorative markers in the margins.