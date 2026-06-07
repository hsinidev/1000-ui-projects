---
name: Focus & Flow
colors:
  surface: '#f7f9fd'
  surface-dim: '#d8dade'
  surface-bright: '#f7f9fd'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f8'
  surface-container: '#eceef2'
  surface-container-high: '#e6e8ec'
  surface-container-highest: '#e0e2e6'
  on-surface: '#191c1f'
  on-surface-variant: '#42493e'
  inverse-surface: '#2d3134'
  inverse-on-surface: '#eff1f5'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#526351'
  on-secondary: '#ffffff'
  secondary-container: '#d2e5ce'
  on-secondary-container: '#566755'
  tertiary: '#60233e'
  on-tertiary: '#ffffff'
  tertiary-container: '#7c3a55'
  on-tertiary-container: '#ffaac8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#d5e8d1'
  secondary-fixed-dim: '#b9ccb5'
  on-secondary-fixed: '#101f11'
  on-secondary-fixed-variant: '#3a4b3a'
  tertiary-fixed: '#ffd9e4'
  tertiary-fixed-dim: '#ffb0cc'
  on-tertiary-fixed: '#3b0520'
  on-tertiary-fixed-variant: '#71314c'
  background: '#f7f9fd'
  on-background: '#191c1f'
  surface-variant: '#e0e2e6'
typography:
  h1:
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.02em
  h2:
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.75'
    letterSpacing: '0'
  body-md:
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.75'
    letterSpacing: '0'
  label:
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1120px
  gutter: 32px
  section-gap: 80px
  element-gap: 24px
---

## Brand & Style

The brand personality is grounding, reliable, and deeply empathetic to the cognitive load of the user. This design system prioritizes "High-Structure Minimalism"—a style that rejects the chaos of modern web design in favor of a quiet, intentional environment. The emotional response should be one of immediate relief; the UI acts as an external executive function aid rather than another source of noise. 

The aesthetic is characterized by a "Clear Border" approach, utilizing structural lines to define relationships between elements rather than using depth, motion, or vibrant gradients. This creates a predictable and safe digital space where users can focus on their coaching goals without distraction.

## Colors

The palette is anchored by a deep **Forest Green** as the primary action color. This choice provides a sense of growth and stability while being significantly more soothing than high-vibrancy blues or reds. 

The background uses a warm **Off-White** (Ivory-toned) to eliminate the harsh glare of pure white screens, which can contribute to sensory overload. Secondary elements utilize **Sage Neutrals** and soft grays to create subtle distinctions between layout sections. Contrast is strictly maintained for accessibility, ensuring that all functional elements are easily identifiable without the use of "loud" colors.

## Typography

This design system utilizes **Inter** for its systematic clarity and excellent legibility at all sizes. To accommodate the cognitive needs of users with ADHD, the typography employs a "generous leading" strategy. Line heights are set significantly wider (1.75x for body text) than standard UI conventions to prevent the "wall of text" effect and aid in tracking.

Hierarchy is enforced through distinct weight shifts rather than color changes. Headlines are concise and bold, while body text is kept at a comfortable, slightly larger-than-standard 18px size for primary reading tasks to reduce visual strain.

## Layout & Spacing

The layout philosophy centers on a **Fixed Grid** model. Content is contained within a centralized column to prevent eye-scanning fatigue on wide monitors. A 12-column grid is used internally, but margins are intentionally exaggerated to create a sense of "air."

A strict 8px spacing rhythm ensures that elements feel organized and deliberate. The use of "empty space" is treated as a functional component of the design, used to separate disparate ideas and reduce the feeling of clutter. No two modules should feel crowded together; the "Section Gap" variable is used aggressively to ensure clear mental separation between different coaching tasks.

## Elevation & Depth

This design system deliberately avoids shadows to minimize visual complexity. Instead of using Z-axis depth (elevation), it uses **Bold Borders** and **Tonal Layers** to define hierarchy.

1. **Surface 1 (Base):** The Off-White background.
2. **Surface 2 (Containers):** Defined by a 1px solid border in a soft neutral or a slightly darker off-white fill.
3. **Active State:** Indicated by an increase in border thickness (from 1px to 2px) using the Primary Forest Green, rather than a shadow or glow.

This flat, structured approach ensures that the interface feels solid and "grounded" to the screen.

## Shapes

The shape language is "Soft-Geometric." A consistent **0.25rem (4px)** corner radius is applied to buttons, input fields, and cards. This provides a subtle softening of the interface—making it feel approachable and modern—without losing the "High-Structure" feel of sharp, organized boxes. Larger components, like progress cards, may use a 0.5rem radius to denote them as primary containers.

## Components

### Buttons
Primary buttons are solid Forest Green with white text. Secondary buttons use a Forest Green border with no fill. All buttons have clear, high-contrast hover states that change the border thickness or fill color subtly, without animation.

### Vertical Progress Steppers
The core navigation for coaching sessions. These are positioned on the left side of content containers. Each step is connected by a solid 2px line, providing a visual "path" that anchors the user's progress through the portal.

### Input Fields
Inputs use a light neutral background and a 1px border. On focus, the border changes to Forest Green with a 2px width. Error states use a high-contrast muted terracotta, avoiding bright "emergency" reds.

### Cards
Cards are the primary container for information. They feature 1px solid borders and no box-shadow. Header areas within cards are separated by a horizontal rule to maintain the "organized" look.

### Interaction Rules
- **No Motion:** No auto-playing videos, flashing icons, or sliding transitions. Transitions should be instant or a very fast (100ms) fade.
- **Micro-Copy:** Every component includes space for "helper text" to reduce ambiguity and "task paralysis."