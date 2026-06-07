---
name: Scent-Sense
colors:
  surface: '#fbf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#fbf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f1'
  surface-container: '#efeeeb'
  surface-container-high: '#e9e8e5'
  surface-container-highest: '#e4e2e0'
  on-surface: '#1b1c1a'
  on-surface-variant: '#434843'
  inverse-surface: '#30312f'
  inverse-on-surface: '#f2f0ee'
  outline: '#737872'
  outline-variant: '#c3c8c1'
  surface-tint: '#506354'
  primary: '#334537'
  on-primary: '#ffffff'
  primary-container: '#4a5d4e'
  on-primary-container: '#c0d5c2'
  inverse-primary: '#b7ccb9'
  secondary: '#665e4b'
  on-secondary: '#ffffff'
  secondary-container: '#ebdec6'
  on-secondary-container: '#6a624f'
  tertiary: '#38443b'
  on-tertiary: '#ffffff'
  tertiary-container: '#4f5b51'
  on-tertiary-container: '#c5d2c6'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d3e8d5'
  primary-fixed-dim: '#b7ccb9'
  on-primary-fixed: '#0e1f13'
  on-primary-fixed-variant: '#394b3d'
  secondary-fixed: '#ede1c9'
  secondary-fixed-dim: '#d1c5ae'
  on-secondary-fixed: '#211b0c'
  on-secondary-fixed-variant: '#4d4634'
  tertiary-fixed: '#d9e6d9'
  tertiary-fixed-dim: '#bdcabe'
  on-tertiary-fixed: '#131e16'
  on-tertiary-fixed-variant: '#3e4a40'
  background: '#fbf9f6'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2e0'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
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
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
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
  base: 8px
  section-gap-desktop: 120px
  section-gap-mobile: 64px
  grid-margin-desktop: 80px
  grid-gutter: 24px
---

## Brand & Style
This design system centers on a "Serene & Biological" aesthetic, positioning the product as a high-end, AI-driven sanctuary for olfactory discovery. The personality is compassionate and sophisticated, bridging the gap between clinical precision and botanical artistry. 

The visual style is a hybrid of **Glassmorphism** and **Tactile Organicism**. It utilizes soft, "breathing" UI elements—micro-animations that mimic slow inhalation and exhalation—to create a calming, immersive experience. High-end luxury is conveyed through generous whitespace, sophisticated serif typography, and a "frosted-leaf" glass effect that feels both modern and natural.

## Colors
The palette is rooted in a forest floor ecosystem. **Moss Green (#4A5D4E)** serves as the primary brand color, used for meaningful actions and headers. **Sand (#E8DCC4)** provides a warm, organic neutral base that prevents the interface from feeling cold or clinical. **Deep Forest (#1B261E)** is reserved for high-contrast text and deep interactive states.

The interface relies heavily on a custom "Glassmorphism" layer—semi-transparent white surfaces that sit atop soft, moving gradients of Moss Green and Sand. This creates a sense of depth and translucency, reminiscent of dew on a leaf or frosted laboratory glassware.

## Typography
The typographic scale emphasizes a "Literary Luxury" feel. **Playfair Display** is used for all headlines to provide a sense of heritage and bespoke craftsmanship. **Inter** is utilized for body copy and UI labels to ensure clinical legibility and a modern, functional counterpoint to the decorative serif. 

Letter spacing is slightly increased for labels to evoke high-end fashion branding, while body text maintains standard tracking for optimal readability of fragrance notes and scientific descriptions.

## Layout & Spacing
The design system employs a **Fluid Grid** with wide margins to create a "breathable" atmosphere. Desktop layouts utilize a 12-column grid with 80px margins, while mobile transitions to a 4-column grid with 20px margins. 

The vertical rhythm is intentionally loose. Sections are separated by large gaps to prevent information density from overwhelming the user. Components should use an 8px base unit for internal padding, but overall layout positioning should favor "optical centering" and asymmetrical balance to feel more organic and less rigid.

## Elevation & Depth
Depth is achieved through **Glassmorphism and Backdrop Blurs** rather than traditional drop shadows. Surfaces appear as translucent panels floating over a dynamic background.

1.  **Base Layer:** Soft, animated gradients of Moss Green and Sand.
2.  **Surface Layer:** Semi-transparent white (`rgba(255, 255, 255, 0.4)`) with a 20px - 40px backdrop blur.
3.  **Border Detail:** A 1px translucent white stroke (`rgba(255, 255, 255, 0.5)`) on the top and left edges to simulate light hitting glass.
4.  **Shadows:** When necessary for accessibility, use very soft, diffused ambient shadows tinted with Deep Forest (#1B261E) at 5% opacity.

## Shapes
This design system avoids harsh angles. The shape language is "Biological," inspired by smooth river stones and petals. While the standard `rounded-md` (0.5rem) is used for utility elements, primary buttons and signature cards use asymmetrical or highly rounded radii to appear more natural. Icons should feature rounded terminals and soft joins to maintain the serene aesthetic.

## Components
-   **Buttons:** Primary buttons use a "Pebble" shape—slightly asymmetrical rounded corners. They feature a soft Moss Green gradient and a subtle "pulse" animation on hover, mimicking a heartbeat.
-   **Glassmorphic Cards:** Main content containers have 24px corner radii, a 20px backdrop blur, and a thin white inner-border. They should appear to lift slightly when interacted with.
-   **Scent Chips:** Interactive fragrance notes are represented as small, circular glass elements that glow faintly in the color of the scent's family (e.g., floral, woody).
-   **Inputs:** Text fields are underline-only or very subtly shaded containers to maintain a minimalist, non-obstructive profile. The focus state transitions the underline into a soft Moss Green glow.
-   **Progress Indicators:** Use organic, "growth-based" animations—visualizing the AI "cultivating" the fragrance formula rather than a standard loading bar.
-   **Selection Controls:** Radio buttons and checkboxes use leaf-inspired shapes instead of perfect circles or squares.