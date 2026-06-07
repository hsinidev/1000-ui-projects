---
name: Venture-Academy Design System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb596'
  primary: '#ffb596'
  on-primary: '#581e00'
  primary-container: '#ff6600'
  on-primary-container: '#561d00'
  inverse-primary: '#a33e00'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#979696'
  on-tertiary-container: '#2f2f2f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb596'
  on-primary-fixed: '#360f00'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: JetBrains Mono
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 2.5rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 1.5rem
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  mono-label:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.1em
  data-point:
    fontFamily: JetBrains Mono
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0em
spacing:
  unit: 4px
  gutter: 1px
  margin-sm: 16px
  margin-md: 24px
  margin-lg: 48px
  container-max: 1440px
---

## Brand & Style

This design system is built on the philosophy of **Industrial Functionalism**. It bridges the gap between high-stakes venture capital and engineering precision. The aesthetic is "engineering-grade," prioritizing clarity, data density, and a utilitarian atmosphere.

The style leans heavily into **Brutalism** and **Technical Minimalism**, utilizing rigid structures that suggest a blueprint or a terminal. It is designed to evoke a sense of "work-in-progress" excellence—where the focus is on the raw mechanics of building and funding startups. 

**Visual Keynotes:**
- **Technical Accents:** Small-scale typography for coordinates, version numbers, and system status.
- **Rigidity:** Strict adherence to a visible or felt grid.
- **Urgency:** Use of high-visibility safety colors for critical actions.

## Colors

The palette is rooted in a high-contrast, dark-mode-first environment. 

- **Primary (Safety Orange):** Reserved strictly for primary calls to action, active states, and critical alerts. It represents the "active" current in the machine.
- **Charcoal & Deep Surfaces:** Backgrounds use `#242424`. Secondary surfaces or containers use slightly lighter tones (`#2A2A2A`) to create hierarchy without using shadows.
- **White:** Used for primary content, headers, and high-contrast UI elements to ensure maximum legibility against the dark background.
- **Technical Accents:** A matrix-green or amber may be used sparingly for status indicators, mimicking hardware LEDs.

## Typography

Typography follows a dual-path logic: **JetBrains Mono** for structural, technical, and navigational elements; **Inter** for long-form reading and data-heavy body content.

- **Headlines:** Always Monospace. Use all-caps sparingly for section headers to evoke a "manual" or "logbook" feel.
- **Body:** Inter provides the necessary legibility for complex venture math and curriculum text.
- **Metadata:** Use `mono-label` for small technical details like coordinates (e.g., `SECTION_01 // 40.7128° N`), timestamps, or breadcrumbs.

## Layout & Spacing

The layout is a **Rigid Fixed-Width Grid** or a **Tight Fluid Grid** that mimics technical schematics. 

- **The Grid:** A 12-column system where columns are separated by visible 1px borders rather than empty gutters.
- **Borders as Spacing:** Elements should feel "locked" into their grid cells. Vertical and horizontal lines should be used to separate content blocks, creating a "blueprint" effect.
- **Density:** High information density is preferred. Whitespace should be intentional and "boxed in" by borders rather than flowing freely.
- **Technical Accents:** Place small "+" symbols or coordinate markers (e.g., [A1], [B2]) at the intersection of major grid lines.

## Elevation & Depth

This design system avoids shadows entirely to maintain its "flat-industrial" aesthetic. Depth is achieved through **Tonal Layering** and **High-Contrast Outlines**.

- **Surface Tiers:** Background is `#242424`. Raised cards or active panels use a slightly lighter `#2D2D2D`. 
- **Borders:** Use solid 1px or 2px borders. For inactive elements, use `#333333`. For active or "focused" elements, use the Safety Orange.
- **Intersections:** Use hairline rules to divide sections. Where panels overlap (like a modal or a slide-out), use a solid 2px white or orange border to create a sharp "cut-out" effect against the background.

## Shapes

The shape language is strictly **Geometric and Sharp**. 

- **Corner Radius:** All elements (buttons, inputs, cards, tags) have a 0px radius. Roundness is forbidden to maintain the industrial, precision-machined look.
- **Iconography:** Use stroke-based icons with sharp angles and consistent 2px weights. 
- **Buttons:** Rectangular blocks. Primary buttons should be solid Safety Orange with black text for maximum punch.

## Components

### Buttons
- **Primary:** Solid `#FF6600` background, `#242424` text, JetBrains Mono Bold. 
- **Secondary:** Transparent background, 1px `#FFFFFF` border, white text.
- **Ghost:** Monospace text with a leading `>` character (e.g., `> INITIALIZE_TX`).

### Input Fields
- **Default:** Transparent background with a bottom border or full 1px border in `#404040`.
- **Focus:** Border changes to `#FF6600`. Include a small blinking cursor or a "System Ready" label in the corner.

### Status Indicators
- Use small circular "LED" dots. 
- Colors: `#00FF41` (Active/Ready), `#FF6600` (Processing), `#FF0000` (Error).

### Data Cards
- Rigid containers with visible 1px borders. 
- Include a "Header Strip" in a contrasting gray with the title in a small Monospace font.

### Progress Bars
- Stepped, blocky indicators rather than smooth fills. Each segment represents a distinct percentage (e.g., 10 blocks for 100%).

### Technical Accents
- **Crosshairs:** Use small "L" shaped brackets on the four corners of primary image containers or video players.
- **Breadcrumbs:** Use `/` separators (e.g., `HOME / VENTURE_CAPITAL / MODULE_04`).