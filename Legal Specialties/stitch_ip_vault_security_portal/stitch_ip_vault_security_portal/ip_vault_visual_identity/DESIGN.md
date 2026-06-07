---
name: IP-Vault Visual Identity
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#44474e'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#495f84'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#001b3d'
  on-primary-container: '#6f84ac'
  inverse-primary: '#b1c7f2'
  secondary: '#5e5e5d'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdd'
  on-secondary-container: '#626361'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#001b3c'
  on-tertiary-container: '#6185bd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b1c7f2'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#31476b'
  secondary-fixed: '#e3e2e0'
  secondary-fixed-dim: '#c7c6c4'
  on-secondary-fixed: '#1b1c1b'
  on-secondary-fixed-variant: '#464746'
  tertiary-fixed: '#d5e3ff'
  tertiary-fixed-dim: '#a7c8ff'
  on-tertiary-fixed: '#001b3c'
  on-tertiary-fixed-variant: '#1f477b'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.0'
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-page: 48px
  border-thick: 2px
  border-heavy: 4px
---

## Brand & Style

This design system is built to evoke the impenetrable nature of a physical bank vault, translated into a digital interface for Intellectual Property and Patent Law. The brand personality is **uncompromising, elite, and fortified**. It targets high-stakes inventors, corporate legal teams, and stakeholders who prioritize the absolute security of their intellectual assets.

The visual style is a fusion of **Institutional Brutalism** and **Modern Corporate** aesthetics. It rejects soft, "friendly" consumer trends in favor of structural integrity. Every element is designed to look heavy and permanent, utilizing thick structural borders and a monochrome-leaning palette to communicate a "Zero-Trust" security environment that is both professional and authoritative.

## Colors

The palette is restricted to three core tones to maintain a serious, high-contrast environment.

*   **Midnight Blue (Primary):** A deep, near-black blue used for primary actions, structural headers, and text to provide a sense of depth and authority.
*   **Platinum Silver (Secondary):** A metallic neutral used for surface backgrounds, secondary containers, and borders. It provides a tactile, "brushed metal" feel.
*   **Pure White (Neutral):** Used strictly for high-visibility content areas and active input fields to ensure maximum legibility.
*   **Accent (Alert Red/Success Green):** Used sparingly only for critical status indicators (e.g., "Patent Filed" or "Security Breach"), maintaining the "Bank Vault" signal logic.

## Typography

The typography strategy prioritizes structural clarity and institutional weight. 

**Inter** is utilized for headlines and labels to provide a mechanical, systematic feel. Headlines should use heavy weights (700+) to simulate the impact of engraved or stamped text. Labels and button text should be set in uppercase with slight tracking to mimic government or military documentation.

**Public Sans** is used for body text and legal disclosures. Its institutional heritage (originally designed for government use) reinforces the "official" nature of the design system while ensuring high legibility for complex patent filings and legal jargon.

## Layout & Spacing

This design system follows a **Fixed Grid** model to create a sense of rigid structure and predictability. The layout is centered on a 12-column grid with generous gutters.

The spacing rhythm is based on an 8px base unit, but applied with "heavy" intent. Content is grouped in clearly defined blocks separated by thick borders rather than whitespace alone. The layout should feel "locked-in," with consistent horizontal alignment that suggests a reinforced framework. Padding inside components should be ample to ensure that the content never feels crowded, maintaining a premium, "gallery-like" presentation of intellectual property data.

## Elevation & Depth

Elevation in this design system is achieved through **Tonal Layering and Bold Borders** rather than traditional shadows. To maintain the "Bank-Vault" aesthetic, we avoid soft, ambient shadows which feel too airy and consumer-focused.

1.  **Plinth Layering:** Components do not float; they sit on "Platinium Silver" surfaces. Depth is indicated by switching between White and Silver backgrounds.
2.  **Inset Effects:** For active inputs or "Vault" containers, use a subtle 1px inner stroke to create a recessed, "etched" look.
3.  **High-Contrast Outlines:** Every card, button, and module must have a minimum 2px solid border in Midnight Blue. This creates a "blueprint" or "technical drawing" feel that reinforces the structural integrity of the UI.

## Shapes

The shape language is strictly **Sharp (0px radius)**. Curves are avoided entirely to maintain a high-security, industrial aesthetic. Every button, input field, and card must have 90-degree corners. This evokes the imagery of steel plates, safe-deposit boxes, and official legal documents. Any use of circular elements should be restricted to iconography (e.g., wax seals or circular vault locks).

## Components

**Buttons:** Primary buttons are solid Midnight Blue with White uppercase text. They feature a 2px "offset" border or a thick bottom-weighted stroke to feel like physical, heavy-duty switches.

**Cards:** "Vault Cards" feature a 2px Midnight Blue border and a 4px header strip. They are used to house sensitive patent data. Every card should feature a "Security Status" seal in the top right corner.

**Input Fields:** Recessed White backgrounds with a 2px Silver border that turns Midnight Blue on focus. Labels sit outside the field in a bold, uppercase Inter font.

**Security Icons:** Use custom line-art iconography with a heavy 2px stroke weight. Common motifs include shielded locks, braided wax seals, and biometric scan lines.

**Lists:** Data lists should resemble a ledger, with thick horizontal separators and "Locked/Unlocked" status indicators for each row.

**Additional Components:**
*   **The "Seal":** A floating or fixed badge component used to verify the authenticity of a patent or document.
*   **The "Vault Progress" Bar:** A segmented progress bar (rather than a smooth one) to show filing stages, feeling like a mechanical locking mechanism clicking into place.