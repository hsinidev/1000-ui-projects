---
name: Precision-Luxe
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2b2a2a'
  surface-container-highest: '#353434'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c7c7'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9192'
  outline-variant: '#444748'
  surface-tint: '#c8c6c5'
  primary: '#c8c6c5'
  on-primary: '#313030'
  primary-container: '#1a1a1a'
  on-primary-container: '#848282'
  inverse-primary: '#5f5e5e'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#00dddd'
  on-tertiary: '#003737'
  tertiary-container: '#001e1e'
  on-tertiary-container: '#009292'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e5e2e1'
  primary-fixed-dim: '#c8c6c5'
  on-primary-fixed: '#1c1b1b'
  on-primary-fixed-variant: '#474746'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#00fbfb'
  tertiary-fixed-dim: '#00dddd'
  on-tertiary-fixed: '#002020'
  on-tertiary-fixed-variant: '#004f4f'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.04em
  spec-data:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-mono:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  precision-unit: 4px
  gutter: 24px
  margin-edge: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to evoke the tactile precision of high-end cinema optics. It targets an elite audience of cinematographers and technical directors who value industrial reliability and optical clarity. The aesthetic combines **Industrial Minimalism** with **Technical Glassmorphism**, creating an environment that feels like a high-tech cleanroom or a lens calibration laboratory.

The emotional response should be one of "Optical Authority"—confidence in the gear and the data presented. Visuals are defined by high-contrast interfaces, razor-sharp edges, and a "Focus-Pull" depth strategy that uses variable blurring to direct user attention with surgical precision.

## Colors

The palette is anchored in a monochromatic "Deep Charcoal" base to mimic the anodized aluminum of lens barrels. "Silver" serves as the primary structural color, used for technical borders, dividers, and inactive icons, reflecting the metallic components of professional camera mounts.

"Laser-Cyan" is the solitary high-visibility accent. It is reserved exclusively for interactive elements, active states, and data visualizations (such as focal charts or MTF curves). This color mimics the illuminated digital readouts on high-end follow-focus systems.

## Typography

This design system utilizes two distinct typographic voices. **Space Grotesk** is used for all primary headings. It should be styled with wide-set tracking (letter-spacing) to emphasize its architectural and geometric qualities.

**Inter** handles all functional information. For lens specifications and technical data, Inter should be set in Uppercase with increased letter-spacing to mimic industrial engravings. Body text remains clean and highly legible, prioritizing the transmission of technical specifications over decorative flair.

## Layout & Spacing

The layout philosophy follows a **Fixed 12-Column Grid** with a strict 8px/4px underlying rhythm. Content is organized into "Technical Modules" that snap to the grid, reinforcing the feeling of a precision-engineered instrument.

Margins are generous to provide breathing room for high-fidelity product imagery, while gutters remain tight to maintain a sense of structural density. Vertical spacing should be used to clearly delineate technical spec sheets from lifestyle editorial sections.

## Elevation & Depth

Depth in the design system is achieved through "Optical Layering" rather than traditional drop shadows.
- **Silver Strokes:** All containers are defined by 1px solid Silver strokes. No soft shadows are permitted.
- **Focus-Pull Blurs:** Background surfaces utilize `backdrop-filter: blur(12px)` to simulate the bokeh of a wide-open lens. This "out of focus" effect is used to separate modals and floating panels from the primary content.
- **Z-Axis Hierarchy:** Higher elevation layers are indicated by increased transparency in the charcoal background, revealing more of the silver-stroked grid beneath through the glassmorphic blur.

## Shapes

The shape language is strictly **Sharp (0px)**. There are no rounded corners in this design system. Every button, input field, card, and image frame must have 90-degree angles to reflect the industrial manufacturing of camera equipment and the precision of optical glass.

Visual interest is created through internal 45-degree chamfers on specific interactive elements (like the corners of a "Live View" frame) to mimic camera viewfinder masks.

## Components

- **Buttons:** Primary buttons are "Ghost" style with a 1px Silver stroke and Laser-Cyan text. On hover, they fill with Laser-Cyan and switch text to Deep Charcoal.
- **Cards:** Product cards utilize a subtle "Glass" background with a 1px Silver top-border. Technical specs are listed in a grid format inside the card.
- **Data Visualization:** MTF and Distortion charts must use Laser-Cyan lines against the Deep Charcoal background for maximum contrast.
- **Focus-Pull Modals:** Overlays that dim the background and apply a heavy blur, forcing the user's "visual focus" onto the central content.
- **Status Indicators:** Small, circular dots in Laser-Cyan (for "In Stock") or Silver (for "Out of Stock"), evoking the look of illuminated tally lights on a cinema camera.
- **Input Fields:** Bottom-border only, using Silver. When active, the border transitions to Laser-Cyan with a subtle glow (1px spread).