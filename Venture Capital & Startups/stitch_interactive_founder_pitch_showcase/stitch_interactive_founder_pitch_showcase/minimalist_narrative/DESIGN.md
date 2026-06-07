---
name: Minimalist Narrative
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
  on-surface-variant: '#434656'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004ced'
  primary: '#003ec7'
  on-primary: '#ffffff'
  primary-container: '#0052ff'
  on-primary-container: '#dfe3ff'
  inverse-primary: '#b7c4ff'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#4c4e4f'
  on-tertiary: '#ffffff'
  tertiary-container: '#656666'
  on-tertiary-container: '#e4e5e5'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b7c4ff'
  on-primary-fixed: '#001452'
  on-primary-fixed-variant: '#0038b6'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-hero:
    fontFamily: Manrope
    fontSize: 4.5rem
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Manrope
    fontSize: 2.5rem
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 1.75rem
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-lg:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: -0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  container-max: 1280px
  gutter: 1.5rem
  margin-mobile: 1.25rem
  stack-sm: 0.5rem
  stack-md: 1.5rem
  stack-lg: 4rem
  section-padding: 8rem
---

## Brand & Style
The design system is engineered for high-stakes storytelling where clarity is the ultimate form of sophistication. It adopts a **Minimalist-Narrative** aesthetic, stripping away superfluous decoration to ensure the narrative arc of a pitch remains the focal point. The personality is authoritative yet visionary—balancing the editorial weight of a premium magazine with the functional precision of a financial dashboard.

The style leverages **High-Contrast Minimalism**, utilizing expansive whitespace to create a sense of breathing room and intellectual "calm." Impact is achieved through scale and rhythm rather than ornamentation. Every element serves a structural purpose, using crisp borders and a restricted palette to establish a professional, high-fidelity environment that inspires confidence in investors and stakeholders.

## Colors
The palette is hyper-focused to eliminate cognitive load and drive action. 

*   **Pure White (#FFFFFF)**: The foundation. It acts as the canvas, providing the "generous whitespace" essential for a modern, high-fidelity feel.
*   **Charcoal (#1A1A1A)**: The anchor. Used for primary typography and structural elements to ensure maximum legibility and a sense of permanence.
*   **Electric Blue (#0052FF)**: The catalyst. This high-vibrancy blue is reserved strictly for primary interactive triggers, call-to-actions, and critical data highlights. 
*   **Functional Greys**: A subtle range of greys is used for borders and secondary text to maintain hierarchy without breaking the high-contrast tension between the Charcoal and White.

## Typography
This design system utilizes a dual-font strategy to separate narrative from utility. 

**Manrope** is used for headlines to provide a refined, contemporary character. Large-scale hero text uses tight letter-spacing and heavy weights to create "narrative impact," turning short phrases into visual anchors.

**Inter** is employed for body copy, UI elements, and data visualization. Its systematic, neutral design ensures high readability at small sizes, particularly on mobile screens. For data points, high-contrast weights (Bold/Extra Bold) are used to make metrics pop against the minimalist background, ensuring that even complex charts remain accessible at a glance.

## Layout & Spacing
The layout follows a **Fluid Grid** model with a strict adherence to a 12-column system for desktop and a 4-column system for mobile. 

*   **Rhythm**: A 4px baseline grid ensures vertical consistency. 
*   **Whitespace**: Large `section-padding` values are used to isolate narrative beats, preventing the deck from feeling cluttered.
*   **Mobile Optimization**: On 6-inch screens, the layout shifts to a single-column stack. Margins are reduced to `1.25rem` to maximize screen real estate for data visualization, while "hit areas" for interactive elements are maintained at a minimum of 44px to ensure ease of use.

## Elevation & Depth
This design system rejects heavy shadows in favor of **Low-Contrast Outlines and Structural Layers**. Depth is communicated through:

1.  **Crisp Borders**: 1px solid lines using a light grey (#E5E5E5) or Charcoal (#1A1A1A) define the boundaries of content blocks and interactive cards.
2.  **Tonal Differentiation**: Subtle shifts from White (#FFFFFF) to a very light Off-White (#F5F5F5) are used to distinguish background sections from foreground components.
3.  **Active Elevation**: Only upon interaction (e.g., hovering over a chart or card) does a subtle, highly diffused "Ambient Shadow" appear to indicate focus. This keeps the interface feeling flat, fast, and high-fidelity until utility demands otherwise.

## Shapes
The shape language is primarily **Geometric and Disciplined**. A "Soft" roundedness (`0.25rem`) is applied to buttons, input fields, and small UI components to prevent the interface from feeling aggressive while maintaining its professional edge. 

Larger containers and section breaks utilize sharp corners to reinforce the grid-based, architectural feel of the pitch deck. Interactive "chips" or status indicators may use a fully rounded "pill" shape to distinguish them from structural elements.

## Components
Consistent component behavior is vital for a high-fidelity digital deck:

*   **Buttons**: Primary buttons are solid Electric Blue with White text. Secondary buttons use Charcoal outlines with a 1px weight. The hit area is strictly enforced for mobile accessibility.
*   **Interactive Cards**: Used for feature highlights or data deep-dives. These feature a 1px #E5E5E5 border and use generous internal padding (`stack-md`).
*   **Data Visualizations**: Charts use Electric Blue for the primary data series and Charcoal for axes and labels. Lines are crisp (2px stroke) and avoid fills unless using a very low-opacity Electric Blue tint.
*   **Progress Indicators**: A slim, 2px horizontal bar at the top of the viewport in Electric Blue tracks the user's journey through the narrative.
*   **Input Fields**: Minimalist 1px bottom-border only (underline style) for a "form-less" feel, turning Electric Blue on focus.
*   **Navigation**: A persistent, compact bottom bar for mobile devices provides quick access to "Next Slide" and "Appendix" triggers.