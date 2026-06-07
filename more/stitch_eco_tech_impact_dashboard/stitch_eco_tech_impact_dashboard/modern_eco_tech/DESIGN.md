---
name: Modern Eco-Tech
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3e4a3f'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#6e7a6e'
  outline-variant: '#bdcabc'
  surface-tint: '#006d36'
  primary: '#006d36'
  on-primary: '#ffffff'
  primary-container: '#50c878'
  on-primary-container: '#005025'
  inverse-primary: '#66dd8b'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#49645d'
  on-tertiary: '#ffffff'
  tertiary-container: '#9bb8b0'
  on-tertiary-container: '#2f4943'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#83fba5'
  primary-fixed-dim: '#66dd8b'
  on-primary-fixed: '#00210c'
  on-primary-fixed-variant: '#005227'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#cbe9e0'
  tertiary-fixed-dim: '#b0cdc5'
  on-tertiary-fixed: '#04201b'
  on-tertiary-fixed-variant: '#324c46'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  data-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 40px
  card-padding: 24px
  stack-sm: 8px
  stack-md: 16px
---

## Brand & Style

This design system establishes a high-fidelity environment for sophisticated green investing. The brand personality is "Analytic Naturalism"—bridging the gap between raw environmental impact and precise financial growth. It targets institutional-grade retail investors who demand data density without sacrificing the emotional connection to ecological health.

The visual style is a refined **Glassmorphism**. By using translucent layers and high-precision borders, the UI evokes the feeling of looking through a clean laboratory lens at a lush forest. It balances "High-Tech" (transparency, neon accents, precision grids) with "Grounded Nature" (organic hues, soft blurs, and spacious layouts). The resulting experience is premium, trustworthy, and forward-thinking.

## Colors

The palette is anchored by **Emerald Green (#50C878)**, used strategically for growth indicators, primary actions, and brand accents. **Frosted White (#F5F5F5)** serves as the base for light mode, providing a crisp, airy foundation. **Slate Grey (#708090)** handles secondary data and utility elements, ensuring financial legibility without the harshness of pure black.

In Dark Mode, the system pivots to **Deep Forest (#05110F)** surfaces. The Emerald Green remains the primary accent but gains a subtle outer glow to simulate bioluminescence. Surfaces utilize a dark-tinted glass effect, layering deep greens over slate to maintain a sense of depth and organic richness.

## Typography

The typography system uses a tri-font approach to manage high data density with professional clarity. **Manrope** is used for headlines to provide a modern, balanced, and premium feel. **Inter** serves as the workhorse for body copy and financial tables, chosen for its exceptional readability at small sizes. **Space Grotesk** is reserved for labels and mono-style data points to inject a "tech" edge.

Financial data should always prioritize vertical alignment. Use tabular lining for numbers within data-dense grids to ensure that investment totals and percentage changes remain easy to scan and compare.

## Layout & Spacing

The layout utilizes a **12-column fluid grid** designed for dashboard environments. To accommodate high data density, the system employs a "tight-yet-breathable" rhythm based on a 4px baseline. Gutters are generous at 24px to prevent the glassmorphic blurs of adjacent cards from bleeding into a cluttered visual mess.

Information is grouped into logical modules. Large-scale data visualizations (charts) should span at least 8 columns, while secondary metrics and "Carbon Offset" stats occupy 4-column widgets. Margins are kept wide (40px) to maintain a premium, editorial feel that distinguishes the platform from utilitarian banking apps.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and backdrop saturation rather than traditional heavy shadows.

1.  **Base Layer:** The background uses a subtle radial gradient (Emerald to Frosted White/Deep Forest) to provide a sense of natural light.
2.  **Mid Layer (Cards):** Surfaces use a `backdrop-filter: blur(20px)` with a 60% opacity fill. A 1px solid border (white at 20% opacity) defines the edge.
3.  **High Layer (Modals/Popovers):** Increased blur (40px) and a slightly thicker, brighter border.
4.  **Shadows:** When used, shadows are "Ambient Tints"—low-spread, high-blur shadows that inherit a slight green hue (#50C878 at 10% opacity) to simulate light passing through a forest canopy.

## Shapes

The shape language is **Rounded (Level 2)**. A base radius of 0.5rem (8px) is applied to buttons and input fields, while larger containers and Glassmorphic cards use a 1rem (16px) or 1.5rem (24px) radius. This "squircle" approach softens the technical data and makes the interface feel more organic and approachable, reflecting the "Eco" aspect of the brand.

Charts and data visualizations should avoid sharp 90-degree corners; line graphs should use smooth tension (monotone cubic interpolation) to mimic the flowing lines found in nature.

## Components

*   **Glassmorphic Cards:** The primary container. Features a subtle inner glow on the top-left edge to simulate a light source hitting glass.
*   **Dynamic Charts:** Use Emerald Green for positive growth and Slate Grey for baseline data. Negative trends are represented by a muted "Earthen Red" (#D27D60). Chart fills use a linear gradient from Emerald (20% opacity) to transparent.
*   **Eco-Tech Icons:** Custom weight (1.5px) stroke icons. Elements like "Growth" should be represented by leaf-integrated bar charts; "Security" by a shield with a vein pattern.
*   **Dark-Mode Toggle:** A prominent, high-tactile switch. In light mode, it features a sun icon over a sky-blue gradient; in dark mode, a crescent moon over a deep forest-green gradient.
*   **Buttons:** Primary buttons are solid Emerald Green with white text. Secondary buttons are "Ghost" style with a glass border and frosted background.
*   **Input Fields:** Translucent fills with 1px borders that "bloom" (glow) in Emerald Green when focused.
*   **Impact Tracker:** A custom component displaying real-time carbon sequestration or tree-planting equivalents, using high-precision typography and animated SVG icons.