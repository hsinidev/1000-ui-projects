---
name: NexusHub Corporate
colors:
  surface: '#f8f9fe'
  surface-dim: '#d9dade'
  surface-bright: '#f8f9fe'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f3f8'
  surface-container: '#edeef2'
  surface-container-high: '#e7e8ec'
  surface-container-highest: '#e1e2e7'
  on-surface: '#191c1f'
  on-surface-variant: '#41474f'
  inverse-surface: '#2e3134'
  inverse-on-surface: '#eff0f5'
  outline: '#717880'
  outline-variant: '#c1c7d0'
  surface-tint: '#206393'
  primary: '#1c6090'
  on-primary: '#ffffff'
  primary-container: '#3c79ab'
  on-primary-container: '#fdfcff'
  inverse-primary: '#96ccff'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e4e2e1'
  on-secondary-container: '#656464'
  tertiary: '#5a5c5c'
  on-tertiary: '#ffffff'
  tertiary-container: '#737575'
  on-tertiary-container: '#fcfcfc'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#cee5ff'
  primary-fixed-dim: '#96ccff'
  on-primary-fixed: '#001d32'
  on-primary-fixed-variant: '#004a75'
  secondary-fixed: '#e4e2e1'
  secondary-fixed-dim: '#c8c6c6'
  on-secondary-fixed: '#1b1c1c'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f8f9fe'
  on-background: '#191c1f'
  surface-variant: '#e1e2e7'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
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
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin: 32px
  stack-xs: 4px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  stack-xl: 64px
---

## Brand & Style

The design system is engineered to embody the prestige and architectural precision of Grade-A commercial real estate. It targets high-level decision-makers, brokers, and enterprise tenants who prioritize efficiency, reliability, and modern luxury. 

The aesthetic follows a **Corporate / Modern** style, characterized by a structured layout, generous whitespace, and a high-contrast visual hierarchy. The emotional response is one of institutional trust and urban sophistication—evoking the feeling of stepping into a glass-fronted lobby in a primary business district. Clarity and precision guide every decision, ensuring that complex leasing data feels accessible and premium.

## Colors

The palette is anchored by **Steel Blue**, a color that balances professional authority with modern tech sensibilities. It is used for primary actions, active states, and key brand moments. **Graphite** serves as the primary foundation for typography and structural elements, providing a softer, more sophisticated alternative to pure black.

**White** is the dominant background color, providing the "crisp" canvas required for high-end digital experiences. Neutral slates are utilized for secondary borders and subtle background shifts to maintain a "clean-room" aesthetic without appearing flat.

## Typography

This design system utilizes **Inter** for its utilitarian precision and exceptional readability in data-heavy environments. The typography scale is intentionally high-contrast to establish clear information architecture.

Headlines use tighter letter spacing and heavier weights to mimic architectural signage. Body text is optimized for legibility with a generous line height. Small labels and metadata use an all-caps treatment with increased letter spacing to provide a technical, "blueprinted" feel.

## Layout & Spacing

The layout philosophy is based on a **Fixed Grid** for desktop views to maintain a curated, editorial appearance, transitioning to a fluid model for smaller breakpoints. A 12-column grid system is used, with a focus on asymmetrical compositions that reflect modern architectural plans.

Spacing follows a strict 8px baseline rhythm. Generous vertical "breathing room" (stack-xl) is encouraged between major sections to emphasize the "Grade-A" premium nature of the content. Internal component padding should be precise and consistent, favoring larger horizontal cushions to evoke a sense of spaciousness.

## Elevation & Depth

This design system uses **Ambient Shadows** and **Tonal Layers** to create a sense of organized depth. 

- **Level 0 (Base):** Crisp White (#FFFFFF) for the main background.
- **Level 1 (Subtle):** Very soft, diffused shadows (Y: 2px, Blur: 4px, 5% Opacity Graphite) are used for secondary cards and container separation.
- **Level 2 (Active/Floating):** Higher elevation shadows (Y: 10px, Blur: 20px, 10% Opacity Graphite) are reserved for dropdowns, modals, and primary hover states.
- **Structural Lines:** 1px borders in a soft slate (#E2E8F0) are used to define zones without adding visual weight, maintaining the "clean lines" requirement.

## Shapes

The shape language is disciplined and geometric. A **Soft (0.25rem)** border radius is the standard for almost all UI elements, including buttons and input fields. This provides just enough approachable softness to feel modern while maintaining the structural integrity of a "sleek" corporate environment. Larger containers, such as property cards, may use the `rounded-lg` (0.5rem) setting to create a distinct frame for high-quality architectural photography.

## Components

- **Buttons:** Primary buttons use a solid Steel Blue fill with White text. Secondary buttons use a Graphite outline with a subtle hover fill. Transitions should be instant or very fast (150ms) to feel responsive and high-end.
- **Input Fields:** Use a subtle 1px border (#E2E8F0) that shifts to Steel Blue on focus. Labels sit outside the field in the `label-caps` style for maximum clarity.
- **Cards:** Property listings are housed in White cards with a subtle Level 1 shadow and no border. High-resolution imagery should span the full width of the card top.
- **Chips/Badges:** Used for office categories (e.g., "Coworking", "Executive"). These use a light Steel Blue tint (10% opacity) with Steel Blue text for a sophisticated, low-contrast look.
- **Lists:** Real estate data tables and lists use thin horizontal dividers (#E2E8F0) and alternating row highlights in a very faint grey for readability.
- **Search/Filters:** A prominent, wide search bar with an integrated "Filter" icon is a centerpiece component, utilizing Level 2 elevation to appear "docked" above content.