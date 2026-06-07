---
name: Guardian Standard
colors:
  surface: '#faf8ff'
  surface-dim: '#dad9e0'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f9'
  surface-container: '#efedf3'
  surface-container-high: '#e9e7ee'
  surface-container-highest: '#e3e2e8'
  on-surface: '#1a1b20'
  on-surface-variant: '#444650'
  inverse-surface: '#2f3035'
  inverse-on-surface: '#f1f0f6'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dcdddd'
  on-secondary-container: '#5f6161'
  tertiary: '#2d0700'
  on-tertiary: '#ffffff'
  tertiary-container: '#501300'
  on-tertiary-container: '#d37758'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdbd0'
  tertiary-fixed-dim: '#ffb59e'
  on-tertiary-fixed: '#390b00'
  on-tertiary-fixed-variant: '#783018'
  background: '#faf8ff'
  on-background: '#1a1b20'
  surface-variant: '#e3e2e8'
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
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
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
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  button:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
  emergency:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '800'
    lineHeight: 24px
    letterSpacing: 0.02em
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
  xl: 32px
  container-padding-desktop: 24px
  container-padding-mobile: 16px
  gutter: 16px
---

## Brand & Style

The design system is engineered to evoke a sense of absolute institutional reliability, balancing the gravity of high-security childcare with a modern, professional approachability. The brand personality is authoritative yet calm—acting as a digital silent partner for daycare administrators and a rapid-response tool for staff.

The aesthetic follows a **Corporate / Modern** style, emphasizing structural integrity and clarity. It avoids the playfulness of typical "early childhood" apps in favor of a "safety-first" executive look. This ensures that parents feel their children are in a secure, well-managed environment, and staff feel equipped with professional-grade tools. By utilizing high-density layouts for administrators and streamlined, high-contrast interfaces for mobile staff, the design system bridges the gap between data-rich oversight and emergency readiness.

## Colors

The palette is anchored by **Royal Blue**, a color selected to communicate authority, security, and deep-seated trust. This primary hue is used for headers, primary actions, and navigational anchors to provide a consistent "security" frame for the application.

**Soft Grey** serves as the primary background color, providing a low-fatigue surface for long-term administrative use and creating subtle depth between container layers. **High-contrast White** is reserved for content cards and active surfaces to ensure maximum legibility.

Functional colors are critical for this design system. They utilize high-saturation tones to ensure status icons (like feeding or napping) are unmistakable at a glance. The **Emergency Red** is distinct from standard error states, reserved exclusively for the Panic Button and critical security breaches to ensure immediate recognition.

## Typography

This design system utilizes **Inter** exclusively to leverage its exceptional legibility in data-dense environments. The typography is structured to facilitate rapid information processing, particularly for administrators scanning child manifests or staff responding to alerts.

Weight is used strategically to indicate hierarchy: Bold and Semi-Bold weights are reserved for headers and critical data points, while Regular weights are used for instructional text and secondary information. A specialized "Emergency" style is defined for high-stress mobile actions, ensuring that even under duress, the text is clear and readable.

## Layout & Spacing

The design system employs a strict **8px grid system** to maintain mathematical harmony and alignment across all screens. 

- **Admin Panel (Desktop):** A 12-column fluid grid is used to maximize data density. Content should be organized into modular "Dashboard Widgets" that can span 3, 4, or 6 columns. Padding within tables and data lists is compressed (sm/md) to allow for more rows of information to be visible above the fold.
- **Staff Interface (Mobile):** A 4-column fluid grid with generous safe-area margins (24px) for one-handed operation. Spacing between interactive elements is increased to prevent accidental taps, particularly around the high-stakes Panic Button.

The layout philosophy prioritizes "Information First," ensuring that the most critical status updates (e.g., "Child Check-in") are never more than one level deep in the hierarchy.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** supplemented by crisp, **Ambient Shadows**.

1.  **Level 0 (Background):** Soft Grey (#F2F2F2). Non-interactive foundation.
2.  **Level 1 (Cards/Tables):** White (#FFFFFF) with a 1px border in a slightly darker grey (#E0E0E0). These surfaces hold the primary content.
3.  **Level 2 (Dropdowns/Modals):** White surfaces with diffused shadows (Y: 4px, Blur: 12px, 10% Opacity Black) to indicate temporary overlay status.
4.  **Level 3 (Emergency Alerts):** High-elevation surfaces with tinted shadows (Emergency Red glow) to command immediate attention.

This approach creates a clean, organized "stacked" appearance that feels structural and deliberate, reinforcing the theme of security.

## Shapes

To balance the strict "security" aesthetic with the childcare context, the design system utilizes **Rounded** geometry (0.5rem base). 

- **Buttons & Inputs:** Use the standard 0.5rem corner radius to appear modern and approachable.
- **Dashboard Cards:** Use `rounded-lg` (1rem) to create a soft, contained feel for grouped data.
- **Status Pills:** Use fully rounded (pill-shaped) geometry to distinguish them from interactive buttons.

This subtle rounding softens the clinical feel of the Royal Blue and Soft Grey palette, making the software feel modern and helpful rather than cold and purely institutional.

## Components

### Buttons
- **Primary:** Royal Blue background, White text. High-contrast and solid.
- **Secondary:** White background, Royal Blue border and text. Used for less critical actions.
- **Panic Button:** Large, circular or heavy-pill shaped component. Emergency Red background with high-contrast White text and icon. Requires a "long-press" or "swipe" interaction on mobile to prevent accidental triggers.

### Status Icons & Chips
- **High-Contrast:** Use specific functional colors (Green for "Active/Safe", Amber for "Napping/Away") with high-contrast glyphs.
- **Consistency:** All status icons must be contained within a standard 24px square bounding box for alignment in data rows.

### Data Tables (Admin)
- Compressed row heights with subtle 1px dividers. 
- Row hover states use a 2% Royal Blue tint to assist eye-tracking across wide screens.

### Input Fields
- Clear, labeled borders. 
- Validation states must use high-contrast Functional colors (Green/Red) and include an icon to ensure accessibility for color-blind users.

### Activity Feed Cards
- Summary cards for child activities (feeding, diapering) use icons as the primary visual anchor on the left, followed by a bold timestamp and a short descriptive label.