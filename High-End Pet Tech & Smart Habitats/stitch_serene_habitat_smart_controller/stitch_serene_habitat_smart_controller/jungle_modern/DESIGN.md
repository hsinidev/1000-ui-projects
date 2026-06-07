---
name: Jungle Modern
colors:
  surface: '#101412'
  surface-dim: '#101412'
  surface-bright: '#363a37'
  surface-container-lowest: '#0b0f0d'
  surface-container-low: '#191c1a'
  surface-container: '#1d211e'
  surface-container-high: '#272b28'
  surface-container-highest: '#323633'
  on-surface: '#e0e3df'
  on-surface-variant: '#c3c8bd'
  inverse-surface: '#e0e3df'
  inverse-on-surface: '#2d312e'
  outline: '#8d9289'
  outline-variant: '#434840'
  surface-tint: '#b1cfa7'
  primary: '#b1cfa7'
  on-primary: '#1e361a'
  primary-container: '#2d4628'
  on-primary-container: '#97b48d'
  inverse-primary: '#4b6544'
  secondary: '#ffb59c'
  on-secondary: '#5c1900'
  secondary-container: '#7b2e10'
  on-secondary-container: '#ff9b79'
  tertiary: '#c8c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#404040'
  on-tertiary-container: '#adabab'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#cdebc1'
  primary-fixed-dim: '#b1cfa7'
  on-primary-fixed: '#082007'
  on-primary-fixed-variant: '#344d2e'
  secondary-fixed: '#ffdbcf'
  secondary-fixed-dim: '#ffb59c'
  on-secondary-fixed: '#390c00'
  on-secondary-fixed-variant: '#7b2e10'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#101412'
  on-background: '#e0e3df'
  surface-variant: '#323633'
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
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
  data-label:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-margin: 24px
  gutter: 16px
---

## Brand & Style

This design system establishes a "Nature-Tech" aesthetic, balancing the raw, organic essence of a tropical habitat with the precision of a high-end smart home controller. The brand personality is professional, grounded, and sophisticated, targeting reptile enthusiasts who view their hobby through a lens of scientific care and aesthetic beauty.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. It utilizes expansive negative space and a restrained palette to maintain clarity, while employing translucent, blurred layers to evoke the sensation of looking through a terrarium’s misted glass. The emotional response is one of calm reliability—providing a sense of control over a complex biological environment.

## Colors

The palette is rooted in the "Jungle-Modern" narrative, using deep, earthy tones to ground the interface.

- **Primary (Deep Moss Green):** Used for primary actions, active states, and branding elements. It represents the vitality of the flora.
- **Secondary (Terra-Cotta):** Used as a functional accent for heat-related data, warnings, or vital "Warmth" toggles.
- **Tertiary/Background (Charcoal Black):** The primary canvas color, providing a high-contrast backdrop that allows the green and terra-cotta to pop like light through a canopy.
- **Neutrals:** Off-white "Mist" tones are used for secondary text and icons to ensure legibility without the harshness of pure white.

Color application should follow a 60-30-10 rule, where Charcoal Black dominates, Moss Green provides the structural identity, and Terra-Cotta highlights critical climate interactions.

## Typography

This design system employs a dual-font strategy to balance character with utility.

- **Headlines:** *Plus Jakarta Sans* provides a soft, rounded, and organic feel. Its geometric yet friendly curves mimic natural forms.
- **Body & Interface:** *Inter* is used for all functional text, settings, and descriptive content. It ensures maximum readability across varying device sizes.
- **Data Visualization:** *JetBrains Mono* is used sparingly for environmental metrics (temperature, humidity percentages, timers) to emphasize technical precision and the "smart controller" aspect of the product.

Use tight tracking for display headers and generous line-height for body copy to maintain an airy, sophisticated feel.

## Layout & Spacing

The layout follows a **fluid grid** model with significant breathing room to prevent the interface from feeling "claustrophobic"—a contrast to the dense jungle theme.

- **Rhythm:** An 8px base unit drives all spacing decisions. 
- **Margins:** Mobile layouts should maintain a 24px safe area on the horizontal axis. 
- **Grouping:** Use large 48px (lg) gaps between major content sections (e.g., Temperature Controls vs. Light Scheduling) to create clear mental boundaries without the need for heavy dividing lines.
- **Padding:** Internal card padding should be generous (24px to 32px) to accommodate the large corner radii.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and tonal layering rather than traditional drop shadows.

- **The Humid Overlay:** Overlays and modals use a high-density backdrop blur (20px-30px) with a subtle 10% white tint to simulate misted glass.
- **Floating Surface:** Primary cards use a slightly lighter Charcoal variation (#222222) with a 1px "inner glow" stroke (Moss Green at 15% opacity) on the top and left edges to simulate light catching an edge.
- **Active State Depth:** When a button or card is pressed, it should scale slightly (98%) and increase in saturation rather than moving closer to the user, maintaining a tactile, physical feel.

## Shapes

The shape language is the defining "Organic" element of this design system. Inspired by river stones and leaf silhouettes, the system rejects sharp corners.

- **Pebble Radii:** All primary containers and cards use a minimum radius of 24px.
- **Pill Elements:** Buttons, chips, and input fields utilize full pill shapes (100px radius) to maintain a soft, friendly touch.
- **Iconography:** Icons must be "crisp and minimal"—thin 1.5pt strokes with slightly rounded caps to match the typography. Avoid filled icon styles unless indicating an active toggle state.

## Components

- **Control Cards:** The primary vessel for data. Large, 24px+ rounded corners. Backgrounds use a subtle dark gradient or glass effect.
- **Pebble Buttons:** Primary buttons are Moss Green with Mist-colored text. Secondary buttons are Charcoal with a 1px border. All buttons use high internal padding (16px vertical, 32px horizontal).
- **Environment Toggles:** Custom switches that look like physical sliders found on high-end audio equipment, utilizing the Terra-Cotta color for the "On" state of heating elements.
- **Humidity Gauges:** Circular or semi-circular progress rings with a "mist" glow effect behind the progress line.
- **Climate Chips:** Small pill-shaped badges used for status updates (e.g., "Day Cycle," "Misting Active").
- **Inputs:** Minimalist fields with only a bottom border or a very soft, semi-transparent background fill. Labels use the "Data-Label" mono font for a scientific feel.
- **The "Habitat View":** A specialized component that uses a full-screen blurred image of the reptile's environment as the background, with glassmorphic cards floating on top.