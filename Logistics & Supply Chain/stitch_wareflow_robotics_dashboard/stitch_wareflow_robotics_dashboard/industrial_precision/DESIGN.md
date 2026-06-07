---
name: Industrial Precision
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#c8c6c5'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b6b5b4'
  tertiary: '#f7f6f6'
  on-tertiary: '#2f3131'
  tertiary-container: '#dadada'
  on-tertiary-container: '#5e5f60'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
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
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
spacing:
  unit: 8px
  gutter: 16px
  margin: 24px
  container-padding: 20px
  bento-gap: 12px
---

## Brand & Style

This design system is built for the high-stakes environment of modern logistics and robotics. The personality is unapologetically utilitarian, prioritizing speed of recognition and technical accuracy over decorative flair. It draws heavily from **Modern Industrialism** and **Brutalism**, utilizing a strict "Bento-box" grid layout to compartmentalize complex data streams into digestible, actionable modules.

The aesthetic evokes the feeling of a high-end control room: high-contrast, strictly organized, and resilient. It communicates reliability and mechanical efficiency, ensuring that warehouse operators and floor managers can navigate dense information architectures without cognitive fatigue. The UI should feel like a piece of precision machinery—cold, calculated, and highly responsive.

## Colors

The palette is rooted in safety and visibility standards. **Safety Yellow (#FFD700)** is the primary action and highlight color, used sparingly to draw immediate attention to critical status changes, primary buttons, and alerts. **Charcoal (#2C2C2C)** serves as the primary surface color, providing a low-glare foundation suitable for long shifts in industrial environments.

**Light Grey (#E5E5E5)** is reserved for high-readability text and structural borders. A deeper **Neutral (#1A1A1A)** is used for background layers to create a sense of depth without relying on shadows. This high-contrast approach ensures that the interface remains legible under harsh warehouse lighting or on mobile ruggedized tablets.

## Typography

The typography strategy pairs **Space Grotesk** for headlines and **Inter** for functional text. Space Grotesk provides a technical, geometric edge that mimics architectural blueprints and industrial signage. Inter is utilized for its exceptional legibility in data-heavy environments, particularly for SKU numbers, quantities, and logistics coordinates.

Use `label-caps` for all non-interactive headers within bento-box modules to mimic stamped industrial plates. All numerical data should prioritize the `mono-data` style to ensure vertical alignment in tables and lists, facilitating rapid scanning of inventory levels.

## Layout & Spacing

The layout follows a strict **Bento-box grid** model. Content is organized into discrete rectangular containers that sit on a 12-column fluid grid. This ensures that the UI can scale from large terminal monitors to handheld scanners without losing structural integrity.

Spacing is governed by an 8px base unit. Containers within the bento grid should maintain a consistent 12px gap to emphasize the modularity of the system. Internal padding within modules should be generous (20px) to prevent data clusters from feeling cluttered, maintaining a "technical-clean" look.

## Elevation & Depth

This design system rejects traditional shadows in favor of **Bold Borders** and **Tonal Layers**. Depth is communicated through color stacking rather than light source simulation. 

1. **Floor:** The deepest layer (#1A1A1A).
2. **Modules:** Bento containers use #2C2C2C with a 1px solid border of #3D3D3D.
3. **Interactive:** Active elements or hovered modules use a Safety Yellow border to indicate focus.
4. **Overlay:** Modals or tooltips use a solid #2C2C2C fill with a high-contrast #E5E5E5 border to "cut" through the background.

Use hairline strokes for all separators to maintain a precise, engineered feel.

## Shapes

The shape language is strictly **Sharp (0)**. There are no rounded corners in the core design system. This reinforces the industrial, rugged nature of the product. Every button, input field, and bento-box container must feature 90-degree angles to maintain a cohesive, machine-like aesthetic. 

When necessary to indicate "soft" interactions (like status dots or user avatars), use octagons or chamfered corners rather than circles to stay consistent with the technical theme.

## Components

### Buttons
Primary buttons are solid Safety Yellow with black text, utilizing a heavy 2px black bottom border for a tactile "press" effect. Secondary buttons use a Charcoal fill with a Light Grey border. 

### Bento Cards
Each card must feature a `label-caps` header in the top-left corner, often accompanied by a small industrial icon (e.g., a forklift, a gear, or a barcode). Cards should have a hover state that lightens the background hex slightly to indicate interactivity.

### Data Inputs
Input fields are dark containers with a bottom-only border of Light Grey. Upon focus, the border shifts to Safety Yellow and the label floats above the field in a smaller caps font.

### Chips & Status Indicators
Status indicators should use "Hazard Styling." For example, a "Critical" status chip features diagonal yellow and black warning stripes as a border. "Normal" status uses a simple Light Grey outline.

### Icons
Icons must be "Heavyweight Technical" style—drawn with a consistent 2px stroke, utilizing open paths and geometric shapes. Avoid rounded terminals; all icon ends should be butt-capped for a sharper appearance.