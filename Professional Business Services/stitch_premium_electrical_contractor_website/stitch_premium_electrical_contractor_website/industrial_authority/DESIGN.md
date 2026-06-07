---
name: Industrial Authority
colors:
  surface: '#001429'
  surface-dim: '#001429'
  surface-bright: '#273a51'
  surface-container-lowest: '#000f20'
  surface-container-low: '#061d32'
  surface-container: '#0b2136'
  surface-container-high: '#172b41'
  surface-container-highest: '#22364c'
  on-surface: '#d1e4ff'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#d1e4ff'
  inverse-on-surface: '#1e3248'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#fff9ef'
  on-secondary: '#3a3000'
  secondary-container: '#ffdb3c'
  on-secondary-container: '#725f00'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#1d1f1f'
  on-tertiary-container: '#858687'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffe16d'
  secondary-fixed-dim: '#e9c400'
  on-secondary-fixed: '#221b00'
  on-secondary-fixed-variant: '#544600'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#001429'
  on-background: '#d1e4ff'
  surface-variant: '#22364c'
typography:
  h1:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  button:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  label:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built upon the principles of structural integrity, precision, and unwavering safety. It targets high-value commercial and industrial clients who prioritize reliability and technical expertise above all else. The visual language conveys an "Expert-on-Site" persona—authoritative, serious, and meticulously organized.

The aesthetic direction is **Corporate / Modern** with a focus on high-contrast functionality. It utilizes a disciplined application of "Industrial Yellow" to mimic safety signage and high-visibility equipment, ensuring that critical information and calls-to-action are impossible to miss. The design avoids unnecessary flourishes, favoring clean lines and a structured layout that reflects the geometric order of electrical engineering and architectural blueprints.

## Colors

The palette is anchored by **Deep Navy Blue**, used for primary surfaces to establish a sense of depth, permanence, and professional calm. **Industrial Yellow** serves as the high-visibility tactical layer, reserved strictly for interactive elements, warnings, and essential highlights. 

**White** is utilized for primary typography and icons on dark backgrounds to ensure AAA accessibility. A secondary neutral navy-gray is employed for nested containers and subtle UI borders to maintain hierarchy without breaking the sophisticated dark-mode aesthetic.

## Typography

This design system utilizes **Public Sans** for its institutional clarity and neutral, technical appearance. The typographic hierarchy is characterized by heavy weights (Bold and ExtraBold) for headings to project authority and confidence. 

To ensure maximum legibility in high-stress or low-light environments (common in field work), body text maintains a generous line height. Functional labels and button text use increased letter spacing and uppercase styling to mimic industrial tagging and labeling systems.

## Layout & Spacing

The design system employs a **fixed grid** model to communicate stability and rigor. A 12-column grid is standard for desktop views, transitioning to a simplified 4-column grid for mobile devices. 

The spacing rhythm is based on an **8px linear scale**, ensuring all elements align to a predictable technical grid. Generous margins and "safe zones" are used around high-priority content to prevent visual clutter and maintain a premium, organized feel.

## Elevation & Depth

To maintain a professional and "Safety-First" tone, the design system avoids excessive shadows or "floaty" elements. Instead, it utilizes **tonal layers and low-contrast outlines**. 

Depth is achieved by stacking Navy shades: the primary background is the darkest, while interactive cards and modals sit on a slightly lighter navy surface. Borders are crisp and used specifically to define structural boundaries. When elevation is necessary (e.g., a high-priority modal), a tight, high-opacity shadow is used to make the element feel like a solid physical panel rather than a soft cloud.

## Shapes

The shape language is dominated by **clean lines and subtle geometry**. A "Soft" roundedness (4px) is applied to buttons and containers to modernize the aesthetic without losing the precision of a professional contractor's toolset. This slight radius prevents the UI from feeling aggressive or "sharp," while remaining far from the "friendly" playfulness of pill-shaped designs.

## Components

### Buttons
Primary buttons are solid **Industrial Yellow** with **Deep Navy Blue** text. This combination provides the highest possible contrast for action items. Secondary buttons use a Navy background with a 1px White or Yellow border.

### Cards
Cards are designed as "Service Panels." They feature a slightly lighter navy background than the main canvas and a subtle top-border in Yellow to indicate active status or priority.

### Inputs & Form Fields
Input fields use a dark background with a white border. Upon focus, the border transitions to Industrial Yellow, and a subtle "warning" glow may be applied if a field is required or contains an error, reinforcing the safety-first mindset.

### Icons
Icons must be **stroke-based and functional**. Avoid illustrative or "cute" icons; instead, use glyphs that resemble technical schematics or industry-standard safety symbols.

### Status Indicators
Status chips use a "Caution Tape" inspired design—highly legible text paired with a small, solid square indicator (Green for 'Live/Safe', Red for 'Danger/Fault', Yellow for 'Warning/Maintenance').