---
name: Resilio-Hub
colors:
  surface: '#fff9e8'
  surface-dim: '#e3dbb0'
  surface-bright: '#fff9e8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fdf4c8'
  surface-container: '#f7efc3'
  surface-container-high: '#f1e9be'
  surface-container-highest: '#ebe3b8'
  on-surface: '#1f1c02'
  on-surface-variant: '#42474d'
  inverse-surface: '#353113'
  inverse-on-surface: '#faf2c6'
  outline: '#72787e'
  outline-variant: '#c2c7cd'
  surface-tint: '#3d627d'
  primary: '#001a2b'
  on-primary: '#ffffff'
  primary-container: '#003049'
  on-primary-container: '#7398b6'
  inverse-primary: '#a5cbea'
  secondary: '#bb0021'
  on-secondary: '#ffffff'
  secondary-container: '#e61730'
  on-secondary-container: '#fffbff'
  tertiary: '#2b1100'
  on-tertiary: '#ffffff'
  tertiary-container: '#4a2200'
  on-tertiary-container: '#e67600'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cae6ff'
  primary-fixed-dim: '#a5cbea'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#244a64'
  secondary-fixed: '#ffdad7'
  secondary-fixed-dim: '#ffb3af'
  on-secondary-fixed: '#410005'
  on-secondary-fixed-variant: '#930018'
  tertiary-fixed: '#ffdcc6'
  tertiary-fixed-dim: '#ffb784'
  on-tertiary-fixed: '#301400'
  on-tertiary-fixed-variant: '#713700'
  background: '#fff9e8'
  on-background: '#1f1c02'
  surface-variant: '#ebe3b8'
typography:
  headline-xl:
    fontFamily: Public Sans
    fontSize: 40px
    fontWeight: '800'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 30px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-bold:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
  label-mono:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 16px
  margin-desktop: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The brand personality is forged in crisis: it is stoic, authoritative, and unshakable. This design system serves emergency responders and citizens in high-stress environments where every second counts. The emotional response must be one of absolute reliability and clarity—eliminating ambiguity through "hardened" visual structures.

The design style is a hybrid of **Brutalism** and **Institutional Modernism**. It rejects soft aesthetics and decorative flourishes in favor of heavy strokes, high-contrast boundaries, and a rigid information hierarchy. The interface prioritizes rapid scanning and tactical utility, ensuring that critical data is immediately distinguishable from background operations even in low-visibility or high-stress outdoor scenarios.

## Colors
The palette is built on high-contrast signals to ensure authoritative hierarchy. 

- **Navy (#003049):** Used for primary navigation, headers, and core structural elements. It provides the "institutional" weight and professional grounding.
- **Signal Red (#D90429):** Reserved exclusively for active emergencies, critical alerts, and life-safety information. It must be used sparingly to maintain its psychological impact.
- **White (#FFFFFF):** The primary canvas color for maximum legibility and offline readability under varied lighting conditions.
- **Support Tones:** A muted ochre/sand neutral is utilized for secondary containers to reduce eye strain without sacrificing the "hardened" aesthetic, while an amber tone is used for "Warning" states that do not reach the "Critical" threshold of Signal Red.

## Typography
The typography system utilizes **Public Sans** for headlines to leverage its institutional and government-standard clarity. **Inter** is used for all functional body text and data entry due to its superior legibility on mobile screens and high x-height.

In high-alert states, headlines should use tight letter-spacing and heavy weights to command attention. Body text maintains generous line height to ensure readability during physical movement or in "offline" field conditions. Labels use uppercase styling and increased tracking for clear identification of data fields and status types.

## Layout & Spacing
This design system utilizes a **fluid grid** optimized for mobile-first deployment. The layout relies on a strict 4px baseline grid to maintain alignment across dense data visualizations.

On mobile devices, a single-column layout is preferred for primary information feeds, using 16px side margins. On larger tablet or desktop views, a 12-column grid is implemented, but content width is capped to prevent long line lengths that hinder rapid scanning. Vertical rhythm is aggressive, using "stack" units to tightly group related information while using large gaps to separate distinct emergency events.

## Elevation & Depth
Depth is conveyed through **Bold Borders** and **Tonal Layers** rather than shadows. In an emergency context, shadows can create visual "fuzziness" that slows down cognitive processing. 

Hierarchy is established by:
1.  **Z-Index Tiering:** High-priority alerts are given a thick 3px or 4px solid black or Navy border to "lift" them from the page.
2.  **Surface Inversion:** The most critical information uses dark backgrounds (Navy or Red) with light text, while standard information uses light backgrounds with dark text.
3.  **Flat Stacking:** Elements do not float; they sit on the surface or are inset into containers, emphasizing the "hardened" and grounded nature of the tool.

## Shapes
The shape language is strictly **Sharp (0)**. Right angles are used throughout to reinforce the "hardened" and authoritative aesthetic. Rounded corners are perceived as softer and more consumer-oriented; sharp corners communicate precision, urgency, and institutional reliability. All buttons, cards, input fields, and alert banners must use 0px border-radius.

## Components

- **Buttons:** Large, high-hit-area rectangles with 2px solid borders. Primary buttons use Navy background with White text; Critical actions use Signal Red. Active states use a solid color shift with no transition delay.
- **High-Visibility Alert Headers:** Full-bleed banners at the top of the viewport. Critical alerts must pulse or use a high-contrast chevron pattern (Red/White) to indicate immediate danger.
- **Hardened Cards:** Containers for data points. They feature 2px borders and a dedicated "Header" area with a contrasting background color to categorize the data (e.g., "Location," "Resource," "Threat").
- **Status Indicators:** Square icons using a traffic-light system (Red/Amber/Green) but supplemented with heavy iconography (X, !, Check) to ensure accessibility for colorblind users in the field.
- **Data Visualizations:** High-contrast line and bar charts using the primary palette. Grid lines are prominent and labeled clearly for rapid coordinate or value extraction.
- **Input Fields:** Thick borders (2px) that darken on focus. Labels are always visible (never floating) to ensure the user never loses context during data entry in the field.
- **Offline Sync Indicator:** A persistent, high-contrast status bar showing local storage capacity and last-sync timestamp, critical for "mobile-first" reliability.