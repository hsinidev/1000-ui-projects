---
name: BioSphere-LIMS
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
  on-surface-variant: '#434654'
  inverse-surface: '#263143'
  inverse-on-surface: '#ecf1ff'
  outline: '#747685'
  outline-variant: '#c4c5d6'
  surface-tint: '#2854cc'
  primary: '#214fc7'
  on-primary: '#ffffff'
  primary-container: '#4169e1'
  on-primary-container: '#f8f7ff'
  inverse-primary: '#b6c4ff'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#565a5b'
  on-tertiary: '#ffffff'
  tertiary-container: '#6f7274'
  on-tertiary-container: '#f6f8fa'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#00164e'
  on-primary-fixed-variant: '#003baf'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9ff'
  on-background: '#111c2d'
  surface-variant: '#d8e3fb'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  data-mono:
    fontFamily: Public Sans
    fontSize: 13px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Public Sans
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 12px
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 12px
  margin: 24px
  container-max: 1600px
  density-compact: 4px
  density-comfortable: 8px
---

## Brand & Style

The design system is engineered for the high-stakes environment of large-scale scientific research. It prioritizes data integrity, auditability, and cognitive efficiency over decorative flair. The brand personality is expert, immutable, and hyper-reliable, evoking the same sense of trust as a piece of calibrated laboratory hardware.

The aesthetic follows a **Corporate / Modern** approach with a heavy emphasis on **Minimalism** to manage high information density. Every pixel must serve a functional purpose. The UI should evoke a "clinical" emotional response—clean, sterile, and absolute—ensuring that researchers can navigate complex datasets without visual fatigue or ambiguity.

## Colors

This design system utilizes a high-contrast, clinical palette to differentiate between structural elements and interactive data. 

- **Royal Blue (#4169E1)** is the primary action color, reserved for key interactions, primary buttons, and active states. 
- **Slate Grey (#708090)** serves as the structural backbone, used for borders, icons, and secondary text to provide a sophisticated, technical feel.
- **White (#FFFFFF)** and **Off-White (#F8FAFC)** provide the "clean-room" backdrop, ensuring that data points remain the focal point.
- **Functional Colors** for GLP/GMP compliance (Success, Warning, Error) are highly saturated to ensure instant recognition during rapid audits.

## Typography

The design system employs **Public Sans** for its institutional clarity and neutral metrics. The type scale is optimized for high-density layouts where vertical space is at a premium. 

To maintain clinical precision, use `data-mono` (tabular figures) for all numerical technical data, ensuring that columns of figures align perfectly for easy comparison. `label-caps` should be used for table headers and metadata descriptors to provide a clear visual hierarchy against body text. All type should favor high contrast against backgrounds to meet accessibility standards for professional lab environments.

## Layout & Spacing

This design system utilizes a **Fixed Grid** approach for primary dashboard views to ensure consistency across large-format laboratory monitors. A 12-column system is used for structural layouts, while a strict 4px baseline grid governs internal component spacing.

High-density is achieved through "compact" padding scales, allowing for more data rows to be visible above the fold. Gutters are kept narrow (12px) to maximize horizontal space for complex data tables. Layouts should be strictly aligned to the grid to reinforce the "organized and robust" aesthetic.

## Elevation & Depth

To maintain a "clinical and precise" feel, this design system avoids heavy shadows and decorative blurs. Instead, it uses **Low-contrast outlines** and **Tonal layers** to establish hierarchy.

- **Level 0 (Base):** White (#FFFFFF) for the primary workspace.
- **Level 1 (Surface):** Off-white (#F8FAFC) for sidebars, headers, and grouping containers, separated by 1px borders in Slate Grey at 20% opacity.
- **Level 2 (Active/Pop-over):** Uses a crisp 1px solid border in Slate Grey with a very tight, low-opacity (10%) ambient shadow to indicate temporary focus.
- **Separators:** Use thin, 1px horizontal and vertical lines rather than whitespace to define boundaries in data-heavy tables.

## Shapes

The design system uses **Sharp (0px)** corners for all UI elements. This decision reinforces the "robust and industrial" nature of a LIMS. Square edges suggest modularity, precision, and a no-nonsense technical environment. Primary buttons, input fields, and status badges should all maintain perfectly square corners to differentiate the system from consumer-grade applications.

## Components

### Data Tables
The core of the system. Use zebra-striping (F8FAFC) for readability. Headers must be sticky with a 2px Slate Grey bottom border. Columns containing numerical data must use tabular figures and right-alignment.

### Status Indicators (GLP/GMP)
Rectangular badges with a 1px solid border matching the status color. Backgrounds should be a 10% tint of the status color. Use `label-caps` for the text within.

### Interactive Timelines
For chain-of-custody, use a vertical track. Nodes are 8px solid squares. Active nodes use Royal Blue; completed nodes use Slate Grey. Hovering over a node reveals a high-density "technical card" with timestamps and operator IDs.

### Buttons
- **Primary:** Solid Royal Blue, White text, 0px radius.
- **Secondary:** White background, 1px Slate Grey border, Slate Grey text.
- **Action Icons:** 16px glyphs within a 24px hit area to maintain density.

### Input Fields
Strict 1px Slate Grey borders. Focus state is a 2px Royal Blue internal border. Labels are positioned top-left in `label-caps` to save horizontal space.

### Compliance Badges
Small, high-contrast markers placed in the top-right of containers to indicate that the data viewed is locked or verified under specific regulatory protocols.