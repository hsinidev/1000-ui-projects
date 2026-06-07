---
name: LendScale Design System
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#3e4850'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#6e7881'
  outline-variant: '#bec8d2'
  surface-tint: '#006591'
  primary: '#006591'
  on-primary: '#ffffff'
  primary-container: '#0ea5e9'
  on-primary-container: '#003751'
  inverse-primary: '#89ceff'
  secondary: '#545f71'
  on-secondary: '#ffffff'
  secondary-container: '#d8e3f9'
  on-secondary-container: '#5a6577'
  tertiary: '#5c5f61'
  on-tertiary: '#ffffff'
  tertiary-container: '#999c9e'
  on-tertiary-container: '#303436'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c9e6ff'
  primary-fixed-dim: '#89ceff'
  on-primary-fixed: '#001e2f'
  on-primary-fixed-variant: '#004c6e'
  secondary-fixed: '#d8e3f9'
  secondary-fixed-dim: '#bcc7dc'
  on-secondary-fixed: '#111c2b'
  on-secondary-fixed-variant: '#3c4759'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Public Sans
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-lg:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: 0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base-unit: 8px
  margin-mobile: 16px
  margin-desktop: 32px
  gutter: 24px
  container-max: 1200px
---

## Brand & Style

This design system is built to bridge the gap between institutional reliability and modern accessibility. The brand personality is "The Supportive Expert"—knowledgeable and secure, yet easy to talk to. The target audience includes small business owners looking for growth capital and individual investors seeking transparent P2P opportunities. 

The chosen style is **Corporate / Modern**. It leverages significant whitespace and a refined color palette to reduce the cognitive load often associated with financial data. The UI evokes a sense of calm and competence, ensuring users feel their capital and personal information are in safe hands. The visual language avoids over-decoration, focusing instead on clarity, legibility, and high-trust signals.

## Colors

The palette is anchored by **Sky Blue**, a primary color chosen for its association with transparency and optimism. This is used strategically for primary actions and brand-heavy elements to drive conversion. 

**Charcoal** serves as the secondary and text color, providing the necessary weight and authority to financial figures and legibility to long-form terms. **White** is the dominant background color, used to create a "breathable" environment that feels clean and modern. Secondary neutrals are utilized for subtle borders and backgrounds to distinguish between different content sections without introducing visual noise.

## Typography

The design system utilizes **Public Sans** across all touchpoints. Chosen for its institutional clarity and neutral yet friendly personality, it ensures that complex lending terms are highly legible even on small mobile screens.

Headlines use a semi-bold weight to establish a clear information hierarchy, while body copy utilizes generous line-heights (1.5x - 1.6x) to facilitate scanning. Large financial figures should always be set in a prominent weight to provide immediate clarity on loan amounts, interest rates, and investment returns.

## Layout & Spacing

This design system employs a **Fluid Grid** model built on an 8px base unit. For mobile devices, a single-column layout with 16px side margins ensures that content remains accessible and buttons are easily tappable. On desktop, a 12-column grid provides the structure needed for complex dashboards and application forms.

Whitespace is used as a functional tool to group related information. High-conversion pages (like loan applications) should feature increased vertical padding between sections to maintain focus and prevent user fatigue.

## Elevation & Depth

To maintain a professional yet welcoming feel, this design system uses **Ambient Shadows** to create a sense of depth. Shadows should be soft, diffused, and slightly tinted with the Charcoal secondary color to avoid a "muddy" appearance.

The elevation strategy uses three tiers:
1. **Base Layer (Level 0):** Used for the main background.
2. **Card Layer (Level 1):** Subtle 1px borders or very soft shadows (4px blur, 2% opacity) to lift content containers.
3. **Interactive Layer (Level 2):** More pronounced shadows (12px blur, 6% opacity) for hover states on buttons and active cards to provide tactile feedback.

## Shapes

The shape language is defined by a consistent **Rounded** aesthetic. A standard radius of 8px (0.5rem) is applied to form inputs, small buttons, and tags. Larger containers like cards and primary call-to-action buttons use a 12px or 16px radius to soften the overall interface and make it feel more approachable.

Avoid sharp 90-degree angles, as they can appear overly rigid and aggressive in a financial context. Circles are reserved exclusively for avatars and icon backgrounds.

## Components

### Buttons
Primary buttons use the Sky Blue fill with white text, utilizing a minimum height of 48px for mobile accessibility. Secondary buttons use a Charcoal outline or a light grey fill. All buttons should have a 12px corner radius.

### Input Fields
Inputs must be clearly labeled with floating labels or labels placed above the field. They feature an 8px corner radius and a 2px Sky Blue border focus state to ensure the user always knows where they are in a form.

### Cards
Cards are the primary vehicle for P2P loan listings and investment summaries. They should feature a White background, a subtle 1px border (#E2E8F0), and a Level 1 shadow. 

### Chips & Tags
Used for status indicators (e.g., "Verified," "Funded," "Pending"). These should have a pill shape (fully rounded) and use low-saturation background colors to avoid competing with primary action buttons.

### Progress Indicators
Essential for the lending application process. Use a horizontal stepper on desktop and a simple "Step X of Y" bar on mobile to maintain a streamlined flow and encourage completion.