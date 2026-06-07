---
name: Artisanal Global Learner
colors:
  surface: '#fef9f3'
  surface-dim: '#ded9d4'
  surface-bright: '#fef9f3'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f8f3ed'
  surface-container: '#f2ede7'
  surface-container-high: '#ece7e2'
  surface-container-highest: '#e6e2dc'
  on-surface: '#1d1b18'
  on-surface-variant: '#57423d'
  inverse-surface: '#32302c'
  inverse-on-surface: '#f5f0ea'
  outline: '#8b716c'
  outline-variant: '#dec0b9'
  surface-tint: '#a53b25'
  primary: '#a13923'
  on-primary: '#ffffff'
  primary-container: '#c25138'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb4a4'
  secondary: '#006496'
  on-secondary: '#ffffff'
  secondary-container: '#68bdfe'
  on-secondary-container: '#004b73'
  tertiary: '#735802'
  on-tertiary: '#ffffff'
  tertiary-container: '#8e711f'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad3'
  primary-fixed-dim: '#ffb4a4'
  on-primary-fixed: '#3e0500'
  on-primary-fixed-variant: '#842410'
  secondary-fixed: '#cce5ff'
  secondary-fixed-dim: '#91cdff'
  on-secondary-fixed: '#001e31'
  on-secondary-fixed-variant: '#004b72'
  tertiary-fixed: '#ffdf96'
  tertiary-fixed-dim: '#e7c268'
  on-tertiary-fixed: '#251a00'
  on-tertiary-fixed-variant: '#5a4400'
  background: '#fef9f3'
  on-background: '#1d1b18'
  surface-variant: '#e6e2dc'
typography:
  display-lg:
    fontFamily: beVietnamPro
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
  headline-lg:
    fontFamily: beVietnamPro
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
  headline-md:
    fontFamily: beVietnamPro
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-lg:
    fontFamily: lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.02em
  label-md:
    fontFamily: lexend
    fontSize: 12px
    fontWeight: '500'
    lineHeight: 16px
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
  lg: 40px
  xl: 64px
  margin-mobile: 20px
  gutter: 16px
---

## Brand & Style
The design system is rooted in the concept of a "Global Village," blending the warmth of traditional craftsmanship with the clarity of modern educational tools. It evokes a sense of belonging, curiosity, and tactile discovery. 

The visual style is **Tactile and Organic**. It moves away from sterile, plastic interfaces toward a "handcrafted" digital experience. Surfaces should feel like high-quality paper, clay, or woven fabric. This approach makes the technology feel approachable for children and trustworthy for parents, emphasizing human connection over machine precision. The aesthetic celebrates imperfection through organic shapes and textile-inspired motifs, creating an inclusive environment that feels like a global home.

## Colors
The palette is a dialogue between the earth and the sky. The primary **Terracotta** provides a grounded, nurturing foundation reminiscent of clay and soil. The secondary **Azure** injects energy and a sense of vast possibility. 

A warm **Saffron** serves as a tertiary accent for interactive highlights and celebratory moments. The neutral base is a soft **Parchment** rather than a stark white, reducing eye strain and reinforcing the tactile, paper-like quality of the interface. Functional colors (success, error) should be slightly desaturated to maintain the earthy, natural harmony of the primary palette.

## Typography
Typography is selected for its extreme legibility and friendly character. **Be Vietnam Pro** is used for headlines; its contemporary yet warm terminals provide a welcoming "storytelling" vibe. 

**Lexend** is the primary typeface for body text and labels. Specifically designed to reduce visual stress and improve reading speed, it is the perfect choice for an educational context. The scale uses generous font sizes and line heights to ensure the UI remains accessible to preschoolers who are developing fine motor skills and early literacy, as well as diverse global users who may be navigating the app in a non-native language.

## Layout & Spacing
The layout follows a **fluid grid** model with exaggerated safe areas. Preschool interfaces require higher tolerance for "missed" taps, so the spacing rhythm is intentionally spacious. 

We utilize an 8px base grid, but layout-level margins are pushed to 24px or 40px to create a sense of calm and focus. Content is organized into "islands" of information rather than dense lists. On tablet devices, the layout should utilize a multi-column structure that mirrors the spread of an illustrated children’s book, ensuring that no single line of text becomes too long to track easily.

## Elevation & Depth
Depth in this design system is achieved through **Tonal Layers** and **Subtle Materiality** rather than realistic light sources. 

1.  **Stacked Surfaces:** Background elements use the Parchment base, while active containers use a slightly elevated pure white or a very pale tint of the primary color.
2.  **Tinted Shadows:** Shadows are never gray. They are soft, diffused blurs using a low-opacity version of the object's own color or a deep Terracotta. This creates a "glow" that feels organic and integrated.
3.  **Pattern Overlays:** Subtle, low-contrast textile patterns (like mudcloth dashes or ikat zig-zags) are used on secondary layers to provide visual richness without adding cognitive load. These patterns help distinguish between "active" interactive areas and "passive" informational areas.

## Shapes
The shape language is **Rounded and Friendly**, prioritizing safety and softness. While a standard 0.5rem (8px) radius is the baseline, primary containers and buttons often use even more aggressive rounding (up to 24px) to mimic the feel of smooth river stones or hand-molded clay. 

Avoid sharp 90-degree corners entirely. Use "squircle" mathematics where possible to ensure transitions between straight lines and curves feel natural and organic. Patterns and decorative motifs should utilize hand-drawn, slightly irregular lines to maintain the "human-made" aesthetic.

## Components
Consistent styling across components reinforces the global, community-focused narrative.

-   **Buttons:** Large, "chunky" targets with a minimum height of 56px. They feature a subtle "bottom-heavy" shadow to give them a pressable, tactile quality. Primary buttons use Terracotta with white Lexend Bold text.
-   **Cards:** Containers feature a soft 16px corner radius. A decorative "textile strip" (Ikat or Mandala pattern) is applied as a top border or a small side-accent to categorize content by cultural or educational themes.
-   **Input Fields:** Borders are soft and slightly thicker (2px) to feel substantial. The focus state uses a vibrant Azure glow.
-   **Chips/Tags:** Pill-shaped with a light fill of the primary or secondary color. They serve as "badges" for global landmarks or cultural motifs.
-   **Icons:** Custom-drawn icons of landmarks (e.g., Baobab trees, Pyramids, Pagodas) use a mono-line style with rounded ends. They are never purely geometric; they retain a slight "sketch" quality.
-   **Progress Bars:** Styled to look like a growing seed or a weaving loom, where the "progress" adds more pattern or color to the track.