---
name: ScholarFund
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#444650'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fd8b00'
  on-secondary-container: '#603100'
  tertiary: '#60603e'
  on-tertiary: '#ffffff'
  tertiary-container: '#aead85'
  on-tertiary-container: '#414122'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#e6e5b9'
  tertiary-fixed-dim: '#cac99f'
  on-tertiary-fixed: '#1d1d03'
  on-tertiary-fixed-variant: '#484828'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: Lexend
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Lexend
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Lexend
    fontSize: 24px
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
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
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
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system is built to balance the gravity of academic achievement with the warmth of community support. The brand personality is **authoritative yet accessible**, functioning as a bridge between high-stakes financial trust and the vibrant aspirations of students. 

The aesthetic follows a **Modern Academic** style—a fusion of traditional institutional reliability and contemporary digital agility. It utilizes high-contrast elements to ensure maximum accessibility and clarity. To prevent the interface from feeling sterile, subtle academic motifs such as light grid patterns (reminiscent of graph paper) and minimalist graduation icons are integrated into backgrounds and empty states. This evokes a sense of "work-in-progress" and "future potential," rather than a rigid, finished monument.

## Colors

The palette is anchored by **Royal Blue (#002366)**, used for navigation, headers, and primary branding to instill immediate confidence and institutional trust. **Bright Orange (#FF8C00)** serves as the high-energy "Action Color," reserved exclusively for primary calls-to-action (CTAs) and progress indicators to drive momentum.

The background uses **Cream (#FFFDD0)** instead of pure white to soften the visual experience and create a "parchment-like" warmth that is easier on the eyes during long reading sessions. Text is rendered in a near-black neutral (#1A1A1A) to maintain a high contrast ratio against the cream background, meeting WCAG AAA standards for readability.

## Typography

This design system utilizes **Lexend** for headlines. Its geometric but open letterforms were specifically designed to reduce visual stress and improve reading speed, making it the perfect "friendly academic" face. 

For body copy and functional UI elements, **Public Sans** provides an institutional, neutral clarity. It is a workhorse typeface that conveys stability. To maintain a clear hierarchy, "Label-Caps" are used for small metadata (like scholarship categories or dates) to provide a distinct visual break from standard body prose.

## Layout & Spacing

The layout operates on a **12-column fluid grid** with a maximum container width of 1280px to prevent line lengths from becoming unreadable on ultra-wide monitors. A strict **8px spacing scale** ensures vertical rhythm across all components.

Information-heavy pages (like scholarship listings) use a more condensed 16px-24px gutter to maximize content visibility, while landing and marketing pages utilize 48px-80px of "breathable" white space (Cream space) to emphasize key messaging and student photography.

## Elevation & Depth

Depth is handled through **ambient shadows** rather than heavy borders. Shadows should be soft and diffused, using a slight tint of the Primary Royal Blue (e.g., `rgba(0, 35, 102, 0.08)`) to ensure they look natural on the Cream background.

- **Level 0 (Flat):** Main background surfaces.
- **Level 1 (Soft):** Cards, input fields, and secondary buttons. These appear slightly lifted to invite interaction.
- **Level 2 (Lifted):** Hover states and navigation bars.
- **Level 3 (High):** Modals and urgent notifications.

This system avoids "floating" elements without purpose; every elevation change must signify a functional layer of information.

## Shapes

The shape language is **Rounded**, using a 0.5rem (8px) base radius. This specific curvature is intentional: it is round enough to feel approachable and modern, but sharp enough to maintain a sense of professional structure. 

Buttons and input fields follow the base radius, while larger containers like "Scholarship Cards" or "Featured Student" banners may use the `rounded-xl` (1.5rem) setting to create a softer, more protective visual frame for human-centric content.

## Components

### Buttons
- **Primary:** Bright Orange background with White text. Bold weight. Used for "Donate Now" or "Apply."
- **Secondary:** Royal Blue background with White text. Used for "Learn More" or "View Profile."
- **Outline:** Royal Blue border with transparent background. Used for tertiary actions.

### Cards
Scholarship cards feature a Level 1 shadow and a subtle 1px border in a darkened shade of Cream. The top edge of cards may feature a 4px "accent strip" in Royal Blue to denote institutional backing.

### Input Fields
Fields should have a solid Cream background that is slightly darker than the page background to create a "recessed" feel, with a 2px Royal Blue border appearing only on focus.

### Progress Bars
Used for funding goals. The track should be a light Royal Blue tint, with the active fill using the Bright Orange to show "energy" toward the goal.

### Academic Accents
Use a 10% opacity "Grid Line" pattern as a background fill for the header section of the platform. This grounds the "Vibrant" colors in a structured, "Academic" environment.