---
name: Vibrant Protection
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#494456'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#7a7488'
  outline-variant: '#cbc3d9'
  surface-tint: '#6d23f9'
  primary: '#4800b2'
  on-primary: '#ffffff'
  primary-container: '#6200ee'
  on-primary-container: '#d0beff'
  inverse-primary: '#cfbdff'
  secondary: '#586400'
  on-secondary: '#ffffff'
  secondary-container: '#d1ed00'
  on-secondary-container: '#5c6900'
  tertiary: '#3b3d41'
  on-tertiary: '#ffffff'
  tertiary-container: '#525458'
  on-tertiary-container: '#c8c8cd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e8ddff'
  primary-fixed-dim: '#cfbdff'
  on-primary-fixed: '#22005d'
  on-primary-fixed-variant: '#5300cd'
  secondary-fixed: '#d4f000'
  secondary-fixed-dim: '#b9d200'
  on-secondary-fixed: '#191e00'
  on-secondary-fixed-variant: '#424b00'
  tertiary-fixed: '#e2e2e7'
  tertiary-fixed-dim: '#c6c6cb'
  on-tertiary-fixed: '#1a1c1f'
  on-tertiary-fixed-variant: '#45474b'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
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
  label-bold:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
  button:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '700'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
  container-max: 1200px
---

## Brand & Style

This design system is built for the modern creator economy, blending high-stakes professional liability with the energetic aesthetic of digital content creation. The brand personality is "The Professional Hype-Man": authoritative enough to trust with legal protection, yet vibrant enough to feel like a peer. 

The style utilizes a **Modern-Tactile** approach. It leverages the structured organization of **Bento-box layouts** to simplify complex insurance information into digestible, interactive modules. The visual language balances high-conversion energy with extreme clarity, using "Electric Yellow" as a precision tool for calls-to-action against a sophisticated "Vibrant Purple" foundation.

## Colors

The palette is designed for high impact and functional hierarchy. 
- **Primary (Vibrant Purple):** Used for brand presence, headers, and secondary actions. It provides a professional, deep backdrop that makes the accent color pop.
- **Secondary (Electric Yellow):** The "Conversion King." This color is reserved exclusively for primary buttons, critical alerts, and key data points. 
- **Neutral:** A range of deep charcoals and soft off-whites. Pure white (#FFFFFF) is used for card surfaces to maintain a clean, trustworthy "Pro" feel.
- **Success/Error:** While adhering to the palette, subtle emerald and rose tints are used for status indicators, ensuring they don't clash with the Electric Yellow.

## Typography

The typography utilizes **Plus Jakarta Sans** for its friendly, rounded terminals and exceptional modern readability. It mimics the approachable nature of "Quicksand" but provides the professional weight and kerning required for a fintech/legal product.

- **Headlines:** Use ExtraBold (800) weights with tight letter spacing to create a "bold creator" look.
- **Body:** Use Regular (400) weights with generous line heights to ensure complex policy terms are easy to scan.
- **Labels:** Use Bold (700) and uppercase styling for small metadata or section tags to provide a crisp, organized hierarchy within the Bento cards.

## Layout & Spacing

This design system employs a **Fixed-Width Grid** model optimized for Bento-box layouts. 
- **Grid:** A 12-column grid on desktop with 24px gutters. 
- **Bento Logic:** Elements should span 3, 4, 6, or 12 columns. Vertical spacing between Bento cards should match the horizontal gutter (24px) to create a perfect masonry appearance.
- **Rhythm:** Use an 8px base unit. Internal card padding is consistently 32px to provide a premium, airy feel that balances the high-energy colors.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Tonal Layering**. 
- **Cards:** Use large, ultra-soft shadows (32px+ blur, 4% opacity) with a slight purple tint (#6200EE) to ground white cards on the tertiary background.
- **Floating Actions:** Primary buttons use a slightly sharper shadow to suggest interactivity and "press-ability."
- **Layering:** Backgrounds are kept at a neutral off-white (#F4F4F9), while active card surfaces are pure white (#FFFFFF). This subtle contrast guides the eye to the content without visual clutter.

## Shapes

The shape language is defined by **Extreme Softness**. 
- **Containers:** All Bento cards must have a corner radius of at least 24px to evoke a friendly, modern app aesthetic. 
- **Interactive Elements:** Buttons and input fields use a 16px radius (rounded-lg) to maintain consistency with the large card corners. 
- **Icons:** Use thick-stroke (2pt) icons with rounded caps and joins to match the typography.

## Components

- **Buttons:** Primary buttons are Electric Yellow with black text. On hover, they should scale slightly (1.02x) and deepen in shadow. Secondary buttons use a thick Purple stroke and no fill.
- **Bento Cards:** The foundational element. Cards should have distinct "Header" and "Content" areas. Some cards may use the Vibrant Purple as a fill with white text to highlight "Hot" features like "Active Claims."
- **Inputs:** Use thick 2px borders in soft gray. On focus, the border transitions to Vibrant Purple with a subtle glow.
- **Chips/Badges:** Small, pill-shaped indicators for status (e.g., "Insured," "Pending"). Use high-contrast background fills from the brand palette.
- **Creator Dashboard Stats:** Large-format typography within Bento cards, using the Electric Yellow for the numerical values to draw immediate attention.