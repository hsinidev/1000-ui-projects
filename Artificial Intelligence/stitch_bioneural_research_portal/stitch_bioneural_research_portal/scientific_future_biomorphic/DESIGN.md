---
name: Scientific-Future Biomorphic
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#424752'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#727784'
  outline-variant: '#c2c6d4'
  surface-tint: '#115cb9'
  primary: '#003f87'
  on-primary: '#ffffff'
  primary-container: '#0056b3'
  on-primary-container: '#bbd0ff'
  inverse-primary: '#acc7ff'
  secondary: '#006e20'
  on-secondary: '#ffffff'
  secondary-container: '#90f691'
  on-secondary-container: '#007322'
  tertiary: '#3e4244'
  on-tertiary: '#ffffff'
  tertiary-container: '#55595c'
  on-tertiary-container: '#ccd0d3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d7e2ff'
  primary-fixed-dim: '#acc7ff'
  on-primary-fixed: '#001a40'
  on-primary-fixed-variant: '#004491'
  secondary-fixed: '#93f993'
  secondary-fixed-dim: '#77dc7a'
  on-secondary-fixed: '#002105'
  on-secondary-fixed-variant: '#005316'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c3c7ca'
  on-tertiary-fixed: '#181c1e'
  on-tertiary-fixed-variant: '#43474a'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
  mono-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.02em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  container-max: 1440px
  gutter: 20px
---

## Brand & Style

The visual identity of this design system centers on the intersection of advanced computational intelligence and biological discovery. It evokes a "Scientific-Future" atmosphere: an environment where the sterility of a high-end laboratory meets the fluidity of organic life. The target audience—biotech researchers and data scientists—requires a workspace that feels both highly technical and intuitively human.

The design style combines **Minimalism** with **Glassmorphism** and **Biomorphic UI** elements. By utilizing heavy whitespace and a restricted palette, the interface achieves a sterile, professional feel. This is softened by organic curves and translucent data overlays that mimic the appearance of microscopic views and cellular structures. The emotional response is one of precision, clarity, and breakthrough innovation.

## Colors

The palette is anchored by **Sterile White**, providing a vast, clean canvas that reflects the purity of a clinical environment. **Laboratory Blue** serves as the primary functional color, used for primary actions, navigation, and structural emphasis, conveying stability and institutional trust. 

**Mint** acts as the high-visibility accent, representing biological vitality, AI-driven insights, and positive data states. For neutral scales, use cool-toned grays to maintain the "Laboratory" aesthetic, avoiding warm browns or yellows. Backgrounds should utilize subtle gradients or 3D molecular patterns in low-contrast tints to add depth without distracting from the data.

## Typography

This design system utilizes a dual-font strategy to balance technical rigor with modern legibility. **Space Grotesk** is the primary choice for headlines and data-heavy identifiers; its geometric and slightly "tech" character reinforces the scientific-future aesthetic. 

**Inter** is used for all body text, inputs, and instructional labels. It provides the high-performance legibility required for reviewing complex pharmaceutical data. For numeric values in tables and dashboards, use Space Grotesk to ensure digits are distinct and carry a futuristic, measured feel.

## Layout & Spacing

The layout follows a **fluid grid** system within a fixed maximum width for desktop environments, ensuring that information remains legible on large research monitors. A 12-column grid is standard, but for the "Biomorphic" feel, components should often be offset or use asymmetrical padding to mimic organic growth patterns.

Spacing is based on a 4px baseline grid to allow for the high-density requirements of drug discovery tools. High-density data views should prioritize vertical compactness (8px - 12px between rows), while marketing or landing pages should lean into the "Minimalist" aesthetic with generous margins (48px+) to allow the "Sterile White" space to breathe.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and **Soft Biomorphic Shadows**. Rather than traditional heavy shadows, this design system uses translucent layers with a `backdrop-filter: blur(12px)`. This suggests a "microscope slide" effect where data overlays float above 3D molecular backgrounds.

Shadows must be extremely diffused and low-opacity, using a tint of Laboratory Blue (#0056B3) instead of pure black to maintain the sterile feel. Surfaces are tiered:
1.  **Base:** Sterile White with molecular background patterns.
2.  **Raised:** Solid white cards with soft, large-radius shadows for primary content.
3.  **Overlay:** Semi-transparent glass panels for floating widgets, tooltips, and data visualizations.

## Shapes

The "Biomorphic" nature of the design system is primarily expressed through shape. While standard containers use a **Rounded** (0.5rem) base, interactive elements and card enclosures should utilize "squircle" geometries or slightly varying radii to feel more organic. 

Avoid sharp 90-degree corners entirely. Large-scale background elements and data visualization containers should use `rounded-xl` (1.5rem) to evoke the feel of cellular membranes. Buttons should be either fully rounded (pill-shaped) or use a generous 0.75rem radius to contrast with the rigid data they contain.

## Components

**High-Density Data Tables:** 
Optimized for mobile via "Expandable Cards"—on small screens, rows transform into biomorphic cards with Laboratory Blue headers. On desktop, use zebra-striping in very faint Laboratory Blue (#0056B3 at 2% opacity) and sticky headers.

**Buttons:** 
Primary buttons are solid Laboratory Blue with pill-shaped corners. Secondary buttons use a "Ghost" style with Laboratory Blue outlines. Mint is reserved for "Action Success" or "Initiate AI Synthesis" buttons.

**Interactive Timelines:** 
Used for clinical trial stages or drug development pipelines. Use a continuous Mint-colored path with organic, circular nodes that pulse when hovered.

**Data Visualization Widgets:** 
Utilize glassmorphism for backgrounds. Charts should favor curved lines (splines) over jagged steps to maintain the biomorphic aesthetic. Use Mint for "active" data strands and Laboratory Blue for "baseline" metrics.

**Inputs & Cards:** 
Input fields use a subtle inner shadow and a Mint focus ring to signal AI-readiness. Cards should have a thin 1px border in a very light gray (#E1E4E8) to define boundaries against the Sterile White background.