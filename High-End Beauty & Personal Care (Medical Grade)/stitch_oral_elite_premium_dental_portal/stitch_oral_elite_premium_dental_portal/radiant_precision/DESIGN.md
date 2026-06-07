---
name: Radiant Precision
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3f484c'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6f787d'
  outline-variant: '#bfc8cd'
  surface-tint: '#0c6780'
  primary: '#0c6780'
  on-primary: '#ffffff'
  primary-container: '#87ceeb'
  on-primary-container: '#005870'
  inverse-primary: '#89d0ed'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#5e5e5d'
  on-tertiary: '#ffffff'
  tertiary-container: '#c5c4c2'
  on-tertiary-container: '#505150'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#baeaff'
  primary-fixed-dim: '#89d0ed'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#004d62'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e3e2e0'
  tertiary-fixed-dim: '#c7c6c4'
  on-tertiary-fixed: '#1b1c1b'
  on-tertiary-fixed-variant: '#464746'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
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
    lineHeight: '1.6'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-page: 64px
  section-gap: 120px
---

## Brand & Style
The design system is anchored in the concept of **Radiant Precision**. It caters to a discerning clientele seeking perfection in both health and aesthetics. The brand personality is authoritative, sterile yet welcoming, and unapologetically premium. 

The visual style is a fusion of **Minimalism** and **Modern Corporate**, elevated by tactile "luxury" cues. It emphasizes hyper-clarity and structural integrity to evoke a sense of clinical safety. The UI should feel like a high-end dental atelier: bright, airy, and meticulously organized. We avoid visual clutter to reduce patient anxiety, instead using generous whitespace to signal exclusivity and calm.

## Colors
The palette is dominated by **Brilliant White (#FFFFFF)** to establish a foundation of clinical purity. **Sky Blue (#87CEEB)** serves as the primary action color, chosen for its psychological associations with serenity, breath, and hygiene. 

Luxury is introduced through a dual-tone silver strategy. **Platinum (#E5E4E2)** is used for subtle backgrounds and large-surface containers, while **Silver (#C0C0C0)** is reserved for borders, dividers, and decorative metallic gradients. Gradients should be used sparingly—appearing on primary buttons or header accents—to mimic the sheen of polished medical instruments or high-end jewelry.

## Typography
This design system utilizes **Inter** exclusively to maintain a systematic and utilitarian clarity. The typeface’s high x-height and neutral character reinforce the clinical aspect of the brand.

To achieve a "luxurious" feel, we employ tight tracking on large display headings and generous line-heights for body copy. Headlines should use a medium weight to feel substantial without being heavy. Small labels and metadata should use uppercase styling with increased letter spacing to emulate the branding found on high-end cosmetic packaging.

## Layout & Spacing
The layout follows a **Fixed Grid** model to project a sense of stability and controlled environment. A 12-column grid is used for desktop views, with wide page margins to ensure content feels "presented" rather than just placed.

Spacing is aggressive; "The Luxury of Space" is a core principle. Use large vertical gaps (section-gap) between different content blocks to prevent the interface from feeling crowded. Internal component padding should be generous to ensure touch targets are comfortable and the UI feels breathable.

## Elevation & Depth
Depth is conveyed through **Low-Contrast Outlines** and **Ambient Shadows**. This design system avoids heavy drop shadows in favor of 1px solid borders in Silver (#C0C0C0) to define containers.

When elevation is required (e.g., for modals or floating cards), use a "Polished Surface" effect: a multi-layered, highly diffused shadow with very low opacity (3-5%) and a slight blue tint (#87CEEB) in the shadow color. This creates a glow rather than a dark void, maintaining the radiant aesthetic. Subtle linear gradients (top-to-bottom) on cards moving from White to Platinum create a soft, metallic curvature.

## Shapes
The shape language is **Soft (0.25rem)**. While sharp corners feel too aggressive and fully rounded "pill" shapes feel too casual, a subtle radius provides a bridge between clinical precision and human approachability. 

Borders are always crisp and 1px wide. Interactive elements like buttons and input fields should maintain this consistent radius to ensure a cohesive, architectural look throughout the system.

## Components
- **Buttons**: Primary buttons feature a subtle metallic linear gradient (Sky Blue to a slightly lighter tint). They use 1px borders in a darker shade of the primary color. Text is always centered and set in a medium weight.
- **Input Fields**: Fields use a 1px border in Silver (#C0C0C0). On focus, the border transitions to Sky Blue with a soft 2px outer glow. Labels sit strictly above the field in the uppercase Label-SM style.
- **Cards**: Cards are Brilliant White with a 1px Silver border. They should not have shadows unless they are interactive or hoverable.
- **Chips**: Used for dental services or tags. They feature a Platinum background with no border and Sky Blue text to keep them light and non-intrusive.
- **Progress Indicators**: For treatment plans, use thin, precise lines. Completed steps are Sky Blue; upcoming steps are Silver.
- **Trust Elements**: Testimonial blocks and certification badges should be framed in "Silver Metallic" containers to emphasize high-end validation and professional clarity.