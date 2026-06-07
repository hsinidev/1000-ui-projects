---
name: Terra & Tail
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e4e2e1'
  on-surface: '#1b1c1c'
  on-surface-variant: '#444841'
  inverse-surface: '#303030'
  inverse-on-surface: '#f3f0f0'
  outline: '#757870'
  outline-variant: '#c5c8be'
  surface-tint: '#54634c'
  primary: '#526049'
  on-primary: '#ffffff'
  primary-container: '#6a7961'
  on-primary-container: '#f8ffee'
  inverse-primary: '#bccbb0'
  secondary: '#7f5537'
  on-secondary: '#ffffff'
  secondary-container: '#ffc6a1'
  on-secondary-container: '#7a5033'
  tertiary: '#5c5c58'
  on-tertiary: '#ffffff'
  tertiary-container: '#757571'
  on-tertiary-container: '#fefcf7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d8e8cb'
  primary-fixed-dim: '#bccbb0'
  on-primary-fixed: '#121f0d'
  on-primary-fixed-variant: '#3d4b35'
  secondary-fixed: '#ffdcc6'
  secondary-fixed-dim: '#f2bb97'
  on-secondary-fixed: '#301400'
  on-secondary-fixed-variant: '#643e22'
  tertiary-fixed: '#e4e2dd'
  tertiary-fixed-dim: '#c8c6c2'
  on-tertiary-fixed: '#1b1c19'
  on-tertiary-fixed-variant: '#474744'
  background: '#fcf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e1'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.25'
  h3:
    fontFamily: Noto Serif
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
---

## Brand & Style

This design system centers on a "Modern Organic" aesthetic, designed to evoke feelings of tranquility, transparency, and premium care. The target audience is the discerning pet owner who values sustainability as much as nutritional integrity. 

The visual direction is **Tactile Minimalism**. It avoids the sterility of pure digital minimalism by introducing soft textures, natural color shifts, and physical metaphors. The interface should feel like high-quality recycled stationery—refined, grounded, and unmistakably premium. Every element is designed to build trust through clarity and a gentle, non-aggressive presence.

## Colors

The palette is derived from a natural landscape. The Primary **Sage Green** (#7D8C73) represents growth and health, used for key actions and brand moments. The Secondary **Warm Wood** (#B58463) provides a grounding, earthy contrast for accents and secondary buttons.

The background system relies on **Soft Cream** (#F9F7F2) instead of pure white to reduce eye strain and enhance the "recycled paper" feel. **Charcoal** (#2C2C2C) is reserved for typography to ensure AA accessibility while remaining softer than pure black. Decorative accents may use a desaturated leaf green for success states and a muted clay for warnings.

## Typography

The typographic pairing balances heritage and modern utility. **Noto Serif** is used for headlines to convey a sense of editorial authority and timeless quality. Its sophisticated serifs should be set with slightly tight tracking in large formats to feel cohesive.

**Be Vietnam Pro** serves as the workhorse for all interface elements and body copy. Chosen for its warm, open counters and approachable geometry, it ensures high legibility on mobile devices. Use the "label-caps" style for small metadata or section headers to provide a clear structural hierarchy without overwhelming the page.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy on desktop to maintain a curated, editorial feel, transitioning to a fluid system on mobile. We utilize a 12-column grid with generous gutters to promote "plenty of whitespace," which is essential for the premium brand positioning.

Spacing follows an 8px linear scale. Vertical rhythm should prioritize large "breathing rooms" between sections (64px to 96px) to prevent the interface from feeling cluttered or transactional. Group related elements tightly using 8px or 16px increments to create clear visual associations.

## Elevation & Depth

This design system avoids harsh dropshadows. Instead, it utilizes **Ambient Shadows**—soft, diffused, and slightly tinted with the Primary Sage Green color. These shadows should look like light hitting a physical object on a matte surface.

- **Level 1 (Cards):** 0px 4px 20px rgba(125, 140, 115, 0.08)
- **Level 2 (Dropdowns/Modals):** 0px 12px 32px rgba(125, 140, 115, 0.12)

Depth is also achieved through **Tonal Layers**. Elements can sit on a slightly darker cream or a very pale sage background to create separation without needing a border or shadow.

## Shapes

The shape language is "Organic Geometric." While the grid is structured, individual components use a **Rounded** (0.5rem base) corner radius to feel safe and friendly. Large containers like product cards or hero imagery should use `rounded-xl` (1.5rem) to emphasize the soft, approachable nature of the brand. Avoid sharp 90-degree angles entirely to maintain the eco-friendly, "soft-edge" aesthetic.

## Components

### Buttons
Primary buttons use the Sage Green background with white text. Secondary buttons use a "ghost" style with a 1.5px Warm Wood border. All buttons feature a 500ms transition on hover, subtly deepening the background color or increasing the shadow spread.

### Input Fields
Inputs are defined by a soft cream background slightly darker than the page, with a bottom-only 2px border in a muted charcoal. This creates a "stationary" feel. Focus states transition the border to Sage Green.

### Chips & Tags
Used for dietary attributes (e.g., "Grain-Free," "Organic"). These should be pill-shaped with a low-opacity Sage Green fill and dark text.

### Icons
Icons must be **monoline and organic**. Lines should have slightly rounded caps and ends. Avoid complex fills; use a 1.5pt stroke weight consistently.

### Cards
Cards are the primary container for products. They should have no visible border, using only the Level 1 Ambient Shadow and a 1.5rem corner radius. Imagery within cards should have a slight "warmth" filter to align with the Warm Wood tones.

### Progress Indicators
For checkout or subscription setups, use a custom "growing leaf" or simple organic dot motif instead of standard industrial bars.