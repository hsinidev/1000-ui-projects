---
name: Alpine Fresh Luxury UI
colors:
  surface: '#f4fafd'
  surface-dim: '#d4dbdd'
  surface-bright: '#f4fafd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eef5f7'
  surface-container: '#e8eff1'
  surface-container-high: '#e2e9ec'
  surface-container-highest: '#dde4e6'
  on-surface: '#161d1f'
  on-surface-variant: '#41484d'
  inverse-surface: '#2b3234'
  inverse-on-surface: '#ebf2f4'
  outline: '#71787e'
  outline-variant: '#c1c7ce'
  surface-tint: '#2e6385'
  primary: '#2e6385'
  on-primary: '#ffffff'
  primary-container: '#a5d8ff'
  on-primary-container: '#285f80'
  inverse-primary: '#9accf3'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#d1d2d2'
  on-tertiary-container: '#585a5a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#9accf3'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#0c4b6c'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f4fafd'
  on-background: '#161d1f'
  surface-variant: '#dde4e6'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
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
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system is engineered to evoke the serene, high-altitude atmosphere of a premium mountain retreat. The brand personality is exclusive, crystalline, and majestic, targeting a discerning audience that values both technical precision and aesthetic tranquility. 

The visual direction combines **Minimalism** and **Glassmorphism**. By prioritizing generous whitespace and translucent layering, the interface mimics the optical qualities of ice and frosted glass. The goal is to create an emotional response of "breathability"—giving the user the same sense of clarity one feels when breathing in crisp mountain air. Every interaction should feel effortless and lightweight, avoiding heavy blocks of color in favor of light-refracting surfaces and ethereal depth.

## Colors

The palette for this design system is rooted in the "Alpine-Fresh" concept, utilizing a high-key light mode to maximize luminosity.

*   **Primary (Ice Blue):** Used for interactive elements, highlights, and subtle brand accents. It represents the sky and glacial ice.
*   **Secondary (Silver):** Applied to sophisticated gradients, borders, and secondary icons to provide a metallic, premium finish.
*   **Tertiary (Crisp White):** The foundation of the system, used for backgrounds and surfaces to create a "fresh snow" effect.
*   **Neutral (Deep Slate):** A high-contrast dark tone reserved strictly for typography and essential iconography to ensure AAA accessibility against white and light blue backgrounds.
*   **Status Indicators:** Instead of aggressive reds or greens, "Open" is represented by a vibrant Sky Blue, and "Closed" by a muted, frosted Silver, maintaining the palette’s harmony.

## Typography

This design system utilizes **Inter** for all levels of the hierarchy to ensure a modern, utilitarian, yet premium feel. The typographic rhythm relies on high contrast between sizes and generous line heights to preserve the "airy" aesthetic.

Headlines use a tighter letter-spacing and heavier weights to anchor the page, while body text is set with ample leading to improve readability against translucent backgrounds. A specialized `label-caps` style is used for technical data, such as altitude or weather metrics, providing a professional, "instrument-panel" feel common in high-end outdoor gear.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model with an emphasis on "Negative Space Luxury." The system utilizes a 12-column grid for desktop, but the defining characteristic is the oversized outer margins (xl) and internal gutters (md).

Spacing is governed by an 8px rhythmic scale. Components should never feel crowded; if in doubt, increase padding to the next scale increment. This "generous whitespace" is critical to evoking the feeling of a vast mountain landscape. Use the `xl` spacing unit to separate major sections, ensuring each piece of content feels like a distinct "peak" in the visual journey.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** rather than traditional heavy shadows. 

1.  **Backdrop Blurs:** Surfaces should use a 20px to 30px Gaussian blur on the background layer, combined with a 60% opacity white fill.
2.  **Frosted Borders:** Elements are defined by a 1px inner border (stroke) using a linear gradient of White to Silver at 30% opacity. This creates a "glint" effect similar to the edge of an icicle.
3.  **Shadows:** Shadows must be extremely subtle and "cool-tinted." Use a low-opacity Ice Blue (#A5D8FF) for shadow colors instead of pure black to maintain the frozen, ethereal quality.
4.  **Layering:** High-priority cards (like booking engines) sit on the highest "elevation," featuring the most pronounced blur and a slightly more opaque white background.

## Shapes

The shape language of this design system is **Rounded**, balancing the harshness of mountain peaks with the softness of fresh powder.

*   **Standard Components:** Buttons and input fields use a 0.5rem (8px) radius.
*   **Cards and Containers:** Larger surfaces use `rounded-lg` (1rem) or `rounded-xl` (1.5rem) to feel approachable and modern.
*   **Interactive Accents:** Small chips and status indicators use full pill-shaping (100px radius) to distinguish them from structural content.

## Components

### Buttons
Primary buttons feature a sophisticated Silver-to-White linear gradient (45-degree angle) with a subtle Ice Blue glow on hover. Typography inside buttons should be `body-md` with semi-bold weighting. Secondary buttons use a "Ghost" style with a 1px silver border and glassmorphic background.

### Piste Status Indicators
Refined status indicators are pill-shaped. "Open" uses a soft light blue background with dark blue text; "Closed" uses a frosted silver background with slate text. These are accompanied by thin, minimalist icons (e.g., a simple line-art lift or snowflake).

### Glassmorphic Cards
Cards are the primary content container. They must feature the 20px backdrop blur and the 1px frosted border mentioned in the Elevation section. Card headers should use `headline-md` for clear section identification.

### Input Fields
Inputs are minimalist: a simple bottom-border in Silver that transitions to Ice Blue when focused. The background of the input area is a very faint 10% opacity Ice Blue to provide a "cool" touch target.

### Luxury Imagery
All photography should be high-contrast with a cool temperature bias, emphasizing textures of snow, wood, and metal. Images should be housed in containers with the standard `rounded-lg` radius to maintain consistency.