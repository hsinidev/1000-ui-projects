---
name: Industrial Authority
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
  secondary: '#abcdcd'
  on-secondary: '#143535'
  secondary-container: '#2e4e4e'
  on-secondary-container: '#9dbfbe'
  tertiary: '#e7c433'
  on-tertiary: '#3b2f00'
  tertiary-container: '#c9a810'
  on-tertiary-container: '#4c3e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#fedcbe'
  primary-fixed-dim: '#e1c1a4'
  on-primary-fixed: '#291806'
  on-primary-fixed-variant: '#59422c'
  secondary-fixed: '#c6e9e9'
  secondary-fixed-dim: '#abcdcd'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#2c4c4c'
  tertiary-fixed: '#ffe174'
  tertiary-fixed-dim: '#e7c433'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#554500'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
spacing:
  unit: 8px
  gutter: 24px
  margin: 32px
  container-max: 1440px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The design system is built on the principles of structural integrity and field-readiness. It targets civil engineers and project managers who require tools as reliable as the machinery they operate. The aesthetic is defined by **Industrial Brutalism**—a style that prioritizes function over flourish, utilizing heavy borders and raw textures to create an interface that feels constructed rather than merely rendered. 

The emotional response should be one of absolute confidence and permanence. By leveraging tactile metaphors like concrete grain and asphalt grit, this design system bridges the gap between the digital workspace and the physical job site. It is a rugged, authoritative framework designed to withstand high-pressure environments and complex logistical demands.

## Colors

The palette is rooted in the earth and the industrial materials of civil works. The primary **Earthy Brown (#4B3621)** provides a grounded, soil-like foundation, while the **Slate (#2F4F4F)** secondary color represents the reinforced steel and asphalt of modern infrastructure. 

For critical UI interactions and alerts, the system utilizes high-visibility accents: **Safety Yellow (#F4D03F)** for primary actions and warnings, and **Construction Orange (#E67E22)** for secondary emphasis and status changes. The default dark mode uses deep charcoal and near-black tones to reduce eye strain in varying field lighting conditions and to emphasize the "heavy" nature of the architecture.

## Typography

Typography in this design system is selected for maximum legibility and an institutional, authoritative presence. **Newsreader** is utilized for headings; its heavy serif strokes provide the "slab-like" weight required to convey durability. These headings should be set with tight tracking and high weights to mimic traditional blueprint or technical manual headers.

**Public Sans** serves as the primary body face, chosen for its neutral, institutional clarity—ensuring that dense engineering specifications remain readable. For technical data, UI labels, and utility readouts, **Inter** provides a systematic and functional contrast. All utility labels should be treated with uppercase styling and increased letter spacing to evoke the feel of stamped metal plates.

## Layout & Spacing

This design system employs a **Fixed Grid** model to maintain a sense of structural rigidity. A 12-column system is used for desktop layouts with a substantial 24px gutter, ensuring that elements never feel cramped or fragile. 

The spacing rhythm is strictly based on an 8px base unit. Visual groups should be separated by "heavy" margins (32px or greater) to reinforce the idea of distinct modules and components. Components are stacked vertically using "stack" tokens that prioritize generous breathing room for touch targets, accommodating users who may be operating tablets in the field.

## Elevation & Depth

Depth is conveyed through **Bold Borders** and **Tonal Layers** rather than soft shadows. This design system rejects ambient lighting in favor of hard, high-contrast boundaries that mirror the physical edges of construction materials.

1.  **Surfaces:** Use heavy 2px or 3px solid borders in Slate or Safety Yellow to define active areas.
2.  **Stacking:** Higher elevation is achieved by shifting background tones from deep charcoal to the Primary Earthy Brown, creating a "stacked plate" effect.
3.  **Textures:** Background surfaces should incorporate subtle CSS-based noise or SVG patterns representing concrete grain or asphalt texture, increasing in density as the surface moves "closer" to the user.
4.  **Active State:** Elements in focus do not glow; they receive a thick, high-contrast offset border (industrial "hazard" stripes for critical focus).

## Shapes

The shape language of this design system is **Sharp (0)**. There are no rounded corners in the interface. Every button, input field, card, and modal is a perfect rectangle with 90-degree angles, reflecting the precision of engineering and the hard edges of structural steel and concrete blocks. This lack of curvature reinforces the "rugged" brand persona and ensures the UI feels uncompromising and durable.

## Components

### Buttons
Buttons are designed as heavy "utility" blocks. Primary buttons use the Safety Yellow background with black text and a 3px bottom-border to simulate a physical toggle. Secondary buttons use a transparent background with a thick Earthy Brown stroke.

### Status Indicators
Status indicators must be high-contrast and utilize the "Hazard" pattern (diagonal yellow and black stripes) for warnings or critical errors. Active maintenance status should be flagged with the Construction Orange accent.

### Input Fields
Fields are encased in a 2px Slate border. Labels are always positioned outside the field in the "Label-Bold" uppercase style. Focus states use a Safety Yellow "corner bracket" effect rather than a full border change.

### Cards & Modules
Cards utilize a "Concrete" texture background with a subtle inner-stroke of Slate. There is no drop shadow; instead, cards are separated from the background by a 1px solid black "cut line."

### Data Grids
Given the nature of civil engineering, data grids are essential. They should use alternating row colors (Slate and Charcoal) and heavy vertical dividers to maintain the look of a technical ledger.

### Additional Components
- **Progress Gauges:** Heavy, segmented bars (rather than smooth gradients) to track completion.
- **Blueprint Overlays:** Semi-transparent layers for technical drawings using a blueprint-blue tint and white monospaced annotations.