---
name: Nocturnal Care Aesthetic
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c8c5ce'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#919098'
  outline-variant: '#47464e'
  surface-tint: '#c3c3eb'
  primary: '#c3c3eb'
  on-primary: '#2c2d4d'
  primary-container: '#1a1b3a'
  on-primary-container: '#8383a8'
  inverse-primary: '#5b5b7e'
  secondary: '#ffb951'
  on-secondary: '#452b00'
  secondary-container: '#c2841a'
  on-secondary-container: '#3c2500'
  tertiary: '#b6c4ff'
  on-tertiary: '#1d2d61'
  tertiary-container: '#06194e'
  on-tertiary-container: '#7483bd'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c3c3eb'
  on-primary-fixed: '#171837'
  on-primary-fixed-variant: '#434465'
  secondary-fixed: '#ffddb3'
  secondary-fixed-dim: '#ffb951'
  on-secondary-fixed: '#291800'
  on-secondary-fixed-variant: '#633f00'
  tertiary-fixed: '#dce1ff'
  tertiary-fixed-dim: '#b6c4ff'
  on-tertiary-fixed: '#03164c'
  on-tertiary-fixed-variant: '#354479'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  technical-data:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
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
  gutter: 20px
  margin-safe: 24px
---

## Brand & Style

This design system is engineered for patients navigating the complexities of TMJ and Sleep Apnea—conditions often accompanied by light sensitivity and chronic discomfort. The brand personality is that of a **Clinical Specialist with a Bedside Manner**: it is deeply technical and authoritative, yet visually quiet and empathetic.

The visual style is a fusion of **Modern Corporate** reliability and **Minimalism**, optimized for "low-glare" environments. By prioritizing a dark-default interface, the design system minimizes ocular strain and provides a sanctuary for users who may be experiencing migraines or jaw tension. The aesthetic uses subtle depth and soft transitions to avoid the harshness often found in traditional medical software, ensuring the user feels cared for rather than merely processed.

## Colors

The palette is anchored in **Deep Indigo**, a color that evokes the tranquility of night and the precision of a specialist’s clinic. Unlike pure black, this base provides a softer canvas that reduces high-contrast "haloing" for sensitive eyes.

- **Primary (Deep Indigo):** Used for structural backgrounds and deep tonal layers.
- **Secondary (Soft Amber):** Reserved exclusively for high-priority actions, progress indicators, and "active" health states. Its warmth provides a clear, non-aggressive path forward.
- **Neutrals (Slate Grays):** These are tinted with a hint of blue to maintain a cohesive, cool temperature, ensuring technical data feels objective and calm.
- **Functional Gradients:** Use very shallow linear gradients (e.g., Indigo to a slightly lighter Navy) on large surfaces to prevent "flat-panel" fatigue and give the UI a tangible, high-end medical feel.

## Typography

This design system utilizes a sophisticated typographic pairing to balance authority with utility.

- **Headings (Newsreader):** The serif choice brings a "specialist" editorial feel to the system. It signals a human doctor’s presence behind the screen. It should be used for titles and empathetic check-ins.
- **Body & Interface (Inter):** A utilitarian sans-serif ensures that technical data—such as apnea-hypopnea index (AHI) or TMJ tracking—is crystal clear. The high x-height of Inter aids in legibility at smaller sizes on mobile devices.
- **Technical Readouts:** Use the 'technical-data' style for numerical values and time-stamps to distinguish raw data from instructional prose.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid** model. Content containers conform to a 12-column grid on desktop but allow for generous "safe margins" to prevent content from touching the screen edges, which can be visually jarring.

- **Rhythm:** An 8px baseline grid is used to maintain vertical rhythm. 
- **Breathing Room:** Because this design system serves patients who may be in pain, spacing is intentionally loose. Avoid "dense" layouts; use `lg` and `xl` spacing to separate major sections, allowing the user to focus on one task or piece of data at a time.
- **Gutter Strategy:** Wider gutters (20px+) are preferred to ensure that data-rich cards do not feel visually cluttered.

## Elevation & Depth

To maintain a "low-glare" environment, this design system avoids traditional high-offset dropshadows. Instead, depth is communicated through **Tonal Layering**:

1.  **Level 0 (Base):** Deep Indigo (`#1A1B3A`).
2.  **Level 1 (Cards/Surface):** A slightly lighter variant (`#1E1F26`).
3.  **Level 2 (Modals/Popovers):** A navy-gray with a subtle 1px stroke (`#4E5D94` at 20% opacity) rather than a shadow.

When depth is necessary, use **Ambient Tints**: shadows should be large and diffused with a color tint derived from the Primary Indigo, never pure black. This creates a "glow" effect rather than a harsh cutout.

## Shapes

The shape language is defined by **Softness and Organic Geometry**. Sharp corners are avoided to reinforce the empathetic and "comfortable" nature of the product.

- **Default Components:** Buttons and input fields use a `0.5rem` radius.
- **Data Cards:** Larger containers use a `1rem` (rounded-lg) radius to feel like smooth, physical medical instruments.
- **Interactive States:** Use subtle scale transforms (98%) on click rather than heavy color changes to provide tactile feedback without visual "flashing."

## Components

### Buttons
- **Primary:** Soft Amber background with Deep Indigo text. This provides the highest contrast for the main call to action.
- **Secondary:** Transparent with a 1.5px border in Primary Indigo-light.
- **Ghost:** Text-only for tertiary actions, using the Amber color for the label to maintain findability.

### Technical Data Cards
Cards should feature a header using `label-caps` for the category (e.g., "SLEEP QUALITY") and a large numeric readout in `h1`. Include a subtle sparkline or technical diagram at the bottom of the card to show trends over time.

### Progress Indicators
For self-tests (like TMJ pain assessments), use a "Soft Fill" bar. The unfilled portion should be a muted Indigo, and the filled portion a Soft Amber. Avoid pulsing animations; use a slow, steady fade for state transitions.

### Technical Diagrams
Medical illustrations or jaw alignment diagrams should use monochromatic line art in `text_secondary` with Soft Amber highlights to indicate areas of concern or focus.

### Accessible Navigation
Navigation must be high-contrast. Use a fixed bottom bar on mobile with large touch targets (minimum 48px height) to accommodate users who may have reduced dexterity during a flare-up.