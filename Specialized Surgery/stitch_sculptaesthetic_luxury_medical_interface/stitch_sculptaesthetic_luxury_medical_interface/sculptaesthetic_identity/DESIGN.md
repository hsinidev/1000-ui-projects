---
name: SculptAesthetic Identity
colors:
  surface: '#fff8f5'
  surface-dim: '#e1d8d4'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2ed'
  surface-container: '#f5ece7'
  surface-container-high: '#efe6e2'
  surface-container-highest: '#e9e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#484740'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#79776f'
  outline-variant: '#c9c6bd'
  surface-tint: '#605e5b'
  primary: '#605e5b'
  on-primary: '#ffffff'
  primary-container: '#f5f1ed'
  on-primary-container: '#6f6d6a'
  inverse-primary: '#c9c6c2'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#655d51'
  on-tertiary: '#ffffff'
  tertiary-container: '#fcf0e1'
  on-tertiary-container: '#756c60'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e6e2de'
  primary-fixed-dim: '#c9c6c2'
  on-primary-fixed: '#1c1c19'
  on-primary-fixed-variant: '#484744'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#ede1d2'
  tertiary-fixed-dim: '#d0c5b6'
  on-tertiary-fixed: '#201b12'
  on-tertiary-fixed-variant: '#4d463b'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 72px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  section-padding: 128px
---

## Brand & Style
This design system is built upon the intersection of clinical precision and high-fashion editorial. It targets a discerning, affluent demographic that views aesthetic procedures as an investment in self-actualization rather than mere vanity. The visual narrative moves away from the "clinical coldness" of traditional medicine, opting instead for the warmth of a luxury boutique and the structured elegance of a gallery.

The chosen style is **Minimalism** with an emphasis on **Editorial Layout**. This is achieved through expansive white space, a deliberate lack of decorative clutter, and a focus on high-fidelity photography. The emotional response is one of calm, trust, and exclusivity—invoking the feeling of stepping into a private atelier.

## Colors
The palette is rooted in organic, skin-adjacent nude tones. **Sand** (#F5F1ED) serves as the primary canvas, providing a softer, more luxurious foundation than pure white. **Champagne** (#ECE0D1) acts as a subtle secondary tone for layering and structural depth. 

**Matte Gold** (#C5A059) is used sparingly as an accent to denote premium status and highlight interactive calls to action. **Deep Charcoal** (#2D2926) provides the necessary contrast, used exclusively for typography and hairline borders to ensure readability and a grounded, professional feel.

## Typography
Typography in this design system creates an "Editorial-First" hierarchy. **Noto Serif** is utilized for all headlines and display elements; its refined serifs and classic proportions signal authority and timeless beauty. High-level headers should utilize tighter letter-spacing for a modern, fashion-forward look.

**Manrope** provides a clean, neutral counter-balance for body text and functional labels. It ensures that medical information remains legible and professional. For metadata and utility labels, an uppercase Manrope with wide tracking (letter-spacing) is preferred to mimic the labeling found in luxury product packaging.

## Layout & Spacing
The design system employs a **Fixed Grid** model to maintain the rigid structure of a printed magazine. A 12-column grid is standard, but the primary differentiator is the "Breathing Room"—massive vertical margins and section paddings that prevent the interface from feeling crowded.

Layouts should be asymmetrical, often pushing imagery off-center to allow typography to occupy its own "white space" column. Elements are aligned to a strict 8px baseline, ensuring that despite the airy feel, the underlying structure is mathematically precise and clinical.

## Elevation & Depth
To maintain a high-fashion aesthetic, this design system avoids heavy shadows. Depth is communicated through **Tonal Layers** and **Low-Contrast Outlines**. 

Surfaces are distinguished by slight shifts between Sand, Champagne, and White. Where separation is required, use 0.5px or 1px hairline borders in Charcoal (at 15-20% opacity). For primary interactive elements, a very soft, diffused ambient shadow (0px 20px 40px rgba(45, 41, 38, 0.05)) may be used to suggest a gentle "lift" off the page without breaking the minimalist aesthetic.

## Shapes
The shape language of this design system is **Sharp (0)**. Right angles and straight lines reflect architectural precision and the surgical accuracy of the boutique. 

Buttons, input fields, and card containers should avoid rounded corners entirely to maintain a high-end, bespoke feel. The only exception to this rule is for "Natural Result" imagery and profile avatars, which may use a circular mask to emphasize the softness and organic nature of the human face and body.

## Components
### Buttons
Primary buttons are solid Deep Charcoal with Matte Gold text or vice versa. Secondary buttons are "Ghost" style—sharp-edged rectangles with a 1px Charcoal border and no fill. All button labels use the `label-caps` typography style.

### Input Fields
Inputs are minimalist, consisting of a single 1px Charcoal bottom border (underline style). Labels sit above the line in small-caps Manrope. Error states are indicated by a subtle shift to a muted terracotta, avoiding harsh reds that conflict with the nude palette.

### Cards
Cards for services or surgeon profiles do not use backgrounds or shadows. They are defined by their content alignment and generous padding. A hairline top-border is often used to separate items in a list or grid.

### Imagery Containers
All imagery should use a subtle grain overlay or soft-focus lighting. Photographs are never framed with borders; they bleed to the edge of their grid columns or fill the background to create an immersive, editorial experience.

### Additional Components
- **Procedure Timeline:** A minimalist vertical line with Charcoal dots representing the patient journey stages.
- **Before/After Slider:** A thin Matte Gold handle used to toggle between high-resolution results imagery.