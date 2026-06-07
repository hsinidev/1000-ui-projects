---
name: Clinical Precision
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
  on-surface-variant: '#43474c'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#74777c'
  outline-variant: '#c4c7cc'
  surface-tint: '#50606f'
  primary: '#4e5e6d'
  on-primary: '#ffffff'
  primary-container: '#667686'
  on-primary-container: '#fdfcff'
  inverse-primary: '#b8c8da'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#416261'
  on-tertiary: '#ffffff'
  tertiary-container: '#5a7a7a'
  on-tertiary-container: '#f3fffe'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e4f6'
  primary-fixed-dim: '#b8c8da'
  on-primary-fixed: '#0d1d2a'
  on-primary-fixed-variant: '#394857'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#c6e9e9'
  tertiary-fixed-dim: '#abcdcd'
  on-tertiary-fixed: '#002020'
  on-tertiary-fixed-variant: '#2c4c4c'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
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
    lineHeight: '1.6'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 8px
  container-max: 1200px
  gutter: 32px
  margin-page: 64px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 80px
---

## Brand & Style
The design system is anchored in the concept of surgical precision and medical excellence. It evokes an emotional response of absolute trust, cleanliness, and advanced technical proficiency. The target audience includes patients seeking complex oral and maxillofacial procedures and referring medical professionals who require clear, authoritative information.

The style is a disciplined **Minimalism** with a **Clinical** edge. It prioritizes functionality and clarity over decorative elements, using "negative space" as a functional tool to reduce cognitive load during high-stakes medical decision-making. The aesthetic is intentional, sharp, and uncompromisingly professional.

## Colors
The palette is strictly limited to ensure a medical-grade atmosphere. **Slate Grey (#708090)** serves as the primary brand color, used for key UI anchors, primary buttons, and iconography. **Sterile White (#FFFFFF)** is the foundational background color, ensuring maximum light and cleanliness.

A tertiary **Dark Slate (#2F4F4F)** is utilized for high-contrast text and deep structural elements to ensure accessibility standards are exceeded. Neutral greys are used sparingly for hairline dividers and subtle backgrounds to maintain the "white space" integrity without sacrificing layout structure.

## Typography
This design system utilizes a sophisticated typographic pairing to balance tradition with modernity. **Newsreader** is used for all headings to provide a classic, authoritative, and literary tone that suggests years of expertise and academic rigor.

**Inter** is the functional workhorse for all body copy, interface labels, and data displays. Its high x-height and neutral character ensure legibility in clinical contexts. Headlines should utilize tighter tracking for a more composed look, while labels utilize uppercase styling and wider tracking for immediate scanability.

## Layout & Spacing
The layout follows a **Fixed Grid** philosophy. A strict 12-column grid is used for desktop views, with generous gutters and page margins to prevent the UI from feeling "crowded." 

The spacing rhythm is based on an 8px base unit. Vertical rhythm is critical; use large "stack-lg" increments between major sections to emphasize the minimalist aesthetic. Alignment should be predominantly left-aligned to mirror medical documents and formal journals.

## Elevation & Depth
In alignment with the "sharp corners" and "medical-grade" requirements, this design system rejects soft shadows and blurs. Depth is conveyed through **Bold Borders** and **Tonal Layers**.

Surface elevations are represented by 1px solid borders in Slate Grey or very light grey (#E2E8F0). Elements do not "float" over the background; they are "carved" into it or separated by hair-thin dividers. This creates a flat, architectural feel that reinforces the precision of surgical instruments.

## Shapes
The shape language is defined by a **sharpness** value of 0. There are no rounded corners in this design system. Every button, input field, card, and container features 90-degree angles. This geometric rigidity communicates discipline, technical accuracy, and a modern clinical environment.

## Components
- **Buttons:** Solid Slate Grey backgrounds with White text for primary actions. Secondary actions use a 1px Slate Grey border with no fill. All buttons are rectangular with no corner radius.
- **Input Fields:** 1px Slate Grey borders. Labels sit strictly above the field in the "label-sm" style. No shadows or glows on focus; instead, use a 2px border thickness to indicate activity.
- **Cards:** Minimal containers with a 1px #E2E8F0 border. Use ample internal padding (32px) to ensure content clarity.
- **Chips/Badges:** Rectangular with Slate Grey text on a light grey background. Used for procedural categories or status updates.
- **Lists:** Separated by horizontal hair-thin lines. Avoid bullet points; use indentation or Slate Grey vertical bars for emphasis.
- **Checkboxes:** Square, sharp-edged, with a simple Slate Grey fill when active.
- **Additional Components:** "Data Tables" are critical for surgical stats and pricing; these should be border-collapsed and high-contrast. "Procedure Timeline" components should use vertical lines and sharp nodes to show patient journeys.