---
name: AgriData Precision
colors:
  surface: '#fcf9f4'
  surface-dim: '#dcdad5'
  surface-bright: '#fcf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ee'
  surface-container: '#f0ede9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e5e2dd'
  on-surface: '#1c1c19'
  on-surface-variant: '#45483c'
  inverse-surface: '#31302d'
  inverse-on-surface: '#f3f0eb'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#52652a'
  primary: '#33450d'
  on-primary: '#ffffff'
  primary-container: '#4a5d23'
  on-primary-container: '#bed58e'
  inverse-primary: '#b8cf88'
  secondary: '#9e4127'
  on-secondary: '#ffffff'
  secondary-container: '#ff8b6b'
  on-secondary-container: '#75230b'
  tertiary: '#434032'
  on-tertiary: '#ffffff'
  tertiary-container: '#5b5748'
  on-tertiary-container: '#d3ccba'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4eca2'
  primary-fixed-dim: '#b8cf88'
  on-primary-fixed: '#141f00'
  on-primary-fixed-variant: '#3b4d14'
  secondary-fixed: '#ffdbd1'
  secondary-fixed-dim: '#ffb5a1'
  on-secondary-fixed: '#3b0800'
  on-secondary-fixed-variant: '#7f2a12'
  tertiary-fixed: '#e9e2cf'
  tertiary-fixed-dim: '#ccc6b4'
  on-tertiary-fixed: '#1e1c10'
  on-tertiary-fixed-variant: '#4a4739'
  background: '#fcf9f4'
  on-background: '#1c1c19'
  surface-variant: '#e5e2dd'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Newsreader
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
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
---

## Brand & Style

This design system is built at the intersection of traditional agronomy and advanced geospatial intelligence. The brand personality is authoritative, reliable, and meticulously technical. It avoids the fluff of consumer-grade apps in favor of a "tool-first" philosophy, prioritizing high-density information display and clarity for field operators and data analysts alike.

The design style follows a **Modern/Corporate** aesthetic with **Brutalest** undertones—specifically through the use of crisp 1px borders and a strict grid. It evokes the feeling of high-end field equipment and laboratory software. The visual language balances the organic nature of agriculture with the rigid precision of data science, utilizing a "Parchment" base to reduce eye strain during long periods of monitoring.

## Colors

The color palette is derived from natural soil and vegetation states. **Moss Green** serves as the primary brand color, representing healthy crops and stability. **Terracotta** acts as the secondary action color, used for primary call-to-actions, critical alerts, and soil-related data points.

**Parchment** is the foundation of this design system, used for large-scale backgrounds to provide a tactile, paper-like quality that is softer than pure white. Neutrals are deep charcoals rather than true blacks to maintain a sophisticated, grounded appearance. For GIS mapping, the system utilizes a custom set of spectral greens and earthy browns to represent NDVI and soil moisture indices.

## Typography

Typography is used to distinguish between editorial narrative and technical data. **Newsreader** provides a sturdy, traditional serif for headlines, lending a sense of established expertise and academic rigor to report titles and section headers.

**Inter** is the workhorse of the design system, used for all UI elements, body text, and data visualizations. For technical values, telemetry, and coordinates, the system utilizes Inter’s **tabular numbers** feature to ensure vertical alignment in data tables. Heavy-weight uppercase labels are used for metadata to provide immediate scannability in dense dashboard environments.

## Layout & Spacing

This design system employs a **12-column fluid grid** for high-level dashboards, transitioning to a **fixed-width container** for specialized analytical reports. A 4px baseline grid ensures vertical rhythm, particularly important when stacking multiple rows of data sensors.

The layout philosophy emphasizes **Data Density**. Gutters are kept tight (16px) to maximize the "above the fold" real estate for GIS maps and charts. Padding within cards and modules is standardized to 16px to maintain a compact, instrument-panel feel without sacrificing legibility.

## Elevation & Depth

Hierarchy is established through **Bold Borders** and **Tonal Layers** rather than dramatic shadows. Surfaces are primarily flat, sitting directly on the Parchment background with 1px solid borders in a muted Moss Green or light grey.

Depth is used sparingly to indicate interactivity. A "Low-Contrast Outline" approach is applied to secondary containers. When shadows are used (specifically for floating GIS controls or modals), they are **Small and Crisp**, utilizing a high-offset, low-blur technique with a Moss Green tint (e.g., `rgba(74, 93, 35, 0.1)`) to maintain the grounded, technical feel.

## Shapes

The shape language is primarily **Soft (0.25rem)**. The design system avoids large radii and "pill" shapes to prevent the UI from appearing too consumer-oriented or "playful." 

Corners on data cards, buttons, and input fields use a consistent 4px radius. This provides a subtle modern touch while retaining the structural integrity of a grid-based system. GIS map markers and icons should follow a geometric, "cut-corner" or sharp-angled aesthetic to emphasize precision.

## Components

### Buttons & Inputs
Buttons utilize solid Moss Green for primary actions and Terracotta for high-priority or destructive actions. Input fields feature a 1px border that thickens on focus, with a "Parchment" fill that is 5% darker than the background to create a "well" effect.

### Chips & Data Tags
Chips are used for filtering crop types and sensor states. They use a low-saturation version of the primary colors with small-caps typography. They are rectangular with the standard 4px radius.

### Data Tables
Tables are the heart of the system. They feature subtle zebra-striping using a slightly darker parchment tint. Borders are horizontal-only to allow for vertical scanning of coordinates and yield data.

### GIS Controls
Map controls (zoom, layer toggle, legend) are housed in semi-opaque Parchment containers with crisp borders. They are positioned in the top-right of map viewports to ensure the map remains the focal point.

### Telemetry Cards
Small, information-dense cards displaying weather, moisture, and drone status. These cards use a vertical progress bar or "sparkline" to show 24-hour trends without requiring full chart modules.