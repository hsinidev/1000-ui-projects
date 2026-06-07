---
name: Biological Purity
colors:
  surface: '#f7faf9'
  surface-dim: '#d7dbda'
  surface-bright: '#f7faf9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f3'
  surface-container: '#ebeeed'
  surface-container-high: '#e6e9e8'
  surface-container-highest: '#e0e3e2'
  on-surface: '#181c1c'
  on-surface-variant: '#3f4a3d'
  inverse-surface: '#2d3131'
  inverse-on-surface: '#eef1f0'
  outline: '#6f7a6c'
  outline-variant: '#becab9'
  surface-tint: '#006e20'
  primary: '#006e20'
  on-primary: '#ffffff'
  primary-container: '#98ff98'
  on-primary-container: '#007924'
  inverse-primary: '#77dc7a'
  secondary: '#0c6780'
  on-secondary: '#ffffff'
  secondary-container: '#9ae1ff'
  on-secondary-container: '#09657f'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#e8e8e8'
  on-tertiary-container: '#666868'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#93f993'
  primary-fixed-dim: '#77dc7a'
  on-primary-fixed: '#002105'
  on-primary-fixed-variant: '#005316'
  secondary-fixed: '#baeaff'
  secondary-fixed-dim: '#89d0ed'
  on-secondary-fixed: '#001f29'
  on-secondary-fixed-variant: '#004d62'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f7faf9'
  on-background: '#181c1c'
  surface-variant: '#e0e3e2'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
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
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  gutter: 1.5rem
  margin: 2rem
---

## Brand & Style

This design system is built upon the intersection of advanced hydro-intelligence and the restorative power of nature. The brand personality is serene, scientific, and transparent, aimed at eco-conscious homeowners and facility managers who prioritize chemical-free living. 

The aesthetic marries **Minimalism** with **Glassmorphism**, creating a digital environment that feels as clear and refreshing as the water it monitors. By utilizing expansive whitespace and translucent layering, the UI evokes a sense of breathability and calm. The visual language moves away from rigid, clinical tech patterns toward organic, "liquid" forms that suggest movement and biological harmony, establishing a deep sense of trust through clarity and precision.

## Colors

The palette is anchored in high-vibrancy, natural hues that reflect a healthy ecosystem. **Mint Green** serves as the primary driver, symbolizing biological life and filtration efficiency. **Sky Blue** provides a secondary focus, representing water clarity and depth. 

The background environment remains **Crisp White** or very light neutral tones to maximize the "glass" effect of foreground elements. For safety-critical data, the system utilizes high-contrast indicators: a deep forest green for optimal health, amber for maintenance warnings, and a vibrant coral-red for immediate safety hazards. These colors ensure that water quality metrics are legible even in high-glare outdoor environments.

## Typography

This design system utilizes **Inter** for all typographic layers to maintain a modern, tech-forward, and highly legible interface. The type scale is designed with generous line heights to enhance readability and contribute to the overall airy aesthetic.

Headlines use tighter letter spacing and heavier weights to feel grounded and authoritative. Body text is prioritized for comfort, using a slightly larger base size (16px-18px) to accommodate outdoor usage where lighting conditions vary. Labels and data points utilize increased letter spacing and semi-bold weights to ensure that vital statistics—such as pH levels and oxygen saturation—are immediately scannable.

## Layout & Spacing

The layout philosophy follows a **fluid grid** model that prioritizes "breathing room." Content is organized into modular containers that flow vertically like a stream. A 12-column system is used for desktop views, transitioning to a flexible single-column stack for mobile devices.

Margins are intentionally large (32px+) to prevent the interface from feeling cluttered, reinforcing the serene brand promise. Spacing between sections uses a rhythmic 8px base, with larger gaps (40px-64px) between distinct functional groups to define hierarchy without the need for heavy dividers.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and **Ambient Shadows**. Instead of traditional solid shadows, surfaces use a combination of:

1.  **Backdrop Blurs:** Elements possess a 16px to 24px blur radius, allowing the biological background colors to bleed through softly.
2.  **Inner Glows:** A subtle 1px white border with 40% opacity is applied to the top and left edges of containers to simulate a light-catching glass edge.
3.  **Soft Diffused Shadows:** Shadows are extra-diffused (large blur, low spread) and tinted with a hint of the Sky Blue primary color rather than pure grey, creating an "underwater" suspension effect.
4.  **Tonal Layering:** Interactive elements sit on the highest "elevation," appearing more opaque and vibrant than static informational containers.

## Shapes

The shape language is strictly **Rounded**, avoiding sharp corners to mirror the organic forms found in nature. Standard containers use a 16px (1rem) radius, while larger interactive cards utilize a 24px (1.5rem) radius.

To differentiate this design system, certain decorative elements and data visualizations should employ "liquid" geometry—non-perfect circles and flowing paths that mimic water droplets or ripples. All buttons and input fields follow a high-roundedness pattern to feel soft and approachable to the touch.

## Components

### Buttons
Primary buttons are pill-shaped with a soft gradient from Sky Blue to Mint Green. They feature a subtle outer glow when active. Secondary buttons use a glassmorphic style with a semi-transparent white background and a thin stroke.

### Cards & Containers
Cards are the primary organizational unit. They must feature a `backdrop-filter: blur()` and a semi-transparent white background (rgba 255, 255, 255, 0.6). They should appear to float above the background pattern.

### High-Contrast Indicators
Safety indicators for water health use a circular "pulse" animation. A "Safe" status is represented by a steady, soft Mint Green glow, while "Critical" alerts use a high-contrast red with a more rapid, sharp pulse to command attention.

### Input Fields
Fields are minimally designed with a bottom border or a very soft inset shadow. Focus states transition the border to Sky Blue and increase the backdrop blur of the field.

### Liquid Progress Bars
Instead of standard linear loaders, progress indicators (like filtration percentage) use a "wave" fill effect, where the color fill has a moving, undulating top edge to represent liquid volume.

### Lists
Lists are presented as "floating tiles" with generous vertical padding and soft separators, avoiding hard lines in favor of subtle shifts in background opacity.