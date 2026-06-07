---
name: JusticeFlow
colors:
  surface: '#fbf9f9'
  surface-dim: '#dbdad9'
  surface-bright: '#fbf9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3f3'
  surface-container: '#efeded'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e2'
  on-surface: '#1b1c1c'
  on-surface-variant: '#5b403d'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#8f6f6c'
  outline-variant: '#e4beba'
  surface-tint: '#ba1a20'
  primary: '#af101a'
  on-primary: '#ffffff'
  primary-container: '#d32f2f'
  on-primary-container: '#fff2f0'
  inverse-primary: '#ffb3ac'
  secondary: '#5f5e5e'
  on-secondary: '#ffffff'
  secondary-container: '#e2dfde'
  on-secondary-container: '#636262'
  tertiary: '#565858'
  on-tertiary: '#ffffff'
  tertiary-container: '#6e7070'
  on-tertiary-container: '#f4f4f4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb3ac'
  on-primary-fixed: '#410003'
  on-primary-fixed-variant: '#930010'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c7'
  on-tertiary-fixed: '#1a1c1c'
  on-tertiary-fixed-variant: '#454747'
  background: '#fbf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  display:
    fontFamily: Inter
    fontSize: 4.5rem
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-h1:
    fontFamily: Inter
    fontSize: 3rem
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-h2:
    fontFamily: Inter
    fontSize: 2.25rem
    fontWeight: '700'
    lineHeight: '1.3'
  headline-h3:
    fontFamily: Inter
    fontSize: 1.5rem
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Public Sans
    fontSize: 1.25rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 1rem
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Public Sans
    fontSize: 0.875rem
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 0.75rem
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  stack-sm: 8px
  stack-md: 24px
  stack-lg: 48px
---

## Brand & Style

This design system is built for the "Defender" archetype. It represents an unwavering commitment to justice, combining the urgency of civil liberties with the stoic stability of a high-end criminal defense firm. The brand personality is courageous, direct, and authoritative. It does not apologize for its presence; it stands as a monolith of reliability in high-stakes environments.

The visual style is **High-Contrast / Bold** with a focus on **Structural Minimalism**. We avoid decorative flourishes in favor of raw, architectural layouts that convey the gravity of legal proceedings. Every element serves to direct the user toward critical information or immediate action, utilizing extreme contrast to create a clear path through complex legal landscapes.

## Colors

The palette is restricted to three high-impact tones to maintain a serious and institutional tone. **Deep Charcoal (#1A1A1A)** is the foundation, used for headers, text, and heavy structural blocks to provide a sense of grounded authority. **Alert Red (#D32F2F)** is the primary action color, reserved strictly for calls to action, urgent status indicators, and critical navigational points—symbolizing courage and the "stop and look" nature of defense work.

**Pure White (#FFFFFF)** serves as the canvas, providing maximum legibility and "legal paper" clarity. This design system relies on a light default mode to ensure that long-form legal documents and case details remain accessible and professional under high-stress conditions.

## Typography

Typography in this design system is divided into two distinct functional roles. **Inter** is utilized for headlines and labels; its systematic and utilitarian nature provides the "Bold and Authoritative" voice required for the headers. Headlines should be set with tight leading and slight negative letter-spacing to create a compact, heavy visual weight.

**Public Sans** is the body typeface, chosen for its institutional clarity and neutral "official" tone. It ensures that legal citations, case summaries, and fine print are highly legible. We use a generous line-height for body text to maintain readability during extended periods of review. **Label-caps** should be used for status indicators and category tags to differentiate them from prose.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop to maintain a rigid, disciplined structure that mirrors legal documentation. A 12-column grid is used with substantial gutters to ensure content density never feels overwhelming or chaotic. 

The spacing rhythm is strictly based on an 8px scale. We prioritize vertical "stacking" to create a clear hierarchy of information. Large "stack-lg" gaps are used to separate major sections of a case or legal filing, while "stack-sm" is used to keep related data points (like a case number and its status) tightly grouped. Alignment should be predominantly left-justified to emphasize a straightforward, direct narrative.

## Elevation & Depth

To maintain a sense of stability and "absolute" truth, this design system rejects soft, ambient shadows. Instead, it utilizes **Bold Borders** and **Tonal Layers** to create depth. 

Surface tiers are created by layering Deep Charcoal elements over Pure White backgrounds. High-contrast outlines (2px solid #1A1A1A) are used for interactive containers, such as input fields and case cards, creating a "flat but layered" look. When an element needs to feel elevated (such as a modal or an urgent alert), it should use a hard, offset shadow—a solid block of color (often #1A1A1A at 100% opacity) shifted 4px to 8px down and right—rather than a blur.

## Shapes

The shape language of this design system is **Sharp (0px)**. Every element—from buttons to input fields to cards—utilizes hard 90-degree angles. This choice is intentional; it conveys a lack of compromise, a rigid adherence to the law, and a sense of institutional permanence. 

The only exception to the sharp rule is the use of circular icons or "pills" for status badges, which provides a visual "pop" against the otherwise rectangular grid, ensuring that urgent status updates are immediately identifiable.

## Components

### Buttons
Buttons are large, rectangular, and use the Primary Alert Red for "Primary" actions and Deep Charcoal for "Secondary" actions. They feature uppercase **Inter** labels with heavy weights. The hover state should involve a color inversion or a thick 4px black border to emphasize the "Courageous" style.

### Input Fields
Inputs must have a 2px solid #1A1A1A border. Upon focus, the border thickens to 3px or changes to Alert Red. Labels are always positioned above the field in **label-caps** to ensure the user knows exactly what data is being requested at all times.

### Case Cards
Cards are the primary way information is grouped. They feature a 2px charcoal border and a thick top-border (4px) in Alert Red if the case has an "Urgent" status. They use high-contrast text and no shadows.

### Status Chips
Status chips are the only rounded elements in the system (pill-shaped). They use high-contrast color fills (e.g., Red for "Urgent", Charcoal for "Closed", White with a border for "Pending") to provide immediate visual feedback on the state of a case.

### Legal Lists
Lists should be used for chronologies or evidence lockers. Each item is separated by a 1px charcoal divider. We use a "data-point" layout where the timestamp or legal code is in bold Inter on the left, with the description in Public Sans on the right.