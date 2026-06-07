---
name: AppSecure Design System
colors:
  surface: '#051424'
  surface-dim: '#051424'
  surface-bright: '#2c3a4c'
  surface-container-lowest: '#010f1f'
  surface-container-low: '#0d1c2d'
  surface-container: '#122131'
  surface-container-high: '#1c2b3c'
  surface-container-highest: '#273647'
  on-surface: '#d4e4fa'
  on-surface-variant: '#c6c6cc'
  inverse-surface: '#d4e4fa'
  inverse-on-surface: '#233143'
  outline: '#909096'
  outline-variant: '#45464b'
  surface-tint: '#c3c6d3'
  primary: '#c3c6d3'
  on-primary: '#2c303a'
  primary-container: '#0a0e17'
  on-primary-container: '#777b87'
  inverse-primary: '#5a5e69'
  secondary: '#f5fff5'
  on-secondary: '#003920'
  secondary-container: '#00ffa3'
  on-secondary-container: '#007146'
  tertiary: '#c0c6dd'
  on-tertiary: '#2a3042'
  tertiary-container: '#070d1e'
  on-tertiary-container: '#757a8f'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dfe2ef'
  primary-fixed-dim: '#c3c6d3'
  on-primary-fixed: '#181b25'
  on-primary-fixed-variant: '#434751'
  secondary-fixed: '#52ffac'
  secondary-fixed-dim: '#00e290'
  on-secondary-fixed: '#002111'
  on-secondary-fixed-variant: '#005231'
  tertiary-fixed: '#dce2f9'
  tertiary-fixed-dim: '#c0c6dd'
  on-tertiary-fixed: '#151b2c'
  on-tertiary-fixed-variant: '#404659'
  background: '#051424'
  on-background: '#d4e4fa'
  surface-variant: '#273647'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  code-sm:
    fontFamily: monospace
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
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
  container-padding: 1.5rem
  gutter: 1rem
  panel-gap: 2px
  density: compact
---

## Brand & Style

This design system is engineered for the high-context, low-latency environment of DevSecOps. The brand personality is clinical, vigilant, and performance-oriented, mirroring the precision of a professional IDE. It prioritizes information density over white space, ensuring that security analysts and developers have immediate access to critical telemetry.

The visual style blends **Minimalism** with **Cyber-Utility**. By utilizing a "Code-Editor" aesthetic, the system creates a familiar mental model for developers. It employs high-contrast elements and subtle luminescence to direct attention to active states and vulnerabilities without causing visual fatigue during long sessions.

## Colors

The palette is anchored by **Deep Navy**, serving as the "canvas" to reduce eye strain. **Neon Mint** is the tactical color, used exclusively for primary actions, success states, and indicating "secure" status. 

- **Backgrounds:** Use the primary Deep Navy for the main editor surface. Use slightly lighter tonal variants (Tertiary) for sidebars and panels to create structural hierarchy.
- **Accents:** Neon Mint should be used sparingly for high-impact UI triggers. Apply a subtle 8px-12px blur glow to these elements to simulate an emissive hardware interface.
- **Data Visualization:** Use variants of White and cool-toned grays for secondary data, reserving the highest contrast for critical alerts.

## Typography

This design system utilizes a dual-font strategy to distinguish between system navigation and technical output.

- **Navigation & Labels:** Use **Inter** for its neutral, highly legible characteristics in dense UI clusters. Labels for metadata should often use the `label-caps` style to provide a distinct visual anchor.
- **Headlines:** **Space Grotesk** provides a technical, geometric edge to page titles and high-level dashboard metrics.
- **Technical Data:** All code blocks, terminal outputs, and SHA hashes must use a **Monospace** stack. This ensures character alignment and reinforces the developer-centric aesthetic.

## Layout & Spacing

The layout philosophy follows a **Fixed-Panel Grid**, reminiscent of modern IDEs like VS Code. 

- **Structure:** The interface is divided into a 4-panel architecture: Activity Bar (narrow left), Sidebar (navigation/file tree), Main Stage (editor/dashboard), and Inspector (right-side contextual data).
- **Density:** Use a tight 4px baseline grid. Elements should be packed closely to maximize the "at-a-glance" data footprint.
- **Separation:** Eschew large margins in favor of 1px or 2px gaps between panels. This "bento-box" style layout maximizes screen real estate for complex security logs.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Bold Borders** rather than traditional shadows.

- **Planes:** The deepest layer is the primary background. As elements rise in importance (e.g., modals, popovers), the background color shifts slightly lighter (e.g., from #0A0E17 to #161C2D).
- **Borders:** Use 1px solid borders for all container definitions. For inactive states, use a low-opacity navy border. For active or focused states, transition the border to Neon Mint.
- **Glow:** The only "shadow" permitted is a specialized "Neon Glow." This is a drop-shadow with 0px offset and a vibrant spread, applied only to active buttons or critical status indicators to signify "power on" states.

## Shapes

The shape language is industrial and precise. 

- **Radius:** A "Soft" rounding (0.25rem) is used for buttons and primary input fields to prevent the UI from feeling overly aggressive while maintaining a professional, tool-like appearance.
- **Tabs:** Use "tab" shapes for panel switching—rectangular with 0px bottom radius to sit flush against the content area, mirroring browser or editor tabs.
- **Icons:** Use linear, 1.5pt stroke icons. Avoid filled icons unless used for high-severity alert status.

## Components

- **Buttons:** Primary buttons feature a solid Neon Mint background with black text. Secondary buttons utilize a "Ghost" style with a Neon Mint border and no fill, intensifying the glow effect on hover.
- **Chips/Badges:** Small, rectangular badges with monospace text. Status badges use a "dot" indicator (e.g., a pulsing Mint dot for "Secure," a steady White dot for "Inactive").
- **Inputs:** Dark-filled backgrounds with 1px borders. On focus, the border transitions to Neon Mint with a 4px outer glow. Use monospace fonts for inputs handling technical strings.
- **Cards/Panels:** These should not have shadows. Use a 1px border (#1E293B) and a header bar with a slightly darker background to group related data.
- **Data Grids:** High-density tables with subtle zebra-striping. Hovering over a row should trigger a 1px Neon Mint left-border "active line" highlight.
- **Code Blocks:** Syntax-highlighted surfaces using a specialized palette that complements the Deep Navy background, ensuring high contrast for security-sensitive keywords.