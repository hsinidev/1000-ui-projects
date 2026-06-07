---
name: Soma-Body
colors:
  surface: '#fbf9f6'
  surface-dim: '#dbdad7'
  surface-bright: '#fbf9f6'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f0'
  surface-container: '#efeeeb'
  surface-container-high: '#eae8e5'
  surface-container-highest: '#e4e2df'
  on-surface: '#1b1c1a'
  on-surface-variant: '#4d453c'
  inverse-surface: '#30312f'
  inverse-on-surface: '#f2f0ed'
  outline: '#7f766a'
  outline-variant: '#d1c5b8'
  surface-tint: '#725a39'
  primary: '#725a39'
  on-primary: '#ffffff'
  primary-container: '#d2b48c'
  on-primary-container: '#5b4526'
  inverse-primary: '#e1c299'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5d5f5f'
  on-tertiary: '#ffffff'
  tertiary-container: '#b8b9b9'
  on-tertiary-container: '#484a4a'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#feddb3'
  primary-fixed-dim: '#e1c299'
  on-primary-fixed: '#281801'
  on-primary-fixed-variant: '#584324'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f6'
  on-background: '#1b1c1a'
  surface-variant: '#e4e2df'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin: 64px
  section-gap: 128px
---

## Brand & Style

The brand personality is rooted in the intersection of clinical precision and artistic beauty. It targets a discerning clientele seeking body transformation through a lens of self-care and medical excellence rather than mere vanity. The UI must evoke a sense of quiet confidence, serenity, and professional rigor.

This design system utilizes a **Sculptural Minimalism** style. It leverages expansive whitespace to denote luxury and breathing room, drawing inspiration from high-end architectural galleries. While the foundation is minimalist, the interface feels "tactile" through the use of organic, flowing transitions and subtle depth that mimics the natural curves of the human form. The result is a digital environment that feels as curated and sterile as a medical suite, yet as warm and welcoming as a luxury spa.

## Colors

The palette is restrained to maintain an atmosphere of sophistication and focus. 

- **Sand (#D2B48C):** The primary brand color, used for key actions, subtle accents, and to evoke warmth and skin-like tones.
- **Warm Charcoal (#333333):** Used for primary typography and structural elements, providing high-contrast readability without the harshness of pure black.
- **Pure White (#FFFFFF):** The primary surface color, creating a "clean room" aesthetic that emphasizes medical-grade hygiene.
- **Bone (Neutral - #F9F7F4):** A secondary background color used to create soft differentiation between sections without breaking the minimalist flow.

Avoid using vibrant colors for alerts; use tonal shifts of Sand or Charcoal to maintain the serene visual hierarchy.

## Typography

The typography strategy relies on the contrast between the historic elegance of the serif and the modern efficiency of the sans-serif.

- **Headlines:** **Noto Serif** is used to convey a "sculpted" feel. Headlines should use generous line height and tight letter spacing for a high-fashion, editorial look.
- **Body & UI:** **Manrope** provides a balanced, clean, and modern feel. Its geometric nature complements the organic shapes of the UI while ensuring clinical clarity for medical information.
- **Hierarchy:** Use all-caps labels for small metadata or navigation items to provide a structured, professional rhythm against the fluid headline styles.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to maintain a curated, boutique-site feel, transitioning to a fluid model for mobile devices. 

- **Grid:** A 12-column centered grid with wide 64px margins. Elements should frequently occupy the center 6 or 8 columns to create intentional "void" space on the flanks.
- **Rhythm:** Use a strict 8px base unit. Vertical spacing between sections should be exceptionally generous (128px+) to reinforce the minimalist, low-stress user experience.
- **Alignment:** Balance organic, off-center imagery with strictly aligned typography to create a sense of professional stability.

## Elevation & Depth

Depth is conveyed through **Tonal Layers** and **Ambient Shadows** rather than traditional elevation.

- **Surface Tiers:** Use subtle shifts between Pure White and Bone backgrounds to indicate depth. 
- **Shadows:** Shadows are rarely used. When necessary (e.g., for floating modals or primary cards), they must be extra-diffused with a large blur radius (30px+) and very low opacity (5-8%), using a Warm Charcoal tint to avoid a "muddy" look.
- **Soft Focus:** Background blurs (10px-20px) are used behind navigation bars to maintain the feeling of light passing through the interface, suggesting transparency and honesty.

## Shapes

The shape language is the core of the "Soma" identity. It avoids sharp medical corners in favor of **Organic, Flowing Curves**.

- **Containers:** Use `rounded-xl` (1.5rem) for most cards and containers to mimic the softness of the human body.
- **Buttons:** Use fully rounded (pill-shaped) silhouettes for primary actions to encourage interaction through a friendly, soft-touch aesthetic.
- **Images:** Photography should use asymmetrical radii—for example, a top-left and bottom-right corner radius of 100px while others remain at 16px—to create a bespoke, sculptural appearance.

## Components

- **Buttons:** Primary buttons are Solid Sand with Warm Charcoal text. Secondary buttons are outlined in a thin (1px) Charcoal border with no fill. Interaction states should involve a gentle expansion of the button width rather than a color flash.
- **Input Fields:** Use "floating labels" with a simple bottom border in Warm Charcoal (0.5 opacity). This maintains the minimalist aesthetic and avoids "boxy" forms that feel too administrative.
- **Cards:** Cards should have no borders. Use a subtle Bone (#F9F7F4) background to separate them from the Pure White page background. 
- **Chips:** Used for medical tags or treatment categories. These should be small, pill-shaped, and use the Label-Caps typography style.
- **Progress Indicators:** For multi-step consultations, use thin, elegant lines that "grow" fluidly, avoiding heavy blocks or numbers.
- **Additional Component: The "Gallery Frame":** A specific container for anatomical or result imagery that uses a soft-focus border and wide internal padding to treat medical photos like fine art.