---
name: Sovereign Counsel
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
  on-surface-variant: '#44474e'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#465f88'
  primary: '#000a1e'
  on-primary: '#ffffff'
  primary-container: '#002147'
  on-primary-container: '#708ab5'
  inverse-primary: '#aec7f6'
  secondary: '#af2b3e'
  on-secondary: '#ffffff'
  secondary-container: '#fd6673'
  on-secondary-container: '#680018'
  tertiary: '#090b0c'
  on-tertiary: '#ffffff'
  tertiary-container: '#202222'
  on-tertiary-container: '#888989'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d6e3ff'
  primary-fixed-dim: '#aec7f6'
  on-primary-fixed: '#001b3d'
  on-primary-fixed-variant: '#2d476f'
  secondary-fixed: '#ffdada'
  secondary-fixed-dim: '#ffb3b5'
  on-secondary-fixed: '#40000b'
  on-secondary-fixed-variant: '#8e0f28'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-xl:
    fontFamily: newsreader
    fontSize: 60px
    fontWeight: '600'
    lineHeight: 72px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: 56px
  headline-md:
    fontFamily: newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: 40px
  headline-sm:
    fontFamily: newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: 32px
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 40px
---

## Brand & Style

This design system is engineered for a law firm that serves as a strategic shield for employers. The brand personality is unapologetically corporate, decisive, and authoritative. It aims to evoke an emotional response of absolute security and intellectual rigor.

The chosen style is **Corporate / Modern**, leaning heavily into traditional institutional structures but refined with modern digital precision. It prioritizes stability and trust through a highly organized visual hierarchy, favoring structured grids over fluid spontaneity. Every element is designed to feel permanent and deliberate, reflecting the high-stakes nature of labor law and employer representation.

## Colors

The palette is anchored in heritage and power. **Navy Blue (#002147)** serves as the primary color, utilized for structural elements, headers, and primary navigation to establish immediate authority. **Burgundy (#800020)** is reserved for high-importance call-to-actions and critical alerts, providing a sophisticated contrast that signals urgency without sacrificing professionalism.

**White** is the essential canvas, providing the necessary "air" to make complex legal information digestible. Neutral grays are used sparingly for borders and subtle backgrounds to maintain the structured grid without introducing visual clutter.

## Typography

This design system utilizes a sophisticated typographic pairing to balance tradition with utility. **Newsreader** is the headline face; its literary and authoritative character mimics the prestige of printed legal briefs and formal documentation. 

**Inter** is employed for all functional and body text. Its neutral, systematic design ensures maximum legibility in complex data environments, such as risk assessments and investigation reports. Large display headings use a tighter letter-spacing for a more modern, editorial feel, while labels use uppercase styling with increased tracking to denote categorization and hierarchy.

## Layout & Spacing

The layout philosophy is built upon a **Fixed Grid** model. This conveys stability and ensures that information is presented in a predictable, rhythmic fashion. A 12-column grid is standard for desktop, with generous gutters to prevent content density from becoming overwhelming.

Spacing follows a strict 8px base unit. Vertical rhythm is critical; section headers must have significant top-margin clearance to allow the eye to reset. Components are aligned to the grid with rigorous consistency, reinforcing the "structured" and "decisive" brand pillars.

## Elevation & Depth

This design system rejects excessive shadows in favor of **Low-contrast outlines and Bold borders**. Depth is communicated through structural layering rather than atmospheric effects.

1.  **Borders:** Use 1px solid lines in a muted version of the primary Navy or a mid-tone gray (#D1D5DB) to define containers.
2.  **Tonal Layers:** High-priority cards or "Investigation" modules use a very subtle off-white or light navy tint (#F8FAFC) to separate themselves from the primary background.
3.  **Shadows:** When necessary for interactivity (e.g., a hovered card), use a single, sharp "hard shadow" rather than a soft blur, maintaining the decisive, architectural feel of the UI.

## Shapes

The shape language is strictly **Sharp (0px)**. Roundness is perceived as approachable and soft, which conflicts with the authoritative and corporate nature of this design system. 

Every button, input field, and container features hard 90-degree angles. This geometric rigidity reinforces the concept of a firm that is structured, precise, and uncompromising. The only exception to this rule is the use of circular status indicators or radio buttons for standard accessibility and recognition.

## Components

### Buttons
Primary buttons are the "Request an Investigation" CTA. They are styled with a solid **Burgundy (#800020)** background, white uppercase Inter text, and no border. The "decisive" nature is captured through a high-contrast hover state that shifts to a darker shade of burgundy. Secondary buttons use the **Navy (#002147)** with a 1px border.

### Risk Mitigation Checklist
This interactive component uses a "split-pane" layout. On the left, a vertical list of risk categories; on the right, the interactive items. Checkboxes are custom-styled squares. When a risk is "mitigated," the item background shifts to a very light Navy tint, and the text undergoes a subtle opacity change.

### Input Fields
Inputs are minimalist: a 1px bottom-border only or a full sharp-edged stroke. Labels are consistently placed above the field in **Label-MD** typography. Error states are indicated by a 2px Burgundy border.

### Cards & Investigations
Investigation status cards use a thick left-hand border (4px) in either Burgundy (Critical), Navy (Active), or Gray (Archived) to signify status without relying solely on text.

### Navigation
A top-tier persistent bar in Navy Blue with white typography. Navigation links are capitalized with a subtle underline effect on hover, reflecting the professional and academic nature of the legal field.