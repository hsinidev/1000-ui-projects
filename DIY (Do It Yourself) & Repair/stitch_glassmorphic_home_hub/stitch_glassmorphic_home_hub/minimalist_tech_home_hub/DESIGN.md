---
name: Minimalist-Tech Home Hub
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bac9cc'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849396'
  outline-variant: '#3b494c'
  surface-tint: '#00daf3'
  primary: '#c3f5ff'
  on-primary: '#00363d'
  primary-container: '#00e5ff'
  on-primary-container: '#00626e'
  inverse-primary: '#006875'
  secondary: '#b0c6ff'
  on-secondary: '#002d6e'
  secondary-container: '#0068ed'
  on-secondary-container: '#f2f3ff'
  tertiary: '#efecec'
  on-tertiary: '#313030'
  tertiary-container: '#d3d0cf'
  on-tertiary-container: '#5a5959'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#9cf0ff'
  primary-fixed-dim: '#00daf3'
  on-primary-fixed: '#001f24'
  on-primary-fixed-variant: '#004f58'
  secondary-fixed: '#d9e2ff'
  secondary-fixed-dim: '#b0c6ff'
  on-secondary-fixed: '#001945'
  on-secondary-fixed-variant: '#00429b'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

The visual identity of this design system centers on the intersection of absolute privacy and high-performance automation. It evokes the feeling of a "digital sanctuary"—a secure, silent guardian for the home. The aesthetic is defined by **Minimalist-Tech**, utilizing a sophisticated dark-mode environment where depth is created through translucency rather than heavy shadows.

The emotional response should be one of calm control. By stripping away unnecessary ornamentation and relying on **Glassmorphism**, the UI feels lightweight and non-intrusive. High-tech precision is signaled through razor-thin borders and soft, atmospheric glows that indicate activity without causing visual fatigue. This system prioritizes clarity and speed, ensuring the user feels the software is a powerful, transparent tool rather than a complex burden.

## Colors

The palette is rooted in the "Deep Grid"—a collection of near-black grays and pure blacks that preserve OLED power efficiency and minimize light bleed in home environments. 

- **Foundation:** The base background is an absolute black to provide infinite depth.
- **Accents:** The Primary Cyan (#00E5FF) is used exclusively for active states, connectivity indicators, and "online" signatures. It should be applied with a soft Gaussian blur (glow) to simulate hardware LEDs.
- **Glass System:** Surfaces use a semi-transparent dark gray with a high background blur (20px–40px). Every glass element must feature a 1px solid border in `glass_stroke` to define edges against the dark background.
- **Privacy Mode:** When sensitive data is displayed, the UI should shift toward the Secondary Blue to signal a "Secure State."

## Typography

This design system utilizes a dual-font strategy to balance human-centric control with technical precision. 

**Manrope** is the primary typeface for all functional communication and headings. It provides a warm, modern, and trustworthy feel that keeps the automation hub from feeling overly sterile. 

**Space Grotesk** is reserved for technical data points, sensor readings, and system logs. Its geometric, tech-forward construction mimics the look of monospace type without sacrificing readability. Use `label-caps` for section headers within cards to reinforce the "instrument panel" aesthetic. All numerical data should be rendered in `data-mono` to ensure alignment and a high-tech cadence.

## Layout & Spacing

The layout follows a **Fluid Grid** model with a modular 8px rhythm. The structure is designed to be "edge-to-edge" on smaller control tablets but transitions to a centered, max-width container (1440px) on desktop displays.

- **Grid:** Use a 12-column grid for dashboards. 
- **Gaps:** Elements are separated by a 24px gutter to maintain a sense of "air" and minimalism.
- **Padding:** Internal card padding should be generous (24px) to ensure touch targets are accessible for wall-mounted tablets.
- **Alignment:** All technical data labels should align to the top-left of their respective containers, while primary actions (switches/sliders) should occupy the bottom or right-hand zones for ergonomic access.

## Elevation & Depth

Depth is achieved through **Glassmorphism and Tonal Layering** rather than traditional drop shadows. 

1.  **Level 0 (Floor):** Pure black (#000000). The void where the background sits.
2.  **Level 1 (Base Layer):** Dark charcoal surfaces (#0A0A0A) used for sidebars or secondary navigation.
3.  **Level 2 (Active Cards):** Frosted glass panels (`glass_fill`) with a 32px backdrop blur. These elements "float" above the floor.
4.  **Level 3 (Modals/Overlays):** Lighter glass panels with a 1px bright cyan border glow.

Avoid using heavy black shadows. Instead, use a very faint, spread-out glow in the primary color (opacity 5-10%) to suggest that an active component is emitting light onto the surface below it.

## Shapes

The shape language is "Soft-Tech." While the overall aesthetic is precise and grid-based, sharp corners are avoided to make the home environment feel more inviting.

- **Standard Radius:** 4px (0.25rem) for small elements like checkboxes and input fields.
- **Component Radius:** 8px (0.5rem) for cards, buttons, and glass panels.
- **Large Radius:** 12px (0.75rem) for main dashboard containers or modal windows.

This subtle rounding maintains a professional, "machined" look (reminiscent of brushed aluminum or cut glass) while removing the aggression of 90-degree angles.

## Components

- **Buttons:** Primary buttons should be ghost-style with a 1px `primary_color` border and a subtle inner glow. On hover, the background fills with a 10% opacity primary color.
- **Cards:** The core of the system. Cards must use the glass effect with a `glass_stroke` border. Titles should be in `label-caps` at the top left.
- **Switches & Toggles:** Use a "pill" track but keep the thumb square-ish (4px radius) to maintain the tech feel. When "on," the track should emit a soft cyan glow.
- **Data Visualizations:** Charts should use thin 1px lines without area fills. Use the primary color for the data line and a secondary blue for historical comparisons.
- **Status Indicators:** Use small "pulsing" circles for active sensors. The pulse should be a soft, expanding ring of the primary color with 0% opacity at the outer edge.
- **Input Fields:** Bottom-border only or very subtle 1px glass borders. When focused, the bottom border glows cyan.
- **Monitors:** A specialized component for displaying live camera feeds or energy usage logs, using `data-mono` typography overlays on top of the frosted glass footer.