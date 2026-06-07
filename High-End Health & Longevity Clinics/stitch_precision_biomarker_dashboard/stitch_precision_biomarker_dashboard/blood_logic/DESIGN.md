---
name: Blood-Logic
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
  on-surface-variant: '#43474e'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#455f88'
  primary: '#002045'
  on-primary: '#ffffff'
  primary-container: '#1a365d'
  on-primary-container: '#86a0cd'
  inverse-primary: '#adc7f7'
  secondary: '#006d3c'
  on-secondary: '#ffffff'
  secondary-container: '#85f6ad'
  on-secondary-container: '#00723f'
  tertiary: '#1b2127'
  on-tertiary: '#ffffff'
  tertiary-container: '#30363c'
  on-tertiary-container: '#989fa6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#adc7f7'
  on-primary-fixed: '#001b3c'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#88f9b0'
  secondary-fixed-dim: '#6bdc96'
  on-secondary-fixed: '#00210f'
  on-secondary-fixed-variant: '#00522c'
  tertiary-fixed: '#dde3eb'
  tertiary-fixed-dim: '#c1c7cf'
  on-tertiary-fixed: '#161c22'
  on-tertiary-fixed-variant: '#41474e'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
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
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: -0.02em
  data-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '400'
    lineHeight: '1'
    letterSpacing: 0.02em
  label:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 24px
---

## Brand & Style
The design system is engineered for high-stakes clinical environments where precision and rapid data interpretation are paramount. It evokes a sense of "Clinical Precision"—combining the cold reliability of laboratory instrumentation with the intuitive speed of modern SaaS. The UI is designed to be invisible yet authoritative, prioritizing data density and legibility over decorative elements.

The aesthetic leans into **Corporate / Modern** with a technical edge. It utilizes high-contrast interfaces, sharp structural alignments, and a utilitarian approach to information architecture. The goal is to instill absolute confidence in the user, ensuring that every data point is unmistakable and every action is deliberate.

## Colors
The palette is rooted in a "Laboratory Blue" (#1A365D), which serves as the anchor for headers, primary navigation, and critical structural elements. This deep indigo provides a stable, authoritative backdrop for the bright "Mint" (#48BB78) used for success states, vital signs within normal ranges, and primary calls to action.

The neutral palette is biased toward cool grays to maintain the sterile, clinical feel. High-contrast text (#1A365D on #FFFFFF) ensures maximum readability under varied lighting conditions. Warning and alert colors should be used sparingly but must be vibrant enough to break the cool-toned harmony when immediate attention is required.

## Typography
This design system employs a dual-font strategy. **Inter** is the primary typeface for all UI labels, navigation, and descriptive text, chosen for its exceptional legibility and neutral personality. 

For all quantitative data points, lab results, and timestamps, **JetBrains Mono** is utilized. As a monospaced font, it ensures that columns of numbers align perfectly, allowing technicians to scan and compare vertical data sets with mathematical accuracy. Letter spacing is tightened for headlines to maintain a compact feel, while labels are slightly tracked out for clarity at small sizes.

## Layout & Spacing
The layout follows a **Fluid Grid** model to maximize screen real estate on medical-grade monitors. A 12-column system is used for primary dashboard layouts, allowing for flexible arrangements of data widgets and analytics panels. 

Spacing is governed by a strict 4px base unit. To achieve high data density, internal padding within cards and tables is kept to `sm` (8px) or `md` (16px). This allows for a "glanceable" interface where the user can see the maximum amount of information without scrolling, while using `lg` (24px) margins to separate distinct functional zones.

## Elevation & Depth
Elevation is primarily conveyed through **Tonal Layers** and **Low-contrast Outlines** rather than heavy shadows. This maintains a clean, clinical aesthetic and prevents the UI from feeling cluttered.

1.  **Base Layer:** The application background (#F8FAFC) serves as the foundation.
2.  **Surface Layer:** Cards and data containers are pure white (#FFFFFF) with a 1px solid border (#E2E8F0).
3.  **Active Layer:** Elements requiring immediate interaction or focus may use a very subtle, diffused shadow (0px 2px 4px rgba(26, 54, 93, 0.05)) to suggest "lift."

Dividers are used frequently but subtly to define rows and columns within data-dense views, ensuring the eye can follow technical paths without visual interruption.

## Shapes
The shape language is conservative and professional. A "Soft" roundedness (4px) is applied to buttons, input fields, and containers. This slight softening prevents the UI from feeling "sharp" or hostile while maintaining the structured, grid-based discipline of a technical tool. Pills are reserved strictly for status chips (e.g., "Active," "Pending," "Critical") to differentiate them from actionable buttons.

## Components
-   **Buttons:** Primary buttons use Laboratory Blue with white text. Secondary buttons use a white fill with a 1px border. The "Mint" color is reserved for "Confirm" or "Complete" actions.
-   **Data Tables:** The core of the system. Use alternate row striping (Zebra-striping) with a very light gray (#F1F5F9). Headers must be sticky, using the uppercase Label style for maximum clarity.
-   **Status Chips:** Small, pill-shaped indicators. Use a light tint of the status color for the background (e.g., light green for Mint) with high-contrast text.
-   **Input Fields:** Sharp, 1px bordered boxes that turn Laboratory Blue on focus. Labels are positioned above the field in the "label" typographic style.
-   **Sparklines:** Integrated directly into data tables to show trends over time without requiring a full chart view.
-   **Cards:** Clean white surfaces with 1px borders. Header sections of cards are separated by a subtle horizontal rule.
-   **Gauges & Progress Bars:** Use the Mint color for "healthy" metrics, transitioning to amber or red only when clinical thresholds are breached.