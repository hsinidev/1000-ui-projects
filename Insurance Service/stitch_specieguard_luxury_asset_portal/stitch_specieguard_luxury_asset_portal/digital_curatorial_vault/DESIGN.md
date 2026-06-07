---
name: Digital Curatorial Vault
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1b1c1c'
  surface-container: '#1f2020'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e4e2e1'
  on-surface-variant: '#d0c5af'
  inverse-surface: '#e4e2e1'
  inverse-on-surface: '#303030'
  outline: '#99907c'
  outline-variant: '#4d4635'
  surface-tint: '#e9c349'
  primary: '#f2ca50'
  on-primary: '#3c2f00'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#735c00'
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
  tertiary: '#d0cdcd'
  on-tertiary: '#313030'
  tertiary-container: '#b4b2b2'
  on-tertiary-container: '#454544'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e4e2e1'
  surface-variant: '#353535'
typography:
  display-xl:
    fontFamily: notoSerif
    fontSize: 72px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '300'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-edge: 64px
  vault-padding: 40px
---

## Brand & Style

This design system targets high-net-worth individuals, gallery owners, and private collectors. The brand personality is one of stoic reliability, quiet exclusivity, and museum-grade reverence for the objects it protects. The UI should evoke the emotional response of entering a private viewing room in an elite auction house—silent, secure, and impeccably curated.

The visual style is a fusion of **Minimalism** and **Glassmorphism**. It utilizes expansive, intentional whitespace to let high-resolution imagery of fine art breathe. UI components are treated as "Digital Vault" modules—layered translucent surfaces that suggest depth and fortified security without the bulk of traditional skeuomorphism. This creates an atmosphere of modern luxury where protection is invisible yet ever-present.

## Colors

The palette is anchored in a dark-mode-first approach to simulate the dim, controlled environment of a professional gallery. 

- **Deep Charcoal (#1A1A1A):** Used as the primary canvas color to represent the "Vault" walls.
- **Marble White (#F5F5F5):** Reserved for primary typography and high-contrast instructional elements.
- **Gold Accents (#D4AF37):** Used sparingly as a "hallmark" color for success states, luxury status indicators, and subtle interactive highlights.
- **Translucent Overlays:** A 5-10% opacity variation of Marble White is used for glass surfaces to create a sense of layered crystal.

## Typography

This design system uses a high-contrast typographic pairing to signal authority and modernity. **Noto Serif** provides the intellectual and timeless foundation required for high-value asset management, while **Manrope** offers a refined, geometric clarity for technical data and interactive UI.

Headings should often utilize "Label-Caps" as subtitles above them to create an editorial, catalog-like feel. Generous line heights are required to maintain a sense of airiness and prestige.

## Layout & Spacing

The layout follows a **Fixed Grid** model of 12 columns, centered on the screen to feel like a framed piece of art. Margin edges are intentionally wide (64px+) to isolate the content from the viewport edges, reinforcing the feeling of a private, secure space.

Spacing follows an 8px rhythm, but utilizes "Massive Gaps" (80px, 120px, 160px) between major sections to emphasize an editorial aesthetic. Content should never feel crowded; if a screen feels busy, increase the whitespace rather than reducing the content size.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and subtle tonal layering rather than traditional drop shadows.

- **The Base Surface:** Deep Charcoal (#1A1A1A).
- **The Vault Layer:** Glassmorphic containers with a `backdrop-filter: blur(20px)` and a 1px border of 15% opacity Marble White. This creates the "Digital Vault" effect.
- **The Highlight Layer:** Subtle, long-offset ambient shadows (0px 30px 60px) with 40% opacity of the background color, used only for active modals or pulled-up asset cards to suggest they are floating closer to the viewer.

## Shapes

The design system adopts a **Sharp (0)** roundedness strategy. Hard 90-degree corners communicate architectural precision, security, and the literal framing of artwork. Circular elements are strictly reserved for profile avatars or specific status "pips." All containers, buttons, and input fields must maintain sharp, clean edges to reflect the high-end, bespoke nature of the service.

## Components

### Buttons
Primary buttons are solid Marble White with Deep Charcoal text, featuring sharp corners. Secondary buttons use a "Ghost" style: transparent background with a 1px Gold (#D4AF37) or White border. Hover states should involve a subtle expansion of the letter spacing rather than a color shift.

### Input Fields
Inputs are minimalist underlines or glassmorphic boxes with no background fill until focused. Focus states are indicated by the transition of the bottom border to Gold. Labels use the "Label-Caps" style, floating above the input.

### Cards (The Asset Frame)
Cards are the "Digital Vault" containers. They feature a 1px frosted border, a heavy backdrop blur, and internal padding of 40px. Images within cards should have a subtle inner-glow to look as if they are illuminated by gallery lighting.

### Status Indicators & Chips
Chips should be rectangular and thin. Use Gold for "Insured" or "Verified" statuses. Success and security states should feel like a wax seal or a hallmark stamp.

### Additional Components: The "Provenance Timeline"
A vertical, thin-line timeline component used to show the history of an asset. It uses Gold dots for major milestones and Manrope typography for the technical metadata.