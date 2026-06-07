---
name: Heritage-Stable
colors:
  surface: '#f9f9f7'
  surface-dim: '#dadad8'
  surface-bright: '#f9f9f7'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f2'
  surface-container: '#eeeeec'
  surface-container-high: '#e8e8e6'
  surface-container-highest: '#e2e3e1'
  on-surface: '#1a1c1b'
  on-surface-variant: '#4f453f'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f1ef'
  outline: '#81756e'
  outline-variant: '#d2c4bc'
  surface-tint: '#705a4c'
  primary: '#26170c'
  on-primary: '#ffffff'
  primary-container: '#3d2b1f'
  on-primary-container: '#ac9181'
  inverse-primary: '#dec1af'
  secondary: '#526168'
  on-secondary: '#ffffff'
  secondary-container: '#d2e2eb'
  on-secondary-container: '#56656d'
  tertiary: '#271701'
  on-tertiary: '#ffffff'
  tertiary-container: '#3f2b10'
  on-tertiary-container: '#af926e'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#fbddca'
  primary-fixed-dim: '#dec1af'
  on-primary-fixed: '#28180d'
  on-primary-fixed-variant: '#574335'
  secondary-fixed: '#d5e5ee'
  secondary-fixed-dim: '#b9c9d2'
  on-secondary-fixed: '#0f1d24'
  on-secondary-fixed-variant: '#3a4950'
  tertiary-fixed: '#ffddb6'
  tertiary-fixed-dim: '#e2c19b'
  on-tertiary-fixed: '#291801'
  on-tertiary-fixed-variant: '#594325'
  background: '#f9f9f7'
  on-background: '#1a1c1b'
  surface-variant: '#e2e3e1'
typography:
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Noto Serif
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Metropolis
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Metropolis
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-edge: 40px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The brand identity centers on the intersection of equestrian tradition and cutting-edge infrastructure technology. It evokes the feeling of a high-end architectural firm managing a legacy estate. The target audience includes estate managers, professional trainers, and luxury property owners who value reliability, precision, and aesthetic harmony.

The design style is **Corporate Modern with a Minimalist focus**, utilizing structural alignment and premium materiality. It avoids decorative clutter in favor of "architectural" space, where the hierarchy is defined by sharp lines, generous margins, and full-bleed photography of stables and arenas. The mood is intentionally grounded—feeling as solid as the timber and stone of the structures it manages—while providing the invisible, high-tech layer of smart sensors and automated climate controls.

## Colors

The palette is derived from natural, premium materials: dark walnut, weathered slate, and limestone.

- **Primary (Deep Earthy Brown):** Used for structural elements, navigation headers, and primary typography. It provides the "grounded" weight of the app.
- **Secondary (Slate Grey):** Used for technical data, secondary icons, and infrastructure-related UI components.
- **Tertiary (Warm Ochre/Tan):** An accent color used sparingly for active states, high-value status indicators, or "call-to-action" highlights that need to feel organic yet noticeable.
- **Neutral (Crisp White & Bone):** Backgrounds are primarily a very slightly off-white (#F9F9F7) to reduce screen glare and feel more like high-quality stationery than a digital screen.
- **Status Colors:** Use desaturated greens for "Stable" and muted ambers for "Maintenance Required" to maintain the professional, architectural tone.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage and technology. 

- **Headlines:** Use **Noto Serif**. This font provides the "literary" and "architectural" feel. Use it for estate names, section headers, and major titles. 
- **Interface & Data:** Use **Metropolis**. Its geometric precision reflects modern infrastructure. It is used for all controls, body text, and navigation items.
- **Technical Data:** For sensor readings, coordinates, and timestamps, use **Geist** (mono) at small sizes to emphasize the "high-tech" management aspect.
- **Styling:** Use uppercase with increased letter spacing for `label-caps` to categorize data sections, echoing architectural blueprints.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** approach for desktop and tablet to maintain an editorial, "folio" feel. 

- **Grid:** A 12-column grid with generous 24px gutters. 
- **Margins:** Large 40px external margins are used to frame the content, preventing the UI from feeling cramped.
- **Imagery:** Use full-bleed landscape imagery at the top of main dashboard views. Content cards should overlap these images slightly (40-80px) to create a sense of physical layering.
- **Rhythm:** Vertical spacing is intentionally "airy" to allow the user to focus on critical data without visual noise.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layering** and **Subtle Ambient Shadows** rather than aggressive elevation.

- **The Base:** The primary surface is Bone (#F9F9F7).
- **Cards:** Secondary surfaces are Crisp White (#FFFFFF) with a thin 1px border in a very light Slate (#E0E3E5).
- **Shadows:** Use extremely soft, large-radius shadows (Blur: 30px, Opacity: 4%, Color: Primary Brown) to give cards a slight "lift" without looking like standard software.
- **Depth:** Use background blurs (15px) only on top-level navigation overlays to maintain focus on the architectural imagery behind them.

## Shapes

The shape language is "Soft-Sharp." While we avoid aggressive rounding to maintain a professional and structural feel, we use a 0.25rem (4px) radius to prevent the UI from feeling hostile or overly technical.

- **Small Elements (Inputs, Buttons):** 4px corner radius.
- **Large Elements (Cards, Imagery):** 8px corner radius.
- **Visual Dividers:** 1px solid lines in Slate Grey at 20% opacity are used to separate logical sections, mimicking drafting lines.

## Components

- **Buttons:** Primary buttons use the Primary Brown background with White text, square-ish with a 4px radius. Secondary buttons use a Slate Grey ghost style (border only).
- **Input Fields:** Bottom-border only or very light grey fills with sharp corners. Labels sit above the field in `label-caps` typography.
- **Status Chips:** Small, rectangular chips with desaturated background tints and dark text. Used for "Occupied," "Ventilation On," or "Secure."
- **Data Cards:** Cards should have a "Metric > Label" hierarchy. Use the Serif font for the numerical value to give it a premium, bespoke look.
- **Inventory Lists:** High-contrast lists with thin dividers and large hit areas. Use high-quality icons with a thin (1.5pt) stroke weight.
- **Infrastructure Maps:** Custom-styled interactive floorplans using slate and cream tones, avoiding standard map colors to maintain the brand's aesthetic.