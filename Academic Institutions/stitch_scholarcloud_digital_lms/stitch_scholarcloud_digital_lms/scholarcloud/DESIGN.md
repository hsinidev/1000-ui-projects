---
name: ScholarCloud
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#3e4850'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#6e7881'
  outline-variant: '#bec8d2'
  surface-tint: '#006591'
  primary: '#006591'
  on-primary: '#ffffff'
  primary-container: '#0ea5e9'
  on-primary-container: '#003751'
  inverse-primary: '#89ceff'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fd'
  on-secondary-container: '#57657b'
  tertiary: '#8a5100'
  on-tertiary: '#ffffff'
  tertiary-container: '#de8712'
  on-tertiary-container: '#4d2b00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#89ceff'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#004c6e'
  secondary-fixed: '#d5e3fd'
  secondary-fixed-dim: '#b9c7e0'
  on-secondary-fixed: '#0d1c2f'
  on-secondary-fixed-variant: '#3a485c'
  tertiary-fixed: '#ffdcbd'
  tertiary-fixed-dim: '#ffb86e'
  on-tertiary-fixed: '#2c1600'
  on-tertiary-fixed-variant: '#693c00'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
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
  sm: 8px
  md: 16px
  lg: 24px
  xl: 32px
  container-margin: 16px
  gutter: 16px
---

## Brand & Style

The brand personality for this design system is centered on **academic empowerment and cognitive clarity**. It is designed for students and educators who require a high-utility environment that minimizes distractions while maximizing information density. The emotional response should be one of "effortless productivity"—the interface feels like a high-precision tool that organizes complex curricula into manageable, actionable steps.

The visual style is **Corporate / Modern**, leaning heavily into **Minimalism**. It prioritizes functional aesthetics over decorative elements. By utilizing high-quality typography and strategic whitespace, the design system ensures that "data-rich" never feels "cluttered." The interface feels "alive" through the use of dynamic progress-ring visualizations, providing immediate, satisfying feedback on user achievement.

## Colors

The palette is anchored by a vibrant **Primary Sky Blue**, chosen to evoke focus and digital-native intelligence. This is balanced against a deep **Slate** for secondary elements and primary text, ensuring high legibility and a grounded, professional feel.

- **Primary:** Used for actionable elements, progress indicators, and active states.
- **Secondary/Text:** Used for body copy and structural icons to maintain a sophisticated contrast.
- **Background:** Pure White is the primary canvas, supplemented by a very light slate neutral for card backgrounds and section grouping.
- **Semantic Accents:** Success emeralds are used sparingly for completion states within the progress-ring visualizations.

## Typography

This design system utilizes **Inter** exclusively to leverage its exceptional legibility and systematic weight distribution. The typography hierarchy is structured to guide the eye through dense course material without fatigue.

- **Headlines:** Set with slight negative letter-spacing and semi-bold weights to command attention.
- **Body:** Generous line-heights are applied to ensure long-form educational content is readable.
- **Labels:** Used for metadata and UI controls, employing medium-to-bold weights at smaller sizes to maintain clarity.

## Layout & Spacing

The design system employs a **Fluid Grid** model with a mobile-first philosophy. Layouts are built on an 8px base unit, ensuring consistent vertical and horizontal rhythm across all viewports.

- **Mobile (Default):** A single-column layout with 16px side margins. Touch targets for buttons and links are strictly a minimum of 44px in height.
- **Desktop/Tablet:** Content expands into a 12-column grid. Side margins increase to 32px or greater to allow for a centered "focus mode" reading experience.
- **Rhythm:** Components use 16px (md) padding as a standard, with 8px (sm) reserved for tighter groups of data or controls.

## Elevation & Depth

To maintain the "Precise & Productive" aesthetic, depth is conveyed through **Ambient Shadows** and **Tonal Layers**. We avoid heavy, dark shadows in favor of light, diffused elevation that suggests layers of paper or digital "sheets."

- **Level 0 (Background):** Pure White (#ffffff).
- **Level 1 (Cards/Surface):** White surface with a 1px border (#e2e8f0) or an extremely soft shadow (0px 4px 6px -1px rgba(51, 65, 85, 0.05)).
- **Level 2 (Popovers/Modals):** High-diffusion shadows with a subtle Slate tint to separate interactive overlays from the main workspace.
- **Interactive Depth:** Buttons use a subtle inner-shadow on "active/pressed" states to provide tactile confirmation.

## Shapes

The shape language of this design system is **Rounded**, striking a balance between modern friendliness and professional rigidity. 

- **Standard Elements:** Buttons, input fields, and small cards utilize a 0.5rem (8px) radius.
- **Large Containers:** Dashboard widgets and main content areas utilize a 1rem (16px) radius to soften the larger visual footprint.
- **Progress Rings:** These should be perfectly circular (rounded-full) with a stroke width that scales proportionally to the container size (typically 10-15% of the diameter).

## Components

### Progress-Ring Visualizations
The signature element of this design system. Rings should use the Primary Sky Blue for the "progress" stroke and a very light Slate (#f1f5f9) for the "track." Completion status (100%) may transition to Emerald Green.

### Buttons
- **Primary:** Sky Blue background, white text. No gradient. 8px corner radius.
- **Secondary:** Transparent background with a Slate border (#cbd5e1) and Slate text.
- **Shadows:** Subtle "bottom-heavy" shadow to give a slight 3D lift.

### Cards
Cards are the primary container for course modules and data blocks. They feature a 1px Slate border and 16px of internal padding. Titles should always be H3 or Body-MD (Semi-bold).

### Input Fields
Inputs must be highly visible with a 1px border. On focus, the border transitions to Primary Sky Blue with a 2px outer "glow" or ring using 20% opacity of the primary color.

### Chips & Badges
Used for tagging categories (e.g., "Math," "Due Today"). These use the Pill-shaped (rounded-full) style with a 12px label-sm font size.

### Lists & Data Rows
For data-rich environments, use horizontal dividers (1px, #f1f5f9). High contrast between the primary label and the secondary metadata is essential for rapid scanning.