---
name: ABC-Explorer Desktop
colors:
  surface: '#fcf8f9'
  surface-dim: '#dcd9da'
  surface-bright: '#fcf8f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f4'
  surface-container: '#f0edee'
  surface-container-high: '#eae7e8'
  surface-container-highest: '#e5e2e3'
  on-surface: '#1b1b1c'
  on-surface-variant: '#414755'
  inverse-surface: '#303031'
  inverse-on-surface: '#f3f0f1'
  outline: '#717786'
  outline-variant: '#c1c6d7'
  surface-tint: '#005bc1'
  primary: '#0058bc'
  on-primary: '#ffffff'
  primary-container: '#0070eb'
  on-primary-container: '#fefcff'
  inverse-primary: '#adc6ff'
  secondary: '#bc000a'
  on-secondary: '#ffffff'
  secondary-container: '#e2241f'
  on-secondary-container: '#fffbff'
  tertiary: '#745b00'
  on-tertiary: '#ffffff'
  tertiary-container: '#d0a600'
  on-tertiary-container: '#4f3d00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e2ff'
  primary-fixed-dim: '#adc6ff'
  on-primary-fixed: '#001a41'
  on-primary-fixed-variant: '#004493'
  secondary-fixed: '#ffdad5'
  secondary-fixed-dim: '#ffb4aa'
  on-secondary-fixed: '#410001'
  on-secondary-fixed-variant: '#930005'
  tertiary-fixed: '#ffe08b'
  tertiary-fixed-dim: '#f1c100'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#584400'
  background: '#fcf8f9'
  on-background: '#1b1b1c'
  surface-variant: '#e5e2e3'
typography:
  display-lg:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  label-md:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 64px
---

## Brand & Style

This design system is built on a **High-Contrast / Bold** aesthetic that bridges the gap between a playful learning environment for children and a high-utility management tool for adults. The brand personality is energetic, dependable, and highly legible. 

By utilizing thick borders and a vibrant primary palette against expansive white space, the UI achieves a "Neo-Brutalist Lite" feel—retaining the structural integrity of a professional desktop application while remaining approachable. The focus is on clarity and large interactive hit targets to ensure the experience feels tactile and physical even on a digital screen.

## Colors

The color palette uses high-chroma primary colors to denote hierarchy and function.
- **Primary (Blue):** Used for main actions, navigation states, and administrative headers.
- **Secondary (Red):** Used for critical alerts, "stop" actions, and high-energy decorative accents.
- **Tertiary (Yellow):** Used for rewards, progress indicators, and "soft" highlights.
- **Neutral (Carbon):** A near-black (#1A1A1B) is used for all borders and text to maintain extreme contrast and readability.
- **Surface:** The background remains pure White (#FFFFFF) to provide a spacious, clean canvas that prevents the bold colors from feeling overwhelming on large desktop monitors.

## Typography

The design system exclusively utilizes **Lexend**, a typeface specifically designed to improve reading proficiency. 

For the desktop environment, we lean into larger scales to accommodate the increased viewing distance of a monitor. Headlines use tighter tracking and heavier weights to anchor the page. Body text is set with generous line heights to ensure long-form content for parents and admins remains accessible and reduces cognitive load.

## Layout & Spacing

The layout follows a **Fixed Grid** model for centralized content (max-width 1440px) to ensure optimal line lengths for reading. 

- **Grid:** A 12-column system with 24px gutters.
- **Rhythm:** Spacing follows an 8px baseline. Use `lg` (48px) spacing between major sections and `md` (24px) for internal component grouping.
- **Margins:** Desktop views should maintain a minimum of 64px lateral margins to provide "breathing room," reinforcing the kid-friendly, spacious aesthetic.

## Elevation & Depth

This design system rejects traditional soft shadows in favor of **Bold Borders** and **Hard Offsets**. 

- **Flat Depth:** Depth is communicated via a 3px solid black (#1A1A1B) border on all containers.
- **Tactile Offsets:** Active states or "floating" cards use a solid color offset (a 4px - 8px shift) rather than a blur. This creates a "sticker" or "wooden block" feel that is physically intuitive for children while appearing organized and rigid for admins.
- **Layering:** When elements need to stack, use a simple hierarchy of border thickness or contrasting fill colors rather than gradients or blurs.

## Shapes

The shape language is defined by **Rounded** geometry. This softens the high-contrast "brutalist" borders, ensuring the UI feels safe and friendly.

- **Components:** Standard buttons and input fields use a 0.5rem (8px) radius.
- **Containers:** Large cards and modals use the `rounded-xl` (1.5rem / 24px) setting to create a friendly, "cushioned" look for the main content areas.
- **Interactive Elements:** Checkboxes and small icons maintain a consistent 8px radius to ensure a cohesive visual vocabulary.

## Components

### Buttons
Primary buttons are styled with a 3px black border, a Primary Blue fill, and White Lexend text (Bold). On hover, they shift 4px down and right with a solid shadow appearing behind them.

### Cards
Cards use a White background with a 3px black border. Headers within cards should have a solid Primary Yellow or Blue background to clearly separate the title from the body content.

### Inputs & Forms
Input fields must have a minimum height of 56px for desktop comfort. They feature a 2px black border that thickens to 4px on focus. Labels are always persistent and set in `label-bold`.

### Progress Bars & Chips
Chips use highly saturated fills (Red, Blue, or Yellow) with black text. Progress bars are chunky (16px height) with a secondary color fill against a light grey track, always encased in a black border.

### Administrative Tables
Tables should avoid thin grey lines. Instead, use alternating row stripes in very pale tints of the primary colors and thick 3px borders for the outer container. Headers are always bold and capitalized.