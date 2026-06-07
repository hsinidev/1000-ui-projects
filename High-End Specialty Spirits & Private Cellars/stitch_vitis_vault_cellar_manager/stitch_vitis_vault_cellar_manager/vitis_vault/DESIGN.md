---
name: Vitis-Vault
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#554240'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#89726f'
  outline-variant: '#dcc0bd'
  surface-tint: '#9d4139'
  primary: '#210000'
  on-primary: '#ffffff'
  primary-container: '#4a0404'
  on-primary-container: '#d26a5f'
  inverse-primary: '#ffb4aa'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#0f0902'
  on-tertiary: '#ffffff'
  tertiary-container: '#282014'
  on-tertiary-container: '#938777'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#7e2b23'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#efe0cd'
  tertiary-fixed-dim: '#d2c4b2'
  on-tertiary-fixed: '#221a0f'
  on-tertiary-fixed-variant: '#4f4538'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: EB Garamond
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: EB Garamond
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style
The design system embodies the heritage, prestige, and meticulous care associated with rare wine collecting. It targets high-net-worth individuals and professional sommeliers who view their collections as both a passion and a significant asset. 

The visual language draws heavily from **Classical Minimalism** and **Tactile Skeuomorphism**. It prioritizes a physical, "tangible" feel through the use of paper-like textures and metallic accents that evoke the experience of reading a vintage wine list or a leather-bound cellar ledger. The emotional response should be one of calm authority, permanence, and quiet luxury.

## Colors
The palette is rooted in the organic tones of viticulture and traditional archiving. 

- **Primary (Deep Burgundy):** Used for critical branding elements, primary buttons, and active states. It represents the richness of red wine and adds weight to the interface.
- **Secondary (Gold):** Specifically reserved for borders, highlights, and decorative accents. It should be applied sparingly to mimic gold foil stamping.
- **Background (Parchment):** The primary canvas. This is not a flat hex; it should be accompanied by a subtle, low-opacity grain texture to simulate high-quality heavy-stock paper.
- **Neutrals:** Darker charcoals and muted sepias are used for text and secondary information to maintain high legibility without the harshness of pure black.

## Typography
The typographic scale emphasizes hierarchy and editorial grace.

- **Headlines:** Uses *Playfair Display*. High-contrast serifs provide an immediate sense of prestige. For the largest display titles, use a slightly tighter letter spacing to create a customized, logotype feel.
- **Body:** Uses *EB Garamond*. This ensures that long-form data, such as tasting notes or provenance histories, remain highly readable and scholarly.
- **Labels and Metadata:** Uses *Work Sans* in all-caps for technical data (e.g., ABV, Vintage Year, Bin Location). This provides a modern, functional counterpoint to the more decorative serifs, ensuring that the interface remains a practical tool.

## Layout & Spacing
This design system utilizes a **Fixed Grid** philosophy for desktop to maintain an intimate, gallery-like feel. Content is centered within a 1280px container to prevent excessive eye travel and preserve the generous whitespace that signals luxury.

- **Rhythm:** An 8px base unit drives all spacing. Component padding should lean towards the larger side (e.g., 24px or 32px) to give elements "room to breathe."
- **Breakpoints:** On mobile, margins reduce significantly (20px), and the 12-column grid collapses to 1 column. 
- **Negative Space:** Use white space as a structural element to separate different vintages or cellar wings, rather than relying on heavy dividers.

## Elevation & Depth
Depth is created through **Tonal Layers** and **Subtle Outlines** rather than aggressive shadows.

1.  **Level 0 (Base):** The textured parchment background.
2.  **Level 1 (Cards/Containers):** Slightly lighter or smoother parchment surfaces, defined by a 1px Gold border (#D4AF37) or a very thin, soft Burgundy stroke.
3.  **Elevation:** Use "Ambient Shadows" only for floating elements like dropdown menus. These shadows should be warm-toned (using a dark sepia instead of black) and extremely diffused (20% opacity or less).
4.  **Insets:** Interactive states like pressed buttons should use a subtle inner shadow to mimic a "debossed" or stamped effect in paper.

## Shapes
The shape language is **Sharp (0px)**. To maintain the traditional and authoritative aesthetic, rounded corners are avoided entirely. 

Square corners evoke the edges of wine labels, wooden crates, and architectural cellar structures. This rigidity reinforces the "vault" metaphor—stable, secure, and permanent. Any softness in the UI should come from the organic nature of the paper textures and the curves of the serif typography, not the containers themselves.

## Components
- **Buttons:** Rectangular with no radius. Primary buttons are Deep Burgundy with Gold text. Secondary buttons use a Gold 1px border with Burgundy text.
- **Sophisticated Cards:** Cards represent individual bottles. They feature a 1px Gold border and a subtle inner "inset" border (2px spacing from the edge) to mimic traditional framing.
- **Data Tables:** Used for cellar inventory. These should use hairline Burgundy horizontal dividers and "Label Caps" for headers. No vertical lines; use alignment to create structure.
- **Input Fields:** Bottom-border only (underlined style) to mimic a signature line on a document. Labels should float above in "Label Caps".
- **Interactive Elements:** Hover states on list items should use a very faint Burgundy tint (5% opacity) to highlight rows without obscuring the background texture.
- **Specialty Component - "The Sommelier Ribbon":** A vertical Gold accent used on the left side of "Featured" or "Investment Grade" bottles to denote high status.