---
name: Emergency Mobile Dental
colors:
  surface: '#f5fafc'
  surface-dim: '#d6dbdd'
  surface-bright: '#f5fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4f6'
  surface-container: '#eaeff1'
  surface-container-high: '#e4e9eb'
  surface-container-highest: '#dee3e5'
  on-surface: '#171c1e'
  on-surface-variant: '#5d3f3d'
  inverse-surface: '#2c3133'
  inverse-on-surface: '#ecf1f3'
  outline: '#926e6c'
  outline-variant: '#e7bcba'
  surface-tint: '#bf0022'
  primary: '#ac001e'
  on-primary: '#ffffff'
  primary-container: '#d90429'
  on-primary-container: '#ffeae8'
  inverse-primary: '#ffb3af'
  secondary: '#5b5d74'
  on-secondary: '#ffffff'
  secondary-container: '#ddddf9'
  on-secondary-container: '#5f6178'
  tertiary: '#495567'
  on-tertiary: '#ffffff'
  tertiary-container: '#616d81'
  on-tertiary-container: '#e8efff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad7'
  primary-fixed-dim: '#ffb3af'
  on-primary-fixed: '#410005'
  on-primary-fixed-variant: '#930018'
  secondary-fixed: '#e0e0fc'
  secondary-fixed-dim: '#c4c4df'
  on-secondary-fixed: '#181a2e'
  on-secondary-fixed-variant: '#43455b'
  tertiary-fixed: '#d7e3fa'
  tertiary-fixed-dim: '#bbc7dd'
  on-tertiary-fixed: '#101c2c'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#f5fafc'
  on-background: '#171c1e'
  surface-variant: '#dee3e5'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  callout:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '800'
    lineHeight: '1.0'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-margin: 20px
  gutter: 16px
  touch-target-min: 48px
  component-gap-sm: 12px
  component-gap-md: 24px
  section-padding: 40px
---

## Brand & Style

This design system is engineered for high-stakes, medical-grade reliability. The brand personality is authoritative, urgent, and hyper-efficient, prioritizing rapid cognitive processing for users in physical distress. The target audience includes individuals experiencing acute dental pain or trauma who require immediate, professional intervention at their location.

The aesthetic follows a **High-Contrast / Corporate Modern** hybrid. It utilizes the stark clarity of medical instrumentation combined with modern mobile patterns. Every visual element is designed to minimize friction; whitespace is used strategically to isolate critical information, while bold color blocks signal the path to immediate care. The UI should evoke a sense of "clinical calm"—reassuring the user through professional structure while acknowledging the urgency of their situation.

## Colors

The color palette is functionally driven to distinguish between "action" and "information."

*   **Signal Red (#D90429):** Reserved exclusively for high-urgency primary actions, emergency status indicators, and the "Call Now" triggers.
*   **Navy Blue (#2B2D42):** Used for primary text, navigation headers, and structural elements to establish a foundation of trust and professional authority.
*   **Crisp White (#FFFFFF):** The primary background color to maintain a sterile, clinical feel and maximize contrast for readability.
*   **Cool Grey (#8D99AE & #EDF2F4):** Used for secondary information, borders, and disabled states to ensure the interface doesn't feel cluttered or overwhelming during a crisis.

## Typography

This design system utilizes **Inter** for its exceptional legibility and systematic appearance. The typographic scale is exaggerated to ensure that even users with blurred vision or high stress levels can navigate the content effortlessly.

Headlines use heavy weights (700-800) and tighter letter spacing to create a sense of presence and importance. Body copy is kept at a generous size (minimum 16px) with ample line height to ensure medical instructions and service details are digestible. "Label-bold" is used for metadata and status indicators, often paired with high-contrast backgrounds.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model optimized for mobile-first consumption. It utilizes a 4-column system for mobile devices with 20px outer margins to prevent content from crowding the screen edges.

The spacing rhythm is strictly based on an 8px baseline grid. Large touch targets are a priority; no interactive element should be smaller than 48px in height. Vertical spacing between different service types or emergency options is kept generous (24px+) to prevent accidental taps during rapid navigation.

## Elevation & Depth

To maintain a clean, medical-grade aesthetic, this design system avoids heavy shadows and decorative depth. Instead, it utilizes **Tonal Layers** and **Subtle Ambient Shadows**.

*   **Surface Tiers:** The base background is White (#FFFFFF). Cards and secondary containers use a very light grey (#EDF2F4) or a 1px Navy Blue border to define boundaries.
*   **Shadows:** When depth is required (e.g., for floating action buttons or active cards), use a soft, 12% opacity Navy Blue shadow with a large blur radius (16px) and 4px vertical offset. This makes elements appear to float slightly above the surface without looking "heavy" or distracting.
*   **Active States:** Interactive cards should use a subtle inner glow or a 2px Signal Red stroke when selected, rather than a shadow change, to maintain the flat, clean aesthetic.

## Shapes

The shape language uses **Rounded (Value: 2)** geometry to soften the clinical nature of the service, making it feel more approachable and modern.

*   **Primary Containers:** Use `rounded-lg` (1rem / 16px) for cards and modals to create a friendly but structured appearance.
*   **Buttons:** Use `rounded-xl` (1.5rem / 24px) for a "pill-lite" look that clearly differentiates interactive elements from informational boxes.
*   **Small Elements:** Chips and labels use `rounded-md` (0.5rem / 8px).
*   **Map Interfaces:** Map containers should feature the same 16px corner radius when windowed, or be full-bleed to maximize the viewable area.

## Components

### Buttons
*   **Emergency 'Call Now' (Floating):** A large, circular or pill-shaped button in Signal Red (#D90429) that remains anchored to the bottom right. It must feature a high-contrast phone icon and bold "CALL NOW" text.
*   **Primary Actions:** Pill-shaped, Navy Blue (#2B2D42) with White text for scheduling or confirmation.
*   **Secondary Actions:** Outline buttons with a 2px Navy Blue stroke.

### Cards
*   **Urgency Cards:** High-contrast cards used for triage. They feature a Bold Headline, a brief subtext, and a large icon. High-priority symptoms (e.g., "Severe Bleeding") may use a light red tint (#FFF0F0) with a Signal Red left-accent border.
*   **Service Cards:** Clean white backgrounds with subtle Navy Blue icons.

### Inputs & Forms
*   **Input Fields:** Minimalist style with a 1px Grey (#8D99AE) bottom border or full light-grey fill. Focus states utilize a 2px Navy Blue border.
*   **Checkboxes/Radios:** Large-scale (24x24px) to ensure easy selection for users who may have limited manual dexterity due to pain.

### Map & Location
*   **Live Tracker:** A map-centric view showing the "Dentist-on-the-Way." The marker should be a Navy Blue pin with a Signal Red pulsing aura to indicate live movement.
*   **Location Bar:** A persistent, high-visibility bar at the top or bottom of the screen confirming the user's current service address.

### Status Indicators
*   **Arrival Chips:** Using high-visibility green for "Arriving" or Signal Red for "High Demand" to set clear expectations.