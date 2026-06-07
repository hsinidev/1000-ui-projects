---
name: Zen Atmospheric Wellness
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cfc4c5'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#988e90'
  outline-variant: '#4c4546'
  surface-tint: '#c6c6c6'
  primary: '#c6c6c6'
  on-primary: '#303030'
  primary-container: '#000000'
  on-primary-container: '#757575'
  inverse-primary: '#5e5e5e'
  secondary: '#f4bb92'
  on-secondary: '#4a280a'
  secondary-container: '#653d1e'
  on-secondary-container: '#e1aa82'
  tertiary: '#c4c7ca'
  on-tertiary: '#2d3134'
  tertiary-container: '#000000'
  on-tertiary-container: '#737579'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#ffdcc5'
  secondary-fixed-dim: '#f4bb92'
  on-secondary-fixed: '#301400'
  on-secondary-fixed-variant: '#653d1e'
  tertiary-fixed: '#e0e2e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1f'
  on-tertiary-fixed-variant: '#44474a'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  h1:
    fontFamily: Playfair Display
    fontSize: 4.5rem
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Playfair Display
    fontSize: 3rem
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Playfair Display
    fontSize: 2rem
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.7'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.2em
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
  gutter: 32px
  margin-edge: 64px
  section-gap: 160px
---

## Brand & Style

The brand personality of this design system is defined by quiet luxury, meditative stillness, and an uncompromising focus on high-end wellness. It targets a discerning audience seeking an escape from digital noise, emphasizing the transition from the chaotic world to the grounded, elemental experience of steam, wood, and stone.

The visual style is a fusion of **Minimalism** and **Tactile Minimalism**. It utilizes heavy whitespace—referred to here as "Ma" or the space between—to create a sense of breathing room. Atmospheric depth is achieved through misty textures and soft-glow heat effects that mimic the appearance of light diffusing through steam. High-performance cinematic video backgrounds of mountain landscapes serve as the foundational layer, ensuring the digital interface feels like a window to a remote destination rather than a complex tool.

## Colors

The palette is rooted in the elemental materials of a high-end sauna: scorched earth, organic timber, and rising steam. 

- **Deep Black (#000000):** Used for the primary canvas to create an immersive, void-like atmosphere where focus is singular.
- **Warm Wood (#8B5E3C):** Reserved for primary actions and grounding structural elements, providing a tactile warmth against the cooler tones.
- **Steam Grey (#E5E7EB):** Utilized for primary typography and translucent overlays, creating the "mist" effect.

This design system defaults to **dark mode** to enhance the "soft-glow" heat effects and maintain a sense of nocturnal tranquility. Accent glows should utilize a low-opacity radial gradient of Warm Wood to simulate embers or radiant heat.

## Typography

The typographic hierarchy relies on the tension between the romantic, high-contrast **Playfair Display** and the utilitarian precision of **Inter**. 

Headlines must be treated as editorial elements, often center-aligned with generous vertical margins. **Playfair Display** should be used sparingly for large, evocative statements. Body copy leverages **Inter** for maximum legibility against photographic or video backgrounds. Labels and small metadata should always use the `label-caps` style with increased letter spacing to evoke a sense of premium architectural signage.

## Layout & Spacing

This design system utilizes a **fixed grid** layout centered on a 12-column system. To reinforce the luxury narrative, margins and gutters are significantly wider than industry standards. 

The spacing rhythm follows a strict 8px base unit, but emphasizes large "Section Gaps" (160px+) to ensure that no two content blocks compete for the user's attention. Layouts should favor asymmetrical compositions to mimic the organic flow of nature, with content occasionally "floating" over video backgrounds to maintain a sense of depth and lightness.

## Elevation & Depth

Depth in this design system is not conveyed through shadows, but through **Backdrop Blurs** and **Luminance**. 

1.  **Misty Layers:** Surfaces use the Steam Grey color at 5%–10% opacity with a high background blur (20px–40px). This creates a "frosted glass" effect that feels like condensation on a window.
2.  **Soft-Glow Heat:** Active states or high-priority focal points use a soft, inner-glow (box-shadow: inset) using the Warm Wood color at very low opacity. 
3.  **Z-Axis:** Video backgrounds sit at the lowest level (Z-0). Content containers sit at Z-10. Navigation and modal overlays sit at Z-20, utilizing a darker, more opaque blur to focus the user’s gaze.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding of corners bridges the gap between the sharp, precision-cut stone of modern architecture and the organic softening of natural mountain elements. 

- UI containers and cards should use `rounded-sm`.
- Form inputs and smaller interactive components use `rounded-sm`.
- Large buttons may occasionally use a 0px (Sharp) radius when they are intended to look like structural monoliths, but the system standard remains Soft.

## Components

- **Buttons:** Primary buttons are solid Warm Wood with Deep Black text. Secondary buttons are "Ghost" style with a Steam Grey border (0.5px) and a subtle backdrop blur.
- **Cards:** Defined by their lack of visible borders. They use a "Misty Layer" background (low-opacity Steam Grey with backdrop-blur) to separate themselves from the video background.
- **Inputs:** Minimalist bottom-border only. On focus, the border transitions from Steam Grey to Warm Wood with a faint outer glow mimicking heat.
- **Navigation:** A floating, transparent header that increases in blur-density upon scroll. Links use `label-caps` typography.
- **Chips/Badges:** Small, pill-shaped elements with high transparency and Steam Grey text, used for wellness tags (e.g., "4000m Altitude").
- **Video Player:** Integrated seamlessly into the background with no visible frame, featuring controls that only appear on hover to maintain the "Zen" aesthetic.