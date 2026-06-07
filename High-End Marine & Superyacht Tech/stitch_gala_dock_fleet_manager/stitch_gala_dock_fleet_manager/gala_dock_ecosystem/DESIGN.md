---
name: Gala-Dock Ecosystem
colors:
  surface: '#0c1609'
  surface-dim: '#0c1609'
  surface-bright: '#323c2d'
  surface-container-lowest: '#071105'
  surface-container-low: '#141e11'
  surface-container: '#182214'
  surface-container-high: '#222d1e'
  surface-container-highest: '#2d3828'
  on-surface: '#dae6d0'
  on-surface-variant: '#baccb0'
  inverse-surface: '#dae6d0'
  inverse-on-surface: '#293324'
  outline: '#85967c'
  outline-variant: '#3c4b35'
  surface-tint: '#2ae500'
  primary: '#efffe3'
  on-primary: '#053900'
  primary-container: '#39ff14'
  on-primary-container: '#107100'
  inverse-primary: '#106e00'
  secondary: '#c9c6c5'
  on-secondary: '#313030'
  secondary-container: '#4a4949'
  on-secondary-container: '#bab8b7'
  tertiary: '#f9fafa'
  on-tertiary: '#2f3131'
  tertiary-container: '#dddddd'
  on-tertiary-container: '#606162'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#79ff5b'
  primary-fixed-dim: '#2ae500'
  on-primary-fixed: '#022100'
  on-primary-fixed-variant: '#095300'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c9c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#0c1609'
  on-background: '#dae6d0'
  surface-variant: '#2d3828'
typography:
  headline-xl:
    fontFamily: Montserrat
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Montserrat
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-display:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: -0.03em
spacing:
  unit: 4px
  container-padding-mobile: 1rem
  container-padding-desktop: 2rem
  gutter: 1rem
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2rem
---

## Brand & Style

The design system is engineered for the high-stakes environment of luxury maritime logistics. It targets yacht captains and fleet managers who require split-second decision-making capabilities. The brand personality is **Precise, Command-Oriented, and High-Octane**. 

The visual style merges **High-Contrast Minimalism** with **Futuristic Glassmorphism**. We utilize deep, "Carbon Black" layers to represent the structural integrity of a vessel, accented by "Neon Mint" to signify active energy and technological precision. Subtle carbon fiber textures are applied to structural elements to reinforce the luxury-industrial nature of yacht tenders and toys. The interface must feel like a tactical heads-up display (HUD), prioritizing raw performance and clarity over decorative elements.

## Colors

This design system utilizes a high-contrast dark-mode palette optimized for low-light bridge environments and bright sunlight visibility on deck.

- **Carbon Black (#0A0A0A):** The foundation. Used for all primary backgrounds to reduce eye strain and maximize the "pop" of active elements.
- **Neon Mint (#39FF14):** The pulse of the fleet. Reserved strictly for primary actions, active status indicators, and critical data points.
- **Crisp White (#FFFFFF):** Primary typography and high-level icons to ensure maximum legibility against the dark background.
- **Urgent Recall (#FF3B30):** A specialized signal color used exclusively for "Recall" actions and emergency fleet alerts, creating an immediate visual hierarchy of danger vs. routine.

## Typography

Typography is treated as a functional tool for data density and urgent communication. 

- **Display & Headlines:** Montserrat provides a geometric, bold authority. Use heavy weights (700-800) for fleet statuses to evoke a sense of power.
- **Body & Interface:** Inter is used for its exceptional legibility and neutral tone, ensuring that even complex toy inventory lists remain readable.
- **Functional Labels:** Space Grotesk is employed for technical data, coordinates, and "Recall" buttons to provide a futuristic, monospaced-adjacent aesthetic that feels like a precision instrument.

## Layout & Spacing

This design system follows a **Mobile-First Tactical Grid**. On mobile, we use a single-column fluid layout with rigorous 16px (4-unit) side margins to ensure touch targets remain clear of screen edges.

The spacing rhythm is based on a **4px base unit**. Elements are stacked using tight vertical spacing to maximize information density, allowing captains to see the entire fleet status at a glance without excessive scrolling. On tablet and desktop, the layout expands into a 12-column grid, with high-priority "Recall" controls and fleet maps pinned to persistent side-panels for immediate access.

## Elevation & Depth

Depth is achieved through **Tonal Stacking and Glassmorphism** rather than traditional drop shadows.

1.  **Base Layer:** Solid Carbon Black (#0A0A0A).
2.  **Surface Layer:** A slightly elevated dark grey (#1A1A1A) with a subtle carbon fiber pattern overlay (low opacity).
3.  **Floating Layer (Glass):** Used for modals and urgent recall overlays. These utilize a 20px backdrop blur with a 1px "Neon Mint" or "White" inner border to simulate a physical glass panel floating over the engine room.
4.  **Indicators:** Active states are indicated by an outer glow using the Neon Mint color, simulating an LED illumination effect.

## Shapes

The shape language is **Aggressive and Sharp**. This design system avoids soft, organic curves in favor of industrial precision. 

- All primary buttons and containers use **0px (Sharp)** corners to reflect the sleek, metallic nature of luxury yacht engineering.
- Specialized "Recall" buttons may feature a 45-degree "clipped corner" (chamfer) effect to distinguish them from standard navigation, further emphasizing their tactical importance.
- Dividers are thin, 1px lines at 10% opacity, maintaining a clean, technical blueprint aesthetic.

## Components

- **The 'RECALL ALL' Button:** A high-impact, full-width component with a pulsing red background or heavy Neon Mint border. It is always sticky to the bottom of the mobile viewport.
- **Fleet Status Cards:** Sharp-edged containers with a glassmorphism header. They display critical telemetry (Battery, Location, Driver) using the 'Data-Display' typographic style.
- **Interactive Map Pins:** Neon Mint circles with a radial pulse effect to indicate real-time movement of tenders and jet skis.
- **Toggle Switches:** Rectangular and industrial, moving between "Docked" (Dimmed White) and "Deployed" (Neon Mint).
- **Glass Modals:** Used for emergency confirmations, featuring a heavy backdrop blur and high-contrast typography to ensure focus remains on the urgent decision.
- **Status Chips:** Small, rectangular labels with uppercase 'Space Grotesk' text. "In-Use" chips are Neon Mint; "Maintenance" chips are Amber; "Available" chips are White.