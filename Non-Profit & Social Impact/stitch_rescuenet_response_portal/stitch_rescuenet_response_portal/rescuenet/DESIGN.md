---
name: RescueNet
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#5e3f3a'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#926e69'
  outline-variant: '#e8bdb6'
  surface-tint: '#c00000'
  primary: '#9e0000'
  on-primary: '#ffffff'
  primary-container: '#cc0000'
  on-primary-container: '#ffdad4'
  inverse-primary: '#ffb4a8'
  secondary: '#476083'
  on-secondary: '#ffffff'
  secondary-container: '#bdd6ff'
  on-secondary-container: '#445d80'
  tertiary: '#4b4d4d'
  on-tertiary: '#ffffff'
  tertiary-container: '#636565'
  on-tertiary-container: '#e2e3e3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad4'
  primary-fixed-dim: '#ffb4a8'
  on-primary-fixed: '#410000'
  on-primary-fixed-variant: '#930000'
  secondary-fixed: '#d4e3ff'
  secondary-fixed-dim: '#afc8f0'
  on-secondary-fixed: '#001c3a'
  on-secondary-fixed-variant: '#2f486a'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
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
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.4'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.4'
spacing:
  unit: 8px
  container-margin: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style
The design system is engineered for high-stakes, international disaster relief environments where speed of information and clarity of action are paramount. The brand personality is **authoritative, resilient, and urgent**. It targets three distinct user groups: field responders requiring rapid data entry, government officials seeking situational awareness, and global donors responding to immediate crises.

The visual style is a hybrid of **High-Contrast Bold** and **Corporate Modern**. It eschews decorative flourishes in favor of a utilitarian aesthetic that remains functional in low-light conditions or on low-resolution mobile devices. Every design decision prioritizes legibility and reduced cognitive load during high-stress scenarios.

## Colors
The palette is restricted to a high-impact triadic scheme to ensure accessibility and clear signaling. 
- **Signal Red (#CC0000):** Reserved exclusively for high-priority alerts, emergency actions, and critical status updates.
- **Navy Blue (#001F3F):** Used for primary navigation, professional branding elements, and information density to provide a sense of stability and trust.
- **White (#FFFFFF):** The primary surface color to maximize contrast and ensure readability in sunlight or low-bandwidth environments where complex gradients would fail.
- **Neutral (#1A1A1A):** Used for typography and iconography to maintain a high contrast ratio against white surfaces, exceeding WCAG AAA standards where possible.

## Typography
This design system utilizes **Inter** for its exceptional legibility and comprehensive character set, which is vital for international coordination. 

Headlines use heavy weights (700-800) to create a clear information hierarchy at a glance. Body text is set with generous line heights to prevent "rivers" of text and ensure readability during rapid scanning. Label styles utilize uppercase and bold weights to distinguish metadata from content, particularly in data-heavy field reports.

## Layout & Spacing
The layout follows a **fluid 12-column grid** that collapses into a single-column stack on mobile devices. A strict 8px base unit governs all spatial relationships. 

Spacing is intentionally generous around interactive elements to prevent "fat-finger" errors during high-stress field operations, yet tight within data cards to maximize the information visible on a single screen. Margin and gutter widths are kept consistent to reinforce a sense of structural "robustness" and order.

## Elevation & Depth
This design system avoids soft shadows and complex blurs to ensure performance on older hardware and visibility in harsh lighting. Instead, it utilizes **Bold Borders** and **Tonal Layers** to convey hierarchy.

- **Level 0 (Base):** White background.
- **Level 1 (Cards):** Defined by a 1px or 2px solid stroke in Navy Blue or Light Gray. No shadow.
- **Level 2 (Alerts):** Solid fills of Signal Red or Navy Blue.
- **Overlays:** High-contrast 4px black borders for modals to ensure they physically separate from the background content.

## Shapes
The shape language is strictly **Sharp (0px)**. This eliminates "softness" from the UI, reinforcing the professional and urgent nature of disaster relief. Rectilinear components maximize screen real estate and align perfectly with the grid, creating a rigorous, technical appearance that feels like a precision tool rather than a consumer app.

## Components

### Alert Headers
High-visibility banners positioned at the very top of the viewport. These use a **Signal Red** background with **White Bold Typography**. They must contain a succinct "Status" label and a "Time-Since-Update" stamp.

### Buttons
- **Primary:** Navy Blue background, White text, 0px radius. Heavy weight typography.
- **Urgent/Donate:** Signal Red background, White text. Reserved for life-saving actions or immediate financial contributions.
- **Outline:** 2px Navy Blue border, transparent background, for secondary actions.

### Field Report Cards
Data-dense containers using a 1px border. They utilize a "Split-Header" layout: the left side contains the primary metric (e.g., "Casualties" or "Supply Level") in bold display type, while the right side contains metadata in small labels.

### Quick-Donate Sticky Footer
A persistent, full-width bar at the bottom of the screen. It features a simplified "Amount Select" and a single high-contrast Signal Red button. On mobile, this remains pinned to ensure the most critical conversion path is always accessible.

### Input Fields
Strictly rectangular with high-contrast borders (2px). Active states utilize a Signal Red focus ring to ensure the user knows exactly where they are typing, even on low-quality screens.