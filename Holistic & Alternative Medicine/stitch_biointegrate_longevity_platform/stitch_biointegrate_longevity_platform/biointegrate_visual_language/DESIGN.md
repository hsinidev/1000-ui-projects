---
name: BioIntegrate Visual Language
colors:
  surface: '#141316'
  surface-dim: '#141316'
  surface-bright: '#3a393c'
  surface-container-lowest: '#0f0e10'
  surface-container-low: '#1c1b1e'
  surface-container: '#201f22'
  surface-container-high: '#2b292c'
  surface-container-highest: '#363437'
  on-surface: '#e6e1e5'
  on-surface-variant: '#c9c5ce'
  inverse-surface: '#e6e1e5'
  inverse-on-surface: '#313033'
  outline: '#938f98'
  outline-variant: '#48454e'
  surface-tint: '#cac1ed'
  primary: '#cac1ed'
  on-primary: '#322b4f'
  primary-container: '#120b2e'
  on-primary-container: '#7f78a0'
  inverse-primary: '#605980'
  secondary: '#ceffdf'
  on-secondary: '#003921'
  secondary-container: '#01f5a0'
  on-secondary-container: '#006b43'
  tertiary: '#c7c4d9'
  on-tertiary: '#2f2f3f'
  tertiary-container: '#10101e'
  on-tertiary-container: '#7c7b8e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#e6deff'
  primary-fixed-dim: '#cac1ed'
  on-primary-fixed: '#1d1639'
  on-primary-fixed-variant: '#484267'
  secondary-fixed: '#50ffaf'
  secondary-fixed-dim: '#00e293'
  on-secondary-fixed: '#002111'
  on-secondary-fixed-variant: '#005232'
  tertiary-fixed: '#e3e0f5'
  tertiary-fixed-dim: '#c7c4d9'
  on-tertiary-fixed: '#1a1a29'
  on-tertiary-fixed-variant: '#464556'
  background: '#141316'
  on-background: '#e6e1e5'
  surface-variant: '#363437'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Space Grotesk
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
    lineHeight: '1.5'
    letterSpacing: '0'
  data-display:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

The design system is engineered to evoke a sense of clinical precision, advanced longevity science, and absolute data security. It targets a high-net-worth audience interested in biohacking and functional medicine.

The visual style is a hybrid of **Minimalism** and **Glassmorphism**, set against a mandatory dark-themed environment. The aesthetic prioritizes legibility and data density without overwhelming the user. Key visual drivers include:
*   **Scientific Rigor:** High-contrast data points and monospaced accents reflect a laboratory-grade interface.
*   **Futuristic Vitality:** Neon accents represent the "spark" of biological optimization.
*   **Depth and Transparency:** Layers of frosted glass create a sophisticated sense of hierarchy, mimicking the complexity of biological systems.
*   **Security:** Thin, precise borders and structured layouts instill confidence in the handling of sensitive health information.

## Colors

The design system utilizes a deep, nocturnal palette to emphasize high-tech immersion and reduce eye strain during data analysis.

*   **Primary (Deep Indigo):** Used for structural depth and primary brand moments. It provides a more sophisticated alternative to pure black.
*   **Accent (Neon Mint):** Reserved for critical bio-data, progress indicators, "Optimal" health ranges, and interactive call-to-actions. It should be used sparingly to maintain high impact.
*   **Backgrounds:** Pure Black is the base for all screens to ensure maximum contrast and "infinity" depth. Dark Indigo grays are used for container backgrounds to create subtle layering.
*   **Typography:** White is reserved for primary headers and critical values. Muted Silver (Indigo-tinted gray) is used for labels, descriptions, and secondary metadata to establish a clear information hierarchy.

## Typography

The design system employs a dual-font strategy to balance human-centric readability with technical sophistication.

**Inter** is the workhorse for all body copy, instructional text, and medical descriptions. It provides a clean, neutral canvas that ensures high legibility for complex health reports.

**Space Grotesk** serves as the "Scientific Accent" font. Its geometric, slightly technical character is used for headlines, biomarkers, and any numerical data points. All biomarker values and time-stamps should use the `data-display` or `label-caps` styles to emphasize the biohacking/lab-result feel.

## Layout & Spacing

The design system follows an 8px grid system to ensure mathematical harmony across all views. 

The layout philosophy utilizes a **fixed-width grid** (12 columns) for desktop environments to maintain a "command center" feel, while shifting to a fluid vertical stack for mobile. 

*   **Margins:** Generous outer margins (40px+) emphasize the premium nature of the brand.
*   **Rhythm:** Spacing between data cards should remain tight (16px or 24px) to keep related biomarkers grouped, while major sections are separated by 64px+ to allow the eye to rest.
*   **Data Density:** Information-heavy views (like lab results) should utilize the 8px unit strictly to maximize the "dashboard" utility without sacrificing clarity.

## Elevation & Depth

Hierarchy in this design system is achieved through **Glassmorphism** and tonal layering rather than traditional heavy shadows.

*   **Level 0 (Base):** Pure Black (#000000).
*   **Level 1 (Surface):** Dark Indigo gray with a 1px border of `rgba(255, 255, 255, 0.05)`.
*   **Level 2 (Active/Floating):** Frosted glass effect. Background blur set to 20px with a semi-transparent Deep Indigo fill (`rgba(18, 11, 46, 0.7)`).
*   **Interactive Glow:** High-priority elements (like active progress rings or health alerts) utilize a subtle outer glow using the Neon Mint accent color (`drop-shadow: 0 0 15px rgba(0, 245, 160, 0.3)`).

Borders are always thin (1px) and use low-opacity white or indigo-silver to define boundaries without adding visual bulk.

## Shapes

The design system uses a **Soft** shape language to bridge the gap between clinical instruments and high-end consumer technology.

*   **Standard Elements:** Cards, input fields, and buttons use a 4px (0.25rem) corner radius. This maintains a precise, engineered look.
*   **Data Containers:** Larger dashboard modules or modal overlays use 8px (0.5rem) to feel more approachable.
*   **Data Visualization:** Circular elements (progress rings, health dials) are used extensively for holistic scores. These should always be perfect circles to contrast against the rectangular grid of the UI.

## Components

### Buttons
*   **Primary:** Solid Neon Mint background with Pure Black text. 4px radius. Use for "Book Consultation" or "Save Protocol."
*   **Secondary:** Ghost style. 1px Neon Mint border with White text.
*   **Tertiary:** Glass style. Semi-transparent Indigo background with White text and subtle blur.

### Data Visualization
*   **Health Timelines:** Thin horizontal lines with "biomarker nodes." Active nodes should glow in Neon Mint.
*   **Progress Rings:** Circular gauges with a thickness of 4px. Use a muted indigo track and a Neon Mint "fill" to represent percentage completion of health goals.
*   **Trend Charts:** Line charts using 2px thick paths. Avoid area fills unless they are high-transparency gradients (Mint to Transparent).

### Cards & Containers
*   Cards are the primary container for biomarkers. They feature a 1px border, a subtle background blur, and a headline in `label-caps`. 
*   Incorporate "Biomarker Badges"—small monospaced labels that indicate whether a value is "Optimal," "Sub-optimal," or "Critical" using color-coded status glows (Mint for Optimal, Amber for Sub-optimal).

### Inputs & Selectors
*   Fields are dark-filled with 1px borders that glow subtly when focused.
*   Labels always use `label-caps` and are positioned above the input field for maximum clarity.