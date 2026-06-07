---
name: Stealth Operations
colors:
  surface: '#1b110a'
  surface-dim: '#1b110a'
  surface-bright: '#43372e'
  surface-container-lowest: '#150c06'
  surface-container-low: '#241912'
  surface-container: '#281d15'
  surface-container-high: '#33281f'
  surface-container-highest: '#3f3229'
  on-surface: '#f3dfd1'
  on-surface-variant: '#ddc1ae'
  inverse-surface: '#f3dfd1'
  inverse-on-surface: '#3a2e25'
  outline: '#a48c7a'
  outline-variant: '#564334'
  surface-tint: '#ffb77d'
  primary: '#ffb77d'
  on-primary: '#4d2600'
  primary-container: '#ff8c00'
  on-primary-container: '#623200'
  inverse-primary: '#904d00'
  secondary: '#c1c8ca'
  on-secondary: '#2b3234'
  secondary-container: '#434a4c'
  on-secondary-container: '#b2babc'
  tertiary: '#85cfff'
  on-tertiary: '#00344c'
  tertiary-container: '#00b5fc'
  on-tertiary-container: '#004360'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcc3'
  primary-fixed-dim: '#ffb77d'
  on-primary-fixed: '#2f1500'
  on-primary-fixed-variant: '#6e3900'
  secondary-fixed: '#dde4e6'
  secondary-fixed-dim: '#c1c8ca'
  on-secondary-fixed: '#161d1f'
  on-secondary-fixed-variant: '#41484a'
  tertiary-fixed: '#c7e7ff'
  tertiary-fixed-dim: '#85cfff'
  on-tertiary-fixed: '#001e2e'
  on-tertiary-fixed-variant: '#004c6c'
  background: '#1b110a'
  on-background: '#f3dfd1'
  surface-variant: '#3f3229'
typography:
  display-data:
    fontFamily: JetBrains Mono
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 12px
  margin: 16px
---

## Brand & Style

This design system is engineered for precision, reliability, and technical authority. It adopts a **Stealth-Industrial** aesthetic, prioritizing data density and immediate situational awareness. The visual language is inspired by professional monitoring equipment and mission-critical cockpits, utilizing a "Dark Mode First" philosophy to reduce eye strain in low-light cellar environments.

The emotional response should be one of absolute control and accuracy. By blending elements of **Brutalism** (heavy borders, monospaced data) with **High-Contrast Modernism**, the interface feels like a high-performance tool rather than a consumer application. Key visual signatures include hairline borders, technical "glow" states for active hardware, and rhythmic alert animations.

## Colors

The palette is anchored by **Deep Midnight Blue**, providing a void-like background that allows technical data to recede or pop based on priority. **Graphite** serves as the structural layer, used for containers and recessed surfaces to create a sense of physical machinery.

**Safety Orange** is reserved strictly for primary actions, critical interactive points, and active sensor states, ensuring high glanceability. **Critical Red** is used exclusively for "Threshold Breach" events, often accompanied by a luminance-based pulse. All secondary information is rendered in muted slate tones to maintain a clear visual hierarchy where the most important data (temperature, humidity, pressure) remains the brightest element on the screen.

## Typography

This design system utilizes a dual-font strategy to balance legibility with technical character. 

1.  **Inter (Sans-Serif):** Used for all UI labels, navigation, and instructional text. It provides a clean, neutral foundation that ensures the interface remains professional and readable at small scales.
2.  **JetBrains Mono (Monospace):** Used for all numerical values, sensor IDs, and timestamps. The fixed-width nature of the font prevents "layout jump" when data updates in real-time and emphasizes the technical, programmatic nature of sensor management.

Headlines should be kept concise. Use uppercase labels for metadata to reinforce the industrial, "stamped" aesthetic.

## Layout & Spacing

The layout philosophy follows a **High-Density Fluid Grid**. Efficiency is prioritized over whitespace; information is packed tightly to allow professionals to monitor dozens of sensors on a single screen without scrolling.

A 12-column grid is used for desktop views, shifting to a single-column stack for mobile sensor alerts. Gutters are intentionally narrow (12px) to maximize the "data-per-pixel" ratio. Components should align to a strict 4px baseline grid to maintain the architectural rigors of the stealth aesthetic. Margins are kept consistent at 16px to ensure content doesn't bleed into the physical edges of the device display.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Stacking** and **Luminance**, rather than traditional drop shadows.

*   **Level 0 (Background):** Deep Midnight Blue.
*   **Level 1 (Containers):** Graphite surfaces with 1px solid borders (#3E4648).
*   **Level 2 (Active/Hover):** Surfaces that gain a subtle inner glow or a brighter border weight.

Interactive elements do not "float"; they appear as integrated panels within a hardware rack. To indicate a critical state, components utilize an outer glow (Safety Orange or Critical Red) with a 10-20px blur and low opacity (20%) to simulate the light emission of an LED indicator.

## Shapes

The shape language is **Rigid and Industrial**. To maintain the stealth-inspired look, avoid overly rounded or "bubbly" elements. A universal radius of 4px (Soft) is applied to containers and buttons to prevent the interface from feeling sharp/hostile while maintaining a disciplined, geometric structure.

Buttons and status indicators should feel like physical toggles. Progress bars and sensor graphs should use square caps and sharp corners to emphasize mathematical precision.

## Components

### Primary Buttons
High-contrast Safety Orange (#FF8C00) backgrounds with black text. On hover, the button should gain a 4px outer glow of the same color. For "destructive" or "stop" actions, use Critical Red.

### Data Cards
Graphite backgrounds with a top-aligned 2px accent bar indicating status (Orange = Active, Red = Alert, Grey = Standby). All numerical data inside the card must use JetBrains Mono.

### Status Indicators (LEDs)
Small circular elements (8px) that use a "Glow" effect. 
- **Active:** Safety Orange with a pulse animation.
- **Critical:** Red-pulse animation (0.5s fade-in/out).
- **Offline:** Dark Graphite with no glow.

### Input Fields
Darker than the container background, using a 1px border. Focus state changes the border to Safety Orange and adds a subtle inner glow.

### Sensor Charts
Line charts should use thin 1.5px strokes. Fill the area beneath the line with a very low opacity gradient of the line's color to provide volume without cluttering the high-density layout.

### Threshold Alerts
Alerts appear as full-width "Banners" at the top of the viewport or specific containers, utilizing a Critical Red background with high-contrast white monospaced text for the error code.