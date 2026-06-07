---
name: Bio-Garden OS
colors:
  surface: '#fcf9f5'
  surface-dim: '#dcdad6'
  surface-bright: '#fcf9f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f0'
  surface-container: '#f0edea'
  surface-container-high: '#eae8e4'
  surface-container-highest: '#e5e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#434843'
  inverse-surface: '#30302e'
  inverse-on-surface: '#f3f0ed'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#924a28'
  on-secondary: '#ffffff'
  secondary-container: '#ffa278'
  on-secondary-container: '#783615'
  tertiary: '#161817'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a2c2b'
  on-tertiary-container: '#929392'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#ffdbcd'
  secondary-fixed-dim: '#ffb596'
  on-secondary-fixed: '#360f00'
  on-secondary-fixed-variant: '#753413'
  tertiary-fixed: '#e2e3e1'
  tertiary-fixed-dim: '#c6c7c5'
  on-tertiary-fixed: '#1a1c1b'
  on-tertiary-fixed-variant: '#454746'
  background: '#fcf9f5'
  on-background: '#1b1c1a'
  surface-variant: '#e5e2df'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: EB Garamond
    fontSize: 36px
    fontWeight: '500'
    lineHeight: 42px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  headline-sm:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  title-lg:
    fontFamily: Manrope
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  data-display:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
    letterSpacing: 0.05em
  label-md:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin-desktop: 64px
  container-margin-mobile: 20px
  gutter: 24px
  section-gap: 80px
  element-gap: 16px
---

## Brand & Style

This design system is built upon the "Lush & Grounded" philosophy, positioning the product as a premium, high-tech companion for the modern indoor gardener. It balances the tactical requirements of a smart OS with the emotional tranquility of nature. 

The visual style is a sophisticated blend of **Tactile Minimalism** and **Organic UI**. It rejects the harshness of traditional tech interfaces in favor of soft, asymmetrical pebble shapes and "liquid" depth. The target audience values artisanal quality and environmental connection, expecting an interface that feels as much like furniture or a garden tool as it does software. The emotional response should be one of calm, focused attention and horticultural pride.

## Colors

The palette is derived from an earthy, botanical spectrum. **Deep Forest Green** (#1B3022) serves as the primary anchor, used for headers, primary containers, and brand-heavy moments. **Terra-Cotta** (#D27D56) provides a warm, clay-like contrast, utilized specifically for interactive elements, calls to action, and critical status updates. 

**Off-White** (#F9F9F7) is the canvas, providing a breathable, paper-like background that feels more natural than pure white. Text is primarily rendered in a soft charcoal (#2C2C2A) to maintain legibility without the jarring contrast of pure black against the organic palette. High-contrast data visualization should utilize varying tints of Terra-Cotta and Forest Green to ensure data is "readable at a glance" while remaining within the ecosystem's tonal range.

## Typography

The typographic strategy pairs the intellectual, classic feel of a serif with the utilitarian precision of a modern sans-serif. 

**EB Garamond** is used for display and headline levels. It should feel "grounded"—utilizing medium to semi-bold weights to ensure it has enough visual gravity against the deep green backgrounds. **Manrope** is the workhorse for all functional data, body text, and labels. It provides a clean, neutral counterpoint that ensures the complex data of soil PH, moisture levels, and growth timelines is easily digestible. For data-heavy readouts (e.g., temperature), use the `data-display` style with increased letter spacing to emphasize the "smart" nature of the OS.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to create a centered, editorial feel that mimics a luxury magazine. On mobile devices, it transitions to a **Fluid Grid** to maximize space for sensor data and plant imagery.

A 12-column grid is used for desktop (max-width 1440px), while mobile uses a 4-column grid. The spacing system is strictly based on 8px increments. Large "Section Gaps" are encouraged to create breathing room between different plant zones or biological metrics, reinforcing the sense of tranquility. Content should be grouped into organic clusters rather than rigid, edge-to-edge blocks.

## Elevation & Depth

This design system avoids traditional drop shadows in favor of **Liquid Shadows**. These are extra-diffused, large-radius shadows with low opacity (5-8%) that use a slight tint of the Primary Forest Green rather than pure black. This makes components feel as though they are softly resting on a surface rather than hovering high above it.

Hierarchy is further established through **Tonal Layering**:
- **Level 0 (Base):** Off-White.
- **Level 1 (Cards/Surface):** White or very faint Green-tinted White with a liquid shadow.
- **Level 2 (In-set):** Deep Forest Green for high-priority status panels or navigation headers.
- **Interactive:** Terra-Cotta accents do not use shadows; they use color-fills to indicate presence and "active" state.

## Shapes

The shape language is "Pebble-like" and organic. While the base `roundedness` is set to 2 (0.5rem), this design system encourages the use of **Variable Radii**. 

Containers and cards should ideally use slightly asymmetrical corner radii (e.g., 24px, 40px, 32px, 48px) to mimic the irregular beauty of river stones. Buttons must always be fully rounded (pill-shaped) to feel tactile and soft to the touch. Avoid hard 90-degree angles entirely to maintain the "Lush" brand personality.

## Components

### Buttons
Primary buttons are pill-shaped, filled with Terra-Cotta, and use Off-White text. Secondary buttons use a Forest Green stroke with no fill. All buttons should have a subtle "squish" animation on press to reinforce the tactile nature of the system.

### Cards
Cards are the primary container. They use organic, pebble-like shapes and liquid shadows. For "Plant Health" cards, the background may subtly transition to a very soft Green or Clay gradient depending on the plant's status.

### Data Visualization
Charts should avoid thin lines. Use thick, rounded-cap strokes for line charts and "blob" shapes for bar charts. High contrast is key: use Terra-Cotta against Forest Green backgrounds for vital signs (Water, Light) and Forest Green against Off-White for historical growth data.

### Inputs & Sliders
Sliders (for light/temp control) should be thick and "juicy," with a large, pebble-shaped thumb. Input fields use a soft, clay-colored bottom border rather than a full box to maintain a clean, grounded look.

### Specialized Components
- **Growth Timeline:** A vertical, vine-like line connecting pebble-shaped milestones.
- **Environment Dial:** A circular gauge for humidity and temp that uses a "liquid fill" effect to show levels.
- **Species Chip:** Small, high-radius chips used to categorize plants, using muted tints of the primary palette.