---
name: Sovereign Heritage
colors:
  surface: '#fcf9f2'
  surface-dim: '#dcdad3'
  surface-bright: '#fcf9f2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ec'
  surface-container: '#f1eee7'
  surface-container-high: '#ebe8e1'
  surface-container-highest: '#e5e2db'
  on-surface: '#1c1c18'
  on-surface-variant: '#44474e'
  inverse-surface: '#31312c'
  inverse-on-surface: '#f3f0e9'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#af2b3e'
  on-secondary: '#ffffff'
  secondary-container: '#fd6673'
  on-secondary-container: '#680018'
  tertiary: '#735c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#cca830'
  on-tertiary-container: '#4f3e00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#ffdada'
  secondary-fixed-dim: '#ffb3b5'
  on-secondary-fixed: '#40000b'
  on-secondary-fixed-variant: '#8e0f28'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#fcf9f2'
  on-background: '#1c1c18'
  surface-variant: '#e5e2db'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-edge: 64px
  section-gap: 120px
---

## Brand & Style

The design system is engineered to evoke the atmosphere of a private family office or a historic merchant bank. It targets high-net-worth individuals who value discretion, institutional stability, and exclusivity. The brand personality is authoritative yet quiet, prioritizing long-term trust over transient trends.

The visual style is a fusion of **Minimalism** and **Tactile Sophistication**. It utilizes expansive whitespace to denote "digital luxury," where breathing room is a commodity. High-contrast layouts create a clear hierarchy of information, while gold accents and subtle textures (reminiscent of heavy bond paper or fine grain leather) provide a sensory, premium experience that differentiates the interface from standard fintech products.

## Colors

The palette is anchored by **Deep Navy Blue**, representing institutional depth and reliability. **Rich Burgundy** is used sparingly for critical actions or to denote "Heritage" status tiers. **Metallic Gold** is strictly an accent color, reserved for thin borders, iconography, and subtle highlights to signal premium value.

The background uses a "Paper" white (#FFFFFF) contrasted with a "Vellum" neutral (#F4F1EA) for sectioning, ensuring the interface feels grounded and physical rather than clinical.

## Typography

This design system utilizes **Noto Serif** for all headlines to establish a traditional, literary authority. For body text, **Work Sans** provides a professional, grounded, and highly legible counterpoint that ensures complex financial data remains accessible.

Large display titles should use tight letter spacing and bold weights to command attention. Labels and metadata should utilize the "label-caps" style—uppercase with increased tracking—to mimic the formal engraving found on high-end stationery.

## Layout & Spacing

The layout follows a **Fixed Grid** model to maintain a sense of structured permanence. Content is centered within a generous container, flanked by significant margins that prevent the UI from feeling cluttered. 

Vertical rhythm is intentionally "loose," with large gaps between sections to allow the eye to rest. Use a 12-column grid for data layouts, but prefer single-column centered orientations for editorial or high-level account overviews. Gutters are wide (32px) to reinforce the premium, un-crowded aesthetic.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layers** and **Bold Outlines** rather than aggressive shadows. Surfaces do not "float" as much as they "rest" upon one another. 

To denote depth:
- **Base Layer:** The primary canvas (Paper White).
- **Secondary Surfaces:** Soft Vellum (#F4F1EA) inset panels for grouping content.
- **Accents:** Use 1px Metallic Gold (#D4AF37) borders for primary containers and dividers.
- **Shadows:** Use only for high-priority modals. Shadows should be ultra-diffused (32px+ blur) with a low opacity Navy tint (5-10%) to maintain a sophisticated, non-digital look.

## Shapes

The design system utilizes **Sharp** (0px) corners for all primary UI elements, including buttons, cards, and input fields. This architectural approach communicates precision, rigidity, and timelessness. Circles are permitted only for specific functional icons or user avatars to provide a singular point of organic contrast.

## Components

### Buttons & Inputs
Buttons are rectangular with 1px gold borders for secondary actions and solid Navy backgrounds for primary actions. Input fields use only a bottom-border treatment in the default state, evolving into a full gold-framed box upon focus to simulate formal fill-in-the-blank documents.

### High-Trust Elements
- **Encrypted Badges:** Small, gold-embossed icons featuring a wax-seal motif to denote secure transactions.
- **Stealth-Mode Toggle:** A custom-designed switch that "dims" sensitive financial figures into a textured blur, allowing the user to view the UI in public spaces without revealing net worth.
- **Interactive Data Visualizations:** Charts use a restricted palette of Navy and Gold. Lines should be razor-thin (1px) with subtle gradient fills beneath them.

### Cards & Lists
Lists are separated by thin, full-width gold dividers. Cards do not have shadows; they are defined by a light-grey or vellum background fill and a sharp 1px border.

### Stealth Navigation
Navigation should be minimalist, hidden behind a "Menu" label or a sophisticated thin-line icon to maximize screen real estate for the user's data.