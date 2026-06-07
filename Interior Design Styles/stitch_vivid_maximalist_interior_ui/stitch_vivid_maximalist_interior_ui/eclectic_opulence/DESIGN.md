---
name: Eclectic Opulence
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#20201f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353535'
  on-surface: '#e5e2e1'
  on-surface-variant: '#bfcab8'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8a9483'
  outline-variant: '#40493c'
  surface-tint: '#84db74'
  primary: '#84db74'
  on-primary: '#003a01'
  primary-container: '#046307'
  on-primary-container: '#87de76'
  inverse-primary: '#166d13'
  secondary: '#e9c349'
  on-secondary: '#3c2f00'
  secondary-container: '#af8d11'
  on-secondary-container: '#342800'
  tertiary: '#ffb2be'
  on-tertiary: '#660026'
  tertiary-container: '#aa0045'
  on-tertiary-container: '#ffb6c2'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#9ff88d'
  primary-fixed-dim: '#84db74'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#005303'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#ffd9de'
  tertiary-fixed-dim: '#ffb2be'
  on-tertiary-fixed: '#3f0015'
  on-tertiary-fixed-variant: '#900039'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 80px
    fontWeight: '700'
    lineHeight: 90px
    letterSpacing: -0.02em
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
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
  gutter: 24px
  margin-page: 64px
  overlap-sm: -24px
  overlap-lg: -48px
---

## Brand & Style

This design system embodies a "more is more" philosophy, tailored for high-end interior design where personality and curation are paramount. The brand personality is fearless, sophisticated, and deeply tactile. It targets an audience that values bespoke craftsmanship and isn't afraid of bold color or historical layers.

The visual style is **Tactile and High-Contrast**, leaning heavily into physical metaphors. It utilizes rich textures—such as gold foil and deep velvet-like backgrounds—to create a sense of digital luxury. The UI is intentionally dense and layered, moving away from flat minimalism to embrace an eclectic mix of patterns and ornate details while maintaining a professional, structured finish.

## Colors

The palette is anchored by a deep **Emerald Green** primary, used for large structural surfaces to provide a grounding, lush environment. **Gold** serves as the primary accent, utilized for interactive elements, decorative borders, and foil-textured highlights. 

Secondary jewel tones—**Sapphire**, **Amethyst**, and **Ruby**—are used as "zonal" colors to differentiate various collections or service tiers. To ensure accessibility and readability, text is primarily rendered in **Parchment** (an off-white) or **Gold** against these dark, saturated backgrounds. Backgrounds should frequently incorporate bold, dark-themed floral patterns where the jewel tones intersect, ensuring that contrast ratios never dip below 4.5:1 for body text and 3:1 for decorative headers.

## Typography

This design system utilizes a high-contrast typographic pairing to balance editorial flair with modern usability. 

**Newsreader** is the expressive engine of the system. Used for all headings and display text, it brings a literary, authoritative, and classic interior-design-journal aesthetic. Its high stroke contrast allows it to stand out against busy floral backgrounds.

**Manrope** provides a clean, functional counterpoint for body copy, navigation, and labels. It is chosen for its geometric clarity and high legibility at smaller scales, ensuring that even within a maximalist layout, the core information remains accessible. All labels and buttons use a bold weight of Manrope with increased letter spacing to ensure they aren't lost among decorative elements.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model (12-column) but introduces intentional "visual noise" through **overlapping and layered elements**. While the underlying structure is rigid to ensure professional alignment, components are frequently offset using negative spacing (`overlap-sm` and `overlap-lg`) to break the grid's containment.

Spacing is generous to prevent the maximalist aesthetic from feeling cluttered. Large page margins create a "frame" effect, similar to a matted photograph. Elements should feel stacked, as if they were physical samples on an interior designer's mood board.

## Elevation & Depth

Hierarchy is established through **Physical Stacking and Ambient Shadows**. Instead of generic grey shadows, this design system uses deep, tinted shadows (e.g., a Sapphire-tinted shadow on a Sapphire background) to maintain color richness.

1.  **Base Layer:** Rich floral patterns or solid Emerald surfaces.
2.  **Middle Layer:** Content cards with semi-opaque jewel-tone backgrounds.
3.  **Top Layer:** Interactive elements, gold foil-bordered callouts, and floating images.

Decorative gold foil borders (1px to 2px) act as a "lift" mechanism, highlighting the topmost interactive layer. Backdrop blurs are used sparingly to suggest depth through "frosted glass" effects on modal overlays, but the primary depth indicator remains the hard-edged overlap of opaque, textured surfaces.

## Shapes

The design system utilizes **Soft** roundedness (0.25rem / 4px). This subtle rounding mimics the finished edges of high-end furniture or custom cabinetry—not sharp enough to be aggressive, but not round enough to feel "bubbly" or informal.

Decorative elements may utilize more complex shapes, such as arched frames for imagery (reminiscent of architectural doorways) or circular gold seals for badges. Buttons and input fields remain strictly rectangular with the standard soft-radius to maintain a professional, architectural foundation.

## Components

### Buttons
Primary buttons are styled with a **Gold Foil texture** background and dark Emerald text. They use a bold weight of the body font. Secondary buttons use a thick 2px Gold border with transparent backgrounds and Gold text.

### Cards
Cards are the primary vehicle for the "layered" look. They should feature 1px Gold borders and can sit on top of floral backgrounds. Images within cards often extend beyond the top or side border of the card itself to create a 3D effect.

### Input Fields
Inputs use high-contrast Parchment backgrounds with deep Emerald text. When focused, the border transitions from a thin neutral to a thick 2px Gold foil border.

### Decorative Dividers
Standard horizontal rules are replaced by ornate, gold-leaf-inspired SVG dividers or simple thin gold lines with a central floral icon.

### Chips & Tags
Chips use the secondary jewel tones (Ruby, Sapphire, Amethyst) to categorize content. They are always high-saturation with white or parchment text to ensure high visibility.

### Navigation
The navigation bar should feel like a solid architectural element, utilizing a deep Jewel tone background with a gold-leaf bottom border that remains fixed as the user scrolls through the layered content.