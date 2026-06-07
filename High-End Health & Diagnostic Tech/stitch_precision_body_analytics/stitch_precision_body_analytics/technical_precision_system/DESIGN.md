---
name: Technical Precision System
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
  on-surface-variant: '#44474a'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f1f1f1'
  outline: '#75777a'
  outline-variant: '#c5c6ca'
  surface-tint: '#5d5e61'
  primary: '#000101'
  on-primary: '#ffffff'
  primary-container: '#1a1c1e'
  on-primary-container: '#838486'
  inverse-primary: '#c6c6c9'
  secondary: '#585f62'
  on-secondary: '#ffffff'
  secondary-container: '#dae1e4'
  on-secondary-container: '#5d6467'
  tertiary: '#000101'
  on-tertiary: '#ffffff'
  tertiary-container: '#002021'
  on-tertiary-container: '#009395'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#e2e2e5'
  primary-fixed-dim: '#c6c6c9'
  on-primary-fixed: '#1a1c1e'
  on-primary-fixed-variant: '#454749'
  secondary-fixed: '#dde3e7'
  secondary-fixed-dim: '#c1c8cb'
  on-secondary-fixed: '#161d1f'
  on-secondary-fixed-variant: '#41484b'
  tertiary-fixed: '#5af8fb'
  tertiary-fixed-dim: '#2ddbde'
  on-tertiary-fixed: '#002020'
  on-tertiary-fixed-variant: '#004f51'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  headline-lg:
    fontFamily: JetBrains Mono
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  mono-data:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1280px
---

## Brand & Style

The design system is rooted in the "Engineering-Grounded" aesthetic, prioritizing clinical accuracy and structural transparency. It targets a sophisticated demographic—athletes, medical patients, and longevity enthusiasts—who demand data integrity over decorative flair.

The UI avoids soft trends, instead adopting a **Modern-Brutalist** hybrid style. This is characterized by rigid structural grids, visible 1px boundaries, and a "form follows function" philosophy. The emotional response is one of absolute reliability, calm authority, and technical superiority. It feels like a high-end laboratory instrument: cold enough to be precise, but organized enough to be approachable.

## Colors

The palette is anchored in a grayscale spectrum to maintain a medical-grade atmosphere. 
- **Primary & Neutral:** We use "Earthy Grey" (#1A1C1E) for text and structural lines to provide a softer alternative to pure black, paired with "Silver" and "White" surfaces.
- **Functional Accents:** Color is reserved strictly for data visualization and status. 
- **Lean Mass (Teal/Blue):** High-contrast #20B2AA represents healthy tissue.
- **Fat Mass (Amber):** #FFBF00 is used for adipose tissue, providing a warm contrast that is distinct from warning-reds.
- **System Feedback:** Use subtle blue-greys for interactive states, ensuring no element distracts from the core medical data.

## Typography

This design system utilizes a dual-font strategy to balance legibility with technical character.
- **Primary Sans (Inter):** Used for all long-form body copy and descriptions to ensure maximum readability and a modern medical feel.
- **Technical Mono (JetBrains Mono):** Used for headlines, data points, labels, and coordinates. This emphasizes the "measured" nature of DEXA scans. 
- **Formatting:** Labels should frequently use uppercase with increased letter-spacing to mimic engineering blueprints. All numerical data must be monospaced to prevent layout shift during updates.

## Layout & Spacing

The layout is governed by a **Strict 12-Column Grid** with a 4px base unit. 
- **Alignment:** Every element must snap to the grid. Use 1px borders as visual "guides" that remain visible in the UI to reinforce the sense of a structured report.
- **Gutters:** Maintain a constant 16px gutter between cards and data modules.
- **Density:** High information density is encouraged. Negative space should be used strategically to group related data clusters rather than just for "breathing room."
- **Borders:** Instead of using whitespace to separate sections, use 1px solid borders in #D1D5DB.

## Elevation & Depth

This system intentionally avoids shadows to maintain a flat, clinical profile. 
- **Tonal Layering:** Depth is achieved through "Tonal Stacking." Backgrounds use #FFFFFF, while interactive or secondary containers use #F5F5F5.
- **Strict Flatness:** No ambient shadows or blurs. If an element is "above" another (like a modal), it is differentiated by a heavy 2px border and a distinct background color shift, not a shadow.
- **Precision Lines:** Use 1px and 2px strokes to define hierarchy. A 2px border indicates a primary container or focused state; 1px is the default for all other subdivisions.

## Shapes

The design system uses a **Sharp (0px)** corner radius across all components. This architectural approach reinforces the "Engineering-Grade" aesthetic. Roundness is perceived as "soft" or "consumer-grade," whereas sharp 90-degree angles communicate precision, accuracy, and technical rigidity. 

Exception: Only circular elements (like radio buttons or status pips) are allowed to be non-rectangular.

## Components

- **Buttons:** Rectangular with 1px solid borders. Primary buttons use a dark earthy-grey fill with white mono text. Ghost buttons use a 1px border and transition to a subtle silver fill on hover.
- **Data Cards:** 1px bordered containers. Headers are separated by a horizontal 1px line. All cards should include a small "coordinate" or "ID tag" in the top-right corner in 10px mono font.
- **Inputs:** Flat fields with 1px borders. Focused states change the border color to the primary accent (Teal) and increase stroke weight to 2px.
- **Visualization:** Bar charts and body maps should use flat blocks of color (#accent_lean_hex and #accent_fat_hex) without gradients.
- **Status Chips:** Small rectangular boxes with monospaced labels. Use a light silver background for neutral states and high-contrast accents for biological markers.
- **Grid Lines:** Decorative but functional 1px vertical and horizontal lines may extend beyond containers to the edge of the viewport to simulate a continuous drafting sheet.