---
name: Cyber-Biological Health Interface
colors:
  surface: '#101417'
  surface-dim: '#101417'
  surface-bright: '#36393d'
  surface-container-lowest: '#0b0f11'
  surface-container-low: '#191c1f'
  surface-container: '#1d2023'
  surface-container-high: '#272a2d'
  surface-container-highest: '#323538'
  on-surface: '#e0e2e6'
  on-surface-variant: '#cdc3d4'
  inverse-surface: '#e0e2e6'
  inverse-on-surface: '#2d3134'
  outline: '#968e9e'
  outline-variant: '#4a4452'
  surface-tint: '#d6baff'
  primary: '#d6baff'
  on-primary: '#430089'
  primary-container: '#5e2ca5'
  on-primary-container: '#ccabff'
  inverse-primary: '#7343bb'
  secondary: '#ddfcff'
  on-secondary: '#00363a'
  secondary-container: '#00f1fe'
  on-secondary-container: '#006a70'
  tertiary: '#c6c4df'
  on-tertiary: '#2f2e43'
  tertiary-container: '#49485f'
  on-tertiary-container: '#b9b7d2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ecdcff'
  primary-fixed-dim: '#d6baff'
  on-primary-fixed: '#280057'
  on-primary-fixed-variant: '#5a27a1'
  secondary-fixed: '#74f5ff'
  secondary-fixed-dim: '#00dbe7'
  on-secondary-fixed: '#002022'
  on-secondary-fixed-variant: '#004f54'
  tertiary-fixed: '#e2e0fc'
  tertiary-fixed-dim: '#c6c4df'
  on-tertiary-fixed: '#1a1a2e'
  on-tertiary-fixed-variant: '#45455b'
  background: '#101417'
  on-background: '#e0e2e6'
  surface-variant: '#323538'
typography:
  h1:
    fontFamily: spaceGrotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: atkinsonHyperlegibleNext
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: atkinsonHyperlegibleNext
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: spaceGrotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  margin: 20px
  gutter: 16px
---

## Brand & Style

This design system establishes a high-fidelity environment where biological intuition meets computational precision. The brand personality is rooted in **Futuristic Trust**—positioning the platform as a sophisticated extension of the user’s own neural network. 

The aesthetic is **Cyber-Biological**, a fusion of clinical cleanliness and advanced digital craftsmanship. It utilizes **Glassmorphism** to create a sense of light and transparency, mirroring the clarity required in medical diagnostics. Subtle, generative organic patterns (inspired by neural pathways and cellular structures) breathe life into the static charcoal canvas, ensuring the interface feels responsive and "alive" rather than cold or purely mechanical.

## Colors

The palette is designed for deep-focus environments, prioritizing visual comfort and information hierarchy.

*   **Primary (Deep Purple):** Represents the mystery and depth of the human mind. Used for primary actions and brand presence.
*   **Secondary (Glass-Cyan):** A high-vibrancy accent that mimics medical lasers and digital synapses. Used for critical highlights, data points, and active states.
*   **Background (Charcoal/Black):** A true-dark foundation that allows glass layers to pop and minimizes eye strain during cognitive monitoring.
*   **Text (Neural-White):** An off-white, high-legibility hue that prevents the harsh glare of pure white while maintaining maximum contrast against the dark backdrop.

## Typography

This design system employs a dual-font strategy to balance technical innovation with medical accessibility. 

**Space Grotesk** is used for headlines and navigation elements. Its geometric, slightly eccentric forms convey a cutting-edge, scientific tone. 

**Atkinson Hyperlegible Next** is used for all body copy and clinical data. As a font designed specifically for readability and clarity, it reinforces the "Trust-Centric" pillar of the brand, ensuring that critical health information is never misread. All data-heavy displays should utilize tabular figures to maintain vertical alignment in charts.

## Layout & Spacing

This design system utilizes a **Mobile-First Fluid Grid**. On mobile devices, the layout relies on a 4-column system with a 20px outer margin. 

The spacing rhythm is governed by an 8px baseline grid to ensure mathematical harmony. Components should use generous internal padding (MD or LG) to emphasize the "Glassmorphism" effect, allowing the background neural patterns to be partially visible through the "breathable" whitespace of the containers. Vertical rhythm should prioritize grouping related medical data through proximity, using XL spacing only to separate major cognitive sections.

## Elevation & Depth

Depth is conveyed through **Glassmorphic Stacking** rather than traditional drop shadows. 

1.  **Base Layer:** The Charcoal background with subtle, animated neural filaments.
2.  **Surface Layer:** Semi-transparent containers (Background Blur: 20px) with a 1px inner border in a low-opacity Neural-White to define edges.
3.  **Active Layer:** Elements that require attention utilize a "Cyan Glow"—a soft, diffused outer glow (0px 0px 15px) using the Glass-Cyan color, simulating a bioluminescent pulse.
4.  **Interaction:** When a user taps a card, it should slightly increase in scale and its background blur intensity should increase, visually "lifting" it closer to the user.

## Shapes

The shape language reflects the **Cyber-Biological** theme by avoiding both sharp clinical corners and overly playful circles. A consistent **Rounded (0.5rem)** radius is applied to standard UI elements like input fields and buttons. 

Larger containers and cards use **Rounded-LG (1rem)** or **Rounded-XL (1.5rem)** to evoke organic, pebble-like forms found in nature. These soft edges contrast with the technical, geometric typography, creating a balanced visual tension between the "Human" and the "Machine."

## Components

*   **Buttons:** Primary actions are filled with a Deep Purple gradient, featuring a Cyan "glow" on hover/active states. Secondary actions use a ghost-style border with a high background blur.
*   **Medical Cards:** Must feature a glassmorphic background. Use the top-right quadrant for critical status indicators (e.g., heart rate, neural load) using Glass-Cyan text.
*   **Neural Inputs:** Text fields should be dark-themed with a subtle 1px Neural-White border that transitions to a solid Glass-Cyan border when focused.
*   **Data Chips:** Small, pill-shaped elements used for tagging cognitive states. They should be semi-transparent with Glass-Cyan text.
*   **Progress Orbs:** Instead of linear bars, use circular "Neural Pulse" loaders that expand and contract organically to show processing states.
*   **Bio-Feedback Toggles:** Use a fluid animation when toggled, where the switch "bleeds" color from Charcoal to Deep Purple like a liquid capillary.