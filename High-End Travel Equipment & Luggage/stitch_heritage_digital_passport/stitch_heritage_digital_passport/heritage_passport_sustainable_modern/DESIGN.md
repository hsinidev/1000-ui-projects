---
name: Heritage-Passport Sustainable-Modern
colors:
  surface: '#fff8f5'
  surface-dim: '#e1d8d4'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2ed'
  surface-container: '#f5ece7'
  surface-container-high: '#efe6e2'
  surface-container-highest: '#e9e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#434843'
  inverse-surface: '#34302c'
  inverse-on-surface: '#f8efea'
  outline: '#737973'
  outline-variant: '#c3c8c1'
  surface-tint: '#4d6453'
  primary: '#061b0e'
  on-primary: '#ffffff'
  primary-container: '#1b3022'
  on-primary-container: '#819986'
  inverse-primary: '#b4cdb8'
  secondary: '#675d4e'
  on-secondary: '#ffffff'
  secondary-container: '#efe0cd'
  on-secondary-container: '#6d6354'
  tertiary: '#281200'
  on-tertiary: '#ffffff'
  tertiary-container: '#462300'
  on-tertiary-container: '#cb8341'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d0e9d4'
  primary-fixed-dim: '#b4cdb8'
  on-primary-fixed: '#0b2013'
  on-primary-fixed-variant: '#364c3c'
  secondary-fixed: '#efe0cd'
  secondary-fixed-dim: '#d2c4b2'
  on-secondary-fixed: '#221a0f'
  on-secondary-fixed-variant: '#4f4538'
  tertiary-fixed: '#ffdcc2'
  tertiary-fixed-dim: '#ffb77b'
  on-tertiary-fixed: '#2e1500'
  on-tertiary-fixed-variant: '#6d3a00'
  background: '#fff8f5'
  on-background: '#1e1b18'
  surface-variant: '#e9e1dc'
typography:
  display-lg:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-lg-mobile:
    fontFamily: Libre Caslon Text
    fontSize: 28px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '400'
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
  label-sm:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
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
  container-max: 1280px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
---

## Brand & Style

The design system establishes a bridge between ancestral legacy and future-proof technology. It targets high-net-worth individuals and conscious collectors who value provenance, environmental stewardship, and digital permanence. The emotional response is one of "Quiet Authority"—a blend of the security found in a physical vault and the efficiency of a high-end digital interface.

The design style is **Tactile Minimalism**. It rejects the coldness of traditional tech by incorporating organic, paper-like textures and a warm, earthy palette, while maintaining modern rigor through precise grid systems and generous whitespace. Every interaction should feel intentional, mimicking the weighted experience of handling a physical passport or an archival document.

## Colors

The palette is rooted in the natural world, emphasizing longevity and value.

- **Deep Forest Green (#1B3022):** Used for primary typography, headers, and structural elements. It provides the "Heritage" weight.
- **Warm Sand (#F5E6D3):** The foundational surface color. It creates a soft, eye-strained-free environment that feels more like parchment than a screen.
- **Metallic Copper (#B87333):** Reserved exclusively for interactive highlights, verification states, and premium details. It represents the "conductive" element of the blockchain and the "preciousness" of the assets.
- **Background Paper (#FDF9F3):** A lighter tint of sand used for card surfaces to create subtle contrast against the primary page background.

## Typography

The typography strategy pairs the historical gravitas of **Libre Caslon Text** with the surgical precision of **Hanken Grotesk**. 

- **Headings:** Use Libre Caslon Text for all editorial titles and section headers. The slight imperfections in the serif shapes evoke traditional printing presses.
- **Body:** Hanken Grotesk provides high readability for complex data and asset descriptions. It should be set with generous line heights to maintain the "Modern" half of the design system.
- **Labels:** Small caps and increased letter spacing are used for metadata, blockchain hashes, and secondary navigation to differentiate technical data from narrative content.

## Layout & Spacing

This design system utilizes a **Fixed Grid** approach for desktop to mirror the layout of a physical ledger or luxury magazine. 

- **Grid:** A 12-column grid with a 1280px maximum width. On mobile, this collapses to a single-column layout with 20px side margins.
- **Rhythm:** Spacing follows an 8px incremental scale. Large sections should be separated by at least 80px (10 units) to provide the "Generous Whitespace" required for a premium feel.
- **Composition:** Asymmetric layouts are encouraged for gallery views, while data-heavy blockchain views must adhere strictly to the grid for clarity.

## Elevation & Depth

Depth is achieved through physical metaphors rather than digital glows.

- **Surface Layers:** Use very subtle "Paper" textures (fine-grain noise at 2-3% opacity) on all main surfaces.
- **Shadows:** Avoid heavy black shadows. Instead, use soft, diffused "Ambient Shadows" tinted with Deep Forest Green (e.g., `rgba(27, 48, 34, 0.08)`). Shadows should appear as if the element is resting just millimeters above a textured paper surface.
- **Interactive Depth:** When a card is hovered, the shadow should slightly expand, and a 1px Metallic Copper internal border may appear to "illuminate" the element.

## Shapes

The shape language is primarily **Soft (0.25rem)**. This mimics the slightly rounded corners of hand-cut high-quality cardstock. 

- **Large Components:** Cards and main containers use `rounded-lg` (0.5rem) to feel approachable but structured.
- **Interactive Elements:** Buttons and input fields use the base `rounded` (0.25rem). 
- **Icons:** Use geometric, thin-stroke icons with slightly blunted terminals to match the Hanken Grotesk typeface.

## Components

- **Premium Cards:** Set on `background_paper_hex` with a 1px border of `#E5D6C3`. Content should have internal padding of at least 32px.
- **Blockchain Verification Badges:** Circular or hex-shaped emblems using a Metallic Copper stroke. When "Verified," the badge utilizes a subtle copper shimmer gradient.
- **Lifecycle-Chain Timeline:** A vertical or horizontal 1px Deep Forest Green line connecting nodes. Completed nodes are solid Copper; pending nodes are outlined Green. Each node, when clicked, reveals a "Certificate of Authenticity" layout.
- **Buttons:**
    - *Primary:* Deep Forest Green background with Warm Sand text. No hover color change; instead, a subtle shift in shadow depth.
    - *Secondary:* Transparent with a 1px Metallic Copper border and Copper text.
- **Input Fields:** Minimalist underlines or 1px strokes. Focus states swap the stroke color to Metallic Copper and introduce a very faint Copper tint to the field background.
- **Lifecycle Nodes:** These represent the asset's journey. Each node must include a timestamp in `label-sm` and a brief description in `body-md`.