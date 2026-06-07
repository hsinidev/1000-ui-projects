---
name: High-Velocity Growth
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#5a4136'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#8e7164'
  outline-variant: '#e2bfb0'
  surface-tint: '#a04100'
  primary: '#a04100'
  on-primary: '#ffffff'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#ffb693'
  secondary: '#7c5800'
  on-secondary: '#ffffff'
  secondary-container: '#feb700'
  on-secondary-container: '#6b4b00'
  tertiary: '#5f5e5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#9a9898'
  on-tertiary-container: '#313130'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#ffdea8'
  secondary-fixed-dim: '#ffba20'
  on-secondary-fixed: '#271900'
  on-secondary-fixed-variant: '#5e4200'
  tertiary-fixed: '#e5e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1c1b1b'
  on-tertiary-fixed-variant: '#474646'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 4.5rem
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  h2:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.03em
  h3:
    fontFamily: Inter
    fontSize: 2rem
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  body-lg:
    fontFamily: Work Sans
    fontSize: 1.25rem
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Work Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  button:
    fontFamily: Inter
    fontSize: 1rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.02em
  label:
    fontFamily: Inter
    fontSize: 0.875rem
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 0.5rem
  sm: 1rem
  md: 1.5rem
  lg: 2.5rem
  xl: 4rem
  gutter: 24px
  margin: 32px
  max_width: 1280px
---

## Brand & Style
The design system is engineered for high-performance marketing education. It targets ambitious professionals who demand speed, results, and modern expertise. The brand personality is aggressive yet disciplined—combining the raw energy of growth hacking with the precision of data analytics. 

The aesthetic leverages a **High-Contrast / Bold** movement with subtle nods to **Brutalism** through the use of sharp edges and dense information layouts. The visual language is designed to trigger a sense of urgency and momentum, using expansive white space to let the bold orange accents and high-contrast typography command attention. Every interface element is optimized for conversion, ensuring that the path from "interest" to "enrollment" is friction-focused and visually unavoidable.

## Colors
The palette is built on a "Signal & Void" strategy. **Bold Orange (#FF6B00)** serves as the primary signal color, reserved exclusively for interactive elements and critical growth metrics. The **Deep Black (#0F0F0F)** provides the structural weight, creating a grounded, professional frame. 

A signature **Success Gradient** transitions from the primary orange to a golden yellow, used for achievement states, high-value CTAs, and progress indicators. The **Off-White (#F9F9F9)** background ensures the interface remains breathable and reduces eye strain during long-form learning sessions, while maintaining a stark, modern contrast against the dark typography.

## Typography
The typography system uses **Inter** for headlines to achieve a technical, geometric authority. Headings should utilize heavy weights (Bold to Black) and tight letter-spacing to create a "wall of impact" for value propositions. 

**Work Sans** is selected for body copy due to its exceptional readability at various sizes, maintaining a professional and approachable tone. All labels and buttons use Inter in uppercase to instill a sense of command and clarity. Contrast is key: keep headline-to-body ratios high to ensure clear information hierarchy.

## Layout & Spacing
This design system employs a **Fixed Grid** model (12 columns) for desktop experiences to maintain a disciplined, editorial feel. The spacing rhythm is based on a 4px baseline grid, favoring larger "XL" gaps between major sections to emphasize the minimalist aesthetic. 

Content should be grouped in high-density modules separated by wide margins. This "Density vs. Air" approach mirrors the fast-paced nature of growth hacking—focused execution followed by strategic oversight. Use the **xl** spacing unit for section vertical padding to maintain the "premium bootcamp" vibe.

## Elevation & Depth
Depth is achieved through **Bold Borders** and **Tonal Layers** rather than soft shadows. This maintains the "Sharp & Energetic" requirement. 

- **Level 0 (Base):** Off-white background.
- **Level 1 (Cards):** White background with a 1px solid #0F0F0F border. 
- **Level 2 (Interactive):** Elements feature a 4px "hard shadow" (an offset solid fill of black) when hovered, creating a tactile, clickable feel without using blurs.
- **Overlays:** Use high-opacity (90%) black backdrops for modals to keep the focus entirely on the conversion task at hand.

## Shapes
The shape language is defined by **Soft** (Level 1) rounding. Most containers and buttons use a 4px (0.25rem) radius. This provides a "technical precision" look while avoiding the coldness of perfectly sharp 0px corners. 

Data visualizations and growth charts should use straight lines and sharp vertices to emphasize accuracy. Large image containers may use the `rounded-lg` (0.5rem) setting to slightly soften the photography of students and mentors, but all functional UI remains tight and architectural.

## Components
- **Buttons:** Primary CTAs use the "Success Gradient" with white uppercase text. Secondary buttons use a thick 2px black border with no fill.
- **Input Fields:** Sharp 1px black borders that turn Bold Orange on focus. Labels sit strictly above the field in uppercase Inter.
- **Chips/Tags:** Used for "Bootcamp Modules" or "Skills." Small, rectangular with a #0F0F0F background and white text.
- **Cards:** White background, 1px black border, and a 4px black hard shadow on hover. Headlines inside cards should be H3 or H4.
- **Progress Bars:** Thick 8px tracks in light grey with the "Success Gradient" representing completion. 
- **Conversion Dock:** A sticky footer or sidebar element for "Enroll Now" actions, using the Deep Black background and the Primary Orange for the button to ensure it is the highest-contrast element on any page.
- **Metric Displays:** Large, H1-sized orange numbers for "Growth Stats" (e.g., +240% ROI) to provide immediate visual proof of the bootcamp's value.