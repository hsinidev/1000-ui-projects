---
name: Zenith-Gear Expedition System
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#47352e'
  surface-container-lowest: '#180b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362620'
  surface-container-highest: '#42312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb596'
  primary: '#ffb596'
  on-primary: '#581e00'
  primary-container: '#ff6600'
  on-primary-container: '#561d00'
  inverse-primary: '#a33e00'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#989696'
  on-tertiary-container: '#2f2f2f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb596'
  on-primary-fixed: '#360f00'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#42312a'
typography:
  display-xl:
    fontFamily: IBM Plex Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: IBM Plex Serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: IBM Plex Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 16px
  margin-mobile: 20px
---

## Brand & Style

This design system embodies the "Rugged-Luxe" aesthetic, merging the uncompromising durability required for extreme expeditions with the sophisticated precision of high-end engineering. It is designed for elite explorers who demand equipment that performs under pressure without sacrificing a premium feel.

The visual style is **Tactile & High-Contrast**. It draws inspiration from aerospace instrumentation and professional mountaineering equipment. The interface should feel like a piece of precision gear: heavy-duty, reliable, and technically advanced. We employ subtle metallic gradients and micro-textures—reminiscent of brushed titanium and carbon fiber—to create depth, while maintaining a rigorous, grid-based layout that prioritizes clarity in high-stress environments.

## Colors

The palette is anchored by **Charcoal (#222222)** and a deeper obsidian background to ensure maximum contrast and visual comfort in low-light environments. **Silver (#C0C0C0)** serves as the structural color, used for borders, icons, and secondary information to evoke the feel of machined metal.

**Safety Orange (#FF6600)** is the "Critical Action" color. It is reserved exclusively for high-visibility accents, primary Call-to-Actions (CTAs), and essential status indicators. This mimicry of expedition safety gear ensures that the most important interactions are immediately discoverable. Surface colors use a layered approach to define hierarchy, moving from a deep black base to lighter charcoal elevations.

## Typography

This design system utilizes a high-contrast typographic pairing to signal both heritage and technical modernity. 

- **Headlines:** We use **IBM Plex Serif** (Bold) to provide a heavy, industrial slab-serif feel. It communicates authority and the "Luxe" aspect of the brand through its structured, traditional bone-structure.
- **Body Text:** **Hanken Grotesk** provides a sharp, contemporary, and highly legible experience. Its neutral but precise character ensures that technical specifications and equipment details are easy to digest.
- **Data & Metadata:** **JetBrains Mono** is introduced for technical specs, coordinates, and pricing. This monospaced font reinforces the "technical precision" narrative.

All headings should be treated with tight tracking, while labels and data points utilize increased letter spacing for a "schematic" look.

## Layout & Spacing

This design system follows a **Fixed-Fluid Hybrid Grid**. On mobile, we utilize a strict 4-column system with 20px side margins to ensure content remains centered and impactful. For larger screens, a 12-column grid is used with a maximum content width of 1440px.

The spacing rhythm is strictly 8px-based to maintain a sense of mechanical alignment. Elements are grouped in "modules" that feel like nested compartments in a rugged equipment case. Significant whitespace is used between sections to elevate the "Luxe" feel, while dense, tight spacing is used within technical component cards to simulate an instrument cluster.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering and Material Textures** rather than traditional soft shadows. 

1.  **Base Layer:** The deepest background (#121212), representing the foundation.
2.  **Surface Layer:** Elevated containers use #1E1E1E with a subtle 1px Silver (#C0C0C0) border at 15% opacity to define the edge.
3.  **Active State:** Elements that are "active" or "pressed" may feature a faint inner glow or a metallic brushed texture overlay to simulate physical engagement.
4.  **Tactile Borders:** Instead of shadows, use "rim lighting"—a 1px top border that is slightly lighter than the rest of the element to suggest a light source hitting the top edge of a physical object.

## Shapes

To reinforce the industrial and rugged nature of the brand, this design system uses **Sharp (0px)** corners for almost all structural elements. 

The use of 90-degree angles suggests architecture, structural beams, and machined parts. This "zero-radius" philosophy applies to buttons, input fields, cards, and images. The only exception to this rule is for purely functional circular elements, such as radio buttons or specific circular status pips, to ensure they are instantly recognizable as interactive UI patterns.

## Components

### Buttons
Primary buttons use a solid **Safety Orange** fill with black text, utilizing the heavy slab-serif for maximum impact. Secondary buttons are outlined in **Silver** with a subtle hover state that introduces a metallic sheen or light-gray fill.

### Input Fields
Fields are dark-themed with a 1px Silver border. Upon focus, the border transitions to Safety Orange. Labels are always placed above the field in the **JetBrains Mono** label style to look like technical labels on a control panel.

### Cards
Cards for expedition gear should feel like "spec sheets." They utilize high-contrast product photography against a Charcoal background, with technical details (weight, temperature rating, etc.) aligned to a sub-grid using the monospaced font.

### Progress & Status
Use "heavy-duty" progress bars—thicker than standard—with a segmented design to look like battery or fuel indicators. Safety Orange is used for critical levels, while Silver is used for standard progress.

### Interactive Accents
Incorporate "Crosshair" or "Coordinate" markers in corners of images or sections to enhance the expedition/navigational feel.