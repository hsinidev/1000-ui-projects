---
name: Aero-Aviation Hub
colors:
  surface: '#f6faff'
  surface-dim: '#d2dbe4'
  surface-bright: '#f6faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#ecf5fe'
  surface-container: '#e6eff8'
  surface-container-high: '#e0e9f2'
  surface-container-highest: '#dbe4ed'
  on-surface: '#141d23'
  on-surface-variant: '#44474e'
  inverse-surface: '#293138'
  inverse-on-surface: '#e9f2fb'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#090b0c'
  on-tertiary: '#ffffff'
  tertiary-container: '#1f2223'
  on-tertiary-container: '#87898a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f6faff'
  on-background: '#141d23'
  surface-variant: '#dbe4ed'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: 48px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
    letterSpacing: 0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  button:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  page-margin: 80px
  section-gap: 120px
  gutter: 24px
  container-max: 1440px
  unit-xs: 4px
  unit-sm: 8px
  unit-md: 16px
  unit-lg: 32px
---

## Brand & Style

The brand personality is rooted in the "Sky-Sleek" aesthetic—a fusion of high-altitude tranquility and executive precision. It targets ultra-high-net-worth individuals and corporate flight departments who demand seamlessness and discretion. The UI must evoke an emotional response of "effortless ascension": the feeling of being above the clouds, away from the friction of the ground.

This design system utilizes a **Minimalist-Glassmorphism** hybrid. It leverages the expansive whitespace of minimalism to signify luxury and "room to breathe," while incorporating glassmorphism’s semi-transparent layers to mimic the look of cockpit instrumentation and cabin windows. High-resolution imagery of expansive horizons and soft-focus aircraft interiors serves as the emotional foundation, while thin-line vector icons ensure the interface feels precise and engineered.

## Colors

The palette is anchored by **Deep Navy Blue**, representing the stability of the night sky and the authority of the aviation industry. **Cloud White** serves as the primary canvas color, ensuring the interface remains "Airy" and light. 

**Gold Accents** are used sparingly as a "prestige signal" for primary calls to action, active states, and premium tier indicators. To maintain a sophisticated look, Gold should never be used for large background areas; it is reserved for highlights, thin borders, and icon details. Interactive elements utilize a subtle transition from Deep Navy to a slightly muted gold to signify selection.

## Typography

This design system employs a classic typographic contrast. **Noto Serif** provides an authoritative, literary feel for headlines, reminiscent of high-end editorial magazines. **Inter** is used for all functional and body text to ensure maximum legibility and a modern, utilitarian feel against the more decorative serif.

To enhance the "Airy" feel, utilize generous line heights and increased letter spacing for all-caps labels. Headings should be set with slight negative letter-spacing in larger sizes to maintain a tight, professional appearance. Hierarchy is primarily driven by font weight and the intentional use of Gold for small-scale emphasis.

## Layout & Spacing

The layout philosophy is based on a **Fixed Grid** model within a maximum container width of 1440px, allowing for extreme "Wide Margins" on larger displays to emphasize exclusivity. The rhythm is dictated by a strict 8px base unit, but with an emphasis on "Macro-spacing"—purposefully large gaps between sections to prevent visual clutter.

Content should feel uncrowded. Use the `section-gap` to separate distinct narrative blocks. Use the `page-margin` to ensure that even on standard desktop resolutions, the content feels framed like a piece of art rather than a dense data portal.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism and Tonal Layers** rather than traditional heavy shadows. Surfaces are categorized as "Cloud Layers":
- **Base Layer:** Solid Cloud White (#F8F9FA).
- **Floating Surfaces:** Semi-transparent white (80-90% opacity) with a 20px backdrop blur. This creates a sense of light passing through the interface.
- **Overlays:** Ultra-thin 1px borders in Deep Navy (at 10% opacity) or Gold (at 20% opacity) define edges without adding visual weight.
- **Shadows:** When necessary, use extremely diffused, low-opacity Deep Navy shadows (#002147 at 4% opacity) with a large blur radius (30px+) to suggest that elements are hovering gently above the page.

## Shapes

The shape language is "Soft-Precision." While aviation is often associated with aerodynamic curves, the luxury sector demands the stability of structured geometry. 

We use a **Soft (0.25rem)** base radius for standard components like input fields and small cards to maintain a crisp, clean-lined appearance. Large containers or image blocks may use **Rounded-LG (0.5rem)** to subtly soften the overall aesthetic. Sharp corners should be avoided as they feel too aggressive for a calm, high-end experience.

## Components

- **Buttons:** Primary buttons use a solid Deep Navy background with Cloud White text, or a Ghost style with a 1px Gold border. All buttons use a subtle hover state where the background opacity shifts or the gold border glows slightly.
- **Input Fields:** Minimalist design with only a bottom border (1px) in a light grey, transitioning to Gold on focus. Labels are always in `label-caps`.
- **Cards:** Use the glassmorphism approach—semi-transparent white backgrounds with a subtle backdrop blur and a 1px Cloud White border for a "frosted" effect.
- **Icons:** Use ultra-thin (1pt or 1.5pt) vector icons. Avoid solid fills; use "Long-line" icon styles where the lines are open and airy.
- **Status Indicators:** Use Gold for "Confirmed" or "Active" and Deep Navy for "Pending."
- **Flight Trackers:** Custom component featuring a thin Gold line representing the flight path, with frosted glass tooltips for aircraft data.
- **Imagery Containers:** Images should always occupy large ratios of the screen, often serving as the background for the frosted glass components.