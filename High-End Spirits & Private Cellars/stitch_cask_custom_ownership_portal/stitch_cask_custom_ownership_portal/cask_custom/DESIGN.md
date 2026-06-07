---
name: Cask-Custom
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
  on-surface-variant: '#d5c3b6'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#9e8e82'
  outline-variant: '#51443a'
  surface-tint: '#f9ba82'
  primary: '#f9ba82'
  on-primary: '#4c2700'
  primary-container: '#8b5a2b'
  on-primary-container: '#ffddc2'
  inverse-primary: '#835425'
  secondary: '#e9bf8e'
  on-secondary: '#442b07'
  secondary-container: '#5e411b'
  on-secondary-container: '#d7ae7e'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#656565'
  on-tertiary-container: '#e5e3e2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdcc1'
  primary-fixed-dim: '#f9ba82'
  on-primary-fixed: '#2e1500'
  on-primary-fixed-variant: '#683d0f'
  secondary-fixed: '#ffddb7'
  secondary-fixed-dim: '#e9bf8e'
  on-secondary-fixed: '#2a1700'
  on-secondary-fixed-variant: '#5e411b'
  tertiary-fixed: '#e4e2e2'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  headline-xl:
    fontFamily: IBM Plex Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: IBM Plex Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  headline-md:
    fontFamily: IBM Plex Serif
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin: 40px
  container-max: 1280px
---

## Brand & Style

The design system is anchored in an "Industrial-Luxe" aesthetic, merging the raw, unyielding nature of a distillery floor with the refined exclusivity of a private club. It targets a discerning audience that values craftsmanship, heritage, and the tactile nature of bespoke production. 

The visual style is **Tactile and High-Contrast**. It rejects the softness of modern consumer web design in favor of sharp edges, heavy textures, and physical metaphors. The UI should feel like it was machined from steel and carved from oak. Key visual drivers include brushed metal surfaces, wood grain overlays, and structural elements reminiscent of technical blueprints and barrel hoops.

## Colors

The design system utilizes a dark-mode-first palette to evoke the dim, controlled environment of a rickhouse. 

- **Primary & Secondary (Oak Tones):** Used for call-to-action elements, accent borders, and highlighting premium barrel data. These warm tones provide a necessary "organic" contrast to the cold industrial backdrop.
- **Tertiary (Weathered Steel):** Used for structural lines, icons, and inactive states. It bridges the gap between the matte black and the wood accents.
- **Neutral (Matte Black):** The foundation. It provides a deep, non-reflective surface that allows high-contrast typography and textures to pop.

Surface colors should prioritize #1A1A1A for the base background, with subtle shifts to #222222 for container differentiation.

## Typography

Typography in this design system is a study in contrast between heritage and technical precision.

- **Headlines:** Use **IBM Plex Serif**. Its sturdy, slab-serif structure communicates authority and history. Headers should be treated like stenciled markings on a barrel—bold and uncompromising.
- **UI & Technical Elements:** Use **JetBrains Mono**. The monospaced nature reinforces the industrial, "spec-sheet" feel of a bespoke program. It should be used for all data points, labels, and navigation elements to provide a clean, engineered aesthetic.
- **Hierarchy:** Maintain high contrast in scale between headlines and body text. Use uppercase styling for labels to mimic industrial signage.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** system, emphasizing structure and architectural rigidity. 

- **Grid Model:** Use a 12-column grid for desktop views with a 24px gutter. The content is contained within a fixed width to ensure a "curated" feel, rather than stretching infinitely.
- **Spacing Rhythm:** All spacing must be multiples of 8px. Use generous margins (40px+) between major sections to allow the heavy textures and bold headers to breathe.
- **Alignment:** Every element must align to the hard vertical and horizontal axes. Avoid centered layouts unless used for singular, high-impact splash moments.

## Elevation & Depth

In this design system, depth is communicated through **Tonal Layers and Tactile Textures** rather than traditional soft shadows.

- **Etched vs. Embossed:** Instead of drop shadows, use 1px inner borders or "rim lighting" effects (1px solid lines on the top/left edges) to make elements appear machined into the surface.
- **Textural Contrast:** Use background images of brushed dark metal for primary containers and heavy oak grain for secondary sections. 
- **Industrial Dividers:** Dividers should look like physical seams. Use double-lines with 1px of "Weathered Steel" (#4A4A4A) or a subtle "rivet" pattern (small repeated dots) to separate sections.
- **Zero Shadows:** Avoid diffused blurs. If a shadow is necessary for legibility, use a hard, 100% opaque offset shadow in matte black to mimic a physical layer.

## Shapes

The shape language is strictly **Sharp (0px)**. 

Every UI component—from buttons and input fields to large cards and image containers—must feature 90-degree corners. This reinforces the "Industrial-Luxe" theme, suggesting objects that are cut, welded, or carved rather than molded. Avoid all pill shapes or rounded corners, as they conflict with the rugged, established tone of the design system.

## Components

- **Buttons:** Large, rectangular blocks. Primary buttons use a solid #8B5A2B background with black text. Secondary buttons use a #4A4A4A border with no fill, creating a "ghost" effect. 
- **Cards:** Heavy containers with a #1A1A1A background and a 1px #4A4A4A border. Include a "serial number" label in the top-right corner using the Label-SM typography to enhance the technical feel.
- **Input Fields:** Bottom-border only, or a full 1px box. Use #4A4A4A for the border. The focus state should transition the border to #C29B6D.
- **Chips/Badges:** Styled as "ID Tags" with sharp corners and monospaced text.
- **Progress Bars:** Represented as "filling barrels" or mechanical gauges. Use the Oak wood tones (#C29B6D) for active progress and Matte Black for the track.
- **Dividers:** Use thick, 2px or 4px lines that look like steel beams or copper piping, specifically at the top of sections to anchor the content.
- **Custom Scrollbars:** Styled to be thin, sharp, and colored in Weathered Steel to blend into the industrial UI.