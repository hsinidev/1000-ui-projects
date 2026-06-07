---
name: Executive Command
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
  on-surface-variant: '#584141'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#8c7071'
  outline-variant: '#e0bfbf'
  surface-tint: '#af2b3e'
  primary: '#570013'
  on-primary: '#ffffff'
  primary-container: '#800020'
  on-primary-container: '#ff828a'
  inverse-primary: '#ffb3b5'
  secondary: '#4b53bc'
  on-secondary: '#ffffff'
  secondary-container: '#8991fe'
  on-secondary-container: '#1b218f'
  tertiary: '#252829'
  on-tertiary: '#ffffff'
  tertiary-container: '#3b3e3f'
  on-tertiary-container: '#a7a9aa'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdada'
  primary-fixed-dim: '#ffb3b5'
  on-primary-fixed: '#40000b'
  on-primary-fixed-variant: '#8e0f28'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#00006e'
  on-secondary-fixed-variant: '#3239a3'
  tertiary-fixed: '#e1e3e4'
  tertiary-fixed-dim: '#c5c7c8'
  on-tertiary-fixed: '#191c1d'
  on-tertiary-fixed-variant: '#454748'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Newsreader
    fontSize: 20px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Newsreader
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.08em
  button:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.0'
spacing:
  unit: 4px
  container-max: 1280px
  gutter: 24px
  margin-edge: 48px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is engineered to reflect the high-stakes environment of elite B2B sales. The personality is authoritative, uncompromising, and prestigious. It targets high-level professionals who value precision, tradition, and results.

The visual style is a fusion of **Minimalism** and **Corporate/Modern**, prioritizing clarity and structural integrity. By utilizing a high-contrast palette and sharp geometry, the interface evokes the feeling of a bespoke boardroom presentation. Every element is intentional, removing unnecessary ornamentation to focus on data density and actionable insights. The emotional response should be one of immediate trust and the recognition of "expert status."

## Colors

The color strategy uses deep, traditional tones to establish a "Corporate-Elite" atmosphere. 

- **Primary (Deep Burgundy):** Reserved strictly for primary call-to-actions, critical highlights, and brand-defining moments. It signifies power and urgency.
- **Secondary (Navy Blue):** Used for structural elements like headers, sidebars, and secondary navigation. It provides a stable, professional foundation.
- **Neutral/Background:** The design defaults to a "Crisp White" base for content areas to ensure maximum readability. A light grey (#F8F9FA) is used for subtle sectioning.
- **Interactive States:** High-contrast shifts are mandatory. Hovering on Burgundy should move toward a deeper shade or introduce a crisp Navy border. Text on dark backgrounds must remain 100% white for accessibility and "sharpness."

## Typography

This design system employs a sophisticated typographic pairing to balance modern efficiency with traditional authority. 

**Inter** is used for all functional and structural elements (Headlines, Labels, Buttons, Navigation). It should be set with tight letter-spacing in headlines to create a "dense" and "heavy" professional feel.

**Newsreader** is utilized for body copy, long-form insights, and quotes. This serif choice signals a literary and academic pedigree, vital for a high-ticket bootcamp environment. 

All labels and meta-data should use Inter in All-Caps with increased tracking to differentiate "data" from "narrative."

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** model for desktop to maintain a controlled, editorial appearance. Content is organized on a 12-column grid.

Spacing is governed by a strict 4px baseline grid. Information hierarchy is enforced through generous vertical "Stack" spacing between sections, while keeping related data points tightly grouped. 

Margins are wide to allow the content to "breathe" and appear premium. Data-dense layouts (like negotiation tables or curriculum schedules) should use 8px cell padding to maximize information density without sacrificing the sharp, organized aesthetic.

## Elevation & Depth

To maintain the "Corporate-Elite" aesthetic, elevation is handled with extreme subtlety. This system avoids floating elements or heavy blurs.

- **Subtle Drop Shadows:** Use only for primary interactive cards and modals. Shadows should be "sharp" (low blur radius, e.g., 4-8px) and use a high-opacity Navy Blue tint rather than pure black to feel integrated into the palette.
- **Tonal Layering:** Depth is primarily created through background color shifts (e.g., a Navy sidebar against a White content area). 
- **Borders over Shadows:** Prefer 1px solid borders in Navy or Light Grey to define containers. This reinforces the "Sharp" aesthetic more effectively than soft shadows.

## Shapes

The shape language is strictly **Sharp**. 

- **0px Border Radius:** Applied to all buttons, input fields, cards, and containers. This communicates a non-nonsense, industrial, and precise brand character.
- **Line Weights:** 1px lines are the standard. 2px lines may be used for active state underlines or primary button borders to increase visual weight.
- **Iconography:** Use geometric, stroke-based icons with sharp miters and no rounded caps.

## Components

- **Buttons:** Rectangular with 0px radius. Primary buttons use Deep Burgundy with White text. Secondary buttons use Navy Blue or a "Ghost" style with a 1px Navy border. Hover states must be an immediate color inversion or a significant darkening.
- **Input Fields:** Bottom-border only or full 1px border. Use Newsreader for user-input text and Inter for labels. Error states use a high-contrast Red, maintaining the sharp-cornered box.
- **Cards:** White background with a 1px light grey border. No shadow by default; apply a subtle sharp shadow on hover to indicate interactivity.
- **Progress Bars:** For "Negotiation Mastery" or "Course Completion," use a 2-tone Navy and Burgundy bar with sharp ends.
- **Data Tables:** High-density, 1px horizontal dividers only. Header rows should be Navy Blue with White Inter (All-Caps) text.
- **Chips/Tags:** Sharp-edged boxes. Use Navy backgrounds for category tags and Burgundy for "Live" or "Urgent" status indicators.
- **Modals:** Centered, 0px radius, heavy Navy border. The backdrop should be a high-opacity Navy Blue overlay (80-90%) to completely focus the user on the task.