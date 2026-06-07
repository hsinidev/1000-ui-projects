---
name: Aura-Light
colors:
  surface: '#08122d'
  surface-dim: '#08122d'
  surface-bright: '#2f3855'
  surface-container-lowest: '#030c28'
  surface-container-low: '#111a36'
  surface-container: '#151e3a'
  surface-container-high: '#202945'
  surface-container-highest: '#2b3450'
  on-surface: '#dbe1ff'
  on-surface-variant: '#d5c4b2'
  inverse-surface: '#dbe1ff'
  inverse-on-surface: '#262f4c'
  outline: '#9d8e7e'
  outline-variant: '#504537'
  surface-tint: '#fabb65'
  primary: '#ffe2c2'
  on-primary: '#462b00'
  primary-container: '#ffbf69'
  on-primary-container: '#774c00'
  inverse-primary: '#835401'
  secondary: '#bec5e5'
  on-secondary: '#282f49'
  secondary-container: '#414863'
  on-secondary-container: '#b0b7d7'
  tertiary: '#e7e7e7'
  on-tertiary: '#2f3131'
  tertiary-container: '#cacbcb'
  on-tertiary-container: '#545656'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddb5'
  primary-fixed-dim: '#fabb65'
  on-primary-fixed: '#2a1800'
  on-primary-fixed-variant: '#643f00'
  secondary-fixed: '#dbe1ff'
  secondary-fixed-dim: '#bec5e5'
  on-secondary-fixed: '#131a33'
  on-secondary-fixed-variant: '#3e4660'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#08122d'
  on-background: '#dbe1ff'
  surface-variant: '#2b3450'
typography:
  headline-xl:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 0.5rem
  sm: 1rem
  md: 2rem
  lg: 4rem
  xl: 8rem
  gutter: 24px
  margin-safe: 32px
---

## Brand & Style

This design system is built on the concept of "Illuminated Sophistication." It targets a discerning audience that values wellness, ambiance, and the intersection of technology and comfort. The personality is serene yet commanding, prioritizing a human-centric approach to environmental control.

The aesthetic direction is a refined blend of **Minimalism** and **Glassmorphism**. By leaning into deep, atmospheric backgrounds, the UI allows "light" to become a functional and decorative material. The interface does not merely control light; it mimics its properties through soft diffusions, high-end translucency, and a tactile sense of depth. The emotional response should be one of calm, luxury, and intuitive mastery over one’s surroundings.

## Colors

The palette is anchored by the deep, infinite depth of **Midnight Blue**, serving as the canvas for all interactions. This dark mode foundation ensures that the primary accent, **Warm Amber**, resonates with the intensity of a physical light source.

- **Primary (Warm Amber):** Used for active states, light intensity indicators, and high-priority interactions. It should often be accompanied by a CSS `box-shadow` or `filter: drop-shadow` to simulate a glow.
- **Secondary (Midnight Blue):** The primary background color. It provides the "atmosphere" required for the glass elements to appear luminous.
- **Tertiary (Silk White):** Reserved for high-contrast typography and subtle border highlights on glass containers.
- **Neutrals:** A range of desaturated blues are used for secondary surfaces and inactive states, ensuring the UI maintains its cool, nocturnal character.

## Typography

This design system utilizes **Manrope** for its modern, geometric construction and balanced proportions. The type scale is designed to feel airy and premium, with a preference for lighter weights in large displays to convey elegance.

Headlines should be treated as editorial elements, often using "Silk White" with a very subtle `text-shadow` in high-intensity scenarios. Labels are always uppercase with increased letter spacing to provide a technical, high-end appliance feel. Body text maintains high legibility with generous line heights, preventing the interface from feeling cluttered amidst the atmospheric effects.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop and a **Fluid Grid** for mobile, centered around an 8px rhythmic unit. To achieve the "Atmospheric" aesthetic, the design system mandates significantly more whitespace than a standard utility app.

Margins and paddings should be "generous," allowing glow effects and box shadows to bleed naturally without overlapping adjacent content. Components are spaced to feel like individual "islands of light" within the dark canvas. Large-scale layouts should utilize a 12-column grid with wide 24px gutters to reinforce the premium, expansive feel.

## Elevation & Depth

Depth is articulated through **Glassmorphism** and light-based hierarchy rather than traditional shadows.

1.  **Base Layer:** The solid Midnight Blue background.
2.  **Mantle Layer:** Semi-transparent containers with a `backdrop-filter: blur(20px)` and a subtle 1px border using a low-opacity Silk White.
3.  **Luminous Layer:** Active elements that emit a "glow" using `box-shadow: 0 0 30px rgba(255, 191, 105, 0.4)`.
4.  **Floating Layer:** High-priority overlays or modals that use a more intense blur and a slightly lighter fill to appear physically closer to the user.

Tactility is achieved by using subtle inner shadows on "pressed" states, giving the impression of high-quality, frosted glass buttons being physically engaged.

## Shapes

The shape language is consistently **Rounded**. A 0.5rem (8px) base radius is applied to standard components, while larger cards and containers utilize 1rem (16px) to 1.5rem (24px). This softness contrasts with the technical nature of lighting control, making the system feel approachable and human-centric. Circles are used exclusively for light-source icons and toggle handles to represent the radial nature of light emission.

## Components

- **Buttons:** Primary buttons use a solid Warm Amber fill with a Silk White or Midnight Blue label. On hover, they emit a soft amber glow. Secondary buttons are "Glass" style: transparent with a Silk White border and high-blur backdrop.
- **Glass Cards:** The primary container. These feature a 20% opacity Silk White fill, 40px backdrop blur, and a 1px border. They should have generous internal padding (32px+).
- **Intensity Sliders:** Horizontal or radial tracks. The "filled" portion of the track should glow in Warm Amber, while the handle is a tactile, frosted glass circle.
- **Status Chips:** Small, pill-shaped elements with low-opacity Amber backgrounds and high-contrast text to indicate "Active" or "Scheduled" states.
- **Light Nodes:** Unique to this design system, these are interactive circular icons representing individual lamps. They vary in glow intensity and "warmth" (color temperature) based on the actual state of the physical light.
- **Inputs:** Minimalist fields with only a bottom border that illuminates when focused. The placeholder text should be Silk White at 50% opacity.