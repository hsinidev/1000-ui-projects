---
name: Oceanic Drift
colors:
  surface: '#f4fafd'
  surface-dim: '#d4dbdd'
  surface-bright: '#f4fafd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef5f7'
  surface-container: '#e8eff1'
  surface-container-high: '#e2e9ec'
  surface-container-highest: '#dde4e6'
  on-surface: '#161d1f'
  on-surface-variant: '#3e494a'
  inverse-surface: '#2b3234'
  inverse-on-surface: '#ebf2f4'
  outline: '#6f797a'
  outline-variant: '#bec8ca'
  surface-tint: '#006972'
  primary: '#00535b'
  on-primary: '#ffffff'
  primary-container: '#006d77'
  on-primary-container: '#9becf7'
  inverse-primary: '#82d3de'
  secondary: '#a43c12'
  on-secondary: '#ffffff'
  secondary-container: '#fe7e4f'
  on-secondary-container: '#6b1f00'
  tertiary: '#414e46'
  on-tertiary: '#ffffff'
  tertiary-container: '#58665e'
  on-tertiary-container: '#d4e3d9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#9ff0fb'
  primary-fixed-dim: '#82d3de'
  on-primary-fixed: '#001f23'
  on-primary-fixed-variant: '#004f56'
  secondary-fixed: '#ffdbcf'
  secondary-fixed-dim: '#ffb59c'
  on-secondary-fixed: '#380c00'
  on-secondary-fixed-variant: '#822800'
  tertiary-fixed: '#d7e6dc'
  tertiary-fixed-dim: '#bbcac0'
  on-tertiary-fixed: '#121e18'
  on-tertiary-fixed-variant: '#3c4a42'
  background: '#f4fafd'
  on-background: '#161d1f'
  surface-variant: '#dde4e6'
typography:
  h1-display:
    fontFamily: Epilogue
    fontSize: 4.5rem
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2-headline:
    fontFamily: Epilogue
    fontSize: 3rem
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3-title:
    fontFamily: Epilogue
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Plus Jakarta Sans
    fontSize: 0.875rem
    fontWeight: '700'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 2rem
  section-padding: 6rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
  stack-lg: 3rem
---

## Brand & Style
This design system captures the rhythmic, immersive essence of surf culture. The brand personality is adventurous yet serene, targeting a community that values the harmony between high-action sport and environmental tranquility. 

The aesthetic direction is a blend of **Glassmorphism** and **Minimalism**. It uses translucent layers to mimic the clarity of water and expansive whitespace to represent the horizon. Every interaction should feel fluid and unhurried, evoking the sensation of being offshore. High-impact photography serves as the structural foundation, with UI elements acting as elegant overlays that never obstruct the "view."

## Colors
The palette is rooted in the maritime environment. 
- **Deep Teal** is used for primary actions, navigation, and core branding, providing a sense of depth and reliability.
- **Vibrant Coral** serves as a high-energy accent for CTAs and notifications, reminiscent of tropical reefs.
- **Seafoam** acts as the primary background and secondary surface color, creating an airy, low-strain reading environment.
- **Neutral** tones are kept warm and dark for typography to ensure legibility against the soft Seafoam backdrops.

## Typography
The typography strategy contrasts the ruggedness of surfing with the softness of the lifestyle. 
- **Epilogue** is the voice of the brand: bold, geometric, and adventurous. Use it for large headlines and impactful statements. 
- **Plus Jakarta Sans** provides a welcoming, modern counterpoint for body copy and UI labels. Its slightly rounded terminals complement the organic shape language of the design system. 
Large line-heights are prioritized to maintain the "airy" feel of the interface.

## Layout & Spacing
The layout follows a **fluid grid** model with generous margins to evoke a sense of vastness. 
- Sections should use significant vertical padding (Section-Padding) to allow content to breathe. 
- Grid columns are flexible, but content should rarely feel "cramped." 
- Use asymmetrical placements for images to create a dynamic, organic flow that mimics the movement of waves rather than a rigid corporate structure.

## Elevation & Depth
Depth is achieved through **Glassmorphism** and **Ambient Shadows**. 
- **Surfaces:** Use semi-transparent Seafoam or White backgrounds with a high backdrop-blur (20px-30px) for navigation bars and overlays.
- **Shadows:** Avoid harsh blacks. Use extra-diffused shadows tinted with the Deep Teal color at very low opacity (5-10%) to create a "floating" effect.
- **Transitions:** Elements should fade and slide into place with "Ease-Out" curves, simulating the smooth motion of a swell.

## Shapes
The shape language is strictly **Rounded**. Sharp corners are avoided to maintain an organic, approachable feel. 
- Standard components use a 0.5rem radius.
- Large cards and immersive containers use a 1.5rem radius.
- Interactive elements like buttons may lean toward pill-shapes to emphasize their "squishy," tactile nature.

## Components
- **Buttons:** Primary buttons use a solid Coral fill with white text. Secondary buttons use a Deep Teal outline with a subtle seafoam hover state.
- **Cards:** Feature "Immersive Cards" with edge-to-edge photography and text overlays using the Glassmorphism style (blurred bottom-third).
- **Inputs:** Soft, filled backgrounds (Seafoam Light) rather than heavy borders. Focus states should use a subtle Deep Teal glow.
- **Chips:** Small, rounded tags used for categories (e.g., "Beginner," "Big Wave") with low-saturation Teal backgrounds.
- **Navigation:** A floating, blurred header that stays fixed to the top, giving the impression of looking through clear water.
- **Progress Indicators:** Use smooth, wave-like loading animations to maintain the brand’s fluid identity.