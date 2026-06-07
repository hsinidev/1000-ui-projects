---
name: RecoveryPath
colors:
  surface: '#f9faf6'
  surface-dim: '#d9dad7'
  surface-bright: '#f9faf6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f0'
  surface-container: '#edeeea'
  surface-container-high: '#e7e9e5'
  surface-container-highest: '#e2e3df'
  on-surface: '#1a1c1a'
  on-surface-variant: '#43474a'
  inverse-surface: '#2e312f'
  inverse-on-surface: '#f0f1ed'
  outline: '#73787b'
  outline-variant: '#c3c7ca'
  surface-tint: '#516169'
  primary: '#192830'
  on-primary: '#ffffff'
  primary-container: '#2f3e46'
  on-primary-container: '#99a9b2'
  inverse-primary: '#b9c9d3'
  secondary: '#3f665c'
  on-secondary: '#ffffff'
  secondary-container: '#bee8dc'
  on-secondary-container: '#436a60'
  tertiary: '#3d1e0b'
  on-tertiary: '#ffffff'
  tertiary-container: '#57331f'
  on-tertiary-container: '#ce9b80'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e5ef'
  primary-fixed-dim: '#b9c9d3'
  on-primary-fixed: '#0e1d25'
  on-primary-fixed-variant: '#3a4951'
  secondary-fixed: '#c1ebdf'
  secondary-fixed-dim: '#a6cfc3'
  on-secondary-fixed: '#00201a'
  on-secondary-fixed-variant: '#274e45'
  tertiary-fixed: '#ffdbc9'
  tertiary-fixed-dim: '#f1bb9e'
  on-tertiary-fixed: '#301403'
  on-tertiary-fixed-variant: '#633e28'
  background: '#f9faf6'
  on-background: '#1a1c1a'
  surface-variant: '#e2e3df'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Public Sans
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style
The design system is anchored in the concept of "The Solid Foundation." It serves a user base seeking stability, safety, and a clear path forward during a vulnerable time. The aesthetic leans into a refined **Corporate/Modern** style filtered through an organic, earthy lens. 

This is not a cold, clinical interface; it is a warm, professional environment that prioritizes psychological safety. Every element is designed to reduce cognitive load and provide a sense of predictable reliability. The visual language balances the authority of a medical institution with the restorative calm of a natural retreat. High whitespace, intentional alignment, and a lack of aggressive motion create a sanctuary-like digital experience.

## Colors
The palette uses "Safety-First" color psychology. **Deep Slate** is the primary anchor, used for headers, primary actions, and navigation to provide an immediate sense of grounded stability. **Forest Green** serves as the secondary accent, representing growth and the clinical aspect of healing. **Soft Clay** is reserved for human-centric highlights and supportive callouts, introducing warmth and empathy.

The background uses a **Clean Off-White** rather than a stark pure white to reduce eye strain and provide a softer, more "paper-like" tactile quality. Contrast ratios must exceed WCAG AA standards at all times to ensure accessibility for users who may be experiencing sensory sensitivity.

## Typography
This design system employs a high-contrast typographic pairing to establish authority and clarity. **Newsreader** is used for headlines to provide a literary, intellectual, and traditional feel that signals professional expertise.

**Public Sans** is utilized for all body copy and UI elements. Chosen for its institutional heritage and neutral clarity, it ensures that critical health information is processed without distraction. Line heights are intentionally generous (1.6x) to facilitate reading for users under stress. Letter spacing is slightly tightened for large headlines and opened up for small labels to maintain maximum legibility across all scales.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy on desktop to create a "contained" and secure feeling, preventing content from becoming over-extended and overwhelming. A 12-column grid is used with substantial gutters to allow the content to breathe.

The spacing rhythm is strictly 8px-based. Vertical rhythm is emphasized to guide the user down the page in a linear, logical progression. Sections are separated by large 'XL' spacers to prevent information density from causing anxiety. Grouped elements (like form fields or list items) use 'SM' or 'MD' spacing to maintain a clear relationship between labels and data.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines** rather than aggressive shadows. This keeps the UI feeling "flat to the earth" and stable.

1.  **Surface:** The base layer is the Off-White background.
2.  **Container:** Secondary surfaces (like cards) use a slightly lighter white or a very pale Slate tint with a 1px border in a muted Slate-Grey.
3.  **Interactive:** Hover states may use an extremely soft, diffused shadow (12% opacity, 16px blur) to suggest "lifting" a physical object, but the primary indicator of depth should be color shifts or subtle border-weight changes.

## Shapes
The shape language is **Soft**. Sharp 0px corners are avoided as they feel too aggressive or clinical, while fully rounded pill shapes are avoided to maintain a sense of formal structure.

A 4px (0.25rem) base radius is applied to standard components like inputs and buttons. Larger containers like cards use an 8px (0.5rem) radius. This subtle rounding mimics the "human touch" of smoothed stone or clay, reinforcing the nature-inspired healing narrative without sacrificing professional rigor.

## Components
-   **Buttons:** Primary buttons use the Deep Slate background with Off-White text. Secondary buttons use a Forest Green outline. Buttons have a minimum height of 48px to ensure a large, confident hit area.
-   **Cards:** Cards are the primary vessel for information. They feature a 1px solid border in a muted clay or slate, with no heavy drop shadows. They should feel like "sheets" of organized information.
-   **Input Fields:** Use a solid 1px border. On focus, the border thickens and changes to Forest Green, providing a clear "active" state that guides the user's attention.
-   **Chips/Tags:** Used for categorization (e.g., "Inpatient," "Support Group"). These use the Soft Clay color at a low opacity with dark clay text to differentiate from actionable buttons.
-   **Progress Indicators:** Crucial for recovery journeys. These should be thick, horizontal bars using Forest Green to represent growth, always accompanied by clear percentage or "step" text in Public Sans.
-   **Alerts/Safety Banners:** Use the status colors (Success Green/Error Red) but with muted, desaturated backgrounds to ensure they inform the user without causing alarm or panic.