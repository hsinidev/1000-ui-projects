---
name: Geometric STEM System
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#434656'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004dea'
  primary: '#0041c8'
  on-primary: '#ffffff'
  primary-container: '#0055ff'
  on-primary-container: '#e3e6ff'
  inverse-primary: '#b6c4ff'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#505050'
  on-tertiary: '#ffffff'
  tertiary-container: '#686868'
  on-tertiary-container: '#e8e8e8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#001551'
  on-primary-fixed-variant: '#0039b3'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Space Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin: 32px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  stack-xl: 64px
---

## Brand & Style

This design system is built on the intersection of laboratory precision and playground curiosity. It utilizes a **Geometric Minimalist** style that prioritizes clarity and structural integrity, reflecting the logic of STEM education. The aesthetic is "Technical-Tactile"—it feels like a high-end digital tool for parents while remaining inviting enough for children to explore. 

The visual language avoids organic, soft blobs in favor of intentional, mathematical shapes. It evokes a sense of "Engineering the Future," where every UI element feels like a building block in a larger logical sequence. The emotional response is one of confidence, innovation, and "Eureka" moments.

## Colors

The palette is anchored by **Electric Blue**, a high-energy primary that signals action, interactivity, and digital innovation. **Silver** serves as the structural secondary, providing a metallic, "hardware" feel that bridges the gap between software and physical engineering.

**High-Contrast Neutrals** (deep blacks and rich grays) are used for typography and borders to ensure maximum readability and a professional "blueprint" aesthetic. White is the primary canvas color, used generously to provide the "clean" atmosphere required for focused learning. Interaction states (hover/active) should utilize brightness shifts of the Electric Blue rather than introducing new hues.

## Typography

**Space Grotesk** is the sole typeface for this design system, chosen for its idiosyncratic geometric construction and tech-forward personality. Its open counters and distinct letterforms provide excellent legibility for early readers, while its "monospaced-adjacent" look appeals to the scientific nature of the platform.

Headlines should be set with tight letter spacing to emphasize the geometric "lock-up" of the characters. Body text requires generous line height (1.6) to prevent visual fatigue during learning exercises. All labels and metadata should use a slightly heavier weight to maintain the crisp, high-contrast requirement of the brand.

## Layout & Spacing

This design system employs a **12-column fixed grid** for desktop and a **4-column fluid grid** for mobile. The layout is strictly modular, meaning every component's height and width should ideally be a multiple of the **8px base unit**. 

Spacing is utilized to create "Information Zones." Learning areas use wider margins (stack-xl) to reduce cognitive load and focus attention on a single task. Parent dashboards and admin areas utilize denser spacing (stack-md) to allow for data-rich overviews of stats and progress.

## Elevation & Depth

Elevation is conveyed through **Bold Borders** and **Tonal Layers** rather than soft ambient shadows. This maintains the "crisp" and "geometric" requirement.

1.  **Level 0 (Floor):** Pure White (#FFFFFF).
2.  **Level 1 (Cards/Containers):** 1px solid border (#E5E7EB) or Silver background.
3.  **Level 2 (Interactive/Floating):** 2px solid border in Neutral Dark or Electric Blue.

To simulate depth, use a "Hard Shadow" technique: a solid offset block of color (usually Silver or a light gray) 4px behind a primary element, creating a tactile, button-like appearance without blurring the edges.

## Shapes

The design system uses a consistent **8px (0.5rem)** corner radius for all primary containers, buttons, and input fields. This specific "Rounded" level is chosen to make the geometric shapes feel modern and "touchable" without becoming bubbly or juvenile.

Iconography and decorative elements should mirror this: icons should have a 1.5px or 2px stroke width with slightly rounded terminals. Large layout sections may use "Chiseled" corners (45-degree cuts) occasionally to emphasize the STEM/Engineering theme, but the 8px radius remains the standard for user-interactive elements.

## Components

### Buttons
Primary buttons are solid **Electric Blue** with white text, featuring 8px rounded corners. The "Pressed" state should shift 2px down and right to simulate a physical click, often revealing a 1px dark stroke.

### Input Fields
Inputs use a white background with a 1px Silver border. On focus, the border thickens to 2px and changes to Electric Blue. Label text is always positioned above the field in **Label-Bold** style.

### Cards
Cards for learning modules use a 1px border. For children, cards can include a subtle Silver "Hard Shadow" to make them look like physical tiles. For parents, cards are flatter and use Tonal Layers to separate data sets.

### Chips & Badges
Used for categories like "Science" or "Math." These are pill-shaped (overriding the 8px rule to distinguish them as tags) with a light Silver background and high-contrast dark text.

### Progress Indicators
Progress is shown through thick, 8px-high horizontal bars. The "unfilled" portion is Silver, and the "filled" portion is Electric Blue, ensuring the high-contrast requirement is met for clear feedback.

### STEM Specifics
- **Formula Blocks:** Monospaced-looking containers using Space Grotesk for displaying equations.
- **Achievement Hexagons:** Geometric badges awarded for progress, using the 8px corner logic applied to a hexagonal path.