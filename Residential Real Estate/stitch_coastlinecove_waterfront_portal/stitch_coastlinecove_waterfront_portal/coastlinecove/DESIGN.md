---
name: CoastlineCove
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#404751'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#707882'
  outline-variant: '#c0c7d2'
  surface-tint: '#00629e'
  primary: '#005e97'
  on-primary: '#ffffff'
  primary-container: '#0077be'
  on-primary-container: '#f7f9ff'
  inverse-primary: '#9acbff'
  secondary: '#8d4f11'
  on-secondary: '#ffffff'
  secondary-container: '#feac67'
  on-secondary-container: '#773e00'
  tertiary: '#595a5b'
  on-tertiary: '#ffffff'
  tertiary-container: '#717373'
  on-tertiary-container: '#f9f9f9'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cfe5ff'
  primary-fixed-dim: '#9acbff'
  on-primary-fixed: '#001d34'
  on-primary-fixed-variant: '#004a79'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  h1:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Plus Jakarta Sans
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The brand personality of the design system is serene, aspirational, and sophisticated. It is designed for affluent travelers seeking waterfront sanctuary, emphasizing the restorative power of "Blue-Space." The UI should feel as light as a coastal breeze, evoking immediate calmness through clarity and openness.

The chosen style is **Minimalism with soft Tonal Layers**. It prioritizes high-end editorial layouts, using generous whitespace to allow imagery of water and sand to breathe. By avoiding visual clutter and heavy borders, the interface mirrors the expansive horizon of a coastline, shifting the user's focus toward relaxation and premium service.

## Colors

The palette is built on the psychology of "Blue-Space" to induce a meditative state of calm. **Ocean Blue** serves as the primary anchor, used for key actions and brand moments to represent depth and reliability. **Sand** acts as the secondary accent, providing warmth and human connection against the cooler tones.

**Crisp White** is the foundational canvas, ensuring the interface remains bright and airy. Functional neutrals are tinted with a hint of blue-grey to maintain harmony, avoiding harsh blacks that would disrupt the breezy aesthetic.

## Typography

The typography strategy balances modern elegance with effortless readability. **Plus Jakarta Sans** is utilized for headlines; its soft, rounded terminals feel welcoming and contemporary, perfectly capturing a high-end vacation vibe. 

For body text, **Be Vietnam Pro** provides a warm and approachable rhythm. It ensures that property descriptions and travel details remain highly legible across all devices. Large line-heights are applied globally to reinforce the airy, spacious feeling of the design system.

## Layout & Spacing

The layout follows a **Fixed Grid** model centered within the viewport to maintain an editorial, "boutique" feel. A 12-column system is used for desktop, but the design system mandates significant horizontal margins (up to 80px) to prevent the content from feeling cramped.

The spacing rhythm is based on an 8px scale. Spacing between major sections should be generous (using the 'xl' token) to create a sense of luxury and unhurried exploration. Elements should never feel crowded; if in doubt, increase the whitespace.

## Elevation & Depth

To maintain the "Breezy & Bright" aesthetic, depth is created through **Ambient Shadows** rather than stark borders. Shadows should be exceptionally diffused and low-opacity, using a subtle Ocean Blue tint (`rgba(0, 119, 190, 0.08)`) instead of pure grey. This makes components appear as if they are floating on water.

Layers are kept shallow. A primary surface (White) sits on a very light-blue background (#F0F8FF) to define the workspace. Overlays and dropdowns use a subtle backdrop blur (glassmorphism) to mimic the translucency of water and mist, maintaining the high-end, airy feel.

## Shapes

The shape language of the design system is defined by soft, organic curves that mirror the natural landscape of a coastline. Sharp edges are avoided to maintain the theme of calmness. 

Standard components utilize a 0.5rem (8px) radius, while larger containers like cards and the 'Check Availability' CTA use a 1rem (16px) radius to emphasize their approachability and premium nature.

## Components

### Check Availability CTA
The primary call-to-action is a prominent, high-contrast bar. It uses a Crisp White background with a subtle ambient shadow and a bold Ocean Blue button. This component should be "sticky" or positioned in a way that it anchors the user experience without obstructing view-ports.

### Tide & Weather Widget
A specialized utility component that uses thin-stroke iconography. It features a semi-transparent background with a light blur (glassmorphism) and Sand-colored accents for temperature or high-tide markers, connecting the digital experience to the physical environment.

### Buttons & Inputs
Buttons feature 0.5rem rounded corners. The primary state is Ocean Blue with white text, while secondary states use a ghost style with an Ocean Blue outline. Input fields are minimalist, using only a bottom border or a very faint Ocean Blue fill to keep the interface "light."

### Property Cards
Cards are the hero of the search experience. They feature edge-to-edge photography, 1rem corner radii, and info overlays that use the 'Sand' color for pricing and 'Ocean Blue' for "Verified" badges. Whitespace within the card is maximized to separate the title from the metadata.