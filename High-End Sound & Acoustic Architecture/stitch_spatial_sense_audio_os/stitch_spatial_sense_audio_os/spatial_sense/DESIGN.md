---
name: Spatial-Sense
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c5c7c9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8f9194'
  outline-variant: '#44474a'
  surface-tint: '#c6c6c8'
  primary: '#ffffff'
  on-primary: '#2f3132'
  primary-container: '#e2e2e4'
  on-primary-container: '#636466'
  inverse-primary: '#5d5e60'
  secondary: '#bfc6db'
  on-secondary: '#293041'
  secondary-container: '#41495a'
  on-secondary-container: '#b1b8cd'
  tertiary: '#ffffff'
  on-tertiary: '#24304a'
  tertiary-container: '#d9e2ff'
  on-tertiary-container: '#586481'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e2e2e4'
  primary-fixed-dim: '#c6c6c8'
  on-primary-fixed: '#1a1c1d'
  on-primary-fixed-variant: '#454749'
  secondary-fixed: '#dbe2f8'
  secondary-fixed-dim: '#bfc6db'
  on-secondary-fixed: '#141c2b'
  on-secondary-fixed-variant: '#3f4758'
  tertiary-fixed: '#d9e2ff'
  tertiary-fixed-dim: '#bac6e7'
  on-tertiary-fixed: '#0e1b34'
  on-tertiary-fixed-variant: '#3b4662'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  display-lg:
    fontFamily: manrope
    fontSize: 48px
    fontWeight: '300'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: manrope
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: manrope
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
  headline-lg-mobile:
    fontFamily: manrope
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 64px
  margin-tablet: 40px
  margin-mobile: 24px
  card-gap: 24px
---

## Brand & Style
The design system is centered on "Acoustic Serenity"—a philosophy that prioritizes a calm, high-end sensory experience for home audio enthusiasts. The brand personality is sophisticated, precise, and ethereal. It targets a discerning audience that values both technical performance and domestic aesthetics.

The visual style is a refined **Glassmorphism**. It utilizes multi-layered translucency to mimic premium physical materials like polished acrylic and frosted crystal. By leaning into deep background blurs and silk-textured surfaces, the UI feels lightweight yet substantial, ensuring the digital interface complements the physical presence of high-end audio hardware.

## Colors
This design system utilizes a palette optimized for deep immersion and low eye strain in home environments. 

- **Backgrounds:** Deep Midnight Blue serves as the infinite canvas, providing high contrast for glassy elements.
- **Surfaces:** Frosted Glass is achieved through low-opacity white fills with high-saturation background blurs (30px–60px).
- **Typography & Iconography:** Silk White (#F9F9FB) provides a soft, non-piercing legibility that feels premium.
- **Accents:** High-quality gradients are reserved for active states, such as volume levels or playback progress, moving from deep ocean blues to ethereal cyans.

## Typography
The typography is driven by **manrope** for its balanced, modern geometric qualities which remain legible even against complex blurred backgrounds. For technical data and metadata labels (like bitrates or timestamps), **geist** is used to provide a precise, monospaced-adjacent aesthetic that reflects high-performance engineering.

Hierarchy is established through weight variation rather than color. Large display types use lighter weights (300) to feel airy, while functional labels use bolder weights (600) and increased letter spacing to ensure they remain distinct on frosted surfaces.

## Layout & Spacing
This design system employs a **Fluid Grid** with generous margins to evoke a sense of space and luxury. 

- **Desktop/OS:** A 12-column grid with 24px gutters. Content is often grouped into "zones" (Now Playing, Room Selection, Source) rather than a continuous feed.
- **Rhythm:** An 8px linear scale governs all padding and margins. 
- **Adaptation:** On smaller screens (tablets/remotes), the layout reflows from horizontal panes to vertical stacks, increasing the touch target areas for scrubbers and playback controls.

## Elevation & Depth
Depth in this design system is expressed through **Backdrop Blur** and **Inner Glows** rather than traditional drop shadows.

1.  **Base Layer:** The Deep Midnight background.
2.  **Surface Layer:** Glassy control cards with a 40px backdrop blur and a 1px Silk White inner border (10% opacity) to define edges.
3.  **Active Layer:** Elements currently in use (e.g., a selected room) gain a soft, cyan-tinted ambient outer shadow (20% opacity, 40px blur) to appear as if they are subtly emitting light onto the surface below.
4.  **Interactive Elements:** Buttons and sliders feature a subtle "specular highlight" on the top edge to simulate physical light hitting a glass edge.

## Shapes
The shape language is "Organic Geometric." Standard containers use a **1rem (16px)** corner radius to soften the technical nature of the OS. Larger "Immersive Visualization" windows may use **1.5rem (24px)** to feel more like furniture or architectural elements.

Interactive elements like play/pause toggles or small chips use a full pill-shape (rounded-full) to provide a clear affordance for touch and interaction, contrasting against the more structural card layouts.

## Components
- **Glassy Control Cards:** These are the primary containers. They feature a semi-transparent background, a 1px border, and a "sheen" gradient that moves subtly when the user interacts with the device.
- **High-Performance Scrubbers:** Seek bars and volume sliders utilize a thick, frosted track with a Silk White "thumb." The "active" portion of the track is filled with a vibrant Blue-to-Cyan gradient.
- **Immersive 3D Visualizations:** For frequency response or spatial audio mapping, use low-poly 3D meshes with glowing edges, rendered with a shallow depth of field to match the UI's blur-centric aesthetic.
- **Buttons:** Primary actions are solid Silk White with Midnight Blue text. Secondary actions are glass-filled with Silk White outlines.
- **Lists:** Audio tracks are displayed in clean rows with 1px frosted dividers. The "Active" track is indicated by a subtle glow behind the album art.
- **Inputs:** Search and settings fields use a darker, recessed glass effect to signify they are "hollow" and ready for input.