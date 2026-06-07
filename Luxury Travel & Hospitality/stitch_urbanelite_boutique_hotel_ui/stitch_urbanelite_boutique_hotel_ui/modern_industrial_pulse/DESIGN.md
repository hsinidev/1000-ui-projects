---
name: Modern Industrial Pulse
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1c1c1c'
  on-primary-container: '#858484'
  inverse-primary: '#5f5e5e'
  secondary: '#bcc3ff'
  on-secondary: '#001a97'
  secondary-container: '#0033fe'
  on-secondary-container: '#c4caff'
  tertiary: '#c6c6c7'
  on-tertiary: '#2f3131'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#dfe0ff'
  secondary-fixed-dim: '#bcc3ff'
  on-secondary-fixed: '#000d60'
  on-secondary-fixed-variant: '#0029d3'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin: 48px
  container-max: 1280px
---

## Brand & Style

The design system is engineered to reflect the raw, structural energy of a metropolitan center while maintaining the exclusivity of a high-end boutique hotel. The brand personality is aggressive yet sophisticated—a "nocturnal luxury" that favors bold architectural lines over soft ornaments.

The style leverages a fusion of **High-Contrast Bold** and **Minimalism**. It utilizes the "void" of dark space to emphasize key information and the "pulse" of high-energy color to guide the user journey. The interface should feel like a piece of precision-machined equipment: heavy, solid, and impeccably finished. To achieve the industrial look, use subtle noise overlays to mimic concrete textures and hairline strokes to represent metallic joinery.

## Colors

This design system operates primarily in a dark mode environment to simulate the sleek, nighttime atmosphere of a premium city hotel. 

- **Graphite (#1C1C1C):** The foundation. Use this for all primary backgrounds and structural surfaces.
- **Electric Blue (#0033FF):** The high-energy accent. This is reserved exclusively for interactive elements, primary calls to action, and focus states. It represents the digital pulse of the city.
- **Pure White (#FFFFFF):** Used for maximum legibility of content and high-contrast block elements. 
- **Industrial Grey (#333333):** A secondary neutral for borders, dividers, and "metal" surface accents.

## Typography

The typography system is built on a foundation of structural clarity. **Space Grotesk** is used for all headlines and labels to provide a technical, geometric edge that aligns with the industrial aesthetic. Use **Inter** for body copy to ensure maximum readability and a neutral, systematic feel.

All major headlines should be treated as architectural elements. Use tight letter-spacing on large headings to create a dense, "blocky" feel. Labels should always be in uppercase with increased letter-spacing to mimic industrial stencil markings.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model. On desktop, content is constrained to a 1280px 12-column grid to maintain a premium, editorial feel that doesn't feel overly "stretched."

The spacing rhythm is strictly based on an 8px baseline. Use generous margins (48px+) to create an atmosphere of luxury and space. Elements should be aligned to a rigid grid, with high-contrast color blocks used to define sections rather than relying on whitespace alone. This "boxed" layout approach reinforces the industrial, modular nature of the design.

## Elevation & Depth

Elevation in this design system is achieved through **Tonal Layers** and **Low-Contrast Outlines** rather than traditional shadows. 

1.  **Surfaces:** Use shifts in Graphite shades (e.g., from #1C1C1C to #252525) to indicate stacking.
2.  **Borders:** Use 1px "Metallic" strokes (#FFFFFF at 10-15% opacity) to define component boundaries. This mimics the appearance of milled metal edges.
3.  **Active Depth:** When an element is focused, use the Electric Blue as a glowing outer stroke (0px blur, 2px spread) to simulate an illuminated conduit or neon accent.
4.  **Texture:** Apply a 3% opacity grain/noise texture to the base Graphite layer to provide the tactile feel of polished concrete.

## Shapes

The shape language is strictly **Sharp (0px)**. To maintain the Modern Industrial aesthetic, all containers, buttons, and input fields must have hard 90-degree angles. This evokes the feeling of structural steel beams and cut stone. 

Avoid all rounded corners, even in small UI elements like checkboxes or tags. The only exception is the use of circular icons when necessary for standard symbol recognition, though these should ideally be contained within square enclosures.

## Components

- **Buttons:** Primary buttons are solid Electric Blue with White text, using Space Grotesk Bold. Secondary buttons use a White 1px border with no fill. All buttons are rectangular with no corner radius.
- **Input Fields:** Use a "Bottom Border Only" style (2px thickness) in White for an architectural look. Upon focus, the border and the label text transition to Electric Blue.
- **Cards:** Cards should utilize full-bleed photography of urban environments or hotel interiors. Text should be placed in high-contrast color blocks (e.g., White text on a Graphite block) that overlap the image, creating a layered, editorial look.
- **Chips/Tags:** Small rectangular blocks with solid White fills and Graphite text, or vice versa. No rounded edges.
- **Lists:** Separated by thin 1px horizontal lines (#333333), resembling a technical specification sheet.
- **Additional Components:** "Pulse Indicators"—small Electric Blue square pips used next to status text or availability indicators to show high-energy activity.