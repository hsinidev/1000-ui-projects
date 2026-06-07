---
name: Green-Wall
colors:
  surface: '#f9faf2'
  surface-dim: '#d9dbd3'
  surface-bright: '#f9faf2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4ed'
  surface-container: '#edefe7'
  surface-container-high: '#e7e9e1'
  surface-container-highest: '#e2e3dc'
  on-surface: '#191c18'
  on-surface-variant: '#42493e'
  inverse-surface: '#2e312c'
  inverse-on-surface: '#f0f1ea'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#9f402d'
  on-secondary: '#ffffff'
  secondary-container: '#fd876f'
  on-secondary-container: '#732010'
  tertiary: '#3a3937'
  on-tertiary: '#ffffff'
  tertiary-container: '#51504e'
  on-tertiary-container: '#c5c2c0'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#ffdad3'
  secondary-fixed-dim: '#ffb4a5'
  on-secondary-fixed: '#3e0500'
  on-secondary-fixed-variant: '#802918'
  tertiary-fixed: '#e5e2df'
  tertiary-fixed-dim: '#c8c6c3'
  on-tertiary-fixed: '#1c1c1a'
  on-tertiary-fixed-variant: '#474745'
  background: '#f9faf2'
  on-background: '#191c18'
  surface-variant: '#e2e3dc'
typography:
  headline-lg:
    fontFamily: Newsreader
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Work Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.08em
  data-display:
    fontFamily: Work Sans
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  base: 8px
  margin-mobile: 24px
  margin-desktop: 64px
  gutter: 16px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built upon the concept of "Grounded Eco-Tech"—a harmonious bridge between the ancient, tactile world of gardening and the precision of smart home technology. The brand personality is nurturing, intentional, and sophisticated, targeting urban inhabitants who seek to reconnect with nature through data-driven cultivation.

The visual style utilizes a **Tactile Minimalism** approach. It avoids the clinical coldness of typical IoT applications by introducing organic "pebble" geometries and subtle natural textures, such as fine paper grain or stone-like noise. The emotional goal is to evoke the feeling of a quiet morning in a conservatory: calm, fresh, and revitalizing.

## Colors

The palette is rooted in the natural cycle of growth. **Forest Green** serves as the primary anchor, representing vitality and the plant life itself. **Terra-Cotta** is used as the secondary action color, providing a warm, clay-like contrast for critical interactions and call-to-actions. 

**Off-White** acts as the primary canvas, ensuring the interface feels breathable and light. To maintain high contrast without the harshness of pure black, a deep **Charcoal-Green** is used for primary text and iconography. Backgrounds should occasionally incorporate a very subtle "noise" overlay (2-3% opacity) to mimic organic material.

## Typography

This design system employs a sophisticated typographic pairing to balance heritage and utility. 

**Newsreader** is utilized for all editorial headings and plant names, lending a warm, literary character to the experience. Its elegant serifs provide a human touch that contrasts with the technical nature of the app. 

**Work Sans** is used for all functional data, navigation, and body copy. Its clean, stable letterforms ensure that technical specifications—such as pH levels, water humidity, and temperature—remain legible at a glance. Capitalized labels in Work Sans should be used for metadata to create a clear informational hierarchy.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** with exaggerated safe areas to promote a sense of "open space." This design system avoids cluttered interfaces by utilizing a generous 8px baseline grid. 

Mobile layouts should maintain a 24px side margin to allow the pebble-shaped cards to "float" within the viewport. Spacing between different plant modules should be significant (stack-lg) to prevent the UI from feeling congested, mimicking the physical space required for plants to thrive.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and soft, tinted shadows rather than traditional grey drop-shadows. Surfaces should appear as if they are resting gently on one another.

Shadows must be diffused and utilize a slight Forest Green tint (`rgba(45, 90, 39, 0.08)`) to maintain the earthy aesthetic. Interactive elements like buttons should use a soft "inner glow" or subtle gradient to suggest a physical, "squishy" tactile quality. Avoid harsh dividers; use shifts in background tone (Off-White to a slightly darker clay-tinted beige) to define sections.

## Shapes

The shape language of this design system is strictly **Organic and Asymmetric**. All containers, buttons, and image masks must utilize high corner radii to achieve a "pebble" or "river stone" effect.

While the variable defines a level 3 (Pill-shaped) foundation, the design system encourages using "Smoothing" or "Squircle" properties where available to avoid the mechanical look of standard geometric rounded rectangles. Buttons should be pill-shaped, while cards should use large, soft radii that feel comfortable and hand-molded.

## Components

### Buttons
Primary buttons are pill-shaped and filled with Terra-Cotta, featuring white text for high contrast. Secondary buttons use a Forest Green stroke with a light green tinted fill. The "press" state should involve a subtle scale-down effect (0.98) to enhance the tactile feel.

### Pebble Cards
Cards are the primary container. They should feature a 32px corner radius. For featured plants, the top-right corner radius can be further increased to 64px to create a unique, organic silhouette.

### Input Fields
Inputs are borderless with a soft, clay-tinted background. They should use a subtle inner shadow to look slightly recessed into the page, like a thumbprint in soil.

### Progress Gauges
Instead of linear bars, use circular "Growth Rings" or organic "Leaf Fill" icons to represent water levels and nutrient health.

### Chips/Tags
Used for plant categories (e.g., "Succulent," "Low Light"). These should be small, pill-shaped elements in Forest Green with Off-White text, appearing as small "seeds" of information.