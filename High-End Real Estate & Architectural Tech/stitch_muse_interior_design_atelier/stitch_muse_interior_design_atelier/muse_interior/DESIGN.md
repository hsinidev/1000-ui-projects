---
name: Muse-Interior
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
  on-surface-variant: '#444748'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#747878'
  outline-variant: '#c4c7c8'
  surface-tint: '#5d5f5f'
  primary: '#5d5f5f'
  on-primary: '#ffffff'
  primary-container: '#ffffff'
  on-primary-container: '#747676'
  inverse-primary: '#c6c6c7'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e5e2e1'
  on-secondary-container: '#656464'
  tertiary: '#8c4b55'
  on-tertiary: '#ffffff'
  tertiary-container: '#ffffff'
  on-tertiary-container: '#a8616c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c7'
  on-primary-fixed: '#1a1c1c'
  on-primary-fixed-variant: '#454747'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474646'
  tertiary-fixed: '#ffd9dd'
  tertiary-fixed-dim: '#ffb2bc'
  on-tertiary-fixed: '#3a0915'
  on-tertiary-fixed-variant: '#70343e'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Bodoni Moda
    fontSize: 64px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Bodoni Moda
    fontSize: 48px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Bodoni Moda
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
    letterSpacing: 0em
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.15em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-edge: 64px
  section-padding: 120px
---

## Brand & Style

This design system is engineered for the high-fashion interior design market, prioritizing an editorial aesthetic that mirrors luxury print publications. The brand personality is curated, exclusive, and visionary. It avoids the clutter of traditional e-commerce in favor of a minimalist, "gallery" approach where the interface recedes to let the interior photography lead.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**. It utilizes expansive white space to denote prestige and employs delicate glass-like layers to provide depth without breaking the clean, architectural lines. Every interaction must feel high-performance and intentional, utilizing fluid transitions that mimic the graceful movement of a physical luxury showroom.

## Colors

The palette is anchored by **Crisp White**, used as a high-brightness canvas to evoke a sense of limitless space. **Charcoal** serves as the primary engine for typography and structural contrast, ensuring maximum legibility and a grounded, professional feel. 

**Rose Gold** is the singular accent color, reserved strictly for calls to action, active states, and premium highlights. It should be applied sparingly to maintain its impact. For glassmorphic elements, use semi-transparent white backgrounds with a subtle saturation boost to ensure the rose gold accents "pop" through the frosted surfaces.

## Typography

Typography in this design system follows an editorial hierarchy. **Bodoni Moda** is used for headlines to provide a high-contrast, sophisticated serif look that feels like a masthead. It should be used at large scales with tight leading to emphasize its elegant thick-and-thin strokes.

**Manrope** is the workhorse for all UI and body text. Its geometric yet warm construction provides a clean counterpoint to the serif headlines. Use `label-caps` for navigation items and small UI indicators to maintain an organized, architectural feel.

## Layout & Spacing

This design system utilizes a **Fixed Grid** model for large screens, transitioning to fluid behavior for mobile. The desktop layout is centered on a 12-column grid with a generous 120px vertical rhythm between major sections to prevent visual fatigue.

Whitespace is treated as a core design element rather than "empty space." Horizontal margins are wider than industry standards (64px+) to create a focused, high-end frame for the content. Elements within cards and glass modules should use an 8px base unit for internal padding to maintain a structured, mathematical balance.

## Elevation & Depth

Hierarchy is established through **Glassmorphism** and ultra-soft, ambient shadows. Instead of traditional solid layers, surfaces utilize a `backdrop-filter: blur(20px)` with a high-transparency white fill (`rgba(255, 255, 255, 0.7)`).

Shadows are exceptionally diffused, using large blur radii (30px-60px) and very low opacity (5-10%) to simulate natural gallery lighting. Every glass module must feature a 1px "refined border" in a slightly more opaque white or a very faint charcoal tint to define its edges against the crisp white background.

## Shapes

The shape language is "Soft-Modern." Primary UI elements like buttons and input fields use a subtle 4px radius (`roundedness: 1`). This maintains a sharp, architectural precision while feeling more premium and accessible than harsh 90-degree corners.

Large containers and image carousels may occasionally use `rounded-lg` (8px) to soften the impact of high-contrast photography. Circular shapes are reserved exclusively for profile avatars or specific floating action icons.

## Components

### Buttons
Primary buttons are solid **Charcoal** with white text for high-contrast impact. Secondary buttons use the **Rose Gold** accent with a glass background. All buttons should have a hover state that slightly increases the backdrop blur or adds a subtle glint effect to the Rose Gold.

### Input Fields
Inputs should be minimalist: a single 1px charcoal bottom border that transitions to Rose Gold on focus. Labels use the `label-caps` typography style, positioned above the field to maintain a clean vertical rhythm.

### Cards
Cards are the primary container for interior project showcases. They should feature the glassmorphic style with a subtle 1px border. On hover, cards should slightly lift using an ambient shadow, and the image within should scale marginally (1.05x) to create a high-performance feel.

### Chips & Tags
Used for material types or style categories (e.g., "Mid-Century," "Marble"). These are rendered with a transparent background and a thin charcoal border, using `label-caps` typography.

### Progress & Transitions
Use fluid, "ease-in-out" cubic-bezier timing for all transitions (approx. 400ms). Page transitions should feel like a cinematic fade or a soft slide to emphasize the luxury nature of the platform.