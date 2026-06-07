---
name: Safety-First Service System
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
  on-surface-variant: '#44474d'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#75777e'
  outline-variant: '#c5c6ce'
  surface-tint: '#4e5f7c'
  primary: '#00030a'
  on-primary: '#ffffff'
  primary-container: '#0a1d37'
  on-primary-container: '#7586a5'
  inverse-primary: '#b6c7e9'
  secondary: '#a73400'
  on-secondary: '#ffffff'
  secondary-container: '#d14300'
  on-secondary-container: '#fffbff'
  tertiary: '#000305'
  on-tertiary: '#ffffff'
  tertiary-container: '#00202b'
  on-tertiary-container: '#6c8997'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#b6c7e9'
  on-primary-fixed: '#081c36'
  on-primary-fixed-variant: '#364763'
  secondary-fixed: '#ffdbcf'
  secondary-fixed-dim: '#ffb59c'
  on-secondary-fixed: '#390c00'
  on-secondary-fixed-variant: '#832700'
  tertiary-fixed: '#c9e7f7'
  tertiary-fixed-dim: '#adcbda'
  on-tertiary-fixed: '#001f2a'
  on-tertiary-fixed-variant: '#2e4b57'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-xl:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
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
  label-bold:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1.2'
  label-sm:
    fontFamily: Public Sans
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
  unit: 8px
  gutter: 24px
  margin: 32px
  container-max: 1280px
---

## Brand & Style
The design system is engineered to evoke immediate trust and technical authority. It targets homeowners and property managers who require urgent, high-stakes trade services where safety is non-negotiable. The brand personality is professional, sturdy, and reliable—balancing the "emergency" nature of plumbing and electrical work with a calm, high-fidelity premium aesthetic.

The style follows a **Corporate / Modern** direction. It utilizes heavy whitespace to suggest cleanliness (essential in plumbing) and high-contrast elements to ensure that calls to action and safety warnings are unmistakable. The interface should feel like a precision tool: functional, durable, and sophisticated.

## Colors
The palette is rooted in **Deep Navy Blue**, providing a foundation of institutional authority and expertise. This is contrasted by **Signal Orange**, which is reserved exclusively for primary actions, emergency alerts, and safety-critical information.

**Pure White** is the primary background color to reinforce a sense of hygiene and clarity. Neutral greys are used sparingly for borders and secondary text to maintain high legibility. 

- **Primary (Navy):** Used for headers, footers, and primary branding elements.
- **Accent (Orange):** Used for "Book Now" buttons, status alerts, and icons requiring high visibility.
- **Background:** Strictly white or very light grey (#F8F9FA) to ensure a high-contrast environment for readability.

## Typography
This design system utilizes **Public Sans** for its institutional clarity and neutral, professional tone. The typography hierarchy is designed to communicate urgency through scale and weight.

- **Headlines:** Use Bold and Extra Bold weights (700-800) to project confidence and reliability. Large headings should have slightly tighter letter spacing for a more "solid" and grounded appearance.
- **Body Text:** Maintained at a comfortable 16px-18px for maximum accessibility during high-stress situations (e.g., a burst pipe).
- **Labels:** Uppercase labels in bold weights are used for technical specifications or service categories to ensure they are easily scannable.

## Layout & Spacing
The layout follows a **fixed grid** model for desktop to maintain a structured, sturdy feel, transitioning to a fluid layout for mobile. A strict **8px base unit** ensures all elements are aligned with mathematical precision, reinforcing the theme of technical expertise.

- **Grid:** A 12-column system with generous 24px gutters to prevent visual clutter.
- **Rhythm:** Vertical spacing between sections should be ample (64px to 96px) to allow the "cleanliness" of the white background to facilitate focus.
- **Margins:** Page margins are set to a minimum of 32px to ensure content is never cramped against the viewport edges.

## Elevation & Depth
Depth in the design system is handled with **ambient shadows** and subtle tonal layering. The goal is to make components feel like physical, high-quality objects without being overly decorative.

- **Shadows:** Use large-blur, low-opacity shadows (e.g., `box-shadow: 0 10px 30px rgba(10, 29, 55, 0.08)`) to lift cards and buttons off the page. Shadows should have a slight navy tint to maintain color harmony.
- **Tonal Layers:** Secondary containers can use a subtle off-white background to create a distinct hierarchy without relying on borders.
- **Interactions:** On hover, primary buttons should increase their elevation slightly to encourage clicking and provide tactile feedback.

## Shapes
The shape language is defined by "Approachable Sturdiness." While the design is professional, sharp corners can feel overly aggressive in a service context. 

- **Corner Radii:** Standard components (buttons, input fields) use an **8px radius**. 
- **Larger Containers:** Cards and modals use a **16px radius** (`rounded-lg`) to soften the overall aesthetic and make the brand feel more modern and accessible.
- **Icons:** Should feature consistent stroke weights and slight rounding on terminals to match the UI's geometry.

## Components
Consistent execution of components is vital for building trust.

- **Buttons:** 
  - *Primary:* Orange background with white text for maximum conversion.
  - *Secondary:* Navy background with white text for navigational elements.
  - *Tertiary:* Navy outline for less critical actions.
- **Input Fields:** Thick 2px borders in a medium grey, turning Navy on focus. Labels must always be visible for accessibility.
- **Cards:** White background with a subtle border (#E9ECEF) and a soft ambient shadow. Cards are used to group service packages or technician profiles.
- **Status Badges:** High-contrast pills (e.g., "En Route," "Completed") using the Signal Orange or a deep Success Green.
- **Service Indicators:** Progress bars for tracking a technician's arrival, utilizing the Navy and Orange colors to show movement and status.
- **Iconography:** Line-based icons with a 2px stroke. Icons should be technical and literal (e.g., a realistic wrench or circuit breaker) rather than abstract.