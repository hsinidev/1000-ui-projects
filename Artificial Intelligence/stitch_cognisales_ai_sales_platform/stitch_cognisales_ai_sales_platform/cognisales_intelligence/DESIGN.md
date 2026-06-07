---
name: CogniSales Intelligence
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
  on-surface-variant: '#3c4a42'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#6c7a71'
  outline-variant: '#bbcabf'
  surface-tint: '#006c49'
  primary: '#006c49'
  on-primary: '#ffffff'
  primary-container: '#10b981'
  on-primary-container: '#00422b'
  inverse-primary: '#4edea3'
  secondary: '#545f73'
  on-secondary: '#ffffff'
  secondary-container: '#d5e0f8'
  on-secondary-container: '#586377'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#a0a3a5'
  on-tertiary-container: '#36393b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#6ffbbe'
  primary-fixed-dim: '#4edea3'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#005236'
  secondary-fixed: '#d8e3fb'
  secondary-fixed-dim: '#bcc7de'
  on-secondary-fixed: '#111c2d'
  on-secondary-fixed-variant: '#3c475a'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  title-md:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  caption:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-margin: 16px
  gutter: 12px
---

## Brand & Style

This design system is engineered for high-velocity sales environments where data density must coexist with extreme clarity. The brand personality is **Growth-Focused, Professional, and Energetic**, positioning the tool as an indispensable partner for the modern sales professional. 

The aesthetic follows a **Corporate / Modern** style with a distinct **Data-driven** edge. It leverages heavy whitespace to reduce cognitive load during complex lead analysis, while injecting energy through vibrant success indicators. The interface evokes a sense of "informed momentum"—shifting the user from observation to action with high-contrast visual cues and a mobile-first ergonomic logic.

## Colors

The palette is anchored by **Emerald Green (#10B981)**, symbolizing growth, revenue, and "go" signals. This is balanced by **Navy (#1E293B)**, which provides a professional, stable foundation for navigation and deep text elements. 

**White (#FFFFFF)** serves as the primary canvas to ensure maximum readability and a clean "SaaS" feel. For high-impact moments—such as closing a deal or hitting a quota—the design system utilizes a high-contrast **Success Gradient**, transitioning from Emerald to a deeper Forest Green to add depth and tactile energy to performance metrics.

## Typography

The typography system uses **Inter** for its exceptional legibility and systematic, utilitarian feel. The hierarchy is optimized for "glanceability," ensuring sales reps can extract key insights (like lead scores or deal values) instantly on mobile devices.

Large display sizes utilize a tighter letter-spacing and heavier weights to project confidence. Body copy maintains a generous line height to ensure readability in long-form sales notes or CRM entries. Labels are often treated with semi-bold weights to clearly demarcate data points from their values.

## Layout & Spacing

This design system utilizes a **Fluid Grid** model optimized for the 8pt spacing system. For mobile sales enablement, the layout prioritizes a single-column vertical flow with a standard 16px side margin. On larger screens, the system expands into a multi-column dashboard format where content containers use a 12px gutter.

The spacing rhythm is intentional: tight spacing (4px-8px) for related data points within a card, and generous spacing (24px+) between major functional sections to prevent visual clutter and support a "data-driven" clarity.

## Elevation & Depth

Visual hierarchy is established through **Ambient Shadows** and **Tonal Layers**. Shadows in this design system are sophisticated and diffused—using a Navy-tinted shadow color at low opacity (e.g., `rgba(30, 41, 59, 0.08)`) to maintain a professional look without appearing dated.

Surface depth is tiered:
- **Level 0 (Background):** White or Light Gray (#F8FAFC) for the main canvas.
- **Level 1 (Cards):** White surfaces with subtle 1px borders (#E2E8F0) and low-blur shadows.
- **Level 2 (Modals/Overlays):** Elevated with a larger shadow spread to draw immediate focus for active tasks like "Add Lead."

## Shapes

The design system adopts a **Rounded** shape language to soften the density of the data and provide a modern, approachable feel. Standard components like input fields and small cards use a 0.5rem (8px) radius. Larger dashboard modules and "Success" modals utilize the 1rem (16px) radius for a more prominent, friendly presence. 

Buttons and interactive chips should feel tactile and "tappable," especially on mobile devices, reinforcing the energetic and action-oriented nature of the brand.

## Components

### Buttons & Interaction
Primary buttons feature the **Success Gradient** with white text to draw maximum attention. Secondary buttons use the Navy color with an outline or ghost treatment. All buttons maintain a minimum height of 44px for mobile ergonomics.

### Data Cards
Cards are the primary vessel for sales intelligence. They must feature a 1px soft border and the standard Level 1 shadow. Header areas within cards should use the Navy title font for strong categorization.

### Status Chips
Use high-contrast backgrounds for status indicators:
- **Closed Won:** Emerald Green background / White text.
- **In Progress:** Navy background / White text.
- **High Priority:** High-contrast gradient border.

### Inputs
Search bars and data entry fields utilize the Soft (8px) roundedness with a focused state that uses an Emerald Green 2px ring.

### Sales Performance Charts
Data visualizations should exclusively use the primary Emerald and Navy palette, with secondary grays for axes and gridlines. "Growth" lines should always utilize the primary green to reinforce the brand's core value proposition.