---
name: Kinetic Logic
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#454558'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#757589'
  outline-variant: '#c5c4db'
  surface-tint: '#343dff'
  primary: '#0001bb'
  on-primary: '#ffffff'
  primary-container: '#0000ff'
  on-primary-container: '#b3b7ff'
  inverse-primary: '#bec2ff'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e2'
  on-secondary-container: '#646464'
  tertiary: '#720001'
  on-tertiary: '#ffffff'
  tertiary-container: '#9d0002'
  on-tertiary-container: '#ffa598'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bec2ff'
  on-primary-fixed: '#00006e'
  on-primary-fixed-variant: '#0000ef'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#ffdad5'
  tertiary-fixed-dim: '#ffb4a9'
  on-tertiary-fixed: '#410000'
  on-tertiary-fixed-variant: '#930002'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display:
    fontFamily: Space Grotesk
    fontSize: 4.5rem
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Space Grotesk
    fontSize: 3rem
    fontWeight: '700'
    lineHeight: '1.2'
  h2:
    fontFamily: Space Grotesk
    fontSize: 2.25rem
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Space Grotesk
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 0.875rem
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 40px
---

## Brand & Style

This design system is built for the high-stakes world of commercial retail leasing, where precision and speed are paramount. The brand personality is authoritative, energetic, and unapologetically technical. It avoids the soft, muted trends of consumer apps in favor of a **High-Contrast / Bold** aesthetic that mirrors the intensity of urban commerce.

The visual language is "Data-Forward." Every element is designed to facilitate rapid scanning and decision-making. By leveraging a restricted, high-intensity color palette and a rigid structural grid, the system creates an environment of professional urgency. It evokes a sense of "Information Alpha"—giving users the feeling that they are seeing the market more clearly than their competitors.

## Colors

The palette is anchored by a triad of absolute values: Electric Blue, Pure White, and Deep Black. 

- **Primary Electric Blue (#0000FF):** Used exclusively for primary actions, active states, and critical data highlights. It is the "signal" within the noise.
- **Deep Black (#000000):** Provides the structural framework. Used for heavy typography, borders, and high-impact containers to ground the interface.
- **Pure White (#FFFFFF):** The expansive canvas that ensures the high-contrast elements remain legible and the data visualizations pop.

For data visualizations like heatmaps, use a strictly mathematical scale. Avoid muddy gradients; use stepped increments of the primary blue or high-visibility secondary signals (Neon Green/Red) to denote density and risk.

## Typography

The typographic strategy pairs technical geometric forms with utilitarian clarity. 

**Space Grotesk** is used for all headlines and numerical data callouts. Its quirky, geometric terminals reinforce the tech-forward, data-driven nature of the platform. Use heavy weights for headlines to create a strong vertical rhythm.

**Inter** is the workhorse for body copy, data tables, and interface labels. It provides maximum readability at small sizes, which is essential for complex demographic charts and leasing terms. 

Large-scale data points (like square footage or cap rates) should always be rendered in Space Grotesk with tight letter-spacing to emphasize their importance.

## Layout & Spacing

The layout utilizes a **fixed 12-column grid** for main dashboards to ensure absolute alignment of data modules. A rigid 8px base unit governs all padding and margins, creating a "locked-in" feel that suggests mathematical precision.

Modules and data cards should be packed tightly to maximize information density, using 24px gutters to prevent visual overlap. Whitespace is not used for "breathability" in the traditional sense, but rather as a functional separator to isolate distinct data sets. In report views, use generous 80px vertical spacing (xl) to separate major sections, but maintain high density within the sections themselves.

## Elevation & Depth

This design system eschews soft shadows and organic depth. Instead, it uses **Bold Borders** and **Tonal Layers** to establish hierarchy.

1.  **Level 0 (Background):** Pure White (#FFFFFF).
2.  **Level 1 (Cards/Modules):** White surface with a 1px or 2px solid Black (#000000) border.
3.  **Level 2 (Active/Hover):** Electric Blue (#0000FF) border or a subtle light-gray offset fill.
4.  **Inversion:** High-priority modules may use a solid Black background with White or Electric Blue text to create an immediate focal point.

Depth is communicated through "stacking" rather than "floating." When a modal appears, it does not have a diffused shadow; it has a thick, solid black border and a high-contrast backdrop overlay.

## Shapes

The shape language is strictly **Sharp (0)**. Every button, card, input field, and data container utilizes 90-degree angles. This rejection of rounded corners aligns with the "clean lines" and "professional" requirements, giving the UI a structural, architectural feel reminiscent of floor plans and urban grids.

Interior elements like progress bars or heatmap cells must also remain perfectly rectangular. The only exception to the "sharp" rule is circular icons when used within map markers to denote specific points of interest, though even these should be encased in square tooltips.

## Components

- **Buttons:** Primary buttons are solid Electric Blue with White text, using all-caps labels for a commanding presence. Secondary buttons use a heavy 2px Black border with no fill.
- **Inputs:** Text fields are defined by a bottom-border only (2px Black) until focused, at which point they transition to a full 2px Electric Blue box.
- **Data Tables:** Use "Zebra-striping" with extremely light grays, but maintain heavy Black headers. Cell borders should be minimal to let the data lead.
- **Chips/Tags:** Used for property status (e.g., "AVAILABLE," "UNDER CONTRACT"). These are small, sharp-edged boxes with solid fills and high-contrast text.
- **Heatmaps:** Use a monochromatic Electric Blue scale for density. For demographic "hotspots," use high-saturation Yellow (#FFFF00) to cut through the blue/black theme.
- **Cards:** Dashboard cards must have a header section separated by a 1px horizontal rule. No shadows allowed.
- **Navigation:** A persistent sidebar in Deep Black with Electric Blue active-state indicators provides a "command center" feel.