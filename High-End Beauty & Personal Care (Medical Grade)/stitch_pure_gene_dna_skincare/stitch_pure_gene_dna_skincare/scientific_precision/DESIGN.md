---
name: Scientific Precision
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#46464e'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#77767f'
  outline-variant: '#c7c5cf'
  surface-tint: '#555b88'
  primary: '#00000b'
  on-primary: '#ffffff'
  primary-container: '#121841'
  on-primary-container: '#7c81b0'
  inverse-primary: '#bec3f6'
  secondary: '#006c52'
  on-secondary: '#ffffff'
  secondary-container: '#8ff6d0'
  on-secondary-container: '#007257'
  tertiary: '#000001'
  on-tertiary: '#ffffff'
  tertiary-container: '#181c22'
  on-tertiary-container: '#80848b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dfe0ff'
  primary-fixed-dim: '#bec3f6'
  on-primary-fixed: '#111740'
  on-primary-fixed-variant: '#3e446e'
  secondary-fixed: '#8ff6d0'
  secondary-fixed-dim: '#73d9b5'
  on-secondary-fixed: '#002117'
  on-secondary-fixed-variant: '#00513d'
  tertiary-fixed: '#dfe2ea'
  tertiary-fixed-dim: '#c3c6ce'
  on-tertiary-fixed: '#181c21'
  on-tertiary-fixed-variant: '#43474d'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  title-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built on the intersection of biological science and premium personal care. The brand personality is authoritative, precise, and transparent, aimed at users who value data-driven results over marketing claims. 

The visual style follows a **Modern Clinical** aesthetic. It utilizes heavy whitespace to evoke a sterile, laboratory-grade environment, while incorporating DNA-inspired motifs to reinforce the personalized nature of the product. High-contrast elements ensure that complex genomic data remains accessible and legible. The overall emotional response should be one of profound trust and technological sophistication.

## Colors

The palette is anchored by **Deep Indigo**, used for primary actions and typography to establish scientific authority. **Mint** serves as the functional secondary color, used for success states, progress indicators, and skincare-specific highlights to provide a fresh, clinical contrast.

**Neutrals** are curated with cool, indigo-tinted undertones rather than pure grays to maintain a cohesive brand temperature. Background surfaces use a combination of pure white and subtle indigo washes to separate data modules without relying on heavy borders. High-contrast ratios are strictly maintained for all informative text against background surfaces.

## Typography

The design system utilizes **Inter** exclusively to ensure maximum readability for complex scientific summaries and lab results. The type scale is optimized for data-heavy environments, favoring slightly tighter letter spacing for headlines to maintain a modern look, while using generous line heights for body copy to ensure clarity.

A specialized "data-tabular" style is used for numerical genetic values, and an "uppercase label" style is reserved for categorical headers and status tags. Typography is primarily rendered in Deep Indigo to maintain high contrast and a professional tone.

## Layout & Spacing

The layout philosophy employs a **Fixed Grid** system for dashboard environments and a structured 12-column fluid grid for content-rich pages. A rigorous 4px baseline grid ensures vertical rhythm across data tables and forms.

Spacing is used to group related genomic markers and separate clinical findings from lifestyle recommendations. Large margins (xl) are used at the edges of the viewport to create a "contained" and premium feel, while gutters are kept consistent at 24px to allow for high information density without visual clutter.

## Elevation & Depth

This design system minimizes the use of traditional shadows to maintain a clean, clinical aesthetic. Depth is instead communicated through **Tonal Layers** and **Low-Contrast Outlines**. 

Surfaces are tiered using Indigo-tinted grays. Level 0 is the primary white background; Level 1 is a subtle cool-gray surface for data cards; Level 2 is reserved for interactive elements. When depth is absolutely necessary (e.g., in modals), a very soft, highly diffused Indigo-tinted shadow is used (0px 4px 20px rgba(18, 24, 65, 0.08)). A subtle 1px border in a light indigo-gray is the primary method for defining element boundaries.

## Shapes

The shape language reflects scientific precision. Elements use a "Soft" rounding strategy with a base radius of **4px**. This subtle rounding prevents the UI from feeling overly aggressive or industrial while maintaining the sharp, clean lines expected of a clinical brand.

Double-helix patterns are used as subtle background watermarks, never interfering with content. These motifs should be rendered in a very low-opacity indigo tint (2-3%) to provide texture to large empty surfaces without distracting from the data.

## Components

### Buttons
Primary buttons are solid Deep Indigo with white text, featuring sharp 4px corners. Secondary buttons use a Mint background with Deep Indigo text for high-visibility skincare actions.

### Progress Trackers (Lab Status)
Lab status is visualized through a linear "sequencing" tracker. Completed steps are indicated in Mint, current steps are Deep Indigo with a pulsing micro-animation, and pending steps are light gray.

### Subscription Management Cards
Cards feature a high-contrast header section in Tertiary Indigo. They must clearly display "Next Shipment" dates and "Genetic Formula" IDs using the data-tabular typography style.

### Interactive Data Charts
Charts should use Mint for positive genetic correlations and Soft Gray for baseline data. The use of the primary Deep Indigo is reserved for the user’s specific data points. All charts must include clear hover-states with high-contrast tooltips.

### Input Fields
Fields utilize a 1px Indigo-gray border that thickens to 2px Indigo on focus. Error states use a high-contrast coral (used sparingly) to ensure clinical accuracy is maintained.