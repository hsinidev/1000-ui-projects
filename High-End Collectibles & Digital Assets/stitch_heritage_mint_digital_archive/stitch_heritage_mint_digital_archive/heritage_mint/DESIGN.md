---
name: Heritage-Mint
colors:
  surface: '#fbf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#554240'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#89726f'
  outline-variant: '#dcc0bd'
  surface-tint: '#9d4139'
  primary: '#210000'
  on-primary: '#ffffff'
  primary-container: '#4a0404'
  on-primary-container: '#d26a5f'
  inverse-primary: '#ffb4aa'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#0d0a01'
  on-tertiary: '#ffffff'
  tertiary-container: '#252110'
  on-tertiary-container: '#8f8871'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#7e2b23'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ebe2c8'
  tertiary-fixed-dim: '#cec6ad'
  on-tertiary-fixed: '#1f1c0b'
  on-tertiary-fixed-variant: '#4c4733'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  headline-xl:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Work Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-caps:
    fontFamily: IBM Plex Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
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
  gutter: 16px
  margin-mobile: 20px
  margin-desktop: 64px
  container-max: 1200px
---

## Brand & Style
The design system embodies a **Nostalgic-Refined** aesthetic, positioning the platform as a digital bridge between ancient history and modern blockchain technology. The target audience includes high-net-worth collectors, institutional archivists, and sophisticated investors who value provenance and rarity.

The style is **Tactile-Minimalist**. It avoids the sterility of modern fintech by utilizing physical metaphors: deckled paper edges, subtle fiber textures, and gold foil accents that react to scroll/tilt. The emotional response is one of "The Digital Library"—a quiet, prestigious, and highly secure environment where the user feels like a curator rather than a trader.

## Colors
The palette is rooted in the materials of classical bookbinding and archival preservation.

- **Primary (Deep Burgundy):** Used for key brand moments, primary actions, and headers to evoke the feeling of leather-bound volumes.
- **Secondary (Gold Foil):** A metallic accent (#D4AF37) used sparingly for "Verified" badges, highlights, and decorative borders to denote value.
- **Background (Parchment):** The foundational canvas. Use a subtle grain texture overlay at 5% opacity to prevent the screen from feeling "flat."
- **Foreground (Charcoal):** Provides high-legibility for body text and functional UI iconography, avoiding the harshness of pure black.

## Typography
This design system utilizes a high-contrast typographic pairing to balance tradition with functional clarity.

- **Playfair Display:** Reserved for high-level storytelling, manuscript titles, and section headers. It conveys the authority of a museum title card.
- **Work Sans:** The workhorse for all body content, descriptions, and transactional data. Its neutral character ensures it doesn't compete with the expressive headlines.
- **IBM Plex Sans:** Specifically for technical metadata (token IDs, mint dates, blockchain addresses) and UI labels, providing a modern, systematic counterpoint to the parchment background.

## Layout & Spacing
This design system utilizes a **Fixed Grid** on desktop and a **Fluid Margin** system on mobile. 

The spacing rhythm is generous to evoke a sense of "luxury through whitespace." Elements should never feel crowded; the layout follows a strict 8px baseline grid to ensure vertical rhythm. 

- **Mobile:** A 4-column layout with 20px side margins. Content cards are typically full-width.
- **Desktop:** A 12-column centered layout with 64px margins. Manuscripts are displayed in an asymmetrical "Gallery" style where images may break the grid to suggest a physical table-top arrangement.

## Elevation & Depth
Depth is communicated through physical material stacking rather than digital shadows.

- **Tonal Layers:** The Parchment (#F4EBD0) is the base. Elevated containers use a slightly lighter "Vellum" shade or a very subtle inner glow to suggest the paper is lifting off the surface.
- **Deckled Edges:** Instead of standard drop shadows, high-value cards use a subtle "deckled edge" (torn paper) SVG mask to create a silhouette against the background.
- **Archival Glass:** For modal overlays, use a backdrop blur (12px) with a 20% Charcoal tint, simulating a protective display case.

## Shapes
The shape language is conservative and structural.

- **Soft Corners:** Use a 0.25rem (4px) radius for buttons and input fields to soften the UI without making it feel "bubbly" or informal.
- **Sharp Corners:** Used for archival photography frames and high-level section containers to mimic the edges of a physical book or frame.
- **Decorative Accents:** Gold Foil dividers use a 1px height with a "tapered" effect at the ends, reminiscent of classic manuscript calligraphy.

## Components
- **Buttons:** Primary buttons are Deep Burgundy with Gold Foil labels. Use a subtle serif for button text to maintain the premium feel. Hover states should involve a slight "press" effect (Y-axis translation) rather than a color change.
- **Cards:** Manuscript cards feature a "Full-Bleed" archival photo at the top. The bottom section uses the "Label-Caps" typography for token stats.
- **Chips:** "Status" indicators (e.g., *Minted*, *In Transit*) use a flat, low-contrast border style on Parchment backgrounds, appearing like a wax seal or ink stamp.
- **Input Fields:** Use a simple bottom-border only (1px Charcoal) to mimic a signature line on a document.
- **Navigation:** A minimalist top-bar with a centered "Heritage-Mint" wordmark. Mobile navigation uses a "Curator's Menu"—a full-screen overlay that feels like opening a large folio.
- **Additional Component: The "Provenance Timeline":** A vertical line component using the Gold Foil accent to track the historical ownership and blockchain minting history of a manuscript.