---
name: Atmos-Garden
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#414844'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#006a60'
  on-secondary: '#ffffff'
  secondary-container: '#7af7e5'
  on-secondary-container: '#007166'
  tertiary: '#002d1c'
  on-tertiary: '#ffffff'
  tertiary-container: '#00452e'
  on-tertiary-container: '#75b393'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#7af7e5'
  secondary-fixed-dim: '#5bdac9'
  on-secondary-fixed: '#00201c'
  on-secondary-fixed-variant: '#005048'
  tertiary-fixed: '#b1f0ce'
  tertiary-fixed-dim: '#95d4b3'
  on-tertiary-fixed: '#002114'
  on-tertiary-fixed-variant: '#0e5138'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-display:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '500'
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
  container-padding: 32px
  gutter: 24px
  section-gap: 64px
---

## Brand & Style

The design system is engineered to bridge the gap between biological life and high-end automation. It evokes a "Botanical Tech" aesthetic—an atmosphere that feels as lush and organic as a greenhouse, yet as precise as a laboratory. The visual language is sophisticated and high-end, targeting residential users who value sustainability and cutting-edge home integration.

The style leverages **Glassmorphism** to represent the glass enclosures of a greenhouse, paired with **Soft-UI** patterns to create a tactile, approachable feel. This combination ensures that data-heavy interfaces remain airy and non-intimidating. The emotional response is one of calm control, clarity, and growth.

## Colors

The palette is anchored by **Forest Green**, providing a deep, grounded foundation that represents nature and stability. **Glass-Cyan** acts as the technical highlight, used for active states, data visualizations, and interactive elements to signify water, air, and technology. 

The background is strictly **Off-White**, maintaining a clean, gallery-like space for content. For data-heavy components, a secondary green (#2D6A4F) is utilized to create depth and hierarchy without departing from the monochromatic botanical theme. Accents should be used sparingly to guide the eye toward "Growth Metrics" and "System Health."

## Typography

The design system employs **Manrope** for primary communication, chosen for its modern, balanced, and refined geometric structure. It handles headlines and body copy with professional grace.

For technical data—such as temperature, humidity, and pH levels—the system uses **Geist**. This monospaced-influenced sans-serif provides the precision and technical clarity required for a smart-tech product. Labels should often use the `label-caps` style to provide a structured, architectural feel to the information density.

## Layout & Spacing

This design system utilizes a **Fixed Grid** philosophy for desktop (1280px max-width) and a **Fluid Grid** for mobile devices. The rhythm is based on an 8px base unit to ensure alignment and mathematical harmony.

Layouts should prioritize whitespace to reflect the "open air" of a greenhouse. Data widgets are organized in a 12-column grid, where standard modules span 3 or 4 columns. Large-scale environmental visualizations span the full 12 columns. Margins are generous (32px+) to prevent the interface from feeling crowded, even when displaying complex automation schedules.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Glassmorphism**. Rather than traditional heavy shadows, the design system uses "Atmospheric Shadows"—very soft, diffused blurs with a slight Forest Green tint (#1B4332 at 5-8% opacity) to make cards feel like they are floating over a natural surface.

Interactive surfaces use a **Backdrop Blur** (12px - 20px) to create a frosted glass effect. This is particularly effective for navigation bars and overlay modals, allowing the botanical colors of the background to peak through while maintaining legibility. Borders should be thin (1px) and low-contrast, using a semi-transparent white to define edges.

## Shapes

The shape language is strictly organic. Sharp corners are avoided to mimic the soft curves found in nature. Primary containers use a 1rem (16px) radius, while secondary elements like buttons and input fields use a more pronounced 2rem or pill-shape to invite interaction. 

Icons should follow a "Linear-Organic" style—open paths with rounded terminals that match the font-weight of the surrounding text. Curves in the UI should feel intentional and fluid, never jagged.

## Components

### Buttons
Primary buttons are Forest Green with Off-White text, featuring a subtle inner-glow to suggest volume. Secondary buttons use the Glassmorphism effect: a semi-transparent background with a Glass-Cyan border.

### Cards & Containers
Cards are the primary vehicle for data. They feature a white background with 60% opacity and a 20px backdrop blur. A subtle Soft-UI outer shadow provides a tactile lift from the Off-White background.

### Data Inputs
Input fields are pill-shaped with a soft inset shadow (neomorphic-lite) to indicate they are "hollow" and ready for data entry. The focus state is a 2px Glass-Cyan outer glow.

### Chips & Tags
Used for plant health status (e.g., "Optimal," "Needs Water"). These should be small, high-radius pills using low-saturation versions of the primary colors to avoid visual noise.

### Additional Components
- **Environmental Gauges:** Circular, soft-gradient progress bars using Glass-Cyan to track humidity and light cycles.
- **Timeline Scrubber:** A thin, horizontal control for viewing historical greenhouse data, styled with a frosted-glass handle.
- **Status Orbs:** Pulsing soft-glow indicators used to show "Live" connectivity to the automated sensors.