---
name: Sovereign Intelligence
colors:
  surface: '#111415'
  surface-dim: '#111415'
  surface-bright: '#373a3b'
  surface-container-lowest: '#0c0f10'
  surface-container-low: '#191c1d'
  surface-container: '#1d2021'
  surface-container-high: '#282a2b'
  surface-container-highest: '#323536'
  on-surface: '#e1e3e4'
  on-surface-variant: '#cec3d3'
  inverse-surface: '#e1e3e4'
  inverse-on-surface: '#2e3132'
  outline: '#978d9d'
  outline-variant: '#4c4451'
  surface-tint: '#ddb7ff'
  primary: '#ddb7ff'
  on-primary: '#4a0080'
  primary-container: '#4b0082'
  on-primary-container: '#ba7ef4'
  inverse-primary: '#7b41b3'
  secondary: '#bfc2ff'
  on-secondary: '#181d8c'
  secondary-container: '#3239a3'
  on-secondary-container: '#a9afff'
  tertiary: '#00daf3'
  on-tertiary: '#00363d'
  tertiary-container: '#00373e'
  on-tertiary-container: '#00a9bc'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#f0dbff'
  primary-fixed-dim: '#ddb7ff'
  on-primary-fixed: '#2c0050'
  on-primary-fixed-variant: '#622599'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#00006e'
  on-secondary-fixed-variant: '#3239a3'
  tertiary-fixed: '#9cf0ff'
  tertiary-fixed-dim: '#00daf3'
  on-tertiary-fixed: '#001f24'
  on-tertiary-fixed-variant: '#004f58'
  background: '#111415'
  on-background: '#e1e3e4'
  surface-variant: '#323536'
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
  body:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  data-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 24px
  container-max: 1440px
  density-xs: 4px
  density-sm: 8px
  density-md: 12px
---

## Brand & Style

This design system is engineered for high-stakes environments where information density and clarity are synonymous with security. The brand personality is authoritative, institutional, and unyielding. It serves an elite audience that requires immediate access to complex data without the interference of decorative trends.

The aesthetic follows a **Strict Minimalism** approach fused with **Corporate Modernism**. It prioritizes structural integrity over visual flair. Every element exists to serve a functional purpose, utilizing heavy information density and a "command center" feel to evoke a sense of absolute control and discretion.

## Colors

The color palette is built on a foundation of deep, nocturnal tones to reduce eye strain during prolonged surveillance and data analysis. 

- **Primary (Royal Purple):** Used exclusively for high-level brand moments, primary actions, and verified security states.
- **Secondary (Deep Navy):** The core of the interface, used for navigation, sidebars, and structural backgrounds.
- **Crisp White:** Reserved for high-contrast text and critical data layers to ensure maximum legibility against dark backgrounds.
- **Functional Accents:** A tertiary cyan is used sparingly for interactive data points and graph nodes, while standard semantic colors (Red/Amber/Green) are tuned to high-vibrancy levels to cut through the navy base.

## Typography

Typography in this design system is split between two distinct functions: **Interface Navigation** and **Data Representation**.

1.  **Inter:** Used for all UI labels, headlines, and instructional text. It provides a clean, neutral tone that does not distract from the data.
2.  **JetBrains Mono:** Utilized for all numerical data, coordinates, timestamps, and financial figures. The monospaced nature ensures that columns of numbers align perfectly for rapid scanning and comparison.

Hierarchy is established through weight and capitalization rather than significant size increases to maintain the high-density layout requirements.

## Layout & Spacing

This design system employs a **Strict 12-Column Grid** with a fixed gutter system. Layouts must be rigid and predictable; fluidity is minimized to ensure that analysts can memorize the location of critical data points.

The spacing rhythm is based on a **4px baseline**. Given the high-stakes nature of the intelligence work, density is prioritized. Component padding is kept to the minimum required for legibility (`density-sm` or `density-md`), allowing as much information as possible to be "above the fold." Sections are separated by distinct 1px borders rather than wide margins.

## Elevation & Depth

To maintain a secure and professional aesthetic, this design system avoids soft shadows and ambient blurs. Depth is conveyed through **Tonal Layering** and **High-Contrast Outlines**.

- **Level 0 (Background):** Deep Navy (#000080 or darker) for the primary application canvas.
- **Level 1 (Surfaces):** Slightly lighter navy shades (#000066) for cards and containers.
- **Level 2 (Interaction):** Royal Purple highlights for active states.
- **Keylines:** Every component and container must feature a crisp 1px border. Use 10% opacity white for standard borders and 100% Crisp White for focused or critical alerts. This creates a "blueprint" feel that emphasizes structure.

## Shapes

The shape language is strictly **Sharp (0px radius)**. 

Every UI element—from buttons and input fields to cards and status indicators—must utilize 90-degree corners. This reinforces the authoritative, architectural nature of the intelligence agency. Rounded shapes are viewed as too "consumer-oriented" and are excluded to maintain a serious, mission-critical tone.

## Components

### Buttons & Inputs
Buttons are strictly rectangular. Primary buttons use a solid Royal Purple fill with Crisp White text. Secondary buttons use a Deep Navy fill with a 1px white border. Input fields are transparent with a 1px border, utilizing JetBrains Mono for user-entered data.

### Data-Heavy Cards
Cards are the primary vessel for information. They feature no rounded corners and use 1px borders to separate the header, body, and footer. Headers should have a subtle background tint and include a "Secure Status Indicator" in the top-right corner.

### Secure Status Indicators
These are binary or trinary markers (e.g., Secure, Compromised, Pending). They use high-vibrancy semantic colors and often include a 1px "pulsing" animation for critical alerts to ensure visibility against the dark navy background.

### Interactive Graphs
Graphs utilize thin, 1px lines and sharp-edged nodes. Tooltips must be monospaced and appear instantly without transition animations to respect the user's need for immediate data retrieval.

### Additional Components
- **Data Tables:** High-density rows with alternating tonal stripes (Zebra striping) using subtle navy variations.
- **Breadcrumbs:** Strict "System / Directory / File" formatting to maintain a sense of location within the agency's hierarchy.