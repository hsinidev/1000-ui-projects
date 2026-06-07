---
name: Tactile Maximalism
colors:
  surface: '#11131c'
  surface-dim: '#11131c'
  surface-bright: '#373943'
  surface-container-lowest: '#0c0e17'
  surface-container-low: '#191b24'
  surface-container: '#1d1f29'
  surface-container-high: '#282933'
  surface-container-highest: '#32343e'
  on-surface: '#e1e1ef'
  on-surface-variant: '#c4c5d9'
  inverse-surface: '#e1e1ef'
  inverse-on-surface: '#2e303a'
  outline: '#8e90a2'
  outline-variant: '#434656'
  surface-tint: '#b8c3ff'
  primary: '#b8c3ff'
  on-primary: '#002388'
  primary-container: '#2e5bff'
  on-primary-container: '#efefff'
  inverse-primary: '#124af0'
  secondary: '#d4bbff'
  on-secondary: '#3e127e'
  secondary-container: '#583298'
  on-secondary-container: '#c8aaff'
  tertiary: '#00e299'
  on-tertiary: '#003823'
  tertiary-container: '#007d53'
  on-tertiary-container: '#bcffd8'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b8c3ff'
  on-primary-fixed: '#001356'
  on-primary-fixed-variant: '#0035be'
  secondary-fixed: '#ebdcff'
  secondary-fixed-dim: '#d4bbff'
  on-secondary-fixed: '#260058'
  on-secondary-fixed-variant: '#563096'
  tertiary-fixed: '#4bffb4'
  tertiary-fixed-dim: '#00e299'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005235'
  background: '#11131c'
  on-background: '#e1e1ef'
  surface-variant: '#32343e'
typography:
  display-lg:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
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
  margin: 40px
  stack-gap: 16px
  touch-target-min: 48px
---

## Brand & Style

This design system is engineered for an immersive VR learning environment where digital objects possess physical weight and "squish." The brand personality is hyper-expressive, energetic, and sensory-focused, moving away from flat digital conventions toward a "Tactile Maximalism" aesthetic. 

The target audience consists of lifelong learners and students who require high engagement in virtual spaces. The UI evokes a sense of comfort and playfulness through "inflatable" geometry, making the daunting task of learning feel like a tactile exploration. The visual style blends **Glassmorphism** with **Skeuomorphic** physical metaphors, ensuring every interactive element looks like it could be squeezed, pressed, or caught.

## Colors

The palette utilizes a "Deep Space" foundation to provide maximum contrast for neon-inflected accents. 
- **Electric Blue (Primary):** Used for core action states and primary "inflatable" volumes.
- **Soft Lavender (Secondary):** Applied to secondary information paths and decorative depth layers.
- **Neon Mint (Accent):** Reserved for success states, active progress indicators, and "hot" interactive zones.
- **Deep Layered Background:** A dark, desaturated navy that acts as the infinite void, allowing glass surfaces to catch light and cast soft, colored shadows.

## Typography

The design system utilizes **Lexend** exclusively due to its origins in reading proficiency and its inherently rounded, friendly terminals that match the "pillowy" UI. 
- **Scale:** High contrast between display types and body text to ensure legibility within VR focal planes.
- **Weight:** Heavy weights (700-800) are used for "inflated" headlines to give them visual mass.
- **Readability:** Increased line-heights for body text compensate for potential chromatic aberration in VR headsets.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for three-dimensional spatial canvases. Elements are not pinned to a flat 2D plane but are instead positioned in "Z-space" layers.
- **Rhythm:** A base-8 spacing scale ensures consistency. 
- **VR Safe Zones:** All critical interactions are kept within a 60-degree central field of view.
- **Padding:** High internal padding is required for all "pillowy" containers to prevent text from hitting the curved "inflated" edges of the components.

## Elevation & Depth

Hierarchy is communicated through **Physical Displacement** and **Vibrant Glassmorphism**.
- **The Inflatable Effect:** Objects don't just hover; they have volume. This is achieved using inner glows (top-left) to simulate light hitting a curved plastic surface and drop shadows with high blur (30px+) and low opacity (20%) to suggest a soft landing on the layer below.
- **Glassmorphism:** Secondary panels use a 20px backdrop blur with a 1px "silk" border (white at 15% opacity) to distinguish themselves from the background without losing spatial context.
- **Shadow Tints:** Shadows are never pure black; they inherit the hue of the object (e.g., a blue button casts a soft blue shadow) to simulate ambient light bounce.

## Shapes

The shape language is strictly **Pill-shaped** and ultra-rounded. There are no sharp corners in this design system. 
- **Base Radius:** Large-scale components use a minimum of 2rem (32px) radius to maintain the "inflatable" look.
- **Convexity:** Surfaces should appear slightly convex. This is reinforced through the use of radial gradients that are slightly lighter in the center of the component, mimicking a 3D rounded form catching light.

## Components

- **Pillowy Buttons:** These are the hero components. They feature a 4px bottom "shelf" (a darker shade of the button color) to create a 3D pressable appearance. On hover, the "shelf" shrinks as the button moves down the Z-axis.
- **Glass Chips:** Semi-transparent, pill-shaped tags with a vibrant 1px border. Used for categorizing learning modules.
- **Inflatable Cards:** Large containers with heavy "rounded-xl" corners. They use a subtle inner-shadow to appear as if the content is "nestled" into a soft cushion.
- **Floating Lists:** List items are separated by significant vertical gaps (12px+) and appear as individual floating "pods" rather than a single monolithic block.
- **Tactile Inputs:** Text fields resemble recessed "wells." When focused, they "inflate" outward and glow with a Neon Mint outer shadow.
- **Progress Orbs:** Instead of flat bars, learning progress is shown via 3D glass spheres that fill with "liquid" Electric Blue as the user completes tasks.