---
name: Venture Stability
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
  on-surface-variant: '#414943'
  inverse-surface: '#303031'
  inverse-on-surface: '#f2f0f0'
  outline: '#717973'
  outline-variant: '#c1c8c2'
  surface-tint: '#3b6751'
  primary: '#001b0f'
  on-primary: '#ffffff'
  primary-container: '#013220'
  on-primary-container: '#6f9c84'
  inverse-primary: '#a2d1b7'
  secondary: '#5e5f5c'
  on-secondary: '#ffffff'
  secondary-container: '#e0e0dc'
  on-secondary-container: '#626360'
  tertiary: '#171717'
  on-tertiary: '#ffffff'
  tertiary-container: '#2b2b2b'
  on-tertiary-container: '#929292'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bdedd2'
  primary-fixed-dim: '#a2d1b7'
  on-primary-fixed: '#002113'
  on-primary-fixed-variant: '#234f3b'
  secondary-fixed: '#e3e2df'
  secondary-fixed-dim: '#c7c7c3'
  on-secondary-fixed: '#1b1c1a'
  on-secondary-fixed-variant: '#464744'
  tertiary-fixed: '#e2e2e2'
  tertiary-fixed-dim: '#c6c6c6'
  on-tertiary-fixed: '#1b1b1b'
  on-tertiary-fixed-variant: '#474747'
  background: '#fbf9f9'
  on-background: '#1b1c1c'
  surface-variant: '#e3e2e2'
typography:
  display-lg:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Manrope
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Manrope
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

This design system is built for the high-stakes world of D&O insurance, where perceived stability and professional authority are paramount. The aesthetic is "Modern Venture"—a fusion of traditional institutional trust and the agile, minimalist efficiency of modern tech startups. 

The brand personality is composed, elite, and unwavering. It evokes the feeling of a prestige law firm or a top-tier venture capital fund. The UI employs a High-Contrast Minimalist style, utilizing vast amounts of off-white "breathable" space to allow the deep forest green and sharp black elements to stand out as markers of importance and intentionality. There is no room for decorative fluff; every line and element serves a functional or structural purpose.

## Colors

The palette is anchored in "Stability" psychology. **Deep Forest Green (#013220)** serves as the primary brand anchor, representing growth, wealth, and conservative risk management. **Off-White (#FDFCF8)** is used as the primary canvas color to reduce eye strain and provide a more premium, "paper-like" feel than pure white. **Black (#000000)** is reserved for high-impact typography and structural borders.

Color application should follow a 60-30-10 distribution:
- **60% Off-White:** Backgrounds, large containers, and negative space.
- **30% Deep Forest Green:** Primary actions, navigation headers, and brand accents.
- **10% Black:** Headings, borders, and critical iconography.
- **Neutral Accents:** Soft greys are used exclusively for secondary text and disabled states to maintain the high-contrast integrity of the primary palette.

## Typography

This design system utilizes a dual-typeface strategy to balance tradition and modern clarity. 

**Newsreader** is the editorial choice for headings. Its sophisticated serif strokes convey the authority of a legal document or a financial journal. It should be used for all storytelling and high-level section titles.

**Manrope** is the utilitarian workhorse for body text, forms, and data. As a clean sans-serif with excellent legibility, it ensures that complex insurance terms and policy details are easily digestible. 

For maximum hierarchy, headlines should remain dark (Black or Deep Forest Green), while body text maintains a high-contrast black on off-white background.

## Layout & Spacing

The design system employs a **fixed grid** philosophy for desktop screens to maintain a controlled, editorial appearance. A 12-column grid is used with generous 24px gutters. 

Rhythm is established through an 8px base unit. To emphasize the minimalist aesthetic, excessive "white space" is encouraged—specifically, large vertical gaps (120px+) between major sections to allow the user to focus on one piece of information at a time. Content should be centered within a 1280px max-width container to prevent line lengths from becoming unreadable on ultra-wide monitors.

## Elevation & Depth

To maintain a professional and "flat" institutional feel, this design system avoids heavy drop shadows and faux-3D effects. Depth is conveyed through **Tonal Layers** and **Bold Borders**.

- **Level 0 (Floor):** The Off-White background.
- **Level 1 (Cards):** Defined not by shadows, but by 1px solid black or deep green borders. 
- **Level 2 (Modals/Popovers):** A very subtle, 15% opacity Deep Forest Green shadow with a wide blur (32px) can be used to indicate temporary overlays, though a simple high-contrast border is preferred.

Interactive elements do not "lift" on hover; instead, they change fill color or stroke weight, maintaining a tactile, grounded presence.

## Shapes

The design system uses a **Sharp (0)** roundedness profile. All buttons, input fields, cards, and containers feature 90-degree angles. This geometric rigidity reinforces the brand's themes of precision, legal structural integrity, and uncompromising professionalism. Circular shapes are reserved strictly for icons or radio buttons where convention dictates, but even then, a square-form factor is preferred for checkboxes.

## Components

### Buttons
- **Primary:** Solid Deep Forest Green background with Off-White text. No radius. High-contrast hover state (Black background).
- **Secondary:** Transparent background with a 1.5px Black border. 

### Input Fields
- **Style:** Underline-only or full-border sharp rectangles. 
- **Active State:** Border weight increases from 1px to 2px in Deep Forest Green.
- **Labels:** Small caps Manrope, placed above the field for maximum legibility.

### Cards
- White background with a thin Black border. No shadows. Header sections within cards are separated by a 1px horizontal rule.

### Chips & Tags
- Used for policy status (e.g., "Active", "Under Review"). Rectangular, with a light tint of the status color (e.g., pale green) and a dark border.

### Additional Components
- **Policy Progress Tracker:** A vertical, thin-line stepper using serif numbers (Newsreader) to guide users through the insurance application process.
- **Data Tables:** High-density, sans-serif tables with subtle horizontal stripes in a 5% opacity Green for readability.