---
name: Corporate Intelligence System
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#c4c6cd'
  on-secondary: '#2d3136'
  secondary-container: '#44474d'
  on-secondary-container: '#b3b5bc'
  tertiary: '#b8c3ff'
  on-tertiary: '#002388'
  tertiary-container: '#00155d'
  on-tertiary-container: '#5d7cff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e0e2e9'
  secondary-fixed-dim: '#c4c6cd'
  on-secondary-fixed: '#191c21'
  on-secondary-fixed-variant: '#44474d'
  tertiary-fixed: '#dde1ff'
  tertiary-fixed-dim: '#b8c3ff'
  on-tertiary-fixed: '#001356'
  on-tertiary-fixed-variant: '#0035be'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-fixed:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-tabular:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  density-high: 8px
  container-max: 1440px
---

## Brand & Style
The brand personality is authoritative, analytical, and uncompromisingly precise. This design system is engineered for high-stakes workforce planning where clarity and strategic oversight are paramount. It avoids decorative flourishes in favor of "Corporate Intelligence"—an aesthetic that signals power through data density and technical sophistication.

The design style is a hybrid of **Corporate Modernism** and **Technical Minimalism**. It prioritizes a "Command Center" feel, utilizing a dark-mode-first approach to reduce eye strain during prolonged analytical sessions. Every pixel serves a functional purpose, with a layout that favors information depth over whitespace, ensuring that executives have a holistic view of operations at a single glance.

## Colors
The palette is rooted in a foundation of **Matte Black (#1A1A1A)** and **Deep Navy (#001F3F)**, establishing a serious, nocturnal environment for data-heavy operations. **Silver (#C0C2C9)** acts as the primary wireframe and secondary text color, providing a metallic, premium contrast that guides the eye without overwhelming it.

**Electric Blue (#2E5BFF)** is reserved strictly for interactive states, critical CTA paths, and data visualization. For workforce metrics, use **Slate Gray** for baseline trends and the Electric Blue for growth or active selections. Subtle linear gradients (Navy to Black) are used on large surface areas to provide a sense of depth and "glass-like" finish to the dashboard panels.

## Typography
This design system utilizes **Inter** exclusively to leverage its exceptional legibility at small sizes and high-density tabular settings. The typographic hierarchy is built for rapid scanning: headings are bold and tightly tracked, while body text uses a slightly more generous line height for readability.

Data points and numerical values should utilize Inter's "tabular figures" OpenType feature to ensure columns of numbers align perfectly in workforce spreadsheets. Use the `label-caps` style for table headers and metadata to create a distinct visual anchor between different data modules.

## Layout & Spacing
The layout follows a **Fixed-Fluid hybrid grid**. On desktop, it employs a strict 12-column system with 16px gutters to maximize horizontal data real estate. The density is intentionally high; use an 8px (2-unit) base spacing for related elements within a card and 16px for separating major modules.

Horizontal density is preferred over vertical scrolling. Navigation is handled via a collapsed sidebar to preserve width for complex data tables. On mobile, the system transitions to a single-column flow, stacking high-level metric cards while hiding granular tables behind "View Detail" drill-downs to maintain usability.

## Elevation & Depth
In this design system, depth is communicated through **tonal layering and crisp borders** rather than soft shadows. Backgrounds are Matte Black, while primary containers (cards, sidebars) use Deep Navy. 

To create separation, use 1px solid borders in Silver at 20% opacity. For active or focused elements, use a 1px border of Electric Blue. Subtle "inner glows" (0px 1px 2px rgba(255, 255, 255, 0.05)) may be applied to buttons and cards to give them a machined, technical feel. Avoid heavy ambient shadows; instead, use slightly lighter Navy tints to indicate an element is "closer" to the user.

## Shapes
The shape language is disciplined and geometric. A **Soft (1)** roundedness level (4px / 0.25rem) is applied to all standard UI components like buttons, input fields, and cards. This slight rounding provides a professional polish without sacrificing the "industrial" feel of a technical tool.

Larger containers, such as modal overlays or main content areas, may use `rounded-lg` (8px) to soften the transition between the application and the background. Interactive elements like toggle switches and status badges utilize pill-shapes to provide immediate visual distinction from data fields.

## Components
- **Buttons:** Primary buttons use a solid Deep Navy background with an Electric Blue border and white text. Secondary buttons are "Ghost" style with Silver borders. All buttons feature a 1px crisp border.
- **Input Fields:** Dark-themed inputs with Matte Black backgrounds and Silver-20 borders. Focus states trigger an Electric Blue border glow.
- **Metric Cards:** Use a subtle linear gradient background (Deep Navy to Black). Include a "Sparkline" visualization in the bottom third of the card using Electric Blue.
- **Data Tables:** Highly condensed. Use alternating row backgrounds (Matte Black and Deep Navy). Header text is Silver, all-caps, and 11px.
- **Status Chips:** Small, rectangular badges with 2px rounding. Use monochromatic Silver for neutral states and Electric Blue for active/important statuses.
- **Workforce Planning Nodes:** Custom components for organizational charts; these use thin, Silver connecting lines and Deep Navy cards with technical metadata labels.