---
name: MaritimeDefense
colors:
  surface: '#f9f9ff'
  surface-dim: '#d0daf0'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d9e3f9'
  on-surface: '#121c2c'
  on-surface-variant: '#43474e'
  inverse-surface: '#273141'
  inverse-on-surface: '#ebf1ff'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#476083'
  primary: '#000613'
  on-primary: '#ffffff'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#afc8f0'
  secondary: '#5a5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dce0e0'
  on-secondary-container: '#5f6363'
  tertiary: '#090500'
  on-tertiary: '#ffffff'
  tertiary-container: '#2a1c00'
  on-tertiary-container: '#9e824f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#dfe3e2'
  secondary-fixed-dim: '#c3c7c6'
  on-secondary-fixed: '#181c1c'
  on-secondary-fixed-variant: '#434847'
  tertiary-fixed: '#ffdea5'
  tertiary-fixed-dim: '#e2c289'
  on-tertiary-fixed: '#261900'
  on-tertiary-fixed-variant: '#594316'
  background: '#f9f9ff'
  on-background: '#121c2c'
  surface-variant: '#d9e3f9'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The brand personality is anchored in unwavering authority, elite legal expertise, and a deep-rooted connection to maritime heritage. It evokes the feeling of a steady vessel in a storm—calm, robust, and technologically sophisticated. This design system communicates institutional trust and "old-world" prestige through a modern, high-performance interface.

The visual style is **Corporate / Modern** with a **Solid** architectural feel. It avoids ephemeral trends in favor of structural permanence. Layouts are governed by visible order and deliberate weight, utilizing nautical-inspired precision to guide the user through complex maritime legalities. The UI should feel like a premium physical instrument: heavy, precise, and reliable.

## Colors

The palette is derived from the elemental colors of naval command and maritime luxury.

*   **Deep Navy (Primary):** Represents the depth of the ocean and the gravity of the law. Used for navigation, primary headers, and high-importance surfaces.
*   **Seafoam White (Background):** A soft, cool-toned white that reduces eye strain during long reading sessions of legal documents while maintaining a crisp, professional atmosphere.
*   **Brass (Accent):** Inspired by nautical instruments (sextants, compasses). This is reserved for calls to action, active states, and highlights to signify value and precision.
*   **Slate Grey (Neutral):** Used for secondary text and borders to maintain a professional, low-contrast hierarchy against the Seafoam background.

## Typography

This design system employs a sophisticated dual-font strategy to balance tradition with technical clarity.

**Newsreader** is the voice of authority. Its elegant serifs are used for headlines and editorial pull-quotes, conveying the firm’s long-standing legal tradition. It should be typeset with generous leading to allow the letterforms to breathe.

**Public Sans** is the voice of the modern institution. Its neutral, clean, and highly readable proportions make it ideal for dense legal copy, fine-print clauses, and UI labels. It ensures that complex information remains accessible and transparent.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy, mirroring the structured nature of a ship’s deck plan or a maritime chart. 

*   **Grid:** A 12-column grid system with 24px gutters.
*   **Nautical Lines:** Use thin (1px) borders in a muted Navy or Brass tint to separate sections, reminiscent of latitude and longitude lines.
*   **Rhythm:** Vertical spacing is generous, using the `lg` (48px) and `xl` (80px) units to separate major content blocks, ensuring a premium, unhurried reading experience.
*   **Alignment:** Content should be strictly aligned to the grid to reinforce the feeling of "Solid" reliability.

## Elevation & Depth

To maintain the "Solid" feel, this design system avoids excessive shadows or "floating" elements. Hierarchy is instead established through **Tonal Layers** and **Bold Borders**.

*   **Surface Layers:** Use slight variations of the Seafoam White to differentiate content containers (e.g., a card may be slightly brighter than the background).
*   **Borders:** Rather than shadows, use 1px solid borders in Deep Navy (at 10% opacity) or Brass to define edges.
*   **Depth:** Reserve subtle, tight shadows only for interactive elements like buttons to signify "pressability." The overall interface should feel grounded and flat, like a physical ledger.

## Shapes

The shape language is **Sharp (0px)**. 

Rectangular forms with 90-degree angles are used throughout the design system to communicate strength, discipline, and the structural integrity of a vessel. Buttons, cards, and input fields should avoid rounded corners to maintain the authoritative, professional tone required by maritime law. 

In rare instances where a circular shape is needed (such as status indicators or iconography containers), they should be perfect circles to contrast clearly against the rigid rectangular grid.

## Components

### Buttons
Primary buttons use the **Brass** accent with Deep Navy text. They are rectangular (0px radius) with a subtle "Solid" hover state—shifting to a slightly darker brass or adding a 1px Navy offset border to simulate physical depth. Secondary buttons are "Ghost" style with a Navy outline.

### Input Fields
Inputs are defined by a bottom-only border or a full 1px border in a muted neutral. Use **Public Sans** for input text at 16px to ensure accessibility. Labels are always placed above the input in the **label-md** style (uppercase).

### Cards
Cards are used to house case studies or legal services. They have no shadow; they are distinguished by a subtle 1px border and a background color that is one shade lighter or darker than the main surface.

### Legal Documents / Lists
For complex legal copy, use wide margins and the **body-lg** typography. Bullet points should use custom "Anchor" or "Square" glyphs rather than standard circles to align with the maritime theme.

### Status Chips
Status indicators (e.g., "In Progress," "Settled," "Under Review") should use high-contrast rectangular blocks with minimal padding, utilizing the primary Navy or a professional dark green/red variant, ensuring they look like official stamps on a document.