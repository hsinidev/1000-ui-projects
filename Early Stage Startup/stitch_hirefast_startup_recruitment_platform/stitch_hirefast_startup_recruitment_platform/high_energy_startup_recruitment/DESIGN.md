---
name: High-Energy Startup Recruitment
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#3c4a47'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#6c7a77'
  outline-variant: '#bbcac6'
  surface-tint: '#006a61'
  primary: '#006a61'
  on-primary: '#ffffff'
  primary-container: '#00c2b2'
  on-primary-container: '#004a43'
  inverse-primary: '#40dccb'
  secondary: '#565e74'
  on-secondary: '#ffffff'
  secondary-container: '#dae2fd'
  on-secondary-container: '#5c647a'
  tertiary: '#505f76'
  on-tertiary: '#ffffff'
  tertiary-container: '#9eaec7'
  on-tertiary-container: '#324257'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#65f9e7'
  primary-fixed-dim: '#40dccb'
  on-primary-fixed: '#00201d'
  on-primary-fixed-variant: '#005049'
  secondary-fixed: '#dae2fd'
  secondary-fixed-dim: '#bec6e0'
  on-secondary-fixed: '#131b2e'
  on-secondary-fixed-variant: '#3f465c'
  tertiary-fixed: '#d3e4fe'
  tertiary-fixed-dim: '#b7c8e1'
  on-tertiary-fixed: '#0b1c30'
  on-tertiary-fixed-variant: '#38485d'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-xl:
    fontFamily: Inter
    fontSize: 60px
    fontWeight: '800'
    lineHeight: 72px
    letterSpacing: -0.02em
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '800'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Inter
    fontSize: 30px
    fontWeight: '700'
    lineHeight: 38px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
  label-sm:
    fontFamily: Inter
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
  gutter: 24px
  margin: 32px
---

## Brand & Style

The design system is built to reflect the frantic, high-growth nature of early-stage startups while maintaining a human-centric approach to recruitment. It centers on a **High-Contrast / Bold** aesthetic that utilizes aggressive typography and a vibrant color palette to signal speed and performance. 

The personality is unapologetically energetic and discovery-focused. We balance this intensity with **Modern Minimalism** to ensure the "Fast" in the product name is reflected in the UI's clarity and lack of clutter. The emotional response should be one of momentum—users should feel that finding their next hire or role is an active, exciting pursuit rather than a bureaucratic chore.

## Colors

The palette is driven by **Vibrant Teal**, which serves as the high-energy primary action color. This is contrasted against a **Clean White** base to maintain readability and a "fresh start" feel. **Slate Grey** (in varying weights) provides the structural grounding and professional sophistication required for a recruitment platform.

- **Primary (Vibrant Teal):** Used for call-to-actions, progress indicators, and key interactive moments.
- **Secondary (Deep Slate):** Used for primary text and navigation elements to ensure high readability.
- **Tertiary (Medium Slate):** Used for secondary text, icons, and borders.
- **Neutral (Ghost White):** Used for background surfaces to keep the UI light and airy.

## Typography

This design system utilizes **Inter** exclusively to achieve a systematic, utilitarian, and punchy feel. The type scale is intentionally dramatic. Headings use "Extra Bold" weights with tight letter-spacing to create a sense of urgency and impact. 

Body text remains neutral and highly legible, supporting long-form job descriptions or candidate bios without fatigue. Labels use a semi-bold weight and occasionally uppercase styling to differentiate metadata from primary content.

## Layout & Spacing

The design system employs a **Fluid Grid** model based on a 12-column system. It is designed to maximize screen real estate for data-heavy recruitment workflows while using generous outer margins to keep the content focused.

The spacing rhythm follows an 8px base unit. We use tight gutters (24px) between cards and list items to maintain a "high-density" feel that suggests performance, but use larger vertical "XL" spacing (64px) between major sections to provide visual breathing room.

## Elevation & Depth

Visual hierarchy in this design system is achieved through **Tonal Layers** and **Low-Contrast Outlines** rather than heavy shadows. This keeps the interface feeling "fast" and digital-native.

- **Surface 0:** The main background (#F8FAFC).
- **Surface 1:** Primary containers and cards (Pure White) with a 1px Slate-200 border.
- **Interactive State:** Elements elevate using a subtle, diffused shadow tinted with Teal when hovered, signaling "interactability" and discovery.
- **Overlays:** Modals and flyouts use a heavy backdrop blur (Glassmorphism) to keep the user focused on the task while maintaining the context of the underlying recruitment pipeline.

## Shapes

The shape language is **Rounded**, utilizing a 0.5rem (8px) base radius. This softens the aggressive typography and high-contrast colors, making the platform feel "human-centric" and approachable. 

- **Small Components:** Checkboxes and small tags use 4px (Soft) radius.
- **Standard Components:** Buttons, inputs, and cards use 8px (Rounded).
- **Featured Elements:** Large "Discovery" cards or profile images use 16px (Rounded-LG) to draw the eye.

## Components

### Buttons
Primary buttons are solid Vibrant Teal with white bold text. They should have a slight "lift" on hover. Secondary buttons use a Slate-900 outline with no fill to emphasize the primary action.

### Cards
Cards are the primary vehicle for "Discovery." They feature a white background, an 8px corner radius, and a subtle 1px border. Candidate cards should prioritize the profile image and "Quick Action" buttons.

### Chips & Badges
Used for skills and job tags. These should be high-contrast: Teal backgrounds with dark slate text for active filters, and light grey backgrounds for passive metadata.

### Inputs
Search bars and application forms use a 2px border on focus in Vibrant Teal. Icons should be used within the input field to aid quick visual scanning.

### Discovery Feed
A specialized component for this design system: a vertically scrolling list of candidates or jobs that uses "High-Energy" micro-interactions—like auto-expanding details on hover—to facilitate rapid screening.