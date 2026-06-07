---
name: Pro Tennis Tournament System
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#c4c9ac'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#8e9379'
  outline-variant: '#444933'
  surface-tint: '#acd600'
  primary: '#ffffff'
  on-primary: '#293500'
  primary-container: '#c5f400'
  on-primary-container: '#566c00'
  inverse-primary: '#516600'
  secondary: '#bfc2ff'
  on-secondary: '#181d8c'
  secondary-container: '#3239a3'
  on-secondary-container: '#a9afff'
  tertiary: '#ffffff'
  on-tertiary: '#24296b'
  tertiary-container: '#e0e0ff'
  on-tertiary-container: '#595ea3'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c5f400'
  primary-fixed-dim: '#acd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#00006e'
  on-secondary-fixed-variant: '#3239a3'
  tertiary-fixed: '#e0e0ff'
  tertiary-fixed-dim: '#bfc2ff'
  on-tertiary-fixed: '#0d1056'
  on-tertiary-fixed-variant: '#3b4083'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
typography:
  display-xl:
    fontFamily: Lexend
    fontSize: 72px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Lexend
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
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
  label-caps:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  stats-number:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.0'
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
  lg: 48px
  xl: 80px
  gutter: 20px
  margin: 32px
---

## Brand & Style

This design system is engineered to capture the velocity and precision of professional tennis. The brand personality is high-intensity and authoritative, designed to evoke the feeling of being courtside at a major open. The target audience includes passionate fans, athletes, and analysts who require split-second information updates and high-readability match data.

The chosen style is **High-Contrast / Bold**, utilizing a dark-mode core to make action-oriented elements pop with kinetic energy. Every visual choice is driven by the concept of "The Line"—referencing the technical boundaries of the court. The UI is unapologetically athletic, modern, and precise, avoiding soft fluff in favor of sharp, functional aesthetics.

## Colors

The palette is defined by a high-tension contrast between the synthetic and the traditional. **Electric Lime (#CEFF00)** is the primary driver of action, used exclusively for interactive states, live indicators, and highlight data. **Navy Blue (#000080)** serves as the structural foundation, providing a sophisticated and deep backdrop that minimizes eye strain during long-duration viewing of tournament brackets or live scores.

Supporting neutrals include a crisp off-white for primary text and a deeper navy-black for container nesting. Accents for match statistics (such as fault indicators or heatmaps) should use the primary lime against tonal variations of the navy background to maintain a "radar" or "broadcast" aesthetic.

## Typography

This design system employs a dual-font strategy to balance athletic aggression with technical clarity. **Lexend** is used for headlines, labels, and match scores; its geometric, wide character set evokes the speed and readability of stadium signage. 

**Inter** is utilized for body copy and dense data grids to ensure maximum legibility and a systematic, utilitarian feel. Headline styles should be tightly tracked to increase visual impact, while small labels should use uppercase styling with generous letter spacing to signify categorical importance.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop experiences—mimicking the structured dimensions of a tennis court—and transitions to a structured fluid model for mobile. A 12-column grid is standard, with components snapping to specific column spans to maintain a sense of mathematical precision.

Spacing is governed by a 4px baseline grid. Margins and paddings are generous around hero content to create focal points, but tighten significantly within match statistic cards to allow for rapid comparison of data. Geometric patterns of 1px lines (inspired by court markings) should be used as dividers instead of standard borders.

## Elevation & Depth

Hierarchy in this design system is achieved through **Tonal Layers** and **High-Contrast Outlines** rather than traditional shadows. Surfaces are stacked using varying depths of Navy Blue. 

To create depth:
1.  **Level 0 (Background):** Pure Navy Blue (#000080).
2.  **Level 1 (Cards):** Tertiary Navy (#00004D) or 5% opacity white overlays.
3.  **Interactive:** 1px solid Electric Lime borders for focus states or active selections.

Avoid soft shadows. If a shadow is necessary for legibility over imagery, use a sharp, high-opacity "hard shadow" offset by 4px to maintain the brutalist, high-energy aesthetic.

## Shapes

The shape language of this design system is **Soft (0.25rem)**, leaning towards sharp. This reflects the "precision" aspect of the tournament—where corners are clearly defined but not aggressive. 

Buttons and primary action containers use the standard `rounded-sm` (4px), while larger containers like scorecards or video players may use `rounded-lg` (8px) to provide a subtle modern touch. Interactive elements like "Live" badges or player tags may use a pill-shape to distinguish them from structural UI elements.

## Components

### Buttons
Primary buttons are solid Electric Lime with Navy text, using a bold weight. Hover states should invert or use a 1px border. Secondary buttons use a Navy background with a 1px White or Lime border.

### Scoreboards & Match Cards
These are the core of the system. They feature high-contrast data rows, using Inter for player names and Lexend for the numerical scores. Use 1px vertical dividers to separate sets.

### Chips & Status Indicators
"Live" indicators must use a pulsing Electric Lime dot. Secondary chips for surface types (e.g., Grass, Clay, Hard) use outline styles with all-caps labels.

### Input Fields
Inputs are dark-themed with a 1px Navy-Light border. On focus, the border must transition to Electric Lime. Error states should use a high-visibility Coral or Red, but never at the expense of the Lime primary action.

### Match Statistics
Data visualization (bar charts for serve percentages, heatmaps for ball placement) should use Electric Lime as the "positive" metric and a muted Navy/Grey for the "baseline" metric. Lines should be thin and precise.