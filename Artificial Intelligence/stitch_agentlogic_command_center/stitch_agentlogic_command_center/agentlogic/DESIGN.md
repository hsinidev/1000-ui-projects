---
name: AgentLogic
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a393a'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2b'
  surface-container-highest: '#353436'
  on-surface: '#e5e2e3'
  on-surface-variant: '#cbc3d9'
  inverse-surface: '#e5e2e3'
  inverse-on-surface: '#313031'
  outline: '#958da2'
  outline-variant: '#4a4456'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3b0091'
  primary-container: '#7d3cff'
  on-primary-container: '#f3eaff'
  inverse-primary: '#6f27f1'
  secondary: '#b8c3ff'
  on-secondary: '#002388'
  secondary-container: '#0043eb'
  on-secondary-container: '#c6ceff'
  tertiary: '#00dce5'
  on-tertiary: '#003739'
  tertiary-container: '#00787d'
  on-tertiary-container: '#b3fbff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5600ca'
  secondary-fixed: '#dde1ff'
  secondary-fixed-dim: '#b8c3ff'
  on-secondary-fixed: '#001356'
  on-secondary-fixed-variant: '#0035be'
  tertiary-fixed: '#63f7ff'
  tertiary-fixed-dim: '#00dce5'
  on-tertiary-fixed: '#002021'
  on-tertiary-fixed-variant: '#004f53'
  background: '#131314'
  on-background: '#e5e2e3'
  surface-variant: '#353436'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: -0.01em
  body-base:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  mono-code:
    fontFamily: JetBrains Mono
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 20px
  gutter: 12px
---

## Brand & Style
This design system centers on the concept of "Cognitive Command." The brand personality is hyper-intelligent, precise, and authoritative, designed for technical operators managing complex AI orchestrations. It utilizes a **Glassmorphic** style layered over a deep matte foundation to create a sense of infinite digital depth. The aesthetic movement is a fusion of **Futuristic Minimalism** and **Node-based Visuals**, where every connection is intentional and every transition is fluid. The goal is to make the user feel like they are "inside the machine," looking through a sleek, data-rich heads-up display.

## Colors
The palette is rooted in a **Deep Matte Black** environment to minimize eye strain during long-duration monitoring. **Royal Purple** serves as the primary action color, signifying the premium and sophisticated nature of the AI logic. **Cobalt Blue** is used for secondary structural elements and navigation. 

Crucially, **Vibrant Neon Highlights** (specifically Neon Green and Electric Cyan) are reserved exclusively for "Active" or "Processing" states, creating an immediate visual "pop" against the dark canvas. Gradients should be used sparingly, primarily as subtle angular strokes on borders or as soft glows behind active node clusters.

## Typography
The system employs a dual-font strategy. **Inter** provides high legibility for the primary UI, utilizing tight letter-spacing and varying weights to establish hierarchy in dense information layouts. **JetBrains Mono** is the functional backbone for all agent output, logs, terminal views, and metadata labels. This distinction ensures the user instantly knows when they are reading "System Interface" versus "Agent Intelligence." All labels for technical metrics should be uppercase JetBrains Mono to reinforce the industrial, data-heavy nature of the platform.

## Layout & Spacing
This design system uses a **Fluid Grid** model with high density. On desktop, it utilizes a 12-column system, but on mobile, it shifts to a single-column stack with tight 20px side margins. The spacing rhythm is based on a 4px baseline, allowing for compact "Information Cards" that maximize screen real estate for monitoring multiple agents. 

Mobile layouts must prioritize the "Thumb Zone" for the **Quick-Action Trigger** interface, which sits in a persistent floating glass container at the bottom of the screen. Layouts are defined by "Panels"—distinct glass containers that can scroll independently.

## Elevation & Depth
Depth is achieved through **Glassmorphism and Tonal Layering** rather than traditional drop shadows. 
- **Level 0 (Base):** Deep Matte Black (#050505).
- **Level 1 (Panels):** Semi-transparent dark grey with a 20px backdrop blur and a 1px solid border (rgba 255, 255, 255, 0.08).
- **Level 2 (Active/Selected):** A subtle inner glow of Royal Purple or Cobalt Blue, creating a "lithium-ion" battery effect.
- **Node Connections:** Use 2px strokes with subtle gradients (Primary to Secondary) to represent the flow of data between agents.

## Shapes
The shape language is **Soft** but disciplined. Primary containers and cards use a 0.5rem (8px) corner radius to feel modern and accessible. Smaller elements like input fields and status tags use a 0.25rem (4px) radius to maintain a technical, "engineered" look. Node-based elements (agent avatars or connection points) use circular (pill) shapes to distinguish them from the structural rectangular UI.

## Components
- **Buttons:** Primary buttons use a solid Royal Purple background with white text. Secondary buttons are "ghost" style with a Cobalt Blue 1px border. The "Trigger Task" button on mobile is a large, high-contrast action item with a subtle neon glow effect.
- **Agent Status Chips:** These feature a monospace label and a "heartbeat" dot. The dot pulses with a Neon Green glow when the agent is 'Thinking' or 'Executing.'
- **Glass Cards:** Used for agent summaries. They must include a `backdrop-filter: blur(12px)` and a top-to-bottom subtle gradient border to simulate light hitting the edge of glass.
- **Activity Logs:** Fixed-height containers using the Monospace font. Rows should alternate with a very subtle background tint (2% white) for readability.
- **Node Connectors:** SVG-based lines connecting agent cards. Use "Active" neon colors for paths currently transmitting data.
- **Inputs:** Dark, recessed fields with a 1px Royal Purple focus ring. Placeholders should be low-contrast Cobalt Blue.