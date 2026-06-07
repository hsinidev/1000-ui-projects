---
name: Forest Discipline
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#414844'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#586062'
  on-secondary: '#ffffff'
  secondary-container: '#dae1e3'
  on-secondary-container: '#5d6466'
  tertiary: '#1f2825'
  on-tertiary: '#ffffff'
  tertiary-container: '#353e3a'
  on-tertiary-container: '#9fa9a3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#dde4e6'
  secondary-fixed-dim: '#c1c8ca'
  on-secondary-fixed: '#161d1f'
  on-secondary-fixed-variant: '#41484a'
  tertiary-fixed: '#dbe5df'
  tertiary-fixed-dim: '#bfc9c3'
  on-tertiary-fixed: '#151d1a'
  on-tertiary-fixed-variant: '#3f4945'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  grid_gutter: 20px
  grid_margin: 32px
---

## Brand & Style
The brand personality is authoritative yet encouraging—a digital mentor for aspiring project managers. It balances the rigor of PMP and Agile methodologies with the fluidity of modern collaboration. The target audience consists of ambitious professionals who require high information density without cognitive overload.

The design style is **Corporate / Modern** with a strong emphasis on **Minimalism** and structural clarity. It utilizes a "Bento-box" organizational strategy to compartmentalize complex certification data into digestible, focused modules. The emotional response is one of calm confidence and organized progress.

## Colors
The palette is rooted in stability and focus. **Deep Forest Green** serves as the primary anchor, used for key actions and brand presence to evoke growth and professional maturity. **Charcoal** provides high-contrast legibility for complex data and secondary accents. 

**Off-White** and pure white form the foundation of the surface layers, creating a clean environment that prevents fatigue during long study sessions. Success states utilize a lighter shade of the forest green, while warnings are kept minimal to maintain the professional atmosphere.

## Typography
This design system employs a dual-font strategy. **Manrope** is used for headlines to provide a modern, refined, and balanced appearance that feels contemporary. **Inter** is utilized for all body text, data visualizations, and labels due to its systematic, utilitarian nature and exceptional legibility at small sizes. 

For certification-specific data (timer, score ratios, and agile metrics), use the "data-mono" style which leverages Inter’s tabular num features to ensure numerical alignment in dashboards and tables.

## Layout & Spacing
The layout follows a **Fixed Grid** model for the main content area (max-width 1440px) to ensure reading lines remain comfortable. The "Bento-box" philosophy dictates that information is grouped into distinct containers of varying sizes.

A 12-column grid is used, but elements should primarily be grouped into 3, 4, or 6 column spans to maintain the modular look. Spacing follows a strict 8px rhythm. Margins within bento containers should be consistent (24px) to provide ample breathing room between dense data points.

## Elevation & Depth
Depth is conveyed through **Tonal Layers** combined with **Ambient Shadows**. The background uses the Off-White palette, while the primary Bento containers are pure white. 

Shadows are extremely subtle: a 4px to 12px blur with low-opacity (5%) Charcoal tinting, used only to lift the containers slightly from the background. This creates a "stacked paper" effect rather than a floating one. Avoid heavy blurs or colorful glows; the focus must remain on the content. High-level interactions, like active modal dialogs, use a semi-transparent Charcoal overlay to dim the background.

## Shapes
The shape language is defined by **Rounded** corners. Standard containers use a 0.5rem (8px) radius to strike a balance between professional precision and modern friendliness. Larger Bento modules or main dashboard cards should use the `rounded-lg` (16px) variant to emphasize the modular structure. This soft corner treatment mitigates the "sharpness" of the dense data tables and technical content.

## Components
- **Buttons:** Primary buttons are solid Deep Forest Green with white text and 8px rounded corners. Secondary buttons use a Charcoal outline with no fill.
- **Bento Cards:** The core component. White background, 16px corner radius, and a 1px border in a very light Charcoal tint (#E9ECEF) to define edges in high-brightness environments.
- **Progress Indicators:** Use thick, 8px high bars with the Deep Forest Green for completed sections and Tertiary green for the track.
- **Chips/Tags:** Used for Agile categories (e.g., "Scrum", "Kanban"). Subtle charcoal backgrounds with semi-bold text.
- **Input Fields:** Minimalist design with a 1px Charcoal border that thickens to 2px in Deep Forest Green on focus.
- **Collaborative Avatars:** Small circular images with a 2px white border, stacked with a 4px overlap in collaborative study rooms.
- **Flashcards:** Specialized cards with a distinct 24px corner radius and centralized, large-scale typography for focus-mode studying.