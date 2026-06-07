---
name: Executive Precision
colors:
  surface: '#fbf9f8'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e4e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#4c4546'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#7e7576'
  outline-variant: '#cfc4c5'
  surface-tint: '#5e5e5e'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#1b1b1b'
  on-primary-container: '#848484'
  inverse-primary: '#c6c6c6'
  secondary: '#214ae2'
  on-secondary: '#ffffff'
  secondary-container: '#4365fb'
  on-secondary-container: '#fffbff'
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
  secondary-fixed: '#dee1ff'
  secondary-fixed-dim: '#b9c3ff'
  on-secondary-fixed: '#001257'
  on-secondary-fixed-variant: '#0033c2'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f8'
  on-background: '#1b1c1c'
  surface-variant: '#e4e2e2'
typography:
  display-xl:
    fontFamily: Noto Serif
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
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
  label-bold:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '500'
    lineHeight: '1.2'
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 32px
  margin-page: 64px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
  section-gap: 96px
---

## Brand & Style

The design system is engineered for a high-end demographic that values efficiency, exclusivity, and professional rigor. The brand personality is "The Discerning Concierge"—highly organized, minimalist, and authoritative. 

The visual style is a fusion of **Minimalism** and **High-Contrast Corporate**. It prioritizes a stark, binary foundation to evoke a sense of clarity and expensive simplicity. By stripping away unnecessary ornamentation, the design system focuses the user's attention on high-quality photography and critical data points. The emotional response is one of instant trust and premium service, delivered through an interface that feels both digitally native and editorially curated.

## Colors

This design system utilizes a high-contrast palette to establish a clear hierarchy and corporate authority. 

- **Deep Black (#000000):** Used for primary headings, borders, and structural containers to ground the UI.
- **Crisp White (#FFFFFF):** The primary surface color, used generously to create an open, airy feeling.
- **Electric Blue (#2F54EB):** A high-intensity accent reserved exclusively for calls-to-action, active states, and critical interaction cues.
- **Corporate Neutrals:** A range of cool greys is used for secondary text and subtle dividers to maintain a clean aesthetic without the harshness of pure black-on-white for long-form reading.

## Typography

The typography strategy pairs a sophisticated serif for storytelling with a utilitarian sans-serif for data and navigation.

- **Headlines:** Noto Serif is employed to provide an editorial, premium feel. Larger display sizes should use tighter letter spacing to maintain a "locked-in" corporate look.
- **Body & UI:** Inter provides a systematic, neutral backdrop for functional information. Its high x-height ensures legibility across dense property management dashboards.
- **Labels:** Use uppercase Inter with increased letter spacing for category labels and small metadata to differentiate functional UI from narrative content.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to ensure content remains centered and controlled, reflecting a disciplined corporate identity. 

- **The 8px Rule:** All spacing increments must be multiples of 8px to maintain a rhythmic vertical cadence.
- **Generous Whitespace:** Section gaps are intentionally large (96px+) to prevent the interface from feeling cluttered or "budget."
- **Grid:** A 12-column grid is used for property listings and dashboards. Gutters are wide (32px) to give each module room to breathe, reinforcing the premium nature of the listings.

## Elevation & Depth

Hierarchy in this design system is primarily driven by contrast and scale rather than heavy shadows. 

- **Tonal Layers:** Deep black containers are used for footer areas or high-impact sidebars to create immediate depth against white primary surfaces.
- **Subtle Shadows:** Use a single, highly-diffused ambient shadow for floating elements like dropdowns or cards (e.g., `0px 10px 30px rgba(0,0,0,0.05)`). The shadow should be barely perceptible, serving only to separate the element from the background without breaking the "flat" corporate aesthetic.
- **Flat Borders:** Use 1px solid lines in light grey (#E5E5E5) for structural divisions, ensuring edges remain sharp and defined.

## Shapes

To reflect a "sharp, clean-edged" corporate identity, this design system utilizes a **Sharp (0)** roundedness level. 

- **Right Angles:** All buttons, input fields, cards, and image containers must have 0px border-radius. This geometric rigidity conveys precision, stability, and a modern architectural influence.
- **Interactive States:** Changes in state (hover/active) should be signaled via color shifts or thickness of borders rather than softening of edges.

## Components

- **Buttons:** Primary buttons are solid Deep Black with White text. Secondary buttons are outlined (1px Deep Black). The "Electric Blue" is reserved for the most critical action on a page (e.g., "Book Now" or "Submit Application"). All buttons have 0px radius and 16px vertical / 32px horizontal padding.
- **Input Fields:** Use a simple 1px Deep Black bottom border or a full 1px border. Labels should be small, uppercase Inter. Focus states utilize a 2px Electric Blue border.
- **Cards:** Property cards feature full-bleed imagery with a 0px border-radius. Text content below the image should be aligned to a strict vertical axis.
- **Chips/Badges:** Small, rectangular labels with 0px radius. Use Black background with White text for premium status (e.g., "Verified") and White background with Black border for categories.
- **Lists:** High-density data lists in the management dashboard should use subtle 1px horizontal dividers and avoid zebra-striping to maintain a clean look.
- **Property Hero:** A signature component featuring a large-scale Noto Serif headline overlaid on high-contrast photography with a clear, Electric Blue primary action.