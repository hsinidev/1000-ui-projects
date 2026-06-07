---
name: Haptic Luxe Design System
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#4d4635'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#7f7663'
  outline-variant: '#d0c5af'
  surface-tint: '#735c00'
  primary: '#735c00'
  on-primary: '#ffffff'
  primary-container: '#d4af37'
  on-primary-container: '#554300'
  inverse-primary: '#e9c349'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#725c00'
  on-tertiary: '#ffffff'
  tertiary-container: '#ceb153'
  on-tertiary-container: '#544300'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffe088'
  primary-fixed-dim: '#e9c349'
  on-primary-fixed: '#241a00'
  on-primary-fixed-variant: '#574500'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#ffe081'
  tertiary-fixed-dim: '#e2c464'
  on-tertiary-fixed: '#231b00'
  on-tertiary-fixed-variant: '#564500'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
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
  label-sm:
    fontFamily: Manrope
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  stack-sm: 12px
  stack-md: 32px
  stack-lg: 80px
---

## Brand & Style

The design system is rooted in the intersection of high-end jewelry craftsmanship and intimate digital connection. It targets a discerning audience that values both material quality and emotional resonance. The UI must feel as intentional as a piece of hand-finished gold, evoking a sense of "digital touch" through visual warmth and physical metaphors.

The chosen style is **Minimalist-Refined with Tactile influences**. By utilizing soft-glow effects, organic silhouettes, and generous whitespace, the interface mimics the diffused light of a luxury boutique. The emotional response is one of calm, security, and deep intimacy—prioritizing trust through a polished, uncluttered aesthetic.

## Colors

The palette is anchored by **Pearl (#FDFDFD)** to provide a clean, luminous canvas that allows the jewelry photography to breathe. **Champagne Gold (#D4AF37)** is used for primary actions and brand-critical elements, often paired with a softer secondary gold **(#E3C565)** for gradients and glows.

**Slate (#2F2F2F)** provides the necessary weight and grounding for typography and structural elements, ensuring the design feels "trust-heavy" and established. High-contrast pairings are avoided in favor of tonal shifts to maintain the soft, "haptic" quality of the interface.

## Typography

This design system utilizes **Playfair Display** for headings to communicate heritage, elegance, and romantic luxury. Its high-contrast strokes pair perfectly with the tactile focus of the brand.

**Manrope** is used for all functional and body text. Its modern, balanced proportions ensure high legibility on mobile devices while maintaining a sophisticated, neutral tone that does not compete with the serif headings. Labels and small navigational elements should use Manrope with increased letter spacing and uppercase styling to denote "Luxury Detail."

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to ensure a curated, editorial feel, while transitioning to a fluid model for smaller viewports. Content is centered and focused, avoiding edge-to-edge density to preserve a sense of exclusivity.

A rhythm of **8px** governs the spacing. Large "breathing rooms" (stack-lg) are used between major sections to emphasize the minimalist-refined aesthetic. Components should prioritize vertical padding to enhance the "soft-touch" feel of the interactive areas.

## Elevation & Depth

In this design system, depth is not conveyed through harsh shadows, but through **Ambient Glows** and **Tonal Layering**. 

1.  **The Aura Effect:** Interactive elements like active jewelry cards or "Digital Touch" buttons use a soft, primary-colored outer glow (`box-shadow: 0 0 20px rgba(212, 175, 55, 0.15)`) to simulate the warmth of light hitting gold.
2.  **Surface Tiers:** Use subtle shifts between Pearl (#FDFDFD) and its slightly darker variant (#F5F5F5) to create container depth.
3.  **Haptic Inset:** For form inputs and "pressed" states, use very soft inner shadows to create a physical "indent" feeling, as if pressing into a soft material.

## Shapes

The shape language is strictly **organic and pill-shaped**. Sharp corners are avoided to maintain the "Haptic" narrative—conveying that the interface is safe, soft, and comfortable to touch. 

Pill-shaped buttons and high-radius containers (rounded-xl) evoke the silhouettes of polished gemstones and pearls. This fluidity should extend to image masks and icons, ensuring a cohesive "soft-silhouettes" visual style across the entire journey.

## Components

### Buttons
Primary buttons are fully pill-shaped with a Champagne Gold fill. Text is Slate for legibility. A subtle "shimmer" gradient transition from #D4AF37 to #E3C565 is applied on hover.

### Cards
Jewelry cards use a Pearl surface with a very thin, low-opacity Slate border (10% opacity). They feature a generous corner radius and an "Aura" glow that activates when the user hovers, simulating the jewelry coming to life.

### Inputs
Search and form fields use a pill-shape with a soft inset shadow. The focus state replaces the inset shadow with a 1px Champagne Gold border and a faint gold glow.

### Haptic Feedback Elements
The "Digital Touch" feature—a core brand differentiator—is represented by a pulsing, organic circular button. The pulse uses a radial gradient of Champagne Gold with high blur to mimic a heartbeat or a warm glow.

### Lists
Lists for product attributes use generous vertical padding and soft Slate dividers (5% opacity) that fade out toward the edges, maintaining the minimalist, refined vibe.