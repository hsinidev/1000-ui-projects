---
name: Supportive Academic
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
  on-surface-variant: '#3f484c'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#6f787d'
  outline-variant: '#bfc8cd'
  surface-tint: '#0c6780'
  primary: '#0c6780'
  on-primary: '#ffffff'
  primary-container: '#87ceeb'
  on-primary-container: '#005870'
  inverse-primary: '#89d0ed'
  secondary: '#62603d'
  on-secondary: '#ffffff'
  secondary-container: '#e9e4b8'
  on-secondary-container: '#686643'
  tertiary: '#0060ac'
  on-tertiary: '#ffffff'
  tertiary-container: '#a0c7ff'
  on-tertiary-container: '#005295'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#baeaff'
  primary-fixed-dim: '#89d0ed'
  on-primary-fixed: '#001f29'
  on-primary-fixed-variant: '#004d62'
  secondary-fixed: '#e9e4b8'
  secondary-fixed-dim: '#ccc89e'
  on-secondary-fixed: '#1e1c03'
  on-secondary-fixed-variant: '#4a4828'
  tertiary-fixed: '#d4e3ff'
  tertiary-fixed-dim: '#a4c9ff'
  on-tertiary-fixed: '#001c39'
  on-tertiary-fixed-variant: '#004883'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Lexend
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  h2:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  caption:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  margin: 32px
  container-max: 1200px
---

## Brand & Style
The design system is engineered for educators navigating the high-stakes environment of certification. It balances academic rigor with an approachable, supportive atmosphere. The personality is that of a "trusted mentor"—highly organized and professional, yet warm and encouraging.

The visual style draws from **Modern Minimalism** with **Tactile** influences. It utilizes generous whitespace to reduce cognitive load during intense study sessions. Subtle depth is used to make the interface feel physical and reliable, while rounded forms soften the authoritative nature of the content. The goal is to transform a stressful preparation process into a structured, manageable, and positive journey.

## Colors
The palette is rooted in a sense of calm and clarity.
- **Primary (Sky Blue):** Used for primary actions, progress indicators, and active states. It evokes feelings of openness and optimism.
- **Secondary (Soft Yellow):** Employed as a highlight color for tips, reminders, and "aha!" moments. It provides a warm, sunny contrast without being visually jarring.
- **Background (White):** The primary canvas color, ensuring maximum readability and a clean "blank paper" feel.
- **Neutral (Slate/Off-white):** Used for subtle boundaries, secondary backgrounds, and text to maintain a professional hierarchy.

## Typography
This design system utilizes **Lexend** across all levels. Lexend was specifically designed to reduce visual stress and improve reading fluency, making it the perfect choice for an educational platform.

- **Headlines:** Set with medium to semi-bold weights to provide a clear structure to study modules.
- **Body Text:** Leverages generous line height (1.6) to ensure long-form educational content is easy to digest.
- **Labels:** Slightly tighter tracking and medium weights help distinguish interactive elements from static content.

## Layout & Spacing
The layout follows a **Fixed Grid** model on desktop to keep study materials centered and focused, transitioning to a fluid model on mobile. A 12-column grid is used for dashboard layouts, while a single-column, focused "reading mode" is used for practice exams.

The spacing rhythm is based on an 8px base unit. Wide margins and internal padding within components are encouraged to prevent the UI from feeling cluttered, reinforcing the "organized" brand pillar.

## Elevation & Depth
Depth is conveyed through **Ambient Shadows** that are soft, diffused, and slightly tinted with the primary Sky Blue color. This prevents shadows from looking "dirty" or overly heavy.

- **Level 1 (Cards/Buttons):** A very subtle 4px blur with 5% opacity blue-tinted shadow.
- **Level 2 (Dropdowns/Modals):** A 12px blur with 10% opacity blue-tinted shadow.
- **Surface Tiers:** Use Soft Yellow (#FFFACD) with 30% opacity for "sticky notes" or highlighted instructional callouts to lift them visually from the white background without needing heavy shadows.

## Shapes
In line with the "approachable" aesthetic, this design system avoids sharp corners. A consistent **Rounded (0.5rem)** corner radius is applied to standard components like input fields and buttons. Larger containers, such as lesson cards or progress panels, use **Rounded-LG (1rem)** or **Rounded-XL (1.5rem)** to emphasize a soft, friendly container for learning.

## Components
- **Buttons:** Feature fully rounded ends (pill-shaped) for primary actions. Use Sky Blue for primary buttons with white text, and Soft Yellow for secondary "encouragement" actions (like "Check Answer").
- **Cards:** White backgrounds with a 1px Soft Blue border or a Level 1 ambient shadow. Header areas of cards may use a Soft Yellow background to denote "Tip" or "Note" sections.
- **Input Fields:** Generous internal padding (16px) with a soft 0.5rem radius. Focus states should use a 2px Sky Blue glow.
- **Progress Indicators:** Use thick, rounded bars. The "track" should be a very pale blue, with the "fill" being the vibrant Sky Blue.
- **Chips:** Used for subject tags (e.g., "Mathematics," "Pedagogy"). These should be pill-shaped with light pastel fills and dark-colored text for accessibility.
- **Icons:** Use "friendly" line icons with rounded terminals. Avoid jagged edges or thin, clinical lines. Icons can be paired with a Soft Yellow circular background "blob" for added character.
- **Flashcards:** A unique component for this system, utilizing a Level 2 shadow and extra-large rounded corners (1.5rem) to mimic physical study cards.