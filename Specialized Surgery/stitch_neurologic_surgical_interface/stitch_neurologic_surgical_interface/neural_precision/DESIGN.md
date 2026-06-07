---
name: Neural Precision
colors:
  surface: '#121414'
  surface-dim: '#121414'
  surface-bright: '#38393a'
  surface-container-lowest: '#0d0e0f'
  surface-container-low: '#1a1c1c'
  surface-container: '#1e2020'
  surface-container-high: '#282a2b'
  surface-container-highest: '#333535'
  on-surface: '#e2e2e2'
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e2e2e2'
  inverse-on-surface: '#2f3131'
  outline: '#849495'
  outline-variant: '#3a494b'
  surface-tint: '#00dbe7'
  primary: '#e1fdff'
  on-primary: '#00363a'
  primary-container: '#00f2ff'
  on-primary-container: '#006a71'
  inverse-primary: '#00696f'
  secondary: '#c6c4df'
  on-secondary: '#2f2e43'
  secondary-container: '#47475d'
  on-secondary-container: '#b8b6d0'
  tertiary: '#f8f8f8'
  on-tertiary: '#303030'
  tertiary-container: '#dbdbdb'
  on-tertiary-container: '#606060'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#74f5ff'
  primary-fixed-dim: '#00dbe7'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e2e0fc'
  secondary-fixed-dim: '#c6c4df'
  on-secondary-fixed: '#1a1a2e'
  on-secondary-fixed-variant: '#45455b'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#121414'
  on-background: '#e2e2e2'
  surface-variant: '#333535'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  label-data:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '400'
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
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  gutter: 16px
  margin: 24px
---

## Brand & Style

This design system is engineered to evoke the atmosphere of a high-stakes surgical suite where human biology meets advanced computation. The brand personality is clinical, authoritative, and visionary, targeting surgeons, medical researchers, and high-net-worth patients who demand the apex of technological reliability.

The visual style utilizes **Technical Minimalism** paired with **Glassmorphism**. It avoids unnecessary ornamentation, favoring "functional beauty" derived from data density and architectural structure. The emotional response should be one of profound trust—conveying that every pixel is as precise as a robotic scalpel. 

Visual metaphors center on the "Digital Anatomy." Interfaces should feel like heads-up displays (HUDs) or high-resolution medical imaging software, utilizing thin-line iconography and microscopic detail to reinforce the institute's commitment to microscopic neuro-surgical accuracy.

## Colors

The palette is strictly restricted to reinforce a high-contrast, diagnostic environment. 

- **Pure Black (#000000):** Used for the deepest background layers to simulate the void of a dark operating room or the depth of an MRI scan.
- **Deep Indigo (#1A1A2E):** Serves as the primary surface color for containers, cards, and navigation elements. It provides a sophisticated depth that prevents the UI from feeling flat.
- **Neon Cyan (#00F2FF):** The "Pulse" of the system. Reserved for active states, critical data points, and interactive triggers. This color should be used sparingly to ensure it maintains its high-signal value.
- **Neutral Silver (#E0E0E0):** Used exclusively for typography and icon paths to ensure maximum legibility against the dark backgrounds.

Functional color variants (Success/Warning/Error) should be desaturated to fit the palette, using Cyan for success and a muted Blood Orange for errors.

## Typography

Typography in this design system prioritizes scanning efficiency and technical character. 

**Space Grotesk** is utilized for headlines and labels. Its geometric, slightly "engineered" letterforms evoke the aesthetic of scientific instrumentation. All-caps treatments should be applied to small labels and data headers to mimic the look of surgical monitors.

**Inter** is the workhorse for all body copy and long-form medical text. It is chosen for its exceptional legibility and neutral character, ensuring that complex medical information remains the focus. 

Line heights are generous to prevent visual fatigue in high-information environments, while letter spacing is tightened on large headlines for a modern, aggressive tech feel.

## Layout & Spacing

This design system uses a **Fixed Grid** model on desktop (12 columns, 1200px max-width) and a fluid 4-column model on mobile. 

The rhythm is built on a 4px base unit. Spacing should feel deliberate and airy; sections are separated by large "voids" of Pure Black to emphasize the importance of the content within the Deep Indigo containers. 

Instead of traditional padding for separation, use **Thin-Line Architecture**. Use 1px borders of low-opacity Cyan or Indigo to define boundaries, creating a "schematic" feel. Gutters are kept tight (16px) to maintain a sense of digital density and interconnectedness, echoing neural network pathways.

## Elevation & Depth

Hierarchy is established through **Tonal Layering** and **Luminescent Accents** rather than traditional drop shadows.

1.  **Level 0 (Floor):** Pure Black (#000000). The foundation.
2.  **Level 1 (Sub-surface):** Deep Indigo (#1A1A2E). Used for navigation bars and secondary sidebar content.
3.  **Level 2 (Active Surface):** Deep Indigo with a 1px #00F2FF border at 20% opacity. Used for primary cards and modals.
4.  **Level 3 (Interactive):** Elements that are hovered or focused gain an "Inner Glow" (0 0 10px #00F2FF at 30% opacity) and an increase in border brightness.

Glassmorphism should be applied to floating overlays (like tooltips or dropdowns), using a backdrop blur of 12px and a semi-transparent Deep Indigo fill. This simulates the look of a digital overlay on a surgical monitor.

## Shapes

The shape language is "Soft-Precision." While surgical instruments are sharp, the digital interface should feel modern and accessible.

A consistent **4px (0.25rem)** corner radius is applied to all primary UI elements, such as buttons, input fields, and cards. This provides a subtle "machined" edge that feels finished without the friendliness of highly rounded forms. 

For decorative elements or progress indicators, sharp 0px angles are preferred to maintain the scientific rigor of the aesthetic. Data visualization nodes (neural points) should be perfect circles to contrast against the rectangular structural grid.

## Components

### Buttons
Primary buttons use a solid Neon Cyan fill with Pure Black text for maximum visibility. Secondary buttons are "Ghost" style—1px Cyan borders with transparent backgrounds. Active states must trigger a 5px outer glow of Cyan.

### Inputs
Fields should not be fully enclosed boxes. Use a bottom-only 1px border or a very subtle Indigo background with a Cyan indicator on focus. Labels should be in `label-caps` typography, placed above the field with a monospaced "01, 02, 03" numbering system for complex forms.

### Cards
Cards are defined by their Deep Indigo fill and thin borders. They should never have shadows. If multiple cards are grouped, they should be separated by 1px Indigo lines to appear as a single integrated unit.

### Neural Data Visualizer (Specialty Component)
A custom component for representing spine/brain data. This uses thin 0.5px lines to connect data nodes. Nodes should pulsate with a Cyan glow when active.

### Scanners
Progress bars should be stylized as "Scanners," featuring a vertical or horizontal line that passes over the content area, leaving a brief light-trail effect, simulating medical imaging in progress.