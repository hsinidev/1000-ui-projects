---
name: Modern-Traditional Law
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#544341'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#877270'
  outline-variant: '#dac1bf'
  surface-tint: '#954742'
  primary: '#2a0002'
  on-primary: '#ffffff'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#ffb3ad'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#0e0f0f'
  on-tertiary: '#ffffff'
  tertiary-container: '#242424'
  on-tertiary-container: '#8c8b8b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 32px
  margin-page: 64px
  section-padding: 128px
---

## Brand & Style

This design system is built upon the principles of **Architectural Minimalism** and **Classical Authority**. It targets a high-net-worth and corporate clientele who demand both tradition and modern efficiency. The aesthetic balances the gravity of a heritage law firm with the precision of a modern digital experience.

The style avoids ephemeral trends, opting instead for a "Digital Atelier" feel. It uses structural lines to create a sense of stability and order. The emotional response is one of absolute security, institutional wisdom, and bespoke attention to detail. Every element is intentional, reflecting the meticulous nature of legal practice.

## Colors

The palette is anchored by **Deep Burgundy**, used strategically to signify power and history. **Gold** is used sparingly as a high-contrast accent for interactive states and decorative structural borders, suggesting premium quality without ostentation. 

The background utilizes a **Marble** base, which should be implemented as a subtle, fixed-position texture with soft grey veining to provide depth without distracting from the content. Typography primarily sits on a clean off-white or the marble surface to ensure maximum legibility. Use the Tertiary Slate for secondary text and dividers where the Burgundy is too heavy.

## Typography

The typographic hierarchy establishes a dialogue between the old world and the new. **Noto Serif** (selected as the closest available serif to Playfair Display) is the voice of authority, used for all major headings and pull-quotes. It should be typeset with generous leading to allow the letterforms to breathe.

**Inter** provides a utilitarian counterpoint. It is used for all functional text, data, and long-form legal copy. For navigation and small labels, use Inter in all-caps with increased letter-spacing to mimic the look of traditional stone-carved inscriptions.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to maintain a sense of controlled, architectural structure. Content is centered within a 1200px container. The spacing rhythm is intentionally "slow," utilizing large section paddings to create a gallery-like experience where information is never crowded.

Margins and gutters are wider than standard corporate sites to signal luxury. Vertical rhythm should be strictly maintained, using multiples of 8px to ensure that despite the traditional aesthetic, the digital execution feels precise and modern.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Gold Frameworks** rather than realistic shadows. Surfaces do not "float"; they are "inset" or "layered" like high-end stationery or architectural panels.

- **Primary Surfaces:** Use the Marble texture (#F5F5F5) as the base.
- **Secondary Layers:** Use pure white (#FFFFFF) for cards or content blocks to create a subtle lift.
- **Outlines:** Use 1px Gold (#C5A059) or light grey (#E0E0E0) borders to define boundaries. 
- **Shadows:** If used, they must be extremely diffused and low-opacity (2-5%), acting more as a subtle "glow" or ambient occlusion rather than a directional light source.

## Shapes

The shape language is **Sharp and Euclidean**. In keeping with the architectural theme, rounded corners are avoided entirely. 90-degree angles communicate precision, discipline, and the "hard lines" of the law. 

Interactive elements like buttons and input fields must be perfectly rectangular. Borders should be crisp and consistently 1px or 2px—never variable in weight within the same component.

## Components

### Buttons
Primary buttons use the Deep Burgundy (#4A0E0E) background with white text. Secondary buttons use a transparent background with a 1px Gold border. All buttons are rectangular and utilize uppercase labels with 0.1em letter spacing.

### Input Fields
Inputs are defined by a bottom-border only (1px Slate) in their default state, becoming a full Gold-bordered box upon focus. This mimics the look of a signature line on a legal document.

### Cards
Cards should have no background shadow. Instead, they are defined by a 1px light grey border and a subtle change in background tone (from Marble to White). For featured content, a 2px Gold top-border may be added.

### Navigation
The navigation bar should be persistent and minimalist. Use the "Label-caps" typography style for menu items. Active states are indicated by a thin Gold underline rather than a color change.

### Legal Seals & Accents
Use Gold for decorative "frames" around key testimonials or attorney profiles. Incorporate hairline vertical rules to separate content sections, reinforcing the "grid" and architectural feel.