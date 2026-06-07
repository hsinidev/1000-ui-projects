---
name: Cipher-Ship
colors:
  surface: '#131319'
  surface-dim: '#131319'
  surface-bright: '#39393f'
  surface-container-lowest: '#0d0e13'
  surface-container-low: '#1b1b21'
  surface-container: '#1f1f25'
  surface-container-high: '#292930'
  surface-container-highest: '#34343b'
  on-surface: '#e4e1ea'
  on-surface-variant: '#c6c5d4'
  inverse-surface: '#e4e1ea'
  inverse-on-surface: '#303036'
  outline: '#908f9d'
  outline-variant: '#454652'
  surface-tint: '#bdc2ff'
  primary: '#bdc2ff'
  on-primary: '#1b247f'
  primary-container: '#1a237e'
  on-primary-container: '#8690ee'
  inverse-primary: '#4c56af'
  secondary: '#c7c6c4'
  on-secondary: '#303130'
  secondary-container: '#464746'
  on-secondary-container: '#b5b5b3'
  tertiary: '#c6c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#303030'
  on-tertiary-container: '#989898'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bdc2ff'
  on-primary-fixed: '#000767'
  on-primary-fixed-variant: '#343d96'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#131319'
  on-background: '#e4e1ea'
  surface-variant: '#34343b'
typography:
  headline-lg:
    fontFamily: Geist
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-md:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Geist
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: Geist
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
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
  margin: 40px
  grid-columns: '12'
---

## Brand & Style

The design system is engineered to evoke an atmosphere of absolute impenetrability and technical precision. It targets high-stakes data logistics where trust is the primary commodity. The aesthetic direction leverages a **Technical Minimalist** approach infused with **Tactile Industrial** elements.

The brand personality is authoritative, cold, and unwavering. Users should feel as though they are interacting with a high-end security terminal rather than a standard consumer application. This is achieved through high-contrast interfaces, precision-aligned technical grids, and a palette that mimics heavy-duty metals and deep-space security environments. The interface focuses on "proof of security"—visualizing verification processes and hardware-level integrity at every touchpoint.

## Colors

The color strategy for this design system is built on a foundation of "Structural Dark."

*   **Deep Indigo (#1A237E):** Used as the primary atmospheric layer, providing a sense of depth and institutional trust. It serves as the primary surface for interaction elements.
*   **Platinum Silver (#E5E4E2):** This is the "Technical" highlight. It is used for typography on dark backgrounds, borders that represent metallic casings, and iconography.
*   **Black (#000000):** Reserved for the deepest background layers and "dead-space" to create a high-contrast environment that makes active components pop.
*   **Functional Accents:** A piercing **Secure Green** and **Alert Red** are utilized sparingly for high-contrast security indicators, mimicking the LED status lights found on server racks and hardware vaults.

Backgrounds should utilize subtle linear gradients from Black to Deep Indigo to simulate the sheen of brushed obsidian or matte-finished metal.

## Typography

This design system utilizes **Geist** for its core communication due to its ultra-clean, technical precision and wide apertures which ensure readability in high-stress scenarios.

For technical readouts, PIN entries, and metadata, **JetBrains Mono** is employed. The monospaced nature of the font reinforces the "data transport" narrative and provides an aesthetic link to hardware diagnostics. 

**Hierarchy Rules:**
*   **Headlines:** Keep tight tracking and bold weights to simulate stamped metal labels.
*   **Labels:** Always use uppercase monospaced type for secondary information (e.g., timestamps, serial numbers, or status indicators) to evoke a sense of automated logging.
*   **Contrast:** Use Platinum Silver for primary text and a 60% opacity variant for secondary technical details.

## Layout & Spacing

The layout is governed by a **Fixed Structural Grid** that emphasizes order and predictability. The 8px base unit ensures that every element feels mathematically aligned, reinforcing the high-trust technical nature of the system.

A subtle **"Scanning Grid"** pattern (1px lines at 32px intervals) should be overlaid at low opacity (3-5%) on primary container backgrounds to give the interface a calibrated, technical feel. Content should be grouped into rigid, modular panels that suggest a dashboard of hardware components. Heavy internal padding (32px+) within cards is encouraged to maintain a premium, spacious "vault" feel despite the high-contrast color palette.

## Elevation & Depth

Elevation in this design system is not achieved through soft shadows, but through **Tonal Layering** and **Metallic Sheen**. 

*   **Base Layer:** Solid Black (#000000).
*   **Surface Layer:** Deep Indigo (#1A237E) with a subtle 1px inner border in Platinum Silver at 20% opacity.
*   **Active Layer:** Elements that are "engaged" or "verified" gain a slight outer glow (5px blur) using the accent color (Green or Silver), simulating an illuminated hardware panel.
*   **Glassmorphism:** Use backdrop-blur (12px) on overlays to create a "frosted lens" effect, as if viewing the UI through a reinforced security screen. Avoid heavy drop shadows; use high-contrast borders to define edge-depth instead.

## Shapes

The shape language is strictly **Geometric and Industrial**. 

A low roundedness (0.25rem) is used for containers and buttons to avoid a "consumer-soft" look while preventing the interface from appearing overly aggressive. This "Soft-Industrial" corner radius suggests precision milling.

Special elements, like biometric scanners or progress indicators, may use perfect circles to contrast against the rigid rectangular layout, representing the "human" or "organic" element being verified against the machine.

## Components

### Secure Input Fields
Input fields for PIN codes and hashes must use segmented boxes with a focus state that triggers a high-contrast Platinum border. The cursor should be a solid block rather than a line, reinforcing the terminal aesthetic.

### Tamper-Proof Badges
Status indicators for data integrity should feature a "Hatch Pattern" background and a 1px border. They must include a unique serial number or timestamp in monospaced type to signify a unique, non-fungible security state.

### Biometric Verification Prompts
These components should utilize a circular frame with a horizontal "scanning line" animation that moves vertically. Use the Primary Green accent during the active scan and the Platinum Silver for the idle state.

### Buttons
Buttons are high-contrast blocks. 
*   **Primary:** Platinum Silver background with Black text. No rounded corners (0px) to distinguish them as "Action Triggers."
*   **Secondary:** Deep Indigo background with a 1px Platinum border.
*   **Interaction:** On hover, buttons should trigger a "flicker" effect or a slight increase in border-glow.

### Security Indicators
High-visibility LEDs (small circles with a radial gradient glow) must be placed next to critical data points to indicate "Encrypted," "Locked," or "Transporting" status.