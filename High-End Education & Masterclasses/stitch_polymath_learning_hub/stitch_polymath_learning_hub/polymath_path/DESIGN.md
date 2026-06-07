---
name: Polymath-Path
colors:
  surface: '#141218'
  surface-dim: '#141218'
  surface-bright: '#3b383e'
  surface-container-lowest: '#0f0d13'
  surface-container-low: '#1d1b20'
  surface-container: '#211f24'
  surface-container-high: '#2b292f'
  surface-container-highest: '#36343a'
  on-surface: '#e6e0e9'
  on-surface-variant: '#cbc4d2'
  inverse-surface: '#e6e0e9'
  inverse-on-surface: '#322f35'
  outline: '#948e9c'
  outline-variant: '#494551'
  surface-tint: '#cfbcff'
  primary: '#cfbcff'
  on-primary: '#381e72'
  primary-container: '#6750a4'
  on-primary-container: '#e0d2ff'
  inverse-primary: '#6750a4'
  secondary: '#cdc0e9'
  on-secondary: '#342b4b'
  secondary-container: '#4d4465'
  on-secondary-container: '#bfb2da'
  tertiary: '#e7c365'
  on-tertiary: '#3e2e00'
  tertiary-container: '#c9a74d'
  on-tertiary-container: '#503d00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#cfbcff'
  on-primary-fixed: '#22005d'
  on-primary-fixed-variant: '#4f378a'
  secondary-fixed: '#e9ddff'
  secondary-fixed-dim: '#cdc0e9'
  on-secondary-fixed: '#1f1635'
  on-secondary-fixed-variant: '#4b4263'
  tertiary-fixed: '#ffdf93'
  tertiary-fixed-dim: '#e7c365'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#594400'
  background: '#141218'
  on-background: '#e6e0e9'
  surface-variant: '#36343a'
typography:
  display-lg:
    fontFamily: Sora
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Sora
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Sora
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
---

## Brand & Style
This design system is built for polymaths and lifelong learners who thrive on cross-disciplinary synthesis. The aesthetic is "Vibrant & Connected," utilizing a dark matte foundation to make high-energy "Aha! Moment" gradients pop with maximum intensity.

The design style merges **Modern High-Contrast** with **Glassmorphism**. It utilizes a "Bento-box" layout pattern—a modular, grid-based approach where information is compartmentalized into clean, distinct cells. This structure reflects the organized yet interconnected nature of complex learning loops. The visual direction is fast-paced and intellectual, favoring sharp lines, purposeful motion, and vivid color transitions to signify the bridging of different knowledge domains.

## Colors
The color strategy revolves around a **Matte Black (#121212)** base to ensure a sophisticated, low-fatigue environment for deep study. Accents are strictly defined by two primary gradient "loops":
- **Intellect Loop:** Electric Purple to Teal. Used for core progression, logic, and completed paths.
- **Energy Loop:** Sunset Orange to Neon Pink. Used for discovery, new insights, and active challenges.

Functional colors (success, error, warning) should be mapped to the closest hues within these gradients to maintain a cohesive, high-energy palette. Surfaces are layered using subtle shifts in dark grays to maintain the Bento-box hierarchy without breaking the immersion of the dark theme.

## Typography
The typography system balances technical precision with bold expression. 
- **Sora** is used for headlines to provide a geometric, forward-looking feel that commands attention. 
- **Hanken Grotesk** serves as the workhorse for body text, ensuring maximum readability during long-form reading sessions. 
- **Space Grotesk** is reserved for labels, data points, and "Bento" headers to lean into the technical, polymathic nature of the content. 

Text should always maintain high contrast against the Matte Black background. Use the Energy Loop gradients sparingly on display type to highlight key "Aha!" phrases.

## Layout & Spacing
The layout follows a **Fixed-Fluid Hybrid Bento Grid**. Content is organized into modular containers (Bento boxes) that sit on a 12-column grid. 

Each box should have consistent internal padding (`md: 1.5rem`) to maintain a clean, rhythmic appearance. Vertical rhythm is driven by an 8px base unit. The "connectivity" aspect of the brand is visualized through "Learning Lines"—thin, 1px gradient strokes that occasionally connect adjacent Bento boxes, guiding the user's eye through the multi-disciplinary loop.

## Elevation & Depth
In this design system, depth is achieved through **Tonal Layering and Glassmorphism** rather than traditional drop shadows.

1.  **Level 0 (Base):** Matte Black (#121212).
2.  **Level 1 (Bento Cards):** Surface Gray (#1E1E1E) with a subtle 1px inner border (10% white opacity).
3.  **Level 2 (Active/Hover):** Glassmorphic overlay. 5% white fill with a 20px backdrop blur and a vibrant gradient border (1.5px).

Shadows, when used, are "Ambient Glows"—highly diffused, low-opacity blurs that take the color of the active gradient (e.g., a soft teal glow beneath a completed module card) to simulate light emission from the "intellect" within the box.

## Shapes
The shape language is "Rounded" to soften the high-contrast intensity and make the interface feel approachable. 

Standard Bento boxes and UI containers use `rounded-lg` (1rem). Small interactive elements like chips and input fields use `rounded-md` (0.5rem). Special call-to-action buttons may use pill-shapes to distinguish them from the modular grid. The consistency of these radii is critical to maintaining the professional, "engineered" feel of the design system.

## Components
- **Bento Cards:** The primary container. Must feature a "Label-caps" header. Borders are subtle unless the card is "Active," in which case it gains a gradient stroke.
- **Action Buttons:** High-energy. Use the "Energy Loop" gradient as a background for primary actions, with white bold text. Secondary actions use ghost styles with gradient borders.
- **Connection Chips:** Small, pill-shaped tags used to show disciplinary tags (e.g., "Physics", "Art"). These use a semi-transparent fill of the "Intellect Loop" colors.
- **Progress Loops:** Circular indicators that use the "Intellect Loop" gradient to show completion.
- **Input Fields:** Minimalist. Darker than the surface color, with a bottom-only gradient border that activates on focus.
- **Aha! Modals:** Full glassmorphic overlays with heavy backdrop blur (30px) to isolate the breakthrough moment from the background grid.