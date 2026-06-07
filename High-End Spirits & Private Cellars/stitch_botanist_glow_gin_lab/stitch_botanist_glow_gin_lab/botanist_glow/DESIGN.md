---
name: Botanist-Glow
colors:
  surface: '#f3faff'
  surface-dim: '#c7dde9'
  surface-bright: '#f3faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e6f6ff'
  surface-container: '#dbf1fe'
  surface-container-high: '#d5ecf8'
  surface-container-highest: '#cfe6f2'
  on-surface: '#071e27'
  on-surface-variant: '#3f4a3c'
  inverse-surface: '#1e333c'
  inverse-on-surface: '#dff4ff'
  outline: '#6f7a6b'
  outline-variant: '#becab9'
  surface-tint: '#006e1c'
  primary: '#006e1c'
  on-primary: '#ffffff'
  primary-container: '#4caf50'
  on-primary-container: '#003c0b'
  inverse-primary: '#78dc77'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#9a9b9b'
  on-tertiary-container: '#313333'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#94f990'
  primary-fixed-dim: '#78dc77'
  on-primary-fixed: '#002204'
  on-primary-fixed-variant: '#005313'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f3faff'
  on-background: '#071e27'
  surface-variant: '#cfe6f2'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: DM Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: DM Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-label:
    fontFamily: DM Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: DM Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-padding: 24px
  gutter: 16px
  section-gap: 48px
  pebble-padding: 20px
---

## Brand & Style

This design system is anchored in the intersection of artisanal distillation and modern luxury. The brand personality is luminous, refreshing, and deeply rooted in botanical authenticity. It targets a discerning, epicurean audience that values the tactile quality of premium spirits and the precision of craft infusions.

The visual style is a sophisticated blend of **Neomorphism** and **Organic Minimalism**. By utilizing soft, extruded UI elements and "pebble" shapes, the interface mimics the frosted surface of high-end glassware and the smooth edges of river-washed stones. The aesthetic avoids harsh digital edges in favor of a "Soft-UI" approach, creating a tactile environment that feels as refreshing as the product itself. Every interaction should feel gentle, premium, and inherently natural.

## Colors

The palette is defined by its transparency and vibrancy. **Leaf Green (#4CAF50)** serves as the primary accent, used sparingly to draw attention to botanical ingredients and call-to-action elements. **Glass-Cyan (#E0F7FA)** is the foundational background color, providing a cool, liquid-like atmosphere that allows Soft-UI highlights and shadows to manifest. 

**Pure White (#FFFFFF)** is used for the elevated "pebble" surfaces to create a sense of pristine purity. For neumorphic effects, use white for top-left highlights and a slightly deeper version of the Cyan base for bottom-right shadows to maintain a cohesive "glow" rather than a muddy grey appearance.

## Typography

The typographic hierarchy balances heritage and clarity. **EB Garamond** is the voice of the brand, utilized for headlines and display text to evoke the elegance of historical botanical catalogs and luxury spirit labeling. It should be typeset with generous leading to maintain an airy, premium feel.

**DM Sans** provides the functional counterpoint. It is used for all technical data, ingredient lists, and infusion instructions. Its low-contrast, geometric forms ensure high readability on mobile devices, even at smaller sizes. Data labels should use a bold weight with increased letter spacing to create a distinct visual "tag" for ingredient attributes.

## Layout & Spacing

Following a **mobile-first, fluid grid approach**, this design system prioritizes a centered, single-column flow that expands into a multi-column arrangement on larger displays. The layout relies on "safe margins" of 24px to prevent content from feeling cramped against the screen edges.

Vertical rhythm is driven by the **8px base unit**. Significant whitespace (section gaps of 48px or more) is intentional, reinforcing the luxury positioning by allowing the botanical imagery and tactile UI elements to "breathe." Content blocks are housed within organic pebble shapes, which use internal padding of 20px to ensure text never touches the curved boundaries.

## Elevation & Depth

Depth is achieved through **Soft-UI Neumorphism** rather than traditional elevation. Surfaces do not "float" with drop shadows; instead, they appear to be pushed out from or recessed into the Glass-Cyan background.

1.  **Extruded (Positive) Surface:** Use for primary cards and buttons. A 4px to 8px blur shadow is applied: white (#FFFFFF) on the top-left and a soft cyan-tinted shadow (#B2EBF2) on the bottom-right.
2.  **Recessed (Negative) Surface:** Use for input fields and search bars. Apply inner shadows to create a "pressed-in" look, suggesting a vessel or a container.
3.  **Luminous Glow:** For high-priority botanical features, apply a soft outer glow using Leaf Green (#4CAF50) at 15% opacity to simulate a light source within the glass.

## Shapes

The shape language is strictly **Organic and Curvilinear**. Sharp corners are non-existent in this design system. All containers, buttons, and image masks utilize high corner radii to create "pebble" and "pill" shapes.

This fluidity reflects the organic nature of the ingredients—leaves, berries, and liquid. Use asymmetric border radii (e.g., 60px 40px 70px 50px) for decorative background elements to enhance the artisanal, hand-crafted feel of the infusion process.

## Components

### Buttons
Buttons are pill-shaped and tactile. The primary action uses an extruded white surface with Leaf Green text. On "hover" or "active" states, the button should appear to "sink" (recess) into the surface using inner shadows.

### Cards (Pebbles)
Cards are the primary content containers. They should feature a soft-UI extrusion. For botanical infusions, cards can have an asymmetric organic shape rather than a standard pill.

### Ingredient Chips
Small, pill-shaped labels used for flavor notes (e.g., "Juniper," "Citrus"). These use a Glass-Cyan background with a subtle Leaf Green border and bold DM Sans labels.

### Input Fields
Inputs are recessed "wells" in the UI. The inner shadow indicates a field ready for data entry. Use the Serif typeface for the user's input to make the interaction feel like a personal entry in a botanist's journal.

### Infusion Progress Bars
A custom component featuring a thick, pill-shaped track (recessed) with a Leaf Green "liquid" fill (extruded) that moves as the infusion time elapses.

### Image Containers
Images of botanicals or bottles should be housed in soft, rounded "window" shapes that mimic the distortion and magnification found in thick glass bottles.