---
name: Artisanal Harvest
colors:
  surface: '#fcf9f3'
  surface-dim: '#dcdad4'
  surface-bright: '#fcf9f3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ed'
  surface-container: '#f0eee8'
  surface-container-high: '#ebe8e2'
  surface-container-highest: '#e5e2dc'
  on-surface: '#1c1c18'
  on-surface-variant: '#424844'
  inverse-surface: '#31312d'
  inverse-on-surface: '#f3f0ea'
  outline: '#727973'
  outline-variant: '#c2c8c2'
  surface-tint: '#496455'
  primary: '#173124'
  on-primary: '#ffffff'
  primary-container: '#2d4739'
  on-primary-container: '#98b5a3'
  inverse-primary: '#b0cdbb'
  secondary: '#94492c'
  on-secondary: '#ffffff'
  secondary-container: '#fe9d7a'
  on-secondary-container: '#773318'
  tertiary: '#1f3017'
  on-tertiary: '#ffffff'
  tertiary-container: '#35462c'
  on-tertiary-container: '#9fb492'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ccead6'
  primary-fixed-dim: '#b0cdbb'
  on-primary-fixed: '#062014'
  on-primary-fixed-variant: '#324c3e'
  secondary-fixed: '#ffdbcf'
  secondary-fixed-dim: '#ffb59b'
  on-secondary-fixed: '#380d00'
  on-secondary-fixed-variant: '#763217'
  tertiary-fixed: '#d4e9c4'
  tertiary-fixed-dim: '#b8cdaa'
  on-tertiary-fixed: '#101f09'
  on-tertiary-fixed-variant: '#3a4c31'
  background: '#fcf9f3'
  on-background: '#1c1c18'
  surface-variant: '#e5e2dc'
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
    lineHeight: '1.3'
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
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
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.4'
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
  margin-desktop: 64px
---

## Brand & Style

This design system targets the conscious consumer who values transparency, sustainability, and the tactile quality of local produce. The brand personality is grounded, honest, and sophisticated—evoking the feeling of a high-end farmers' market rather than a digital supermarket.

The visual style is a **Tactile / Minimalist** hybrid. It utilizes a generous use of whitespace to ensure a premium, "clean" aesthetic, while integrating subtle organic textures and hand-drawn elements to emphasize the "farm-to-table" narrative. The emotional response should be one of calm trust and physical connection to the earth.

## Colors

The color strategy centers on a foundational "Oatmeal" and "Paper" backdrop to maintain cleanliness. 
- **Primary (Forest):** Used for primary actions, navigation, and core branding to ground the interface in nature.
- **Secondary (Terracotta):** Reserved for accent moments, such as seasonal highlights, sale badges, or call-to-action buttons that require warmth.
- **Tertiary (Sage):** Used for success states, secondary categories, and subtle backgrounds.
- **Neutrals:** The "Bark" color replaces pure black for typography to keep the contrast soft and organic.

Apply a subtle, low-opacity noise grain or "paper" texture to the main background surfaces to enhance the artisanal feel.

## Typography

The typography pairing balances rustic charm with modern accessibility. **Noto Serif** provides an editorial, handcrafted feel for headlines, suggesting quality and tradition. **Be Vietnam Pro** is used for body copy and UI labels; its warm, friendly terminals and high legibility ensure that the shopping experience remains effortless and contemporary. 

Use sentence case for most headings to maintain a humble, approachable tone. Use all-caps with increased tracking for labels and small metadata to provide structural clarity.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to ensure content remains centered and curated, like a printed catalog. 
- Use an 8-pixel scale for all padding and margins.
- Implement a 12-column grid with wide 24px gutters to allow the product photography to breathe.
- Maximize whitespace between sections (e.g., 80px–120px) to prevent the earthy color palette from feeling heavy or cluttered.
- Layouts should prioritize high-quality, unclipped product imagery that often breaks the grid slightly for a more organic, less "templated" appearance.

## Elevation & Depth

Depth is conveyed through **Ambient Shadows** and tonal layering rather than harsh lines. 
- **Surface Tiers:** Use the "Oatmeal" neutral for the base background, with "Paper" (pure white-ish) for cards and floating elements.
- **Shadows:** Shadows should be extremely soft, using a Forest or Bark tint instead of pure black (e.g., `rgba(45, 71, 57, 0.08)`). This keeps the elevation feeling like natural light hitting paper.
- **Physicality:** Use subtle inner shadows on input fields to suggest they are "pressed" into the paper surface.

## Shapes

The shape language is defined by **Rounded** corners that mimic the soft curves found in nature. 
- Avoid sharp 90-degree angles to maintain the "organic" brand pillar.
- **Standard UI elements:** Use a 0.5rem (8px) radius.
- **Featured Cards/Images:** Use a 1rem (16px) radius to create a softer, more inviting container.
- **Icons:** Icons must be hand-drawn or "rough-cut" styles with slightly irregular line weights to reinforce the artisanal narrative.

## Components

- **Buttons:** Primary buttons use a solid Forest green with Noto Serif text for a premium feel. Secondary buttons use a Sage outline with a 1px "hand-drawn" stroke style.
- **Cards:** Product cards use a Paper background with a soft shadow. Use Noto Serif for the product title and Be Vietnam Pro for the price and weight metadata.
- **Input Fields:** Soft Oatmeal fill with a subtle 1px border in Sage. Focus states should transition the border to Forest.
- **Chips/Badges:** Use "organic" shapes—pill-shaped but with slightly irregular curves—for categories like "Organic," "Local," or "Gluten-Free."
- **Hand-drawn Accents:** Use small, illustrative flourishes (like a leaf or a hand-drawn underline) for "Best Seller" or "Farmer's Choice" sections.
- **Quantity Pickers:** Use a tactile design with large touch targets and Forest green icons for incrementing/decrementing.