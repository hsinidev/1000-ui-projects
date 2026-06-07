---
name: Stadium-Lights Design System
colors:
  surface: '#041710'
  surface-dim: '#041710'
  surface-bright: '#293d35'
  surface-container-lowest: '#01110b'
  surface-container-low: '#0b1f18'
  surface-container: '#10231c'
  surface-container-high: '#1a2e26'
  surface-container-highest: '#253931'
  on-surface: '#d1e8dc'
  on-surface-variant: '#c1c8c2'
  inverse-surface: '#d1e8dc'
  inverse-on-surface: '#21342c'
  outline: '#8b938d'
  outline-variant: '#414844'
  surface-tint: '#a5d0b9'
  primary: '#a5d0b9'
  on-primary: '#0e3727'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#3f6653'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#e9c400'
  on-tertiary: '#3a3000'
  tertiary-container: '#c9a900'
  on-tertiary-container: '#4c3e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffe16d'
  tertiary-fixed-dim: '#e9c400'
  on-tertiary-fixed: '#221b00'
  on-tertiary-fixed-variant: '#544600'
  background: '#041710'
  on-background: '#d1e8dc'
  surface-variant: '#253931'
typography:
  display-xl:
    fontFamily: Lexend
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  stat-value:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1'
    letterSpacing: -0.02em
spacing:
  base: 4px
  unit-1: 4px
  unit-2: 8px
  unit-4: 16px
  unit-6: 24px
  unit-8: 32px
  unit-12: 48px
  gutter: 20px
  margin: 24px
---

## Brand & Style

This design system captures the electric intensity of a night match under the floodlights. The brand personality is aggressive, high-performance, and immersive, targeting fans who demand real-time data with the visceral feel of being in the stands. 

The aesthetic style is **High-Contrast / Bold** integrated with **Glassmorphism**. It utilizes deep, dark backgrounds to simulate the pitch at night, contrasted against "light-spill" effects and razor-sharp UI components. The interface should feel fast and reactive, mimicking the split-second nature of professional football. Visual weight is prioritized for live data, using glow effects to draw the eye to changing scores and active game events.

## Colors

The palette is anchored by a deep "Pitch Green" (#1B4332), providing a rich, organic base that mimics a professional turf under night sky conditions. The secondary color is a "Crisp White," reserved for high-readability text and primary icons to ensure maximum contrast against the dark background.

Accents are strictly functional. "Stadium Yellow" (#FFD700) is used for highlights, warnings, and yellow card events, while a vibrant "Card Red" (#D90429) is reserved for critical alerts and red card penalties. The background uses a "Deep Night" neutral (#081C15) to create depth, allowing the green surfaces to appear as if they are illuminated by overhead lights. Subtle radial gradients and glows in Stadium Yellow are used to simulate light spill around active components.

## Typography

This design system utilizes **Lexend** across all levels for its athletic, high-readability, and modern feel. The typographic scale is optimized for "at-a-glance" consumption of live statistics. 

Headlines and display styles use heavy weights (700-800) and tight letter spacing to mimic the look of traditional stadium jerseys and scoreboard displays. For data labels, an uppercase transform with slight tracking is applied to maintain a technical, broadcast-style appearance. Body text remains clean and legible, ensuring that longer descriptions or news feeds do not fatigue the user.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop and a **Fluid Grid** on mobile to ensure the dashboard maintains a structured, "control center" feel. A 12-column system is used with 20px gutters to separate distinct data modules. 

The spacing rhythm is tight (based on a 4px increment), allowing for a high density of information without clutter. Modules should be packed closely together to emphasize the "fast performance" feel, using margins primarily to separate major sections of the pitch view from the statistical sidebars.

## Elevation & Depth

Elevation in this design system is achieved through **Tonal Layering** and **Light spill** rather than traditional soft shadows. 

1.  **Base Layer:** The deepest neutral color, representing the stadium seats and night sky.
2.  **Pitch Layer:** Deep Green surfaces that use subtle top-down linear gradients to simulate floodlight directionality.
3.  **Active Layer:** Cards and containers use semi-transparent dark overlays (Glassmorphism) with high-contrast 1px white borders to appear "lit" from within.
4.  **The Glow:** Active states or live events (like a goal scored) trigger a yellow outer glow (`box-shadow: 0 0 15px rgba(255, 215, 0, 0.4)`), mimicking the intensity of stadium lights focusing on a specific spot on the field.

## Shapes

The shape language is strictly **Sharp (0px)**. All containers, buttons, and input fields must have 0px corner radii. This reinforces the high-performance, technical nature of the dashboard and aligns with the geometric precision of a football pitch's markings. Lines should be thin (1px) but high-contrast, echoing the white chalk lines of the field.

## Components

### Buttons
Primary buttons are solid Crisp White with bold, uppercase black text. Secondary buttons are ghost-style with 1px white borders. All buttons feature a "flash" effect on hover, where a subtle yellow glow emanates from the border.

### Cards & Modules
Modules are the heart of the dashboard. They utilize a dark, semi-transparent background with a 1px border. The header of each card should have a 2px top-border in Pitch Green or Stadium Yellow to denote the category of data.

### Chips & Badges
Chips for player positions or match status (e.g., "LIVE", "FT") are rectangular with no rounding. The "LIVE" badge should utilize a pulsing Stadium Yellow glow to indicate real-time updates.

### Input Fields
Inputs are dark with 1px white borders. On focus, the border transitions to Stadium Yellow with a sharp, 2px outer "beam" effect.

### Match Timeline
A horizontal component representing the 90 minutes. Goals are marked with sharp Yellow diamonds, and cards are represented by solid Red or Yellow rectangles.

### Scoreboard
The primary focal point. It uses the `stat-value` typography. The background should be the darkest neutral to make the white numbers pop, with a faint green radial gradient behind the team names to ground them to the "pitch."