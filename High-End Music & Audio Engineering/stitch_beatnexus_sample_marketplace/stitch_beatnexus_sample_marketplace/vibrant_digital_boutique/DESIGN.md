---
name: Vibrant-Digital Boutique
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#e5bcc5'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#ac878f'
  outline-variant: '#5c3f46'
  surface-tint: '#ffb1c4'
  primary: '#ffb1c4'
  on-primary: '#65002e'
  primary-container: '#ff4a8d'
  on-primary-container: '#590028'
  inverse-primary: '#ba005b'
  secondary: '#abc7ff'
  on-secondary: '#002f66'
  secondary-container: '#448fff'
  on-secondary-container: '#002859'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a29'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffd9e1'
  primary-fixed-dim: '#ffb1c4'
  on-primary-fixed: '#3f001a'
  on-primary-fixed-variant: '#8f0044'
  secondary-fixed: '#d7e2ff'
  secondary-fixed-dim: '#abc7ff'
  on-secondary-fixed: '#001b3f'
  on-secondary-fixed-variant: '#004590'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  h1:
    fontFamily: Epilogue
    fontSize: 80px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  h2:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h3:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Epilogue
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Epilogue
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  mono-label:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
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
  xl: 48px
  xxl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is engineered for a premium, high-octane digital marketplace. The brand personality is aggressive, futuristic, and unapologetically digital, targeting elite music producers who seek cutting-edge sounds. 

The design style is a synthesis of **High-Contrast Bold** and **Glassmorphism**, set against a deep, dark canvas. It utilizes "Vibrant-Digital" aesthetics—characterized by light-emitting elements, overlapping layout structures that suggest movement, and a "cyber-boutique" atmosphere. The UI should evoke the feeling of a high-end hardware synthesizer or a futuristic DAW interface: tactile, glowing, and high-performance.

## Colors

The palette is anchored by **Matte Black (#121212)** to provide a sophisticated, low-reflectance base that allows vibrant accents to pop. **Hot Pink (#FF007F)** serves as the primary action color, used for high-priority triggers and branding. **Electric Blue (#007FFF)** acts as the secondary color, used for technical highlights, secondary actions, and system feedback.

The color system relies heavily on "Light-on-Dark" logic. Vibrancy is achieved not just through flat hex codes, but through "glow" states—using the primary and secondary colors at varying opacities to create atmospheric depth.

## Typography

This design system utilizes **Epilogue** for headings and body copy to provide an editorial, high-contrast feel that leans into the "Boutique" aspect of the product. Headlines should be set with tight leading and negative letter-spacing to create a dense, "heavyweight" visual impact.

For technical metadata—such as BPM, Key, Scale, and File Size—**Space Grotesk** is used. Its geometric, monospaced qualities provide the necessary "scientific" contrast against the expressive headlines, ensuring technical data is legible at a glance.

## Layout & Spacing

The layout follows a **12-column fluid grid** with generous margins. To achieve the "overlapping" aesthetic, elements should frequently break the grid using absolute positioning or negative margins. 

The spacing rhythm is built on a 4px base unit. Use `xxl` (80px) for section vertical padding to emphasize the premium, high-end nature of the content. Overlapping elements should maintain a minimum of `md` (16px) offset to ensure the layering is intentional and distinct.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Glow Tiers** rather than traditional drop shadows.

1.  **Base Layer:** Matte Black (#121212) solid background.
2.  **Surface Layer:** Slightly elevated containers (#1A1A1A) with 1px solid borders in low-opacity grey.
3.  **Glass Layer:** 20% opacity white with a 16px backdrop-blur, used for floating navigation or overlay panels.
4.  **Neon Tier:** Elements that require maximum attention use 1px solid borders of Hot Pink or Electric Blue, accompanied by a `0px 0px 15px` outer glow of the same color.

Overlapping elements must use a 1px "Light Leak" (a top-border highlight) to separate layers effectively.

## Shapes

The design system uses **Soft (0.25rem)** roundedness to maintain a technical, sharp-edged feel while avoiding the harshness of pure 90-degree angles. This subtle rounding suggests precision-machined hardware.

Interactive components like buttons and tags use the `rounded-lg` (0.5rem) setting for a slightly more approachable tactile feel, while large card containers and layout sections remain at the base `rounded` (0.25rem) or sharp for a more structural appearance.

## Components

- **Neon-Glow Buttons:** Primary buttons are solid Hot Pink with white text. On hover, they emit a 15px pink outer glow. Secondary buttons use an Electric Blue 1px border with a transparent center.
- **Dark Card Grids:** Product cards use the Matte Black base. On hover, the border transitions from neutral to a vibrant Electric Blue glow, and the background image slightly scales up.
- **Glassmorphism Accents:** Audio players and filter sidebars use a semi-transparent dark glass effect with `backdrop-filter: blur(20px)`.
- **Technical Chips:** BPM and Scale indicators use a monospaced font inside a small, dark grey capsule with high-contrast white text.
- **Input Fields:** Minimalist dark fields with a 1px bottom border. Upon focus, the border animates to Hot Pink with a subtle glow.
- **Waveform Displays:** Rendered in Electric Blue with a secondary "ghost" waveform in Hot Pink to indicate selection or playhead position.