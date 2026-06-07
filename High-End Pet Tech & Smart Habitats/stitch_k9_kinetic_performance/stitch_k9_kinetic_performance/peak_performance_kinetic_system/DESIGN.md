---
name: Peak-Performance Kinetic System
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
  on-surface-variant: '#ebbbb4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#b18780'
  outline-variant: '#603e39'
  surface-tint: '#ffb4a8'
  primary: '#ffb4a8'
  on-primary: '#690100'
  primary-container: '#ff5540'
  on-primary-container: '#5c0000'
  inverse-primary: '#c00100'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#929090'
  on-tertiary-container: '#2a2a2a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930100'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Anybody
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Anybody
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1280px
---

## Brand & Style

The design system is engineered for a high-intensity, professional K9 training environment. It targets elite trainers and working dog enthusiasts who value precision, physical excellence, and raw energy. The aesthetic is **Kinetic & Bold**, drawing heavy inspiration from automotive racing and high-performance engineering.

The UI must evoke a sense of forward momentum. This is achieved through a high-contrast, dark-mode-first approach that utilizes sharp geometry and metallic finishes. The visual narrative shifts away from "friendly" pet care toward "mechanical" performance and tactical discipline. Key stylistic pillars include:
- **High-Contrast Impact:** Deep blacks against vibrant reds to demand immediate attention.
- **Structural Integrity:** Use of subtle carbon fiber patterns in backgrounds to suggest strength and lightweight durability.
- **Machined Precision:** Elements should look "manufactured" rather than "drawn," utilizing micro-gradients to simulate brushed metal or anodized surfaces.

## Colors

This design system utilizes a restricted, high-impact palette designed for maximum legibility in high-activity environments.

- **Racing Red (#FF0000):** Used exclusively for primary actions, critical performance metrics, and highlighting "active" states. It represents the "redline" of performance.
- **Carbon Fiber Grey/Black (#1A1A1A):** The foundation of the UI. It provides a non-distracting, premium backdrop that allows the content to pop.
- **Pure White (#FFFFFF):** Used for primary typography and high-priority icons to ensure maximum contrast against the dark background.
- **Metallic Slate (#333333):** A secondary neutral used for borders, inactive states, and subtle textural depth to mimic machined steel.

## Typography

Typography in this design system is aggressive and functional. 

**Headlines** utilize **Anybody**, specifically set in bold italics to create a visual "lean" that suggests speed and acceleration. These should be tightly tracked to feel dense and powerful.

**Body Text** uses **Inter** for its clinical clarity. While headlines are italicized, body text remains upright to ensure maximum readability during intense training sessions.

**Technical Data** and labels utilize **JetBrains Mono**. This monospaced choice reinforces the "precision" aspect of the brand, suggesting data-driven results and mechanical accuracy.

## Layout & Spacing

This design system employs a **Fixed Grid** model with a rigid 4px baseline. The layout should feel structural and organized, like a technical schematic.

- **Grid:** A 12-column system with 16px gutters. 
- **Rhythm:** Use increments of 8px for vertical spacing between sections (32px, 64px, 128px) to maintain a disciplined, rhythmic flow.
- **Negative Space:** While bold, the layout should not be cluttered. High-performance design requires "breathable" areas to focus the user on critical data points.

## Elevation & Depth

Depth is conveyed through **Tonal Layering** and **Material Simulation** rather than traditional soft shadows.

- **Z-Axis Hierarchy:** Higher elevation elements are indicated by lighter shades of grey (#333333) or subtle "inner glows" that mimic the edge of a metallic plate.
- **Accents:** Use 1px solid borders in Racing Red or Metallic Slate to define container edges. 
- **Textures:** Subtle carbon fiber patterns (low-opacity CSS patterns) should be applied to the base background layer (#1A1A1A) to add tactile quality without distracting from the content. 
- **Gloss:** Occasional high-shine gradients (White at 10% opacity to Transparent) can be used on buttons to simulate a glass or polished metal finish.

## Shapes

The shape language of this design system is **Sharp and Aggressive**. 

Rounding is strictly avoided (0px radius) to maintain a "tactical" and "industrial" feel. Every container, button, and input field should have crisp, 90-degree angles. To add dynamic energy, utilize **diagonal shearing** (e.g., 5-10 degree clips on the corners of buttons or cards) to reinforce the kinetic theme.

## Components

### Buttons
- **Primary:** Solid Racing Red, black text (Bold Italic), sharp edges. Include a subtle 45-degree "cut" on the top-right corner.
- **Secondary:** Transparent background, 2px Racing Red border, red text.
- **Interaction:** On hover, primary buttons shift to a metallic gradient; secondary buttons fill with red.

### Input Fields
- **Style:** Dark backgrounds (#0D0D0D) with 1px Metallic Slate bottom borders only.
- **Focus:** The bottom border transforms into Racing Red with a slight outer glow.

### Cards
- **Style:** Carbon fiber textured backgrounds with 1px solid slate borders.
- **Header:** Use the monospaced label font for card titles to suggest "Component Specs."

### Data Visualization
- **Line Charts:** High-contrast red lines on dark grids. 
- **Gauges:** Circular indicators should look like automotive tachometers, with the "redline" area representing peak performance zones.

### Chips & Status Indicators
- **Form:** Rectangular with no rounding. 
- **Logic:** Use Racing Red for "High Energy/Action," White for "Neutral/State," and Slate for "Standby."

### Additional Components
- **Performance HUD:** A floating overlay for real-time training stats, using semi-transparent black backgrounds and monospaced white text.