---
name: Heritage-Legacy
colors:
  surface: '#fff8ef'
  surface-dim: '#e0d9cd'
  surface-bright: '#fff8ef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf3e6'
  surface-container: '#f4ede0'
  surface-container-high: '#efe7db'
  surface-container-highest: '#e9e2d5'
  on-surface: '#1e1b14'
  on-surface-variant: '#544341'
  inverse-surface: '#333028'
  inverse-on-surface: '#f7f0e3'
  outline: '#877270'
  outline-variant: '#dac1bf'
  surface-tint: '#954742'
  primary: '#2a0002'
  on-primary: '#ffffff'
  primary-container: '#4a0e0e'
  on-primary-container: '#cc726d'
  inverse-primary: '#ffb3ad'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#131003'
  on-tertiary: '#ffffff'
  tertiary-container: '#292514'
  on-tertiary-container: '#938c75'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3ad'
  on-primary-fixed: '#3d0506'
  on-primary-fixed-variant: '#77302d'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ebe2c8'
  tertiary-fixed-dim: '#cec6ad'
  on-tertiary-fixed: '#1f1c0b'
  on-tertiary-fixed-variant: '#4c4733'
  background: '#fff8ef'
  on-background: '#1e1b14'
  surface-variant: '#e9e2d5'
typography:
  headline-xl:
    fontFamily: ebGaramond
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: ebGaramond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: ebGaramond
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: newsreader
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: ebGaramond
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  stack-lg: 48px
  stack-md: 32px
  stack-sm: 16px
---

## Brand & Style

The design system is anchored in the concept of the "Living Archive." It evokes the quiet, hushed atmosphere of a private library while maintaining the accessibility of a modern digital experience. The brand personality is scholarly, authoritative, and deeply respectful of historical provenance. 

The visual style utilizes a **Tactile / Skeuomorphic** approach refined for the digital age. It avoids the clutter of literalism, instead using physical metaphors—such as the weight of heavy paper, the glint of gold leaf, and the depth of layered parchment—to establish trust. This design system prioritizes storytelling through immersive, editorial layouts that treat every rare manuscript and map as a singular masterpiece.

## Colors

The palette is derived from classical bookbinding and archival materials. **Deep Burgundy** serves as the primary accent, used for high-impact branding and calls to action, evoking the richness of leather bindings. **Gold** is reserved for delicate highlights, borders, and decorative elements, mimicking gold-leaf foiling found in illuminations. 

**Parchment** acts as the primary canvas, providing a warm, non-white background that reduces eye strain and reinforces the historical theme. Text is rendered in a deep, ink-like neutral to ensure high legibility against the textured backgrounds.

## Typography

This design system employs a dual-serif pairing to establish an academic and literary tone. **EB Garamond** is used for headlines and decorative labels; its classical proportions and graceful serifs suggest timeless quality. For body copy, **Newsreader** provides a sturdy, legible structure optimized for long-form storytelling and scholarly descriptions.

A "Label Caps" style is utilized for metadata and secondary navigation, using small caps and increased tracking to provide a refined, etched appearance. Line heights are purposefully generous to mimic the typesetting of high-end art books.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** for desktop and a **Fluid storytelling** model for mobile. It prioritizes white space—or rather, "parchment space"—to allow the high-resolution archival photography to breathe. Elements are organized in a 12-column grid on large screens, often using asymmetric offsets to create a curated, editorial feel.

Mobile-first layouts focus on a single-column narrative flow, where spacing increments are used to group related historical data. Margins are intentionally wide to mirror the "gutters" of a printed book, framing the content and focusing the user's attention on the central narrative.

## Elevation & Depth

Hierarchy in the design system is achieved through **Tonal Layers** and **Ambient Shadows**. The background layer is the base Parchment texture. Interactive elements, such as "Manuscript Cards," utilize a subtle, diffused drop shadow (low opacity, wide blur) to appear slightly lifted, as if resting on a physical desk.

Depth is further enhanced through the use of delicate **Gold foil-like dividers**. These are 1px lines that use a subtle linear gradient to simulate the way light catches metallic ink. Overlays and modals utilize a soft backdrop blur to maintain the warmth of the background while focusing on the foreground detail.

## Shapes

The shape language is primarily **Soft** and organic. While sharp corners are too aggressive for the "Heritage-Legacy" theme, perfectly circular corners feel too contemporary. A subtle 4px radius (`roundedness: 1`) is applied to cards and image containers to mimic the natural wear of aged paper and vellum.

Buttons and interactive containers follow this same subtle rounding, ensuring they feel substantial and hand-crafted rather than machine-cut. Borders are kept thin (1px) and are often rendered in Gold or a slightly darker shade of Parchment to maintain a delicate aesthetic.

## Components

### Buttons
Primary buttons are solid Deep Burgundy with white or Gold text. They feature a 1px Gold inner border to suggest a leather-bound book cover. Hover states should include a slight darkening of the burgundy and a subtle increase in shadow depth.

### Cards & Paper Elements
Cards represent individual artifacts. They use a slightly lighter Parchment shade than the background, a 1px border in a "dusty" neutral, and a soft shadow. Archival photography within cards should always be full-bleed or framed with a wide internal margin.

### Dividers & Ornaments
Dividers are not mere gray lines; they are horizontal Gold foil accents. In some instances, a small decorative glyph (such as a stylized fleur-de-lis or compass rose) may sit in the center of the divider to break up long sections of text.

### Inputs & Forms
Input fields are "inscribed" into the page, using a subtle inner shadow to look recessed. The focus state replaces the inner shadow with a 1px Gold border, signaling a refined point of interaction.

### Storytelling Immersive Overlays
For map viewing, a full-screen immersive mode is used. This component features minimal UI controls in Gold and Burgundy, floating over the artifact, allowing the user to zoom into high-resolution details without the distraction of standard navigation.