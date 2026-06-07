---
name: Digital Chic
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dce6'
  primary: '#e3fdff'
  on-primary: '#00373a'
  primary-container: '#00f3ff'
  on-primary-container: '#006b71'
  inverse-primary: '#00696f'
  secondary: '#ffabf3'
  on-secondary: '#5b005b'
  secondary-container: '#fe00fe'
  on-secondary-container: '#500050'
  tertiary: '#f0ffcb'
  on-tertiary: '#253600'
  tertiary-container: '#b1f000'
  on-tertiary-container: '#4c6a00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#6ff6ff'
  primary-fixed-dim: '#00dce6'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f53'
  secondary-fixed: '#ffd7f5'
  secondary-fixed-dim: '#ffabf3'
  on-secondary-fixed: '#380038'
  on-secondary-fixed-variant: '#810081'
  tertiary-fixed: '#b6f700'
  tertiary-fixed-dim: '#9fd800'
  on-tertiary-fixed: '#141f00'
  on-tertiary-fixed-variant: '#374e00'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.2em
  technical-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 2rem
  gutter: 1.5rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2.5rem
---

## Brand & Style

This design system embodies the "Digital Chic" aesthetic, positioning itself at the intersection of high-end interior design and advanced aerospace engineering. It is designed for luxury smart-home environments where the interface acts as a seamless extension of the physical architecture. 

The visual language utilizes **Glassmorphism** and **High-Contrast Neon** elements against a deep, matte foundation to evoke a sense of precision, intelligence, and premium status. The emotional response is one of total control and calm sophistication—surfaces feel like holographic projections etched into obsidian glass. The style is unapologetically futuristic, replacing traditional tactile metaphors with light-based feedback and depth through translucency.

## Colors

The palette is anchored by a true **Matte Black** background, providing the necessary contrast for neon luminosity. 

*   **Primary (Electric Cyan):** Used for critical data, active states, and primary navigation pulses.
*   **Secondary (Cyber Magenta):** Reserved for atmospheric accents, secondary status indicators, and luxury features (e.g., "Mood" or "Entertainment" modes).
*   **Tertiary (Acid Lime):** Utilized for eco-efficiency metrics, power-saving states, and biological/health data.
*   **Glass Layers:** Surfaces are constructed using low-opacity whites with high background blur (30px-50px) to simulate frosted architectural glass. 

All interactive elements should utilize a "glow" property—a drop shadow with 0 spread and high blur—using the primary or secondary hex codes at 50% opacity.

## Typography

**Space Grotesk** is used across all levels to maintain a technical, geometric rigour. The typography should feel engineered rather than "written." 

- **Headlines:** Use tight letter spacing and bold weights to anchor the layout.
- **Labels:** Always set in uppercase with generous tracking (letter spacing) to mimic technical readouts on a HUD.
- **Body:** Kept clean and airy to balance the high-density visual accents.
- **Color Application:** Use high-brightness whites for primary text and 60% opacity whites for secondary technical descriptions. Primary Cyan can be used for numerical data to emphasize importance.

## Layout & Spacing

This design system employs a **Fluid Grid** with a strict 4px baseline rhythm. Layouts are constructed as a series of "Modules" within a 12-column system. 

- **Margins:** Large outer margins (32px+) ensure the interface feels intentional and framed.
- **Visual Rhythm:** Group related "smart" widgets into containers. Use the `stack-lg` spacing to separate major architectural zones (e.g., Climate vs. Security).
- **Alignment:** Every element must align to the grid to maintain the "technical" feel. Avoid centered layouts; prefer left-aligned technical data paired with right-aligned status icons.

## Elevation & Depth

Depth is not communicated through traditional shadows, but through **Tonal Layers and Light Transmittance**.

1.  **Base Layer:** The Matte Black `#050505` foundation.
2.  **Surface Layer:** Frosted glass containers (`rgba(255, 255, 255, 0.03)`) with a `backdrop-filter: blur(40px)`. This creates a sense of floating objects.
3.  **Edge Definition:** Instead of shadows, use 1px "Inner Glow" or "Ghost Borders" (`rgba(255, 255, 255, 0.1)`) on the top and left edges to simulate light catching the edge of a glass pane.
4.  **Active Elevation:** Interactive elements emit a soft neon outer glow (bloom effect) when active or hovered, suggesting energy flowing through the component.

## Shapes

The shape language is "Soft-Tech." While the grid is rigid, the corners are slightly eased to feel approachable and premium.

- **Containers:** Use `rounded-lg` (0.5rem) for frosted glass modules. 
- **Buttons/Inputs:** Use `rounded` (0.25rem) to maintain a sharper, more precise technical appearance. 
- **Icons:** Use geometric, thin-stroke (1.5px) icons. Avoid filled shapes; prefer "outlined" icons that appear to be made of light filaments.
- **Dividers:** Use 1px vertical or horizontal lines with a gradient fade-out to 0% opacity on both ends.

## Components

- **Frosted Glass Containers:** The standard wrapper for all dashboard content. Must include a 1px border with 10% white opacity and a backdrop blur.
- **Glowing Buttons:** Primary buttons are ghost-styled with a primary cyan border. On hover, the border glows, and the text gains a slight neon outer glow.
- **Status Chips:** Small, pill-shaped elements with a solid neon background (Cyan, Magenta, or Lime) but with 20% opacity and 100% opacity text of the same color.
- **High-Tech Dashboard Gauges:** Use circular progress arcs with neon strokes and digital numerical readouts in the center.
- **Input Fields:** Bottom-border only or very subtle ghost-borders. The cursor should be a blinking cyan block to mimic terminal interfaces.
- **Toggle Switches:** Rectangular and mechanical in appearance. When "on," the slider track should fill with a gradient of the primary color and emit a soft glow.
- **Ambient Cards:** Background-less cards that rely on the typography and 1px divider lines to separate information, used for less critical technical readouts.