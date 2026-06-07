---
name: TerraForge
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#dcc0b9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a48b85'
  outline-variant: '#56423d'
  surface-tint: '#ffb5a1'
  primary: '#ffb5a1'
  on-primary: '#601400'
  primary-container: '#af4e33'
  on-primary-container: '#ffe9e3'
  inverse-primary: '#9e4128'
  secondary: '#ffb77b'
  on-secondary: '#4d2700'
  secondary-container: '#7a4100'
  on-secondary-container: '#ffb270'
  tertiary: '#c8c6c5'
  on-tertiary: '#303030'
  tertiary-container: '#6c6b6b'
  on-tertiary-container: '#efedec'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbd1'
  primary-fixed-dim: '#ffb5a1'
  on-primary-fixed: '#3b0900'
  on-primary-fixed-variant: '#7f2b13'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#ffb77b'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6d3a00'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 8px
  gutter: 24px
  margin-edge: 40px
  section-gap: 120px
---

## Brand & Style
This design system centers on "Primal Sophistication." It targets high-net-worth individuals who value the intersection of raw nature and precision engineering. The UI must evoke the feeling of standing on a stone patio at dusk—warm, substantial, and permanent.

The aesthetic is a hybrid of **Tactile Minimalism** and **High-Contrast Brutalism**. We utilize realistic material textures—specifically oxidized metal, honed basalt, and flickering embers—to create a sense of physical weight. The UI is not "digital-first"; it is "material-first," behaving like a high-end physical architectural spec book. Every interaction should feel deliberate and heavy, moving away from the ephemeral lightness of traditional SaaS.

## Colors
The palette is rooted in the earth and the forge. The default mode is **Dark**, utilizing a deep Charcoal and Matte Black base to simulate the night sky or scorched earth, allowing the warmer tones to glow.

- **Deep Terracotta (#AF4E33):** The primary action color, representing fired clay and heat. Use for key CTAs.
- **Brushed Copper (#B87333):** The accent color, used for metallic highlights, interactive states, and refined details.
- **Matte Black (#121212) & Charcoal (#2C2C2C):** These form the structural foundation, used for backgrounds and depth layering.
- **Textured Overlays:** Incorporate a subtle 5% opacity grain or noise texture over all background surfaces to eliminate "flat" digital blacks.

## Typography
The typography contrasts architectural permanence with modern utility. 

**Noto Serif** is used for headlines to provide a literary, high-end feel. It should be typeset with tight tracking in larger sizes to feel like stone-carved lettering. **Work Sans** provides a rugged, industrial balance for body copy, ensuring legibility against textured backgrounds. Use the **Label-Caps** style for navigation items and technical specifications to mimic architectural blueprints.

## Layout & Spacing
This design system uses a **Fixed Grid** philosophy. Content is contained within a centered 12-column track to create a sense of intentionality and "built" structure. 

The spacing rhythm is expansive. We use large "Section Gaps" (120px+) to allow the high-contrast imagery and textures room to breathe. Elements are grouped using a strict 8px base unit, but global layout focuses on asymmetrical balance—mimicking the way a fire pit or stone wall is positioned within a natural landscape.

## Elevation & Depth
Elevation is achieved through **Tonal Layering** and physical metaphors rather than soft shadows.

- **The Forge Floor (Base):** Matte Black (#121212) with a grain texture.
- **The Plinth (Surface):** Charcoal (#2C2C2C) with a subtle 1px Brushed Copper border on the top edge only, simulating light hitting the rim of a metal object.
- **Active Elements:** Instead of shadows, use "inner glow" effects in Deep Terracotta to simulate heat emanating from within a component.
- **Overlays:** Use a heavy backdrop blur (20px+) combined with a 40% opaque Matte Black fill to create a "smoked glass" effect for modals.

## Shapes
The shape language is **Sharp (0)**. There are no rounded corners in this design system. Every element—buttons, cards, inputs—must feature 90-degree angles to reinforce the architectural and "forged" nature of the brand. This hard-edged approach communicates strength, precision, and durability.

## Components
Consistent styling across the interface should follow these rules:

- **Buttons:** Rectangular, no radius. Primary buttons are solid Deep Terracotta with white text. Secondary buttons are "Ghost" style with a 2px Brushed Copper border. Hover states should trigger a "glow" transition rather than a simple color change.
- **Input Fields:** Bottom-border only (2px Charcoal). When focused, the border transitions to Brushed Copper with a subtle flicker animation.
- **Cards:** No shadows. Use a solid Charcoal background with a 1px Matte Black border. Imagery within cards should have a slight vignette to pull the focus inward.
- **Chips/Tags:** Small, rectangular boxes with "Label-Caps" typography. Use a dark red background for "Hot" or "New" items.
- **Navigation:** Top-tier navigation uses high-letter-spaced Work Sans. Active links are indicated by a 2px Copper underline that spans the full width of the text.
- **Specialty Component - "The Hearth":** A signature container for featured content that uses a subtle animated fire-glow gradient (Terracotta to Copper) as its background.