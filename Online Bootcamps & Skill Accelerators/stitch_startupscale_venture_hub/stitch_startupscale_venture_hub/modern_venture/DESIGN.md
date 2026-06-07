---
name: Modern Venture
colors:
  surface: '#f9f9ff'
  surface-dim: '#d3daea'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eefe'
  surface-container-high: '#e2e8f8'
  surface-container-highest: '#dce2f3'
  on-surface: '#151c27'
  on-surface-variant: '#434843'
  inverse-surface: '#2a313d'
  inverse-on-surface: '#ebf1ff'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#5d5f5d'
  on-secondary: '#ffffff'
  secondary-container: '#e2e3e1'
  on-secondary-container: '#636563'
  tertiary: '#171717'
  on-tertiary: '#ffffff'
  tertiary-container: '#2b2b2b'
  on-tertiary-container: '#929292'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#e2e3e1'
  secondary-fixed-dim: '#c6c7c5'
  on-secondary-fixed: '#1a1c1b'
  on-secondary-fixed-variant: '#454746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#f9f9ff'
  on-background: '#151c27'
  surface-variant: '#dce2f3'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
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
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The design system is engineered to evoke an atmosphere of institutional stability and exclusive opportunity. It caters to high-growth founders and seasoned investors, prioritizing clarity over decoration. The visual style is a blend of **High-Fidelity Minimalism** and **Corporate Modernism**, characterized by a rigorous adherence to vertical rhythm and structural integrity. 

By utilizing generous whitespace and a restricted color palette, the system communicates a "less but better" philosophy. Every element is intentional, designed to foster trust and project an image of a premium, secure environment where significant business ventures are nurtured.

## Colors
The palette is anchored by **Deep Forest Green**, a color chosen to represent growth, endurance, and traditional financial stability. This is balanced against a foundational **Off-White**, which serves as the primary canvas color to reduce eye strain and provide a sophisticated alternative to pure white. 

**Black** is reserved for high-contrast elements, such as primary headlines and premium action states, ensuring a crisp, authoritative hierarchy. For functional UI elements like borders and secondary text, a range of neutral greys is used to maintain the minimalist aesthetic without sacrificing legibility.

## Typography
This design system utilizes **Manrope** for its balance of geometric precision and professional warmth. The typography is the primary driver of the "Stability" psychology, employing a strong vertical rhythm and tight letter-spacing for headlines to create an authoritative, "locked-in" appearance.

Headlines should always use the Bold or Semibold weights to command attention, while body copy remains light and spacious to ensure high readability in data-heavy environments. Labels use a higher letter-spacing and uppercase styling where appropriate to differentiate metadata from actionable content.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy to reinforce the brand's sense of structure. A 12-column grid system is used for desktop views, with a maximum container width of 1280px to prevent excessive line lengths and maintain a "contained" and secure feel.

Spacing is built on a 4px baseline, but defaults to 16px (md) and 24px (lg) increments for most component relationships. Generous "air" (64px+) should be applied between major sections to emphasize the premium nature of the content and allow the user's eye to rest, avoiding the cluttered appearance of traditional "startup" dashboards.

## Elevation & Depth
In this design system, depth is communicated through **Low-contrast outlines** and **Tonal layering** rather than aggressive shadows. Surfaces are stacked using subtle variations of the neutral palette. 

When an element must appear elevated (such as a modal or a primary dropdown), use a highly diffused, low-opacity shadow (#000000 at 4-8% opacity) with a large blur radius to maintain a soft, ambient feel. For standard cards and containers, use a 1px border in a soft neutral tone to define boundaries without breaking the flat, high-fidelity aesthetic.

## Shapes
The shape language is disciplined and "Soft," utilizing a 0.25rem (4px) base radius for standard components like buttons and input fields. This slight rounding removes the harshness of pure 90-degree angles while maintaining a precision-engineered look. 

Larger containers like cards or feature blocks may use a 0.5rem (8px) radius to provide a subtle visual nesting effect. Avoid pill-shaped or highly rounded elements, as they contradict the system's focus on authoritative stability.

## Components
- **Buttons:** Primary buttons use the Deep Forest Green background with Off-White text. They are rectangular with a 4px corner radius. Secondary buttons should use a 1px Black or Dark Green border with no fill.
- **Input Fields:** Use a thin 1px border. On focus, the border transitions to Deep Forest Green. Labels are positioned above the field in the `label-md` style.
- **Cards:** White or Off-White backgrounds with a 1px subtle border. No heavy drop shadows; depth is created by the contrast between the card and the page background.
- **Chips/Badges:** Small, rectangular badges with high-contrast background/text pairings. Used for status indicators (e.g., "Seed Stage," "Active").
- **Lists:** Data-heavy lists should use "zebra-striping" with very faint Off-White/Grey alternations or simple 1px horizontal dividers to maintain vertical rhythm.
- **Metric Cards:** Large-format typography for numbers (h1 or h2) paired with small `label-sm` descriptors to highlight key incubator performance indicators.