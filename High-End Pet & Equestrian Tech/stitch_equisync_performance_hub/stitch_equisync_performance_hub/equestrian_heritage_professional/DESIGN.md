---
name: Equestrian Heritage Professional
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#404942'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#717971'
  outline-variant: '#c0c9c0'
  surface-tint: '#316948'
  primary: '#002a15'
  on-primary: '#ffffff'
  primary-container: '#004225'
  on-primary-container: '#75af89'
  inverse-primary: '#98d4ac'
  secondary: '#7c5639'
  on-secondary: '#ffffff'
  secondary-container: '#fecaa5'
  on-secondary-container: '#795336'
  tertiary: '#302100'
  on-tertiary: '#ffffff'
  tertiary-container: '#4b3500'
  on-tertiary-container: '#c29d56'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b4f0c7'
  primary-fixed-dim: '#98d4ac'
  on-primary-fixed: '#002110'
  on-primary-fixed-variant: '#165132'
  secondary-fixed: '#ffdcc4'
  secondary-fixed-dim: '#efbc98'
  on-secondary-fixed: '#2f1501'
  on-secondary-fixed-variant: '#613f24'
  tertiary-fixed: '#ffdea5'
  tertiary-fixed-dim: '#e9c176'
  on-tertiary-fixed: '#261900'
  on-tertiary-fixed-variant: '#5d4201'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  title-sm:
    fontFamily: Playfair Display
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.03em
  label-caps:
    fontFamily: Inter
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-page: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is rooted in the "Equestrian Heritage" aesthetic—a blend of high-end sporting tradition and meticulous performance tracking. It targets professional stable managers, owners, and elite trainers who value order, prestige, and longevity. The visual language evokes the atmosphere of a premier racing club: leather-bound ledgers, polished brass fixtures, and lush green paddocks.

The design style is **Tactile / Skeuomorphic-Modern**. It rejects the flatness of contemporary SaaS in favor of subtle physical cues that imply value and craftsmanship. Key characteristics include:
- **Material Authenticity:** Surfaces mimic the depth of heavy-grain leather and the sheen of brushed brass.
- **Atmospheric Professionalism:** A layout that feels like a bespoke administrative dashboard for a luxury estate.
- **Structured Precision:** High-performance data is presented with the clarity of a horological instrument.

## Colors

The palette is anchored by **Deep Racing Green**, representing authority and the heritage of the turf. **Tan Leather** serves as the primary structural color, used for headers, sidebars, and navigational accents to provide warmth and a tactile feel. **Brass Accents** are used sparingly for interactive elements, borders, and high-level highlights to denote premium status.

The background uses a "Paper" neutral rather than a clinical white, reducing eye strain and reinforcing the traditional ledger aesthetic. Status indicators (Success, Warning, Error) should be muted to maintain the sophisticated atmosphere, avoiding neon or overly vibrant hues.

## Typography

Typography in this design system creates a dialogue between tradition and performance. 

- **Playfair Display** is the authoritative voice. It is used for all major headings and page titles. In "Display" sizes, use heavier weights to mimic the look of traditional gold-leaf or embossed lettering.
- **Inter** handles the heavy lifting of data and performance metrics. It provides the necessary legibility for complex stable management tasks. 
- **Formatting:** Use `label-caps` for table headers and section overlines to provide an institutional, organized feel. Ensure high contrast for all Inter-based data points.

## Layout & Spacing

This design system utilizes a **Fixed Grid** philosophy to create a sense of stable, architectural permanence. Pages are centered within a maximum width of 1440px, evocative of a high-end desktop application.

- **Rhythm:** An 8px base unit drives all padding and margins. 
- **Composition:** Layouts should favor generous margins and clear "stables" of information. Use vertical dividers (in Brass or light Tan) to separate logical groupings of data.
- **Negative Space:** Whitespace (or "Paper space") is treated as a luxury. Do not crowd elements; allow the serif typography to breathe against the Deep Racing Green headers.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Physical Metaphors** rather than heavy shadows.

- **The Ground Plane:** The primary page background is the lightest "Paper" neutral.
- **The Ledger Layer:** Content cards use a subtle 1px border in Tan Leather or Brass.
- **The Inset:** Form inputs and data wells should appear slightly "pressed" into the surface using inner shadows, mimicking the look of debossed leather.
- **Surface Accents:** Use a subtle noise texture (3-5% opacity) on Tan Leather surfaces to simulate high-quality hide.
- **Brass Hardware:** Buttons and primary actions should have a very slight 1px "highlight" on the top edge and a 1px "shadow" on the bottom to give them a metallic, tactile presence.

## Shapes

The shape language is conservative and structural. **Soft (0.25rem)** corners are the standard, providing enough approachability without losing the rigor of a professional tool. 

- **Hard Lines:** Use 0px (sharp) corners for vertical dividers and specific "Hardware" style components like table headers.
- **Buttons/Inputs:** Use the standard 0.25rem (4px) radius. Avoid pill shapes or highly rounded circles, as they conflict with the traditional heritage aesthetic.
- **Brass Elements:** Brass dividers should be 1px thick and can feature "bolted" ornaments (small 4px squares) at intersections for added decorative detail.

## Components

- **Buttons:** Primary buttons use the `accent_brass_gradient` with dark text. Secondary buttons use Deep Racing Green with white text. Tertiary buttons are text-only with a Brass underline on hover.
- **Cards:** White or off-white backgrounds with a thin Tan Leather border. Use a "Header Strip" of Deep Racing Green (4px height) at the top of primary performance cards.
- **Inputs:** Backgrounds should be 2% darker than the card surface with a 1px border that shifts to Brass when focused. Label text should always be `label-caps`.
- **Chips/Badges:** Use Deep Racing Green backgrounds with Brass text for high-status "Elite" tags. Use Tan Leather for standard categorization.
- **Lists:** Rows should be separated by thin, low-opacity Brass lines. Hover states should utilize a very faint Tan Leather tint.
- **Specialty Component: The Performance Gauge:** Circular or linear indicators that use Brass for the "needle" or progress bar, set against a Racing Green track.
- **Data Tables:** High-density, using Inter for all values. Column headers should be fixed with a subtle leather-texture background.