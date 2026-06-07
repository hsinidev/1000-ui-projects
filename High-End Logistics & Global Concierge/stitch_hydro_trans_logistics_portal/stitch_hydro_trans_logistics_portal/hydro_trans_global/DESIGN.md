---
name: Hydro-Trans Global
colors:
  surface: '#101414'
  surface-dim: '#101414'
  surface-bright: '#353a3a'
  surface-container-lowest: '#0a0f0f'
  surface-container-low: '#181c1c'
  surface-container: '#1c2020'
  surface-container-high: '#262b2b'
  surface-container-highest: '#313635'
  on-surface: '#dfe3e2'
  on-surface-variant: '#bdc9c8'
  inverse-surface: '#dfe3e2'
  inverse-on-surface: '#2c3131'
  outline: '#879392'
  outline-variant: '#3e4949'
  surface-tint: '#76d6d5'
  primary: '#76d6d5'
  on-primary: '#003737'
  primary-container: '#008080'
  on-primary-container: '#e3fffe'
  inverse-primary: '#006a6a'
  secondary: '#bec8cd'
  on-secondary: '#293236'
  secondary-container: '#414a4f'
  on-secondary-container: '#b0babf'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#717373'
  on-tertiary-container: '#f9f9f9'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#93f2f2'
  primary-fixed-dim: '#76d6d5'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#dbe4e9'
  secondary-fixed-dim: '#bec8cd'
  on-secondary-fixed: '#141d21'
  on-secondary-fixed-variant: '#3f484c'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#101414'
  on-background: '#dfe3e2'
  surface-variant: '#313635'
typography:
  headline-xl:
    fontFamily: Metropolis
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-reg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-tabular:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 24px
  margin-edge: 40px
  container-max: 1440px
  touch-target: 44px
---

## Brand & Style
The design system reflects the intersection of maritime precision and high-end concierge service. It is built for a dual audience: elite yacht crews managing complex inventories and owners who expect a refined, premium experience. The personality is authoritative, "over-engineered," and serene.

The style is **Nautical-Industrial**. It leverages the structural rigidity of naval engineering (grid lines, monospaced data, heavy borders) but softens it with luxury finishes (refined typography, expansive white space, and a curated color palette). The UI should evoke the feeling of a glass-cockpit instrument panel found on a modern superyacht: high-density information presented with absolute clarity and aesthetic poise.

## Colors
The palette is dominated by **Gunmetal (#2C3539)** to establish a "night-bridge" environment that reduces eye strain in maritime conditions. **Teal (#008080)** serves as the primary action and status color, representing the deep ocean and technical reliability. **Crisp White (#FFFFFF)** is used sparingly for high-priority text and "active" UI highlights to ensure maximum contrast.

Secondary accents should include a technical orange for warnings (engine alerts, delivery delays) to contrast against the teal. Backgrounds should use varying depths of Gunmetal to create hierarchy without breaking the dark-mode immersion.

## Typography
The typographic hierarchy prioritizes legibility under variable lighting conditions. **Metropolis** provides a geometric, structured feel for headings, often used in All-Caps for a navigational "instrument" aesthetic. 

**Inter** handles standard interface text and body copy for its neutral, high-readability characteristics. All technical data, coordinates, timestamps, and inventory IDs must be set in **JetBrains Mono**. This monospaced choice reinforces the industrial-grade precision of the logistics platform and ensures that columns of numbers align perfectly in manifests.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for desktop dashboards to ensure that map overlays and data panels remain in predictable positions—critical for muscle memory in high-pressure logistics. A 12-column grid is used with generous 24px gutters to prevent visual clutter.

On mobile, the system transitions to a high-density list-view optimized for one-handed scanning. Use a 4px base unit for all padding and margins to maintain a tight, "engineered" rhythm. Map-centric layouts should occupy the background layer, with UI "modules" floating in structured sidebars or bottom sheets.

## Elevation & Depth
This design system uses **Tonal Layers** combined with **Low-contrast Outlines** rather than traditional shadows. Depth is achieved by lightening the Gunmetal base:
- **Level 0 (Deep):** Background/Map layer (#1A2023)
- **Level 1 (Surface):** Default panel color (#2C3539)
- **Level 2 (Raised):** Active cards or hovered states (#3E4A50)

To emphasize the nautical-industrial aesthetic, use 1px solid borders in a slightly lighter Gunmetal shade to define shapes. For high-priority overlays (like weather warnings), apply a 20px backdrop blur to "Glassmorphic" containers to maintain the context of the underlying map while ensuring text remains legible.

## Shapes
The shape language is **Sharp (0px)**. To reflect the "industrial-grade" and "high-precision" nature of maritime hardware, UI elements should have hard, 90-degree corners. This creates a rigorous, architectural feel. 

Exceptions are made only for status pips (circular indicators for "Vessel Online") and specific icon enclosures. Buttons, input fields, and containers must remain rectangular to mimic the physical monitors and bulkhead-mounted equipment found in a yacht's engine room or bridge.

## Components
- **Buttons:** Primary buttons use a solid Teal (#008080) fill with White All-Caps JetBrains Mono text. Secondary buttons use a Teal outline with no fill.
- **Data Visualizations:** Charts must use high-contrast lines. Area charts should use a Teal-to-Transparent gradient. Map pins are sharp diamonds, not teardrops.
- **Inventory Cards:** Use a heavy top-border (2px) in Teal to indicate "Selected" or "Active." All metrics within the card must use monospaced fonts.
- **Mobile Scanners:** A dedicated full-screen interface with a high-contrast viewfinder. Feedback for a "Success" scan should trigger a full-border Teal flash.
- **Weather Overlays:** Semi-transparent layers with vector wind-barbs and isobar lines. Legend labels use `label-caps` typography.
- **Input Fields:** Bottom-border only in Crisp White for a sophisticated, minimal look, or full-border Gunmetal for industrial utility.
- **Status Chips:** Rectangular tags with a 1px border. Use color-coded text (Teal for "Delivered," Orange for "In Transit") rather than solid background fills to maintain a clean, high-end look.