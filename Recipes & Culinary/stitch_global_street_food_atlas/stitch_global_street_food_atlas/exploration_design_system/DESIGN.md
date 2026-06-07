---
name: Exploration Design System
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#5a4138'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#8f7066'
  outline-variant: '#e3bfb2'
  surface-tint: '#a83900'
  primary: '#a43700'
  on-primary: '#ffffff'
  primary-container: '#cd4700'
  on-primary-container: '#fffbff'
  inverse-primary: '#ffb59a'
  secondary: '#29695b'
  on-secondary: '#ffffff'
  secondary-container: '#acedda'
  on-secondary-container: '#2e6d5f'
  tertiary: '#914723'
  on-tertiary: '#ffffff'
  tertiary-container: '#b05e38'
  on-tertiary-container: '#fffbff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59a'
  on-primary-fixed: '#380d00'
  on-primary-fixed-variant: '#802a00'
  secondary-fixed: '#afefdd'
  secondary-fixed-dim: '#94d3c1'
  on-secondary-fixed: '#00201a'
  on-secondary-fixed-variant: '#065043'
  tertiary-fixed: '#ffdbcd'
  tertiary-fixed-dim: '#ffb596'
  on-tertiary-fixed: '#360f00'
  on-tertiary-fixed-variant: '#76320f'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
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
    lineHeight: '1.6'
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
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin-edge: 32px
  stack-sm: 16px
  stack-md: 40px
  stack-lg: 80px
---

## Brand & Style

This design system is built to evoke the visceral experience of a well-traveled field journal. The brand personality is **adventurous, authentic, and immersive**, prioritizing high-impact photography and street-level storytelling. 

The visual style is **Tactile Minimalism**. It combines the structured efficiency of modern digital grids with the "rugged" physical characteristics of travel ephemera. By layering subtle paper grain textures and topographic line patterns over a clean, spacious layout, the system creates a sense of place and permanence. The UI acts as a refined frame for vibrant, saturated street food and landscape photography, ensuring the interface feels like an organic extension of the journey rather than a digital barrier.

## Colors

The color palette is grounded in an earthy, sun-baked aesthetic designed to complement diverse food cultures and global landscapes.

- **Primary (Spiced Orange):** Used for primary actions and energetic highlights. It reflects the heat and spice of street food markets.
- **Secondary (Deep Teal):** Provides a cool, sophisticated contrast, used for navigation, footer backgrounds, and grounding elements.
- **Tertiary (Earthy Terracotta):** Reserved for subtle accents, category tags, and secondary decorative elements.
- **Neutral (Warm White):** The "Paper" base. A non-pure white (#F9F7F2) that reduces eye strain and makes the vibrant colors of photography feel more integrated.
- **High-Vibrancy Accents:** A saturated vermillion used sparingly for critical calls-to-action or "Live" indicators to maintain a sense of urgency and excitement.

## Typography

The typographic hierarchy establishes an editorial, "journalistic" tone. 

**Noto Serif** is utilized for all headlines to provide a bold, adventurous, and literary feel. Its classic proportions suggest authority and history. For the best "Exploration" effect, use the `headline-xl` for article titles with tighter letter spacing to create a high-impact, magazine-style header.

**Inter** handles all functional and long-form reading tasks. Its neutral, systematic design ensures legibility across dense directories and ingredient lists. All labels and metadata (dates, locations, tags) should use `label-sm` with increased letter-spacing and uppercase styling to mimic the look of stamped passport entries or technical field notes.

## Layout & Spacing

This design system utilizes a **fixed-grid** model for desktop and tablet to maintain an intentional, editorial structure. 

- **Grid:** A 12-column layout with 24px gutters. Content should be centered with a maximum width of 1280px to prevent line lengths from becoming unreadable.
- **Rhythm:** A 8px base unit drives all spacing. 
- **White Space:** Large vertical gaps (`stack-lg`) are used between major sections to allow the user to "breathe" between different destinations or food stories.
- **Photography:** Images should frequently "break" the grid—either spanning the full width of the screen or offsetting slightly—to create a dynamic, immersive flow that feels less like a template and more like a curated scrapbook.

## Elevation & Depth

Depth in this design system is achieved through **Tonal Layering** and **Materiality** rather than traditional shadows.

- **Stacking:** Elements are layered like physical papers. Lower levels use the base Neutral (Warm White), while interactive elements or "cards" may have a slightly lighter or subtly textured background.
- **Textures:** A low-opacity (2-3%) paper grain overlay is applied globally to the background. Subtle topographic line patterns (Deep Teal at 5% opacity) are used in the background of headers or as section dividers to imply geographic depth.
- **Borders:** Instead of shadows, use 1px "Earthy Terracotta" borders at 15% opacity to define card boundaries. This maintains a flat, rugged aesthetic while providing necessary hit-area cues.
- **Glassmorphism:** Reserved exclusively for mobile navigation bars or "floating" image captions, using a heavy backdrop blur to keep the focus on the underlying photography.

## Shapes

The shape language is **grounded and structured**. A `Soft (1)` roundedness level (0.25rem) is used for buttons, input fields, and tags. This slight rounding prevents the UI from feeling "sharp" or hostile, while remaining much more professional and "rugged" than a fully rounded or pill-shaped system.

Large-scale containers, such as hero images and primary content cards, should maintain sharp corners (`0px`) to reinforce the clean, modern grid and the feel of printed photographs.

## Components

- **Buttons:** Primary buttons use a solid "Spiced Orange" fill with "Warm White" text. They should have a subtle inner-bevel or a 1px darker bottom border to feel "pressed" or tactile.
- **Chips/Tags:** Use the "Deep Teal" or "Terracotta" at low opacities (10%) for the background with full-opacity text. These should look like small, stamped labels.
- **Cards:** Content cards for blog posts or food stalls should feature a full-bleed image at the top. The text area below uses the "Warm White" neutral with no heavy shadow, relying on the 1px soft border for definition.
- **Input Fields:** Minimalist design with a bottom-border only, mimicking a lined notebook. Focus states transition the border to "Spiced Orange."
- **Topographic Dividers:** A unique component consisting of a thin horizontal line interrupted by a small topographic map icon or location coordinates, used to separate major narrative beats.
- **Immersive Galleries:** Use a "polaroid" style framing for certain street food sections, with slightly thicker bottom margins for captions in the `label-sm` style.