---
name: Vibrant Dark Gaming System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d4c0d7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9d8ba0'
  outline-variant: '#514255'
  surface-tint: '#ecb2ff'
  primary: '#ecb2ff'
  on-primary: '#520071'
  primary-container: '#bd00ff'
  on-primary-container: '#ffffff'
  inverse-primary: '#9900cf'
  secondary: '#d3fbff'
  on-secondary: '#00363a'
  secondary-container: '#00eefc'
  on-secondary-container: '#00686f'
  tertiary: '#94db00'
  on-tertiary: '#223600'
  tertiary-container: '#568200'
  on-tertiary-container: '#fffeff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f8d8ff'
  primary-fixed-dim: '#ecb2ff'
  on-primary-fixed: '#320047'
  on-primary-fixed-variant: '#74009f'
  secondary-fixed: '#7df4ff'
  secondary-fixed-dim: '#00dbe9'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#a9f900'
  tertiary-fixed-dim: '#94db00'
  on-tertiary-fixed: '#121f00'
  on-tertiary-fixed-variant: '#334f00'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
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
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
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
  xl: 40px
  xxl: 64px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is built for a high-octane digital marketplace that merges professional software distribution with cutting-edge gaming culture. The brand personality is high-energy and efficient, prioritizing speed and clarity without sacrificing visual impact.

The visual style utilizes **Glassmorphism** as its primary structural layer, using frosted glass effects and vibrant background blurs to create depth in a dark environment. This is complemented by a **Modern/Technical** aesthetic characterized by precise geometry and sharp typography. The interface should feel like a high-end command center: powerful, responsive, and immersive.

## Colors

The palette is anchored in a "Deep Charcoal" base for primary backgrounds to maintain focus and reduce eye strain during long sessions. "Slate" is used for secondary containers and surface differentiation.

The accent strategy utilizes high-saturation neon colors:
- **Electric Purple (#BD00FF):** Primary action color for core CTAs and branding.
- **Cyan (#00F0FF):** Secondary action color for informational links, filters, and active states.
- **Lime (#ADFF00):** Functional accent for success states, notifications, and "In-Stock" indicators.
- **Surface Overlays:** All overlays use a semi-transparent version of the Slate color (approx. 60% opacity) with a 20px-40px background blur to achieve the glass effect.

## Typography

This design system uses a dual-font approach to balance technical precision with extreme readability. **Space Grotesk** is used for headlines to provide a geometric, futuristic feel that resonates with the gaming community. **Inter** is utilized for all body copy and UI labels to ensure maximum functional efficiency and clarity.

Large display headings should use tighter letter spacing and bold weights to command attention, while labels are often set in uppercase with slight tracking to enhance the "technical" instrumentation feel of the interface.

## Layout & Spacing

The design system employs a **12-column fluid grid** for the primary storefront and a **fixed grid** (max-width: 1440px) for detail pages to ensure readability. 

A strict 4px spacing rhythm (4, 8, 16, 24, 40, 64) is enforced to maintain a modular, organized structure. Information density is moderately high to cater to professional users who value efficiency, but content is separated by generous 24px gutters to prevent visual clutter. Modular cards should use the `lg` (24px) padding value internally for content breathing room.

## Elevation & Depth

Hierarchy is established through **Glassmorphism and Tonal Layering** rather than traditional drop shadows. 

1. **Base (Level 0):** Deep Charcoal (#121212) - The main canvas.
2. **Surface (Level 1):** Slate (#1A1A1B) - Used for modular cards and content sections.
3. **Glass (Level 2):** Semi-transparent Slate with 30px background blur - Used for navigation bars, modals, and hover-state overlays.
4. **Glow (Level 3):** Instead of shadows, active elements or high-priority items use a subtle "Outer Glow" using the primary or secondary neon colors at 10-15% opacity to indicate focus or elevation.

Borders are kept thin (1px) and use low-opacity white or the primary accent color to define edges without adding visual weight.

## Shapes

The shape language is "Soft" (Level 1). This choice ensures the UI feels modern and approachable while maintaining the "Sharp" technical feel requested.

- **Buttons & Inputs:** 0.25rem (4px) corner radius for a precise, crisp look.
- **Modular Cards:** 0.5rem (8px) corner radius to differentiate them from smaller interactive components.
- **Glass Overlays:** 0.75rem (12px) corner radius to create a distinct "floating" feel.

Gradients should be used sparingly, primarily as 45-degree linear fills on primary buttons, moving from a deep purple to the electric neon purple.

## Components

### Buttons
Primary buttons use the Electric Purple gradient with white text. Secondary buttons use a Slate background with a 1px Cyan border. Ghost buttons utilize Cyan text with no background. All buttons have a subtle "glow" transition on hover.

### Modular Cards
Cards feature a 1px border (#FFFFFF10) and a subtle gradient background from Slate to Deep Charcoal. On hover, the border color shifts to the Primary Purple.

### Input Fields
Inputs are dark with a 1px Slate border. Upon focus, the border glows Cyan and the background shifts slightly lighter. Labels are placed above the field in `label-md` style.

### Glass Overlays
Used for sidebars and dropdowns. These must include a `backdrop-filter: blur(20px)` and a thin highlight on the top and left edges to simulate light hitting glass.

### Chips & Tags
Used for gaming genres or software categories. These are small, pill-shaped elements with low-opacity versions of the accent colors (e.g., 10% Cyan background with 100% Cyan text).

### Additional Components
- **System Status Indicators:** Small glowing dots (Lime for online, Purple for maintenance).
- **Progress Bars:** Thin 4px bars using the Cyan-to-Purple gradient.
- **Price Badges:** High-contrast Lime blocks with black text for immediate visibility of discounts.