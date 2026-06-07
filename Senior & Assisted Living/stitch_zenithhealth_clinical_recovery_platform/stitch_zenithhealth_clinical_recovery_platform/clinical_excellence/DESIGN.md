---
name: Clinical Excellence
colors:
  surface: '#f4fafd'
  surface-dim: '#d4dbdd'
  surface-bright: '#f4fafd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef5f7'
  surface-container: '#e8eff1'
  surface-container-high: '#e2e9ec'
  surface-container-highest: '#dde4e6'
  on-surface: '#161d1f'
  on-surface-variant: '#3e4949'
  inverse-surface: '#2b3234'
  inverse-on-surface: '#ebf2f4'
  outline: '#6e7979'
  outline-variant: '#bdc9c8'
  surface-tint: '#006a6a'
  primary: '#006565'
  on-primary: '#ffffff'
  primary-container: '#008080'
  on-primary-container: '#e3fffe'
  inverse-primary: '#76d6d5'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#585b5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#717374'
  on-tertiary-container: '#f9fafb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#93f2f2'
  primary-fixed-dim: '#76d6d5'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f4fafd'
  on-background: '#161d1f'
  surface-variant: '#dde4e6'
typography:
  display-lg:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

This design system is built upon the dual pillars of medical precision and restorative comfort. The brand personality is authoritative yet empathetic, designed to instill immediate trust in physicians while providing a serene, legible environment for patients in recovery. 

The visual style follows a **Corporate/Modern** movement with heavy **Minimalist** influences. It prioritizes "clinical excellence" through the use of generous whitespace, high-contrast typography, and a structured grid that reflects the organized nature of a professional medical facility. To balance the sterile clinical feel, the design utilizes soft transitions and high-quality photography of natural light and human care to evoke a "comfortable" rehabilitation experience.

## Colors

The palette is strictly curated to project cleanliness and professional stability. 

*   **Primary (Teal):** Used for primary actions, branding elements, and active states. It represents healing and trust.
*   **Secondary (Silver):** Applied to borders, dividers, and disabled states. It introduces a metallic, precise quality associated with medical technology.
*   **Neutral (Pure White & Slate):** Pure White is the primary canvas color to ensure a sterile, bright environment. Slate is used for high-readability text.
*   **System Colors:** Success (Green), Warning (Amber), and Alert (Red) are used sparingly for physician-facing data alerts, maintaining high saturation against the silver and white background.

## Typography

This design system utilizes two complementary typefaces to bridge the gap between institutional authority and modern accessibility.

**Public Sans** is the primary choice for headlines and labels. Its institutional, neutral character ensures that medical information and navigation feel official and trustworthy. 

**Manrope** is used for all body text and patient-facing content. Its refined, balanced geometric shapes offer superior legibility for patients who may be experiencing visual fatigue, while maintaining a modern, calm professional tone for physician reports. 

Hierarchies are strictly enforced to allow physicians to scan data quickly. High contrast between weights (700 for headers vs 400 for body) is essential for rapid information architecture comprehension.

## Layout & Spacing

The layout utilizes a **Fixed Grid** system (12 columns) on desktop to maintain a predictable, stable environment for users. For physicians managing complex data, the system allows for high-density information layouts within a structured 8px rhythm.

For patient-facing views, the layout expands the "stack" spacing to `stack-lg` to prevent cognitive overload. All interactive elements must maintain a minimum 44px hit target, even if the visual container appears smaller, ensuring accessibility for patients with limited motor dexterity.

## Elevation & Depth

This design system avoids heavy shadows to maintain its clean, clinical aesthetic. Depth is achieved through **Tonal Layers** and **Low-Contrast Outlines**.

*   **Base Layer:** Pure White (#FFFFFF).
*   **Container Layer:** Tertiary Grey (#F8F9FA) used to group related medical data.
*   **Bordering:** 1px solid Silver (#C0C0C0) defines boundaries without adding visual clutter.
*   **Active Elevation:** Only the most critical interactive elements (like modal dialogs or primary CTA buttons) utilize a very soft, diffused ambient shadow (Opacity 5%, Blur 12px) to suggest "lift" without breaking the flat, professional aesthetic.

## Shapes

The shape language is defined as **Soft**. Standard components utilize a 0.25rem (4px) corner radius. This choice is intentional: it is soft enough to feel approachable and "comfortable" for a rehabilitation setting, yet sharp enough to retain the precision of a clinical environment. 

Large containers and cards may use `rounded-lg` (8px) to frame professional imagery, creating a window-like effect that feels modern and architectural.

## Components

### Buttons
Primary buttons are solid Teal with White text. Secondary buttons use a Silver border with Teal text. All buttons use `label-bold` typography and uppercase styling for maximum visibility.

### Cards
Medical record and patient summary cards use a Pure White background with a 1px Silver border. Headers within cards should have a subtle #F8F9FA background tint to separate metadata from the main content.

### Input Fields
Inputs must have a clearly defined Silver border at all times. The focus state transitions the border to Teal with a 2px thickness to assist physicians during rapid data entry.

### Chips & Status Indicators
Status chips (e.g., "In Recovery", "Discharged") use low-saturation background tints of the system colors with high-saturation text to ensure they are legible but not distracting from the primary clinical data.

### Progress Gauges
For rehabilitation tracking, use thin-stroke circular gauges in Teal to show patient progress. These should be accompanied by large, clear `headline-md` percentage text for easy patient viewing.

### Physician Dashboard Specifics
Data tables should utilize alternating row highlights (Zebra striping) in #F8F9FA to assist in horizontal scanning of medication lists and vitals.