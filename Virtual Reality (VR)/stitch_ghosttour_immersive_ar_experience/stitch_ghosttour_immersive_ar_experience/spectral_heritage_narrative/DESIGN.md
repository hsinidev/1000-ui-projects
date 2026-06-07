---
name: Spectral Heritage Narrative
colors:
  surface: '#fff8ef'
  surface-dim: '#e3d9c1'
  surface-bright: '#fff8ef'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fdf3da'
  surface-container: '#f7edd4'
  surface-container-high: '#f1e8cf'
  surface-container-highest: '#ece2c9'
  on-surface: '#201b0c'
  on-surface-variant: '#554240'
  inverse-surface: '#35301f'
  inverse-on-surface: '#faf0d7'
  outline: '#89726f'
  outline-variant: '#dcc0bd'
  surface-tint: '#9d4139'
  primary: '#210000'
  on-primary: '#ffffff'
  primary-container: '#4a0404'
  on-primary-container: '#d26a5f'
  inverse-primary: '#ffb4aa'
  secondary: '#795900'
  on-secondary: '#ffffff'
  secondary-container: '#ffce60'
  on-secondary-container: '#755700'
  tertiary: '#0a0a0a'
  on-tertiary: '#ffffff'
  tertiary-container: '#212121'
  on-tertiary-container: '#898888'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#7e2b23'
  secondary-fixed: '#ffdf9f'
  secondary-fixed-dim: '#f0c053'
  on-secondary-fixed: '#261a00'
  on-secondary-fixed-variant: '#5b4300'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#fff8ef'
  on-background: '#201b0c'
  surface-variant: '#ece2c9'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 20px
    fontWeight: '600'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-padding: 24px
  element-gap: 16px
  ar-safe-zone: 80px
---

## Brand & Style

The design system is engineered to bridge the gap between the physical present and the spectral past. It evokes the feeling of a scholarly explorer’s journal—mysterious, authoritative, and deeply atmospheric. The brand personality is "The Sophisticated Ghost-Hunter": intellectual but prepared for the supernatural.

The chosen style is **Tactile / Skeuomorphic** with a modern editorial backbone. Unlike traditional skeuomorphism that mimics glossy plastic, this design system focuses on organic, historical textures: aged paper, cold metal accents, and deep ink. It prioritizes immersion by ensuring that UI elements feel like artifacts discovered on-site rather than digital overlays, maintaining a "digital antique" aesthetic that respects the AR-first nature of the experience.

## Colors

The palette is rooted in historical gravitas. **Parchment (#F2E8CF)** serves as the primary canvas, replacing clinical whites to reduce eye strain during outdoor AR usage and to provide a warm, organic base. **Deep Burgundy (#4A0404)** is used for primary actions and narrative headings, mimicking the color of dried oxblood or wax seals. 

**Gold (#BC9128)** is reserved for interactive "discoveries," high-level highlights, and iconography, functioning as a beacon within the atmospheric environment. A tertiary charcoal is utilized for technical UI elements that need to recede, ensuring the focus remains on the historical content.

## Typography

The typographic system relies on a high-contrast pairing to distinguish between "Lore" and "Utility." 

**Noto Serif** is the voice of history. It is used for all narrative content, location names, and character quotes. Its classic proportions provide the necessary "literary" feel. **Manrope** provides the functional counterpoint. As a modern sans-serif with excellent legibility, it handles the technical aspects of the AR interface, map coordinates, and system settings. To maintain the nostalgic feel, all utility labels use increased letter-spacing and uppercase styling to mimic early 20th-century cataloging.

## Elevation & Depth

Hierarchy is established through **Physical Layering** rather than digital shadows. Surfaces use a stacked-paper logic:
1.  **The World (Base):** The live AR camera feed.
2.  **The Scrim:** A subtle, burgundy-tinted gradient overlay that darkens the bottom of the feed to ensure text legibility.
3.  **The Artifact (Floating):** Parchment-textured cards that appear to float above the world. These use very soft, wide-diffusion shadows (#4A0404 at 15% opacity) to feel heavy and grounded rather than airy.
4.  **The Detail (Inset):** Buttons and input fields use subtle inner-shadows to appear "pressed" or "embossed" into the paper surfaces.

## Shapes

The shape language avoids the "perfect" geometry of modern tech. A **Soft (0.25rem)** roundedness is applied to all primary containers to mimic the natural wear of old cardstock. 

To enhance the immersive quality, secondary containers and buttons should utilize a "deckle edge" or slightly irregular border-image where possible, preventing the UI from looking like a standard mobile app. Horizontal rules should appear as thin, hand-drawn ink lines or gold foil dividers with tapered ends.

## Components

**Buttons:** Primary actions are filled in Deep Burgundy with Gold serif text. Secondary actions use a Gold border (2px) with an "ink-bleed" hover effect. 

**Parchment Cards:** The cornerstone of the design system. These must feature a subtle bitmap texture overlay of aged fiber. Edges are slightly darkened (vignetted) to suggest age.

**AR Wayfinders:** Floating markers in the 3D space should use the Gold palette with a "pulsing" inner glow, appearing like a flickering gaslight or a ghostly ember.

**Lists & Chronologies:** Use Noto Serif for titles and Manrope for metadata. Items are separated by subtle parchment-toned dividers.

**Navigation:** A bottom-anchored "Journal" bar using gold-toned iconography. The center button (AR Trigger) is always distinguished by a gold foil circular border.