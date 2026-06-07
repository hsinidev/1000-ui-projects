---
name: Spirit-Archive
colors:
  surface: '#141313'
  surface-dim: '#141313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a29'
  surface-container-highest: '#353434'
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
  on-tertiary: '#313030'
  tertiary-container: '#e5e2e1'
  on-tertiary-container: '#656464'
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
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c9c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#141313'
  on-background: '#e5e2e1'
  surface-variant: '#353434'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
spacing:
  unit: 4px
  gutter: 24px
  margin: 48px
  container-max: 1440px
---

## Brand & Style

The core philosophy of this design system is **Digital Provenance & Vault Security**. It is designed for collectors and institutions who require absolute certainty regarding the authenticity of high-value assets. The visual language balances the cold, technical precision of blockchain technology with the tactile, prestigious nature of rare spirits.

The aesthetic is **Industrial Hardened Minimalism**. It rejects softness and organic shapes in favor of sharp 90-degree angles, "tamper-proof" structural elements, and a high-security "Control Center" feel. The UI should evoke the sensation of accessing a high-clearance digital vault where every interaction is logged and verified. Key motifs include laser-thin scanning lines, micro-textures reminiscent of brushed metal, and monospaced data strings that emphasize technical transparency.

## Colors

The palette is strictly limited to convey a sense of "Hardened" authority. 

*   **Deep Black (#0A0A0A):** Acts as the primary substrate. It represents the "Dark Vault" environment, providing maximum contrast for high-security data.
*   **Deep Indigo (#1A1B41):** Used for structural reinforcement and container backgrounds. It provides depth without sacrificing the "Night Vision" technical feel.
*   **Platinum Silver (#E5E4E2):** The primary interactive and highlight color. It should be applied to key data, borders, and typography to mimic the sheen of precious metals.
*   **Success/Error:** Use a high-vibrancy "Cyan-Mint" for verified states and a "Precision Red" for tamper alerts. These should appear as glowing "LED" status indicators against the dark background.

Metallic gradients should be used sparingly, moving from #C0C0C0 to #E5E4E2 at 45-degree angles to simulate brushed aluminum on primary buttons and headers.

## Typography

This design system utilizes a dual-font strategy to separate brand narrative from technical fact.

1.  **Inter (UI & Narrative):** Used for headlines, descriptions, and primary navigation. It provides a clean, modern, and Swiss-inspired foundation that feels authoritative and objective.
2.  **JetBrains Mono (Data & Security):** Used for all blockchain hashes, provenance IDs, bottle numbers, and "Scanning" readouts. This monospaced font reinforces the "Hardened" technical nature of the registry.

All labels should be set in uppercase with increased letter spacing to emulate the stamped engravings found on industrial machinery or high-end watch movements.

## Layout & Spacing

The layout philosophy is based on a **Precision Fixed Grid**. Alignment is paramount; every element must feel "bolted" into place.

*   **Grid:** A 12-column system with 24px gutters.
*   **Rhythm:** All spacing (padding, margins) must follow a 4px base unit. 
*   **Scanning Lines:** Horizontal and vertical lines (1px width, #2D2E5A) should frequently be used to subdivide sections, creating a "schematic" or "blueprint" look.
*   **Margins:** Generous outer margins (48px+) ensure the content feels like a protected asset in the center of the screen, rather than edge-to-edge web content.

## Elevation & Depth

Standard shadows are prohibited in this design system. Depth is instead achieved through **Tonal Layering** and **Structural Outlines**.

*   **Layer 0 (Background):** Deep Black (#0A0A0A).
*   **Layer 1 (Containers):** Deep Indigo (#1A1B41) with a 1px solid border of #2D2E5A.
*   **Layer 2 (Active States):** Use inner glows (0px blur, 1px spread) in Platinum Silver to suggest an element is "pressed" or "engaged."
*   **Scanning Motif:** A 1px horizontal line with a subtle linear-gradient (Transparent -> Platinum -> Transparent) should slowly animate vertically across "Verification" cards to simulate an active security scan.
*   **Micro-textures:** Use a subtle noise or "brushed metal" SVG overlay (opacity 3%) on Layer 1 surfaces to give them a physical, tamper-proof feel.

## Shapes

The shape language is strictly **Geometric and Sharp**. 

*   **Corners:** All corners are 0px (Sharp). This conveys an industrial, uncompromising, and "hardened" security feel.
*   **Accents:** Use 45-degree chamfered corners for buttons or status badges to emphasize the "milled metal" aesthetic.
*   **Borders:** Use double-borders (a 1px Platinum line inside a 2px Deep Indigo frame) for the most critical data points to signify "Highest Security" status.

## Components

### Buttons
Primary buttons use a metallic Platinum-to-Silver gradient background with black uppercase text. Secondary buttons are transparent with a 1px Platinum border and "bracket" icons `[ ]` surrounding the text.

### Inputs
Input fields should appear as "Data Ports." They feature a Deep Black background and are only underlined by a 2px Platinum bar that glows slightly when focused. Use JetBrains Mono for all user input.

### Provenance Cards
The centerpiece of the UI. These cards must have a 1px Platinum border and a "Scanning" animation overlay. All serial numbers should be displayed in a larger monospaced font with a light "glow" effect to mimic a high-end digital readout.

### Status Indicators (Tamper-Proof)
Instead of simple dots, use "Security Seals." These are small rectangular blocks that resemble physical break-away tabs. If a record is "Verified," the seal is Cyan-Mint; if "Compromised," it is Red and features a "Caution" hatch pattern (striped diagonal lines).

### Navigation
Top-level navigation should be strictly horizontal, separated by vertical 1px divider lines. No dropdowns; use "Drill-down" side panels to maintain the feeling of a technical diagnostic tool.