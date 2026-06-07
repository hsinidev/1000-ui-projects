---
name: Architectural Digital Gallery
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
  on-surface-variant: '#4c4546'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#1a1c1c'
  on-tertiary-container: '#838484'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e2'
  primary-fixed-dim: '#c6c6c6'
  on-primary-fixed: '#1b1b1b'
  on-primary-fixed-variant: '#474747'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 80px
    fontWeight: '400'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.15em
  nav-item:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.0'
    letterSpacing: 0.02em
spacing:
  unit: 4px
  gutter: 24px
  margin-page: 80px
  section-gap: 160px
  container-max: 1440px
---

## Brand & Style

This design system is anchored in clinical precision and high-fidelity minimalism, specifically tailored for the architectural domain where the work must speak louder than the interface. The brand personality is silent, sophisticated, and authoritative. It draws heavily from Swiss Modernism, emphasizing a rational organization of space and a reductionist aesthetic.

The target audience consists of high-end clientele, developers, and design critics who value structural integrity and clarity. The UI evokes an emotional response of "controlled luxury"—the feeling of walking through a quiet, well-lit physical gallery where every detail is intentional. The visual style is characterized by extreme high contrast, rigorous alignment, and the complete absence of decorative ornamentation.

## Colors

The color palette is strictly monochrome to ensure that project photography is the only source of hue within the environment. 

- **Primary (#000000):** Used for all high-level typography, primary borders, and structural anchors.
- **Secondary (#FFFFFF):** The primary background color, serving as "the wall" of the gallery.
- **Accent Grey (#E0E0E0):** Utilized for structural lines, dividers, and inactive states to maintain hierarchy without breaking the high-contrast rhythm.
- **Subtle Grey (#F5F5F5):** Reserved for large-scale background shifts or hover states on interactive surfaces to provide a clinical, low-impact feedback loop.

## Typography

The typography strategy relies on a structural tension between two distinct classifications. Project titles and editorial narratives utilize a refined serif to convey heritage and intellectual depth. Technical data, navigation, and metadata utilize a geometric sans-serif to emphasize precision and modern engineering.

- **Headlines:** Set in a refined serif. Large-scale display sizes should use tighter tracking to create a "block-like" architectural presence.
- **Body:** Set in a professional, grounded sans-serif for maximum readability in architectural descriptions. 
- **Labels:** Set in a technical, geometric sans-serif, often in uppercase with generous letter spacing to evoke the feeling of blue-print annotations.

## Layout & Spacing

This design system employs a strict 12-column fixed grid with "luxurious" outer margins. The philosophy is based on the concept of *negative space as a structural element*. 

- **Margins:** Page margins are exceptionally wide (80px+) to frame the content like a matted photograph.
- **Section Gaps:** Significant vertical breathing room (160px) is required between project modules to allow the viewer to reset their focus.
- **Rhythm:** All vertical spacing must be a multiple of the 4px base unit, ensuring a mathematical rigor that mirrors architectural drafting.
- **Alignment:** Content should predominantly align to the left or center axis, with metadata often "hanging" in the margins to maintain the clinical grid feel.

## Elevation & Depth

Depth is conveyed through stacking and containment rather than shadows. This design system rejects all blurs and ambient shadows in favor of a "flat-layered" approach.

- **Structural Borders:** Hierarchy is defined by 1px solid lines. A #000000 border indicates a primary container, while a #E0E0E0 border indicates a secondary or nested element.
- **Tonal Layering:** In instances where depth is required (such as modals or overlays), a simple solid background shift to #F5F5F5 or #FFFFFF is used.
- **Line Work:** Vertical and horizontal hair-lines are used to separate technical data, mimicking the aesthetics of an architectural floor plan.

## Shapes

The shape language is uncompromisingly rectilinear. 

- **Corners:** Every UI element—including buttons, input fields, image containers, and cards—must have 0px corner radii. Sharp corners reinforce the themes of precision, clinical accuracy, and structural rigidity.
- **Stroke:** All strokes must be consistent at 1px. No varying stroke weights should be used unless for extreme emphasis (e.g., a 2px active state).

## Components

Components in this design system serve as the technical framework for the architectural imagery.

- **Buttons:** Rectangular with a 1px solid #000000 border. Default state is transparent/white background with black text. Hover state is a full black fill with white text (instant transition, no ease).
- **Project Cards:** Full-bleed image containers with 0px radius. Project titles appear below the image in the refined serif, while metadata (year, location) appears in the geometric sans-serif label style.
- **Navigation:** A minimalist top bar or side-docked rail. Text links only, no icons. Active states are indicated by a simple 1px underline.
- **Input Fields:** A single 1px bottom border (#000000). Labels sit above the line in small caps geometric sans-serif.
- **Gallery Lightbox:** Pure #FFFFFF background with "Close" and "Info" controls positioned at the extreme corners of the viewport, maintaining the generous margin philosophy.
- **Architectural Specs:** A custom component for project details, using a table-style grid with 1px #E0E0E0 dividers to list materials, square footage, and collaborators.