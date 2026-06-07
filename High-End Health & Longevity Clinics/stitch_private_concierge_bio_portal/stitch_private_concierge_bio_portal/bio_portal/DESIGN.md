---
name: Bio-Portal
colors:
  surface: '#f6faff'
  surface-dim: '#d2dbe4'
  surface-bright: '#f6faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#ecf5fe'
  surface-container: '#e6eff8'
  surface-container-high: '#e0e9f2'
  surface-container-highest: '#dbe4ed'
  on-surface: '#141d23'
  on-surface-variant: '#444650'
  inverse-surface: '#293138'
  inverse-on-surface: '#e9f2fb'
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
  tertiary-container: '#26292a'
  on-tertiary-container: '#8e9091'
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
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#f6faff'
  on-background: '#141d23'
  surface-variant: '#dbe4ed'
typography:
  h1:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.1em
  quote:
    fontFamily: Playfair Display
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 32px
  margin-page: 64px
  section-gap: 120px
  card-padding: 40px
---

## Brand & Style
The brand personality is **Executive, Private, and Clinical**. This design system targets a high-net-worth demographic that values discretion, immediate access, and clinical excellence. The UI must evoke a sense of "digital sanctuary"—a place that feels secure, calm, and highly personalized.

The visual direction is a **Modern Soft-UI**. It avoids the heavy, dated look of first-generation Neumorphism in favor of a "Soft-Elevated" approach. Elements appear to emerge subtly from the expansive white background through the use of dual-light-source shadows rather than harsh borders. The interface emphasizes negative space to reduce cognitive load, reflecting the concierge nature of the service where every detail is handled with precision.

## Colors
The palette is rooted in **Royal Blue (#002366)**, signifying authority and medical trust. This is used sparingly for primary navigation, headings, and heavy-weight interactions. **Gold (#D4AF37)** is the "Elite" accent color, reserved strictly for premium call-to-actions, status indicators for 'Elite' tier members, and subtle decorative flourishes.

The canvas is **Pure White (#FFFFFF)**. To achieve the Soft-UI effect, we use a "Clinical Grey" (#F8F9FA) for subtle background offsets behind elevated cards. Semantic colors (Success, Warning, Error) should be desaturated to maintain the sophisticated, calm atmosphere.

## Typography
The typographic scale emphasizes a contrast between traditional prestige and modern efficiency. **Playfair Display** provides the editorial, high-end feel for all major headings and section titles. **Inter** is utilized for all functional text, data displays, and body copy to ensure maximum legibility and a clinical, systematic feel.

All Gold-accented text should use slightly increased tracking (letter spacing) to enhance the "luxury brand" aesthetic. Headlines should prioritize optical kerning to maintain balance on large displays.

## Layout & Spacing
This design system employs a **Fixed Centered Grid** for the main content area to maintain a sense of containment and exclusivity, avoiding the "stretched" look of wide-fluid layouts. The rhythm is based on an 8px baseline, but with significantly expanded padding to emphasize the "Maximum White Space" requirement.

Sections are separated by large vertical gaps (120px+) to allow the eye to rest. Content cards use generous internal padding (40px) to ensure clinical data never feels cramped. Navigation is typically anchored to the top or a slim, floating left sidebar to keep the center of the screen clear.

## Elevation & Depth
Depth is achieved through **Soft-UI Neumorphism**. Instead of traditional drop shadows, elements use a combination of two shadows:
1.  **Bottom-Right Shadow:** A soft, diffused Royal Blue tint (`rgba(0, 35, 102, 0.05)`) with a large blur (30px-50px).
2.  **Top-Left Highlight:** A crisp White (`#FFFFFF`) highlight to simulate light hitting a raised surface.

Surface levels are minimal:
-   **Level 0:** The pure white base.
-   **Level 1:** Raised cards and containers for primary content.
-   **Level 2:** Inset fields for inputs (concave effect) and active buttons.
Avoid "stacking" more than two layers of depth to maintain a clean, modern appearance.

## Shapes
The shape language is defined by **pronounced, organic curves**. All primary containers and cards must use a 24px radius to feel approachable and "soft." Interactive elements like buttons and input fields use a slightly tighter 12px-16px radius. Circular treatments are reserved for profile avatars and "Quick Action" floating buttons. No sharp 90-degree corners are permitted in this design system.

## Components
### Buttons
- **Primary:** Royal Blue background with white Inter Medium text. Subtle soft-shadow elevation.
- **Elite CTA:** Gold background with Royal Blue text. This is reserved for "Book Specialist" or "Upgrade Membership."
- **Ghost:** Transparent background with a thin 1px Royal Blue border, used for secondary actions.

### Cards
Cards are the primary vessel for information. They must be pure white, using the Soft-UI elevation style. No borders; the depth is defined entirely by the soft shadow-play.

### Input Fields
Inputs should use the "Inset" Neumorphic effect, appearing as if they are carved into the card surface. This provides a clear tactile affordance for data entry. Use Inter for input text.

### Status Indicators
Status indicators (e.g., "Lab Results Ready") use a Gold dot for high-priority items and a subtle Royal Blue for standard updates.

### Additional Components
- **The Health Timeline:** A vertical, minimal line using Royal Blue and Gold nodes to track patient history.
- **Concierge Chat Bubble:** A floating, Soft-UI circular button always present in the bottom right, providing immediate access to the private coordinator.
- **Biometric Data Chips:** Small, rounded pills used to display vitals (Pulse, Sleep, etc.) with high-contrast Royal Blue typography.