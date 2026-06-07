---
name: Precision Analytical
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#44474c'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#75777d'
  outline-variant: '#c4c6cd'
  surface-tint: '#515f74'
  primary: '#303e51'
  on-primary: '#ffffff'
  primary-container: '#475569'
  on-primary-container: '#bbcae1'
  inverse-primary: '#b9c7df'
  secondary: '#565f6a'
  on-secondary: '#ffffff'
  secondary-container: '#dae3f0'
  on-secondary-container: '#5c6570'
  tertiary: '#323d50'
  on-tertiary: '#ffffff'
  tertiary-container: '#495468'
  on-tertiary-container: '#bdc8e0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e3fc'
  primary-fixed-dim: '#b9c7df'
  on-primary-fixed: '#0d1c2e'
  on-primary-fixed-variant: '#3a485b'
  secondary-fixed: '#dae3f0'
  secondary-fixed-dim: '#bdc8d3'
  on-secondary-fixed: '#131d25'
  on-secondary-fixed-variant: '#3e4852'
  tertiary-fixed: '#d8e3fb'
  tertiary-fixed-dim: '#bcc7de'
  on-tertiary-fixed: '#111c2d'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-tabular:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  grid-columns: '12'
  grid-gutter: 16px
  grid-margin: 32px
---

## Brand & Style
This design system is engineered for high-stakes talent acquisition where data integrity and professional trust are paramount. The brand personality is clinical, authoritative, and global—eschewing decorative flourishes in favor of information density and technical accuracy. 

The visual style is **Corporate / Modern** with a heavy influence from **Minimalism**. It prioritizes a "dashboard-first" mentality, ensuring that recruiters can scan vast amounts of talent data without cognitive fatigue. The aesthetic communicates a sense of "intelligence-grade" software, using clean lines and a restricted palette to focus the user’s attention on metrics, trends, and candidate profiles.

## Colors
The palette is rooted in a professional spectrum of grays and slate blues to maintain a neutral, unbiased environment for talent evaluation. 

- **Primary (Slate Blue):** Used for structural elements, primary actions, and branding accents.
- **Secondary (Silver):** Applied to borders, dividers, and disabled states to provide subtle definition.
- **Tertiary (Deep Navy):** Reserved for high-contrast typography and critical UI anchors.
- **Neutral (Ghost White):** Used for background surfaces to provide a crisp, clean canvas.

Success, warning, and error states should utilize desaturated versions of green, amber, and red to ensure they harmonize with the Slate Blue foundation without breaking the analytical tone.

## Typography
Inter is the foundational typeface for this design system, chosen for its exceptional legibility in data-heavy environments and its neutral, technical character. 

Hierarchy is established through weight and case rather than size alone. **Label-caps** are utilized for table headers and section metadata to provide clear categorization. For numerical data within tables and charts, the `data-tabular` style must be used with "tabular figures" enabled to ensure vertical alignment of digits, facilitating easier comparison of candidate scores and salary data.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for desktop views to maintain a controlled information density, transitioning to a fluid model for mobile quick-capture interfaces. 

The rhythm is governed by a strict 4px baseline. Components are spaced with precision to maximize "above-the-fold" data visibility. Layouts should favor structured columns; use 12-column grids for dashboards where data tables might span 8-10 columns, leaving sidebars for filtering and quick-capture inputs. Gutters are kept tight (16px) to emphasize the interconnected nature of the data.

## Elevation & Depth
Depth is communicated through **Tonal Layers** and **Low-contrast Outlines** rather than traditional shadows. This approach maintains a flat, professional profile that feels integrated rather than floating.

- **Level 0 (Background):** #F8FAFC. The base canvas.
- **Level 1 (Cards/Containers):** #FFFFFF with a 1px border in #CBD5E1. Used for primary content modules.
- **Level 2 (Interaction/Popovers):** #FFFFFF with a 1px border and a very soft, high-diffusion shadow (8% opacity) to indicate temporary focus or modality.

Surfaces should never appear "heavy." The goal is a stacked paper aesthetic where depth is suggested by subtle shifts in value and crisp perimeters.

## Shapes
The shape language is **Soft (Level 1)**, utilizing a 4px (0.25rem) radius for standard components like buttons and input fields. This slight rounding prevents the UI from feeling overly aggressive or "brutalist" while maintaining a sharp, technical edge.

Larger containers such as cards may use an 8px (0.5rem) radius to define major content areas. Interactive elements like tags or "chips" for candidate skills should maintain the 4px standard to ensure they feel like functional data points rather than playful UI elements.

## Components
- **Data Tables:** The core of the system. Use zebra-striping with #F8FAFC for row readability. Headers must be fixed on scroll, using `label-caps` typography.
- **Radar Charts:** Used for candidate competency mapping. Lines should be 1.5px thick in Slate Blue, with a semi-transparent Slate Blue fill (10% opacity).
- **Trend Lines:** Monotone lines (Slate Blue) with area fills to show recruitment velocity or talent pool growth.
- **Quick-Capture Inputs:** Designed for mobile efficiency. Use "Floating Labels" to save vertical space. The active state should feature a 2px Slate Blue bottom-border.
- **Buttons:** Primary buttons use a solid Slate Blue fill with White text. Secondary buttons use a Silver border with Slate Blue text.
- **Cards:** Used for candidate snapshots. Must include a clear information hierarchy: Name (H3), Current Role (Body-md), and Key Metrics (Label-caps).
- **Status Badges:** Small, rectangular badges with a 2px radius. Use neutral backgrounds with high-contrast text to indicate "Vetted," "In-Progress," or "Placed."