---
name: Offensive Intelligence
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#f8f5f5'
  on-tertiary: '#303030'
  tertiary-container: '#dbd9d8'
  on-tertiary-container: '#5f5e5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is engineered to evoke the high-stakes environment of offensive cybersecurity and real-time threat hunting. The brand personality is clinical, authoritative, and hyper-efficient, prioritizing rapid data processing and signal detection over decorative elements. The target audience includes Tier 3 SOC analysts and threat researchers who require a high-density, low-fatigue interface for prolonged deep-work sessions.

The aesthetic leans heavily into **Offensive-Tech**, a blend of **Minimalism** and **High-Contrast Tactical** design. It utilizes a "black-out" foundation to eliminate visual noise, allowing critical alerts to pierce the interface with neon intensity. The style emphasizes technical precision through sharp geometric lines, monochromatic depth, and subtle emissive glows that simulate a high-performance terminal.

## Colors

The palette is anchored by **Matte Black (#050505)** and **Graphite (#1A1A1A)** to create a void-like environment where depth is defined by texture rather than brightness. The primary action and "alive" state color is **Neon Cyan (#00F0FF)**, used sparingly for active signals, primary buttons, and critical data paths.

- **Primary (Neon Cyan):** Reserved for data highlights, active selection states, and primary calls to action. It should always carry a subtle 2px Gaussian blur glow when used against pure black backgrounds.
- **Secondary (Graphite):** Used for structural elements like sidebars and container backgrounds to differentiate them from the void background.
- **Surface (Matte Black):** The default application background.
- **Functional Accents:** A high-saturation "Blood Red" (#FF003C) is used exclusively for detected threats and anomalies, creating an immediate visual hierarchy of urgency.

## Typography

This design system utilizes a dual-font strategy to balance technical aesthetics with readability. **Space Grotesk** is used for headlines, labels, and data points to provide a futuristic, geometric feel that mirrors terminal outputs. Its eccentric character shapes reinforce the "tech" aesthetic. 

**Inter** is utilized for body copy and dense descriptions, providing the necessary neutral grounding for long-form logs and analytical reports. All typography should be rendered with high contrast against the dark background, utilizing pure white (#FFFFFF) for primary text and a 60% opacity white (#999999) for secondary descriptions.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with a rigid 4px base unit to ensure all elements align to a technical "pixel-perfect" rhythm. The system uses a 12-column grid for dashboard views, with tight 16px gutters to maintain a high-density information environment.

Data visualizations should span specific column increments (3, 6, or 12) to maintain horizontal alignment across the dashboard. Padding within containers is kept minimal (12px to 16px) to maximize the "data-to-ink" ratio, allowing as much information on screen as possible without sacrificing clarity.

## Elevation & Depth

In this dark-mode-only system, depth is conveyed through **Tonal Layering** and **Subtle Outlines** rather than traditional shadows. 

1.  **Level 0 (Background):** Pure Matte Black (#050505).
2.  **Level 1 (Containers):** Graphite (#1A1A1A) with a 1px solid border of #333333.
3.  **Level 2 (Active Elements):** Same as Level 1, but with a 1px solid border of Neon Cyan (#00F0FF) and a 4px outer glow of the same color at 20% opacity.

Floating elements like tooltips or context menus should use a semi-transparent blur effect (Backdrop Filter: blur(10px)) to maintain context of the data underneath while clearly separating the foreground layer.

## Shapes

The design system employs a **Sharp (0px)** corner radius across all UI components. This rejection of rounded corners emphasizes the "offensive" and "technical" nature of the tool, signaling precision and a lack of decorative softness. 

Buttons, input fields, cards, and data bars must all feature 90-degree angles. To prevent the UI from feeling dated, these sharp edges are paired with ultra-thin 1px borders and occasional "clipped corner" accents on primary headers to evoke stealth-tech aesthetics.

## Components

- **Buttons:** Primary buttons are solid Neon Cyan with black text, featuring a subtle outer glow. Secondary buttons are transparent with a 1px Graphite border.
- **Chips/Badges:** Small, rectangular blocks with monospaced text. For "Critical" status, the chip should have a solid Blood Red background; for "Active," a Neon Cyan outline.
- **Input Fields:** Bottom-border only or full-outline fields in Graphite. On focus, the border transitions to Neon Cyan with a faint vertical "scanline" animation.
- **Cards:** Simple Graphite rectangles. Headers within cards should be separated by a 1px horizontal line.
- **Data Visualizations:** Line charts should use 1px width lines with a gradient fill below the line that fades to transparent. Anomaly points should be marked with a "crosshair" icon.
- **Terminal Feed:** A dedicated component for real-time logs using the `mono-data` typography, featuring a blinking 1px cursor and high-speed scroll animations.
- **Scanlines:** A global, low-opacity (2%) horizontal pattern overlaying the entire UI to simulate a high-tech monitor.