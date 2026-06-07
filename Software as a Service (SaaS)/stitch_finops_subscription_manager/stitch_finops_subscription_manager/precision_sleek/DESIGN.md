---
name: Precision-Sleek
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c7'
  on-tertiary: '#303031'
  tertiary-container: '#19191a'
  on-tertiary-container: '#838183'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e3'
  tertiary-fixed-dim: '#c8c6c7'
  on-tertiary-fixed: '#1b1b1c'
  on-tertiary-fixed-variant: '#474647'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-main:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-max: 1440px
  gutter: 24px
---

## Brand & Style

The design system is engineered for high-stakes financial environments where clarity, speed, and trust are paramount. It targets CFOs, FinOps leads, and engineering teams who require a reliable lens into complex billing data. 

The visual direction merges **Minimalism** with high-performance **Glassmorphism**. The aesthetic is dark-mode first, utilizing semi-transparent surfaces to create a sense of depth without clutter. The experience is defined by "Financial Precision"—meaning every pixel, border, and data point is rendered with absolute sharpness. Subtle glows and high-contrast silver borders guide the user's eye to critical metrics, evoking the feel of a premium, high-tech command center.

## Colors

This design system utilizes a sophisticated dark palette designed to reduce eye strain during long analytical sessions. 

- **Deep Navy (#0A192F):** Used for the primary background and structural depth. It provides a more expansive feel than pure black.
- **Matte Black (#1A1A1B):** Used for elevated surfaces, sidebars, and input containers to create internal contrast.
- **Silver (#C0C0C0):** The primary color for borders, secondary text, and iconography. It provides the "high-contrast" metallic edge required for precision.
- **Accent Glow:** A subtle cyan-tinted glow is used sparingly to highlight active states or positive financial trends.
- **Functional Colors:** Success and danger states use high-vibrancy tones to remain legible against the dark backgrounds.

## Typography

The design system relies on **Inter** for its utilitarian, systematic feel and excellent legibility in data-heavy interfaces. 

- **Numerical Precision:** When displaying currency and metrics, always use `font-variant-numeric: tabular-nums` to ensure columns of figures align perfectly.
- **Contrast:** Headlines should use the Silver (#C0C0C0) palette to stand out against the Deep Navy background, while body text uses a slightly desaturated silver to maintain hierarchy.
- **Hierarchy:** Use all-caps labels for metadata and section headers to create a "technical document" aesthetic.

## Layout & Spacing

The design system employs a **Fixed Grid** approach for the main dashboard to ensure data visualizations remain predictable across different screen sizes. 

- **Grid Model:** A 12-column grid with 24px gutters.
- **Rhythm:** A strict 4px baseline grid ensures vertical alignment of data rows and labels.
- **Density:** The layout favors "Comfortable Density." While data-rich, it uses generous outer margins (40px+) to frame the "Hub" and prevent a claustrophobic feel.
- **Information Grouping:** Use white space rather than lines to separate logic blocks, reserving borders only for primary card containers.

## Elevation & Depth

Depth in this design system is achieved through **Glassmorphism** and high-contrast strokes rather than traditional shadows.

- **The Glass Effect:** Cards use a semi-transparent fill of Matte Black (#1A1A1B) at 60-80% opacity with a `backdrop-filter: blur(12px)`.
- **Primary Stroke:** Every card must have a 1px solid border using Silver (#C0C0C0) at 20% opacity. For active or focused states, increase this opacity to 50% and add a subtle outer glow.
- **Layering:** 
    1. **Level 0 (Base):** Deep Navy (#0A192F).
    2. **Level 1 (Cards):** Glassmorphic Matte Black.
    3. **Level 2 (Modals/Popovers):** Solid Matte Black with a 1px Silver border at 80% opacity.

## Shapes

To reinforce the feeling of precision and institutional trust, this design system uses **Sharp (0px)** corners for all primary containers, cards, and input fields. 

The absence of rounded corners signals a technical, "no-fluff" environment. Small exceptions can be made for interior elements like toggle switches or status indicators (dots), but all structural UI components must remain strictly rectangular to maintain the high-contrast, architectural aesthetic.

## Components

### Buttons
- **Primary:** Solid Silver (#C0C0C0) with Matte Black text. No rounding.
- **Secondary:** Ghost style with a 1px Silver border and Silver text. On hover, apply a subtle glow effect (`box-shadow: 0 0 10px rgba(192, 192, 192, 0.3)`).

### Cards
- Always glassmorphic. 
- Headers within cards should have a subtle bottom border (1px, Silver, 10% opacity) to separate titles from content.

### Input Fields
- Background: Matte Black (#1A1A1B).
- Border: 1px Silver (#C0C0C0) at 20% opacity.
- Focus State: Border opacity increases to 100%, and the text cursor should be the accent color.

### Data Visualizations
- **Charts:** Use thin 1.5px lines for line charts. 
- **Gradients:** Area charts should use a vertical gradient from Silver (20% opacity) to Transparent.
- **Grid Lines:** Use the Deep Navy background color, but slightly lighter, for grid lines to keep them secondary to the data.

### Chips & Status
- Use sharp-edged boxes with a background tint of the status color (e.g., 10% Green for 'Paid') and a solid 1px border of that same color. Text should be uppercase and 10px - 12px.

### Additional Components
- **Metric Tiles:** Large-format numbers with a small trend indicator (sparkline) integrated into the background.
- **Timeline Stepper:** For subscription lifecycles, using vertical silver lines and sharp square nodes.