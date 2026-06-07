---
name: Emergency Design System
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
  on-surface-variant: '#d0c6ab'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#999077'
  outline-variant: '#4d4732'
  surface-tint: '#e9c400'
  primary: '#fff6df'
  on-primary: '#3a3000'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#705d00'
  secondary: '#ffb4a8'
  on-secondary: '#690001'
  secondary-container: '#ae0203'
  on-secondary-container: '#ffb8ae'
  tertiary: '#f6f6f6'
  on-tertiary: '#2f3131'
  tertiary-container: '#d9dada'
  on-tertiary-container: '#5e5f60'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#ffdad5'
  secondary-fixed-dim: '#ffb4a8'
  on-secondary-fixed: '#410000'
  on-secondary-fixed-variant: '#930002'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: '0'
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-md:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-bold:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  button-text:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.02em
spacing:
  base: 8px
  touch-target-min: 56px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system is engineered for high-stakes environments where cognitive load must be minimized and speed of comprehension is paramount. The brand personality is authoritative, urgent, and unflinching. It prioritizes utility over aesthetics, evoking the functional reliability of physical hazard signage and emergency services equipment.

The visual style utilizes a mix of **Brutalism** and **High-Contrast Bold**. By employing heavy strokes, saturated signal colors, and a complete absence of decorative elements, the design system ensures that critical information is never obscured. It is designed to be legible in extreme conditions, including low-light environments, high-glare outdoor settings, and for users experiencing high stress or visual impairment.

## Colors
The palette is restricted to high-visibility "signal" colors to ensure maximum contrast and clear information hierarchy. This design system defaults to a **Dark Mode** to reduce eye strain in nighttime operations and to allow vibrant alerts to pop with maximum intensity.

- **Primary (#FFD700):** A high-visibility "Safety Yellow" used for primary actions and cautionary information. It provides the highest contrast against the black background.
- **Secondary (#D92D20):** A deep "Emergency Red" reserved strictly for critical alerts, stop commands, and immediate hazards.
- **Neutral/Background (#000000):** Pure black to provide infinite contrast for text and to preserve battery life on OLED mobile devices during field operations.
- **Surface (#1A1A1A):** A slight grey used for container separation while maintaining high-contrast ratios.

All color combinations are strictly audited to meet **WCAG AAA** standards, ensuring a minimum contrast ratio of 7:1 for all functional text and 4.5:1 for large graphical elements.

## Typography
The design system utilizes **Public Sans**, a typeface designed for government and institutional use. It was selected for its exceptional legibility, neutral tone, and robust character definition, which prevents "letter crowding" in high-stress reading scenarios.

Typography is scaled larger than standard consumer applications to account for shaky hands or moving vehicles. We avoid thin weights entirely. Bold and Extra Bold weights are used for headlines to create a clear visual anchor, while regular weights are used for body text to ensure maximum readability against dark backgrounds. All labels use increased letter-spacing to enhance character recognition at a distance.

## Layout & Spacing
The layout follows a **Fluid Grid** model with an emphasis on vertical stacking to facilitate easy one-handed scrolling on mobile devices. 

A strict 8px spacing rhythm is applied across the system. To ensure accessibility for users in protective gear (like gloves) or those with motor impairments, the minimum touch target for any interactive element is set to **56px**, exceeding standard guidelines. Margins are generous to prevent accidental triggers at the edge of the screen, and gutters are wide to maintain clear separation between distinct data points or action groups.

## Elevation & Depth
In this design system, depth is communicated through **Bold Borders** and **Tonal Layers** rather than shadows. Shadows are avoided as they can appear muddy on high-brightness screens or in high-contrast modes.

- **Level 0 (Base):** Pure black (#000000).
- **Level 1 (Card/Container):** Dark Grey (#1A1A1A) with a 2px solid border in White or Primary Yellow.
- **Level 2 (Interactive/Focus):** Elements are "lifted" using a thicker 4px border or a solid color fill. 

Structural hierarchy is achieved by "stacking" containers. When an element is active or requires immediate attention, it utilizes a high-visibility stroke or a full-color flood (e.g., a Red alert box) to dominate the visual field.

## Shapes
The design system employs **Sharp (0px)** corners for all UI elements. This geometric rigidity reinforces the professional, serious, and industrial nature of crisis response. Sharp corners allow for more efficient use of screen real estate and create a clear, unmistakable boundary for touch targets. The absence of curves ensures that every pixel is utilized for information or clear delineation, echoing the aesthetic of technical blueprints and tactical displays.

## Components
Consistent component behavior is critical for reducing "time-to-action" during emergencies.

- **Buttons:** Large, full-width blocks with a 56px minimum height. Primary buttons use a solid Yellow fill with Black text. Danger buttons use a solid Red fill with White text. Outlined buttons use a 2px stroke.
- **Input Fields:** Heavy 2px white borders with high-contrast cursor indicators. Labels are always visible above the field; placeholder text is avoided to prevent confusion.
- **Status Chips:** Rectangular tags with high-contrast backgrounds. They use uppercase text to denote urgency (e.g., "ACTIVE," "RESOLVED," "CRITICAL").
- **Alert Cards:** Large, full-width containers with a thick left-accent border (8px) in the alert's semantic color. 
- **Checkboxes & Radios:** Oversized targets (32px icons) with heavy strokes to ensure the state is visible even at a glance or with low visual acuity.
- **Crisis Banner:** A persistent, high-contrast bar at the top of the UI for broadcasting the most critical system-wide information, utilizing a pulsing "Signal Red" or "Safety Yellow" background.