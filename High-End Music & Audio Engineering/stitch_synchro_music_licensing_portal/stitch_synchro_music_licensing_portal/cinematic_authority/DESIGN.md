---
name: Cinematic Authority
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c5c6d2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e909c'
  outline-variant: '#444650'
  surface-tint: '#b3c5ff'
  primary: '#b3c5ff'
  on-primary: '#0d2c6e'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#435b9f'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#272929'
  on-tertiary-container: '#8f9090'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
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
    lineHeight: '1'
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
  margin: 48px
  section-gap: 80px
---

## Brand & Style

This design system establishes a premium, "Cinematic-Corporate" identity tailored for high-stakes music licensing. The brand personality is authoritative, reliable, and deeply rooted in the world of film and television. It bridges the gap between creative artistry and executive professionalism.

The visual style utilizes a high-contrast foundation, combining the depth of full-bleed cinematic imagery with the structural clarity of a modern corporate interface. Glassmorphism is used strategically to create layers of information that feel "projected" onto the screen, echoing the medium of film. The result is an environment that feels expensive, exclusive, and operationally precise.

## Colors

The palette is anchored by **Royal Blue**, signaling trust and institutional strength. **Silver** is used as a metallic accent to represent the "silver screen" and premium hardware, while **White** provides high-contrast legibility against dark, cinematic backdrops.

The system defaults to a dark mode to allow imagery to pop and to mimic the atmosphere of a screening room. Royal Blue is used for primary actions and brand presence, while Silver serves as a sophisticated secondary color for borders, iconography, and subtle UI flourishes.

## Typography

The design system utilizes **Inter** across all levels to achieve a sharp, systematic, and technical aesthetic. Headlines are set with tight tracking and heavy weights to command attention, mirroring the impact of film title cards. 

Body text prioritizes clear line heights for maximum readability during complex contract reviews or metadata browsing. Label styles use uppercase transformation and increased letter spacing to provide a structural, navigational feel that contrasts with the fluid nature of cinematic backgrounds.

## Layout & Spacing

This design system employs a **Fixed Grid** model to ensure content feels curated and intentional rather than sprawling. A 12-column grid is used for desktop layouts, providing a robust framework for complex data and media displays.

Spacing is generous to evoke a sense of "luxury" and "prestige." Large vertical gaps (Section-Gaps) separate major content blocks, ensuring the cinematic background imagery has room to breathe. Components are spaced using an 8px base unit to maintain mathematical rhythm across the interface.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional drop shadows. Surfaces are treated as semi-transparent panels with a "frosted" backdrop blur (minimum 12px) to maintain legibility over moving or high-contrast images.

- **Surface 0:** Full-bleed cinematic background image or video.
- **Surface 1:** Glass containers with a 1px Silver (#C0C0C0) border at 20% opacity.
- **Surface 2:** Active or elevated states using a 1px White border at 40% opacity to "lift" the element closer to the viewer.
- **Overlays:** Darkened scrims are applied to backgrounds (30-50% black) to ensure white typography meets accessibility standards.

## Shapes

To maintain the "Sharp" and "Corporate" requirements, the shape language uses a subtle **Soft (0.25rem)** corner radius. This prevents the UI from feeling dated or aggressive while avoiding the overly "playful" nature of highly rounded systems.

Interactive elements like buttons and input fields follow this 4px (0.25rem) standard. Larger cards or sections may scale up to 8px (0.5rem) to maintain visual proportion, but never more. Lines are crisp, and borders are consistently thin (1px) to emphasize precision.

## Components

### Buttons
Primary buttons are solid **Royal Blue** with white text. Secondary buttons use a **Silver** ghost style (1px border) with white text. Hover states should increase the opacity of the glass background or the intensity of the blue.

### Cards
Cards are the primary vehicle for "Glassmorphism." They feature a semi-transparent dark background, a 1px silver stroke, and a backdrop-filter blur. For film/TV assets, cards should feature a 16:9 image aspect ratio.

### Input Fields
Inputs are dark and semi-transparent with a 1px silver bottom border. On focus, the border transitions to Royal Blue with a subtle glow. Label text sits strictly above the input in the "label-sm" style.

### Music Player & Waveforms
As a music agency, the player is a critical component. It should appear as a pinned glass bar at the bottom of the screen. Waveforms are rendered in Silver, turning Royal Blue as they are played.

### Chips & Tags
Used for "Genre" or "Mood" metadata. These are small, pill-shaped containers with a 1px Silver border and no fill, ensuring they do not compete with primary actions.