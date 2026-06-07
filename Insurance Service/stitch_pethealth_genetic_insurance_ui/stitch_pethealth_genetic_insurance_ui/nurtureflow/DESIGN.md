---
name: NurtureFlow
colors:
  surface: '#f4faff'
  surface-dim: '#cbdde7'
  surface-bright: '#f4faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e7f6ff'
  surface-container: '#dff1fb'
  surface-container-high: '#d9ebf5'
  surface-container-highest: '#d4e5ef'
  on-surface: '#0d1e25'
  on-surface-variant: '#53433f'
  inverse-surface: '#23333a'
  inverse-on-surface: '#e2f3fd'
  outline: '#86736e'
  outline-variant: '#d8c2bb'
  surface-tint: '#8d4d38'
  primary: '#8d4d38'
  on-primary: '#ffffff'
  primary-container: '#ffab91'
  on-primary-container: '#793d29'
  inverse-primary: '#ffb59e'
  secondary: '#136964'
  on-secondary: '#ffffff'
  secondary-container: '#a4f0e9'
  on-secondary-container: '#1d706a'
  tertiary: '#715b37'
  on-tertiary: '#ffffff'
  tertiary-container: '#d9bc90'
  on-tertiary-container: '#5f4b28'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd0'
  primary-fixed-dim: '#ffb59e'
  on-primary-fixed: '#390c01'
  on-primary-fixed-variant: '#713623'
  secondary-fixed: '#a4f0e9'
  secondary-fixed-dim: '#89d4cd'
  on-secondary-fixed: '#00201e'
  on-secondary-fixed-variant: '#00504b'
  tertiary-fixed: '#fddeb0'
  tertiary-fixed-dim: '#e0c296'
  on-tertiary-fixed: '#281900'
  on-tertiary-fixed-variant: '#584322'
  background: '#f4faff'
  on-background: '#0d1e25'
  surface-variant: '#d4e5ef'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '600'
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
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style

This design system is built on the concept of "Nurturing Science." It balances the clinical precision of genetic data with the emotional warmth of pet ownership. The brand personality is empathetic, transparent, and joyful. 

The visual style is **Organic Minimalism**. It utilizes a clean, airy layout to ensure that complex medical information is never overwhelming, while incorporating soft, asymmetrical "blob" shapes and fluid containers to evoke a sense of life and playfulness. The interface should feel less like a financial tool and more like a wellness companion. High-quality, candid pet photography with warm lighting is essential to grounding the data in real-world love.

## Colors

The palette is designed to be soothing yet energetic. 
- **Peach (Primary):** Used for primary actions and brand moments. It conveys warmth and the "human" (or animal) side of care.
- **Mint (Secondary):** Represents health, vitality, and the scientific aspect of genetic data. It is used for accents, success states, and health-related visualizations.
- **Charcoal (Neutral):** Provides the necessary grounding. All typography and structural borders use this color to ensure high legibility and a sense of authority.
- **Cream (Background):** A soft, off-white base that prevents the interface from feeling clinical or cold.

## Typography

This design system uses a dual-font strategy to balance friendliness with readability. 
- **Plus Jakarta Sans** is the headline face. Its soft, rounded geometric forms feel optimistic and modern. 
- **Lexend** is used for all body copy and labels. Specifically designed for reading proficiency, it excels at making complex genetic risk factors and insurance terms easy to digest. 

Maintain generous line heights (1.6 for body) to ensure the interface feels breathable and accessible to all users.

## Layout & Spacing

The layout follows a **Fluid Grid** model with an emphasis on generous whitespace. The spacing rhythm is based on an 8px scale, ensuring consistent alignment. 

- **Organic Margins:** Rather than rigid edges, sections should often use staggered vertical spacing or "blob" background containers that bleed off-canvas to break the "boxed" feel of traditional insurance apps.
- **Information Density:** Genetic data views should utilize card-based layouts with high internal padding (24px+) to prevent data fatigue.

## Elevation & Depth

This design system avoids harsh shadows. Instead, it uses **Tonal Layers** and **Ambient Tinted Shadows**. 
- **Depth:** Higher elevation elements (like "Breed Risk" cards) use a soft, diffused shadow tinted with the primary Peach or Secondary Mint colors (e.g., 10% opacity, 20px blur).
- **Surface Tiering:** Use subtle shifts in background color (Cream to pure White) to create hierarchy without needing borders.
- **Glassmorphism:** Use subtle backdrop blurs (10px) on navigation bars to maintain the "airy" feel while overlaying photography.

## Shapes

The shape language is the core differentiator of this design system. 
- **Rounded Corners:** A base radius of 16px (rounded-lg) is applied to most cards and containers.
- **Blobs:** Hero sections and background decorative elements should use CSS `border-radius` with 4-point asymmetrical values (e.g., `60% 40% 30% 70% / 60% 30% 70% 40%`) to create "organic puddles" of color.
- **Interactive Elements:** Buttons and tags use a pill-shape (fully rounded) to maximize the friendly, approachable aesthetic.

## Components

- **Buttons:** Primary buttons are pill-shaped, using the Peach color with Charcoal text for maximum contrast. They should have a subtle "squish" animation on hover.
- **Genetic Risk Chips:** These use the Mint color with varying opacities to indicate risk levels (Lower risk = lighter Mint, higher risk = saturated Mint).
- **Pet Profile Cards:** Large, rounded cards with a prominent photo. Use an organic "blob" mask for the pet’s headshot instead of a standard circle.
- **Data Visualizations:** Genetic markers should be represented by soft, rounded bar charts and circular "petals" rather than sharp line graphs.
- **Inputs:** Input fields are softly rounded with a Charcoal border at 20% opacity, moving to 100% Peach on focus. Labels always sit above the field in Lexend Bold.
- **Progress Indicators:** Use a "paw print" or "bone" icon sequence for multi-step onboarding to keep the tone playful.