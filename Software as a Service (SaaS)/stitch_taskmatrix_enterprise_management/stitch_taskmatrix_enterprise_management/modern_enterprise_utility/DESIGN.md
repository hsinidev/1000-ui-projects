---
name: Modern Enterprise Utility
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#47464f'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#787680'
  outline-variant: '#c8c5d0'
  surface-tint: '#5b598c'
  primary: '#070235'
  on-primary: '#ffffff'
  primary-container: '#1e1b4b'
  on-primary-container: '#8683ba'
  inverse-primary: '#c4c1fb'
  secondary: '#006c49'
  on-secondary: '#ffffff'
  secondary-container: '#6cf8bb'
  on-secondary-container: '#00714d'
  tertiary: '#02003c'
  on-tertiary: '#ffffff'
  tertiary-container: '#09007e'
  on-tertiary-container: '#767aff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e3dfff'
  primary-fixed-dim: '#c4c1fb'
  on-primary-fixed: '#181445'
  on-primary-fixed-variant: '#444173'
  secondary-fixed: '#6ffbbe'
  secondary-fixed-dim: '#4edea3'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#e1e0ff'
  tertiary-fixed-dim: '#c0c1ff'
  on-tertiary-fixed: '#07006c'
  on-tertiary-fixed-variant: '#2f2ebe'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: 24px
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  body-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '400'
    lineHeight: 18px
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  mono-num:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  gutter: 16px
  margin: 24px
---

## Brand & Style

This design system is built for the high-stakes environment of enterprise project management. The brand personality is **authoritative, precise, and facilitating**. It balances the weight of complex data with the light touch of modern collaboration. 

The visual style follows a **Corporate Modern** approach. It avoids unnecessary ornamentation, focusing instead on high-utility density and structured clarity. By utilizing expansive white space and a restricted color palette, the interface reduces cognitive load, allowing users to focus on critical path decision-making and resource optimization. The emotional response should be one of "controlled efficiency"—users should feel that the system is powerful enough to handle massive data sets without becoming overwhelming.

## Colors

The palette is anchored by **Deep Indigo**, used for primary navigation, headings, and heavy UI elements to establish a foundation of stability and professionalism. **Mint** serves as the high-impact accent, reserved exclusively for progress indicators, "on-track" status updates, and primary action completions.

The background is kept a pristine **White** to ensure maximum contrast and legibility. A scale of cool grays is utilized for secondary information and borders to maintain a clean, architectural structure. Subtle variations of Indigo (tints) are used for hover states and selected items to maintain brand cohesion without the vibration of high-saturation colors.

## Typography

The typography system relies on **Inter**, a typeface designed for computer screens and complex UIs. It is chosen for its exceptional tall x-height and tabular figure support, which is critical for the numerical density of Gantt charts and resource graphs.

Hierarchy is established primarily through weight and size rather than color. Tabular numbers are forced for all data-heavy views to ensure vertical alignment in columns. Headings use tighter letter spacing for a modern, "locked-in" appearance, while labels utilize uppercase tracking to differentiate meta-data from primary content.

## Layout & Spacing

This design system employs a **12-column fluid grid** for dashboard views and a **fixed-sidebar/fluid-content** model for primary application views. The system is built on a **4px baseline grid** to ensure mathematical consistency across all components.

Information density is categorized into three levels:
1. **Compact:** (8px padding) for data tables and Gantt chart rows.
2. **Default:** (16px padding) for task cards and side panels.
3. **Spacious:** (24px padding) for empty states and onboarding flows.

Margins and gutters are kept rigid to emphasize the "Robust" feel of the system, ensuring that elements feel structurally sound.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Low-contrast Shadows**. The background layer is the lowest (White), while the primary content area sits on a subtle gray surface (Surface 1). 

Components that require user interaction, such as Task Cards and Popovers, utilize "Ambient Shadows"—diffused, low-opacity (8-12%) shadows with a slight Indigo tint. This creates a soft lift without breaking the clean, flat aesthetic. Borders are used as the primary separator for static elements, while shadows are strictly reserved for elevated, interactive, or floating elements.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding provides a modern touch that takes the edge off the "institutional" feel of enterprise software without sacrificing the "Robust" and professional look. 

Buttons and input fields use the standard 4px radius. Larger containers, like cards or modals, may use a 8px (rounded-lg) radius to create a softer visual nested hierarchy. Progress bars and workload indicators use slightly more rounded caps to appear more approachable and distinct from structural containers.

## Components

### Buttons & Inputs
Buttons use solid Deep Indigo for primary actions and Ghost styles (Indigo border) for secondary actions. Input fields use a 1px Slate-200 border, turning Indigo on focus with a subtle glow.

### Task Cards
Task cards feature a clear hierarchy: Title (Medium weight), Metadata (Small Body), and a bottom-aligned bar for subtask progress indicators. Subtask status is represented by micro-pips (Indigo for pending, Mint for complete).

### Enterprise Gantt Charts
Gantt bars use Deep Indigo for active phases and light Indigo tints for planned/baseline phases. Critical path connections are rendered with 1px solid Indigo lines with directional arrows. Milestones are represented by diamond shapes.

### Workload Bars & Resource Graphs
Workload bars use a split-fill technique: the background is a neutral gray, the "used" capacity is Mint, and "over-capacity" is indicated by a subtle pattern overlay rather than a jarring red, maintaining the professional color balance.

### Additional Components
- **Status Chips:** Small, semi-rounded badges using high-contrast text on low-saturation backgrounds (e.g., Mint text on soft Mint tint).
- **Resource Avatars:** Circular avatars with a 2px white border, often grouped in "stacks" to show project members.
- **Tree Lists:** Hierarchical lists for WBS (Work Breakdown Structure) using indented 1px vertical guidelines.