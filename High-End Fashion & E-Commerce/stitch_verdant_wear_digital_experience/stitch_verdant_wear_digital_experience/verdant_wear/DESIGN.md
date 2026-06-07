---
name: Verdant-Wear
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbd9d9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#eae8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#414844'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#78582f'
  on-secondary: '#ffffff'
  secondary-container: '#fed39f'
  on-secondary-container: '#795930'
  tertiary: '#242628'
  on-tertiary: '#ffffff'
  tertiary-container: '#393c3d'
  on-tertiary-container: '#a5a6a7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#ffddb7'
  secondary-fixed-dim: '#eabf8d'
  on-secondary-fixed: '#2a1700'
  on-secondary-fixed-variant: '#5e411a'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  data-ui:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

This design system is built for a high-end, eco-conscious audience that values the intersection of luxury craftsmanship and environmental stewardship. The brand personality is grounded, sophisticated, and transparent. 

The aesthetic follows an **Organic Minimalism** style. It rejects the clinical sharpness of traditional tech interfaces in favor of soft, natural geometries and tactile warmth. High-quality photography featuring models in natural environments is central to the visual narrative. Every interaction should feel intentional and calm, evoking the stillness of a forest floor rather than the frantic pace of fast fashion.

## Colors

The palette is derived directly from the natural world to reinforce the brand's eco-consciousness. 

- **Primary (Deep Forest Green):** Used for primary actions, branding, and high-impact headers. It represents stability and the brand's core mission.
- **Secondary (Natural Wood/Sand):** Used for accents, call-to-action highlights, and subtle borders. It provides a warm, tactile contrast to the deep green.
- **Surface (Soft Off-White):** The primary canvas color. It is softer on the eyes than pure white, providing a "paper-like" quality that feels premium and organic.
- **Status Colors:** Use muted versions of standard status colors (e.g., a sage green for success, a terracotta for errors) to ensure they do not clash with the earthy palette.

## Typography

This design system utilizes a high-contrast typographic pairing to balance heritage luxury with modern functionalism.

- **Headings:** **Noto Serif** is used for all editorial and storytelling headers. Its classic proportions convey the "luxury" aspect of the brand. Use wide tracking for display sizes to enhance the premium feel.
- **UI & Data:** **Manrope** provides a clean, highly legible sans-serif for functional data, navigation, and dense information. Its geometric but friendly nature keeps the UI feeling contemporary and accessible. Use uppercase styling for labels and small UI hints to create a distinct separation from narrative text.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to maintain a curated, editorial appearance. Content is centered within a 1440px container with generous side margins to create a sense of exclusivity and breathability.

A 12-column grid is used for desktop, while a 4-column grid is used for mobile. Spacing follows an 8px base unit, but section vertical spacing should be exceptionally generous (e.g., 120px+) to allow the photography and organic shapes room to breathe. Avoid overcrowding elements; transparency in the supply chain should be mirrored by "transparency" in the layout via whitespace.

## Elevation & Depth

To maintain the organic feel, this design system avoids heavy, artificial shadows. Instead, it uses **Tonal Layers** and **Ambient Depth**:

- **Layering:** Use subtle shifts in background color (e.g., moving from the Off-White background to a very light Sand surface) to indicate hierarchy.
- **Shadows:** When necessary, use extremely diffused, low-opacity shadows tinted with the Deep Forest Green (#1B4332) rather than pure black. This makes the shadows feel like they are part of a natural environment with ambient light.
- **Glassmorphism:** Use soft backdrop blurs (10px–20px) for navigation overlays and modals to maintain a connection to the nature-integrated photography underneath.

## Shapes

The shape language is the primary differentiator of this design system. It moves away from standard rectangles in favor of **Organic Geometry**:

- **Standard Elements:** Buttons and input fields use a medium-high roundedness (0.5rem to 1rem) to feel soft to the touch.
- **Organic Blobs:** Large UI containers or image masks should utilize asymmetrical, "blob-like" shapes to mimic natural forms like stones or leaves.
- **Dividers:** Traditional horizontal lines are replaced with leaf-patterned or "rough-edge" dividers that look like deckled paper or organic growth.

## Components

### Buttons
Primary buttons are solid Deep Forest Green with White text. Secondary buttons use the Sand color for a border or background. All buttons have a high-pill radius and hover states that involve a slight organic "swell" (scale) rather than just a color change.

### Chips & Tags
Used for material types (e.g., "Organic Cotton") and eco-labels. These should have a sand-colored background and use the `data-ui` typography style for high scannability.

### Cards
Cards do not have borders. They use a slightly darker off-white or sand tint to differentiate from the background, featuring soft-radius corners and high-quality imagery.

### Input Fields
Outlined with a thin, low-contrast Sand border. On focus, the border thickens slightly and changes to Deep Forest Green. Use the Manrope font for all user-inputted data.

### Special Components
- **Sustainability Tracker:** A visual component using organic progress bars (tapered, leaf-like shapes) to show the eco-impact of a specific garment.
- **Nature Dividers:** SVG-based leaf patterns used to separate long-form content sections.