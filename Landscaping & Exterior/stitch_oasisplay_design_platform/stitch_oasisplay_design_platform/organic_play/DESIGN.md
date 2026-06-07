---
name: Organic Play
colors:
  surface: '#fbf9f5'
  surface-dim: '#dbdad6'
  surface-bright: '#fbf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ef'
  surface-container: '#efeeea'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e4e2de'
  on-surface: '#1b1c1a'
  on-surface-variant: '#41493c'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f0ed'
  outline: '#717a6b'
  outline-variant: '#c1c9b9'
  surface-tint: '#2d6b1f'
  primary: '#2a691d'
  on-primary: '#ffffff'
  primary-container: '#438334'
  on-primary-container: '#f8ffef'
  inverse-primary: '#93d87e'
  secondary: '#006398'
  on-secondary: '#ffffff'
  secondary-container: '#6cbdfe'
  on-secondary-container: '#004b75'
  tertiary: '#79542e'
  on-tertiary: '#ffffff'
  tertiary-container: '#956c44'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#aef597'
  primary-fixed-dim: '#93d87e'
  on-primary-fixed: '#022200'
  on-primary-fixed-variant: '#115206'
  secondary-fixed: '#cde5ff'
  secondary-fixed-dim: '#94ccff'
  on-secondary-fixed: '#001d32'
  on-secondary-fixed-variant: '#004b74'
  tertiary-fixed: '#ffdcbd'
  tertiary-fixed-dim: '#eebd8e'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#61401b'
  background: '#fbf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2de'
typography:
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.02em
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
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style
The design system is built upon the intersection of **Organic Minimalism** and **Tactile Sustainability**. It aims to evoke the sensory experience of an outdoor playground: the freshness of the air, the solidity of timber, and the softness of grass. 

The personality is "The Professional Caretaker"—knowledgeable and precise enough for architects and urban designers, yet warm and approachable for parents. The aesthetic avoids the neon-bright "plastic" look of traditional play areas in favor of a sophisticated, nature-inspired palette. Visuals prioritize whitespace to represent safety and clarity, while hand-drawn elements introduce a human touch that differentiates this design system from sterile corporate interfaces.

## Colors
The palette is derived directly from natural landscapes. 
- **Grass Green (Primary):** Used for growth-oriented actions, primary buttons, and success states. It represents the foundation of the play area.
- **Sky Blue (Secondary):** Used for informational elements, links, and accents. It provides a sense of openness and freedom.
- **Natural Wood (Tertiary):** A warm, earthy brown used for structural elements, secondary buttons, and borders. It adds a tactile, sturdy feel to the UI.
- **Oatmeal (Neutral):** The background color is a soft off-white rather than a pure sterile white, reducing eye strain and feeling more "recycled" and sustainable.

## Typography
This design system utilizes **Plus Jakarta Sans** for its exceptional balance of modern geometry and friendly, open counters. The typeface feels optimistic and approachable while maintaining the legibility required for technical documentation and safety specifications.

Headlines should use tighter tracking to feel cohesive, while body text uses a generous 1.6x line-height to ensure accessibility for parents browsing on mobile devices or designers reviewing long-form proposals.

## Layout & Spacing
The layout follows a **Fixed Grid** model for desktop (1280px container) to maintain a curated, editorial feel. A 12-column system is used with generous 24px gutters.

The spacing rhythm is based on an 8px scale, but emphasizes "breathable" margins. Rather than crowding components, this design system encourages large 48px or 80px vertical gaps between sections to reflect the spaciousness of a park. Elements should often be center-aligned to create a balanced, calm reading experience.

## Elevation & Depth
Depth in this design system is achieved through **Tonal Layers** and **Ambient Shadows** rather than high-contrast silhouettes. 

Surfaces use very soft, diffused shadows (Blur: 20px, Opacity: 6%) with a slight tint of the Natural Wood color (#A67C52) to prevent the "gray" muddy look of default shadows. To simulate physical materials, some containers may use a subtle, low-opacity grain texture overlay. We avoid glassmorphism in favor of "solid" feeling surfaces that suggest stability and safety.

## Shapes
Shapes are intentionally soft to mirror the "no-sharp-edges" safety philosophy of children's play equipment. 

The primary radius is 0.5rem (8px), which scales up to 1.5rem (24px) for large containers and cards. This "Rounded" approach ensures that even large components feel friendly. Icons must always use rounded caps and joins to match the UI's curvature.

## Components
- **Buttons:** Primary buttons are pill-shaped with a subtle "squishy" shadow that moves on press, mimicking a tactile playground surface.
- **Input Fields:** Use a thick 2px border in the "Natural Wood" tone. Focus states transition the border to "Grass Green" with a soft outer glow.
- **Cards:** Feature large corner radii (24px) and use the Oatmeal neutral color as a base, separated from the background by a thin, low-contrast "Wood" border.
- **Hand-Drawn Icons:** All iconography must appear hand-sketched with slight imperfections. This adds a playful, artisanal layer to the professional layout.
- **Progress Bars:** Designed to look like growing vines or wooden slats being filled, reinforcing the sustainable theme.
- **Chips/Labels:** Small, fully rounded (pill-shaped) tags used for material types (e.g., "Oak," "Recycled Rope").