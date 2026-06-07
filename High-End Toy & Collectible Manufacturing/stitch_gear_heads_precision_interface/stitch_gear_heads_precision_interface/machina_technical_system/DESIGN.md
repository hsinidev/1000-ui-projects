---
name: Machina Technical System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#121212'
  on-primary-container: '#7e7d7d'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#ffb4a8'
  on-tertiary: '#690100'
  tertiary-container: '#2f0000'
  on-tertiary-container: '#fb0000'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474646'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffdad4'
  tertiary-fixed-dim: '#ffb4a8'
  on-tertiary-fixed: '#410000'
  on-tertiary-fixed-variant: '#930100'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  spec-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 4px
  gutter: 16px
  margin: 32px
  panel-padding: 24px
  stack-sm: 8px
  stack-md: 16px
---

## Brand & Style

The design system is engineered to evoke the precision of high-end automotive manufacturing and the raw aesthetic of professional workshops. It targets the serious collector—the "Gear-Head"—who values mechanical integrity and technical specification over mere decoration.

The visual style is a fusion of **Industrial Brutalism** and **Tactile Skeuomorphism**. It utilizes high-contrast structural lines, blueprint-inspired background patterns, and metallic textures to create an interface that feels like a piece of high-performance machinery. Every element is designed to look "machined" rather than "rendered," providing an emotional response of reliability, speed, and premium engineering.

## Colors

The palette is strictly functional, rooted in the materials of the automotive industry. 

- **Matte Black (#121212):** Used as the primary canvas to simulate carbon fiber and powder-coated chassis components.
- **Chrome/Silver (#C0C0C0):** Utilized for structural borders, iconography, and interactive triggers, mimicking polished steel.
- **Racing Red (#FF0000):** Reserved exclusively for critical alerts, "ignition" actions, and performance highlights.
- **Technical Blue (Secondary Accent):** A muted #1E293B should be used for background grid lines and blueprint schematics to provide depth without distracting from the primary content.

## Typography

This design system utilizes a dual-typeface strategy to balance readability with technical flair. 

**Space Grotesk** is used for headlines, labels, and technical specifications. Its geometric nature mimics the aesthetic of monospaced fonts while maintaining superior legibility at various scales. It should be used in all-caps for labels and navigation to reinforce the "instrumentation" feel.

**Inter** is the workhorse for long-form descriptions and body copy, ensuring that complex product details are easily digestible against dark, high-contrast backgrounds. Technical specs should always be rendered in the `spec-mono` style to distinguish data from narrative text.

## Layout & Spacing

The layout follows a **Fixed 12-Column Grid** reminiscent of a drafting table. Elements are aligned to a strict 4px baseline grid to ensure mathematical precision. 

Margins and gutters are generous to prevent the dense technical imagery from feeling cluttered. Content is organized into "Modules" or "Cells," separated by high-contrast Chrome dividers. Navigation should be positioned in a "Dashboard" configuration—either fixed to the left or top—mimicking a vehicle's control panel. Backgrounds should feature a subtle 32px square grid pattern in a low-opacity technical blue to reinforce the blueprint theme.

## Elevation & Depth

Depth in this design system is not achieved through soft shadows, but through **Tonal Layering** and **High-Contrast Outlines**. 

- **Surface 0:** The "Chassis" (Matte Black background).
- **Surface 1:** "Panels" (Neutral #1A1A1A) with 1px Chrome borders.
- **Surface 2:** "Inlays" (Deep black #0A0A0A) used for input fields or data readouts, creating an inset "gauged" look.

Interactive elements use "Chiseled" edges—1px inner highlights on the top and left to simulate a beveled metallic surface. Use 0% blur on all shadows to maintain a crisp, industrial edge.

## Shapes

The design system employs a **Sharp (0px)** corner radius for all primary structural elements, reflecting machined metal components. 

Subtle variation is allowed only for "internal" components like buttons or progress bars, which may use a 2px radius to imply a slightly more ergonomic "touch point." However, cards, modals, and primary containers must remain strictly rectangular. Large containers should occasionally feature "clipped corners" (45-degree chamfers) to evoke the look of customized performance parts.

## Components

### Buttons
Primary buttons should feature a Chrome/Silver background with Black text. On hover, they shift to Racing Red with White text, mimicking an "activated" state. Secondary buttons are outlined in 1px Silver with no fill.

### Gauges & Data Visualization
Instead of standard progress bars, use circular or linear gauges that resemble tachometers. Use Racing Red for "critical" zones (e.g., limited stock or high-performance stats).

### Input Fields
Inputs are inset (inner shadow, 0 blur) to look like they are carved into the dashboard. Labels are always positioned above the field in `label-caps` style.

### Cards
Product cards must include a "Spec-Sheet" footer. This is a dedicated section at the bottom of the card using a monospaced font to list scale (e.g., 1:18), material, and weight.

### Technical Overlays
Use blueprint-style line work as decorative elements behind product photos. Components like tooltips should appear as "call-outs" with diagonal leader lines pointing to specific parts of the car model.