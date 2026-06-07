---
name: Heritage-EV
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
  on-surface-variant: '#c0c9c0'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8a938b'
  outline-variant: '#404942'
  surface-tint: '#98d4ac'
  primary: '#98d4ac'
  on-primary: '#00391f'
  primary-container: '#004225'
  on-primary-container: '#75af89'
  inverse-primary: '#316948'
  secondary: '#e1c299'
  on-secondary: '#402d10'
  secondary-container: '#5b4526'
  on-secondary-container: '#d2b48c'
  tertiary: '#c6c6c6'
  on-tertiary: '#2f3131'
  tertiary-container: '#373939'
  on-tertiary-container: '#a2a2a2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#b4f0c7'
  primary-fixed-dim: '#98d4ac'
  on-primary-fixed: '#002110'
  on-primary-fixed-variant: '#165132'
  secondary-fixed: '#feddb3'
  secondary-fixed-dim: '#e1c299'
  on-secondary-fixed: '#281801'
  on-secondary-fixed-variant: '#584324'
  tertiary-fixed: '#e3e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 64px
    fontWeight: '600'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: EB Garamond
    fontSize: 40px
    fontWeight: '500'
    lineHeight: 48px
  headline-lg-mobile:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  headline-md:
    fontFamily: EB Garamond
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-data:
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
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
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  container-max: 1280px
---

## Brand & Style

This design system occupies the intersection of automotive history and sustainable innovation. The brand personality is **Stewardship**: a deep respect for the engineering soul of classic vehicles, enhanced by the silent power of electric propulsion. The target audience consists of discerning collectors and eco-conscious enthusiasts who value craftsmanship over convenience.

The visual style is **Tactile Luxury**. It moves beyond flat digital trends to embrace high-end physical metaphors. Inspired by the dashboard of a 1960s grand tourer, the UI features brushed metal finishes, fine-stitched leather textures, and analog-inspired components. It avoids the cold minimalism of modern tech in favor of a warm, "mechanical" digital experience that feels heavy, intentional, and permanent.

## Colors

The palette is anchored in the prestige of the racing circuit and the warmth of a bespoke interior. 

*   **Deep British Racing Green (#004225):** The primary brand signature. Used as the deep foundation for surfaces and primary brand moments.
*   **Warm Tan Leather (#D2B48C):** The secondary accent. Used for high-priority interactive elements, icons, and highlights to evoke the feel of premium upholstery.
*   **Polished Chrome (#C0C0C0):** The tertiary trim. Used for borders, dividers, and "metal" toggle states, reflecting light and providing high-end contrast.
*   **Deep Onyx (#1A1A1A):** The neutral base, providing a "chassis" for the design that ensures the green and tan elements remain the focus.

The default mode is dark to maintain the cockpit-like atmosphere and highlight the luminous quality of the data overlays.

## Typography

The typography system creates a "mechanical-luxe" contrast. **EB Garamond** provides a literary, historical weight for headings, suggesting a legacy brand. **Hanken Grotesk** serves as the primary sans-serif for descriptions and general interface text, offering a precise and modern counter-balance.

For performance data—such as voltage, range, and torque—**Space Mono** is utilized. Its fixed-width nature mimics the vintage LCD or mechanical odometer readouts found in high-end instrumentation, reinforcing the technical nature of the electrification process.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model on desktop to mirror the structured, centered nature of a car’s dashboard. The layout is built on a 12-column grid with generous margins to create a sense of exclusivity and "breathing room."

Spacing follows a strict 4px base unit, but emphasizes large internal paddings (32px+) within cards and containers to mimic the spacious feel of a luxury cabin. On mobile, the grid collapses to a single column with increased vertical rhythm, ensuring that high-resolution photography of vehicle components remains the centerpiece.

## Elevation & Depth

Depth is achieved through **Tonal Layering** and **Material Skewmorphism**. Rather than generic drop shadows, the system uses "inner glows" and "beveled edges" to make elements appear recessed into or extruded from a leather or metal surface.

*   **Surfaces:** The primary background is a deep, textured green. Overlays use a subtle grain texture to simulate leather.
*   **Shadows:** Use low-spread, high-opacity shadows tinted with the primary green (#002213) to create a "weighted" look.
*   **Glass:** Secondary data panels use a "smoked glass" effect with a Chrome border, simulating the crystal of a watch or a speedometer.

## Shapes

The shape language is **Soft (0.25rem)**. While the overall feel is high-tech, the edges are reminiscent of machined metal parts and hand-cut leather. Completely sharp corners feel too aggressive, while pill-shapes feel too "consumer tech." 

The subtle 4px radius on buttons and input fields provides a tailored, bespoke appearance. Larger containers, such as modal windows or vehicle detail cards, may use a 0.5rem (rounded-lg) radius to feel more substantial and protective.

## Components

*   **Buttons:** Primary actions are styled as "Push-buttons" with a Tan Leather fill and dark text. They feature a subtle 1px inner highlight on the top edge to simulate a physical bevel.
*   **Inputs:** Fields are recessed (inset shadow) with a Chrome-colored border that glows subtly when focused. Labels always appear in uppercase Hanken Grotesk above the field.
*   **Gauges:** Instead of standard progress bars, use circular "Analog Gauges" with Chrome needles to display battery life and power output.
*   **Cards:** Vehicle cards should feature a "stitching" border—a dashed line in a slightly lighter green—to reinforce the leather-craft aesthetic.
*   **Toggles:** Mode switches (Eco vs. Sport) are designed as physical knurled metal toggles that slide with a high-friction animation.
*   **Status Chips:** Use a Chrome-rimmed "enamel" style, with the internal color representing the status (e.g., a glowing green led-dot for 'Connected').