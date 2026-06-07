---
name: Luminous Precision
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#b9cac9'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#839493'
  outline-variant: '#3a4a49'
  surface-tint: '#00dddd'
  primary: '#ffffff'
  on-primary: '#003737'
  primary-container: '#00fbfb'
  on-primary-container: '#007070'
  inverse-primary: '#006a6a'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#ffffff'
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#00fbfb'
  primary-fixed-dim: '#00dddd'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '300'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin-page: 64px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system centers on the intersection of structural engineering and optical clarity. It is designed to evoke the feeling of standing inside a high-rise atrium: expansive, transparent, and meticulously calculated. The brand personality is elite, technical, and avant-garde, catering to architects and developers who value precision over ornamentation.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. By stripping away unnecessary depth markers like shadows and replacing them with ultra-thin "structural" borders and refraction effects, the UI mimics the physical properties of high-end architectural glass. The aesthetic prioritizes legibility and a sense of "lightness" despite its dark, high-contrast foundation.

## Colors

The palette is strictly limited to maintain an atmosphere of technical sophistication. 

- **Crystal Cyan**: Used sparingly as a "laser-precision" accent for active states, data points, and critical calls to action. It represents the edge of a glass pane catching the light.
- **Deep Black & Pure White**: These form the structural core of the design system. The background is a true Deep Black to allow translucent layers and cyan accents to vibrate with maximum contrast.
- **Translucency**: A fundamental "color" in this system is the 10-20% opacity white or cyan used for glass layers, creating a sense of depth without adding visual weight.

## Typography

This design system utilizes **Space Grotesk** for headlines and labels to reinforce the architectural and technical nature of the firm. Its geometric quirks provide a "blueprint" feel. **Manrope** is used for body text to ensure maximum readability and a premium, balanced tone.

Typographic hierarchy is achieved through scale and tracking rather than heavy weights. Headlines should remain light or regular to feel airy. High-contrast labels should always be uppercase with increased letter spacing to mimic architectural notations.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model, strictly aligned to a 12-column system. This reflects the rigidity and safety of commercial glazing structures. 

Large, intentional margins (64px+) are used to frame content like a gallery exhibit. Spacing is used to create "breathing room" between technical data points, ensuring the UI never feels cluttered despite the high-information density. Elements should be aligned to a 4px baseline grid to maintain mathematical precision in every view.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and layering rather than traditional shadows. 

- **Backdrop Blur**: Every surface layer must use a high-density backdrop blur (20px - 40px) to simulate frosted glass.
- **Ultra-Thin Borders**: Instead of shadows, surfaces are defined by 0.5pt or 1pt borders. Use a semi-transparent white (15% opacity) for top and left borders to simulate a "light edge," and a darker or lower-opacity stroke for bottom and right edges.
- **Z-Axis Hierarchy**: Higher elevation levels are indicated by increased transparency (letting more background color through) and sharper border definitions. No drop shadows are permitted; depth must feel like physical layers of glass stacked on top of one another.

## Shapes

The shape language is strictly **Sharp**. There are no rounded corners in this design system. Every container, button, and input field must have 0px border-radius to reflect the cut-glass nature of the industry. 

The use of 45-degree angled cuts is permitted for decorative elements or specific UI tags to further emphasize the architectural theme. Visual interest is generated through the intersection of straight lines and the play of light through translucent fills.

## Components

### Buttons
Primary buttons use a "Ghost" style: a 1px Crystal Cyan border with a very low-opacity cyan fill. Upon hover, the fill opacity increases, and the border glows slightly using a cyan outer stroke (not a shadow). Secondary buttons are Pure White strokes with no fill.

### Cards
Cards are the primary container for the glassmorphism effect. They feature a 0.5px white border at 20% opacity and a backdrop blur. Content inside cards should be padded generously (32px+) to maintain the minimalist aesthetic.

### Input Fields
Inputs are bottom-border only (1px white). When focused, the border transitions to Crystal Cyan and a subtle, vertical "scanning" line appears momentarily to signify the precision of the system.

### Progress & Data Visualization
Use thin, 2px lines for progress bars. Data visualizations should exclusively use Crystal Cyan for the primary data line, with thin, grey 0.5px grid lines in the background.

### Architectural Photography Frames
All imagery should be treated as a structural component. Use "Ken Burns" subtle zoom animations on hover to give life to static glass structures. Images should be slightly desaturated to allow the Crystal Cyan UI elements to stand out.