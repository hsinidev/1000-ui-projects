---
name: Bio-Paws
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#454652'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#767683'
  outline-variant: '#c6c5d4'
  surface-tint: '#4c56af'
  primary: '#000666'
  on-primary: '#ffffff'
  primary-container: '#1a237e'
  on-primary-container: '#8690ee'
  inverse-primary: '#bdc2ff'
  secondary: '#3b6663'
  on-secondary: '#ffffff'
  secondary-container: '#bbe8e4'
  on-secondary-container: '#3f6a67'
  tertiary: '#002019'
  on-tertiary: '#ffffff'
  tertiary-container: '#00372d'
  on-tertiary-container: '#65a393'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e0e0ff'
  primary-fixed-dim: '#bdc2ff'
  on-primary-fixed: '#000767'
  on-primary-fixed-variant: '#343d96'
  secondary-fixed: '#beebe7'
  secondary-fixed-dim: '#a2cfcb'
  on-secondary-fixed: '#00201e'
  on-secondary-fixed-variant: '#224e4b'
  tertiary-fixed: '#afefdd'
  tertiary-fixed-dim: '#94d3c1'
  on-tertiary-fixed: '#00201a'
  on-tertiary-fixed-variant: '#065043'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Montserrat
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Montserrat
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Montserrat
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: '0'
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
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.08em
  data-mono:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: -0.01em
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
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style
The design system is engineered to bridge the gap between complex genetic science and the emotional bond of pet ownership. The brand personality is **authoritative, clinical, and visionary**, evoking the feeling of a high-end laboratory that is accessible to the modern consumer.

The style is **Minimalist High-Contrast**. It relies on the tension between the Deep Indigo (stability/authority) and Mint (vitality/health). Visual layouts should prioritize white space to suggest cleanliness and precision. A subtle "Double-Helix" motif is used as a graphic watermark or a background pattern, reinforcing the DNA-focused mission without cluttering the interface. The aesthetic is "Lab-to-Life"—utilizing medical-grade data density balanced with human-centric warmth.

## Colors
This design system utilizes a high-contrast palette to ensure legibility and a sense of medical professionalism. 

*   **Deep Indigo (#1A237E):** Used for primary actions, headings, and core branding. It represents the "Bio" and the scientific rigor.
*   **Mint (#B2DFDB):** Used for accents, secondary buttons, success states, and highlight areas. It represents "Paws," health, and longevity.
*   **Crisp White (#FFFFFF):** The primary canvas color to maintain a sterile, clinical environment.
*   **Subtle Neutrals:** A cool-toned light grey is used for background fills to separate content modules without breaking the minimalist aesthetic.

## Typography
The typography strategy prioritizes data legibility and structural hierarchy. 

**Montserrat** is used for headlines to provide a bold, geometric presence that feels contemporary and tech-forward. **Inter** is the workhorse for all body text, data points, and labels, selected for its exceptional readability in data-heavy medical reports. 

Use the "Label-Caps" style for section headers and small metadata to create a "tabbed folder" or "medical chart" feel. For genomic sequences or technical data, ensure Inter’s medium weight is used to maintain clarity against the Deep Indigo background.

## Layout & Spacing
The design system employs a **Fixed Grid** model for desktop interfaces, utilizing a 12-column system with a 1280px max-width container to reflect the structured nature of scientific data. 

Spacing is based on an **8px linear scale**, ensuring consistent vertical rhythm. Content blocks should use generous "lg" and "xl" padding to prevent information density from becoming overwhelming. Use "md" gutters between data cards and "sm" spacing between related form elements. All alignment should be strictly mathematical, reinforcing the brand's precision.

## Elevation & Depth
This design system avoids heavy shadows to maintain its minimalist aesthetic. Instead, depth is conveyed through **Tonal Layers** and **Low-Contrast Outlines**.

*   **Primary Surface:** Pure White.
*   **Secondary Surface:** Background Subtle (#F5F7FA) for container grouping.
*   **Interactive Elements:** Use 1px solid borders in a lightened Indigo or Mint instead of drop shadows.
*   **Modals/Pop-overs:** When necessary, use an "Ambient Shadow"—a very soft, Indigo-tinted blur (e.g., `0px 10px 30px rgba(26, 35, 126, 0.08)`) to suggest elevation without breaking the flat-tech feel. 
*   **Glassmorphism:** Use a subtle backdrop blur (12px) for sticky navigation bars to provide a modern "sterile glass" effect.

## Shapes
The shape language is defined by **Controlled Softness**. While the brand is scientific, it is also for pet lovers, requiring a friendly touch. 

A base roundedness of **0.5rem (8px)** is used for standard buttons and input fields. Larger containers and cards use **1rem (16px)** to create a distinct, modern-tech silhouette. The "Double-Helix" motif should be utilized as a background masking shape or a subtle line-art decoration, never as a primary structural container.

## Components
Consistent component styling ensures the interface feels like a unified scientific tool.

*   **Buttons:** Primary buttons are solid Deep Indigo with White text. Secondary buttons are Mint with Deep Indigo text. Both use the `rounded-lg` (8px) setting.
*   **Input Fields:** Ghost-style inputs with 1px Deep Indigo borders (20% opacity) that transition to 100% Mint on focus.
*   **Cards:** White surfaces with a 1px #E0E0E0 border. In the corner of diagnostic cards, place a subtle, low-opacity Mint Double-Helix pattern.
*   **Chips:** Used for pet health status or DNA markers. They should be pill-shaped with Mint backgrounds and Indigo text for high visibility.
*   **Data Visualizations:** Use the Indigo-to-Mint gradient for charts. Data points should be crisp, utilizing the "data-mono" typography for values.
*   **Progress Indicators:** Use a DNA-strand animation for loading states to reinforce the brand narrative.