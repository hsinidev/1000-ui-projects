---
name: Industrial Efficiency
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#5a4136'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#8e7164'
  outline-variant: '#e3bfb1'
  surface-tint: '#a33e00'
  primary: '#a33e00'
  on-primary: '#ffffff'
  primary-container: '#ff6600'
  on-primary-container: '#561d00'
  inverse-primary: '#ffb596'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#969797'
  on-tertiary-container: '#2e3030'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb596'
  on-primary-fixed: '#360f00'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h1:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h2:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-tabular:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  status-badge:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  sidebar-width: 320px
  gutter: 12px
  margin-page: 24px
  density-compact: 4px
  density-comfortable: 12px
---

## Brand & Style

The design system is built upon the principles of industrial reliability and high-velocity utility. It is designed for operators who require split-second decision-making capabilities in high-pressure logistics environments. The aesthetic is unapologetically functional, prioritizing data density and legibility over decorative elements.

The style is a hybrid of **Minimalism** and **High-Contrast Utility**. By stripping away unnecessary ornamentation and utilizing a strict visual hierarchy, this design system ensures that critical information—such as shipment delays or stock shortages—is immediately surfaced. The emotional response is one of "calm control" amidst complex workflows, evoking the feeling of a well-oiled mechanical system.

## Colors

The color palette utilizes high-visibility signals against a neutral, industrial backdrop. **Safety Orange** is reserved exclusively for primary actions, critical alerts, and active states, ensuring these elements "pop" against the UI. **Charcoal** provides deep structural contrast, used primarily for headers, navigation, and primary text to anchor the interface.

**Light Grey** serves as the foundational surface color, reducing eye strain during long shifts by providing a softer contrast than pure white. Status colors (Success, Warning, Error) are calibrated for high accessibility, ensuring they remain distinguishable even in data-dense grids.

## Typography

The design system employs **Inter** for its exceptional legibility and systematic character. The typography strategy focuses on "scanning" rather than "reading." 

Data-dense views utilize a specialized `data-tabular` style that leverages tabular numerals to ensure columns of figures align perfectly for quick comparison. Headlines are kept compact with tight letter-spacing to save vertical space. Uppercase labels are used sparingly for metadata categories to create a clear distinction between labels and user data.

## Layout & Spacing

This design system uses a **Fluid Grid** model for the primary content area, allowing data tables to expand across ultra-wide monitors common in logistics hubs. A **Fixed Sidebar** pattern is used for the 'Quick-Action' panel, ensuring that essential tools are always pinned to the right side of the viewport.

The spacing rhythm is based on a strict 4px baseline grid. Padding in data tables is minimized (Compact Density) to maximize the "above the fold" information, while page margins are kept generous to prevent the interface from feeling cluttered. Gutters between columns are set to 12px to maintain clear separation of data points without wasting screen real estate.

## Elevation & Depth

Visual hierarchy is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than soft shadows. This reinforces the industrial, flat aesthetic. 

- **Level 0 (Background):** Light Grey (#F5F5F5) surface.
- **Level 1 (Cards/Containers):** Pure White (#FFFFFF) surfaces with a 1px solid border (#E0E0E0).
- **Level 2 (Headers/Navigation):** Charcoal (#333333) with high-contrast white text.
- **Level 3 (Interaction):** Subtle 2px "Machined" borders for focused elements.

Shadows are used only for temporary overlays like tooltips or dropdown menus, where they are rendered as sharp, high-opacity "Block Shadows" to maintain the robust visual language.

## Shapes

The shape language is characterized by **Soft** (4px) corner radii. This subtle rounding provides a "machined" feel—precise and modern—while avoiding the aggressive sharpness of a 0px radius. 

The consistency of this 4px radius across buttons, input fields, and cards creates a cohesive, structural rhythm. Progress bars and status badges follow this same rule; the design system intentionally avoids pill-shaped or fully rounded elements to maintain its utility-focused, architectural integrity.

## Components

### Data Tables
Tables are the core of the interface. They must feature fixed headers, zebra-striping for row tracking, and a hover-state that highlights the entire row in a very subtle tint of orange (#FFF0E6). Cells containing status markers should use high-contrast badges.

### Status Badges
Badges use solid, saturated background colors with white text for maximum visibility. 
- **Shipped:** Green background.
- **Pending:** Charcoal background.
- **Late:** Safety Orange background.

### Quick-Action Sidebar
A persistent vertical container on the right. It features large, icon-plus-label buttons for high-frequency tasks like "Add Stock" or "Print Label." It uses a slightly darker grey surface to distinguish it from the main workspace.

### Buttons
Primary buttons are solid Safety Orange with white text. Secondary buttons are outlined Charcoal. All buttons use the `label-caps` typography style to emphasize their role as triggers for action.

### Input Fields
Inputs use a white background with a 1px Charcoal border. When focused, the border weight increases to 2px in Safety Orange, providing an unmistakable "Active" signal to the operator.