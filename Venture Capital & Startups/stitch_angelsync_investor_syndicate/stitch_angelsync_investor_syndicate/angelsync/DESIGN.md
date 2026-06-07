---
name: AngelSync
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
  on-surface-variant: '#44474e'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#090b0c'
  on-tertiary: '#ffffff'
  tertiary-container: '#1f2223'
  on-tertiary-container: '#87898a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-xl:
    fontFamily: notoSerif
    fontSize: 60px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: notoSerif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: notoSerif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  title-lg:
    fontFamily: inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 30px
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1200px
  gutter: 32px
  margin-page: 64px
  section-gap: 128px
---

## Brand & Style

This design system is engineered to evoke an atmosphere of exclusive membership and institutional stability. The brand personality is authoritative yet understated, catering to high-net-worth individuals who value discretion and precision. 

The aesthetic is a hybrid of **Minimalism** and **Tactile Luxe**. By stripping away unnecessary decorative elements and focusing on material honesty—specifically the juxtaposition of deep pigments against organic stone textures—the UI achieves a "digital concierge" feel. Every interaction must feel intentional, reinforcing a high-trust environment where the user's capital and privacy are paramount.

## Colors

The palette is anchored by **Deep Navy Blue**, providing a foundation of professional gravity and security. **Champagne Gold** is utilized sparingly as a high-contrast accent for interactive elements and borders, signaling premium value without becoming gaudy. 

The background strategy utilizes a "White Marble" approach, alternating between pure whites and very light grey-tints to simulate natural stone veining. This creates a rich, physical depth that distinguishes the interface from standard flat corporate designs. Neutral tones are kept strictly in the cool-grey spectrum to maintain the crispness of the navy and gold.

## Typography

This design system employs a classic serif-on-sans pairing to balance heritage with modernity. **Noto Serif** is used for all headlines to provide a literary, established feel reminiscent of premium financial publications. 

**Inter** is the functional workhorse for all data-heavy and body contexts, ensuring maximum legibility across complex investment tables and syndicate documents. Letter spacing is slightly widened for labels to enhance the sense of "luxury breathing room," while headlines use tighter tracking for a sophisticated, editorial impact.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy, centering content within a generous 1200px container to simulate the feel of a bespoke ledger or high-end magazine. Wide horizontal margins (64px+) are mandatory to prevent the UI from feeling cluttered or "busy."

The spacing rhythm is aggressive in its use of whitespace; large gaps between sections (128px) are encouraged to allow the marble textures to settle and provide visual relief. Internal component padding should be "refined"—giving data and text ample room to be parsed without competition from neighboring elements.

## Elevation & Depth

Hierarchy is established through **Low-Contrast Outlines** and **Tonal Layering** rather than heavy shadows. 

1.  **Surfaces:** The primary surface is a matte off-white. Secondary surfaces (cards) feature a subtle marble texture.
2.  **Borders:** A 1px Champagne Gold border is the primary indicator of a focused or elevated container.
3.  **Shadows:** When necessary for functional depth (e.g., dropdowns), use "Ambient Shadows"—extremely diffused (20-40px blur), low opacity (5-8%), and slightly tinted with Navy to keep the shadow feeling "expensive" rather than muddy.

## Shapes

The shape language of this design system is **Soft**, leaning toward the sharp end of the spectrum. A 0.25rem (4px) base radius is applied to buttons and inputs to prevent them from feeling aggressive, while maintaining the structural integrity of a serious financial tool. 

Large containers and marble cards may occasionally use the 0.5rem (8px) radius to feel more approachable, but pill-shaped elements are strictly forbidden as they conflict with the "Sophisticated-Luxe" narrative.

## Components

### Cards
Cards are the centerpiece of the investment experience. They must feature a subtle marble texture background (opacity 5-10%), a 1px Champagne Gold border, and internal padding of at least 32px. Use Noto Serif for the card title and Inter for the metadata.

### Buttons
*   **Primary:** Solid Deep Navy background with Champagne Gold text. 
*   **Secondary:** Ghost style with a 1px Gold border and Navy text.
*   **Interaction:** On hover, primary buttons should slightly deepen in tone, and secondary buttons should take on a very faint Gold tint fill.

### Inputs & Selects
Inputs use a minimal bottom-border style or a very faint grey outline. When focused, the border transitions to Champagne Gold. Labels are always positioned above the input in `label-sm` (uppercase).

### Icons
Use thin-line icons (1px stroke). Icons should never be filled; they should appear as delicate wireframes, primarily in Navy or Gold.

### Additional Components
*   **Portfolio Status Chips:** Small, rectangular chips with Gold borders and light-navy backgrounds to denote investment stages (e.g., "Closed," "Open," "Pending").
*   **Syndicate Progress Bar:** A thin, elegant 4px bar using Gold for progress and a light marble-grey for the track.