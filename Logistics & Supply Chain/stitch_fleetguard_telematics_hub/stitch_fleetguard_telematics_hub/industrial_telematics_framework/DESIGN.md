---
name: Industrial Telematics Framework
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#e3bfb1'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#aa8a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb595'
  primary: '#ffb595'
  on-primary: '#571e00'
  primary-container: '#ff6700'
  on-primary-container: '#561e00'
  inverse-primary: '#a23f00'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c9c6c5'
  on-tertiary: '#313030'
  tertiary-container: '#999797'
  on-tertiary-container: '#303030'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcd'
  primary-fixed-dim: '#ffb595'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7c2e00'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  data-display:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  touch-target-min: 48px
  gutter: 1.5rem
  margin: 2rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2rem
---

## Brand & Style

The brand personality of the design system is unyielding, utilitarian, and high-performance. It is designed for the heavy trucking industry, where clarity and reliability are paramount. The visual language evokes the physical controls of heavy machinery—built to withstand vibrations, low-light conditions, and high-pressure environments.

The chosen style is a hybrid of **Brutalism** and **Tactile Modernism**. It prioritizes function over form, utilizing heavy strokes, high-contrast interfaces, and large interactive surfaces. The UI should feel "bolted down," using structural lines and "machined" edges to create a sense of physical presence and professional-grade reliability. This design system ensures that drivers and fleet managers can interpret complex telematics data at a glance, regardless of environmental factors.

## Colors

This design system utilizes a high-contrast palette optimized for visibility in truck cabs and industrial settings. The default state is **Dark Mode** to minimize driver eye fatigue and glare during night shifts.

*   **Safety Orange (#FF6700):** Reserved for primary actions, critical alerts, and branding highlights. It acts as the "ignition" color.
*   **Deep Black (#0A0A0A):** The foundation of the interface, providing a non-reflective background that makes data points pop.
*   **Industrial Silver (#C0C0C0):** Used for structural elements, iconography, and secondary text, mimicking the look of brushed aluminum and steel.
*   **Neutral Layers:** Variations of dark grays are used to create depth without sacrificing the "blacked-out" aesthetic.

## Typography

Typography in this design system is engineered for maximum legibility at a distance. We use **Inter** for its neutral, technical clarity and exceptional readability in high-contrast scenarios.

Headlines and data points use extra-bold weights to mimic stamped serial numbers and industrial signage. Data-heavy displays (like speed, fuel, or engine hours) utilize the `data-display` style, which features increased letter spacing and a heavy weight to ensure clarity even when the screen is vibrating or in motion. All labels for controls should be uppercase to reinforce the mechanical aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model designed to adapt from handheld rugged tablets to large integrated dashboard units.

A 12-column grid is used for desktop views, collapsing to 4 columns on mobile/handheld devices. Gutters are intentionally wide (24px) to create clear visual separation between data modules, preventing accidental taps. Accessibility is a priority: all interactive elements must respect a minimum touch target of 48px. Layouts should favor a "modular" approach, where each metric or control lives within its own clearly defined container, evoking the look of a physical dashboard instrument cluster.

## Elevation & Depth

Depth in this design system is conveyed through **machined layers** and **hard borders** rather than soft ambient shadows. 

We use a "Tonal Stacking" approach:
1.  **Base Level:** Deep Black (#0A0A0A) for the background.
2.  **Raised Level:** Industrial Silver or Dark Gray surfaces with 2px solid borders to simulate beveled edges of metal plates.
3.  **Active Level:** Safety Orange strokes are used to "illuminate" active states, much like a backlit physical button.

Shadows, when used, are hard-edged and high-opacity (Brutalist style) to maintain the rugged aesthetic. Backdrop blurs are avoided to keep the interface feeling grounded and opaque.

## Shapes

The shape language of the design system is **Soft-Industrial**. We use a 4px (0.25rem) corner radius for most components. This subtle rounding mimics the look of stamped metal or injection-molded industrial plastics—strong and durable, but not sharp to the touch. 

Larger containers may use the `rounded-lg` (8px) setting for visual hierarchy, but the overall aesthetic should remain blocky and structural. Pill-shapes and perfect circles are reserved strictly for status indicators or specific toggle icons, ensuring they stand out against the predominantly rectangular architecture.

## Components

Components in this design system are built for durability and ease of use in high-stakes environments.

*   **Buttons:** High-contrast blocks with 2px borders. Primary buttons use a solid Safety Orange fill with Black text. Secondary buttons use Silver borders with no fill. On "press," the button should shift 2px down and right to simulate a physical mechanical click.
*   **Data Cards:** Heavy-duty containers with a header "riveted" to the top (marked by a different background shade). Information is presented in large, bold typography.
*   **Inputs:** Fields are framed by thick borders. When focused, the border weight increases and changes to Safety Orange.
*   **Gauges & Progress:** Linear indicators are preferred over circular ones to maximize space efficiency. Progress bars should have a segmented look, mimicking LED bars on physical hardware.
*   **Chips/Status:** High-visibility tags with uppercase text. Use the status color palette (Success, Error, Warning) with high-saturation backgrounds for instant recognition.
*   **Navigation:** Large, side-aligned rail navigation is recommended for driver accessibility, ensuring the most used tools are always within reach of the thumb.