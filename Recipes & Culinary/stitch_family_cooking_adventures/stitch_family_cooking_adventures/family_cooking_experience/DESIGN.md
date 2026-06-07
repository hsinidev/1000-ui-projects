---
name: Family Cooking Experience
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
  on-surface-variant: '#4d4732'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#7e775f'
  outline-variant: '#d0c6ab'
  surface-tint: '#705d00'
  primary: '#705d00'
  on-primary: '#ffffff'
  primary-container: '#ffd700'
  on-primary-container: '#705e00'
  inverse-primary: '#e9c400'
  secondary: '#0c6780'
  on-secondary: '#ffffff'
  secondary-container: '#9ae1ff'
  on-secondary-container: '#09657f'
  tertiary: '#904d00'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffd1af'
  on-tertiary-container: '#914d00'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe16d'
  primary-fixed-dim: '#e9c400'
  on-primary-fixed: '#221b00'
  on-primary-fixed-variant: '#544600'
  secondary-fixed: '#baeaff'
  secondary-fixed-dim: '#89d0ed'
  on-secondary-fixed: '#001f29'
  on-secondary-fixed-variant: '#004d62'
  tertiary-fixed: '#ffdcc3'
  tertiary-fixed-dim: '#ffb77d'
  on-tertiary-fixed: '#2f1500'
  on-tertiary-fixed-variant: '#6e3900'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  headline-xl:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '700'
    lineHeight: '1.2'
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-page: 32px
  stack-sm: 12px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

The brand personality of this design system is exuberant, inclusive, and fundamentally joyful. It aims to transform the kitchen from a place of chores into a digital playground where families bond. The target audience includes parents looking for accessible activities and children who need high-legibility, high-contrast interfaces that feel like a game rather than a manual.

The design style is **Tactile / High-Contrast**. It utilizes physical metaphors—buttons that look "squishy" and cards that feel like thick paper—to create a kid-safe environment that encourages exploration. Organic, "blob" shapes and hand-drawn elements break the rigidity of standard digital interfaces, evoking a sense of creativity and mess-friendly fun.

## Colors

The palette is built on a "Sunshine and Sky" foundation. The Primary Yellow (#FFD700) is used for high-energy interactions and focal points, while the Sky Blue (#87CEEB) provides a calming but friendly secondary base for containers and secondary actions. 

Energetic accents of Orange and Lime Green are reserved for success states, gamified progress, and interactive highlights. To maintain a "soft" feel, pure black is avoided in favor of a deep Charcoal Neutral (#4A4A4A), and the background uses a warm Off-White (#FFFDF5) to reduce eye strain and feel more organic than a stark digital white.

## Typography

This design system utilizes **Plus Jakarta Sans** for its inherently soft terminal endings and optimistic geometry. The type scale is intentionally oversized to accommodate younger readers and parents multi-tasking in a busy kitchen.

Headlines are set with extra-bold weights to create a strong visual hierarchy, while body text maintains a generous 20px size for maximum legibility at arm's length (e.g., when a tablet is sitting on a counter). Tight letter spacing is used on large headlines to give them a "sticker-like" compact feel, while body copy is given ample line height to prevent the interface from feeling cluttered.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with "Chunky" constraints. The content is organized in a 12-column system, but with significantly larger gutters (24px) than standard applications to ensure that touch targets are isolated and easy to hit for smaller fingers.

Spacing rhythm is based on an 8px base unit, but most component spacing uses multiples of 3 (24px, 48px) to create a more open, breathable feel. Large page margins (32px+) ensure that the UI never feels cramped against the edge of the device, reinforcing the "safe" and friendly aesthetic.

## Elevation & Depth

Depth is communicated through **Ambient Shadows** that are color-tinted rather than neutral gray. Instead of traditional "lift," objects in this design system appear to be slightly raised stickers or soft plastic blocks resting on a surface.

Shadows are characterized by:
- **Low Blur:** Keeps the edges feeling crisp and intentional.
- **Color Tints:** Shadows under a blue card will have a subtle blue hue to maintain the vibrancy of the palette.
- **Offset Depth:** A consistent 4px or 8px vertical offset is used to give buttons a "pressable" appearance. When hovered or pressed, the shadow offset reduces to 0px, simulating physical compression.

## Shapes

The shape language is the core of the design system's friendliness. We utilize **Pill-shaped (Level 3)** roundedness for almost all containers and interactive elements. 

Beyond simple radii, the system encourages the use of **Organic Blobs**—irregular, non-geometric shapes—for background decorations and image masks. This breaks the "computer-like" feel of the interface. All containers must have a minimum border-radius of 24px, ensuring there are no sharp "scary" corners anywhere in the family experience.

## Components

### Buttons
Buttons are "Chunky." They feature a 4px solid bottom border (or a deep shadow) to give them a 3D effect. The Primary button is Yellow with a dark charcoal label. On active states, the button shifts down 4px to simulate a physical click.

### Simplified Recipe Cards
Recipe cards strip away complex metadata. They prioritize a large, rounded image and a bold title. Visual "Quick Stats" (like time or difficulty) are presented as colorful hand-drawn chips rather than plain text. 

### Gamified Achievement Badges
Badges are circular or organic-shaped icons featuring thick outlines and vibrant gradients. They use the hand-drawn icon style to feel like physical stickers earned during a cooking lesson.

### Input Fields & Controls
Inputs use extra-thick borders (2px+) and 32px corner radii. Focus states are indicated by a thick Sky Blue outer glow. Sliders and toggles are oversized, utilizing large "thumb" handles that are easy to drag for users of all ages.

### Lists
Lists are treated as a series of stacked, high-radius cards rather than simple rows with dividers. This creates a "collection" feel that is more engaging and tactile.