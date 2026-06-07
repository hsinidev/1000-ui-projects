---
name: Kinetic Authority
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#45464d'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#76777d'
  outline-variant: '#c6c6cd'
  surface-tint: '#565e74'
  primary: '#000000'
  on-primary: '#ffffff'
  primary-container: '#131b2e'
  on-primary-container: '#7c839b'
  inverse-primary: '#bec6e0'
  secondary: '#bb0112'
  on-secondary: '#ffffff'
  secondary-container: '#e02928'
  on-secondary-container: '#fffbff'
  tertiary: '#000000'
  on-tertiary: '#ffffff'
  tertiary-container: '#0d1c2f'
  on-tertiary-container: '#76859b'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dae2fd'
  primary-fixed-dim: '#bec6e0'
  on-primary-fixed: '#131b2e'
  on-primary-fixed-variant: '#3f465c'
  secondary-fixed: '#ffdad6'
  secondary-fixed-dim: '#ffb4ab'
  on-secondary-fixed: '#410002'
  on-secondary-fixed-variant: '#93000b'
  tertiary-fixed: '#d5e3fd'
  tertiary-fixed-dim: '#b9c7e0'
  on-tertiary-fixed: '#0d1c2f'
  on-tertiary-fixed-variant: '#3a485c'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display-xl:
    fontFamily: Public Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Public Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Public Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 48px
  gutter: 20px
  margin: 24px
  masonry_gap: 16px
---

## Brand & Style

The design system is engineered for a high-velocity news environment where speed and credibility are paramount. It adopts a **Corporate Modern** style with leanings toward **Minimalism** to ensure the content remains the focal point. The aesthetic is "Newspaper 2.0"—stripping away the bulk of traditional media while retaining the structural authority of print.

The interface evokes a sense of urgency through sharp transitions and high-contrast accents, balanced by a sophisticated, stable foundation. It targets a globally-minded audience that values efficiency, clarity, and factual integrity. Every element is designed to minimize cognitive load, allowing users to scan, digest, and move through information rapidly.

## Colors

The palette is anchored by **Deep Navy (Slate 900)** to establish institutional trust and "Signal Red" for high-priority alerts.

- **Primary:** Deep Navy (#0F172A) is used for headers, primary navigation, and dominant branding elements.
- **Secondary (Breaking):** Signal Red (#DC2626) is reserved exclusively for "Breaking News" banners, live indicators, and critical updates.
- **Neutral Foundation:** A sophisticated range of Slates and Grays. In light mode, #F8FAFC provides a clean backdrop; in dark mode, the surface shifts to a deep #020617.
- **Support Colors:** Success (Emerald), Info (Blue), and Warning (Amber) are used sparingly for utility functions like "Saved" states or notification badges.

## Typography

This design system utilizes a dual-sans-serif approach to maximize legibility and hierarchy.

- **Headlines:** **Public Sans** provides a sturdy, institutional feel. Heavy weights (Bold/ExtraBold) and tight letter-spacing are used for news titles to create high visual impact.
- **Body Text:** **Work Sans** is chosen for its optimized screen readability at varied sizes, ensuring long-form articles remain comfortable to read.
- **Interface Labels:** **Inter** is used for utility elements, timestamps, and metadata (e.g., "Time-to-Read") due to its neutral, functional character.

Hierarchy is enforced through strict vertical rhythm and clear weight differentiation between the news source and the story content.

## Layout & Spacing

The layout utilizes a **Flexible Modular Masonry System**. Content blocks are organized based on priority rather than a rigid vertical list, allowing for a dynamic front page that accommodates different media aspect ratios (16:9, 4:3, 1:1).

- **Grid:** A 12-column desktop grid that collapses to 4 columns on mobile. 
- **Density:** Spacing is tight (4px/8px increments) to maximize information density, typical of high-traffic news portals. 
- **Rhythm:** White space is used strategically as a separator between different "beats" of news (e.g., Politics vs. Tech) rather than between individual headlines.
- **Masonry logic:** Cards can span 1, 2, or 3 columns depending on the importance of the story.

## Elevation & Depth

This design system minimizes the use of shadows to maintain a "fast" and "flat" feel. Depth is communicated through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surface Tiers:** Backgrounds use the base neutral color, while article cards in the masonry grid use a slightly elevated white or light-gray surface.
- **Borders:** Subtle 1px borders in `slate-200` (light mode) or `slate-800` (dark mode) define content boundaries without adding visual weight.
- **Interaction:** On hover, article cards may use a very soft, diffused ambient shadow (4% opacity) or a slight background tint change to indicate interactivity.
- **Banners:** The persistent breaking news banner is pinned to the top of the viewport with a high-contrast background and 0 elevation, acting as a structural anchor.

## Shapes

The shape language is **Soft (0.25rem)**. This slight rounding takes the edge off the high-density layout, making the platform feel modern and accessible without losing its authoritative, professional character.

- **Cards & Inputs:** Use the base 4px (0.25rem) radius.
- **Buttons:** Primary call-to-actions follow the base radius.
- **Chips/Badges:** Metadata tags (like category labels) use a slightly higher radius (rounded-lg) to distinguish them from structural elements.
- **Images:** Media within the masonry grid must follow the 4px corner radius to maintain a cohesive "tile" appearance.

## Components

The components are optimized for utility and recognition speed.

- **Breaking News Banner:** Persistent, full-width, Signal Red background. Features an auto-scrolling headline ticker or a single high-priority alert.
- **Article Cards:** Contain a headline, a "Save for Later" (bookmark icon) in the top right, a "Time-to-Read" indicator (e.g., "5 min read") at the bottom, and a high-resolution thumbnail.
- **Save for Later:** A toggle icon (Outline to Solid) that uses the Primary Navy color when active.
- **Reading Progress Bar:** A thin 2px Signal Red line at the top of the viewport that fills as the user scrolls through an article.
- **Metadata Chips:** Small, low-contrast capsules used for categorizing content (e.g., #WorldNews, #Tech).
- **Buttons:** High-contrast for primary actions (Subscribe), ghost-style for secondary actions (Share, More).
- **Input Fields:** Minimalist design with clear focus states using a 2px Deep Navy bottom border or subtle outline.