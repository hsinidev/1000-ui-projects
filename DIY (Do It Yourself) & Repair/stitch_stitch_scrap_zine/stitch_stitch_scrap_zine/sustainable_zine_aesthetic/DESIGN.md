---
name: Sustainable Zine Aesthetic
colors:
  surface: '#fdf8f8'
  surface-dim: '#ddd9d9'
  surface-bright: '#fdf8f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f7f3f2'
  surface-container: '#f1edec'
  surface-container-high: '#ebe7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#46474a'
  inverse-surface: '#313030'
  inverse-on-surface: '#f4f0ef'
  outline: '#76777b'
  outline-variant: '#c7c6ca'
  surface-tint: '#5f5e5f'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1c'
  on-primary-container: '#858384'
  inverse-primary: '#c8c6c7'
  secondary: '#5f5e59'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2db'
  on-secondary-container: '#65645f'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#161e00'
  on-tertiary-container: '#718e00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e5e2e3'
  primary-fixed-dim: '#c8c6c7'
  on-primary-fixed: '#1b1b1c'
  on-primary-fixed-variant: '#474647'
  secondary-fixed: '#e5e2db'
  secondary-fixed-dim: '#c9c6c0'
  on-secondary-fixed: '#1c1c18'
  on-secondary-fixed-variant: '#474742'
  tertiary-fixed: '#c3f400'
  tertiary-fixed-dim: '#abd600'
  on-tertiary-fixed: '#161e00'
  on-tertiary-fixed-variant: '#3c4d00'
  background: '#fdf8f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 32px
  container-max: 1280px
---

## Brand & Style

The design system is rooted in the **Tactile Neo-Brutalism** movement, blending the raw, unapologetic nature of DIY punk zines with the intentionality of modern sustainability movements. It is designed to evoke a sense of creative urgency and "found-object" authenticity, moving away from the polished, sterile look of traditional e-commerce or blogs.

The target audience consists of makers, upcyclers, and eco-conscious activists who value the "process" as much as the "product." The UI should feel assembled rather than programmed—using grit, high-contrast visuals, and overlapping textures to create a digital collage that rewards exploration. The emotional response is one of rebellion against fast fashion, channeled through a visual language that feels hand-made, recycled, and repurposed.

## Colors

The palette for this design system mimics the limitations of physical printing. 

- **Ink Black (#1A1A1B):** A deep, slightly charcoal-toned black used for heavy borders, primary text, and "marker" strokes. It should never be pure #000, maintaining a matte, printed feel.
- **Newsprint (#F4F1EA):** The primary background color. It provides a warm, recycled paper texture that reduces eye strain and reinforces the upcycled theme.
- **Neon Green (#CCFF00):** A high-visibility "sustainability" accent. Used for highlights, calls to action, and alerts. It represents the "vibrancy of new life" found in upcycled goods.
- **Electric Blue (#2E5BFF):** An "ink-stain" accent used for links, secondary actions, and decorative overlaps. It simulates the over-saturation of cheap riser-graph printing.

Color application should often feel "misregistered," with accents slightly offset from their containers to mimic low-fidelity printing errors.

## Typography

Typography in this design system is a clash between the traditional and the industrial. 

**Newsreader** is utilized for headlines to provide a literary, editorial authority. It should be used in heavy weights with tight tracking to create a "blocky" magazine feel. Use italics sparingly for emphasis, mimicking hand-corrected manuscripts.

**Space Grotesk** serves as the functional, industrial backbone for body copy and UI labels. Its geometric and slightly technical nature provides a sharp contrast to the serif headlines, suggesting the "instructional" or "blueprint" aspect of upcycling and DIY fashion.

For maximum zine-impact, headlines may occasionally be set with a background "highlight" or "black-out" box to simulate clippings glued onto the page.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid with Intentional Disruption**. While a standard 12-column grid provides the structural foundation, elements are encouraged to "break" the grid through rotation (1-3 degrees) and overlapping margins.

- **The Clipping Effect:** Elements like images or callouts should use negative margins to overlap adjacent sections, creating a layered, collage-like appearance.
- **Rhythm:** A strict 4px/8px baseline is used for internal component spacing, but external layout spacing is intentionally irregular to avoid a "corporate" symmetry.
- **Gutters:** Wide 24px gutters ensure that even when elements overlap, the primary content remains legible. 
- **Margins:** Page containers use generous 32px margins to prevent content from hitting the edge of the viewport, simulating the "safe area" of a physical print.

## Elevation & Depth

This design system rejects ambient, soft shadows in favor of **Structural Layering** and **Hard Offsets**.

- **Stacked Layers:** Hierarchy is communicated by physical stacking. Use high z-index values and "paper-tear" CSS masks to make elements appear as if they are sitting on top of one another.
- **Hard Shadows:** Use "drop-shadow" effects with 0 blur and 4px-8px offsets. These should be colored in `Ink Black` or `Electric Blue` to create a "pop-out" effect similar to stickers or thick cardboard cutouts.
- **Borders:** Every container must have a visible border (minimum 2px). Borders are the primary way to define elevation, rather than light or shadow.
- **Texture:** A global "grain" overlay (low-opacity noise) should be applied to the background to give the entire interface a tactile, newsprint surface quality.

## Shapes

The shape language is strictly **Sharp and Angular**. 

- **Corners:** Standard corners are 0px (Sharp). This reflects the aesthetic of paper being cut with scissors or a utility knife.
- **Irregular Edges:** Use SVG masks to create "jagged" or "torn" edges on the top or bottom of cards and sections. 
- **Tape Elements:** Decorative elements or buttons should use a "masking tape" shape—long rectangles with slightly irregular, torn ends.
- **Stroke Weights:** Use varying stroke weights (2px for standard, 4px for emphasis) to create a hand-drawn, marker-heavy feel.

## Components

### Buttons
Buttons do not look like digital inputs. They are styled as **Adhesive Tape**. 
- **Primary:** Neon Green background with Ink Black text, using a jagged "torn" edge mask on the left and right.
- **Secondary:** Hand-drawn border (irregular width) with a hover effect that fills the background with a "scribble" texture.

### Cards
Cards mimic **Magazine Clippings**. 
- They should have a 1px solid border and a 6px hard offset shadow. 
- Images within cards should have a white "Polaroid" border. 
- Content inside should look slightly unaligned, as if pasted in a hurry.

### Input Fields
Inputs are styled as **Marker Underlines**. Instead of a full box, use a heavy 4px bottom border. On focus, the border color shifts to Electric Blue, and a small "hand-drawn" checkmark or arrow appears.

### Chips & Tags
Chips look like **Dymo Embossed Labels** or small scraps of paper. Use high-contrast color pairings (White on Black) and sharp corners.

### Special Component: "The Scrapbook Header"
A decorative component for article intros that combines a large serif headline, a "cut-out" image with a rough mask, and a "piece of tape" (the category tag) overlapping the corner of the image.