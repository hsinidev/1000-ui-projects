---
name: Amber-Rare
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
  on-surface-variant: '#e0c0b2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#a78b7e'
  outline-variant: '#584238'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#562000'
  primary-container: '#ea6b1e'
  on-primary-container: '#4b1b00'
  inverse-primary: '#a04100'
  secondary: '#ffb77b'
  on-secondary: '#4d2700'
  secondary-container: '#7a4100'
  on-secondary-container: '#ffb270'
  tertiary: '#e9c349'
  on-tertiary: '#3c2f00'
  tertiary-container: '#cca830'
  on-tertiary-container: '#4f3e00'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#ffdcc2'
  secondary-fixed-dim: '#ffb77b'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#6d3a00'
  tertiary-fixed: '#ffe088'
  tertiary-fixed-dim: '#e9c349'
  on-tertiary-fixed: '#241a00'
  on-tertiary-fixed-variant: '#574500'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353535'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 64px
    fontWeight: '700'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '600'
    lineHeight: 48px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-md:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '500'
    lineHeight: 36px
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-sm:
    fontFamily: Work Sans
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
  container-max: 1280px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style

This design system establishes a high-end, digital concierge experience for the rare whiskey and bourbon market. The aesthetic is **Moody & Warm**, drawing inspiration from the amber hues of aged spirits and the low-light ambiance of a private tasting room. 

The design style is a hybrid of **Tactile Minimalism and Glassmorphism**. It utilizes realistic textures—liquid ripples, polished glass, and brushed metal—set against a strictly structured, dark minimalist framework. Every interaction should feel intentional and exclusive, evoking the sense of a premium physical exchange. The UI disappears to highlight the liquid assets, using high-contrast photography to drive the emotional connection to the product.

## Colors

The palette is anchored in the deep, nocturnal tones of an oak-aged cellar. 

- **Primary (Burnt Orange):** Used for primary actions and to signify heat or "spirit." It represents the core color of premium bourbon.
- **Secondary (Polished Copper):** Reserved for accents, borders, and metallic finishes. It provides a tactile, industrial-luxe feel.
- **Neutral (Deep Charcoal):** The foundation of the entire UI. It creates the "moody" atmosphere and allows high-contrast photography to pop.
- **Tertiary (Metallic Gold):** Used sparingly for status indicators of high-tier rarity or exclusive membership badges.

Avoid pure white; for text and icons, use a "Warm Silver" (#E5E5E5) or "Antique Parchment" (#F5F5DC) at reduced opacities to maintain the low-light aesthetic.

## Typography

Typography in this design system balances traditional craftsmanship with modern utility. 

**Playfair Display** is the editorial voice. It should be used for headlines, product names, and quotes. Use its italic variant to highlight years or limited edition series names to add a touch of sophistication.

**Work Sans** serves as the functional engine. It provides a clean, neutral contrast to the serif headings, ensuring that technical data—such as proof, age, and market price—is highly legible. 

All labels and small metadata should use **Work Sans** with increased letter spacing and uppercase styling to mimic the "tax strip" or label detailing found on vintage bottles.

## Layout & Spacing

The layout follows a **Fixed Grid** model on desktop to maintain a boutique, curated feel, preventing the content from feeling "stretched" or utilitarian. 

- **Desktop:** 12-column grid with a 1280px max-width. Use wide margins (64px+) to create a sense of luxury and breathing room.
- **Tablet:** 8-column grid with 32px margins. 
- **Mobile:** 4-column grid with 20px margins.

Spacing should be generous. Use vertical rhythm to separate "chapters" of content (e.g., product story vs. technical specs). Components should utilize an 8px base unit, favoring larger increments (32px, 48px, 64px) to emphasize exclusivity and avoid a cluttered, retail-heavy appearance.

## Elevation & Depth

This design system uses **Tonal Layers and Glassmorphism** to create depth without relying on traditional heavy shadows.

- **The Base:** The Deep Charcoal (#1A1A1A) acts as the deepest layer.
- **Surface Containers:** Use a slightly lighter charcoal (#242424) for cards and containers, differentiated by a 1px "Polished Copper" border at 20% opacity.
- **Glass Overlays:** For navigation bars and modal overlays, use a backdrop-filter blur (20px) with a semi-transparent black fill. This mimics the look of a heavy glass bottle.
- **Metallic Highlights:** Instead of shadows, use subtle top-edge inner glows (linear gradients of #B87333 to transparent) on buttons and cards to simulate light hitting a copper edge.

## Shapes

The shape language is **Soft (Level 1)**. 

Rectangular forms with subtle 0.25rem (4px) rounding suggest the weight and stability of a square decanter. Avoid high-radius or pill-shaped buttons as they appear too casual for this brand's premium positioning. 

Secondary elements like "Quick View" cards or tooltip containers can scale up to `rounded-lg` (8px) to feel more approachable, but the primary architectural elements of the site should remain sharp and disciplined. Copper accents should be applied as thin, 1px strokes rather than thick blocks of color.

## Components

- **Buttons:** Primary buttons use a solid **Burnt Orange** fill with **Antique Parchment** text. Secondary buttons are "Ghost" style with a 1px **Polished Copper** border and a subtle hover glow.
- **Input Fields:** Dark backgrounds with a bottom-only border in Polished Copper. Labels should float and utilize the `label-sm` typography style.
- **Cards:** Product cards must feature high-contrast photography. The card itself should have no shadow but a faint 1px border. On hover, the border opacity should increase, and the metallic highlight should brighten.
- **Chips/Tags:** Used for "Limited Edition" or "Barrel Proof." These should be small, rectangular with 2px rounding, using the `label-sm` font.
- **Liquid Scrollbar:** Custom-styled scrollbars should be thin, using Polished Copper for the thumb to mimic the "legs" of a whiskey glass.
- **Rarity Indicator:** A custom component—a vertical "thermometer" or meter—rendered in a metallic gradient to show current market availability.