---
name: Kinetic Precision
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f3'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1b1b1b'
  on-surface-variant: '#434656'
  inverse-surface: '#303030'
  inverse-on-surface: '#f1f1f1'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004dea'
  primary: '#0041c8'
  on-primary: '#ffffff'
  primary-container: '#0055ff'
  on-primary-container: '#e3e6ff'
  inverse-primary: '#b6c4ff'
  secondary: '#5e5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2e2e2'
  on-secondary-container: '#646464'
  tertiary: '#4e5050'
  on-tertiary: '#ffffff'
  tertiary-container: '#666868'
  on-tertiary-container: '#e7e7e7'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#001551'
  on-primary-fixed-variant: '#0039b3'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1b1b1b'
  on-secondary-fixed-variant: '#474747'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#f9f9f9'
  on-background: '#1b1b1b'
  surface-variant: '#e2e2e2'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
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
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: '0'
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin: 40px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 80px
---

## Brand & Style

The brand personality is authoritative, high-energy, and surgically precise. This design system is built for a premium commercial real estate environment where speed of data and clarity of information are paramount. It avoids the soft, organic trends of consumer apps in favor of a "High-Contrast / Bold" aesthetic that feels engineered rather than merely designed.

The visual language draws from modern technical documentation and high-end automotive interfaces. By combining massive typography with a restricted, high-impact color palette, the UI evokes a sense of "Tech-Forward" urgency. The emotional response should be one of confidence and efficiency, positioning the platform as the definitive tool for high-stakes commercial leasing.

## Colors

This design system utilizes a stark, high-contrast palette to drive visual hierarchy. **Electric Blue (#0055FF)** is the primary action color, used strategically for interactive elements and key data highlights to maintain an energetic "glow" against the monochrome base.

**Deep Black (#000000)** and **Pure White (#FFFFFF)** form the structural foundation. There are no mid-tone greys; depth is created through the juxtaposition of solid black blocks and crisp white negative space. This "all-or-nothing" approach to color ensures that data visualizations and high-resolution photography remain the focal points without visual clutter.

## Typography

The typography strategy is a tale of two intents: impact and utility. **Space Grotesk** is used for all headlines and data-heavy callouts. Its geometric, slightly eccentric letterforms provide the "tech-forward" edge required for a modern leasing portal. Headlines should be set with tight letter-spacing to emphasize the bold, architectural nature of the font.

**Inter** serves as the workhorse for body text and UI labels. It provides maximum readability for complex lease terms and property details. To maintain the energetic vibe, labels are often set in uppercase with increased letter spacing, acting as "signposts" within the data-rich environment.

## Layout & Spacing

This design system employs a **Fixed Grid** philosophy to maintain a premium, editorial feel on desktop screens. A strict 12-column grid with a 1440px maximum width ensures that information density is controlled and consistent. 

The spacing rhythm is strictly based on an 8px square grid. Large "Section Gaps" are used to separate distinct property data sets, while tight "Stack" units keep related metadata clusters together. The layout should feel "locked-in" and architectural, avoiding fluid percentage-based widths where possible to maintain the integrity of the high-contrast color blocks.

## Elevation & Depth

To maintain the high-contrast, energetic vibe, this design system eschews traditional soft shadows and blurs. Instead, it uses **Bold Borders** and **Tonal Layers** to communicate hierarchy.

- **Primary Depth:** Achieved through solid Deep Black containers placed on Pure White backgrounds.
- **Interactive Depth:** Elements do not "lift" via shadows; instead, they change color (e.g., a white card gaining an Electric Blue 2px border on hover).
- **Overlays:** Use solid black or blue fills with 0% transparency for modals and menus to maintain a "hard" aesthetic. Depth is a matter of layering flat planes, not simulating light sources.

## Shapes

The shape language is defined by **Sharp Corners (0px)**. This reinforces the "Data-driven" and "Modern" narrative, suggesting precision and institutional strength. Every element—from buttons and input fields to high-resolution property cards—must adhere to these 90-degree angles. 

When subtle differentiation is needed for smaller UI components like tags or status indicators, a "very slight radius" of no more than 2px may be used, but the default state for the design system is strictly orthogonal.