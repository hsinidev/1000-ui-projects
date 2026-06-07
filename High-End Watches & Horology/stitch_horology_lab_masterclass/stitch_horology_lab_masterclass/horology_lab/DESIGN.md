---
name: Horology-Lab
colors:
  surface: '#faf9f6'
  surface-dim: '#dadad7'
  surface-bright: '#faf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f4f0'
  surface-container: '#eeeeea'
  surface-container-high: '#e8e8e5'
  surface-container-highest: '#e2e3df'
  on-surface: '#1a1c1a'
  on-surface-variant: '#434843'
  inverse-surface: '#2f312f'
  inverse-on-surface: '#f1f1ed'
  outline: '#747872'
  outline-variant: '#c3c8c1'
  surface-tint: '#526255'
  primary: '#455548'
  on-primary: '#ffffff'
  primary-container: '#5d6d5f'
  on-primary-container: '#ddeedd'
  inverse-primary: '#bacbba'
  secondary: '#6b5c4c'
  on-secondary: '#ffffff'
  secondary-container: '#f4dfcb'
  on-secondary-container: '#716252'
  tertiary: '#52514f'
  on-tertiary: '#ffffff'
  tertiary-container: '#6b6967'
  on-tertiary-container: '#ede9e6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e7d6'
  primary-fixed-dim: '#bacbba'
  on-primary-fixed: '#101f14'
  on-primary-fixed-variant: '#3b4a3e'
  secondary-fixed: '#f4dfcb'
  secondary-fixed-dim: '#d7c3b0'
  on-secondary-fixed: '#241a0e'
  on-secondary-fixed-variant: '#524436'
  tertiary-fixed: '#e5e2df'
  tertiary-fixed-dim: '#c9c6c3'
  on-tertiary-fixed: '#1c1b1a'
  on-tertiary-fixed-variant: '#484745'
  background: '#faf9f6'
  on-background: '#1a1c1a'
  surface-variant: '#e2e3df'
typography:
  display-lg:
    fontFamily: Literata
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Literata
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
  body-main:
    fontFamily: Literata
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  data-mono:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  gutter: 24px
  margin: 32px
---

## Brand & Style
This design system centers on the intersection of horological precision and the tactile humanity of craftsmanship. The aesthetic is "Scientific & Human"—a blend of laboratory-grade organization and the warmth of a master watchmaker’s workbench. 

The style leans into **Minimalism** with a **Tactile** edge. It prioritizes high-end educational delivery through a methodical layout, ensuring that complex technical data feels approachable. The emotional response is one of calm focus, academic authority, and premium exclusivity. High-density information is balanced by generous whitespace and soft, organic shapes that mimic the curves of a watch crystal or a polished movement plate.

## Colors
The palette is rooted in the natural materials of a traditional workshop. 

*   **Sage Green (Primary):** A muted, sophisticated green used for primary actions, progress indicators, and branding. It represents the "Lab" aspect—controlled and calm.
*   **Pale Wood (Secondary):** A warm, sandy beige used for accents and secondary containers. It introduces the "Human" element, evoking the workbench.
*   **Crisp White & Off-White:** The primary background is pure white to maintain a clinical, educational clarity, while the tertiary off-white is used for subtle sectioning.
*   **Ink Black (Neutral):** A soft black used for typography to ensure maximum legibility without the harshness of true hex #000.

## Typography
The typographic system creates a dialogue between tradition and technology.

*   **The Editorial Voice:** **Literata** is used for all narrative and instructional content. Its calligraphic roots and modern proportions make long-form educational reading comfortable and authoritative.
*   **The Technical Voice:** **JetBrains Mono** is utilized for technical specifications, measurements, timestamps, and UI labels. This monospaced font conveys the mechanical precision of watchmaking and the methodical nature of the lab.
*   **Hierarchy:** Large headlines should use tighter tracking, while technical labels should be all-caps with increased letter spacing to emphasize their "labeled instrument" character.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy for desktop (1280px max-width) to replicate the focused view through a loupe. It utilizes a 12-column structure with generous gutters to prevent visual clutter.

Spacing is based on a 4px baseline grid. Content-heavy pages (like lessons) should use an asymmetric layout: a wide column for video/editorial and a narrower side column for technical specs and data-viz. Wide margins (the 'xl' unit) are encouraged to frame the "Scientific" content with "Human" breathing room.

## Elevation & Depth
This design system avoids heavy shadows in favor of **Tonal Layers** and **Low-Contrast Outlines**. 

*   **Tiers:** Depth is created by placing white cards on `tertiary_color_hex` (Pale Wood/Off-white) backgrounds.
*   **Borders:** Use 1px solid borders in a lightened version of the Sage Green or a subtle grey (#E0E0E0) to define containers.
*   **Glassmorphism:** Use a subtle backdrop blur on fixed navigation bars to maintain the "clean lab" feel without obstructing the underlying content flow.
*   **Focus:** Elevation is only used for active overlays (modals or tooltips), where a soft, diffused ambient shadow with a hint of Sage Green tinting is permitted.

## Shapes
The shape language is deliberately **Organic and Rounded** to soften the sharp edges of mechanical diagrams and watch parts.

*   **Containers:** Use `rounded-lg` (1rem) for most content cards and educational modules.
*   **Interactive Elements:** Buttons and tags should utilize a full pill-shape (radius: 999px) to contrast against the rigid, straight lines of monospaced typography.
*   **Media:** Video players and image containers must always feature a radius to maintain the "human" aesthetic.

## Components
*   **Buttons:** Primary buttons are pill-shaped, Sage Green with white Literata text. Secondary buttons use a Pale Wood background with Sage Green text.
*   **Technical Chips:** Use JetBrains Mono in all-caps inside a small, pill-shaped container with a 1px border. Use these for watch specs (e.g., "30M WATER RESISTANT").
*   **Input Fields:** Clean, minimal fields with a 1px bottom border that transforms into a full-pill outline when focused.
*   **Progress Indicators:** Circular "movement-inspired" loaders or thin, precise horizontal bars in Sage Green.
*   **Cards:** White backgrounds with `rounded-lg` corners. Headers inside cards should use a subtle Pale Wood background-fill to separate "Context" from "Content."
*   **Micro-interactions:** Transitions should be fluid and decelerated, mimicking the sweep of a high-frequency mechanical watch hand.