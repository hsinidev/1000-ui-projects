---
name: Institutional Alpha
colors:
  surface: '#f9f9fc'
  surface-dim: '#dadadc'
  surface-bright: '#f9f9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f6'
  surface-container: '#eeeef0'
  surface-container-high: '#e8e8ea'
  surface-container-highest: '#e2e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#414943'
  inverse-surface: '#2f3133'
  inverse-on-surface: '#f0f0f3'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3b6751'
  primary: '#001b0f'
  on-primary: '#ffffff'
  primary-container: '#013220'
  on-primary-container: '#6f9c84'
  inverse-primary: '#a2d1b7'
  secondary: '#50606f'
  on-secondary: '#ffffff'
  secondary-container: '#d1e1f4'
  on-secondary-container: '#556474'
  tertiary: '#151717'
  on-tertiary: '#ffffff'
  tertiary-container: '#292b2b'
  on-tertiary-container: '#919292'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bdedd2'
  primary-fixed-dim: '#a2d1b7'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#234f3b'
  secondary-fixed: '#d4e4f6'
  secondary-fixed-dim: '#b8c8da'
  on-secondary-fixed: '#0d1d2a'
  on-secondary-fixed-variant: '#394857'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e2e2e5'
typography:
  display-xl:
    fontFamily: manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 24px
  gutter: 16px
  card-padding: 20px
  section-gap: 40px
---

## Brand & Style

This design system is engineered for high-stakes venture capital environments where clarity, speed, and institutional trust are paramount. The personality is "Quiet Authority"—it avoids flashy trends in favor of a sophisticated, durable aesthetic that mirrors the stability of a top-tier fund.

The visual style merges **Minimalism** with strategic **Glassmorphism**. By using semi-transparent layers and subtle backdrop blurs, the interface maintains a sense of depth and modernism without sacrificing the legibility required for complex data density. This approach creates a "digital command center" feel, where information feels organized behind a premium lens.

## Colors

The palette is rooted in **Deep Forest Green (#013220)**, utilized primarily for navigation, primary actions, and brand reinforcement to evoke growth and heritage. **Slate (#708090)** serves as the functional bridge, used for secondary icons, borders, and metadata to reduce visual noise.

The canvas is built on **Off-White (#F5F5F5)**, providing a warmer, more sophisticated alternative to pure white that reduces eye strain during long periods of pipeline review. Semantic colors for status indicators (Deal Won, Pass, Due Diligence) should be slightly desaturated to maintain the professional tone.

## Typography

The typography system uses a dual-font approach to balance character with utility. **Manrope** is used for headlines and display text, offering a modern, geometric structure that feels balanced and premium. Its slightly condensed nature allows for impactful headings in dashboard environments.

**Inter** is utilized for all body copy, data tables, and input fields. Its high x-height and exceptional legibility make it the industry standard for financial SaaS applications. Labels utilize a medium weight with slight letter spacing to ensure they are easily scannable within dense Kanban cards and metric widgets.

## Layout & Spacing

The design system employs a **Fluid Grid** model with a 12-column structure for desktop dashboards. To handle the complexity of deal-flow, the layout prioritizes horizontal real estate, allowing the Kanban board to scroll smoothly while keeping global metrics pinned.

The spacing rhythm is based on an **8px linear scale**. Tight padding (8px - 12px) is reserved for data-heavy lists, while generous padding (24px - 32px) is used for "Deep Dive" deal views to provide mental breathing room during analysis.

## Elevation & Depth

Depth is achieved through **Glassmorphism** rather than traditional heavy shadows. Surfaces are layered using "Glass Containers":
1.  **Base Layer:** Off-White background.
2.  **Mid Layer (Cards):** White background at 70% opacity with a 12px backdrop-blur and a 1px solid border in Slate at 20% opacity.
3.  **High Layer (Modals/Popovers):** White background at 90% opacity with a 20px backdrop-blur and a soft, ambient shadow (0px 10px 30px rgba(1, 50, 32, 0.08)).

This stacking logic ensures that even when multiple windows or deal-cards overlap, the hierarchy remains distinct and the "Forest Green" brand color occasionally peeks through the translucency.

## Shapes

The shape language is **Soft (0.25rem / 4px)**. This choice leans toward the "Institutional" side of the aesthetic—sharp enough to feel precise and serious, but with just enough rounding to appear modern and accessible on high-resolution displays. Large containers like Kanban columns or Dashboard sections may use the `rounded-lg` (8px) variant to better frame the glassmorphic effects.

## Components

**Kanban Boards**
Deal cards should utilize the glassmorphic style with a left-accent border colored by "Deal Stage." Use `label-sm` for tags (e.g., "SaaS", "Series A").

**Metric Dashboards**
Value-at-risk and IRR metrics should use `display-xl` for the primary number, paired with a small sparkline graph. Containers should have a subtle inner-glow to simulate light catching the edge of a glass pane.

**Voting Interfaces**
For investment committees, use "Sentiment Sliders" and "Binary Vote" buttons. Buttons should be high-contrast: Primary (Forest Green), Secondary (Outline Slate).

**Mobile-First Utility Buttons**
Floating Action Buttons (FABs) are used for "Quick Note" or "Add Deal." These should be circular, Deep Forest Green, with a white icon, positioned in the bottom-right for thumb-accessibility.

**Input Fields**
Standard fields use a 1px Slate border. On focus, the border transitions to Forest Green with a 2px outer "aura" of the same color at 10% opacity.