---
name: Apex Endurance
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c9ac'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9379'
  outline-variant: '#444933'
  surface-tint: '#abd600'
  primary: '#ffffff'
  on-primary: '#283500'
  primary-container: '#c3f400'
  on-primary-container: '#556d00'
  inverse-primary: '#506600'
  secondary: '#c6c6c6'
  on-secondary: '#303030'
  secondary-container: '#474747'
  on-secondary-container: '#b5b5b5'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c3f400'
  primary-fixed-dim: '#abd600'
  on-primary-fixed: '#161e00'
  on-primary-fixed-variant: '#3c4d00'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 80px
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
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
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
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  data-display:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: -0.01em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
---

## Brand & Style

This design system is built for a high-performance triathlon environment where speed and precision are paramount. The brand personality is aggressive, technical, and unapologetically loud. It targets elite athletes and high-achievers who demand data-rich interfaces and high-energy visuals.

The visual style is **High-Contrast / Bold** mixed with **Brutalism**. It utilizes a dark-mode-first approach to maximize the vibration of the primary neon color. The aesthetic avoids soft gradients or organic shapes, opting instead for a rigid, grid-based structure that feels like a precision instrument or a high-end race machine. The UI should evoke an immediate sense of urgency and adrenaline.

## Colors

The palette is restricted to a high-octane "Toxic Neon" and a "Deep Black" to ensure maximum visual impact.

- **Primary:** #CCFF00 (Neon Yellow) – Used for primary actions, critical data points, and active states.
- **Secondary/Background:** #000000 (Deep Black) – The canvas for all screens to provide an infinite depth and high contrast.
- **Surface:** #1A1A1A (Carbon Gray) – Used for card backgrounds and section containers to create subtle separation without losing the dark aesthetic.
- **Text/Action:** #FFFFFF (Pure White) – Reserved for high-readability body text and secondary icons.

Photography should be treated with a monochromatic high-contrast filter and overlaid with #CCFF00 at varying opacities to maintain brand consistency.

## Typography

This design system uses **Space Grotesk** for headings and technical labels to provide a geometric, high-performance feel. Its mechanical construction reinforces the "precision" aspect of the brand. For high-density data and long-form reading, **Inter** is used for its superior legibility at small sizes.

Headlines should always be set in bold or black weights with tight tracking. Use uppercase for labels and secondary navigation to evoke the look of technical equipment and racing timing systems.

## Layout & Spacing

The layout is strictly **Grid-based**, utilizing a 12-column system. The spacing rhythm is based on a 4px baseline, but large-scale layouts should favor generous, aggressive whitespace to let the high-impact typography breathe.

Elements should align to hard edges. Gutters are kept tight (16px) to maintain a dense, technical feel, while outer margins are wide (32px+) to frame the content like a viewfinder. Use "Power Strips"—thick vertical or horizontal Neon Yellow lines—to divide major sections of the layout.

## Elevation & Depth

This design system rejects traditional shadows and soft blurs. Depth is achieved through **Tonal Layers** and **Bold Borders**.

- **Level 0:** Deep Black (#000000) base background.
- **Level 1:** Carbon Gray (#1A1A1A) surfaces for cards and modules.
- **Level 2:** Strokes and Borders. Use 1px or 2px solid borders in #CCFF00 or #333333 to define interactive areas.
- **Interactions:** Hover states do not lift; they change color or reveal a solid Neon Yellow fill. No drop shadows are permitted; if depth is required, use a hard "drop-block" (a solid offset color block behind an element).

## Shapes

The shape language is strictly **Sharp**. Every button, card, input, and container must have a 0px border radius. This "Hard Edge" philosophy communicates the uncompromising nature of triathlon sports and the precision of the engineering behind it.

Diagonal cuts (45-degree angles) can be used on corners of buttons or decorative elements to further emphasize the "aggressive" and "aerodynamic" nature of the design system.

## Components

### Buttons
Primary buttons are solid Neon Yellow (#CCFF00) with Black text, utilizing a bold, uppercase label. Secondary buttons are ghost-style with a 2px Neon Yellow border. No rounded corners. The hover state should invert the colors or trigger a solid white fill.

### Cards
Cards use the Level 1 surface (#1A1A1A) with no border-radius. In high-performance data views, cards should have a 1px border. A "Neon Header" (a 4px solid top-border in #CCFF00) can be used to signify priority.

### Input Fields
Fields are Deep Black with a 1px white or gray border. On focus, the border changes to Neon Yellow. Labels are always small, uppercase, and placed above the field.

### Chips & Tags
Technical tags (e.g., "SWIM", "BIKE", "RUN") should be rectangular with solid black backgrounds and Neon Yellow borders/text. They should look like digital readouts.

### Data Visualizations
Charts should use solid Neon Yellow for the primary data line. Use high-contrast grid lines in #333333. Avoid area fills unless they are high-transparency neon overlays.

### Performance Overlays
Use "Crosshair" elements and grid-coordinate labels on photography to give an "augmented reality" or "heads-up display" (HUD) feel to the imagery.