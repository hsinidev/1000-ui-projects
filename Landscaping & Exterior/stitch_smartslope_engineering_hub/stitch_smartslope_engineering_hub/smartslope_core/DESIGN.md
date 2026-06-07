---
name: SmartSlope Core
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
  on-surface-variant: '#d2c4ba'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9b8f85'
  outline-variant: '#4e453d'
  surface-tint: '#e1c1a4'
  primary: '#e1c1a4'
  on-primary: '#402c18'
  primary-container: '#4b3621'
  on-primary-container: '#bd9f83'
  inverse-primary: '#725a42'
  secondary: '#b8c8da'
  on-secondary: '#223240'
  secondary-container: '#394857'
  on-secondary-container: '#a7b7c8'
  tertiary: '#e9c400'
  on-tertiary: '#3a3000'
  tertiary-container: '#c9a900'
  on-tertiary-container: '#4c3e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#fedcbe'
  primary-fixed-dim: '#e1c1a4'
  on-primary-fixed: '#291806'
  on-primary-fixed-variant: '#59422c'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#ffe16d'
  tertiary-fixed-dim: '#e9c400'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#544600'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
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
  data-lg:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  data-md:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  container-max: 1440px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered for the "Rugged-Medical" aesthetic—a hybrid of heavy-duty industrial engineering and high-stakes medical precision. It communicates extreme reliability, technical expertise, and structural integrity. The target audience includes civil engineers, environmental consultants, and large-scale developers who require absolute certainty in hillside stabilization.

The visual style leans heavily into **Brutalism** and **Technical Minimalism**. It utilizes raw structural elements, such as visible grid lines and data-rich readouts, to evoke the feeling of a field-grade diagnostic tool. Backgrounds feature subtle topographic map overlays (isoline patterns) to ground the interface in the physical geography of the company's work. The emotional response should be one of "industrial confidence"—the digital equivalent of a high-end, waterproof field tablet.

## Colors

This design system utilizes a dark-mode default to emphasize high-contrast technical readouts and minimize glare for field use. 

- **Deep Earthy Brown (#4B3621):** Used for structural grounding and deep-layered backgrounds.
- **Slate Grey (#708090):** Used for technical UI elements, secondary text, and inactive states.
- **Safety Yellow (#FFD700):** Reserved exclusively for high-priority Call-to-Action (CTA) elements, critical alerts, and active status indicators.
- **Surface Palette:** The interface uses a dark charcoal (#1A1A1A) foundation with slate-tinted borders to maintain a rugged, metallic feel.

## Typography

Typography is divided into two distinct functional categories: **Authoritative** and **Analytical**.

**Inter** provides the authoritative backbone. Headlines are set with tight tracking and heavy weights to simulate the permanence of stamped metal or architectural plans. 

**Space Grotesk** is used for all technical data, labels, and readouts. Its geometric, technical character mimics laboratory equipment displays. Use `label-caps` for all table headers, small captions, and "status" metadata to reinforce the medical-grade precision of the company’s data.

## Layout & Spacing

This design system employs a **Fixed Grid** model based on a 12-column architectural layout. To reinforce the "Rugged" theme, the grid is often made visible through thin (1px) Slate Grey borders that divide major sections.

The spacing rhythm is strict and linear, using a 4px base unit. Larger margins (40px) are used on the outer edges of the viewport to create a "protected" feel for the content, while internal gutters (24px) provide enough breathing room for dense technical data. Elements should be aligned to the grid precisely, avoiding fluid or organic placements.

## Elevation & Depth

In alignment with the "Rugged-Medical" aesthetic, the design system avoids soft, ambient shadows. Depth is instead conveyed through **Tonal Layers** and **Structural Outlines**:

- **Stacking:** Surface elevations are created by layering darker or lighter shades of charcoal. Higher elevation elements use a lighter grey fill.
- **Borders:** All containers must have a 1px solid border (#333333). Active elements or focused states swap this for a 1px Safety Yellow or Slate Grey border.
- **Scrims:** Backgrounds utilize a low-opacity topographic pattern overlay. This pattern should remain static to provide a sense of "grounding" as the user scrolls.
- **Zero-Shadow Policy:** No drop shadows are permitted. Use high-contrast color shifts to indicate hover and active states.

## Shapes

The shape language is strictly **Sharp (0px)**. All buttons, cards, input fields, and containers must feature 90-degree corners. This evokes the feeling of industrial machinery, precision-cut steel, and professional equipment. 

Avoid circles where possible; even icons and status indicators should lean toward square or diamond shapes to maintain the rigid, geometric aesthetic.

## Components

- **Buttons:** Primary buttons use a solid Safety Yellow (#FFD700) fill with black text, utilizing all-caps Space Grotesk. Secondary buttons use a Slate Grey outline with no fill.
- **Technical Readouts (Cards):** Containers for data should feature a "header bar" in a slightly lighter grey (#333333) with a label-caps title. Add "corner marks" (small L-shaped accents) to the corners of cards to simulate a viewfinder or scanning tool.
- **Inputs:** Text fields are rectangular boxes with 1px Slate Grey borders. On focus, the border turns Safety Yellow. Place labels above the field in `label-caps` typography.
- **Chips / Status Badges:** Use rectangular badges. "Active" or "Stable" states use the Earthy Brown as a background with Safety Yellow text.
- **Data Grids:** Use 1px borders between all cells. Highlight selected rows with a subtle Earthy Brown tint.
- **Topographic Overlays:** Apply a SVG mask of topographic lines at 5-10% opacity to large background sections or header areas to reinforce the hillside control theme.
- **Crosshairs:** Use subtle "+" or crosshair symbols in the corners of sections to emphasize the "Medical/Technical" precision of the layout.