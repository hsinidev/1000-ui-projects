---
name: Command Center Logistics
colors:
  surface: '#101415'
  surface-dim: '#101415'
  surface-bright: '#363a3b'
  surface-container-lowest: '#0b0f10'
  surface-container-low: '#191c1e'
  surface-container: '#1d2022'
  surface-container-high: '#272a2c'
  surface-container-highest: '#323537'
  on-surface: '#e0e3e5'
  on-surface-variant: '#bac9cc'
  inverse-surface: '#e0e3e5'
  inverse-on-surface: '#2d3133'
  outline: '#849396'
  outline-variant: '#3b494c'
  surface-tint: '#00daf3'
  primary: '#c3f5ff'
  on-primary: '#00363d'
  primary-container: '#00e5ff'
  on-primary-container: '#00626e'
  inverse-primary: '#006875'
  secondary: '#b9c7e4'
  on-secondary: '#233148'
  secondary-container: '#3c4962'
  on-secondary-container: '#abb9d6'
  tertiary: '#e6ecff'
  on-tertiary: '#20304f'
  tertiary-container: '#c0d0f7'
  on-tertiary-container: '#49597a'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#9cf0ff'
  primary-fixed-dim: '#00daf3'
  on-primary-fixed: '#001f24'
  on-primary-fixed-variant: '#004f58'
  secondary-fixed: '#d6e3ff'
  secondary-fixed-dim: '#b9c7e4'
  on-secondary-fixed: '#0d1c32'
  on-secondary-fixed-variant: '#39475f'
  tertiary-fixed: '#d8e2ff'
  tertiary-fixed-dim: '#b6c6ed'
  on-tertiary-fixed: '#091b39'
  on-tertiary-fixed-variant: '#374767'
  background: '#101415'
  on-background: '#e0e3e5'
  surface-variant: '#323537'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: 0em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.02em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 8px
  sm: 16px
  md: 24px
  lg: 32px
  xl: 48px
  gutter: 16px
  margin: 24px
---

## Brand & Style

This design system is engineered for the high-stakes environment of global logistics, where clarity and real-time data density are paramount. The brand personality is authoritative, precise, and technologically advanced. It evokes the feeling of a mission-control room—calm under pressure but intensely focused.

The design style combines **Minimalism** with subtle **Glassmorphism**. By using a dark-themed "Command Center" aesthetic, the system reduces eye strain for operators monitoring global shifts 24/7. Visual interest is driven by functional data visualization rather than decorative elements, ensuring that every pixel serves a logistical purpose. The UI is professional and reliable, utilizing thin lines and luminous accents to guide the user's attention through complex information hierarchies.

## Colors

The palette is anchored in a hierarchy of deep navies to provide a structured, receding background that allows critical data to "pop."

- **Primary (Neon Blue):** Reserved for active states, primary actions, and critical data highlights. It mimics the glow of a high-tech console.
- **Secondary (Deep Navy):** The foundational canvas. It provides a rich, dark environment that enhances contrast for light text.
- **Tertiary (Midnight Blue):** Used for structural layering, such as sidebars, headers, and card containers.
- **Neutral (Arctic White):** Used primarily for high-readability typography and icons.

Secondary accents should include functional colors: Emerald Green for "On Time/In Transit," Amber for "Delayed," and Crimson for "Critical Alert." All accent colors must maintain high luminosity against the dark background.

## Typography

This design system utilizes a dual-font strategy to balance technical character with institutional legibility.

- **Space Grotesk** is used for headlines, labels, and data points. Its geometric, technical construction reinforces the high-tech connectivity theme. Use the "Uppercase" variant for labels to create a professional, "classified" look.
- **Inter** is used for all body copy and long-form descriptions. Its neutral, systematic design ensures that even in data-heavy tables, the text remains highly readable and functional.

Weight is used strategically: heavier weights for navigation and critical headers, while lighter weights are reserved for secondary metadata to manage information density.

## Layout & Spacing

The system employs a **Fluid Grid** model with a high-density 12-column structure. Given the "Command Center" requirement, the layout should maximize horizontal real estate, utilizing a dashboard-style configuration where panels can be expanded or collapsed.

The spacing rhythm is based on a 4px baseline, allowing for the tight tolerances required in data-rich environments. For logistics tracking and monitoring, use "Compact" spacing (8px-16px) to keep related information clusters together. Use larger "Section" spacing (32px-48px) to separate distinct functional areas like the global map from the shipment inventory list.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Low-Contrast Outlines**. In a dark UI, traditional shadows are less effective; instead, depth is communicated by shifting the background color.

- **Level 0 (Floor):** The base background (Deep Navy).
- **Level 1 (Panels):** Midnight Blue surfaces with a 1px border in a slightly lighter navy hex to define edges.
- **Level 2 (Popovers/Modals):** Lighter navy surfaces featuring a subtle backdrop blur (Glassmorphism) to maintain the sense of the "Command Center" beneath the overlay.

Interactive elements should use a "Primary Glow"—a very soft, low-opacity Neon Blue outer shadow—to indicate focus or "Live" status.

## Shapes

The shape language is "Soft" (0.25rem), providing a professional and modern look that is more approachable than sharp corners but more serious than fully rounded ones.

- **Standard Elements:** Buttons, input fields, and tags use a 4px radius.
- **Structural Containers:** Larger cards and dashboard panels use a 8px (rounded-lg) radius to create a distinct framing effect.
- **Status Indicators:** Small circular pips are used for "Live" connectivity status, contrasting with the rectangular nature of the rest of the UI.

## Components

- **Buttons:** Primary buttons feature a solid Neon Blue fill with dark text. Secondary buttons use a ghost style with a Neon Blue border and 10% opacity blue fill.
- **Input Fields:** Dark backgrounds with a 1px border. On focus, the border glows Neon Blue with a subtle outer shadow.
- **Data Cards:** Essential for logistics. They should feature a "Header" with Space Grotesk labels and a "Value" section using high-contrast white text.
- **Status Chips:** Small, pill-shaped indicators with high-saturation backgrounds (Green, Amber, Red) but low-opacity fills to keep the "dark" aesthetic consistent.
- **Data Tables:** High-density, borderless between columns, with 1px horizontal dividers. Use "Zebra Striping" with a very subtle tonal shift for readability.
- **Global Map:** A custom vector map using Deep Navy for landmasses and Neon Blue for "Live" shipping lanes and connectivity nodes.
- **Connectivity Badges:** A specific component for this design system that shows real-time "Uptime" or "Sync Status" using a pulse animation in the Primary color.