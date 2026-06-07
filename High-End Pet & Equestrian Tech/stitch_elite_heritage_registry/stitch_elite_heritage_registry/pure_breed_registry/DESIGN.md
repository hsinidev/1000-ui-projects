---
name: Pure-Breed Registry
colors:
  surface: '#fff8f5'
  surface-dim: '#e3d8d1'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fef1eb'
  surface-container: '#f8ece5'
  surface-container-high: '#f2e6df'
  surface-container-highest: '#ece0da'
  on-surface: '#201a17'
  on-surface-variant: '#584141'
  inverse-surface: '#362f2b'
  inverse-on-surface: '#fbeee8'
  outline: '#8c7071'
  outline-variant: '#e0bfbf'
  surface-tint: '#af2b3e'
  primary: '#570013'
  on-primary: '#ffffff'
  primary-container: '#800020'
  on-primary-container: '#ff828a'
  inverse-primary: '#ffb3b5'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#2a271d'
  on-tertiary: '#ffffff'
  tertiary-container: '#403d32'
  on-tertiary-container: '#ada899'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdada'
  primary-fixed-dim: '#ffb3b5'
  on-primary-fixed: '#40000b'
  on-primary-fixed-variant: '#8e0f28'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e9e2d2'
  tertiary-fixed-dim: '#ccc6b7'
  on-tertiary-fixed: '#1e1c12'
  on-tertiary-fixed-variant: '#4a473b'
  background: '#fff8f5'
  on-background: '#201a17'
  surface-variant: '#ece0da'
typography:
  display-lg:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Bodoni Moda
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-md:
    fontFamily: Libre Franklin
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Libre Franklin
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  container-max: 1140px
  gutter: 32px
  margin-edge: 48px
  section-padding: 80px
---

## Brand & Style

The design system is anchored in the heritage of elite equestrian and canine lineage. It evokes the atmosphere of an exclusive private library or a high-end auction house. The emotional response is one of absolute trust, historical significance, and prestige. 

The visual language follows a **Tactile / Skeuomorphic** approach, where digital elements are treated as physical artifacts. Interfaces are not merely "screens" but are presented as hand-laid parchment documents, leather-bound ledgers, and engraved gold plates. High-contrast archival photography—using sepia or deep-tonal black and white—reinforces the sense of a multi-generational legacy.

## Colors

The palette is a sophisticated trio that mimics traditional materials:
- **Deep Burgundy (#800020):** Used for primary actions and "Executive" headers, representing the wax seals of official certificates and fine leather bindings.
- **Parchment (#F5F5DC / #FCF5E5):** The foundation of the design system. It serves as the primary canvas, replacing flat white with a subtle, textured cream that reduces digital eye strain and adds historical weight.
- **Gold (#D4AF37):** Reserved for ornamentation, borders, and "Verified" status indicators. It should be applied with restraint to maintain its "precious metal" value.

Neutral tones are grounded in deep charcoals and umbers rather than pure blacks to maintain a warm, organic feel.

## Typography

This design system utilizes a high-contrast typographic pairing to balance tradition with modern legibility.

- **Headlines:** `Bodoni Moda` provides the dramatic vertical contrast and elegant serifs necessary for an elite registry. Display sizes should leverage tight tracking, while titles should occasionally use italics for a "hand-notated" look.
- **Body & Metadata:** `Libre Franklin` is chosen for its clarity and authoritative, neutral stance. It ensures that complex pedigree data remains legible at small sizes. 
- **Labels:** Small caps with increased letter-spacing are used for categorization to mimic the look of traditional library indexing.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model, centering content like a focused document on a desk. This design system avoids edge-to-edge fluid layouts, preferring defined "canvases" with generous outer margins.

- **The Document Frame:** Main content is often housed in a container that simulates a physical sheet of paper, with consistent internal padding of 48px to 64px.
- **Symmetry:** Layouts should lean toward centered vertical axes, especially for landing pages and certificate views, echoing traditional formal announcements.
- **Negative Space:** Whitespace (or "Parchment space") is used aggressively to signify luxury. No element should feel crowded; the rhythm is slow and deliberate.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layers** and **Tactile Textures** rather than modern drop shadows.

- **The Surface:** The lowest level is a dark, leather-textured background (#2A2420).
- **The Document:** Content sits on "Parchment" containers that use a subtle inner-glow and a very fine 1px gold or sienna border to suggest thickness.
- **Engraving:** Text and icons should appear slightly "pressed" into the paper (subtle 1px offset highlight) or "embossed" for premium buttons.
- **Interactive States:** Instead of floating higher, interactive elements might show a slight change in texture grain or a more pronounced gold foil edge.

## Shapes

The shape language is strictly **Sharp (0)**. 

To maintain the "Archival" aesthetic, rounded corners are avoided. Corners are crisp, suggesting cut paper and hardbound books. When a container must be enclosed, use a fine "double-line" border (a thin gold line followed by a hairline burgundy line) to create a frame effect. 

The only exceptions are "Seal" elements (e.g., status badges), which should be perfectly circular to mimic wax seals or official stamps.

## Components

- **Buttons:** Styled as "Seal Actions." Primary buttons are Deep Burgundy with gold-leaf serif text. They have no corner radius. On hover, the gold border thickens slightly.
- **Input Fields:** Designed as "ledger lines." There are no boxes; instead, a single bottom border (Burgundy) with a Parchment background. The label sits above in Libre Franklin Caps.
- **Cards (The Pedigree Card):** These should feel like physical index cards. They feature a fine gold border, a subtle paper grain texture, and archival-style photography with a slight vignette.
- **Status Chips:** Use a "Wax Seal" metaphor. Circular, slightly irregular edges, in Burgundy or Gold, with a small serif initial or icon inside.
- **Lists:** Data lists should look like a directory ledger, using alternate row shading in a slightly darker Parchment tone and vertical hairline separators.
- **Certificates (Special Component):** A full-screen view that applies an ornate, floral gold-filigree border around the viewport, intended for viewing a breed's formal lineage.