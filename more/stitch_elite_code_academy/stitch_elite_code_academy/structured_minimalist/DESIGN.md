---
name: Structured Minimalist
colors:
  surface: '#fbf9fb'
  surface-dim: '#dbd9dc'
  surface-bright: '#fbf9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f6'
  surface-container: '#efedf0'
  surface-container-high: '#e9e7ea'
  surface-container-highest: '#e3e2e5'
  on-surface: '#1b1c1e'
  on-surface-variant: '#434656'
  inverse-surface: '#303033'
  inverse-on-surface: '#f2f0f3'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004ced'
  primary: '#003ec7'
  on-primary: '#ffffff'
  primary-container: '#0052ff'
  on-primary-container: '#dfe3ff'
  inverse-primary: '#b7c4ff'
  secondary: '#495d92'
  on-secondary: '#ffffff'
  secondary-container: '#afc2fe'
  on-secondary-container: '#3b4f83'
  tertiary: '#4b4e51'
  on-tertiary: '#ffffff'
  tertiary-container: '#636669'
  on-tertiary-container: '#e2e4e7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b7c4ff'
  on-primary-fixed: '#001452'
  on-primary-fixed-variant: '#0038b6'
  secondary-fixed: '#dae2ff'
  secondary-fixed-dim: '#b2c5ff'
  on-secondary-fixed: '#001848'
  on-secondary-fixed-variant: '#314578'
  tertiary-fixed: '#e0e3e6'
  tertiary-fixed-dim: '#c4c7ca'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#44474a'
  background: '#fbf9fb'
  on-background: '#1b1c1e'
  surface-variant: '#e3e2e5'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 72px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  code-snippet:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin: 32px
  section-padding: 80px
---

## Brand & Style

This design system is anchored in the concept of "Architectural Clarity." It is designed for a high-end educational environment where the UI acts as a silent, premium gallery for complex information. The brand personality is authoritative, precise, and elite, aimed at professionals who value rigorous structure and high-signal content. 

The style utilizes a **Structured Minimalist** approach, blending the utilitarian logic of Swiss design with the polished aesthetics of modern high-end editorial platforms. It prioritizes objective hierarchy, removing all decorative friction to focus on the "craft" of coding and design. The visual language conveys competence and reliability through perfectly aligned grids and a disciplined use of color.

## Colors

The palette is intentionally restricted to emphasize the Primary Blue (#0052FF) as the sole driver of action and focus. 

- **Primary Blue:** Used for calls to action, progress indicators, and active states. It represents the "energy" of the learning process.
- **Secondary (Navy):** Used for deep-contrast elements or navigational headers to provide a sense of grounded authority.
- **White & Tertiary:** The canvas is #FFFFFF. The Tertiary Gray (#F5F7FA) is used for subtle grouping and sectioning without introducing heavy borders.
- **Neutrals:** The text uses a rich, near-black (#0A0B0D) to ensure maximum readability and a premium feel, avoiding the "washed out" look of standard grays.

## Typography

This design system relies on **Inter** for its systematic, utilitarian precision. The hierarchy is extreme, using significant scale differences to guide the user's eye through educational curricula.

Headlines should be set with tight tracking to feel "locked in" and professional. Body text uses a generous line height (1.6) to ensure long-form technical content is digestible. Labels are occasionally used in uppercase with slight letter-spacing to denote categories or metadata, maintaining an editorial feel similar to high-end magazines.

## Layout & Spacing

The layout is built on a **rigid 12-column fixed grid** with a 24px gutter. All spacing follows a base-8 unit system to ensure mathematical consistency.

- **Generous Whitespace:** Large vertical gaps (80px+) between sections are required to prevent cognitive overload.
- **Alignment:** All elements must snap strictly to the grid. Use "optical alignment" for icons within buttons, but ensure the containers themselves maintain the grid's rhythm.
- **Information Density:** While the overall layout is spacious, content within cards or modules can be dense to reflect the "technical" nature of the product, provided it is contained within clear, structured boundaries.

## Elevation & Depth

To maintain a "Minimalist" profile, depth is conveyed through **tonal layers** and **low-contrast outlines** rather than heavy shadows.

- **Surface Tiers:** Use Tertiary Gray (#F5F7FA) as a "Step Down" for background areas and White (#FFFFFF) as a "Step Up" for cards and interactive components.
- **Shadows:** When necessary (e.g., on a primary hover state), use a single, highly diffused "Ambient Shadow": `0px 10px 30px rgba(0, 0, 0, 0.04)`.
- **Borders:** Use 1px solid borders in a very light gray (#E2E8F0) to define structural boundaries for code editors and input fields. This reinforces the "Architectural" feel.

## Shapes

The shape language is "Soft-Technical." By using a **4px (0.25rem) base radius**, the design system achieves a look that is more approachable than sharp 90-degree corners, but significantly more professional and "engineered" than heavily rounded or pill-shaped systems.

- **Small Components:** Checkboxes and small buttons use the 4px radius.
- **Large Components:** Course cards and modal containers may scale up to 8px (0.5rem) to maintain visual proportion, but should never exceed this.
- **Media:** Video players and image containers should match the component radius to maintain the rigid structural language.

## Components

### Buttons
- **Primary:** Solid #0052FF with white text. 4px radius. No gradient. High-contrast hover (slightly darker blue).
- **Secondary:** Transparent background with a 1px #0A0B0D border.
- **Tertiary/Ghost:** Text only in #0052FF with a 1px bottom border appearing only on hover.

### Cards
- **Course Cards:** White background, 1px light gray border, 4px radius. Use generous padding (24px-32px). Titles should be prominent, with metadata (duration, level) in the "label-bold" style.

### Form Elements
- **Inputs:** 1px #E2E8F0 border, 4px radius. On focus, the border changes to #0052FF with a subtle 2px outer glow of the same color at 10% opacity.
- **Checkboxes:** Square with a 2px radius to look more "technical."

### Content-Specific Components
- **Code Block:** Dark background (#0A0B0D) with syntax highlighting using a refined palette (muted greens, blues, and purples). Font: Inter (or a system Mono if required for character alignment).
- **Progress Bars:** Thin 4px tracks. The background is #F5F7FA, and the fill is the Primary #0052FF.

### Icons
- Use **thin-line icons** (1.5px stroke width). Icons should be monochromatic (Secondary Navy or Primary Blue) and lack any fill or decorative flourishes.