---
name: DesignSprint UI
colors:
  surface: '#fff7fe'
  surface-dim: '#e1d7e3'
  surface-bright: '#fff7fe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf0fd'
  surface-container: '#f5eaf7'
  surface-container-high: '#efe5f1'
  surface-container-highest: '#eadfec'
  on-surface: '#1f1a22'
  on-surface-variant: '#4c4353'
  inverse-surface: '#342e38'
  inverse-on-surface: '#f8edfa'
  outline: '#7e7384'
  outline-variant: '#cfc2d5'
  surface-tint: '#8234c6'
  primary: '#6100a4'
  on-primary: '#ffffff'
  primary-container: '#7b2cbf'
  on-primary-container: '#e4c2ff'
  inverse-primary: '#deb7ff'
  secondary: '#a03b56'
  on-secondary: '#ffffff'
  secondary-container: '#ff85a1'
  on-secondary-container: '#781b38'
  tertiary: '#414141'
  on-tertiary: '#ffffff'
  tertiary-container: '#595858'
  on-tertiary-container: '#d1cece'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f1dbff'
  primary-fixed-dim: '#deb7ff'
  on-primary-fixed: '#2d0050'
  on-primary-fixed-variant: '#680eac'
  secondary-fixed: '#ffd9df'
  secondary-fixed-dim: '#ffb1c0'
  on-secondary-fixed: '#3f0016'
  on-secondary-fixed-variant: '#81233f'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#fff7fe'
  on-background: '#1f1a22'
  surface-variant: '#eadfec'
typography:
  display-xl:
    fontFamily: Epilogue
    fontSize: 84px
    fontWeight: '700'
    lineHeight: 92px
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Epilogue
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 30px
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 32px
  margin-edge: 64px
  container-max: 1440px
  section-gap: 160px
---

## Brand & Style

This design system is built on the intersection of academic rigor and avant-garde creative expression. It is designed to position the accelerator as an elite, high-performance environment for high-end design talent. The aesthetic balances the austerity of Swiss Minimalism with the expressive energy of a fashion editorial.

The visual style utilizes "maximalist minimalism"—where the canvas is sparsely populated, but every element is bold and intentional. We employ asymmetrical compositions to create a sense of movement and "planned chaos," signaling that this is a place for innovation rather than standard corporate patterns. High-resolution, grain-textured imagery and ultra-smooth micro-interactions elevate the experience to a premium, gallery-like level.

## Colors

The palette is anchored by the purity of White (#FFFFFF), which serves as the negative space required for an editorial layout. Vibrant Purple (#7B2CBF) is used as the primary signal color, representing ambition and depth, while Soft Pink (#FF85A1) acts as a high-contrast accent for interactive highlights and secondary details.

Deep Charcoal (#121212) is introduced for typography and structural lines to provide a more sophisticated grounding than pure black. Gradients are avoided in favor of flat, confident color blocks and tinted overlays on imagery.

## Typography

This design system utilizes a dual-typeface approach to distinguish between "art" and "utility." **Epilogue** is used for large-scale headlines; its geometric and distinctive character provides the editorial "edge" required for an artistic brand. **Inter** is used for all body copy and functional UI elements, ensuring maximum readability and a professional, systematic feel.

Typography should often be used as a graphic element itself. Massive display type should be used with tight tracking to create high-impact visual anchors, while label styles are set in uppercase with generous letter spacing to evoke a sense of architectural labeling.

## Layout & Spacing

The layout philosophy follows a rigid 12-column editorial grid, but elements are frequently offset to create asymmetrical interest. Content should not always center-align; instead, use wide margins and "pull-quote" positioning where text blocks sit in the gutters.

Whitespace is the primary tool for hierarchy. Sections are separated by large vertical gaps (160px+) to allow the eye to rest between intense visual sections. Elements should feel like they are floating within a structured, invisible framework.

## Elevation & Depth

This design system avoids traditional drop shadows to maintain a clean, high-fashion aesthetic. Instead, it uses **Tonal Layers** and **Low-Contrast Outlines**. 

Depth is achieved through layering:
1.  **Base:** Pure White background.
2.  **Mid:** Subtle off-white or very light pink surfaces (#FFF5F7) for container separation.
3.  **High:** Interaction states use crisp 1px borders in the primary Purple or Secondary Pink.

For high-resolution imagery, use subtle "Glassmorphism" for captions—utilizing a heavy backdrop blur (20px) and 80% opacity white fills to ensure text remains legible without obscuring the art.

## Shapes

The shape language is strictly **Sharp (0px)**. To maintain an "Editorial" and "Professional" aesthetic, UI elements like buttons, input fields, and image containers must have hard 90-degree corners. This evokes a sense of precision, architectural structure, and high-end design magazines. 

The only exception to this rule is the use of circular "Pill" shapes for decorative tags or specialized "play" buttons to provide a singular point of visual contrast against the otherwise rectilinear grid.

## Components

### Buttons
Primary buttons are solid Purple with White text, sharp-edged. The hover state should trigger a horizontal "slide-in" fill of Pink or a simple inversion of colors. Secondary buttons use a 1px Charcoal border with no fill.

### Input Fields
Inputs are minimalist, consisting only of a bottom border (1px Charcoal). Labels use the "label-caps" typography style and sit above the line. Error states replace the Charcoal border with a Pink border.

### Cards
Cards do not use shadows. They are defined by their content and occasional 1px light grey borders. When featuring imagery, the image should bleed to the edges of the card container.

### Lists & Navigation
Navigation links should use a "strikethrough" or "underline" animation on hover, using the Pink accent color. List items should be separated by thin, full-width horizontal rules to reinforce the grid.

### Images
All imagery should have a consistent "grain" overlay. Use asymmetrical aspect ratios (e.g., 4:5 or 2:3) rather than standard 16:9 to maintain the artistic feel.