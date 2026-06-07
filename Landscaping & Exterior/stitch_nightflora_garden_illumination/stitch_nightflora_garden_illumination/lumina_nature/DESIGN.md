---
name: Lumina Nature
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#d5c4ab'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#9e8f78'
  outline-variant: '#514532'
  surface-tint: '#ffba20'
  primary: '#ffdca1'
  on-primary: '#412d00'
  primary-container: '#ffb800'
  on-primary-container: '#6b4c00'
  inverse-primary: '#7c5800'
  secondary: '#bec6e0'
  on-secondary: '#283044'
  secondary-container: '#3f465c'
  on-secondary-container: '#adb4ce'
  tertiary: '#d6e1f9'
  on-tertiary: '#263143'
  tertiary-container: '#bac5dd'
  on-tertiary-container: '#475265'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdea8'
  primary-fixed-dim: '#ffba20'
  on-primary-fixed: '#271900'
  on-primary-fixed-variant: '#5e4200'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#d8e3fb'
  tertiary-fixed-dim: '#bcc7de'
  on-tertiary-fixed: '#111c2d'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 4rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 2.5rem
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 1.75rem
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Manrope
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin-page: 64px
  stack-sm: 12px
  stack-md: 32px
  stack-lg: 80px
---

## Brand & Style
This design system centers on the emotional transition between natural dusk and engineered brilliance. The brand personality is authoritative yet evocative, targeting high-end architects, landscape designers, and luxury homeowners who view lighting as a structural material rather than a utility. 

The visual style utilizes a **Glassmorphic-Atmospheric** hybrid. It relies on deep layers of transparency and soft-focus "glow" filters to simulate the behavior of light in physical space. High-resolution photography featuring dramatic architectural shadows and warm focal points is the primary visual driver. The aesthetic evokes a sense of quiet prestige and technical mastery over the environment.

## Colors
The palette is rooted in the "Blue Hour"—that transition from sunset to deep night. 

- **Primary (Golden Amber):** Used exclusively for interactive "glow" states and focal points. It represents the light source itself.
- **Secondary/Tertiary (Midnight & Charcoal):** These define the environment. Midnight blue provides the atmospheric backdrop, while charcoal provides structural depth.
- **Day-to-Night Logic:** 
    - **Day State:** Backgrounds use semi-opaque charcoal (#1E293B at 80% opacity) with subtle amber accents.
    - **Night State:** Backgrounds shift to pure midnight (#0F172A). Contrast ratios are increased, and the Amber (#FFB800) utilizes a `drop-shadow` filter rather than a standard `box-shadow` to create a realistic light bloom effect.

## Typography
The typographic hierarchy creates a dialogue between tradition and modernity. **Noto Serif** is used for headlines to provide a literary, premium editorial feel; it should be set with tighter letter-spacing in larger sizes to feel "bespoke." 

**Manrope** provides a highly legible, clean counterpoint for technical specifications and body copy. Navigation and small labels use Manrope in uppercase with generous letter spacing to maintain clarity against dark, atmospheric backgrounds.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model (12 columns) for desktop, centered within a wide viewport to emphasize a cinematic experience. 

Spacing is intentionally expansive. Large "Stack" increments (80px+) are used between sections to allow photography to breathe. Content components follow an 8px rhythmic grid, but layout-level margins are kept wide (64px) to avoid visual clutter and maintain a "gallery" feel.

## Elevation & Depth
Depth in this design system is conveyed through **Light Emission** rather than physical stacking. 

1. **Ambient Layer:** The base midnight blue background.
2. **Atmospheric Layer:** Uses backdrop-blur (12px to 20px) on charcoal surfaces to create a "frosted glass" effect, simulating light passing through mist.
3. **Emission Layer:** Interactive elements use a primary glow (`box-shadow: 0 0 15px #FFB80066`). In "Night Mode," this is enhanced with a `filter: drop-shadow(0 0 8px #FFB800)` to create a more intense, blurred radiance that bleeds into surrounding elements.

## Shapes
The shape language is **Soft (0.25rem)**. This subtle rounding prevents the UI from feeling overly aggressive or digital, mimicking the softened edges of architectural stone and outdoor fixtures under artificial light.

Buttons and small containers use a standard 4px radius. Larger image containers and "Night Mode" feature cards use a slightly more pronounced 8px (rounded-lg) to accommodate the soft-glow shadows that bleed from their edges.

## Components
- **Buttons:** Primary buttons are charcoal with a thin golden border. On hover, they transition to a solid golden fill with a diffuse `box-shadow` glow.
- **Chips:** Used for "Fixture Type" or "Kelvin Rating," these are pill-shaped with 1px semi-transparent borders.
- **Cards:** Feature high-resolution architectural shots as backgrounds with a bottom-aligned text gradient. The gradient must transition from transparent to #0F172A to ensure text legibility.
- **Input Fields:** Minimalist under-line style or subtle outlined boxes with #FFFFFF20 borders. Focus state triggers a golden bottom border and a subtle amber outer glow.
- **Day/Night Toggle:** A prominent, stylized switch that changes the global CSS variables for contrast and glow intensity.
- **Light Intensity Slider:** A custom range input that increases the brightness and blur radius of the amber accent color throughout the page.