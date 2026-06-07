---
name: Hardened Biometric Hardware
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
  on-surface-variant: '#c4c7c4'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e918e'
  outline-variant: '#444845'
  surface-tint: '#c7c6c4'
  primary: '#ffffff'
  on-primary: '#303130'
  primary-container: '#e3e2e0'
  on-primary-container: '#646463'
  inverse-primary: '#5e5e5d'
  secondary: '#c2c2f2'
  on-secondary: '#2b2d53'
  secondary-container: '#44456e'
  on-secondary-container: '#b4b4e4'
  tertiary: '#ffffff'
  on-tertiary: '#332f30'
  tertiary-container: '#e9e1e1'
  on-tertiary-container: '#686363'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e3e2e0'
  primary-fixed-dim: '#c7c6c4'
  on-primary-fixed: '#1b1c1b'
  on-primary-fixed-variant: '#464746'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c2c2f2'
  on-secondary-fixed: '#16173d'
  on-secondary-fixed-variant: '#42436b'
  tertiary-fixed: '#e9e1e1'
  tertiary-fixed-dim: '#ccc5c5'
  on-tertiary-fixed: '#1e1b1b'
  on-tertiary-fixed-variant: '#4a4646'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-reg:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  container-padding: 24px
  gutter: 16px
  border-width-heavy: 4px
  border-width-standard: 2px
  touch-target-min: 48px
---

## Brand & Style

This design system is engineered to evoke the feeling of high-security institutional vaults and aerospace-grade hardware. The brand personality is uncompromising, stoic, and elite. It utilizes a **Modern Brutalist** aesthetic fused with **Tactile** physical metaphors to communicate an "impenetrable" digital environment. 

The target audience consists of high-net-worth individuals and security professionals who prioritize certainty over whimsy. The UI does not just sit on a screen; it feels bolted to the hardware. Visual weight is used as a proxy for security—thick strokes, high-contrast surfaces, and metallic textures ensure that every interaction feels intentional and physically reinforced.

## Colors

The palette is anchored in **Matte Black** to provide a depth that mimics a powered-down OLED screen, ensuring "Security Green" and "Platinum Silver" elements pop with high visibility. 

- **Matte Black (#121212):** Used for the primary canvas and background layers.
- **Deep Indigo (#1A1B41):** Utilized for "Secure-Touch" interaction zones and primary containers to provide a subtle, sophisticated depth contrast against the black.
- **Platinum Silver (#E5E4E2):** The primary color for typography, icons, and high-impact borders. It should be applied with a subtle linear gradient (top-to-bottom) to mimic brushed metal.
- **Security Green (#00FF41):** Reserved exclusively for successful biometric scans, confirmed transactions, and active security states.

## Typography

Typography balances the institutional clarity of **Public Sans** with the technical, geometric precision of **Space Grotesk**. 

- **Headlines:** Use Space Grotesk for a futuristic, engineering-led feel. 
- **Body:** Public Sans provides a neutral, highly legible experience for legal text and instructions.
- **Data & Addresses:** All wallet addresses, transaction hashes, and balances must use Space Grotesk. Its geometric construction mimics monospaced fonts while maintaining premium readability.
- **Privacy Masking:** When balances are hidden, use a sequence of "•" (U+2022) in Platinum Silver, or a 4px Gaussian blur overlay on the text container.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to ensure UI elements are always centered and balanced on the hardware's physical display. A strict 4px baseline grid governs all vertical rhythm.

- **Margins:** A standard 24px safety margin is required on all sides to prevent UI elements from feeling "crowded" by the physical bezel.
- **Density:** High density for data-rich screens, but low density for action-based screens (e.g., "Confirm Transaction") to prevent accidental touches.
- **Alignment:** Elements should be strictly aligned to the grid, emphasizing a structured, military-grade organization.

## Elevation & Depth

This system eschews soft shadows in favor of **Bold Borders** and **Tonal Layering**. 

- **Z-Axis Hierarchy:** Depth is created by "stacking" Platinum Silver borders. A background is Matte Black; a card is Deep Indigo with a 2px Graphite border; a button is Matte Black with a 4px Platinum Silver border.
- **Metallic Gradients:** Use subtle linear gradients (180°) on Platinum elements (from #F5F5F5 to #B0AFAC) to suggest a 3D, machined-metal edge.
- **Internal Shadows:** Use subtle inner shadows on input fields to make them appear recessed into the "chassis" of the device.

## Shapes

To reinforce the "Hardened" aesthetic, the design system utilizes **Sharp (0px)** corners for all structural components. 

- **Primary Elements:** Buttons, cards, and input fields must have 90-degree angles.
- **Exceptions:** Biometric "Secure-Touch" zones may use a circular motif to represent the fingerprint scanner's physical shape, providing a clear visual affordance for where the user should place their finger.
- **Borders:** Every container must have a visible border (minimum 2px). The contrast between a sharp-cornered container and a thick border creates the signature "Industrial" look.

## Components

- **Tactile Buttons:** Must use a 4px border of Platinum Silver. On press, the background color shifts from Matte Black to Deep Indigo, and the border thickness "sinks" (simulated by a 1px offset shift) to provide physical feedback.
- **Secure-Touch Zones:** Designated areas for biometric scanning. These feature a pulsating Deep Indigo glow and a "scanning line" animation in Security Green that moves vertically across the zone.
- **Information Lists:** Key-value pairs (e.g., "Network Fee: 0.0002 BTC") should be separated by a 1px Graphite dotted line.
- **Privacy Toggles:** Use a "Shield" icon that, when active, blurs all sensitive data containers. 
- **Status Chips:** Small, rectangular chips with 1px borders. Success states use Security Green text and borders; idle states use Platinum Silver.
- **Hardened Inputs:** Recessed fields with a technical "monospaced" cursor (a solid block) and 2px borders that highlight in Security Green when the biometric lock is successfully cleared.