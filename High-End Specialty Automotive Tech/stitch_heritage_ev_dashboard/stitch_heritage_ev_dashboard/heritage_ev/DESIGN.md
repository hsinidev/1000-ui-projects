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
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  readout-lg:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
    letterSpacing: 0.05em
  body-md:
    fontFamily: Space Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
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
  unit: 8px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  container-max: 1280px
---

## Brand & Style

The design system embodies a "Nostalgic-Modern" aesthetic, bridging the gap between the golden age of motoring and the precision of the electric future. It is tailored for high-net-worth enthusiasts who value the soul of a classic car but demand the reliability of modern engineering.

The style is **Tactile-Skeuomorphic**, utilizing high-end physical metaphors. Elements are designed to look like they were machined rather than rendered. The UI features subtle brushed metal finishes, fine-grain leather textures, and "Analog-Digital" hybrid controls. The goal is to evoke a sense of craftsmanship and permanence in a digital interface, moving away from flat design toward something that feels heavy, mechanical, and significant.

## Colors

The palette is rooted in the heritage of grand touring. 

- **Primary:** British Racing Green (#004225) serves as the anchor, used for deep backgrounds and primary brand moments.
- **Secondary:** Tan Leather (#D2B48C) provides warmth and organic contrast, primarily used for highlights, interactive states, and "upholstered" UI containers.
- **Tertiary:** Polished Chrome (#C0C0C0) is reserved for accents, borders, and tactile "hardware" elements like toggles and dials.
- **Neutrals:** The system defaults to a **Dark Mode** foundation, using a "Deep Charcoal" (#1A1A1A) for core interface surfaces to allow the Chrome and Green to feel illuminated and premium.

## Typography

This design system uses a dual-typographic approach to reflect the "Analog-Digital" narrative.

**Libre Caslon Text** is used for headings and brand moments. Its historical weight and refined serifs mimic vintage car badging and owner's manuals. High-level displays use tighter letter-spacing to feel like stamped metal plates.

**Space Grotesk** is used for all technical data, digital readouts, and body copy. Its geometric, technical nature suggests the precision of electric powertrain monitoring. For "readout" styles, increased letter-spacing is applied to simulate the look of 1980s vacuum-fluorescent displays (VFD) or modern precision instrumentation.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** on desktop to maintain a sense of structured, high-end editorial design. On mobile, it transitions to a fluid single-column layout with generous safe-area margins.

The spacing rhythm is built on an 8px base unit. To reinforce the luxury feel, the design system utilizes "Airy Precision"—large margins around structural groups, but tight, technical spacing between labels and their corresponding data values. 

- **Desktop:** 12-column grid with a 1280px max-width. 
- **Mobile:** 4-column grid with increased vertical padding to accommodate touch-friendly, "driver-centric" tap targets.

## Elevation & Depth

Hierarchy is established through **Physical Layering** rather than traditional shadows. This design system treats the screen as a mechanical assembly.

- **Base Layer:** A deep, matte "British Racing Green" or "Charcoal" finish.
- **Recessed Elements:** "Machined" wells for input fields and data displays, using inner shadows and 1px "Polished Chrome" beveled edges to look inset into the dashboard.
- **Raised Elements:** Buttons and cards use a combination of subtle top-lighting (1px highlight) and a soft ambient drop shadow to appear as if they are physical modules mounted to the surface.
- **Materials:** Use a "Fine-Grain Leather" texture overlay (low opacity) on primary containers and a "Brushed Steel" linear gradient on Chrome accents to create a tactile, non-digital appearance.

## Shapes

The shape language is **Soft-Industrial**. While modern UI often leans into extreme rounding, this design system uses a constrained 4px (Soft) radius for primary elements to mimic the precision-cut edges of automotive interior components.

- **Primary Buttons & Cards:** 0.25rem (Soft) corner radius.
- **Dials & Gauges:** Perfect circles to maintain the "Analog instrument" metaphor.
- **Separators:** 1px "Chrome" lines with a slight gradient to simulate a metallic wire or trim piece.

## Components

### Buttons
Primary buttons are styled as "Machined Toggles." They feature a subtle vertical gradient, a 1px Polished Chrome border, and use the Tan Leather color for the label to suggest a high-end tactile switch. Hover states should increase the "internal glow" of the button text.

### Readouts & Inputs
Input fields are "Recessed Slots." They appear sunken into the UI with a dark inner shadow. The text within uses the "readout-lg" style in a bright, phosphor-white or secondary tan to mimic digital telemetry.

### Cards
Cards are treated as "Modules." They use a fine-grain leather texture background with a thin metal bezel. These are used to group technical specs or car history details.

### Switches
Physical toggle switches are used instead of standard modern sliders. These should have a clear "Up/Down" or "Left/Right" mechanical state, utilizing Polished Chrome textures to look like dashboard hardware.

### Gauges
Circular components used for battery life, RPM, and speed. These utilize "Analog-Digital" styling: a physical-looking needle or ring (Chrome) paired with high-contrast digital numbering (Space Grotesk).