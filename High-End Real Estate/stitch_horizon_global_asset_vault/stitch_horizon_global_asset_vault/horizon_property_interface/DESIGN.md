---
name: Horizon Property Interface
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1b1b1b'
  on-surface-variant: '#444650'
  inverse-surface: '#303030'
  inverse-on-surface: '#f1f1f1'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#2559bd'
  on-secondary: '#ffffff'
  secondary-container: '#6c98ff'
  on-secondary-container: '#002f76'
  tertiary: '#131514'
  on-tertiary: '#ffffff'
  tertiary-container: '#282928'
  on-tertiary-container: '#90908e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#dae2ff'
  secondary-fixed-dim: '#b1c5ff'
  on-secondary-fixed: '#001946'
  on-secondary-fixed-variant: '#00419e'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c4'
  on-tertiary-fixed: '#1b1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#f9f9f9'
  on-background: '#1b1b1b'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Work Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Work Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 24px
  margin: 40px
  stroke-heavy: 3px
  stroke-standard: 2px
---

## Brand & Style

This design system is engineered to project absolute institutional authority and "hardened" digital security. The aesthetic combines **refined Minimalism** with **Industrial Brutalism**, creating a "digital vault" experience for high-stakes asset management. 

The visual language rejects soft aesthetics in favor of structural rigidity. By utilizing heavy strokes and sharp geometries, the interface communicates stability, permanence, and impenetrable protection. The target audience—sophisticated global investors—requires a UI that prioritizes data density and clarity over decorative flourishes, evoking the feel of a tactical command center for wealth.

## Colors

The palette is anchored by **Deep Black** and **Platinum Silver**, establishing a high-contrast foundation that mimics physical security hardware and precious metals. 

- **Deep Blue (#002366):** Used for primary structural elements and headers to instill a sense of tradition and corporate legacy.
- **Tactical Accent Blue (#0047AB):** Reserved for critical actions, interactive states, and data highlights. This blue is vibrant enough to cut through the neutral base without compromising the professional tone.
- **Platinum Silver (#E5E4E2):** Serves as the primary surface color, providing a metallic, matte finish that feels more substantial than pure white.
- **Deep Black (#000000):** Used for typography and heavy 2px-3px borders to "lock" the layout in place.

## Typography

This design system utilizes a dual-font strategy to balance editorial authority with functional utility. 

**Work Sans** is used for headlines to provide a grounded, professional weight. **Inter** is the workhorse for body text and interface elements, chosen for its exceptional legibility in data-dense environments. 

For financial figures and security keys, use the `data-mono` style—utilizing Inter’s tabular num features—to ensure vertical alignment in columns. All labels should utilize the `label-caps` style to differentiate metadata from actionable content.

## Layout & Spacing

The layout philosophy is based on a **fixed, rigorous grid**. This design system employs a 12-column grid with generous 40px outer margins to frame the content as a "prestige object."

Spacing is strictly mathematical, built on a 4px baseline unit. Internal gutters are 24px, ensuring that even with heavy 3px borders, the content has sufficient breathing room. Horizontal divisions must be high-contrast, using Deep Black strokes to separate global navigation, page headers, and primary content zones.

## Elevation & Depth

This design system explicitly rejects the use of ambient shadows or soft blurs. Depth is conveyed exclusively through **Bold Borders** and **Tonal Layering**.

- **Level 0 (Base):** Platinum Silver background.
- **Level 1 (Panels):** Defined by 2px Deep Black borders. No offset.
- **Level 2 (Active/Pressed):** Elements do not "lift"; they invert. An active button or selected card fills with Deep Black or Deep Blue, while the text flips to Platinum Silver.
- **Overlays:** Modals and dropdowns use a 3px border and a sharp, solid black 8px offset (hard shadow) to simulate physical stacking without gradients.

## Shapes

The shape language is strictly **Sharp (0px)**. 

Every element—including buttons, input fields, cards, and modal windows—must feature 90-degree corners. This lack of curvature reinforces the "hardened" security narrative, suggesting a system that is unyielding and disciplined. Icons should follow this logic, utilizing straight lines and sharp angles where possible, avoiding organic or overly rounded pictograms.

## Components

### Buttons
Primary buttons are solid Deep Blue with 2px Deep Black borders and white/silver text. Secondary buttons use a Platinum Silver fill with 2px Deep Black borders. Interaction states must be instantaneous; avoid long transitions. Use a "square" aspect ratio for icon-only buttons.

### Input Fields
Inputs feature a 2px border that thickens to 3px Tactical Blue on focus. Use a monospaced-style font (Inter with tracking) for sensitive data entry to emphasize precision.

### Masked Data Patterns
For sensitive asset values, use a custom "security mask" pattern—a repeating diagonal hash or block pattern that obscures data until a "Reveal" (lock icon) button is triggered.

### Cards & Lists
Cards are containers with 2px black borders. List items are separated by solid 2px horizontal rules. In data tables, use alternating row tints (Platinum to a slightly darker silver) to maintain legibility without needing soft shadows.

### Security Motifs
Integrate lock icons and "Secure Connection" badges into the header of every major module. Use heavy stroke-weight icons (2px minimum) to match the UI's structural lines.