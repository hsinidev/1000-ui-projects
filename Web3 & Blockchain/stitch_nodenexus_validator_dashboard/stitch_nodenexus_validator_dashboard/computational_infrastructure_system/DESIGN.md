---
name: Computational Infrastructure System
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#383939'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#292a2a'
  surface-container-highest: '#343535'
  on-surface: '#e3e2e2'
  on-surface-variant: '#c7c6cc'
  inverse-surface: '#e3e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#919096'
  outline-variant: '#46464b'
  surface-tint: '#c5c5d2'
  primary: '#c5c5d2'
  on-primary: '#2e303a'
  primary-container: '#0f111a'
  on-primary-container: '#7b7c88'
  inverse-primary: '#5c5e69'
  secondary: '#ecffe3'
  on-secondary: '#003907'
  secondary-container: '#13ff43'
  on-secondary-container: '#007117'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#111111'
  on-tertiary-container: '#7e7c7c'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e1ef'
  primary-fixed-dim: '#c5c5d2'
  on-primary-fixed: '#191b24'
  on-primary-fixed-variant: '#454651'
  secondary-fixed: '#72ff70'
  secondary-fixed-dim: '#00e639'
  on-secondary-fixed: '#002203'
  on-secondary-fixed-variant: '#00530e'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#121414'
  on-background: '#e3e2e2'
  surface-variant: '#343535'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  data-display:
    fontFamily: monospace
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  data-code:
    fontFamily: monospace
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  nav-secondary:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.2'
  label-caps:
    fontFamily: monospace
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 4px
  gutter: 16px
  margin-mobile: 12px
  margin-desktop: 24px
  stack-tight: 8px
  stack-loose: 32px
---

## Brand & Style

This design system is engineered for the high-stakes environment of blockchain infrastructure management. The aesthetic is "Terminal-Plus"—a fusion of raw computational power and modern UI sophistication. It evokes the feeling of a mission-critical command center, where precision is paramount and latency is the enemy.

The style leans heavily into **Technical Brutalism**. It rejects soft aesthetics in favor of rigid structure, high-contrast data visualization, and explicit mechanical layouts. The interface should feel like a high-performance tool rather than a consumer application, prioritizing rapid information retrieval, real-time monitoring, and absolute clarity under pressure.

## Colors

The color palette is built on a foundation of **Deep Indigo**, providing a sense of immense depth and reduced eye strain during long-term monitoring. 

- **Primary Background:** A deep, near-black indigo used for the canvas.
- **Matrix Green:** Reserved strictly for success states, active node status, and primary "Go" actions. It serves as the primary data highlight.
- **Graphite:** Used for structural borders, separators, and inactive states. This color defines the physical "skeleton" of the UI.
- **Alert States:** Critical errors utilize a high-saturation red to pierce the dark environment, ensuring immediate cognitive recognition of failures.

## Typography

This system employs a dual-font strategy to balance technical utility with navigational clarity. 

1.  **Technical Data:** All metrics, logs, hashes, and real-time streams must use a **Monospace font**. This ensures vertical alignment of numbers and characters, facilitating rapid visual scanning of data tables and logs.
2.  **Navigation & UI:** **Space Grotesk** is used for headlines to maintain a futuristic, geometric edge. **Work Sans** is used for secondary UI elements and descriptive text where readability and space efficiency are required.

All labels should be concise. Use uppercase monospace for meta-labels to distinguish "system-generated" descriptors from user-generated content.

## Layout & Spacing

The layout is built on a strict **4px baseline grid**, reinforcing the computational nature of the design. 

- **Density:** The system prioritizes information density. Padding is kept to the functional minimum to allow for more data-points on screen, particularly on mobile "at-a-glance" dashboards.
- **Grid Patterns:** Subtle 1px graphite grid lines may be used as background motifs to help the eye track data across large spans of screen real estate.
- **Mobile First Status:** On mobile devices, the layout shifts to a single-column stack of high-priority "Status Cards," with real-time alert banners pinned to the top of the viewport.

## Elevation & Depth

This system avoids soft shadows and organic depth. Instead, hierarchy is established through **Tonal Layering** and **Structural Borders**.

- **Surface 0:** The deepest indigo (#08090F) for the global background.
- **Surface 1:** The primary indigo (#0F111A) for card containers and sidebar elements.
- **Borders:** All containers are defined by 1px solid **Graphite** borders. There is no blur or shadow.
- **Interactive Depth:** When an element is active or hovered, the border color transitions to **Matrix Green**, creating a "glow-wire" effect rather than an elevation change.

## Shapes

The shape language is **strictly orthogonal**. 

- **Sharp Edges:** All buttons, cards, and input fields use 0px border-radius. This reinforces the "hard-tech" engineering aesthetic and maximizes screen efficiency by eliminating wasted corner pixels.
- **Data Accents:** Use 45-degree clipped corners (dog-ears) for decorative accents on active tabs or critical alert banners to imply a "high-tech" modularity.

## Components

- **Buttons:** Sharp-edged, solid Graphite background with Matrix Green text for primary actions. On hover, the background fills with Matrix Green and the text flips to Deep Indigo.
- **Status Chips:** Small, monospace-only badges. Active nodes pulse with a 2px Matrix Green dot. Critical nodes use a solid Alert Red background with white text.
- **Data Logs:** Monospace text on a slightly darker background than the container. Every line should be numbered.
- **Input Fields:** Minimalist. A bottom-only border in Graphite that turns into a full Matrix Green box outline only when focused.
- **Real-Time Graphs:** Vector lines in Matrix Green with no fills. Use a subtle Graphite grid background for the graph area.
- **Alert Banners:** Full-width, high-contrast banners (Alert Red or Warning Gold) that stick to the top of the UI, using bold monospace headers.