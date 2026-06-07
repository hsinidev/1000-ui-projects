---
name: Bio-Habitat Design System
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
  on-surface-variant: '#45483c'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#76786b'
  outline-variant: '#c6c8b8'
  surface-tint: '#52652a'
  primary: '#33450d'
  on-primary: '#ffffff'
  primary-container: '#4a5d23'
  on-primary-container: '#bed58e'
  inverse-primary: '#b8cf88'
  secondary: '#725a38'
  on-secondary: '#ffffff'
  secondary-container: '#fcdaaf'
  on-secondary-container: '#775e3c'
  tertiary: '#3f3f3f'
  on-tertiary: '#ffffff'
  tertiary-container: '#575656'
  on-tertiary-container: '#cecbcb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4eca2'
  primary-fixed-dim: '#b8cf88'
  on-primary-fixed: '#141f00'
  on-primary-fixed-variant: '#3b4d14'
  secondary-fixed: '#ffddb2'
  secondary-fixed-dim: '#e1c298'
  on-secondary-fixed: '#291800'
  on-secondary-fixed-variant: '#594323'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  h1:
    fontFamily: Playfair Display
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-tabular:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  gutter: 16px
  margin-mobile: 20px
---

## Brand & Style

This design system is built for the intersection of high-end architectural precision and ecological stewardship. The brand personality is **Lush & Grounded**, prioritizing a visceral connection to the natural world while maintaining the rigorous clarity required for sustainable engineering. It targets eco-conscious developers, regenerative architects, and sustainability-focused investors.

The visual style is a **Tactile-Minimalist** hybrid. It utilizes organic UI shapes—avoiding harsh geometric perfection in favor of soft, asymmetrical "blobs" and rounded containers—to mimic biological forms. The UI must feel alive; this is achieved through "Breathe" animations, which are rhythmic, low-frequency scaling and opacity pulses applied to hero elements and primary call-to-actions, simulating a slow pulmonary cycle. The interface should evoke a sense of calm, structural integrity, and environmental harmony.

## Colors

The palette is derived from a forest floor at dawn, balancing deep botanical tones with warm, structural neutrals.

- **Primary (Moss Green):** Used for primary actions, success states, and brand-critical iconography. It represents growth and vitality.
- **Secondary (Raw Wood):** Applied to structural accents, focus states, and secondary interactive elements. It provides a tactile, earthy warmth.
- **Tertiary (Earthy Charcoal):** Reserved for high-contrast typography and technical data displays to ensure legibility.
- **Neutral (Off-White):** The foundational canvas. It replaces stark pure whites to reduce eye strain and provide a softer, more organic backdrop.

Use moss-tinted transparencies (e.g., 10% opacity Moss Green) for hover states on light backgrounds to maintain the "lush" aesthetic without adding visual weight.

## Typography

This design system employs a high-contrast typographic pairing to distinguish between narrative and data.

- **Headlines:** Playfair Display provides a sophisticated, editorial feel. Use it for storytelling, section headers, and quotes. Its serif nature conveys the "architectural" heritage of the brand.
- **Body & Data:** Inter is used for all functional information, technical specifications, and dense data tables. It is chosen for its exceptional legibility on mobile devices and its neutral, "invisible" character that doesn't compete with the organic visual style.
- **Data Density:** In mobile views, prioritize Inter at smaller scales (14px) with increased letter-spacing for technical labels to maintain clarity within tight layouts.

## Layout & Spacing

The layout philosophy follows a **Fluid Organic Grid**. While technical data is aligned to a strict 8px rhythm for precision, the container edges and decorative elements break the grid slightly to feel less "manufactured."

- **Mobile-First:** Use a 4-column fluid grid for mobile with 20px outer margins.
- **Desktop:** Transition to a 12-column grid with a max-width of 1440px. 
- **Rhythm:** Use "md" (24px) for standard component spacing to ensure the "Breathe" animations have enough clearance to scale without overlapping adjacent elements. 
- **Dividers:** Traditional lines are replaced by leaf-patterned SVG dividers or subtle Raw Wood-colored horizontal rules that taper at the ends.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Ambient Shadows** rather than high-contrast borders.

- **Surface Tiers:** The base layer is Off-White. Secondary containers (cards, sidebars) use a slightly darker "Paper" tint or a very subtle Moss Green wash (2% opacity).
- **Shadows:** Use diffused, low-opacity shadows tinted with Moss Green (`rgba(74, 93, 35, 0.08)`). This prevents the UI from looking "dirty" and reinforces the botanical theme.
- **Tactile Depth:** Elements like buttons or active cards should appear slightly inset or "engraved" into the Raw Wood surfaces, using inner shadows to simulate a physical, carved texture.

## Shapes

The shape language is primarily **Rounded (0.5rem base)**, but utilizes "Soft Blobs" for larger background containers and image masks.

- **Component Radius:** Buttons and inputs use a consistent 8px (0.5rem) radius.
- **Container Radius:** Cards and modals use 16px (1rem) to 24px (1.5rem) to feel approachable.
- **Organic Masks:** For hero imagery or featured architectural renders, use non-perfect circular paths (blobs) to soften the transition between the rigid architecture and the natural environment.

## Components

- **Buttons:** Primary buttons are Moss Green with Off-White text. Use a subtle "Breathe" scale effect (scale 1.02) on hover. Secondary buttons use a Raw Wood outline.
- **Chips:** Small, pill-shaped tags for "Sustainability Ratings" or "Material Types." Use light Moss Green backgrounds with Earthy Charcoal text.
- **Input Fields:** Off-White background with a 1px Raw Wood border. On focus, the border thickens and glows with a soft Moss Green ambient shadow.
- **Cards:** Use high-density layouts for architectural specs (SQFT, Carbon Offset, Material Origin) using Inter at 12px-14px. Headers within cards remain Playfair Display.
- **Leaf-Patterned Dividers:** Custom SVG dividers that mimic a vine or row of leaves, used to separate major content sections vertically.
- **Breathe Animations:** Applied to "In-Stock" indicators or "Live Performance" metrics. A gentle pulse of opacity (from 100% to 70%) every 4 seconds.
- **Data Tables:** High-density, Earthy Charcoal text on Off-White, with alternating row highlights in a very faint Moss Green.