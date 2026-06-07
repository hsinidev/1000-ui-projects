---
name: Cyber-Liability Command
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
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c6c4df'
  on-secondary: '#2f2e43'
  secondary-container: '#47475d'
  on-secondary-container: '#b8b6d0'
  tertiary: '#fff5f0'
  on-tertiary: '#4d2600'
  tertiary-container: '#ffd2b1'
  on-tertiary-container: '#924e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e0fc'
  secondary-fixed-dim: '#c6c4df'
  on-secondary-fixed: '#1a1a2e'
  on-secondary-fixed-variant: '#45455b'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
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
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  margin: 32px
---

## Brand & Style
The design system establishes a high-authority environment tailored for enterprise security officers and risk managers. The brand personality is clinical, vigilant, and high-performance, evoking the feel of a mission-critical command center. 

The style is a sophisticated blend of **Glassmorphism** and **Corporate Modernism**. It utilizes deep layers of transparency to suggest complex data depths while maintaining structural integrity through rigid grid alignment and sharp technical details. Visual interest is driven by "active" elements featuring subtle glowing borders and high-contrast data visualizations that stand out against a matte, dark environment. The focus remains on unwavering precision and technical superiority.

## Colors
The palette is rooted in a "Deep Dark" philosophy. The foundation is **Matte Black (#0D0D0D)**, providing a void-like canvas that eliminates distractions. **Deep Indigo (#1A1A2E)** acts as the secondary surface color, used for containers and elevated panels to create subtle tonal separation.

**Neon Cyan (#00F2FF)** is the high-energy primary accent, reserved for critical interactive elements, progress indicators, and "active" states. Functional accents are strictly utility-driven: **Warning Orange** for liability gaps and risk alerts, and **Success Green** for "Protected" status and system integrity. Data visualizations should leverage the Cyan-to-Indigo gradient for depth, using the Matte Black background to ensure maximum contrast and legibility of complex metrics.

## Typography
This design system utilizes a dual-font strategy to balance editorial authority with technical clarity. **Space Grotesk** is used for headlines to provide a futuristic, geometric edge that reflects high-tech security. 

**Inter** handles all functional text, body copy, and data points. For data-heavy tables and code snippets, Inter is set with tighter tracking and medium-to-bold weights to mimic the legibility of a monospaced font while maintaining superior character balance. All labels and secondary metadata should use the `label-caps` style to create a distinct hierarchy between navigational elements and content.

## Layout & Spacing
The layout follows a **Fixed Grid** model on a 12-column system for dashboard views to ensure consistency in data visualization placement. A strict 4px base unit (the "rhythm") governs all padding and margins. 

Layouts should prioritize high information density without sacrificing clarity. Horizontal sections are separated by sharp 1px dividers rather than large gaps. Use expansive `xl` (40px) margins for external container padding to create a "framed" feel, while internal component spacing remains tight (`sm` or `md`) to maintain a technical, compact aesthetic.

## Elevation & Depth
Depth is conveyed through **Glassmorphism and Tonal Layers**. Instead of traditional drop shadows, this design system uses background blurs (12px to 20px) and semi-transparent indigo fills.

1.  **Floor:** Matte Black (#0D0D0D).
2.  **Level 1 (Cards/Panels):** Deep Indigo (#1A1A2E) at 60% opacity with a 1px border of #FFFFFF at 10% opacity.
3.  **Level 2 (Modals/Popovers):** Surface Indigo at 80% opacity with a Cyan "glow" border (1px, #00F2FF at 30% opacity).

Interactive elements in an active state should appear to "emit" light, using a soft 8px outer glow in the primary Cyan color rather than a shadow.

## Shapes
The shape language is "Soft-Tech." The standard `roundedness: 1` (4px) is applied to buttons, input fields, and small UI components to provide just enough approachability without losing the rigorous, structural feel of an enterprise tool. 

Larger containers and cards use `rounded-lg` (8px). Strict 0px corners are reserved for data bars and decorative "scanning" elements to reinforce the precision-engineering theme.

## Components
- **Buttons:** Primary buttons feature a solid Neon Cyan fill with Matte Black text. Secondary buttons are "Ghost" style with a Cyan 1px border and a subtle 4% Cyan hover fill.
- **Inputs:** Fields use a Matte Black background with a 1px Deep Indigo border. On focus, the border transitions to Neon Cyan with a subtle 2px outer glow.
- **Cards:** Defined by a 1px border and a background blur. Header areas within cards should have a subtle 5% lighter indigo tint.
- **Data Visualizations:** Charts must use high-contrast strokes. Line graphs should feature a "glow" effect on the primary data line.
- **Status Chips:** Small, rectangular indicators with 2px corner radius. They use high-saturation fills (Success Green or Warning Orange) at 20% opacity with solid text for readability.
- **Scanning/Progress Indicators:** Use thin, horizontal "laser" lines that animate vertically or horizontally across cards to indicate active data protection monitoring.