---
name: EarthPulse
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#414844'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3f6653'
  primary: '#012d1d'
  on-primary: '#ffffff'
  primary-container: '#1b4332'
  on-primary-container: '#86af99'
  inverse-primary: '#a5d0b9'
  secondary: '#116c4a'
  on-secondary: '#ffffff'
  secondary-container: '#a1f4c8'
  on-secondary-container: '#1b724f'
  tertiary: '#3a2017'
  on-tertiary: '#ffffff'
  tertiary-container: '#52352b'
  on-tertiary-container: '#c79d90'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c1ecd4'
  primary-fixed-dim: '#a5d0b9'
  on-primary-fixed: '#002114'
  on-primary-fixed-variant: '#274e3d'
  secondary-fixed: '#a1f4c8'
  secondary-fixed-dim: '#86d7ad'
  on-secondary-fixed: '#002113'
  on-secondary-fixed-variant: '#005236'
  tertiary-fixed: '#ffdbcf'
  tertiary-fixed-dim: '#e9bdae'
  on-tertiary-fixed: '#2d150d'
  on-tertiary-fixed-variant: '#5e3f35'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
---

## Brand & Style

This design system is built upon an "Eco-Modern" philosophy, blending the urgent necessity of global reforestation with the sophisticated clarity of modern technology. The brand personality is authoritative yet optimistic, designed to inspire collective action through transparency and beauty.

The visual style is a hybrid of **Minimalism** and **Tactile Organicism**. It prioritizes high-contrast layouts and generous whitespace to ensure that data regarding environmental impact remains the focal point. To prevent the interface from feeling clinical, the design system introduces organic, non-geometric containers and soft textures that mimic the natural world, grounding the digital experience in the physical reality of the earth.

## Colors

The palette is derived from the stratification of a healthy forest. 

- **Deep Forest Green (#1B4332)**: Used for primary branding, deep backgrounds, and high-level headings to provide a sense of stability and depth.
- **Leaf Green (#40916C)**: Reserved exclusively for action-oriented elements (CTAs, success states, and progress indicators). It represents growth and vitality.
- **Earthy Brown (#6D4C41)**: An accent color used for secondary information, borders, or text elements that require a softer contrast than black.
- **Off-White (#F8F9FA)**: The primary canvas color. This provides a clean, breathable environment that makes the forest tones feel more vibrant.

Maintain a high contrast ratio between Leaf Green and Off-White to ensure all interactive elements exceed AA accessibility standards.

## Typography

This design system utilizes **Inter** for all typographic layers to ensure maximum readability and a systematic, modern feel. The hierarchy is designed with a "High-Impact" approach, utilizing tight letter-spacing and bold weights for headlines to create a sense of urgency and importance.

For long-form educational content, body text utilizes an increased line-height (1.6) to prevent eye fatigue. Labels and secondary metadata should be rendered in uppercase with slight tracking to provide a clear distinction from narrative content.

## Layout & Spacing

The layout follows a **fixed-grid** model for desktop experiences, centering content within a 1280px container to maintain visual impact. A 12-column grid provides the structural foundation, with generous 24px gutters to allow the organic shapes of the UI to breathe without crowding.

The spacing rhythm is strictly based on an 8px baseline. Large-scale sections should be separated by significant vertical padding (e.g., 80px or 120px) to reinforce the "Minimalist" aesthetic and give the imagery room to resonate.

## Elevation & Depth

To align with the "Eco-Modern" theme, this design system avoids harsh, artificial shadows. Instead, it employs **Tonal Layers** and **Ambient Tinted Shadows**. 

Depth is primarily created by stacking Off-White containers onto very subtle Earthy Brown or Forest Green tinted backgrounds. When shadows are necessary for interactivity (such as on hover), use a long, diffused blur with a low-opacity green tint (`rgba(27, 67, 50, 0.08)`) to mimic the soft, dappled light of a forest floor rather than a digital drop shadow.

## Shapes

The shape language is the core of the "Eco-Modern" aesthetic. While the underlying grid is rigid, the UI elements are **Organic**. 

- **Standard Elements**: Buttons and input fields use a consistent 0.5rem (8px) radius.
- **Containers**: Cards and feature sections should utilize "blob-like" properties—specifically, slightly asymmetrical border-radii (e.g., `60% 40% 70% 30% / 40% 50% 60% 40%`) to mimic natural forms like stones or leaves.
- **Dividers**: Traditional horizontal rules are replaced with subtle, repeating leaf-pattern SVG masks that create a soft, textured transition between sections.

## Components

### Buttons
Primary actions are rendered in **Leaf Green** with white text. They should feature a subtle "expansion" animation on hover, reinforcing the theme of growth. Secondary buttons use a Deep Forest Green outline with no fill.

### Cards
Cards are the primary vehicle for project transparency. They must use the organic, asymmetrical border-radii described in the Shapes section. Images within cards should always use an object-fit cover to ensure the photography feels immersive.

### Dividers
Section breaks should incorporate the leaf-patterned SVG. These are not mere lines but "organic fringes" that break the horizontal plane, making the transition between background colors feel like a natural edge.

### Input Fields
Forms should be clean and minimalist. Use a thick 2px bottom border in Earthy Brown for the resting state, transitioning to Leaf Green on focus. 

### Impact Metrics
A specialized component for EarthPulse, these are large-format typography blocks paired with organic "blob" backgrounds in very light tints of Leaf Green to highlight key reforestation statistics.