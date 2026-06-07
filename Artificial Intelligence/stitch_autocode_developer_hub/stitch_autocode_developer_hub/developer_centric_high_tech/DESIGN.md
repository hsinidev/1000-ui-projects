---
name: Developer-Centric High-Tech
colors:
  surface: '#131314'
  surface-dim: '#131314'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0f'
  surface-container-low: '#1c1b1c'
  surface-container: '#201f20'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353435'
  on-surface: '#e5e2e2'
  on-surface-variant: '#c6c6cb'
  inverse-surface: '#e5e2e2'
  inverse-on-surface: '#313031'
  outline: '#8f9095'
  outline-variant: '#45474b'
  surface-tint: '#c3c6cf'
  primary: '#c3c6cf'
  on-primary: '#2d3137'
  primary-container: '#0a0e14'
  on-primary-container: '#787b83'
  inverse-primary: '#5b5e66'
  secondary: '#43ed9c'
  on-secondary: '#003920'
  secondary-container: '#01d083'
  on-secondary-container: '#005231'
  tertiary: '#c2c7d0'
  on-tertiary: '#2c3138'
  tertiary-container: '#090e15'
  on-tertiary-container: '#767b84'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2eb'
  primary-fixed-dim: '#c3c6cf'
  on-primary-fixed: '#181c22'
  on-primary-fixed-variant: '#43474e'
  secondary-fixed: '#59feac'
  secondary-fixed-dim: '#31e192'
  on-secondary-fixed: '#002111'
  on-secondary-fixed-variant: '#005230'
  tertiary-fixed: '#dee2ec'
  tertiary-fixed-dim: '#c2c7d0'
  on-tertiary-fixed: '#171c23'
  on-tertiary-fixed-variant: '#42474f'
  background: '#131314'
  on-background: '#e5e2e2'
  surface-variant: '#353435'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  code-display:
    fontFamily: monospace
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.7'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 16px
  sidebar_width: 260px
---

## Brand & Style
The brand personality of this design system is "The Expert Co-Pilot." It is engineered to feel like a high-performance terminal—precise, reliable, and hyper-focused. It targets a sophisticated developer audience that values speed and technical density over decorative fluff. 

The UI style is a fusion of **Modern Minimalism** and **Technical Brutalism**. It utilizes sharp, geometric components and a rigid grid to evoke the feeling of a code editor. To differentiate the product from a static text editor, subtle **Neon-Cyberpunk** elements are introduced specifically for AI-driven features, using glows and syntax-highlighted accents to signify "intelligence" within the machine. The emotional response should be one of complete control, low cognitive load, and futuristic efficiency.

## Colors
The palette is rooted in the "Code Editor" aesthetic. **Midnight Blue** serves as the infinite canvas, providing deep contrast for technical work. **Graphite** is the structural color, used for UI surfaces, dividers, and panel backgrounds to create a clear hierarchy of workspace areas.

**Neon Mint** is the high-energy accent reserved for calls to action, success states, and indicating where the AI is active. To reinforce the developer focus, a secondary palette of syntax-inspired colors (Blue, Purple, Orange) is used for semantic meaning, such as status indicators, variable types, or git-diff states. All backgrounds must prioritize the dark mode environment to reduce eye strain during long coding sessions.

## Typography
Typography is split into two functional roles. For technical content, headings, and data-heavy labels, **Space Grotesk** is used to provide a futuristic, geometric feel that mimics monospace logic but remains highly readable at scale. 

For documentation, long-form articles, and educational content, **Inter** is employed. Its neutral, systematic nature ensures that complex instructions are legible without competing with the code itself. Real code snippets and technical parameters must always fall back to a system monospace font to maintain the "IDE" aesthetic. Letter spacing is tightened on large headings for a "dense" tech look and opened on labels for clarity.

## Layout & Spacing
The layout philosophy follows a **Fixed-Pane Grid**, mirroring the structure of an Integrated Development Environment (IDE). The interface is divided into functional zones: a persistent sidebar for navigation, a primary central "editor" area for main tasks, and a right-side "inspector" or "hub" for AI suggestions.

A strict 8px base unit governs all spacing to ensure mathematical precision. Margin and padding values should be kept consistent across panels to create a sense of rigid structural integrity. Gutters are kept narrow (16px) to maximize screen real estate, emphasizing "technical density" over airy whitespace.

## Elevation & Depth
In this design system, depth is conveyed through **Tonal Layers** rather than traditional shadows. Surfaces closer to the user are lighter in tone (Graphite) compared to the base (Midnight Blue). 

To indicate AI activity or interactive focus, **Low-Contrast Outlines** and **Inner Glows** are used. A subtle, 1px Neon Mint border with a soft outer bloom (2-4px) indicates "active" or "AI-processed" states. This creates a digital, luminescent feel that avoids the physical metaphors of skeuomorphism, keeping the interface firmly in the world of software.

## Shapes
This design system uses a **Sharp (0px)** roundedness model. Every component—from buttons and input fields to cards and modals—features 90-degree angles. This geometric rigidity reinforces the brand's focus on precision and engineering. There are no "soft" elements; the architecture is intended to feel constructed and industrial. Any visual separation should be achieved through 1px borders or subtle tonal shifts rather than rounded corners.

## Components
- **Buttons:** Primary buttons are solid Neon Mint with Midnight Blue text. Secondary buttons are 1px Graphite outlines with Neon Mint text. All buttons have 0px corner radius and high-contrast hover states.
- **Input Fields:** Styled like a terminal input. Graphite background, 1px border. When focused, the border glows Neon Mint.
- **Chips/Badges:** Small, uppercase labels with a background color reflecting syntax highlighting (e.g., a "Function" chip in Purple). 
- **Command Palette:** A centered, floating modal with high technical density, featuring a search input and a list of keyboard-shortcut-mapped actions.
- **Code Blocks:** Styled with a distinct "Graphite" background and a 1px vertical "accent bar" on the left in Neon Mint to denote AI-generated code.
- **Panels/Cards:** Flat surfaces with no shadows, separated by 1px Graphite borders. Use "Label-Caps" typography for header sections within panels.
- **Progress Indicators:** Linear, pixel-thin bars that use the Neon Mint color to show AI processing or loading states.