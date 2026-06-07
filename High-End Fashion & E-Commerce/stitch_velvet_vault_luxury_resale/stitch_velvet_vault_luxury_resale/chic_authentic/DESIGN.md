---
name: Chic & Authentic
colors:
  surface: '#fff8f5'
  surface-dim: '#e1d8d4'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2ed'
  surface-container: '#f5ece7'
  surface-container-high: '#efe6e2'
  surface-container-highest: '#e9e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#584141'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#8c7071'
  outline-variant: '#e0bfbf'
  surface-tint: '#af2b3e'
  primary: '#570013'
  on-primary: '#ffffff'
  primary-container: '#800020'
  on-primary-container: '#ff828a'
  inverse-primary: '#ffb3b5'
  secondary: '#70585b'
  on-secondary: '#ffffff'
  secondary-container: '#f8d8db'
  on-secondary-container: '#755d5f'
  tertiary: '#262829'
  on-tertiary: '#ffffff'
  tertiary-container: '#3c3e3e'
  on-tertiary-container: '#a8a9a9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdada'
  primary-fixed-dim: '#ffb3b5'
  on-primary-fixed: '#40000b'
  on-primary-fixed-variant: '#8e0f28'
  secondary-fixed: '#fbdbde'
  secondary-fixed-dim: '#debfc2'
  on-secondary-fixed: '#281719'
  on-secondary-fixed-variant: '#574144'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  display-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: notoSerif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: '0'
  headline-md:
    fontFamily: notoSerif
    fontSize: 22px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-sm:
    fontFamily: manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-lg:
    fontFamily: manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-md:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

This design system is built on the pillars of "Chic & Authentic," targeting a discerning clientele that values heritage, craftsmanship, and the circular luxury economy. The brand personality is that of an expert curator—sophisticated, knowledgeable, and impeccably organized. 

The visual style follows a **Minimalist Editorial** approach. It leverages generous whitespace to let high-resolution photography of luxury goods breathe, mimicking the experience of a high-end physical boutique or a premium fashion magazine. The interface avoids unnecessary ornamentation, relying instead on structural elegance, precise alignment, and subtle, high-quality borders to establish a sense of "archival" security and trust. Every element is designed to evoke an emotional response of aspiration tempered by reliability.

## Colors

The palette is a sophisticated trio that balances power with softness. 

- **Deep Burgundy (#800020)**: Used as the primary color for brand-critical elements, high-level headers, and primary actions. It represents the "Vault"—security, depth, and timeless luxury.
- **Soft Pink (#FADADD)**: Acts as a supporting accent for backgrounds, secondary buttons, or decorative elements. It softens the austerity of the burgundy and provides a "Chic" feminine touch without sacrificing maturity.
- **Crisp White (#FFFFFF)**: The foundation of the UI. It provides the "Generous Whitespace" required to make the product imagery pop.
- **Neutral (#2D2926)**: A near-black charcoal used for body text and hairline borders to maintain high legibility while appearing softer and more premium than pure black.

## Typography

This design system utilizes a high-contrast typographic pairing to reinforce its "Chic & Authentic" aesthetic. 

**Noto Serif** is used for all headlines and display text. Its refined, classic proportions evoke traditional luxury and editorial authority. It should be used with tight letter-spacing for large displays to maintain a cohesive visual "weight."

**Manrope** is the workhorse for body copy and interface labels. Its modern, balanced geometric construction ensures perfect readability across all device sizes. For labels and navigation items, use uppercase styling with increased letter-spacing to create a clean, organized, and premium feel.

## Layout & Spacing

This design system employs a **Fixed Grid** model on desktop to ensure that product compositions remain intentional and balanced. A 12-column grid is used with generous 24px gutters.

The spacing rhythm is intentionally "loose." We use a base-8 increment system, but prioritize large vertical gaps (section-gaps) between content blocks to prevent the interface from feeling crowded or "discount." Layouts should prioritize asymmetrical balance, often utilizing offset columns to create a dynamic, fashion-forward feel.

## Elevation & Depth

To maintain a "High-End" feel, this design system avoids heavy shadows or complex gradients. Instead, it uses **Low-Contrast Outlines** and **Tonal Layers** to establish hierarchy.

- **Borders**: Hairline borders (1px) in a light neutral or Soft Pink are the primary method for defining sections and cards. This creates a "framed" effect similar to a gallery.
- **Surface Layers**: Subtle shifts in background color (from White to a very faint tint of Soft Pink) are used to distinguish between the main canvas and secondary containers.
- **Shadows**: When depth is strictly necessary (e.g., for modal overlays), use a single, highly-diffused ambient shadow with very low opacity (5-10%) and a slight burgundy tint to maintain color harmony.

## Shapes

The shape language is structured and architectural. We use a **Soft (1)** roundedness level (4px - 12px) to ensure the UI feels modern and approachable without losing the sharp, tailored look associated with luxury fashion. 

Primary buttons and input fields should utilize the base 4px radius, while larger containers like product cards or imagery modules may use up to 8px or 12px. Interactive elements like tags or "Trust Badges" should remain consistently sharp-cornered or only slightly softened to maintain an "official" and authentic appearance.

## Components

### Buttons
- **Primary**: Solid Deep Burgundy with White Manrope (Uppercase). No icons unless necessary for navigation.
- **Secondary**: Outline style with a 1px Deep Burgundy border or solid Soft Pink background.
- **Ghost**: Text-only with an underline that appears on hover, emphasizing the "Editorial" look.

### Cards (Product)
Cards are the hero of this design system. They must be borderless or use a very faint hairline border. The image should occupy at least 70% of the card area. Typography below the image should be center-aligned or strictly left-aligned, using Noto Serif for the product name.

### Trust Signals
"Authenticity Guaranteed" badges and "Expert Verified" labels should be treated with high-contrast styling—often Deep Burgundy text on a Soft Pink background—using the `label-md` typographic style to feel like a seal of quality.

### Input Fields
Clean, minimal lines. Use a bottom-border only or a very light 4-sided border. Focus states should be indicated by a shift to Deep Burgundy for the border color.

### Imagery
All imagery should have a consistent art direction: soft, natural lighting, and minimalist backgrounds. Use "Aspect Ratio" containers to ensure images never appear stretched or distorted.