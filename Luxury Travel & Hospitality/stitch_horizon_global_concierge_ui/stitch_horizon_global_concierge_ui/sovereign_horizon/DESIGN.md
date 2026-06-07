---
name: Sovereign Horizon
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#4a4452'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#7c7483'
  outline-variant: '#cdc3d4'
  surface-tint: '#7345b6'
  primary: '#310065'
  on-primary: '#ffffff'
  primary-container: '#4a148c'
  on-primary-container: '#b889ff'
  inverse-primary: '#d7baff'
  secondary: '#5d5e62'
  on-secondary: '#ffffff'
  secondary-container: '#dfdfe3'
  on-secondary-container: '#616366'
  tertiary: '#222222'
  on-tertiary: '#ffffff'
  tertiary-container: '#373737'
  on-tertiary-container: '#a2a09f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#eddcff'
  primary-fixed-dim: '#d7baff'
  on-primary-fixed: '#280056'
  on-primary-fixed-variant: '#5a2a9c'
  secondary-fixed: '#e2e2e6'
  secondary-fixed-dim: '#c5c6ca'
  on-secondary-fixed: '#1a1c1f'
  on-secondary-fixed-variant: '#45474a'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  utility-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.01em
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
  gutter: 24px
  margin-safe: 32px
---

## Brand & Style

The brand personality is defined by invisible excellence—the quiet confidence of a service that is omnipresent yet never intrusive. Targeted at Ultra-High-Net-Worth Individuals (UHNWI), the interface must evoke an immediate sense of calm, security, and absolute competence. 

This design system employs a **Minimalist** foundation augmented by **Glassmorphism** for depth. The aesthetic prioritizes clarity and high-utility "app-like" density within a spacious, luxurious frame. Every interaction should feel intentional, moving away from decorative clutter toward functional elegance. The emotional response is one of "concierge-in-pocket": high-speed utility meets high-touch luxury.

## Colors

The palette is anchored by **Royal Purple**, used sparingly for primary actions, branding accents, and critical status indicators to signify authority and exclusivity. **White** serves as the primary canvas, ensuring the "cleanliness" and breathable quality expected of premium services.

**Silver** is utilized as a sophisticated accent for borders, dividers, and inactive states, providing a metallic sheen that feels more substantial than standard greys. **Neutral** tones are kept cool to maintain a modern, professional atmosphere. High-contrast black is reserved for primary text to ensure absolute legibility.

## Typography

This design system utilizes a sophisticated typographic pairing to balance heritage with modernity. **Noto Serif** is reserved for headings and editorial moments, grounding the interface in a tradition of literary excellence and premium service.

**Manrope** handles all high-utility UI elements, data points, and body copy. Its geometric yet refined structure ensures clarity in secure communications and rapid-glance "Response Time" indicators. Use all-caps labels with increased letter spacing for category headers to create a structured, architectural feel.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy for desktop (centering at 1280px) and a fluid, high-margin model for mobile. We use an 8px rhythmic scale. Generous whitespace (using 'lg' and 'xl' units) is mandated between major content sections to prevent the UI from feeling "crowded," which is a hallmark of budget interfaces.

Content is organized into an "App-like" card structure. On mobile, these cards should have horizontal "safe area" margins of 20px, while on desktop, they align to a 12-column grid. The spacing rhythm should prioritize vertical breathing room, allowing the user to focus on one high-value task at a time.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Tonal Layers**. We avoid harsh black shadows in favor of extra-diffused, low-opacity Royal Purple tints (e.g., 4% opacity) to create a "lifted" effect for cards.

Interactive elements use a subtle **Glassmorphism** effect: cards may have a very slight backdrop blur and a 1px Silver border to define their edges against the white background. This creates a sense of "layered glass," suggesting a sophisticated, multi-dimensional workspace. Surface-on-surface depth should be used sparingly—only one level of elevation is permitted above the base background to maintain a clean, high-utility feel.

## Shapes

The design system employs **Rounded** geometry (0.5rem base) to soften the professional tone and make the interface feel approachable and modern. 

- **Cards:** Use `rounded-lg` (1rem) to create the signature app-like feel.
- **Buttons & Input Fields:** Use the base `rounded` (0.5rem).
- **Avatars & Status Pips:** Use full circles (pill-shaped) to distinguish human elements and active indicators from structural containers.
- **Silver Accents:** Use thin (1px) strokes for all borders to maintain a precision-engineered look.

## Components

**Buttons:** Primary buttons are solid Royal Purple with white text. Secondary buttons use a Silver 1px stroke with Manrope Medium text. All buttons feature a subtle transition on hover, deepening the purple or adding a light silver fill.

**Cards:** These are the primary containers. They must have a white background, a 1px Silver border, and a soft ambient shadow. Within cards, use "Response Time" pips—small, pulsating circular indicators that change from Silver (pending) to Royal Purple (active/responded).

**Secure Communication:** Chat and message threads must use Noto Serif for the message body to feel like formal correspondence, wrapped in Manrope UI frames. Use a "Lock" icon in Silver next to all sensitive data points.

**Input Fields:** Minimalist design with a 1px Silver bottom-border only in the default state, transitioning to a full Royal Purple border on focus. Labels should be `label-caps`.

**Status Indicators:** A dedicated "Time to Response" component should be present on all request cards, featuring a countdown or "Average: 4m" label in `utility-sm` Manrope.