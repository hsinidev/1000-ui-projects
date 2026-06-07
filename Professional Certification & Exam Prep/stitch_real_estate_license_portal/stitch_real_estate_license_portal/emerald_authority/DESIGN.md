---
name: Emerald Authority
colors:
  surface: '#f8f9ff'
  surface-dim: '#d0dbed'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e6eeff'
  surface-container-high: '#dee9fc'
  surface-container-highest: '#d9e3f6'
  on-surface: '#121c2a'
  on-surface-variant: '#3f4944'
  inverse-surface: '#27313f'
  inverse-on-surface: '#eaf1ff'
  outline: '#6f7973'
  outline-variant: '#bec9c2'
  surface-tint: '#1b6b51'
  primary: '#004532'
  on-primary: '#ffffff'
  primary-container: '#065f46'
  on-primary-container: '#8bd6b7'
  inverse-primary: '#8bd6b6'
  secondary: '#7b5800'
  on-secondary: '#ffffff'
  secondary-container: '#fdc34d'
  on-secondary-container: '#715000'
  tertiary: '#652925'
  on-tertiary: '#ffffff'
  tertiary-container: '#823f3a'
  on-tertiary-container: '#ffb4ad'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#a6f2d1'
  primary-fixed-dim: '#8bd6b6'
  on-primary-fixed: '#002116'
  on-primary-fixed-variant: '#00513b'
  secondary-fixed: '#ffdea6'
  secondary-fixed-dim: '#f7bd48'
  on-secondary-fixed: '#271900'
  on-secondary-fixed-variant: '#5d4200'
  tertiary-fixed: '#ffdad6'
  tertiary-fixed-dim: '#ffb3ac'
  on-tertiary-fixed: '#3b0908'
  on-tertiary-fixed-variant: '#73332f'
  background: '#f8f9ff'
  on-background: '#121c2a'
  surface-variant: '#d9e3f6'
typography:
  h1:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Newsreader
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
  h3:
    fontFamily: Newsreader
    fontSize: 28px
    fontWeight: '500'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Public Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Public Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  data-mono:
    fontFamily: Public Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
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
  gutter: 24px
  margin: 32px
  max_width: 1280px
---

## Brand & Style

The brand personality of this design system is rooted in professional advancement, institutional trust, and academic excellence. It serves an audience of aspiring and established real estate professionals who require a platform that feels as official as a government portal but as intuitive as modern financial software. The visual language conveys a sense of achievement and prestige, ensuring users feel they are making a high-value investment in their careers.

The chosen style is **Corporate / Modern** with a focus on **High-Contrast** elements. It utilizes structured layouts and "clean-room" aesthetics to maximize focus on educational content and certification data. By combining traditional serif flourishes with a rigorous grid, the design system strikes a balance between the historic gravitas of real estate law and the cutting-edge efficiency of digital learning.

## Colors

The palette is centered on "Emerald Excellence" and "Institutional Gold." The Emerald Green serves as the primary driver for navigation, primary actions, and branding, symbolizing growth and stability. Gold is used sparingly as a high-prestige accent for rewards, certifications, and highlights, ensuring it retains its value without cluttering the UI.

White is the foundational background color to ensure maximum readability and a "clean" commercial feel. Neutrals are leaning toward a cool Slate to provide high-contrast legibility for body text and data points. Success and warning states are tonally aligned with the emerald primary to maintain a cohesive visual experience.

## Typography

This design system employs a sophisticated dual-type approach. **Newsreader** is used for headings to evoke the traditional authority of legal documents and academic journals. Its serif structure provides a rhythmic, literary quality that signals high-value information.

For data-heavy interfaces, course modules, and interactive elements, **Public Sans** is utilized. As an institutional-grade typeface, it offers exceptional clarity and neutrality. Use bold weights of Public Sans for "Data Cards" and status labels to ensure information is scannable at a glance. All body text should maintain a generous line height to reduce cognitive load during long study sessions.

## Layout & Spacing

The layout utilizes a **Fixed Grid** model to maintain a sense of order and institutional rigor. The primary container is capped at 1280px to prevent line lengths from becoming unreadable on ultra-wide displays. A 12-column grid is the standard for dashboards, while a centered 8-column layout is preferred for reading-intensive course content.

Spacing follows a strict 8px rhythmic scale. Content density should remain "Medium" to allow for significant whitespace between distinct data modules, reinforcing the "clean" aesthetic and ensuring that high-contrast cards have room to breathe.

## Elevation & Depth

This design system avoids heavy shadows in favor of **Low-Contrast Outlines** and **Tonal Layers**. Hierarchy is established through subtle shifts in background gray levels and crisp 1px borders.

1.  **Level 0 (Surface):** Pure white (#FFFFFF) for the main canvas.
2.  **Level 1 (Sections):** Lightest gray (#F9FAFB) for grouping content areas or sidebars.
3.  **Level 2 (Cards):** White background with a 1px border (#E5E7EB).
4.  **Interactive Hover:** Use a specialized "Gold Glow"—a very soft, low-opacity shadow (#B8860B at 10%)—to indicate focus on primary interactive cards or buttons.

Depth is used to signify "Importance" rather than "Distance," with key certification status cards receiving a slightly thicker left-hand border in Emerald or Gold.

## Shapes

The shape language is **Soft (Level 1)**. This subtle rounding (4px for small elements, 8px for cards) softens the corporate edges without appearing overly casual or "app-like." It maintains a professional, architectural feel consistent with the real estate industry. 

Buttons use the 4px radius to feel precise, while larger dashboard containers and data cards use the 8px radius to create a distinct frame for educational content. Icons should follow a "linear" style with consistent 2px stroke weights and slightly rounded terminals to match the UI.

## Components

### Buttons
Primary buttons are solid Emerald Green with white text, utilizing a "heavy" weight for the label. Secondary buttons use a 1px Emerald border with a transparent background. Gold is reserved exclusively for "Call to Action" buttons that lead to purchase or certification claims.

### Data Cards
Data cards are the cornerstone of the system. They must feature a high-contrast white background, a light gray border, and a "Title Bar" that uses the Emerald primary color or a Gold accent for specific milestones. Content inside should be strictly aligned to the 8px grid.

### Input Fields
Inputs are minimalist: a 1px border that turns Emerald on focus. Labels use "Public Sans" in a bold, smaller size (label-caps) placed above the field for maximum accessibility.

### Progress Indicators
Educational progress is tracked via slim, high-contrast bars. The track is a light neutral, while the progress fill is Emerald Green. When a course is 100% complete, the bar transitions to Gold.

### Certification Badges
Specialized components designed to look like official seals. They utilize the Gold secondary color and serif typography to represent successfully earned licenses or credits.