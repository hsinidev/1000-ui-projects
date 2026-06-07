---
name: BioSquare
colors:
  surface: '#f9f9ff'
  surface-dim: '#d8dae2'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3fb'
  surface-container: '#ecedf6'
  surface-container-high: '#e7e8f0'
  surface-container-highest: '#e1e2ea'
  on-surface: '#191c21'
  on-surface-variant: '#424752'
  inverse-surface: '#2e3037'
  inverse-on-surface: '#eff0f8'
  outline: '#727783'
  outline-variant: '#c2c6d4'
  surface-tint: '#005db6'
  primary: '#00478d'
  on-primary: '#ffffff'
  primary-container: '#005eb8'
  on-primary-container: '#c8daff'
  inverse-primary: '#a9c7ff'
  secondary: '#505f76'
  on-secondary: '#ffffff'
  secondary-container: '#d0e1fb'
  on-secondary-container: '#54647a'
  tertiary: '#42484f'
  on-tertiary: '#ffffff'
  tertiary-container: '#596067'
  on-tertiary-container: '#d4dae2'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#a9c7ff'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#00468c'
  secondary-fixed: '#d3e4fe'
  secondary-fixed-dim: '#b7c8e1'
  on-secondary-fixed: '#0b1c30'
  on-secondary-fixed-variant: '#38485d'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#f9f9ff'
  on-background: '#191c21'
  surface-variant: '#e1e2ea'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  technical-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
  max-width: 1440px
---

## Brand & Style

The brand personality is authoritative, precise, and sterile—mirroring the controlled environments of the life sciences industry. It targets institutional investors, lab managers, and biotech executives who prioritize technical specifications and reliability over emotional flourish. 

The design style is a hybrid of **Minimalism** and **Corporate/Modern**, leaning heavily into a "Technical Precision" aesthetic. It utilizes ample whitespace to simulate the cleanliness of a Grade-A laboratory, while maintaining a high-density information architecture for technical data. The UI should evoke a sense of clinical accuracy, trust, and high-end exclusivity.

## Colors

The palette is anchored by **Laboratory Blue**, a high-chroma primary used to signal action and expertise. The background is a **Sterile White** (slightly cooled to avoid warmth), providing a neutral stage that emphasizes content. **Slate** serves as the primary vehicle for text and structural accents, offering a softer, more sophisticated alternative to pure black.

- **Primary (Laboratory Blue):** Used for primary buttons, active states, and critical technical callouts.
- **Secondary (Slate):** Used for sub-headers, secondary icons, and supporting UI elements.
- **Background (Sterile White):** The primary canvas, ensuring maximum legibility and a clinical feel.
- **Surface (Cool Gray):** Used for subtle sectioning and data table backgrounds to maintain hierarchy without adding visual noise.

## Typography

This design system utilizes a dual-font approach to balance technical character with utilitarian readability. 

**Space Grotesk** is used for headlines and labels. Its geometric, slightly engineered letterforms reinforce the scientific theme and provide a distinct "high-tech" voice. 

**Inter** is used for all body copy and technical specifications. It was selected for its exceptional legibility at small sizes and its neutral, systematic feel, which is essential when displaying complex lab data (e.g., HVAC air changes, floor load capacities, and ceiling heights). 

Tabular figures should be enabled for all data-heavy views to ensure vertical alignment of numerical values.

## Layout & Spacing

This design system employs a **Fixed Grid** model on desktop to maintain a controlled, gallery-like feel for property listings. The layout is built on a 12-column grid with a 1440px max-width.

Spacing follows a strict 4px base unit to ensure technical precision. Large, "sterile" gaps (using `lg` and `xl` units) are used between major sections to prevent information overload. Data density is managed through consistent `md` padding within cards and containers, ensuring that technical specs have enough "room to breathe" while remaining easily scannable.

## Elevation & Depth

To maintain a clean, "medical-grade" aesthetic, this design system avoids heavy shadows. Depth is conveyed primarily through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surface Tiers:** The background is the lowest level. Cards and containers use a pure white surface with a subtle 1px border in Slate at 10% opacity.
- **Micro-Elevation:** On hover, elements may use a highly diffused, 2% opacity shadow to suggest interactability without breaking the flat, technical plane.
- **Functional Overlays:** Modals and dropdowns use a crisp 1px border and a subtle backdrop blur to maintain the "glass" quality of lab equipment while ensuring focus.

## Shapes

The shape language is strictly **Sharp (0px roundedness)**. 

Every UI element—from primary buttons to property image containers and input fields—features hard 90-degree corners. This evokes architectural blueprints and precision instruments, differentiating the platform from consumer-grade real estate apps. Line work should be thin (1px) and consistent across all components to maintain a cohesive, technical feel.

## Components

### Buttons
Primary buttons are solid Laboratory Blue with white text, utilizing uppercase Space Grotesk for a "command" feel. Secondary buttons use a 1px Slate border with no fill. All buttons feature sharp corners and a subtle "fill-in" animation on hover.

### Input Fields & Search
Input fields use a light Slate border (20% opacity) that shifts to Laboratory Blue on focus. Labels sit strictly above the field in uppercase "label-caps" typography. Search bars for lab specs (e.g., "BSL-2", "Fume Hoods") include clear, medical-grade glyphs.

### Property Cards
Cards are the core of the experience. They feature a 1px border and no shadow. Technical specs are displayed in a structured grid within the card using the "technical-mono" type style, separated by thin vertical dividers.

### Technical Chips
Used for labeling lab types (e.g., Vivarium, Wet Lab, Clean Room). These are rectangular with a light blue tinted background and Laboratory Blue text.

### Data Tables
Tables are high-density, using alternating row tints in Cool Gray. Headers are sticky and use the primary Slate color to provide a strong structural anchor for technical data sheets.

### Medical-Grade Iconography
Icons must be "thin-line" (1px stroke), geometric, and non-rounded. They should represent complex lab equipment and real estate metrics with high-fidelity detail.