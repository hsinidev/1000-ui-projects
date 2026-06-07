---
name: Elite Minimalist
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#181a1a'
  on-tertiary-container: '#818383'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '500'
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
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-page: 64px
  section-gap: 120px
---

## Brand & Style
This design system is built on the philosophy of "Quiet Luxury." It caters to a high-net-worth audience that values discretion, architectural precision, and effortless functionality over overt flashiness. The aesthetic is rooted in a blend of **Minimalism** and **Tactile Modernism**, prioritizing negative space to create a sense of digital "breathing room."

The emotional response should be one of calm assurance and exclusivity. By utilizing a dark-mode-first approach with high-end finishes, the UI feels like a private lounge—secure, curated, and premium. Visual elements are reduced to their essential forms, using light and shadow rather than heavy lines to define structure.

## Colors
The palette for this design system is anchored by **Deep Charcoal (#1A1A1A)**, which serves as the primary canvas to evoke depth and sophistication. **Champagne Gold (#D4AF37)** is used sparingly as a "high-light" for critical actions and brand markers, ensuring it remains a symbol of quality rather than an overwhelming presence.

**Off-White (#F9F9F9)** provides high-readability contrast for typography and secondary backgrounds. A muted accent tone, **#3D3A30**, should be used for subtle borders and dividers to bridge the gap between the charcoal and gold, maintaining the "discreet" nature of the identity.

## Typography
This design system utilizes **Manrope** for its entire type scale. Chosen for its modern, geometric construction and exceptional legibility, it balances a professional fintech-like clarity with a softened, contemporary edge.

Headlines should use tighter letter-spacing and heavier weights to anchor sections, while body text requires generous line heights (1.6x) to facilitate scanning. Labels are treated with slight tracking (letter-spacing) and uppercase styling to denote a sense of organized, institutional reliability.

## Layout & Spacing
The layout philosophy relies on a **Fixed Grid** system centered within a wide viewport. By using a 12-column structure with generous margins (64px+), the design system ensures content never feels crowded. 

Spacing is governed by an 8px linear scale. A defining characteristic of this system is the "Section Gap" (120px), which intentionally forces the user to focus on one narrative block at a time. Elements should be aligned with significant negative space—often referred to as "white space"—even in a dark-themed UI, to maintain the premium, gallery-like feel.

## Elevation & Depth
Depth is conveyed through **Tonal Layering** and **Low-Contrast Outlines**. Surfaces are stacked using subtle variations of charcoal; for example, a modal might be one step lighter than the background (#242424 over #1A1A1A).

Shadows are rarely used for "lift." Instead, they are used as "Ambient Glows"—highly diffused, low-opacity (10-15%) blurs that take on a slight gold or bronze tint to suggest a light source hitting a metallic surface. 1px refined borders in muted gold or semi-transparent off-white are the primary method for defining card boundaries and input fields, replacing the need for aggressive drop shadows.

## Shapes
The shape language is **Organic and Rounded**. By utilizing a base corner radius of 0.5rem (8px), the UI sheds the clinical coldness of sharp-edged minimalism in favor of a more approachable, human-centric form. Larger containers like cards and modals should use `rounded-xl` (1.5rem / 24px) to emphasize the organic visual style, creating "soft pods" of information that feel comfortable and modern.

## Components
### Buttons
Buttons are predominantly "Ghost" style or "Solid Deep." Primary buttons use a solid Champagne Gold fill with Deep Charcoal text for maximum contrast. Secondary buttons utilize a 1px Gold border with transparent centers. Hover states should include a subtle "inner glow" rather than a color shift.

### Cards
Cards are defined by their 1px `#3D3A30` borders and `rounded-xl` corners. Backgrounds should be slightly lighter than the page body to create a sense of physical layering.

### Inputs
Input fields are minimalist under-lined or fully enclosed with soft corners. The focus state must be a gentle gold border-glow, avoiding heavy focus rings.

### Navigation
The navigation should be "Floating" or "Persistent Minimalist." Use high-transparency backgrounds with a background-blur (glassmorphism) effect to allow the Deep Charcoal content to peak through, maintaining the sense of depth.

### Chips & Tags
Used for categorization, these should be small, pill-shaped, and use the `label-sm` typography. They serve as subtle markers rather than focal points.