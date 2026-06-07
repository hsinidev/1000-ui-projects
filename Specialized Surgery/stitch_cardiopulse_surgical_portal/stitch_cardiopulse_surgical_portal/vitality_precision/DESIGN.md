---
name: Vitality & Precision
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#5b403d'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#906f6c'
  outline-variant: '#e4beb9'
  surface-tint: '#bb171b'
  primary: '#7c0009'
  on-primary: '#ffffff'
  primary-container: '#a80010'
  on-primary-container: '#ffb2a9'
  inverse-primary: '#ffb4ab'
  secondary: '#515f74'
  on-secondary: '#ffffff'
  secondary-container: '#d5e3fc'
  on-secondary-container: '#57657a'
  tertiary: '#303b4e'
  on-tertiary: '#ffffff'
  tertiary-container: '#475266'
  on-tertiary-container: '#bac5dd'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad6'
  primary-fixed-dim: '#ffb4ab'
  on-primary-fixed: '#410002'
  on-primary-fixed-variant: '#93000c'
  secondary-fixed: '#d5e3fc'
  secondary-fixed-dim: '#b9c7df'
  on-secondary-fixed: '#0d1c2e'
  on-secondary-fixed-variant: '#3a485b'
  tertiary-fixed: '#d8e3fb'
  tertiary-fixed-dim: '#bcc7de'
  on-tertiary-fixed: '#111c2d'
  on-tertiary-fixed-variant: '#3c475a'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  display:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h1:
    fontFamily: Public Sans
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
  h2:
    fontFamily: Public Sans
    fontSize: 30px
    fontWeight: '600'
    lineHeight: '1.3'
  h3:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  emergency-label:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '800'
    lineHeight: '1.0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1280px
  gutter: 24px
---

## Brand & Style

This design system is built upon the pillars of **Clinical Authority** and **Patient Reassurance**. Designed specifically for a high-stakes cardiovascular and thoracic surgical environment, the aesthetic prioritizes clarity, structural integrity, and emotional stability.

The style is **Corporate Modern**, leaning into institutional weight and surgical precision. It avoids unnecessary decorative elements, favoring heavy whitespace to allow complex medical information to breathe. The emotional response is one of absolute trust; the user should feel they are in the hands of world-class experts. Visuals are grounded, using high-quality medical illustrations that are informative rather than clinical or graphic, bridging the gap between technical excellence and human empathy.

## Colors

The palette is anchored by **Deep Crimson**, a color representing both the vitality of the heart and the critical nature of the surgical profession. It is used intentionally for primary actions and emergency indicators. 

**Slate** serves as the professional bedrock, used for typography, iconography, and structural borders to provide a neutral, calming contrast to the intensity of the crimson. **Pure White** is the dominant background color, ensuring a "sterile" and clean medical environment that maximizes legibility. 

- **Primary (Deep Crimson):** Used for CTA buttons, active states, and critical health markers.
- **Secondary (Slate):** Used for secondary navigation, subheaders, and body text.
- **Neutral (Pure White):** Used for global backgrounds and card surfaces.
- **Surface (Slate 50):** Used for subtle section nesting and table headers.

## Typography

This design system utilizes a dual-sans-serif approach to balance institutional authority with technical readability. 

**Public Sans** is the primary choice for headlines and labels. Its institutional, government-grade clarity communicates stability and official status. It should be set with tighter tracking in headlines to appear more authoritative.

**Inter** is used for all body copy and technical data. Its systematic, neutral design ensures that patient reports, surgical descriptions, and instructional content are highly legible even at smaller scales or in dense data tables. High line-heights (1.6x) are mandated for body text to reduce cognitive load for patients under stress.

## Layout & Spacing

The layout follows a **Fixed Grid** philosophy to maintain a sense of structured order and "published" authority. A 12-column grid is used for desktop views with generous 48px margins to ensure the content feels premium and focused.

Spacing follows a strict 8px linear scale. Large vertical rhythms (48px to 80px) are used to separate major surgical categories, while tighter spacing (12px to 24px) is reserved for related medical data within cards. The layout must prioritize the 'Help & Emergency' sticky header, which remains anchored to the top of the viewport at all times, independent of page scroll.

## Elevation & Depth

To maintain a clean, surgical feel, this design system avoids heavy, diffused shadows. Depth is communicated through **Low-Contrast Outlines** and **Tonal Layers**.

- **Surface Tiers:** Primary content sits on Pure White. Secondary information or sidebars sit on a very light Slate-50 background.
- **Borders:** Instead of shadows, elements like cards and input fields use 1px solid borders in Slate-200.
- **Emergency Elevation:** The 'Help & Emergency' header is the only element allowed a subtle, high-opacity "sharp" shadow (Slate-900 at 10% opacity, 4px offset) to signify its life-saving priority over the rest of the interface.

## Shapes

The shape language of this design system is **Soft** but disciplined. 0.25rem (4px) corner radii are applied to buttons, cards, and input fields. This slight rounding removes the "aggression" of sharp corners—making the system feel more human and accessible—while maintaining the rectangular rigor expected of a professional medical institution. 

Interactive elements like "Emergency" buttons may use a slightly higher radius (rounded-lg) to distinguish them as high-touch areas, but never a full pill shape, which would appear too casual for a surgical group.

## Components

### Help & Emergency Sticky Header
The most critical component. It is a full-width bar anchored to the top of the browser. It features a Deep Crimson background with Pure White typography. It must contain a "Call 911" or "Emergency Line" shortcut and a "Symptoms Checker" button. This component should have a higher z-index than all other UI elements.

### Buttons
- **Primary CTA:** Deep Crimson background with white text. Square-ish (4px radius), bold Public Sans labels. Use for "Schedule Consultation" or "View Surgeon Profile."
- **Secondary:** Transparent background with a 2px Slate-500 border. Use for less critical navigational paths.

### Medical Illustration Containers
Illustrations should be contained within Slate-50 rounded frames. They should use a "Blueprint" or "Fine-Line" style—minimalist line art with Deep Crimson accents—to explain complex procedures without being visually overwhelming.

### Information Cards
Cards utilize a 1px Slate border with no shadow. Headers within cards should use a Slate-50 background tint to create clear separation between the title and the technical data below.

### Status Indicators
Use a small, pulsating Deep Crimson dot for "Live" or "Urgent" status updates on patient portals to maintain the "Vitality" theme of the brand.