---
name: Imperial Heritage
colors:
  surface: '#fff8f4'
  surface-dim: '#e0d9d4'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf2ed'
  surface-container: '#f4ede8'
  surface-container-high: '#eee7e2'
  surface-container-highest: '#e8e1dc'
  on-surface: '#1e1b18'
  on-surface-variant: '#554240'
  inverse-surface: '#33302d'
  inverse-on-surface: '#f7efea'
  outline: '#89726f'
  outline-variant: '#dcc0bd'
  surface-tint: '#9d4139'
  primary: '#210000'
  on-primary: '#ffffff'
  primary-container: '#4a0404'
  on-primary-container: '#d26a5f'
  inverse-primary: '#ffb4aa'
  secondary: '#775a19'
  on-secondary: '#ffffff'
  secondary-container: '#fed488'
  on-secondary-container: '#785a1a'
  tertiary: '#0b0b07'
  on-tertiary: '#ffffff'
  tertiary-container: '#22221d'
  on-tertiary-container: '#8b8982'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad5'
  primary-fixed-dim: '#ffb4aa'
  on-primary-fixed: '#410001'
  on-primary-fixed-variant: '#7e2b23'
  secondary-fixed: '#ffdea5'
  secondary-fixed-dim: '#e9c176'
  on-secondary-fixed: '#261900'
  on-secondary-fixed-variant: '#5d4201'
  tertiary-fixed: '#e5e2da'
  tertiary-fixed-dim: '#c9c6be'
  on-tertiary-fixed: '#1c1c17'
  on-tertiary-fixed-variant: '#474741'
  background: '#fff8f4'
  on-background: '#1e1b18'
  surface-variant: '#e8e1dc'
typography:
  headline-display:
    fontFamily: Newsreader
    fontSize: 4.5rem
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 3rem
    fontWeight: '500'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Newsreader
    fontSize: 2.25rem
    fontWeight: '500'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Newsreader
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: '1.7'
  body-md:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  label-md:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '500'
    lineHeight: '1.2'
spacing:
  base: 8px
  container-max: 1280px
  gutter: 32px
  margin-edge: 64px
  section-gap: 128px
---

## Brand & Style

This design system establishes an atmosphere of lineage, authority, and timelessness. The brand personality is "The Custodian"—a protector of history and excellence. It targets high-net-worth individuals, elite breeders, and institutional historians who value pedigree over trends.

The visual style is **Archival Tactile**. It blends the structural integrity of a traditional museum exhibition with the warmth of a private library. UI elements should feel like physical artifacts: heavy paper stock, gold-leaf inlays, and leather-bound detailing. High whitespace is used not for modernity, but for reverence, allowing photography of the breeds to take center stage as "portraits" rather than mere assets.

## Colors

The palette is rooted in classical heraldry. 
- **Parchment (#F5F2E9)** serves as the primary canvas, replacing stark white to reduce digital fatigue and evoke the feel of aged vellum.
- **Deep Burgundy (#4A0404)** is used for primary actions and structural headers, providing a sense of gravitas and administrative power.
- **Gold (#C5A059)** is reserved for accents, seals of authenticity, and high-tier status indicators. 
- **Neutral Dark (#2C2926)** is utilized for body text to ensure maximum legibility against the parchment background while maintaining a softer contrast than pure black.

## Typography

The typographic scale relies on a sharp contrast between the authoritative **Newsreader** (Serif) and the functional **Inter** (Sans-Serif). 

Headlines should utilize Newsreader's italic styles for emphasis, particularly in historical quotes or breed descriptions. Inter is used strictly for utility, data-heavy tables, and long-form reading to ensure the platform feels efficient despite its traditional aesthetic. All "Label-Caps" should be transformed to uppercase to denote category titles or metadata headers, mimicking the look of engraved plates.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model to maintain an editorial, book-like feel. Content is centered within a generous container, surrounded by wide margins that suggest luxury and "unhurried" navigation. 

Vertical rhythm is intentionally spacious. Sections are separated by significant gaps (128px) to prevent the interface from feeling cluttered or "app-like." Information density should remain low; prioritize clarity and "breathing room" for high-resolution archival photography.

## Elevation & Depth

Depth is conveyed through **Tonal Layering and Physicality** rather than modern ambient shadows. 

1.  **The Base:** The Parchment (#F5F2E9) background acts as the lowest level.
2.  **Raised Surfaces:** Use a very thin, 1px solid border in Gold or a slightly darker Parchment shade (#E0DBCB) to define cards. 
3.  **Inset Depth:** Search bars and input fields should feel "pressed" into the paper, achieved through subtle inner shadows or 1px inset borders.
4.  **The "Seal":** Important buttons or status badges should use a "stamped" effect, sitting atop the surface with a crisp, low-blur shadow (e.g., 2px offset, 4px blur, 10% opacity black) to suggest they have been physically placed there.

## Shapes

The shape language is strictly **Sharp (0)**. 

To maintain the prestige of a traditional registry, avoid rounded corners on buttons, cards, and images. Sharp 90-degree angles communicate discipline, structure, and permanence. Decorative elements may include "double-line" borders or notched corners (clipped edges) to evoke the appearance of vintage certificates and official ledgers.

## Components

*   **Buttons:** Rectangular with no radius. Primary buttons are Deep Burgundy with Gold text. Secondary buttons use a Deep Burgundy 1px outline with no fill.
*   **Input Fields:** Minimalist with a bottom border only, or a full 1px border in a muted tone. Use the Label-Caps style for field titles.
*   **Cards:** "Registry Cards" for individual animals should feature a thin Gold border, a large archival-style photo, and centered serif typography.
*   **Chips/Tags:** Used sparingly. These should look like small wax seals or stamped ink marks—no background fill, just a small icon and uppercase text.
*   **Archival Dividers:** Use horizontal rules with a decorative center diamond or fleur-de-lis motif to separate long-form content.
*   **Pedigree Trees:** A custom component using thin, rigid lines (1px) to connect ancestral nodes, emphasizing the structural "bloodline" of the data.
*   **Photography:** Images should utilize a subtle grain overlay and a slightly desaturated "sepia-lite" or high-contrast black-and-white filter to maintain the heritage aesthetic.