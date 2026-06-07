---
name: Hardscape Raw
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4c4546'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#a63b00'
  on-secondary: '#ffffff'
  secondary-container: '#fe5f00'
  on-secondary-container: '#521900'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#191c1e'
  on-tertiary-container: '#818486'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#ffdbce'
  secondary-fixed-dim: '#ffb599'
  on-secondary-fixed: '#370e00'
  on-secondary-fixed-variant: '#7f2b00'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
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
  label-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
spacing:
  base: 4px
  unit-1: 8px
  unit-2: 16px
  unit-4: 32px
  unit-8: 64px
  unit-12: 96px
  border-thick: 2px
  border-heavy: 4px
---

## Brand & Style

The design system is rooted in the "Brutalist-Minimalist" movement, specifically tailored for the DIY masonry and concrete industry. It prioritizes the "as-is" state of materials, echoing the raw honesty of industrial construction. The aesthetic rejects decorative flourishes in favor of structural clarity and utilitarian efficiency. 

The UI should feel heavy, permanent, and functional. It aims to evoke the feeling of a technical manual or an architectural blueprint. By exposing the underlying grid and utilizing high-contrast outlines, the design system emphasizes precision and the physical weight of stone and concrete projects.

## Colors

The palette is derived from the physical materials of the trade. The foundation is built on **Cement Grey** and **Slate**, providing a neutral, textured backdrop. **Stark Black** is used for all structural elements, borders, and primary typography to ensure maximum readability and impact. 

**Industrial Safety Orange** serves as the sole accent color. It is reserved strictly for high-priority calls to action, warnings, or active states, mimicking the use of safety markers on a construction site. This high-contrast approach ensures that the interface remains functional even in high-glare outdoor environments typical of DIY projects.

## Typography

This design system utilizes a combination of **Space Grotesk** for headings to provide a technical, geometric edge, and **Inter** for body copy to maintain legibility. 

Type is treated as a structural element. Headings are oversized and tightly tracked to create a "block-like" visual density. Labels and technical data should be set in uppercase to reinforce the industrial documentation aesthetic. All type must remain sharp; no anti-aliasing softening or decorative ligatures are permitted.

## Layout & Spacing

The layout is governed by a **rigid 12-column geometric grid**. Unlike modern fluid systems that hide their structure, this design system celebrates it. Grid lines (2px black) should be visible between major sections to define the "blueprint" of the page.

Spacing is based on a strict 8px rhythm. Generous whitespace (minimum 64px between sections) is used to prevent the heavy borders and dark colors from feeling cluttered. Content blocks are "poured" into the grid containers, maintaining a fixed-width feel even within fluid containers to mimic the solid nature of masonry.

## Elevation & Depth

This design system is strictly **flat**. Depth is conveyed through **overlapping layers and thick borders** rather than shadows or gradients. 

When an element needs to sit "above" another, it is given a thicker 4px black border or a high-contrast background fill (e.g., a black box on a grey background). There is no Z-axis blur or translucency. If a modal or pop-over is required, it must have a solid, opaque background with a heavy border, creating a physical "heavy object" effect on the screen.

## Shapes

The shape language is defined by the **right angle**. Every element—from buttons and input fields to cards and images—must have a **0px border-radius**. 

The use of sharp corners reflects the precision of cut stone and the formwork used in concrete pouring. Circles are permitted only for functional icons where necessary for universal recognition (e.g., a circular "info" icon), but these should still be contained within square hit areas.

## Components

### Buttons
Primary buttons are solid Black with White text, using a 0px radius and a 2px border. The "Active" or "Call to Action" variant uses Safety Orange. On hover, buttons do not change color; instead, they shift 2px down and right to simulate a mechanical press, or they invert colors (White background, Black text).

### Cards
Cards are defined by 2px Black borders with no shadows. Headlines inside cards are always separated from content by a horizontal 2px line. The background of a card can be Slate or Cement to distinguish it from the main page background.

### Input Fields
Inputs are white-filled rectangular boxes with a 2px Black border. Labels are placed outside the box in a bold, uppercase technical font. Focus states are indicated by an Industrial Safety Orange border.

### Chips & Tags
Tags are styled as "Stencils." They use a light grey background with black monospace text, enclosed in a 1px black border. They should look like stamped serial numbers on a crate.

### Checkboxes & Radios
These must be perfectly square (for checkboxes) or diamonds (for radios). They use thick 2px strokes. The checked state is represented by a solid black fill or a large "X" mark, maintaining the raw, hand-marked feel of a construction site.

### Progress Bars
Progress is visualized as a solid block of Safety Orange moving through a Black-bordered container. The background of the bar should be the "Cement" grey color to represent the "unpoured" area.