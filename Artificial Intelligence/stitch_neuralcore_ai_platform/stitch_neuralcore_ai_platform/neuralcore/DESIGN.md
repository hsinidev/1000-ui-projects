---
name: NeuralCore
colors:
  surface: '#0c1324'
  surface-dim: '#0c1324'
  surface-bright: '#33394c'
  surface-container-lowest: '#070d1f'
  surface-container-low: '#151b2d'
  surface-container: '#191f31'
  surface-container-high: '#23293c'
  surface-container-highest: '#2e3447'
  on-surface: '#dce1fb'
  on-surface-variant: '#cbc3d7'
  inverse-surface: '#dce1fb'
  inverse-on-surface: '#2a3043'
  outline: '#958ea0'
  outline-variant: '#494454'
  surface-tint: '#d0bcff'
  primary: '#d0bcff'
  on-primary: '#3c0091'
  primary-container: '#a078ff'
  on-primary-container: '#340080'
  inverse-primary: '#6d3bd7'
  secondary: '#4cd7f6'
  on-secondary: '#003640'
  secondary-container: '#03b5d3'
  on-secondary-container: '#00424e'
  tertiary: '#4edea3'
  on-tertiary: '#003824'
  tertiary-container: '#00a572'
  on-tertiary-container: '#00311f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e9ddff'
  primary-fixed-dim: '#d0bcff'
  on-primary-fixed: '#23005c'
  on-primary-fixed-variant: '#5516be'
  secondary-fixed: '#acedff'
  secondary-fixed-dim: '#4cd7f6'
  on-secondary-fixed: '#001f26'
  on-secondary-fixed-variant: '#004e5c'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#0c1324'
  on-background: '#dce1fb'
  surface-variant: '#2e3447'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  code-snippet:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
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
  base: 8px
  container-padding: 32px
  gutter: 24px
  sidebar-width: 280px
---

## Brand & Style

The brand personality is high-precision, hyper-intelligent, and visionary. It targets AI engineers and DevOps architects who require a platform that feels as advanced as the models they deploy. 

The design system utilizes a **Glassmorphic-Futuristic** style. It leans heavily into deep atmospheric depth, using the "Midnight Black" canvas to represent the vastness of data, while "Electric" accents guide the eye toward critical actions and neural pathways. Visual interest is generated through subtle background "neural" animations—fine lines and nodes that pulse with soft luminosity—creating a living, breathing interface that feels like a physical extension of the AI core.

## Colors

This design system is built on a dark-first architecture. 

- **Primary (Electric Violet):** Used for primary actions, active states, and neural node highlights.
- **Secondary (Neon Cyan):** Used for data visualization, progress indicators, and technical accents.
- **Tertiary (Quantum Green):** Reserved for success states and stable deployment status.
- **Surface (Midnight Black):** The foundation of the UI, providing a high-contrast backdrop for glassmorphic layers.
- **Accents:** Use gradients transitioning from Electric Violet to Neon Cyan to represent data flow and active processing.

## Typography

The typography strategy balances technical precision with high readability. **Space Grotesk** provides a geometric, futuristic edge for headings. **Manrope** is used for body copy to ensure long-form technical documentation remains legible and professional. 

For the "Neural" aesthetic, code snippets use **Inter** (monospaced stylistic set) with high-contrast syntax highlighting. Use "Label-Caps" for metadata, table headers, and small technical identifiers to evoke a terminal-like feel.

## Layout & Spacing

The layout follows a **Fixed-Fluid Hybrid grid**. Sidebars and navigation panels are fixed-width glassmorphic containers, while the main workspace/canvas area is fluid to accommodate complex model architectures and data visualizations.

Spacing is governed by an 8px rhythmic scale. Use generous padding within cards (24px+) to prevent technical data from feeling cluttered. Elements should feel like they are floating in space; avoid cramped groupings to maintain the "Deep Space" atmosphere.

## Elevation & Depth

Depth is achieved through **Glassmorphism and Tonal Layering** rather than traditional shadows. 

1. **Base Level:** Midnight Black background.
2. **Surface Level:** Semi-transparent containers (Background blur: 12px, Opacity: 40%) with a 1px inner border of low-opacity white (0.1) to catch "light."
3. **Active Level:** Elements that require focus use a subtle outer glow (Neon Cyan or Electric Violet) with a spread of 15px and very low opacity (0.2).
4. **Interactive Level:** Hovered states increase the backdrop blur intensity and border opacity.

## Shapes

The shape language is **Soft-Technical**. We avoid fully rounded "pill" shapes to maintain a serious, high-tech vibe. Instead, a consistent 4px (Soft) corner radius is applied to code blocks, buttons, and input fields. Larger containers like glassmorphic cards may use 8px (Large) to feel more integrated into the atmospheric background.

## Components

- **Glass Cards:** The primary container. Must have a backdrop-filter blur and a subtle 1px border.
- **Action Buttons:** Primary buttons use a linear gradient (Violet to Cyan) with white text. Ghost buttons use the 1px border logic with an icon.
- **Code Snippets:** High-readability blocks with a darker-than-background base and Electric Violet line-highlighters.
- **Neural Inputs:** Text fields should be "Underline-only" or "Ghost-filled" to keep the UI light. The focus state triggers a neon underline glow.
- **Status Chips:** Small, technical indicators with a glow-dot (e.g., a pulsing Green dot for "Live").
- **Node Connectors:** Use thin 1px lines with 0.3 opacity to connect related data points, mimicking the neural network animations.