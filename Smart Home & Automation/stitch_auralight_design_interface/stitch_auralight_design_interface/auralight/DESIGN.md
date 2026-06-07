---
name: AuraLight
colors:
  surface: '#18120b'
  surface-dim: '#18120b'
  surface-bright: '#40382f'
  surface-container-lowest: '#130d07'
  surface-container-low: '#211a13'
  surface-container: '#251e17'
  surface-container-high: '#302921'
  surface-container-highest: '#3b332b'
  on-surface: '#eee0d4'
  on-surface-variant: '#d6c3b0'
  inverse-surface: '#eee0d4'
  inverse-on-surface: '#372f27'
  outline: '#9f8e7c'
  outline-variant: '#524535'
  surface-tint: '#ffb95a'
  primary: '#ffd7a9'
  on-primary: '#462a00'
  primary-container: '#ffb347'
  on-primary-container: '#704700'
  inverse-primary: '#845400'
  secondary: '#c6c4df'
  on-secondary: '#2f2e43'
  secondary-container: '#47475d'
  on-secondary-container: '#b8b6d0'
  tertiary: '#dddedf'
  on-tertiary: '#2e3132'
  tertiary-container: '#c1c2c3'
  on-tertiary-container: '#4d5051'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffddb6'
  primary-fixed-dim: '#ffb95a'
  on-primary-fixed: '#2a1800'
  on-primary-fixed-variant: '#643f00'
  secondary-fixed: '#e2e0fc'
  secondary-fixed-dim: '#c6c4df'
  on-secondary-fixed: '#1a1a2e'
  on-secondary-fixed-variant: '#45455b'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#18120b'
  on-background: '#eee0d4'
  surface-variant: '#3b332b'
typography:
  display:
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
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 40px
  gutter: 24px
  section-gap: 80px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to evoke a sense of quiet luxury, precision, and architectural mastery. It targets discerning homeowners and professional architects who view lighting as a fundamental building material rather than a mere utility. The interface must feel like an extension of the physical environment—immersive, responsive, and sophisticated.

This design system utilizes a **Glassmorphic Minimalism** style. By combining deep, atmospheric backgrounds with translucent, frosted-glass layers, the UI mimics the way light interacts with physical surfaces. Soft, directional glows and expansive white space (negative space) ensure that the high-resolution architectural photography remains the focal point, while the controls feel integrated into the illuminated space.

## Colors

The palette is anchored by **Deep Indigo**, serving as a cinematic void that allows the interface to recede, emphasizing the architectural subjects. **Amber** is used sparingly but powerfully; it represents the "warmth of light" and is reserved exclusively for active states, primary actions, and light intensity indicators. 

**Soft White** provides a crisp, legible contrast against the dark background without being as harsh as pure white. To maintain the "atmospheric" aesthetic, gradients should transition from Amber to transparent to simulate light diffusion, rather than solid blocks of color. Use low-opacity overlays for container backgrounds to preserve the depth of the underlying imagery.

## Typography

This design system utilizes **Manrope** for headlines to provide a refined, modern architectural feel with its geometric yet warm character. **Inter** is used for body text and functional labels to ensure maximum clarity and a systematic, technical precision.

Generous line heights and increased letter-spacing in the "label-caps" style are critical to maintaining the high-end editorial feel. Display text should use a lighter weight (300) to feel elegant and airy, while functional UI elements use medium weights for immediate recognition against complex photographic backgrounds.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid** model. Large-scale desktop views utilize a centered 12-column grid with a maximum content width of 1440px to ensure photography remains immersive but controlled. On smaller viewports, a fluid grid with generous side margins (40px+) is used to maintain a premium "gallery" feel.

The rhythm is based on an 8px base unit. To achieve the "immersive" aesthetic, vertical spacing between major architectural sections should be significantly larger than standard SaaS products, allowing each room or lighting scene to breathe. Content should be grouped logically using "stacks" with consistent gaps to maintain a clear hierarchy.

## Elevation & Depth

Hierarchy in the design system is achieved through **Backdrop Blurs** and **Ambient Light Tints** rather than traditional black shadows. 

1.  **Base Layer:** The Deep Indigo background or full-bleed photography.
2.  **Surface Layer:** A 5% opacity Soft White surface with a 20px - 40px backdrop blur (Glassmorphism). This layer should have a 1px thin border at 10% opacity to define its edges.
3.  **Active Elevation:** When an element is selected or active, it emits an Amber glow (`box-shadow: 0 0 20px rgba(255, 179, 71, 0.3)`). 

This creates a sense of "illuminated depth," where the UI feels like it is floating within the light of the room.

## Shapes

The design system employs a **Rounded** (Level 2) shape language. Standard components like buttons and input fields use a 0.5rem (8px) corner radius. For larger containers and cards, a `rounded-xl` (1.5rem / 24px) radius is preferred to create a soft, welcoming architectural feel that contrasts with the sharp lines of modern photography.

Interactive elements should transition their corner radius slightly on hover (e.g., becoming slightly more rounded) to simulate a "softening" effect as if the light is hitting them directly.

## Components

### Buttons
Primary buttons use the Amber color with dark text. They should have a subtle outer glow that intensifies on hover. Secondary buttons should be "Ghost" style with a Soft White 1px border and a backdrop blur.

### Chips & Tags
Used for room labels or light modes (e.g., "Cinema," "Evening"). These should be semi-transparent glass pills. When active, the background fills with a low-opacity Amber and the text turns Amber.

### Inputs & Sliders
Sliders are critical for dimming controls. The track should be a thin Soft White line, while the "thumb" is a glowing Amber circle. As the slider increases, the Amber glow should expand to represent light intensity.

### Cards
Cards are the primary container for room snapshots. They must use high-resolution photography with a subtle gradient overlay at the bottom to ensure the Soft White typography is legible. 

### Scene Controller
A bespoke component featuring a radial "Light Diffusion" picker, allowing users to drag their finger through a gradient of Amber to Soft White to adjust color temperature.

### Lists
Lists should be expansive, using `stack-md` spacing between items. Item separators should be low-opacity (5%) Soft White lines that do not touch the container edges.