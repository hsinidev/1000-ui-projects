---
name: Human-Centric Professional Excellence
colors:
  surface: '#f8f9f9'
  surface-dim: '#d9dada'
  surface-bright: '#f8f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f4'
  surface-container: '#edeeee'
  surface-container-high: '#e7e8e8'
  surface-container-highest: '#e1e3e3'
  on-surface: '#191c1c'
  on-surface-variant: '#4e4350'
  inverse-surface: '#2e3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#807381'
  outline-variant: '#d1c2d2'
  surface-tint: '#873da6'
  primary: '#732993'
  on-primary: '#ffffff'
  primary-container: '#8e44ad'
  on-primary-container: '#f8d8ff'
  inverse-primary: '#ecb2ff'
  secondary: '#4e6073'
  on-secondary: '#ffffff'
  secondary-container: '#cfe2f9'
  on-secondary-container: '#526478'
  tertiary: '#005747'
  on-tertiary: '#ffffff'
  tertiary-container: '#00725e'
  on-tertiary-container: '#82f7d8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#f8d8ff'
  primary-fixed-dim: '#ecb2ff'
  on-primary-fixed: '#320047'
  on-primary-fixed-variant: '#6c228c'
  secondary-fixed: '#d1e4fb'
  secondary-fixed-dim: '#b5c8df'
  on-secondary-fixed: '#091d2e'
  on-secondary-fixed-variant: '#36485b'
  tertiary-fixed: '#82f7d8'
  tertiary-fixed-dim: '#65dabc'
  on-tertiary-fixed: '#002019'
  on-tertiary-fixed-variant: '#005142'
  background: '#f8f9f9'
  on-background: '#191c1c'
  surface-variant: '#e1e3e3'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
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
    lineHeight: '1.0'
    letterSpacing: 0.05em
  button:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.01em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  section-padding: 64px
  stack-sm: 12px
  stack-md: 24px
---

## Brand & Style

The brand personality is an intentional balance of academic rigor and empathetic support. This design system facilitates a high-stakes learning environment for HR professionals, where the interface must feel as reliable as a mentor and as sophisticated as a modern workplace. 

The design style is **Corporate / Modern** with a lean toward **Minimalism**. It prioritizes clarity and cognitive ease to reduce the mental load on candidates. The aesthetic avoids cold, industrial tropes in favor of warmth through generous white space, organic shapes, and a palette that signals both wisdom (Navy) and innovation (Purple). The UI should evoke a sense of calm confidence and organized progression.

## Colors

This design system utilizes a palette rooted in professional trust. 

- **Primary (Soft Purple):** Used for interactive elements, progress indicators, and primary call-to-actions. It differentiates the platform from standard blue-heavy corporate tools.
- **Secondary (Deep Navy):** Reserved for headers, navigation backgrounds, and high-level typography to establish authority and structure.
- **Background (Off-white/White):** Provides a clean, distraction-free canvas for long-form reading and testing.
- **Success/Compliance (Teal):** Used for correct answers, completed modules, and positive HR outcomes.
- **Warning/Risk (Soft Amber):** Specifically designated for "Compliance Risk" alerts and areas requiring immediate candidate attention.

## Typography

**Manrope** is selected for its modern, balanced, and highly legible characteristics. It excels in both large-scale headlines and dense learning content. 

To ensure the study material is approachable, body text is set with a generous line height (1.6) to prevent eye strain during long study sessions. Headlines use a tighter tracking and heavier weight to provide clear visual signposts. The use of uppercase labels for categories and metadata provides a systematic, organized feel to the educational hierarchy.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop to ensure optimal line lengths for reading comprehension, transitioning to a fluid model for mobile devices. 

A strict 8px spacing scale governs the rhythm of the UI. Vertical rhythm is prioritized; "stack" variables define the distance between related learning content (sm) and distinct content blocks (md). Section padding is intentionally large to create an atmosphere of "Generous Whitespace," signaling that the platform is premium and uncluttered.

## Elevation & Depth

Visual hierarchy is established through **Tonal Layers** and **Ambient Shadows**. 

Surfaces are kept mostly flat to maintain professionalism, but primary cards and interactive modals use soft, diffused shadows with a slight Navy tint (e.g., `rgba(44, 62, 80, 0.08)`). This provides a subtle "lift" without appearing overly trendy. 

Low-contrast outlines in light grey are used for secondary containers to provide structure without adding visual noise. When a user is in "Focus Mode" for an exam, background elements should recede using a slight backdrop blur, bringing the active question surface to the foreground.

## Shapes

The shape language uses a **Rounded** philosophy (Level 2). This choice moves away from the "sharp" edges of traditional law or compliance software, making the platform feel more human-centric and supportive. 

Standard components like buttons and input fields utilize a 0.5rem radius. Larger surfaces, such as module cards and study guides, utilize `rounded-lg` (1rem) or `rounded-xl` (1.5rem) to create a soft, approachable frame for complex information.

## Components

- **Buttons:** Primary buttons use the Soft Purple background with white text. Secondary buttons use a Navy outline. Hover states should involve a subtle darkening of the color rather than a shadow change.
- **Progress Cards:** Use a vertical orientation for learning paths, featuring a "Soft Green" progress bar and the secondary Navy for the module title.
- **Input Fields:** Use a subtle Off-white fill with a 1px border. On focus, the border transitions to Soft Purple with a 2px outer glow.
- **Chips/Badges:** Used for "Exam Topic" tags. These should have a very light Purple or Navy tint with high-contrast text.
- **Quiz Interface:** Questions are housed in "elevation 1" cards. Options are large-area radio buttons that highlight the entire container in Purple when selected.
- **Imagery Treatment:** Photography should always be placed in containers with rounded corners. Images should feature natural lighting and diverse professionals to reinforce the human-centric mission of the design system.