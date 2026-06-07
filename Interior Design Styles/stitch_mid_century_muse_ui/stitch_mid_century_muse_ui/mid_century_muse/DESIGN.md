---
name: Mid-Century Muse
colors:
  surface: '#fff8f6'
  surface-dim: '#e0d8d6'
  surface-bright: '#fff8f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf2f0'
  surface-container: '#f4ecea'
  surface-container-high: '#efe6e4'
  surface-container-highest: '#e9e1df'
  on-surface: '#1e1b1a'
  on-surface-variant: '#504441'
  inverse-surface: '#33302e'
  inverse-on-surface: '#f7efed'
  outline: '#827470'
  outline-variant: '#d4c3be'
  surface-tint: '#77574d'
  primary: '#442a22'
  on-primary: '#ffffff'
  primary-container: '#5d4037'
  on-primary-container: '#d4ada1'
  inverse-primary: '#e7bdb1'
  secondary: '#006b5e'
  on-secondary: '#ffffff'
  secondary-container: '#94f0df'
  on-secondary-container: '#006f62'
  tertiary: '#3f2e00'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a4400'
  on-tertiary-container: '#e2ae04'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#e7bdb1'
  on-primary-fixed: '#2c160e'
  on-primary-fixed-variant: '#5d4037'
  secondary-fixed: '#97f3e2'
  secondary-fixed-dim: '#7ad7c6'
  on-secondary-fixed: '#00201b'
  on-secondary-fixed-variant: '#005047'
  tertiary-fixed: '#ffdf98'
  tertiary-fixed-dim: '#f5bf22'
  on-tertiary-fixed: '#251a00'
  on-tertiary-fixed-variant: '#5a4300'
  background: '#fff8f6'
  on-background: '#1e1b1a'
  surface-variant: '#e9e1df'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Newsreader
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 40px
  xl: 64px
  margin: 20px
  gutter: 16px
---

## Brand & Style

This design system is anchored in the "International Typographic Style" and the functionalism of the Eames era. It bridges the gap between 1950s optimism and contemporary digital utility. The brand personality is sophisticated, curated, and architecturally precise.

The design style is a hybrid of **Minimalism** and **Tactile Retro**. It utilizes high-contrast layouts, thin structural borders, and a focus on geometric purity. The interface should feel like a high-end architectural monograph—clean, intentional, and timeless. By emphasizing ample whitespace and "Eames-era" principles of form-follows-function, the UI evokes a sense of nostalgia without sacrificing modern performance.

## Colors

The color palette is derived from natural materials and mid-century pigment staples. The foundation is an off-white "Vintage Paper" background which reduces the harshness of digital screens and adds an analog warmth. 

- **Walnut (Primary):** A deep, woody brown used for structural elements and key branding moments.
- **Teal (Secondary):** A muted, sophisticated highlight used for secondary actions and subtle category differentiation.
- **Mustard (Accent):** A vibrant, period-accurate yellow reserved for primary calls-to-action and critical focal points.
- **Ink (Neutral):** A soft, off-black used for thin borders and typography to maintain a high-contrast, lithographic appearance.

## Typography

Typography in this design system follows a strict hierarchy to reflect architectural blueprints and editorial design. 

**Space Grotesk** is used for headings and labels. Its geometric, technical nature mirrors the "Futura" obsession of the mid-century period while maintaining modern readability. High-level displays should use tight tracking for a bold, graphic look.

**Newsreader** is used for all long-form body text. This serif provides a literary, sophisticated contrast to the geometric headings, ensuring that architectural descriptions and firm philosophies feel grounded and professional.

## Layout & Spacing

This design system employs a **Fluid Grid** with a mobile-first focus. Navigation is primarily icon-driven and anchored to a bottom bar or a structured geometric menu to ensure ease of use on mobile devices.

The spacing rhythm is based on a 4px baseline, but the layout philosophy prioritizes "Ample Whitespace." Sections should feel airy and uncrowded. Use 40px (lg) or 64px (xl) padding between major content blocks to create a "gallery" feel. Thin 1px black borders are used to define zones without adding visual weight, mimicking the clean lines of a Mies van der Rohe structure.

## Elevation & Depth

To remain true to the flat, graphic nature of Mid-Century print design, this system avoids ambient shadows and blurs. Depth is conveyed through **Bold Borders** and **Tonal Layers**.

- **Stacking:** Elements are layered flatly. A "raised" element is indicated by a thicker border or a shift to a contrasting background color (e.g., a Walnut block on a Cream background).
- **Hard Shadows:** If depth is absolutely required, use "hard-stop" shadows (a solid offset block of Teal or Mustard) rather than soft blurs.
- **Outlines:** Every interactive container uses a 1px or 1.5px solid Ink border to define its footprint within the grid.

## Shapes

The shape language is strictly **Sharp (0px)**. The design system rejects the "bubbliness" of modern SaaS apps in favor of the hard edges found in modular furniture and modernist architecture. 

Geometric motifs—rectangles, perfect circles for icons, and 45-degree angles—should be used as decorative accents. For example, image containers should be sharp-edged, occasionally utilizing a "cut-out" or "asymmetric" frame to reference Eames-era textile patterns.

## Components

### Buttons
Primary buttons are solid Walnut or Mustard with sharp corners and Space Grotesk Uppercase labels. Secondary buttons use a 1px Ink border with a transparent background. Interaction states are shown via a solid color fill or a slight 2px offset "ghost" border.

### Navigation
The mobile navigation is icon-driven, housed in a dedicated bottom bar. Icons must be thin-stroke, geometric line art. Labels are placed immediately below in 10px Space Grotesk.

### Cards
Cards are defined by a 1px border. They do not use shadows. The header of the card should be separated from the body by a horizontal 1px line. Walnut wood textures may be used as a background for "featured" cards to add warmth and tactile appeal.

### Inputs & Form Fields
Input fields are simple underlines or 1px boxes with no rounded corners. Labels sit above the field in uppercase Space Grotesk. Focus states are indicated by a change in border color to Teal.

### Chips & Tags
Geometric and rectangular. Use high-contrast color pairings (e.g., Teal text on a Cream background with a Teal border) to categorize architectural styles or project phases.