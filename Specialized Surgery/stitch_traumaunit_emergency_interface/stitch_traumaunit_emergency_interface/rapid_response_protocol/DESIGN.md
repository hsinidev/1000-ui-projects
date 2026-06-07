---
name: Rapid Response Protocol
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4d4732'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#7e775f'
  outline-variant: '#d0c6ab'
  surface-tint: '#705d00'
  primary: '#705d00'
  on-primary: '#ffffff'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#e9c400'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#d9dada'
  on-tertiary-container: '#5e5f60'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
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
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '500'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
  stat-lg:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '900'
    lineHeight: '1'
spacing:
  base: 8px
  touch-min: 48px
  touch-standard: 56px
  margin-mobile: 20px
  gutter: 16px
  section-gap: 32px
---

## Brand & Style

The design system is engineered for high-stakes medical environments where speed and cognitive clarity are the primary requirements. The brand personality is authoritative, precise, and immediate. It avoids decorative elements to focus entirely on life-saving utility.

The aesthetic follows a **High-Contrast / Bold** movement, utilizing a restricted color palette to create an uncompromising visual hierarchy. This approach ensures that critical information—such as patient vitals or trauma alerts—is never lost in visual noise. The UI conveys "Surgical Precision" through strict alignment and sharp geometry, evoking a sense of technical reliability and extreme professionalism.

## Colors

The color strategy for this design system is based on high-visibility signaling. 

*   **Signal Yellow (#FFD700):** Reserved exclusively for primary actions, critical alerts, and active states. It acts as a beacon within the interface.
*   **Graphite (#333333):** Used for primary typography and structural containers to provide a grounded, serious tone that contrasts sharply against the white background.
*   **White (#FFFFFF):** The primary canvas color, chosen for its clinical association and to maximize the legibility of dark text.
*   **Functional Neutrals:** A secondary scale of grays is used for inactive states and background differentiation to keep the focus on the yellow and graphite "Action Layers."

## Typography

This design system utilizes **Inter** for its exceptional legibility and systematic weight distribution. The typographic scale is aggressive to ensure readability from a distance and under physical or emotional stress.

Headlines use heavy weights (Bold/Extra Bold) and tight letter-spacing to create "blocks" of information that can be scanned instantly. Body text is set with generous line heights to prevent "word crowding." For quantitative data—such as heart rates or trauma scores—the "stat-lg" style provides maximum impact. Every label is designed to be distinct from the value it describes, often utilizing uppercase styling to differentiate data from metadata.

## Layout & Spacing

The layout philosophy is **Mobile-First / Fluid**, optimized for one-handed operation in high-mobility surgical environments. The system uses an 8px base grid to ensure consistent alignment.

Large touch targets are the priority; the design system mandates a minimum height of 48px for any interactive element, with a preference for 56px in critical "Immediate Care" workflows. Margins are generous (20px) to prevent accidental edge-taps on mobile devices. Information is stacked vertically in a single-column layout for mobile to eliminate the cognitive load of scanning multiple columns under pressure.

## Elevation & Depth

To maintain surgical clarity, this design system rejects complex shadows and blurs. Depth is conveyed through **Bold Borders** and **High-Contrast Tonal Layering**.

*   **Primary Surface:** Pure white.
*   **Elevated Containers:** Defined by 2px solid Graphite borders rather than shadows. This creates a "hard" UI that feels structural and unshakeable.
*   **Active States:** Indicated by a Signal Yellow fill, effectively bringing the component to the foreground of the user's attention.
*   **Stacked Content:** When layers are necessary (such as emergency modals), a solid Graphite semi-transparent overlay (80% opacity) is used to completely isolate the background and focus the user on the task at hand.

## Shapes

The shape language is strictly **Sharp (0px radius)**. 

Every UI element—from buttons to input fields to cards—utilizes hard 90-degree corners. This decision reinforces the brand's commitment to "Surgical Precision." Sharp corners maximize screen real estate and align perfectly with the pixel grid, ensuring that the interface feels engineered rather than decorative. This uncompromising geometry communicates reliability and professional rigor.

## Components

Components in this design system are designed for "Zero-Mistake" interaction.

*   **Buttons:** Massively oversized (min 56px height). The Primary button is Signal Yellow with Graphite text. The secondary button is White with a 2px Graphite border.
*   **Status Chips:** Used for trauma levels (e.g., Level 1, Level 2). These use solid Graphite backgrounds with Signal Yellow text for maximum "Urgency" signaling.
*   **Input Fields:** Structured with a thick bottom border (3px) and high-contrast labels. When focused, the border shifts to Signal Yellow.
*   **Lists:** High-density vertical stacks with 2px Graphite separators. Each list item must have a minimum height of 64px to accommodate large touch areas.
*   **Trauma Cards:** Information containers that group patient data. They feature a "Critical Header" (Signal Yellow bar) for patients requiring immediate intervention.
*   **Action Bars:** Fixed-to-bottom buttons on mobile to ensure "Immediate Care" actions are always within thumb reach.