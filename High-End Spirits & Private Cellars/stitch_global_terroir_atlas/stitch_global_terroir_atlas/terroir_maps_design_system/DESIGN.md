---
name: Terroir-Maps Design System
colors:
  surface: '#fcfdc6'
  surface-dim: '#dddda9'
  surface-bright: '#fcfdc6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f7c1'
  surface-container: '#f1f1bb'
  surface-container-high: '#ebebb6'
  surface-container-highest: '#e5e6b1'
  on-surface: '#1c1d00'
  on-surface-variant: '#46483c'
  inverse-surface: '#31320d'
  inverse-on-surface: '#f4f4be'
  outline: '#77786b'
  outline-variant: '#c7c8b9'
  surface-tint: '#586330'
  primary: '#485422'
  on-primary: '#ffffff'
  primary-container: '#606c38'
  on-primary-container: '#dfedac'
  inverse-primary: '#bfcd8f'
  secondary: '#615f4b'
  on-secondary: '#ffffff'
  secondary-container: '#e4e0c7'
  on-secondary-container: '#65634f'
  tertiary: '#445433'
  on-tertiary: '#ffffff'
  tertiary-container: '#5c6c49'
  on-tertiary-container: '#daecc1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe9a9'
  primary-fixed-dim: '#bfcd8f'
  on-primary-fixed: '#171e00'
  on-primary-fixed-variant: '#404b1b'
  secondary-fixed: '#e7e3ca'
  secondary-fixed-dim: '#cac7af'
  on-secondary-fixed: '#1d1c0d'
  on-secondary-fixed-variant: '#494835'
  tertiary-fixed: '#d7e9bd'
  tertiary-fixed-dim: '#bbcda3'
  on-tertiary-fixed: '#121f05'
  on-tertiary-fixed-variant: '#3d4b2b'
  background: '#fcfdc6'
  on-background: '#1c1d00'
  surface-variant: '#e5e6b1'
typography:
  display-xl:
    fontFamily: Libre Caslon Text
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Libre Caslon Text
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Libre Caslon Text
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Libre Caslon Text
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Libre Caslon Text
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Libre Caslon Text
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  caption-italic:
    fontFamily: Libre Caslon Text
    fontSize: 14px
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
  unit: 8px
  sidebar-width: 280px
  container-max: 1440px
  gutter: 32px
  margin-desktop: 48px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built upon the intersection of historical cartography and modern environmental science. The brand personality is **Educational & Earthy**, evoking the feeling of a well-preserved botanical archive or a premium field researcher’s journal. It targets professionals in viticulture, geology, and environmental planning who require high-density information delivered with aesthetic clarity.

The visual style is a blend of **Minimalism** and **Tactile/Archival** elements. It prioritizes expansive whitespace to allow complex data visualizations to breathe, while using organic textures and traditional typography to ground the digital experience in the physical world. The goal is to make the user feel like a curator of the land rather than a mere data entry clerk.

## Colors

The palette is derived directly from the landscape. **Sand (#FEFAE0)** serves as the primary canvas color, providing a warmer, more legible alternative to pure white that mimics aged parchment. **Olive Green (#606C38)** is used for primary actions, success states, and brand highlights, representing vitality and growth.

**Slate (#283618)** acts as the anchor, used for deep contrast in typography and structural borders. For secondary UI elements like inactive tabs or subtle dividers, a muted mid-tone neutral (derived from the Olive and Sand mix) provides soft transitions without breaking the earthy harmony.

## Typography

The typography system exclusively utilizes **Libre Caslon Text** to maintain a sophisticated, archival feel across all levels of hierarchy. This serif typeface excels in long-form educational content and lends authority to data-heavy admin panels.

To differentiate information types on the wide desktop canvas, we utilize traditional typesetting techniques:
- **Display and Headlines:** Use tighter tracking and bold weights for a commanding presence.
- **Body Text:** Generous line heights (1.6) ensure readability during deep research sessions.
- **Labels:** Small caps or all-caps with increased letter spacing are used for metadata, map legends, and sidebar navigation items to provide a distinct visual break from prose.
- **Captions:** Italicized weights are reserved for annotations, citations, and supplementary data visualization notes.

## Layout & Spacing

The layout is optimized for high-resolution desktop displays using a **12-column fixed-width grid** centered within the viewport. To maintain the "expansive" feel, we employ wider-than-standard margins (48px) and gutters (32px).

The admin experience is anchored by a **persistent side navigation** (280px) on the left, which uses a slightly darker tint of the Sand background to create a clear functional split from the content area. White space is treated as a core design element—vertical stacking follows a strict 8px rhythm, but large sections are separated by 48px or more to prevent the UI from feeling cluttered, even when displaying complex map layers and charts.

## Elevation & Depth

This design system avoids heavy drop shadows in favor of **Tonal Layering** and **Low-Contrast Outlines**. Depth is conveyed through subtle color shifts and structural containment:

- **Surface 0 (Background):** The base Sand (#FEFAE0) canvas.
- **Surface 1 (Cards/Sidebar):** A slightly lighter or 2% darker variation of Sand to suggest height.
- **Borders:** All interactive containers and cards use a 1px border of Slate (#283618) at 15% to 25% opacity. This creates a "technical drawing" aesthetic.
- **Interactions:** On hover, a subtle inner glow or a shift to 40% border opacity indicates interactivity.
- **Visualizations:** Data layers on maps may use a soft 4px blur shadow to lift significant findings above the topography, but this is used sparingly.

## Shapes

To balance the "archival" (structured) and "earthy" (organic) themes, all UI components use **soft 8px (0.5rem) rounding**. 

This specific radius is applied to buttons, input fields, cards, and modal containers. It is sharp enough to feel professional and cartographic, but soft enough to feel approachable. Larger containers like the main content area panel may use a larger 16px (1rem) radius on the inner corners to frame the data visualizations gracefully. Icons should follow this language, utilizing rounded terminals and organic curves.

## Components

### Buttons & Actions
Primary buttons are solid Olive Green with Sand text. Secondary buttons use a Slate border (1px) with transparent backgrounds. Tertiary buttons for map controls use a Sand background with a subtle border to blend into the interface.

### Input Fields & Controls
Form inputs are styled with a Sand fill and a 1px Slate border at 20% opacity. Upon focus, the border opacity increases to 80%. Checkboxes and radio buttons use the Olive Green for checked states, maintaining an organic feel.

### Cards & Panels
Cards are the primary vessel for data. They feature a 1px Slate border and 8px corner radius. Header sections within cards should use the `label-sm` typography style with a subtle bottom divider to separate metadata from the primary content.

### Data Visualizations
Charts and maps should use an extended earthy palette: Terracotta, Ochre, and Deep Forest. High-fidelity visualizations should be "framed" within the UI using generous padding, mimicking the look of a matted photograph or an atlas entry.

### Side Navigation
The sidebar is the control center for the admin panel. Navigation items use `body-md` for primary links and `label-sm` for category headers. Active states are indicated by a solid Olive Green vertical bar (4px wide) on the far left of the item.