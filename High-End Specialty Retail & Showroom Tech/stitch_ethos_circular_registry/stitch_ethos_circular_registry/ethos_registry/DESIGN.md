---
name: Ethos-Registry
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#434843'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#8c4f10'
  on-secondary: '#ffffff'
  secondary-container: '#fdad67'
  on-secondary-container: '#763f00'
  tertiary: '#171815'
  on-tertiary: '#ffffff'
  tertiary-container: '#2b2c29'
  on-tertiary-container: '#94938f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#ffb77b'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6d3a00'
  tertiary-fixed: '#e4e2dd'
  tertiary-fixed-dim: '#c8c6c2'
  on-tertiary-fixed: '#1b1c19'
  on-tertiary-fixed-variant: '#474744'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-md-mobile:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  title-sm:
    fontFamily: Playfair Display
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.4'
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
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
---

## Brand & Style

This design system embodies **Sustainable-Modern Luxury**. It targets a discerning audience that values environmental stewardship as much as premium quality. The brand personality is rooted in "Conscious Elegance"—a blend of organic heritage and modern precision.

The visual style is **Tactile Minimalism**. It moves away from the sterile "tech" aesthetic, favoring the warmth of physical materials. By combining generous whitespace with paper-like textures and metallic accents, the UI evokes the feeling of a high-end, bespoke stationary set. Every interaction should feel intentional, calm, and trustworthy, reinforcing a commitment to longevity over trends.

## Colors

The palette is inspired by a deep coniferous forest meeting refined craftsmanship. 

- **Deep Forest Green (#1B3022):** Used for primary actions, high-level navigation, and grounding elements. It provides the "eco-conscious" anchor.
- **Metallic Copper (#B87333):** Used sparingly as an accent for thin borders, icons, and subtle highlights. It signifies "modern luxury."
- **Soft Off-White (#F9F7F2):** The primary background color. Unlike pure white, this shade suggests natural, unbleached paper and reduces eye strain.
- **Neutral (#4A4A4A):** A soft charcoal used for body text to ensure high contrast against the off-white background without the harshness of pure black.

## Typography

The typographic hierarchy relies on the contrast between the evocative **Playfair Display** and the functional **Inter**.

- **Headlines:** Set in Playfair Display. Use high-contrast weights for displays and medium weights for sub-headers. Headlines should have tighter letter spacing to maintain a "printed" look.
- **Body Text:** Set in Inter with increased line height (1.6) and generous paragraph spacing to ensure maximum readability, especially on mobile devices.
- **Labels:** Use Inter in uppercase with tracking (letter spacing) for small metadata, buttons, and navigation items to evoke a modern, architectural feel.

## Layout & Spacing

This design system utilizes a **Fixed Grid** for desktop and a **Fluid Content Model** for mobile. 

- **Desktop:** A 12-column grid with a 1200px max-width. Margins are intentionally wide (64px+) to create a gallery-like focus on content.
- **Mobile:** A 4-column fluid grid. To maintain the "luxury" feel, vertical padding is increased between sections (minimum 48px) to prevent the UI from feeling cluttered.
- **Rhythm:** An 8px linear scale governs all spacing. Components should prioritize "negative space" as a functional element of the design.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Tactile Textures** rather than heavy shadows.

1.  **The Base:** The Soft Off-White background (#F9F7F2) should feature a subtle grain or "paper" noise overlay (2-3% opacity).
2.  **The Cards:** Elevated elements use a slightly brighter white or the same base color but are defined by **Thin Copper Borders (1px)**.
3.  **Shadows:** When used, shadows must be extremely diffused and "long." Use a soft Forest Green tint in the shadow hex (e.g., #1B3022 at 5% opacity) to create a more natural, ambient occlusion effect.

## Shapes

To maintain a sophisticated and architectural aesthetic, the design system utilizes **Sharp (0px)** corners for almost all structural elements.

Square edges reflect the precision of luxury branding and the clean lines of modern sustainable architecture. Use sharp corners for cards, buttons, and input fields. Circular shapes are reserved exclusively for avatars or specific status indicators to provide a singular point of organic contrast.

## Components

- **Buttons:**
    - **Primary:** Solid Forest Green (#1B3022) with White text. Sharp corners. High-contrast for mobile accessibility.
    - **Secondary:** Transparent background with a 1px Copper (#B87333) border and Copper text.
- **Cards:** Use "Minimalist Card" patterns—no heavy drop shadows. Definition is achieved via the 1px Copper border and the subtle paper texture.
- **Input Fields:** Bottom-border only (Copper, 1px) to mimic a high-end ledger or registry book. Labels should be small-caps Inter above the line.
- **Chips/Tags:** Forest Green outlines with light Forest Green tinted backgrounds.
- **Registry Specifics:**
    - **Progress Bars:** Thin, Copper-filled tracks for "gifted" items.
    - **Eco-Badges:** Small, minimalist Forest Green leaf icons or "Sustainable" labels in small-caps Inter.
- **Icons:** Use thin-stroke (1px or 1.5px) icons in Forest Green or Copper. Avoid filled icons to keep the interface light and "airy."