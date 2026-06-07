---
name: Elite Concierge Medicine System
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
  on-surface-variant: '#444650'
  inverse-surface: '#303030'
  inverse-on-surface: '#f2f0f0'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#735c00'
  on-secondary: '#ffffff'
  secondary-container: '#fed65b'
  on-secondary-container: '#745c00'
  tertiary: '#121516'
  on-tertiary: '#ffffff'
  tertiary-container: '#26292b'
  on-tertiary-container: '#8e9092'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#ffe088'
  secondary-fixed-dim: '#e9c349'
  on-secondary-fixed: '#241a00'
  on-secondary-fixed-variant: '#574500'
  tertiary-fixed: '#e1e2e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  title-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.5rem
  DEFAULT: 1rem
  md: 1.5rem
  lg: 2rem
  xl: 3rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-mobile: 24px
  section-padding: 80px
---

## Brand & Style

The brand identity centers on the intersection of modern medical precision and ultra-luxury hospitality. The target audience—high-net-worth families—requires a digital experience that feels as private and attentive as a personal physician.

The aesthetic utilizes **Neumorphic-lite** patterns. Unlike early neomorphism which lacked accessibility, this system uses subtle, multi-layered shadows to create "Soft-UI" depth. Surfaces appear to be gently pressed from the background or floating slightly above it, creating a tactile, organic feel. This "softness" reduces the coldness of typical clinical interfaces, replacing it with a welcoming, executive atmosphere. High-end editorial cues from luxury publishing inform the layout, ensuring that information is presented with breathing room and quiet authority.

## Colors

This design system uses a restricted, high-contrast palette to maintain an aura of exclusivity and clarity. 

*   **Deep Royal Blue (#002366):** Used for primary calls to action, global navigation, and core brand moments. It conveys stability, institutional trust, and heritage.
*   **Metallic Gold (#D4AF37):** Reserved for premium accents, membership status indicators, and subtle decorative borders. It should be used sparingly to maintain its impact.
*   **Crisp White (#FFFFFF):** The primary canvas. Extensive whitespace is mandatory to evoke the "cleanliness" of a private clinic and the "space" of a luxury suite.
*   **Soft Gray (#F8F9FB):** Used for the background of neumorphic "wells" to provide enough contrast for white elements to "pop" or "recede" visually.

## Typography

The typographic hierarchy balances editorial sophistication with clinical legibility.

**Playfair Display** is used for all major headings and introductory statements. It provides a human, bespoke feel that differentiates the service from "mass-market" healthcare apps.

**Inter** handles all functional UI, data display, and body copy. Its high x-height and neutral character ensure that medical data remains legible even at smaller sizes. 

Use `label-caps` for section headers and status labels to provide a structured, "documented" feel to the interface. All serif headlines should favor optical kerning to ensure the high-contrast strokes feel intentional and elegant.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy for desktop to maintain a "centered and focused" executive experience, preventing information from becoming over-extended on wide displays. 

A 12-column grid is used with generous 32px gutters. The primary rhythmic unit is 8px, but layout-level padding favors larger increments (24px, 40px, 64px, 80px) to enforce the "premium" use of space. Content should never feel crowded; if a screen feels busy, increase the `section-padding`. 

Key information, such as medical records or vitals, should be grouped into cards that span 4 or 6 columns to ensure they are the focal point.

## Elevation & Depth

Depth is the defining characteristic of this design system. We move away from flat design toward **Soft-UI** layers.

*   **Raised Surfaces:** Use two shadows—a light shadow (White, -5px -5px, 10px blur) on the top-left and a dark shadow (Light Blue-Gray, 5px 5px, 15px blur) on the bottom-right. This makes elements look like they are molded from the background.
*   **Recessed Surfaces (Wells):** Use inner shadows with the same logic to create "wells" for input fields or data containers.
*   **Floating Elements:** For primary action buttons, use a more traditional, diffused ambient shadow (Deep Royal Blue at 15% opacity) to give them higher prominence than the neumorphic base layers.
*   **Glass Overlays:** For modal backgrounds, use a high-radius backdrop blur (20px+) with a 70% white tint to maintain the clean, clinical aesthetic.

## Shapes

The shape language is defined by extreme softness and fluidity. All primary containers (Cards, Modals) must use a minimum corner radius of **24px** to evoke a sense of safety and modern comfort.

Buttons use a **Pill-shaped (3)** approach to feel friendly and ergonomic. Icons should follow this logic, utilizing rounded caps and joins rather than sharp angles. Gold accents should be applied as thin (2px) strokes or small circular pips to indicate status without cluttering the soft geometry of the containers.

## Components

*   **Buttons:** Primary buttons are Deep Royal Blue with white text. They should have a slight "lift" on hover. Secondary buttons are white with a Gold stroke or text.
*   **Cards:** The primary container. These should feature the neumorphic raised effect against a slightly off-white background (#F8F9FB). No borders; depth is defined solely by shadows.
*   **Input Fields:** Use the "recessed" well effect. The background of the input should be slightly darker than the card it sits on, creating a clear affordance for typing.
*   **Status Indicators:** Use Metallic Gold for "VIP" or "Urgent" statuses. Use a soft, muted green or blue for standard medical confirmations.
*   **Vitals Dashboard:** A specialized component grid using large-format Playfair Display numbers for key metrics (e.g., Heart Rate), paired with Inter labels.
*   **The Signature Line:** A decorative 1px Gold horizontal line used to separate high-level sections, mimicking luxury stationery.