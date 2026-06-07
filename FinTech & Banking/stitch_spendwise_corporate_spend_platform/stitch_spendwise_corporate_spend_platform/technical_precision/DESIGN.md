---
name: Technical Precision
colors:
  surface: '#f5faf8'
  surface-dim: '#d6dbd9'
  surface-bright: '#f5faf8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f5f2'
  surface-container: '#eaefed'
  surface-container-high: '#e4e9e7'
  surface-container-highest: '#dee4e1'
  on-surface: '#171d1c'
  on-surface-variant: '#3d4947'
  inverse-surface: '#2c3130'
  inverse-on-surface: '#edf2f0'
  outline: '#6d7a77'
  outline-variant: '#bcc9c6'
  surface-tint: '#006a61'
  primary: '#00685f'
  on-primary: '#ffffff'
  primary-container: '#008378'
  on-primary-container: '#f4fffc'
  inverse-primary: '#6bd8cb'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#924628'
  on-tertiary: '#ffffff'
  tertiary-container: '#b05e3d'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#89f5e7'
  primary-fixed-dim: '#6bd8cb'
  on-primary-fixed: '#00201d'
  on-primary-fixed-variant: '#005049'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#ffdbce'
  tertiary-fixed-dim: '#ffb59a'
  on-tertiary-fixed: '#370e00'
  on-tertiary-fixed-variant: '#773215'
  background: '#f5faf8'
  on-background: '#171d1c'
  surface-variant: '#dee4e1'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.02em
  display-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h1:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-base:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  tabular-nums:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  grid_columns: '12'
  gutter: 1rem
  margin: 2rem
  container_max_width: 1440px
  base_unit: 4px
---

## Brand & Style

This design system is engineered for corporate financial operations, prioritizing efficiency, clarity, and data density. The brand personality is institutional yet technologically advanced—evoking the reliability of a traditional bank with the agility of a modern fintech platform. 

The visual style follows a **Modern Corporate** aesthetic with a heavy emphasis on **Modular Minimalism**. It utilizes a "Bento Box" structure to organize complex financial data into digestible, high-density modules. The UI avoids unnecessary decorative elements, ensuring that every pixel serves a functional purpose in the spend-management workflow.

## Colors

The palette is anchored by **Teal** as the primary action color, chosen for its association with precision and growth. **Slate** serves as the secondary color, providing a sophisticated range of grays for text, borders, and icon states to maintain high legibility without the harshness of pure black.

- **Primary (Teal):** Used for primary buttons, active states, and key data highlights.
- **Secondary (Slate):** Utilized for body text, metadata, and UI borders.
- **Background (Pure White):** Provides a sterile, professional canvas that maximizes contrast.
- **Semantic Colors:** Precise shades of emerald, rose, and amber are reserved strictly for financial status indicators (Approved, Declined, Flagged).

## Typography

The design system utilizes **Inter** exclusively to leverage its exceptional readability at small sizes and its neutral, systematic character. 

A tight typographic scale is employed to facilitate high information density. For financial tables and balance displays, `font-variant-numeric: tabular-nums` must be used to ensure columns of figures align perfectly, allowing for quick scanning of transaction data. Labels for metadata and table headers use uppercase styling with increased letter spacing to differentiate them from interactive content.

## Layout & Spacing

The layout is governed by a **12-column fluid grid** designed for a modular "Bento" experience. Content is organized into distinct containers (cards) that occupy specific column spans (e.g., 3-column widgets for KPIs, 9-column modules for transaction ledgers).

The spacing rhythm is based on a **4px baseline grid**. Standard padding within modules is set to 16px (4 units) to maintain density while preventing visual clutter. Dashboards should maintain a consistent 24px gutter between bento modules to ensure clear separation of different data streams.

## Elevation & Depth

This design system uses **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows to define hierarchy. Depth is created through subtle surface differentiation:

- **Level 0 (Background):** Pure White (#FFFFFF).
- **Level 1 (Bento Modules):** White background with a 1px border in Slate-200 and a very soft, diffused shadow (0px 2px 4px rgba(15, 23, 42, 0.05)).
- **Level 2 (Overlays/Dropdowns):** White background with a more pronounced shadow (0px 10px 15px rgba(15, 23, 42, 0.1)) to indicate temporary elevation over the grid.

Hover states on interactive modules should trigger a slight border color shift to Teal, rather than an increase in shadow depth, to maintain the technical, flat aesthetic.

## Shapes

The shape language is **Soft** and disciplined. A standard radius of 4px (`0.25rem`) is applied to buttons, input fields, and small UI components. Larger containers and bento-box modules use 8px (`0.5rem`) to soften the overall technical look and provide a modern feel. 

Pill shapes are used exclusively for status "chips" or tags to differentiate them from actionable buttons and structural containers.

## Components

- **Buttons:** Primary buttons are solid Teal with white text. Secondary buttons use a Slate-100 ghost style with Slate-700 text. Use compact heights (32px or 36px) to fit the high-density requirement.
- **Bento Cards:** The core organizational unit. Every card must have a consistent header with a `label-caps` title and an optional action icon (e.g., "Export" or "Expand").
- **Data Tables:** High-density rows with 8px vertical padding. Use Slate-50 alternating row zebra-striping for readability in large datasets. 
- **Input Fields:** Minimalist design with 1px Slate-200 borders. Focus states transition the border to Teal-600 with a 2px outer glow in Teal-100.
- **KPI Chips:** Small, condensed indicators used within cards to show percentage changes (Up/Down) using semantic colors.
- **Progress Bars:** Thin, 4px height bars used within list items to show budget depletion.
- **Breadcrumbs:** Small-scale navigation located above the page title to provide context within deep corporate hierarchies.