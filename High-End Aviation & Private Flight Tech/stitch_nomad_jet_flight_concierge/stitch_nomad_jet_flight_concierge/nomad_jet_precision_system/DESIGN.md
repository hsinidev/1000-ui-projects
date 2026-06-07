---
name: Nomad-Jet Precision System
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#343536'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c5c6cd'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8f9097'
  outline-variant: '#44474d'
  surface-tint: '#b9c7e4'
  primary: '#b9c7e4'
  on-primary: '#233148'
  primary-container: '#0a192f'
  on-primary-container: '#74829d'
  inverse-primary: '#515f78'
  secondary: '#c4c7c9'
  on-secondary: '#2d3133'
  secondary-container: '#464a4b'
  on-secondary-container: '#b6b9bb'
  tertiary: '#b9c8de'
  on-tertiary: '#233143'
  tertiary-container: '#0a1a2a'
  on-tertiary-container: '#748397'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b9c7e4'
  on-primary-fixed: '#0d1c32'
  on-primary-fixed-variant: '#39475f'
  secondary-fixed: '#e0e3e5'
  secondary-fixed-dim: '#c4c7c9'
  on-secondary-fixed: '#191c1e'
  on-secondary-fixed-variant: '#444749'
  tertiary-fixed: '#d4e4fa'
  tertiary-fixed-dim: '#b9c8de'
  on-tertiary-fixed: '#0d1c2d'
  on-tertiary-fixed-variant: '#39485a'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#343536'
typography:
  display-lg:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Geist
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg-mobile:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: Geist
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Geist
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-max: 1440px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
  section-gap: 80px
---

## Brand & Style

This design system is engineered for the high-net-worth traveler who values discretion, efficiency, and technological superiority. The brand personality is "The Invisible Architect"—a concierge service that operates flawlessly in the background. 

The visual style follows a **Modern Minimalist** approach with **Glassmorphic** accents. It prioritizes "Premium Utility," meaning every interface element must serve a functional purpose while maintaining an aesthetic of high-end exclusivity. The UI should evoke the feeling of a private jet cockpit: precise, high-contrast, and impeccably organized. We utilize wide margins to provide "visual oxygen," reinforcing the feeling of luxury and unhurried service.

## Colors

The palette is rooted in a "Night Flight" aesthetic, utilizing a **Dark Mode** default to reduce eye strain and project a discreet, high-tech atmosphere.

- **Deep Navy Blue (#0A192F):** The primary structural color. Used for large surfaces and backgrounds to provide depth.
- **Cloud White (#F8FAFC):** Reserved for high-priority typography and essential icons. It provides a crisp, clinical contrast against the navy.
- **Silver/Metallic (#94A3B8):** Used for secondary information, borders, and thin-line vector work. It mimics the brushed aluminum and titanium found in aerospace engineering.
- **Gradients:** Use subtle linear gradients (Deep Navy to Background Deep) to create a sense of curvature on cards, mimicking the hull of an aircraft.

## Typography

The typography system relies on the technical precision of **Geist** for headings and data points, paired with the legendary readability of **Inter** for body copy.

- **Headlines:** Use Geist with tight letter-spacing to create a "machined" look.
- **Body:** Inter is used for all descriptive text, providing a neutral and trustworthy reading experience.
- **Data Display:** For flight numbers, coordinates, and timestamps, use the Geist font to lean into the developer-friendly, high-tech aesthetic. 
- **Labels:** Small caps with increased tracking (0.1em) should be used for section headers and category tags to denote a sense of organized logistics.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy for desktop to maintain a controlled, editorial feel, transitioning to a fluid model for mobile devices.

- **Rhythm:** All spacing is based on a 4px base unit. 
- **Margins:** Exceptionally wide margins (64px+) on desktop are mandatory to convey exclusivity. Content should never feel "cramped."
- **Grid:** A 12-column grid is used for desktop. For data-heavy concierge screens, use a "Dashboard" layout with a fixed sidebar (280px) and a fluid content area.
- **Mobile:** Breakpoints at 390px (Mobile) and 834px (Tablet). On mobile, horizontal margins shrink to 20px, but vertical "section-gap" remains generous to prioritize focus.

## Elevation & Depth

Depth is signaled through **Tonal Layering** and **Glassmorphism** rather than traditional drop shadows.

- **Surface Tiers:** The base background is `#060E1A`. Primary cards sit at `#0A192F`. Floating elements (modals) use a semi-transparent version of the primary color with a 20px backdrop blur.
- **Borders:** Instead of shadows, use "Ghost Borders"—1px solid strokes using the Metallic color (#94A3B8) at 20% opacity. This defines the shape without adding visual weight.
- **Inner Glow:** High-priority buttons or active states may use a subtle 1px inner-top-border in Cloud White (15% opacity) to simulate a light source reflecting off a metallic edge.

## Shapes

The shape language is **Soft (0.25rem)**. 

While the aesthetic is modern, overly rounded or pill-shaped elements are avoided as they feel too "friendly" and consumer-grade. Small radius corners (4px to 8px) suggest precision engineering and structural integrity. 

- **Interactive Elements:** Buttons and inputs use a 4px (0.25rem) radius.
- **Containers:** Large cards and modal overlays use an 8px (0.5rem) radius.
- **Icons:** Thin-line vector icons (1.5px stroke weight) with sharp terminals, echoing the precise corner radius of the UI.

## Components

- **Buttons:** Primary buttons are Cloud White with Deep Navy text. Secondary buttons are "Ghost" style (Silver border, no fill). Use a "shimmer" hover effect—a subtle diagonal gradient sweep—to suggest a metallic surface.
- **Inputs:** Fields are dark-filled (#060E1A) with a bottom-only 1px Silver border. On focus, the border transitions to a full 1px Cloud White outline.
- **Chips/Status:** Use the Mono-data typography. Flight status chips (e.g., "In Transit") use a low-opacity background of the status color (Success Green) with a high-opacity text.
- **Cards:** Flight cards must be clean. Use Geist for the airport codes (SFO → LHR) in a large font size, separated by a thin-line vector aircraft icon. 
- **Logistics Timeline:** A vertical 1px Silver line connecting thin circles, representing the concierge milestones (Chauffeur, Lounge, Boarding).
- **Interactive Maps:** Dark-themed maps with Silver paths and Cloud White "pulsing" nodes for aircraft location.