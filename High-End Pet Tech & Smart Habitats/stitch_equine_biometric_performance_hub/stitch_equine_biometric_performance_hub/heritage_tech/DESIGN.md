---
name: Heritage Tech
colors:
  surface: '#fcf9f2'
  surface-dim: '#dcdad3'
  surface-bright: '#fcf9f2'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3ec'
  surface-container: '#f0eee7'
  surface-container-high: '#ebe8e1'
  surface-container-highest: '#e5e2db'
  on-surface: '#1c1c18'
  on-surface-variant: '#404942'
  inverse-surface: '#31312c'
  inverse-on-surface: '#f3f0ea'
  outline: '#717971'
  outline-variant: '#c0c9c0'
  surface-tint: '#316948'
  primary: '#002a15'
  on-primary: '#ffffff'
  primary-container: '#004225'
  on-primary-container: '#75af89'
  inverse-primary: '#98d4ac'
  secondary: '#7c5639'
  on-secondary: '#ffffff'
  secondary-container: '#fecaa5'
  on-secondary-container: '#795336'
  tertiary: '#16252f'
  on-tertiary: '#ffffff'
  tertiary-container: '#2c3b45'
  on-tertiary-container: '#95a5b1'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b4f0c7'
  primary-fixed-dim: '#98d4ac'
  on-primary-fixed: '#002110'
  on-primary-fixed-variant: '#165132'
  secondary-fixed: '#ffdcc4'
  secondary-fixed-dim: '#efbc98'
  on-secondary-fixed: '#2f1501'
  on-secondary-fixed-variant: '#613f24'
  tertiary-fixed: '#d5e5f1'
  tertiary-fixed-dim: '#b9c9d5'
  on-tertiary-fixed: '#0e1d26'
  on-tertiary-fixed-variant: '#3a4953'
  background: '#fcf9f2'
  on-background: '#1c1c18'
  surface-variant: '#e5e2db'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: IBM Plex Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: IBM Plex Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-tabular:
    fontFamily: IBM Plex Sans
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-caps:
    fontFamily: IBM Plex Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.08em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1440px
  gutter: 24px
  margin-page: 48px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is defined by "Heritage Tech"—a synthesis of traditional equestrian excellence and cutting-edge biometric precision. It targets a high-stakes audience of professional trainers, veterinarians, and elite owners who demand the reliability of a custom saddle and the analytical depth of a laboratory.

The visual language balances the tactile warmth of luxury stables with the clinical sharpness of performance data. The UI should evoke an emotional response of "Quiet Authority," avoiding flashy animations in favor of deliberate, meaningful transitions. Subtle grain textures and micro-patterns reminiscent of high-grade leather provide a sense of durability and craftsmanship, while thin, precise lines and high-contrast typography signal technological sophistication.

## Colors

The palette is rooted in the tradition of the turf and the tack room. 
- **Deep Racing Green (#004225)**: The primary anchor, used for headers, key navigation, and primary actions. It represents stability and prestige.
- **Rich Tan Leather (#A67B5B)**: Used as an accent color for focus states, highlights, and secondary interactive elements. It provides a human, tactile warmth.
- **Charcoal (#36454F)**: The technical foundation, utilized for secondary text, data visualization axes, and iconography to maintain high readability.
- **Off-white Ivory (#FCF9F2)**: The primary canvas. It softens the interface compared to a stark pure white, enhancing the "heritage" feel while reducing eye strain during long analytical sessions.

Data visualizations should utilize a supporting palette of "muted alerts"—softened reds and ambers that maintain the sophisticated aesthetic even during critical status reporting.

## Typography

Typography in this design system follows a strict hierarchy of "The Editorial Headline" versus "The Industrial Data."

**Playfair Display** is reserved for high-level headings, page titles, and empty-state messaging. Its high-contrast strokes and elegant serifs communicate luxury and tradition.

**IBM Plex Sans** is the workhorse for all functional elements. It was chosen for its exceptional legibility in dense data environments and its slightly technical, engineered feel. Use the "data-tabular" variant for biometric readouts to ensure vertical alignment of numbers. "Label-caps" should be used for small metadata and secondary navigation links to provide a crisp, organized structure.

## Layout & Spacing

This design system utilizes a **fixed grid** approach for desktop dashboards to ensure data visualization remains predictable and precise. Content is housed within a 1440px max-width container using a 12-column grid.

The spacing rhythm is based on an 8px base unit. Generous margins (48px) are used to create "breathing room," reinforcing the premium nature of the product. Information density is managed through distinct "data blocks"—modular components that use 24px gutters to prevent the UI from feeling cluttered despite high amounts of biometric information.

## Elevation & Depth

Depth is achieved through **tonal layers** and **low-contrast outlines** rather than heavy shadows. 

1.  **The Base Layer**: Ivory (#FCF9F2) serves as the background.
2.  **The Content Layer**: White (#FFFFFF) surfaces are used for cards and data modules, featuring a 1px border in a very light tint of Charcoal (#36454F at 10% opacity).
3.  **The Interaction Layer**: When an element is lifted or active, a subtle, diffused "Amber-Tinted Shadow" is used—incorporating the Tan Leather hue into the shadow's hex to create a warm, organic lift.

Backdrop blurs are used sparingly, specifically for mobile navigation overlays and modal backdrops, to maintain a sense of environmental depth without sacrificing the "heritage" aesthetic.

## Shapes

The shape language is "Soft-Technical." Elements use a subtle **0.25rem (4px)** radius for standard components, which provides just enough softness to feel sophisticated while maintaining the sharp, precise lines expected in a professional biometric tool.

- **Standard Buttons/Inputs**: 4px radius.
- **Data Cards**: 8px (rounded-lg) for a more defined modular look.
- **Charts/Graphs**: Sharp corners on the inner data elements, but housed in containers with the standard 4px radius.

## Components

### Buttons
Primary buttons use the Deep Racing Green background with Off-white text. They feature a subtle "grain" overlay to mimic leather texture. Secondary buttons use a Charcoal border with no fill. Interaction states (hover) should transition the border/text to Tan Leather.

### Data Cards
The core of the system. Cards feature a 1px stroke (#36454F at 10%) and a header section utilizing the Serif font. The body of the card uses the Sans-serif for biometric data.

### Inputs & Selects
Inputs use a "Classic Ledger" style—bottom borders only or very light four-sided borders. The focus state is a 2px bottom-border in Tan Leather.

### Biometric Gauges
Custom visualizations representing horse vitals (heart rate, gait symmetry, recovery). These use thin-stroke circular indicators with "Leather Tan" as the active progress color.

### Chips & Badges
Used for horse status (e.g., "Active," "Recovering," "Stabled"). These are rectangular with the standard 4px radius, using low-saturation background tints and high-contrast text in the Sans-serif label-caps style.

### Professional Features
- **Timeline Scrubber**: A horizontal element for reviewing biometric history, using a "saddle-stitch" dashed line aesthetic.
- **Report Generator**: A specific component for exporting "Pedigree Performance" PDFs, emphasizing the Serif typography for an authoritative, printed-document feel.