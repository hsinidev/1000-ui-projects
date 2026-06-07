---
name: Agave-Elite
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
  on-surface-variant: '#56423d'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#89726c'
  outline-variant: '#dcc0b9'
  surface-tint: '#9d4226'
  primary: '#9a4024'
  on-primary: '#ffffff'
  primary-container: '#ba573a'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb59f'
  secondary: '#006a6a'
  on-secondary: '#ffffff'
  secondary-container: '#90efef'
  on-secondary-container: '#006e6e'
  tertiary: '#605b57'
  on-tertiary: '#ffffff'
  tertiary-container: '#79736f'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb59f'
  on-primary-fixed: '#3b0a00'
  on-primary-fixed-variant: '#7e2b11'
  secondary-fixed: '#93f2f2'
  secondary-fixed-dim: '#76d6d5'
  on-secondary-fixed: '#002020'
  on-secondary-fixed-variant: '#004f4f'
  tertiary-fixed: '#e9e1dc'
  tertiary-fixed-dim: '#cdc5c0'
  on-tertiary-fixed: '#1e1b18'
  on-tertiary-fixed-variant: '#4b4642'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  display:
    fontFamily: Metropolis
    fontSize: 64px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Metropolis
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Metropolis
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Metropolis
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Libre Caslon Text
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Libre Caslon Text
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-lg:
    fontFamily: Metropolis
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  label-sm:
    fontFamily: Metropolis
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system targets the discerning spirits connoisseur, blending the raw, earthy heritage of artisanal distillation with high-end, modern architectural precision. The brand personality is authoritative yet tactile, evoking the feeling of a premium lifestyle magazine or a contemporary gallery in Mexico City. 

The visual style is **Modern Architectural with a High-Contrast Bento-Box influence**. It prioritizes structural integrity through rigid grid systems and bold, clean lines. Every element feels deliberate and grounded, utilizing heavy imagery of agave fields, copper stills, and textured glassware to create a sensory-rich experience. The UI is fast, responsive, and tactile, designed to feel like a high-end physical portfolio.

## Colors

The palette is derived from the natural elements of mezcal production: the earth, the plant, and the artisanal process.

- **Terracotta (#C05C3E):** The primary brand color. Used for calls to action, highlights, and to represent the baked earth and "pina" roasting process.
- **Teal (#008080):** The secondary color. Represents the blue-green hue of the Agave Tequilana. Used for navigational elements and subtle accents.
- **Off-White (#F9F7F2):** The canvas. This warm neutral provides a "lifestyle paper" feel, preventing the high-contrast layout from feeling clinical.
- **Deep Charcoal (#2D2926):** Used for primary text and structural lines to ensure high-contrast legibility and a grounded, architectural feel.

## Typography

This design system utilizes a high-contrast typographic pairing to reinforce its "Modern Architectural" and "Lifestyle Magazine" themes.

- **Headlines (Metropolis):** Geometric, bold, and unapologetic. Headlines should be treated as structural elements. Use tight letter-spacing for large display text to mimic architectural signage.
- **Body Text (Libre Caslon Text):** Elegant and scholarly. The serif typeface provides a literary warmth that balances the coldness of the geometric headers. It is used for storytelling, product descriptions, and long-form content.
- **Labels (Metropolis):** All caps and tracked out for a premium, utilitarian feel. Used for navigation, metadata, and buttons.

## Layout & Spacing

The design system employs a **Bento-Box layout** strategy rooted in a 12-column fixed grid. Content is organized into modular containers (cells) of varying sizes that snap to a strict rhythm.

- **The Bento Grid:** Components should be housed in high-contrast blocks. On mobile, these stack vertically; on desktop, they tile to fill the screen width.
- **Margins & Gutters:** Generous margins (32px) ensure the content feels premium and uncrowded. Gutters (24px) provide clear definition between bento cells.
- **Structural Lines:** Use 1px or 2px borders (Deep Charcoal) to define sections instead of relying on shadows, emphasizing the architectural blueprint aesthetic.

## Elevation & Depth

To maintain the architectural feel, this design system avoids traditional soft shadows. Depth is achieved through **Tonal Layering and Bold Outlines**.

- **Flat Stack:** Elements do not "float"; they are layered like physical materials.
- **High-Contrast Borders:** Use 1.5pt solid borders in Deep Charcoal or Teal to define interactive surfaces.
- **Active State Elevation:** When an element is pressed or hovered, it should not lift. Instead, use an "inset" effect or a solid color fill change (e.g., a card background switching from Off-White to Terracotta) to indicate interaction.
- **Glassmorphism:** Use sparingly for mobile navigation overlays. A subtle backdrop blur (12px) over high-resolution imagery maintains the "fast and modern" feel without sacrificing the premium aesthetic.

## Shapes

The shape language is strictly **Sharp (0px)**. This reinforces the architectural and modern boutique theme. Curves are reserved exclusively for the natural organic shapes within photography (agave leaves, bottle silhouettes).

- **Containers:** All bento-box cells and buttons must have 90-degree corners.
- **Interactive Elements:** Buttons and input fields are rectangular, emphasizing the "bold clean lines" of the brand.
- **Image Treatment:** Photos should be cropped into sharp rectangles or squares to fit the grid perfectly.

## Components

- **Buttons:** Sharp-edged, solid color fills (Terracotta or Teal) with Metropolis bold uppercase text. For secondary actions, use "Ghost" buttons with a 2px border.
- **Bento Cards:** High-contrast containers with Off-White backgrounds and Charcoal borders. Every card should feature either a high-resolution image or a bold headline.
- **Input Fields:** Minimalist. A single bottom border in Charcoal. Labels sit above in Metropolis (Label-sm). Error states use a darker shade of Terracotta.
- **Chips/Tags:** Small rectangular blocks with solid Teal backgrounds and white text. No rounded corners.
- **Product Lists:** Visual-heavy. Use large images that take up 70% of the card height, with the product name and price in Libre Caslon Text at the bottom.
- **Navigation:** A fixed, slim architectural header. On mobile, use a full-screen "Bento Menu" that tiles categories like "Tequila," "Mezcal," and "Artisans" into clickable blocks.
- **Fast Interactive Feel:** Use instant state transitions. Hovering over a card should trigger a subtle zoom of the internal image or a solid background color shift.