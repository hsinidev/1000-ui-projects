---
name: Luthier-Living Design System
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
  on-surface-variant: '#d8c2be'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a08c89'
  outline-variant: '#534340'
  surface-tint: '#ffb4a6'
  primary: '#ffb4a6'
  on-primary: '#532118'
  primary-container: '#4a1a12'
  on-primary-container: '#c67e71'
  inverse-primary: '#8b4d42'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#292929'
  on-tertiary-container: '#919090'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a6'
  on-primary-fixed: '#380c06'
  on-primary-fixed-variant: '#6f362d'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-lg:
    fontFamily: Bodoni Moda
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  technical-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 24px
---

## Brand & Style

This design system establishes a visual language of "Traditional & Technical" precision. It bridges the gap between old-world craftsmanship—represented by the luthier’s workshop—and modern acoustic engineering. The brand personality is expert, artisan, and scientific, targeting an exclusive audience that values both the warmth of organic materials and the cold accuracy of high-fidelity data.

The design style is **Tactile & Modern**. It utilizes rich, realistic textures that mimic fine wood grain and brushed metallic finishes, juxtaposed against a highly structured, minimalist digital framework. This creates a "Laboratory of Luxury" aesthetic, where scientific diagrams are rendered with the same elegance as a high-end furniture catalog.

## Colors

The palette is anchored in a **Dark** mode to reflect the moody, immersive atmosphere of a dedicated listening room. 

*   **Primary (Deep Mahogany):** Used for primary surfaces and core brand elements. It evokes warmth and organic quality.
*   **Secondary (Champagne Gold):** Reserved for luxury accents, precision markers, and interactive call-to-actions. It signifies high-end hardware and "Golden Ear" status.
*   **Tertiary (Charcoal):** The technical foundation. Used for UI shells, control panels, and background layering to provide a modern, industrial contrast to the wood tones.
*   **Neutral (Rich Black):** Used for the deepest background layers to ensure the mahogany and gold elements appear to glow with a soft luminescence.

## Typography

The typographic strategy utilizes a high-contrast hierarchy to signal both heritage and innovation.

*   **Headlines:** **Bodoni Moda** provides a sophisticated, editorial feel. Its sharp serifs and dramatic stroke contrast mirror the precision of a stringed instrument.
*   **Body:** **Hanken Grotesk** offers a clean, contemporary balance that ensures long-form technical descriptions remain highly legible and professional.
*   **Technical Labels:** **JetBrains Mono** is employed for acoustic measurements, specifications, and data points. This monospaced font reinforces the scientific, laboratory-grade nature of the brand's engineering.

## Layout & Spacing

This design system employs a **Fixed Grid** on desktop to maintain an editorial, "coffee table book" feel, transitioning to a flexible fluid model for mobile devices.

*   **Desktop:** A 12-column grid with generous 64px outer margins. Content is often centered with significant whitespace to emphasize exclusivity.
*   **Technical Layouts:** Data-heavy sections (like frequency response charts) may break the grid to use the full width of the container for maximum clarity.
*   **Rhythm:** An 8px linear scale governs all padding and margins, ensuring a disciplined, engineered consistency across all components.

## Elevation & Depth

Depth is achieved through **Tonal Layering and Material Textures** rather than traditional drop shadows.

*   **Surfaces:** The base layer is the deepest Charcoal. Elevated "Container" layers use a subtle gradient mimicking the grain of Mahogany.
*   **Metallic Finishes:** Interactive elements utilize a linear gradient to simulate brushed gold or machined aluminum, creating a physical "knob and switch" feel.
*   **Glassmorphism:** Used sparingly for technical overlays. A subtle 12px backdrop blur with a 1px Gold border (0.2 opacity) simulates a glass-covered instrument gauge.
*   **Inner Glows:** Instead of outer shadows, components use subtle inner highlights on the top edge to mimic overhead studio lighting hitting a physical object.

## Shapes

The shape language is **Soft (0.25rem)**. While the brand is technical, purely sharp corners are avoided as they feel too aggressive for luxury furniture. 

*   **Primary Elements:** Standard buttons and input fields use a 4px corner radius to maintain a structural, architectural feel.
*   **Decorative Elements:** Large imagery or featured "hero" containers may use the 8px (rounded-lg) radius to soften the mahogany textures.
*   **Technical Lines:** All diagrammatic lines, dividers, and chart strokes must remain perfectly sharp (0px) to signify mathematical precision.

## Components

*   **Buttons:** Primary buttons feature a "Gold Leaf" finish—a subtle metallic gradient—with black JetBrains Mono text. Hover states should increase the "luminance" of the gold.
*   **Input Fields:** Ghost-style inputs with a Charcoal background and a 1px Mahogany border. On focus, the border transitions to Gold with a soft outer glow.
*   **Cards:** Framed with a 1px semi-transparent gold border. The background should be a dark Mahogany texture.
*   **Charts & Diagrams:** Use thin, 1px Gold lines for data paths and muted Charcoal for grid lines. Labels must be in JetBrains Mono.
*   **The "Tuning" Slider:** A custom component mimicking a high-end amplifier slider, using a brushed metallic handle and a wood-textured track.
*   **Acoustic Chips:** Small, technical tags used for specs (e.g., "15Hz - 25kHz"). These use a Charcoal fill with Gold monospaced text.