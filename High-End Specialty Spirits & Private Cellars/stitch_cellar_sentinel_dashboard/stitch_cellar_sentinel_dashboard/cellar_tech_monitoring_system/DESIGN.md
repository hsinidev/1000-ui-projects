---
name: Cellar-Tech Monitoring System
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e4e2e3'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#e4e2e3'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#45474c'
  surface-tint: '#bec6dc'
  primary: '#bec6dc'
  on-primary: '#283041'
  primary-container: '#020817'
  on-primary-container: '#71798c'
  inverse-primary: '#565e71'
  secondary: '#c8c6c8'
  on-secondary: '#303032'
  secondary-container: '#474649'
  on-secondary-container: '#b6b4b7'
  tertiary: '#e5bfa9'
  on-tertiary: '#422b1c'
  tertiary-container: '#140500'
  on-tertiary-container: '#92725f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe2f8'
  primary-fixed-dim: '#bec6dc'
  on-primary-fixed: '#131c2b'
  on-primary-fixed-variant: '#3f4758'
  secondary-fixed: '#e4e2e4'
  secondary-fixed-dim: '#c8c6c8'
  on-secondary-fixed: '#1b1b1d'
  on-secondary-fixed-variant: '#474649'
  tertiary-fixed: '#ffdcc7'
  tertiary-fixed-dim: '#e5bfa9'
  on-tertiary-fixed: '#2b1709'
  on-tertiary-fixed-variant: '#5b4130'
  background: '#131315'
  on-background: '#e4e2e3'
  surface-variant: '#353436'
typography:
  display-data:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0em
spacing:
  unit: 4px
  container-padding-mobile: 12px
  element-gap: 8px
  grid-gutter: 4px
---

## Brand & Style

The design system is engineered for high-stakes environmental monitoring where precision is paramount. The brand personality is **Technical, Stealth, and Authoritative**, evoking the feeling of a mission-control dashboard used in professional viticulture and high-end cellar management.

The visual style blends **Modern Brutalism** with **Tactical Instrumentation**. It prioritizes data density and rapid pattern recognition over decorative whitespace. Key characteristics include:
- **Stealth Aesthetics:** A darkened interface that minimizes eye strain in low-light cellar environments.
- **High-Performance Readability:** Monospaced data points ensure vertical alignment of digits, critical for comparing fluctuating metrics like humidity and temperature.
- **Industrial Precision:** Thin, high-contrast borders and subtle glows emulate physical hardware displays and glass-cockpit instrumentation.

## Colors

The palette is designed for a "Lights Out" operation mode, utilizing deep pigments to maintain user night vision while providing high-contrast triggers for action.

- **Midnight Blue (#020817):** The foundation. A near-black navy used for the primary canvas to provide more depth than pure black.
- **Graphite (#1C1C1E):** Used for elevated UI components, cards, and structural containers to differentiate depth without losing the stealth feel.
- **Safety Orange (#FF6B00):** The singular action color. Used for primary buttons, active states, and non-critical warnings. It should be used sparingly to maintain its "High-Alert" utility.
- **Critical Red (#FF0033):** Reserved exclusively for life-safety or stock-damaging alerts (e.g., rapid temperature spikes).
- **Data Cyan (#00F0FF):** A secondary accent used strictly for data visualization lines and active sensor "pings" to contrast against the orange/red warning spectrum.

## Typography

This design system utilizes a hybrid typographic approach to maximize both readability and technical character.

- **JetBrains Mono** is the functional workhorse. It is used for all headers, labels, and numeric data to ensure that columns of figures align perfectly, allowing for instant "flicker" detection in data changes.
- **Inter** is utilized for long-form text, descriptions, and tooltips where variable-width characters improve reading speed.
- **Data Density:** Line heights are kept tight (1.0 to 1.2 for data) to pack maximum information onto mobile screens, reflecting a "no-nonsense" industrial utility.

## Layout & Spacing

The layout philosophy follows a **Modular Grid** system based on a 4px base unit. 

- **Density:** Padding is intentionally minimal (12px standard container margins on mobile) to prioritize data visibility over "breathability."
- **Grid:** A 12-column fluid grid is used for desktop, reflowing to a 2-column or single-column stack on mobile. Gutters are kept thin (4px) to emphasize the interconnected, "instrument panel" feel.
- **Alignment:** All elements must align to the hard grid lines. Avoid soft-centering; use edge-to-edge containers where possible to maximize the utility of the small mobile screen footprint.

## Elevation & Depth

In this design system, depth is conveyed through **Tonal Layering and Glowing Outlines** rather than traditional shadows.

- **Surface Tiers:** Background is Midnight Blue. Level 1 containers are Graphite. Level 2 (modals/pop-overs) are a slightly lighter Graphite with a 1px border.
- **Crisp Outlines:** Instead of shadows, use 1px solid borders (#2D2D30). 
- **Active Glow:** Interactive or "Live" elements use a subtle outer glow (0-4px blur) in the color of the data being displayed (e.g., a cyan glow for an active sensor).
- **Z-Index Strategy:** Only Critical Alerts use a high-contrast overlay. All other data is treated as a single, flat plane of glass.

## Shapes

The design system employs **Sharp (0px)** corners for all primary UI elements, including cards, buttons, and input fields. 

This decision reinforces the "Industrial/Tactical" feel and ensures that elements can be packed tightly together without the visual "dead space" created by rounded corners. Occasional 2px chamfers may be used for specific icon containers to mimic machined metal, but the default state is strictly rectangular.

## Components

- **Action Buttons:** Square corners, solid Safety Orange background for primary actions. Text is black or deep navy for maximum contrast. Secondary buttons are outlined in Graphite with white text.
- **Data Cards:** Edge-to-edge on mobile, separated by 1px Graphite dividers. Each card features a "Label-Caps" header and a large "Display-Data" value.
- **Status Indicators:** A small 8px square pulse. A steady Cyan pulse indicates "Normal," while a rapid Red strobe indicates "Critical Alarm."
- **Input Fields:** Dark background (#000000) with a 1px Graphite border. Upon focus, the border changes to Safety Orange with a subtle inner glow.
- **Micro-Sparklines:** Integrated directly into data cards. These should be 1px thick lines with no fill, showing the last 24 hours of data.
- **Technical Readouts:** Use "Data-Mono" for all list-based sensor outputs. Every row should have a subtle hover state or active highlight using a 10% opacity Safety Orange overlay.