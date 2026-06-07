---
name: Botanist-Glow
colors:
  surface: '#e8fdfe'
  surface-dim: '#c9dedf'
  surface-bright: '#e8fdfe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e3f8f8'
  surface-container: '#ddf2f3'
  surface-container-high: '#d7eced'
  surface-container-highest: '#d2e6e7'
  on-surface: '#0b1e1f'
  on-surface-variant: '#42493e'
  inverse-surface: '#213435'
  inverse-on-surface: '#e0f5f6'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#4d6265'
  on-secondary: '#ffffff'
  secondary-container: '#d0e7ea'
  on-secondary-container: '#53686b'
  tertiary: '#37393a'
  on-tertiary: '#ffffff'
  tertiary-container: '#4e5051'
  on-tertiary-container: '#c2c2c3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#d0e7ea'
  secondary-fixed-dim: '#b4cbce'
  on-secondary-fixed: '#091f21'
  on-secondary-fixed-variant: '#364a4d'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#e8fdfe'
  on-background: '#0b1e1f'
  surface-variant: '#d2e6e7'
typography:
  display-lg:
    fontFamily: EB Garamond
    fontSize: 48px
    fontWeight: '500'
    lineHeight: 56px
    letterSpacing: -0.01em
  display-lg-mobile:
    fontFamily: EB Garamond
    fontSize: 36px
    fontWeight: '500'
    lineHeight: 42px
  headline-md:
    fontFamily: EB Garamond
    fontSize: 32px
    fontWeight: '400'
    lineHeight: 40px
  headline-sm:
    fontFamily: EB Garamond
    fontSize: 24px
    fontWeight: '400'
    lineHeight: 32px
  body-lg:
    fontFamily: Hanken Grotesk
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Hanken Grotesk
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Hanken Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.1em
  data-mono:
    fontFamily: Hanken Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
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
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style

This design system embodies the intersection of artisanal craft and modern apothecary luxury. The brand personality is sophisticated, knowledgeable, and refreshing, evoking the sensory experience of a high-end botanical laboratory. The target audience values transparency in ingredients and the tactile beauty of premium spirits.

The visual style is a hybrid of **Soft-UI (Neumorphism)** and **Glassmorphism**. It utilizes organic, pebble-like shapes to mimic nature, while employing high-transparency layers and subtle surface extrusions to create a "frosted glass" effect. The UI feels tactile and "squishy" yet remains airy and premium through the use of extensive whitespace and botanical illustrations.

## Colors

The palette is rooted in a "Botanical Laboratory" aesthetic. 

- **Leaf Green (#2D5A27)**: Used as the primary brand anchor for high-importance actions, headings, and signature botanical accents.
- **Glass-Cyan (#E0F7FA)**: The core of the glassmorphism effect. It is used for large surface areas, subtle overlays, and background washes to evoke the clarity of premium gin and laboratory glassware.
- **Pure White (#FFFFFF)**: Provides the crisp, clean canvas necessary for a luxury feel, used primarily for light-source highlights in neumorphic elements and high-contrast text backgrounds.
- **Neutral (#4A5D5E)**: A desaturated slate used for secondary text and UI icons to maintain legibility without the harshness of pure black.

## Typography

The typography strategy contrasts the heritage of gin production with the precision of a modern lab. 

**EB Garamond** serves as the display typeface, providing an elegant, literary, and premium feel for all headings. For UI elements, data visualization, and long-form body text, **Hanken Grotesk** offers a clean, contemporary, and highly legible sans-serif counterpoint. 

Use expanded letter spacing for small labels and uppercase descriptors to reinforce the "clinical luxury" aesthetic. Headline weights should remain relatively light (400-500) to maintain an airy, sophisticated profile.

## Layout & Spacing

This design system utilizes a **fixed grid** model for desktop to maintain the premium, curated feel of a luxury editorial, and a **fluid grid** for mobile to ensure usability.

- **Desktop**: 12-column grid, 1280px max width, centered. Large margins (64px) allow the botanical illustrations to "breathe" in the periphery.
- **Mobile**: 4-column fluid grid with 20px margins.
- **Rhythm**: All spacing follows an 8px base unit. Component internal padding should be generous (24px+) to avoid crowding the organic shapes.

Layouts should favor asymmetrical compositions and staggered vertical positioning to mimic the natural growth patterns of plants.

## Elevation & Depth

Depth is achieved through two distinct techniques used in tandem:

1.  **Neumorphic Surfaces**: Primary UI containers use "Soft-UI" extrusions. A light source is assumed to be in the top-left, creating a #FFFFFF highlight on the top-left edge and a soft, tinted shadow (using a 10% opacity of the Leaf Green) on the bottom-right. These should be very subtle to appear "molded" from the background.
2.  **Glassmorphic Overlays**: Floating elements like navigation bars, modals, and tooltips use a backdrop filter blur (15px - 25px) combined with the Glass-Cyan (#E0F7FA) at 40-60% opacity. A thin, 1px white border with 20% opacity should define the edges of these glass elements.

## Shapes

The shape language is strictly **organic**. Avoid hard corners or standard geometric rectangles. 

- Use **rounded (0.5rem - 1.5rem)** corners for all standard cards and containers to create a "pebble" or "river stone" feel.
- **Pill-shapes** are reserved for interactive elements like buttons and chips.
- Use **clipping paths** or mask botanical illustrations with irregular, fluid blobs to break the grid and add visual interest.

## Components

- **Buttons**: Primary buttons are Leaf Green with white text, using a pill-shape and a subtle neumorphic "press" effect (inset shadow) on active states.
- **Cards**: Cards should utilize the "Glass-Cyan" transparency with a backdrop blur. They should not have heavy borders; instead, use the neumorphic soft shadows for definition.
- **Input Fields**: Fields appear as "sunken" or concave shapes (inset neumorphic shadows) rather than outlined boxes. Use Hanken Grotesk for input text.
- **Chips/Filters**: Small, pill-shaped elements with a Glass-Cyan background and Leaf Green text.
- **Progress Indicators**: Use fluid, "water-filling" animations for progress bars to align with the gin/infusion lab theme.
- **Botanical Accents**: Floating, high-quality botanical illustrations (leaves, juniper berries, herbs) should be placed behind or partially overlapping glass containers to demonstrate the transparency and depth of the UI.