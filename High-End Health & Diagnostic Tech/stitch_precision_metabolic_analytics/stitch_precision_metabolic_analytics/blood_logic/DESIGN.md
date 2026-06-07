---
name: Blood-Logic
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fb'
  on-surface: '#111c2d'
  on-surface-variant: '#44474d'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#75777e'
  outline-variant: '#c5c6cd'
  surface-tint: '#515f78'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#0d1c32'
  on-primary-container: '#76849f'
  inverse-primary: '#b9c7e4'
  secondary: '#006c4d'
  on-secondary: '#ffffff'
  secondary-container: '#86f8c8'
  on-secondary-container: '#007352'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#171c1f'
  on-tertiary-container: '#808488'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#86f8c8'
  secondary-fixed-dim: '#69dbad'
  on-secondary-fixed: '#002115'
  on-secondary-fixed-variant: '#005139'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  display-data:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Hanken Grotesk
    fontSize: 30px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Hanken Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-label:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
  data-value:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
spacing:
  base: 4px
  gutter: 16px
  margin: 24px
  grid_line: 1px
---

## Brand & Style
The personality of this design system is clinical, authoritative, and unapologetically technical. It is designed for users who view their biological data as a high-performance machine to be tuned, rather than a lifestyle metric to be gamified. The aesthetic draws heavily from 20th-century Swiss International Style and modern laboratory information management systems (LIMS). 

The style is defined by **Scientific Minimalism**: a rigid adherence to grid structures, high-contrast legibility, and the removal of all decorative "fluff." There are no soft shadows or organic blurs; instead, hierarchy is established through line weight, compartmentalization, and precise typographic scaling. The goal is to evoke the feeling of a professional diagnostic workstation—efficient, sterile, and hyper-accurate.

## Colors
This design system utilizes a high-contrast palette designed for clinical clarity. 

- **Laboratory Blue (#0A192F):** Used for primary navigation, deep-background data containers, and high-emphasis text. It provides the "professional weight" of the UI.
- **Sterile White (#FFFFFF):** The primary canvas color. It creates a clean, medical-grade environment that makes data pop.
- **Biomarker Mint (#3EB489):** Reserved exclusively for "Optimal/In-Range" status indicators, success states, and primary call-to-action accents.
- **Data Grey (#64748B):** Used for grid lines, axis labels, and secondary metadata to ensure they remain functional but non-distracting.
- **Alert Red (#E11D48):** Used sparingly for "Out-of-Range" or critical biomarker alerts.

## Typography
The typography strategy distinguishes between **Narrative** and **Technical** information. 

**Hanken Grotesk** handles the narrative layer: headings, descriptions, and UI labels. Its sharp, geometric construction maintains a modern, professional tone. 

**JetBrains Mono** is utilized for all quantitative data, timestamps, and laboratory units (e.g., mg/dL, mmol/L). The monospaced nature ensures that fluctuating real-time values do not cause layout shifts and allows for easy vertical scanning of numerical columns. All data labels should be set in uppercase with slight tracking for maximum legibility at small sizes.

## Layout & Spacing
This design system employs a **Modular Grid** philosophy. The layout is structured on a strict 4px baseline grid. 

- **The Blueprint Layer:** A subtle 32px x 32px background grid is visible in data-heavy views, reinforcing the scientific "worksheet" aesthetic.
- **Containers:** Content is divided into modular "cells" separated by 1px solid borders rather than cards with shadows.
- **Density:** Information density is high. Padding should be efficient (12px to 16px) to allow for the simultaneous display of multiple charts and telemetry feeds without requiring excessive scrolling.
- **Alignment:** All elements must snap to the grid. Vertical lines should be used to separate sidebar navigation from the primary data stage.

## Elevation & Depth
Depth in this design system is achieved through **Tonal Layering** and **Line Work** rather than Z-axis shadows. 

- **Surface Tiers:** The base layer is Sterile White. Secondary modules use a very faint grey (#F8FAFC) to create subtle distinction. Global navigation or critical focus areas use Laboratory Blue to "punch out" from the white canvas.
- **Intersections:** Depth is signaled by 1px "Ghost Borders" (#E2E8F0). When a user interacts with a module, the border weight does not change, but the color shifts to Laboratory Blue.
- **Overlays:** Modals and tooltips use a sharp, 1px Laboratory Blue border and no backdrop blur, maintaining the high-contrast, technical transparency.

## Shapes
In keeping with the themes of precision and structural integrity, this design system uses **Sharp (0px)** corners for all primary containers, buttons, and input fields. 

The use of 90-degree angles reflects the rigid accuracy of a laboratory environment. The only exception to this rule is for status "Pills" (e.g., indicating a sensor is 'Active') which may use a full-radius cap to distinguish them from interactive buttons.

## Components
- **Buttons:** Rectangular with 0px radius. Primary buttons are solid Laboratory Blue with White text. Secondary buttons are 1px Laboratory Blue outlines.
- **Data Charts:** Use thin (1.5px) lines for trends. No curved paths; use straight-line connections between data points to reflect raw, unmanipulated telemetry. Fill areas under the line with a 5% opacity of the line color.
- **Biomarker Chips:** Used for range status. "Within Range" is a Mint outline with a small solid Mint dot. "Out of Range" uses Alert Red.
- **Inputs:** Underlined or fully boxed with a 1px frame. Focus states are indicated by a color shift to Laboratory Blue and the appearance of a small Monospace cursor.
- **The "Telemetry Strip":** A specific component for CGM data—a horizontal scrolling ticker of monospace values and a micro-sparkline, placed at the top of the viewport.
- **Grid Lists:** Data tables should have "Zebra" striping using a 2% Laboratory Blue tint and 1px horizontal dividers.