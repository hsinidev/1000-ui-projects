---
name: Horological Technical System
colors:
  surface: '#111317'
  surface-dim: '#111317'
  surface-bright: '#37393d'
  surface-container-lowest: '#0c0e11'
  surface-container-low: '#1a1c1f'
  surface-container: '#1e2023'
  surface-container-high: '#282a2d'
  surface-container-highest: '#333538'
  on-surface: '#e2e2e6'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e2e2e6'
  inverse-on-surface: '#2f3034'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c2c7cf'
  on-secondary: '#2c3137'
  secondary-container: '#444a50'
  on-secondary-container: '#b4b9c1'
  tertiary: '#cbcfd5'
  on-tertiary: '#2d3136'
  tertiary-container: '#b0b3ba'
  on-tertiary-container: '#41454b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#dee3eb'
  secondary-fixed-dim: '#c2c7cf'
  on-secondary-fixed: '#171c22'
  on-secondary-fixed-variant: '#42474e'
  tertiary-fixed: '#e0e2e9'
  tertiary-fixed-dim: '#c3c6cd'
  on-tertiary-fixed: '#181c21'
  on-tertiary-fixed-variant: '#43474d'
  background: '#111317'
  on-background: '#e2e2e6'
  surface-variant: '#333538'
typography:
  headline-xl:
    fontFamily: ebGaramond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: ebGaramond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: ebGaramond
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.2'
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-technical:
    fontFamily: ibmPlexMono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  hairline: 1px
---

## Brand & Style

This design system is anchored in the intersection of traditional Swiss horology and futuristic blockchain immutability. It targets high-net-worth collectors and technical auditors who value the "machined" precision of a luxury timepiece. The aesthetic is **Industrial-Luxe**: a blend of rigorous engineering blueprints and the refined atmosphere of a private atelier.

The visual language emphasizes transparency and structural integrity. Every element should feel as though it was milled from a single block of steel or hand-set by a master watchmaker. Motion should mimic the rhythmic, stepped intervals of a mechanical movement (the "sweep") rather than the fluid, organic easing found in consumer apps.

## Colors

The palette is dominated by **Slate** and **Brushed Steel**, creating a low-light "vault" environment that allows the **Champagne Gold** accents to signify value and authenticity.

- **Slate (#0D0F12, #1E2227):** Used for the primary canvas to evoke depth and the velvet lining of a watch box.
- **Brushed Steel (#A8ADB5):** Applied to structural elements, borders, and secondary text, simulating CNC-machined components.
- **Champagne Gold (#D4AF37):** Reserved exclusively for "Grand Complications"—critical CTAs, certificates of authenticity, and high-value status indicators.
- **Signal Red (#E63946):** A functional accent used sparingly for "Service Required" alerts or security warnings, inspired by ruby bearings in a watch movement.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage and technology.

- **Headlines:** `ebGaramond` provides a sense of history and provenance. It should be used for product names, section titles, and narrative elements.
- **Body & UI:** `Inter` ensures maximum legibility for descriptions and interface controls, maintaining a clean, neutral tone.
- **Data & Metadata:** `IBM Plex Mono` is the "caliper" font. It is used for blockchain hashes, serial numbers, caliber specifications, and timestamps. The monospaced nature reflects technical readouts and engineering logs.

All caps should be applied to labels and small navigation items to reinforce the industrial-luxe aesthetic.

## Layout & Spacing

The layout is governed by a **strict 12-column engineering grid**. Unlike fluid consumer web layouts, this system uses visible hairline dividers to "frame" content, much like the chassis of a watch movement.

- **Grid:** Content should be partitioned by 1px "Brushed Steel" borders (opacity 20%). 
- **Rhythm:** A 4px baseline grid ensures vertical precision. 
- **Adaptation:** On desktop, use wide margins to create a "spec sheet" feel. On mobile, transition to a 4-column grid, maintaining the hairline dividers to keep the technical structure intact.
- **Safe Areas:** Elements should never feel crowded; use generous padding within bordered containers to evoke the luxury of empty space.

## Elevation & Depth

In this design system, depth is not conveyed through soft shadows, but through **tonal layering and hairline strokes**.

- **Tonal Layers:** Surfaces are stacked using varying shades of Slate. A "raised" card is simply a slightly lighter shade of Slate with a 1px steel border.
- **Milled Edges:** Instead of shadows, use inner glows (subtle Gold or White, 2-5% opacity) on the top edges of cards to simulate light catching a chamfered metal edge.
- **Glassmorphism:** Use sparingly for technical overlays (e.g., a "loupe" view of a watch). High-diffusion backdrop blurs help maintain focus while showing the structural "movement" beneath the surface.

## Shapes

To reflect engineering-grade precision, this design system utilizes **sharp, 0px radiuses** for all primary containers, buttons, and input fields. 

In specific cases where a "mechanical" feel is required—such as a circular complication or a dial-style progress indicator—perfect circles are permitted. However, the containers holding these circles must remain rectangular and sharp. This juxtaposition emphasizes the "machine-cut" nature of the registry.

## Components

- **Buttons:** Primary buttons are Slate with a Champagne Gold 1px border. On hover, the border weight does not change, but the gold gains a subtle outer glow (0px 0px 8px). Text is always uppercase `label-caps`.
- **Registry Cards:** These should look like physical certificates of authenticity. Use a 1px border and a subtle "brushed metal" texture background (CSS noise). Include a monospaced "Serial Number" at the top right.
- **Data Tables:** Use 1px vertical and horizontal dividers. Header cells should have a slightly darker Slate background than body cells.
- **Micro-interactions:**
    - **The Sweep:** Loaders should mimic a mechanical second hand, moving in 1/8th second increments rather than a smooth continuous spin.
    - **The Click:** Button presses should feel "tactile" with a slight 1px offset shift, mimicking a physical pusher on a chronograph.
- **Status Chips:** Use technical iconography (e.g., a gear for "Processing," a shield for "Verified"). Avoid rounded pills; use sharp-edged tags.
- **The Chrono-Dial:** A unique component for this design system, used for visualizing "Time Since Last Service" or "Ownership Duration," styled as a 24-hour mechanical gauge.