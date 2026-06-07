---
name: Organic Professionalism
colors:
  surface: '#fbf8ff'
  surface-dim: '#d5d8f9'
  surface-bright: '#fbf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f2ff'
  surface-container: '#ececff'
  surface-container-high: '#e5e6ff'
  surface-container-highest: '#dee0ff'
  on-surface: '#161a32'
  on-surface-variant: '#414844'
  inverse-surface: '#2b2f48'
  inverse-on-surface: '#f0efff'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#7f5539'
  on-secondary: '#ffffff'
  secondary-container: '#fec6a3'
  on-secondary-container: '#795035'
  tertiary: '#401b1b'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a302f'
  on-tertiary-container: '#d29895'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffdcc7'
  secondary-fixed-dim: '#f2bb98'
  on-secondary-fixed: '#301401'
  on-secondary-fixed-variant: '#643e24'
  tertiary-fixed: '#ffdad8'
  tertiary-fixed-dim: '#f5b7b4'
  on-tertiary-fixed: '#331111'
  on-tertiary-fixed-variant: '#673a39'
  background: '#fbf8ff'
  on-background: '#161a32'
  surface-variant: '#dee0ff'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  h3:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  button:
    fontFamily: manrope
    fontSize: 14px
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
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The design system is rooted in the concept of "Editorial Ecology." It bridges the gap between high-level corporate accountability and environmental stewardship. The brand personality is authoritative yet approachable, aiming to evoke feelings of growth, stability, and transparency. 

The visual style follows a **Modern Minimalism** approach with **Tactile** influences. It prioritizes clarity through generous whitespace ("breathability") and replaces rigid geometric perfection with organic, asymmetric touches that mimic natural forms. The interface should feel like a premium sustainability report—clean, structured, and thoughtfully curated.

## Colors

The palette is derived from natural landscapes to reinforce the ESG mission. 
- **Forest Green (Primary):** Used for primary actions, navigation headers, and core brand moments. It represents depth and institutional strength.
- **Off-White (Canvas):** A warm, paper-like foundation that reduces the harshness of pure white, making long-form data entry and reading more comfortable.
- **Earthy Brown (Accent):** Used for structural elements like borders and secondary UI controls to ground the lighter greens.
- **Sage/Mint & Terracotta:** Functional colors for data visualization. Sage indicates compliance and positive trends, while Terracotta provides a muted, non-alarmist warning for governance risks.

## Typography

This design system utilizes a sophisticated typographic pairing to achieve an "editorial" feel. 
- **Newsreader** is the primary serif for all high-level headings. Its literary heritage suggests prestige and deep-rooted knowledge.
- **Manrope** is the workhorse sans-serif for body text, data points, and UI labels. Its geometric but slightly softened terminals complement the organic theme while maintaining high legibility in complex ESG data tables.

## Layout & Spacing

The layout utilizes a **Fixed Grid** system centered on the canvas to maintain an organized, report-like structure. 
- **Grid:** A 12-column grid with a 24px gutter.
- **Rhythm:** An 8px linear scale is used for component internal spacing, while larger 40px+ gaps are used between major sections to create "breathable" whitespace.
- **Alignment:** Content is often grouped into cards that align with the grid, but decorative "eco-elements" may occasionally break the grid to create a more dynamic, organic feel.

## Elevation & Depth

Hierarchy in the design system is achieved through **Tonal Layering** and **Ambient Shadows**.
- **Surface Tiers:** The main background is Off-White. Content cards use a pure white (#FFFFFF) to pop forward.
- **Shadows:** Shadows are highly diffused and tinted with the Primary Forest Green (e.g., `rgba(27, 67, 50, 0.08)`) to avoid the "dirty" look of grey shadows. 
- **Depth:** Elements should feel like they are resting gently on a surface rather than floating high above it. Only active dropdowns or modals should use higher elevation blurs.

## Shapes

The shape language is the most distinctive aspect of this design system.
- **Leaf-like Radii:** Instead of uniform corners, primary containers and buttons use an asymmetric "leaf" radius—for example, a `16px` radius on the Top-Left and Bottom-Right, with a `4px` radius on the others.
- **Pills:** Interactive elements like chips, tags, and progress bar containers use full pill rounding to suggest smoothness and flow.
- **Borders:** Use thin, 1px Earthy Brown borders at 20% opacity for subtle definition without creating visual clutter.

## Components

- **Buttons:** Primary buttons are Forest Green with white Manrope text and the signature "leaf" asymmetric corners. Secondary buttons use an Earthy Brown outline.
- **Data Cards:** Pure white backgrounds with the soft green-tinted shadow. Headers within cards should use the Newsreader serif font.
- **Progress Bars:** The outer container is a soft Sage pill. The inner progress fill is a vibrant Forest Green, creating a natural monochromatic growth metaphor.
- **Sustainability Score:** A semi-circle gauge using a gradient that transitions from Terracotta (low) to Forest Green (high). The needle or indicator should be Earthy Brown.
- **Compliance Badges:** Digital wax-seal style icons. They feature a circular "scalloped" edge or a leaf-shaped shield, using Sage for "Certified" status.
- **Input Fields:** Soft Off-White backgrounds with an Earthy Brown bottom-border only, providing a clean, "form-on-paper" aesthetic.