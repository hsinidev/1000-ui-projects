---
name: FanZone-Pro
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#37393a'
  surface-container-lowest: '#0c0f0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#fff9ef'
  on-secondary: '#3a3000'
  secondary-container: '#ffdb3c'
  on-secondary-container: '#725f00'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#1f1f1f'
  on-tertiary-container: '#878686'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#ffe16d'
  secondary-fixed-dim: '#e9c400'
  on-secondary-fixed: '#221b00'
  on-secondary-fixed-variant: '#544600'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-xl:
    fontFamily: Lexend
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
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
    lineHeight: '1.6'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  stat-lg:
    fontFamily: Lexend
    fontSize: 40px
    fontWeight: '800'
    lineHeight: '1'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-margin: 24px
  gutter: 16px
  bento-gap: 12px
  section-padding: 48px
---

## Brand & Style

The brand personality is high-octane, elite, and authoritative. This design system is built to evoke the adrenaline of a live stadium environment while maintaining the sleekness of a luxury sports brand. It targets dedicated fans who demand real-time data, high-quality media, and a sense of belonging to an exclusive community.

The aesthetic follows a **High-Contrast / Bold** movement, fused with **Modern** structural precision. It avoids soft, organic shapes in favor of rigid, high-impact layouts that mirror sports broadcasting graphics. Every element is designed to feel "active"—nothing is static. Visual weight is used strategically to prioritize breaking news and live scores, ensuring the user feels the fast-paced nature of professional athletics.

## Colors

This design system utilizes a dark-mode-first approach to maximize the "premium" feel and allow the primary brand colors to pop with maximum intensity.

- **Primary (Deep Navy):** Used for the main app canvas and primary containers. It provides a sophisticated, "pro-league" foundation.
- **Secondary (Gold):** Reserved for high-action focal points—CTAs, live indicators, and highlight stats. It represents victory and prestige.
- **Tertiary (Charcoal):** Utilized for bento-box backgrounds and secondary card surfaces to create depth without losing the dark aesthetic.
- **Neutral (White):** Used primarily for high-readability typography and crisp iconography against the dark backgrounds.

Additional semantic colors (Success Green, Alert Red) should be used sparingly but with high saturation to match the energetic tone.

## Typography

The typography strategy is built on a "Power and Precision" pairing. 

**Lexend** is used for all headlines and display text. Its wide, athletic stance communicates movement and confidence. For key stats (e.g., scores or player numbers), use the `stat-lg` style to ensure the data is the hero of the interface.

**Inter** handles all functional and body text. It is chosen for its exceptional readability in dense data environments like bento-box grids and player comparison tables. Labels should frequently use the `label-bold` style with uppercase transformations to mimic traditional sports jersey lettering and broadcast tickers.

## Layout & Spacing

The design system employs a **Fixed Grid** model (12 columns) for desktop, transitioning to a fluid single-column model for mobile. 

The layout's centerpiece is the **Bento-Box Grid**. Content is organized into modular rectangular containers of varying sizes (e.g., 2x2, 4x2, 6x4) that snap to the grid. This allows for a "dashboard" feel where live stats, news feeds, and video highlights can coexist without visual clutter. 

Spacing follows a strict 8px rhythm. Margins and gutters are kept relatively tight to maintain an energetic, high-density information environment that feels like a command center.

## Elevation & Depth

To maintain the high-contrast aesthetic, this design system avoids soft, natural shadows. Depth is instead achieved through **Tonal Layering** and **Subtle Outlines**:

1.  **Base Layer:** Deep Navy (#001F3F).
2.  **Surface Layer (Bento Boxes):** Charcoal (#333333).
3.  **Accent Outlines:** Active or focused elements receive a 1px solid Gold (#FFD700) or 1px White border with 20% opacity.
4.  **Interactive Glow:** High-priority elements (like a "Live Now" card) may use a subtle outer glow using the Gold primary color to simulate a neon stadium light effect.

Flat surfaces with sharp color transitions are preferred over gradients to ensure the UI feels fast and digitally native.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding of corners strikes a balance between the aggressive sharp edges of traditional brutalism and the overly friendly feel of modern consumer apps. 

Containers, buttons, and input fields should use the `rounded-sm` (4px) or `rounded-md` (8px) tokens. This technical, "machined" look supports the professional nature of the portal. Imagery within bento boxes should follow the container's corner radius for a unified, integrated appearance.

## Components

### Buttons
Primary buttons are solid Gold with Deep Navy text, utilizing the `label-bold` typography. They feature a 2px offset border on hover to create a tactile, "clickable" sensation without using traditional shadows.

### Bento-Box Cards
Cards are the primary organizational unit. Use Charcoal backgrounds. Every card should have a clear header using `headline-md` or `label-bold`. Interactive stats within cards should use Gold for the numerical values.

### Chips / Status Badges
Used for "Live" indicators, period trackers, or player positions. These use a high-saturation background (e.g., Red for live) with a pulsing opacity animation to draw immediate attention.

### Input Fields
Dark-themed inputs with Charcoal backgrounds and 1px White (20% opacity) borders. On focus, the border transitions to 1px Gold with a sharp interior highlight.

### Navigation
Vertical sidebar navigation is preferred for desktop to maximize vertical space for stats. Icons should be hollow/line-art, becoming solid Gold when active.

### Additional Components: Score Ticker
A persistent horizontal component at the top or bottom of the viewport that scrolls or fades through live scores across the league, utilizing high-contrast White text on a Deep Navy background.