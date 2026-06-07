---
name: AdmissionEdge
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444650'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fd8b00'
  on-secondary-container: '#603100'
  tertiary: '#101517'
  on-tertiary: '#ffffff'
  tertiary-container: '#24292c'
  on-tertiary-container: '#8b9094'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#dfe3e7'
  tertiary-fixed-dim: '#c3c7cb'
  on-tertiary-fixed: '#171c1f'
  on-tertiary-fixed-variant: '#43474b'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  headline-xl:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-bold:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Plus Jakarta Sans
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
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The design system is engineered to inspire confidence and momentum in prospective students. The brand personality is **Energetic & Aspirational**, positioning the institution not just as a place of study, but as a launchpad for future success. 

The UI style follows a **Modern/High-Contrast** movement. It utilizes expansive white space to maintain a high-conversion focus, punctuated by aggressive splashes of Royal Blue for authority and Vibrant Orange for action. Visuals must feature high-energy photography—capturing authentic student collaboration, campus movement, and "aha!" moments—to create an emotional bridge between the applicant and their future life.

## Colors

This design system utilizes a high-contrast palette to drive conversion and establish brand authority. 

- **Royal Blue (#002366):** Used for primary navigation, headings, and foundational structural elements. It conveys tradition, trust, and academic excellence.
- **Vibrant Orange (#FF8C00):** Reserved exclusively for high-priority calls to action, interactive states, and progress indicators. It provides an energetic contrast that draws the eye toward conversion points.
- **White (#FFFFFF):** The dominant background color to ensure a clean, "breathable" interface that highlights content and imagery.
- **Tertiary Slate (#F0F4F8):** A soft, cool neutral used for card backgrounds and subtle section differentiation without sacrificing the bright aesthetic.

## Typography

The typography strategy for the design system balances motivation with readability. 

**Lexend** is employed for all headlines to provide a bold, geometric, and "athletic" feel that resonates with active recruitment. Its unique letterforms feel modern and approachable while maintaining a strong presence.

**Plus Jakarta Sans** serves as the body and label typeface. Its soft, contemporary curves ensure that long-form content—such as program descriptions or application instructions—remains inviting and highly legible. Headlines should use tighter letter-spacing to feel punchy and integrated, while body text uses generous line-height for maximum clarity.

## Layout & Spacing

The design system uses a **Fixed Grid** model for desktop, centered within the viewport to maintain focus on the recruitment funnel. A 12-column grid provides the structural foundation, with 24px gutters ensuring content has room to breathe.

The spacing rhythm is based on an 8px scale. Large vertical gaps (48px to 80px) should be used between major sections to emphasize the "clean" aesthetic and prevent information overload. This rhythm ensures that energetic imagery and bold CTAs are never crowded, maintaining a premium, organized feel.

## Elevation & Depth

To maintain the energetic and modern aesthetic, depth is achieved through **Tonal Layers** and **Ambient Shadows**. 

1. **Surface Tiers:** Use the tertiary light blue (#F0F4F8) for secondary containers to create subtle separation from the white background.
2. **Shadows:** Avoid heavy, dark shadows. Use extra-diffused, low-opacity shadows (e.g., 8% opacity of Royal Blue) for primary interactive cards and the Student Ambassador widget. This "tinted shadow" technique ensures the UI feels light and airy.
3. **Overlays:** For video players and modals, use a high-blur backdrop filter (12px to 20px) to maintain the sense of environment while focusing the user's attention.

## Shapes

The design system adopts a **Rounded** shape language to appear friendly and accessible. 

- **Standard Buttons & Inputs:** 0.5rem (8px) corner radius.
- **Cards & Video Players:** 1rem (16px) corner radius for a more prominent, framed look.
- **Floating Widgets & Chips:** 1.5rem (24px) or "Pill" shapes to distinguish them from structural content.

This curvature softens the high-contrast color palette, ensuring the portal feels welcoming to prospective students and their families.

## Components

### Buttons
- **Primary CTA:** Vibrant Orange background, white text, bold Lexend. These should be large and include a subtle hover lift effect.
- **Secondary:** Royal Blue outlines or ghost styles to be used for less critical navigation.

### Student Ambassador Widget
A circular floating action button (FAB) in Royal Blue featuring a student avatar. When expanded, it uses a soft-rounded card with a clean chat interface.

### Progress Bars
Used in quizzes and calculators. Utilize a thick 12px track in Tertiary Slate, with the progress filled in Vibrant Orange. Include percentage labels in bold Plus Jakarta Sans.

### Interactive Video Players
Large-scale components with 16px rounded corners. Play buttons should be centered, utilizing the Vibrant Orange with a pulse animation to draw attention.

### Input Fields
Clean white backgrounds with a subtle 1px stroke in Royal Blue (20% opacity). On focus, the stroke should intensify to 100% Royal Blue with a soft blue outer glow.

### Cards
Feature-rich containers with 16px corners, utilizing high-energy photography as headers and clear, bold typography for descriptions. Every card should lead to a clear "Next Step" link or button.