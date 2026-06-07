---
name: Vault-Secure Design System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1b1b'
  surface-container: '#1f1f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c8c5cf'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#303030'
  outline: '#918f99'
  outline-variant: '#47464e'
  surface-tint: '#c2c2f2'
  primary: '#c2c2f2'
  on-primary: '#2b2d53'
  primary-container: '#1a1b41'
  on-primary-container: '#8283af'
  inverse-primary: '#5a5b84'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c0c1ff'
  on-tertiary: '#1d1d8a'
  tertiary-container: '#060078'
  on-tertiary-container: '#787ce6'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e1e0ff'
  primary-fixed-dim: '#c2c2f2'
  on-primary-fixed: '#16173d'
  on-primary-fixed-variant: '#42436b'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e1e0ff'
  tertiary-fixed-dim: '#c0c1ff'
  on-tertiary-fixed: '#05006c'
  on-tertiary-fixed-variant: '#3639a0'
  background: '#131313'
  on-background: '#e2e2e2'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
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
    fontFamily: Space Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Space Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
spacing:
  unit: 4px
  gutter: 16px
  margin-mobile: 20px
  margin-desktop: 64px
  container-max: 1440px
  border-weight: 3px
---

## Brand & Style

The design system is engineered to evoke an atmosphere of impenetrable security and elite status. It targets high-net-worth individuals navigating the intersection of luxury automotive assets and blockchain technology. The aesthetic—described as **"Hardened Industrial"**—prioritizes structural integrity over decorative softness.

The brand personality is authoritative, precise, and permanent. It avoids the typical "airy" luxury tropes in favor of a "bank-vault" digital experience. Visual signals focus on physical metaphors of strength: thick architectural lines, brushed metal surfaces, and heavy-duty data density that suggests professional-grade tooling. The emotional response is one of absolute trust; the user should feel that their assets are physically locked within the interface.

## Colors

The palette is anchored in a high-contrast dark mode to emphasize the "Vault" metaphor. **Deep Indigo** serves as the primary structural base, providing a depth that feels more sophisticated than pure black. **Platinum Silver** is used for primary text, borders, and metallic accents, creating a high-end, machined aesthetic.

**Black** is reserved for the deepest background layers and "cut-out" sections of the UI. To represent the "Soulbound" blockchain technology, a **Soulbound Glow** (a vibrant, semi-luminescent variation of the indigo) is used sparingly for active states, authentication confirmations, and cryptographic signatures. All gradients should mimic the behavior of brushed platinum, using subtle shifts between silver and cool grays.

## Typography

Typography in this design system creates a hierarchy between "Editorial Luxury" and "Technical Truth." 

**Montserrat** is the display typeface, utilized in heavy weights to feel "stamped" or "engraved" into the interface. It provides a confident, geometric foundation. **Inter** handles the primary body copy, chosen for its exceptional readability in high-density data environments. 

**Space Mono** is the critical secondary typeface, used exclusively for blockchain addresses, transaction IDs, vehicle VINs, and telemetry data. This monospaced accent serves as a visual "proof" of the underlying technology, ensuring that data points look distinct from narrative content.

## Layout & Spacing

The layout philosophy follows a **"Secured Grid"** model. It uses a 12-column fluid system with intentionally rigid gutters to maintain the "hardened" look. While spacing is premium (generous external margins), internal data areas utilize high density to show the user all critical information at a glance, minimizing the need for scrolling during high-stakes actions.

**Mobile-First Approach:** On mobile, components span the full width of the screen to maximize the "block" feel. 
**Desktop Scaling:** On larger screens, content is housed in "Vault Containers" with fixed maximum widths, preventing the UI from feeling stretched and maintaining a sense of architectural control. Vertical rhythm is strictly enforced using 4px increments to ensure all "hardened" borders align across horizontal planes.

## Elevation & Depth

This design system rejects soft, ambient shadows in favor of **Structural Layering**. Depth is communicated through:

1.  **Thick Outlines:** All primary containers use a 3px border in Platinum Silver or Deep Indigo.
2.  **Metallic Gradients:** Surfaces use subtle linear gradients (45-degree angle) to simulate light hitting machined metal.
3.  **Inset States:** Buttons and interactive elements use inner shadows or "pressed" border shifts to feel mechanically engaged.
4.  **Soulbound Illumination:** Elevation "Level 2" is indicated by a subtle outer glow using the Soulbound Indigo, suggesting the component is energized or "live" on the blockchain.

## Shapes

The shape language is dominated by **90-degree angles**. Sharp corners are the default for all buttons, cards, and input fields to reinforce the "hardened" and "secure" brand promise. 

In rare instances where "slight radii" are required for specific mobile hardware ergonomics, the radius must never exceed 2px. The goal is to avoid any visual softness that might contradict the "Vault-Secure" aesthetic. Icons should follow suit, utilizing thick strokes and square terminals rather than rounded caps.

## Components

### Buttons
Primary buttons are block-styled with 3px Platinum Silver borders. The background uses a subtle metallic gradient. Text is Montserrat Bold, uppercase. Hover states trigger the Soulbound Indigo glow effect behind the button.

### Cards (Vaults)
Cards are the primary container. They feature a Deep Indigo background with a 1px internal border and a 3px external structural border. The top-right corner of cards should feature a monospaced "Serial Number" to identify the asset.

### Inputs
Fields use a Black background to appear "sunken" into the UI. The border is 3px Platinum Silver. The cursor and text input utilize Space Mono to emphasize the technical nature of the data being entered.

### Soulbound Chips
Status indicators for blockchain verification (e.g., "Verified Owner") use a semi-transparent Deep Indigo fill with a pulsing Soulbound Indigo border.

### Data Grids
For vehicle specifications and blockchain history, use high-density tables with hairline dividers. All numeric data must be right-aligned and set in Space Mono to allow for easy vertical scanning of values.

### The "Kill-Switch" (Unique Component)
A prominent, high-contrast component for locking or burning digital titles. It features a cross-hatched "hazard" pattern border in Platinum and Indigo, requiring a "slide-to-confirm" interaction to prevent accidental execution.