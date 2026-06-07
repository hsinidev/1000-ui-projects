---
name: Industrial Luxe
colors:
  surface: '#121317'
  surface-dim: '#121317'
  surface-bright: '#38393d'
  surface-container-lowest: '#0d0e12'
  surface-container-low: '#1a1b1f'
  surface-container: '#1e1f23'
  surface-container-high: '#292a2e'
  surface-container-highest: '#343539'
  on-surface: '#e3e2e7'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e3e2e7'
  inverse-on-surface: '#2f3034'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#dec1af'
  on-secondary: '#3f2c20'
  secondary-container: '#574335'
  on-secondary-container: '#ccb09f'
  tertiary: '#ffb77b'
  on-tertiary: '#4d2700'
  tertiary-container: '#2c1400'
  on-tertiary-container: '#b87333'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#fbddca'
  secondary-fixed-dim: '#dec1af'
  on-secondary-fixed: '#28180d'
  on-secondary-fixed-variant: '#574335'
  tertiary-fixed: '#ffdcc2'
  tertiary-fixed-dim: '#ffb77b'
  on-tertiary-fixed: '#2e1500'
  on-tertiary-fixed-variant: '#6d3a00'
  background: '#121317'
  on-background: '#e3e2e7'
  surface-variant: '#343539'
typography:
  display-lg:
    fontFamily: IBM Plex Serif
    fontSize: 56px
    fontWeight: '700'
    lineHeight: 64px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: IBM Plex Serif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
  headline-lg-mobile:
    fontFamily: IBM Plex Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: IBM Plex Serif
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
spacing:
  unit: 8px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  container-max: 1280px
---

## Brand & Style

The design system is defined by an **Industrial-Luxe** aesthetic, merging the raw, tactile environment of a distillery with the precision of high-end bespoke craftsmanship. The brand personality is artisanal and rugged, yet maintains an air of exclusive refinement that appeals to discerning connoisseurs.

The UI style leans heavily into **Tactile Minimalism**. It utilizes physical metaphors—such as the texture of charred white oak barrels and the cool sheen of brushed steel—to ground the digital experience in the physical world of spirits production. Visuals are characterized by high-contrast compositions, crisp structural lines, and subtle inner shadows that create an "etched" or "stamped" effect, mimicking the branding irons and metal plates used in traditional coopering.

## Colors

The palette for this design system is rooted in the materials of the distillery floor. The foundational color is **Deep Matte Black (#1A1A1A)**, used for primary surfaces to evoke a sense of prestige and depth. **Charred Oak Brown (#3D2B1F)** provides warmth and is used for secondary containers or textural overlays, referencing the interior of a toasted barrel.

**Aged Copper (#B87333)** serves as the high-impact accent color, reserved for primary actions, success states, and premium highlights—mimicking the brilliant stills used in distillation. **Brushed Steel Silver (#8E8E93)** is utilized for borders, iconography, and secondary text, providing a cold, structural contrast to the organic wood tones.

## Typography

Typography in this design system emphasizes authority and clarity. For headers, **IBM Plex Serif** is used to achieve a masculine, slab-serif appearance that feels engineered and sturdy. Headlines should utilize tighter letter-spacing to reinforce the "bold" personality.

The body text employs **Inter**, chosen for its utilitarian precision and high readability against dark, textured backgrounds. To maintain the industrial feel, labels and utility text often utilize uppercase styling with increased letter-spacing, reminiscent of stamped metal serial numbers or technical specifications on a cask.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model to mirror the structured environment of a rackhouse. A 12-column grid is standard for desktop, transitioning to a 4-column grid for mobile devices.

Spacing is governed by an 8px base unit, ensuring a rhythmic, mechanical alignment across all components. Large sections are separated by significant vertical padding to maintain the "Luxe" feel of the brand, while functional groups use tighter spacing to emphasize their relationship. Layouts should favor asymmetrical balance, allowing high-quality imagery of the product to occupy significant "negative" space.

## Elevation & Depth

This design system eschews traditional drop shadows in favor of **Tonal Layering** and **Tactile Depth**. 

1.  **Etched Depth (Inner Shadows):** Elements like input fields and button containers use subtle inner shadows to appear "stamped" into the surface.
2.  **Raised Surfaces:** Interactive cards and modals use a slightly lighter shade of the primary background or a brushed metal texture overlay to appear physically placed on top of the base layer.
3.  **Crisp Borders:** 1px solid borders in Brushed Steel (#8E8E93) define boundaries with surgical precision, reinforcing the industrial theme without the need for heavy blur effects.

## Shapes

The shape language is strictly **Sharp (0px radius)**. Every element, from buttons to image containers and cards, features 90-degree corners. This decision reinforces the "Industrial" component of the aesthetic, suggesting precision-cut steel and machined components. Occasional use of "chamfered" corners (45-degree cuts) may be used for decorative elements or special call-to-actions to further the engineering metaphor.

## Components

### Buttons
Primary buttons feature a solid **Aged Copper (#B87333)** background with black text. Secondary buttons are "Ghost" style, with a **Brushed Steel** border and a subtle brushed-metal hover texture. All buttons are rectangular with zero corner radius.

### Input Fields
Inputs are styled to look like etched control panels. They feature the Deep Matte Black background with a 1px steel border and a soft inner shadow. Focus states transition the border color to Aged Copper.

### Cards
Cards utilize the **Charred Oak Brown** as a subtle background tint or a low-opacity wood-grain texture overlay. Borders are mandatory to ensure separation from the primary background.

### Custom Component: The "Batch Label"
A specialized chip component used for barrel details. It features a heavy border, mono-styled Inter typography, and is often styled with a vertical orientation or "stamped" appearance to mimic real distillery barrel tags.

### Lists & Tables
Lists use horizontal 1px steel dividers. Data points (like ABV%, Age, or Barrel No.) are highlighted using the Slab-Serif header font in a smaller size to act as technical data markers.