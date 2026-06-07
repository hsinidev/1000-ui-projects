---
name: Aero-Desk
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#43474e'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#476083'
  primary: '#000613'
  on-primary: '#ffffff'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#afc8f0'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#040607'
  on-tertiary: '#ffffff'
  tertiary-container: '#1c1f20'
  on-tertiary-container: '#848688'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Montserrat
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Montserrat
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Montserrat
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.15em
  interactive-sm:
    fontFamily: Montserrat
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-edge: 48px
  stack-xs: 4px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
  stack-xl: 80px
---

## Brand & Style
The design system embodies the "Sky-Sleek" philosophy: a fusion of high-altitude tranquility and high-performance precision. Targeted at ultra-high-net-worth individuals and elite aviation operators, the aesthetic must evoke immediate trust, exclusivity, and effortless control.

The style is **Luxury Minimalism** enhanced by **Glassmorphism**. It utilizes expansive white space to suggest the openness of the sky, grounded by the authoritative weight of deep navy. Visual interest is driven by metallic accents and light-refractive surfaces rather than heavy ornamentation. Every interaction should feel like a first-class experience—smooth, silent, and bespoke.

## Colors
This design system utilizes a "High-Altitude" palette. 

- **Deep Navy Blue (#001F3F)**: Represents the stratosphere and ultimate authority. Used for primary navigation, headings, and high-impact surfaces.
- **Cloud White (#F8F9FA)**: The primary canvas color. It provides a crisp, clinical cleanliness that feels premium.
- **Metallic Gold (#D4AF37)**: Reserved for "The Golden Touch"—calls to action, status indicators for VIP tiers, and subtle iconography highlights.
- **Atmospheric Accents**: Use highly desaturated blues for subtle background layering to maintain depth without introducing clutter.

## Typography
The typographic hierarchy creates a tension between the classic elegance of **Playfair Display** and the modern efficiency of **Montserrat**.

- **Headlines**: Use Playfair Display to signal heritage and bespoke service. Use tighter letter-spacing for large display sizes to maintain a "vogue" editorial feel.
- **Body & Interface**: Montserrat provides a geometric, high-legibility foundation for technical aviation data, flight paths, and logistics.
- **Micro-copy**: Captions and utility labels should use Montserrat in uppercase with generous letter-spacing to mimic the technical instrumentation found in modern glass cockpits.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid** model. The main content container is capped at 1440px to ensure legibility on ultra-wide displays commonly used by flight dispatchers and executives.

Spacing is governed by an 8px rhythmic grid, but "The Breath" (large vertical padding) is prioritized. Generous margins (48px+) are used to separate primary functional blocks, ensuring the interface never feels crowded. Components should use a "compostable" layout where elements are stacked with consistent `stack-md` gaps to maintain a clean, linear flow of information.

## Elevation & Depth
Depth in this design system is achieved through **Glassmorphism and Refraction** rather than traditional heavy shadows.

- **Surface Tiers**: Base layer is Cloud White. Secondary panels use a 60% opacity white with a 20px backdrop blur to simulate frosted glass.
- **Shadows**: When used, shadows must be "Ambient Blues"—ultra-diffused (#001F3F at 5% opacity) with a large 40px spread to make cards appear as if they are floating in a hazy sky.
- **Glass Stroke**: Every floating element must have a 1px inner border of semi-transparent white or gold to catch the light, creating a "machined edge" look.

## Shapes
The shape language is **Soft-Precision**. While luxury often utilizes sharp edges, this system employs subtle rounding to suggest the aerodynamic curves of a fuselage.

Standard components use a 4px (Soft) radius. Large containers or "Hero" cards may use up to 8px. This slight softening prevents the UI from feeling "sharp" or "aggressive," maintaining the welcoming nature of high-end hospitality. Pill shapes are reserved exclusively for status indicators (e.g., "In Flight," "Reserved") and search bars.

## Components
- **Primary Buttons**: Deep Navy backgrounds with Cloud White text. On hover, a subtle Gold bottom-border (2px) slides in.
- **Luxury Cards**: Use the glassmorphism style—backdrop blur, 1px light border, and high vertical padding. Content should be center-aligned for high-level summaries.
- **Input Fields**: Ghost-style. Only a bottom border in light grey, which transitions to Gold on focus. Labels use the `label-caps` typography style.
- **The "Flight-Path" Progress Bar**: A thin Metallic Gold line with glass-shimmer pulses to indicate current trip status.
- **Chips**: Small, pill-shaped tags with a Navy stroke for "Aircraft Type" and a Gold stroke for "VIP Status."
- **Interactive Map Layers**: Maps should use a custom "Silver/Night" style to match the Deep Navy theme, with flight paths rendered as glowing Gold arcs.