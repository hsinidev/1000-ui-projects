---
name: Wildwood Ethos Desktop
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
  on-surface-variant: '#42493e'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#765934'
  on-secondary: '#ffffff'
  secondary-container: '#fed6a7'
  on-secondary-container: '#795b36'
  tertiary: '#3e3928'
  on-tertiary: '#ffffff'
  tertiary-container: '#56503d'
  on-tertiary-container: '#cbc2ab'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#ffddb6'
  secondary-fixed-dim: '#e6c093'
  on-secondary-fixed: '#2a1800'
  on-secondary-fixed-variant: '#5c421f'
  tertiary-fixed: '#ece2c9'
  tertiary-fixed-dim: '#cfc6ae'
  on-tertiary-fixed: '#201b0c'
  on-tertiary-fixed-variant: '#4c4634'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
typography:
  headline-xl:
    fontFamily: Epilogue
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Epilogue
    fontSize: 36px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Epilogue
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-md:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1440px
  gutter: 24px
  margin-page: 48px
  stack-sm: 16px
  stack-md: 32px
  stack-lg: 64px
---

## Brand & Style

This design system is built for the "Modern Naturalist" educator—individuals who require the reliability of a professional administrative tool but seek the warmth of an outdoor-inspired environment. The aesthetic moves away from cold, corporate SaaS and toward a **Tactile / Minimalist** hybrid. It emphasizes high-quality whitespace and organic forms that evoke the feeling of physical field journals and natural landscapes.

The design should feel:
- **Grounded:** Stable and reliable for complex administrative tasks.
- **Organic:** Avoiding rigid 90-degree corners in favor of soft, natural radii.
- **Adventurous:** Encouraging exploration through subtle textures and deep, forest-inspired tones.
- **Legible:** Optimized for long-form reading and data density required on desktop displays.

## Colors

The palette is derived from the forest floor and highland trails, optimized for desktop screens to ensure sufficient contrast and reduced eye strain.

- **Primary (Forest Green):** Used for main actions, navigation headers, and primary brand moments.
- **Secondary (Earthy Brown):** Reserved for accents, specialized categories, and secondary iconography.
- **Tertiary (Sand):** Serves as a soft alternative to white for container backgrounds and large structural blocks.
- **Neutral (Parchment):** The base canvas color, providing a warm, non-glare background for long-duration work.
- **Text:** The primary text uses a deep, near-black green to maintain harmony with the palette while ensuring AAA accessibility.

## Typography

Typography is balanced between the editorial character of **Epilogue** and the hyper-legibility of **Lexend**.

- **Headlines:** Epilogue provides a geometric yet distinctive feel, perfect for page titles and section headers. Use tight letter spacing for larger displays to maintain visual impact.
- **Body:** Lexend is chosen for its specific design to improve reading speed and comfort, which is essential for educators reviewing curriculum or student data.
- **Desktop Optimization:** Line heights are increased to 1.6 for body text to ensure readability across wide desktop containers.

## Layout & Spacing

This design system utilizes a **Fixed Grid** approach for content-heavy pages and a **Fluid Sidebar** model for administrative dashboards.

- **Grid:** A 12-column grid with a 1440px max-width container ensures content remains readable without excessive line lengths.
- **Rhythm:** An 8px base unit drives all spacing decisions.
- **Margins:** Generous page margins (48px) create a sense of calm and "room to breathe," reflecting the openness of the wild.
- **Data Density:** While the overall feel is spacious, administrative tables should use condensed vertical padding (8px–12px) to allow for efficient data scanning.

## Elevation & Depth

Depth is achieved through **Tonal Layering** rather than traditional drop shadows, maintaining a flat but tactile "paper-on-wood" aesthetic.

- **Level 0 (Canvas):** The base background using the Neutral parchment color.
- **Level 1 (Cards):** Tertiary Sand color with a subtle 1px stroke in a slightly darker earth tone. No shadow.
- **Level 2 (Modals/Overlays):** These use "Ambient Shadows"—extremely soft, low-opacity (#2D5A27 at 8% opacity) blurs that feel like a natural shadow cast by sunlight.
- **Interactive States:** High-priority elements use a slight "lift" (move -2px on Y-axis) rather than heavy color changes to indicate hoverability.

## Shapes

The shape language is strictly **Rounded**. Sharp corners are avoided to maintain the organic, approachable personality of the brand.

- **Base Radius (8px):** Used for input fields and small buttons.
- **Large Radius (16px):** Used for cards, content containers, and image masks.
- **Extra Large Radius (24px):** Used for featured "Hero" sections or decorative background elements.
- **Icons:** Should feature rounded terminals and soft joints to match the UI's curvature.

## Components

- **Buttons:** Primary buttons use the Forest Green background with white Lexend text. They should feel substantial with 16px horizontal padding. Secondary buttons use a 2px stroke of Forest Green with a transparent background.
- **Cards:** Cards are the primary organizational unit. They should have a 1px "Earthy Brown" border at 10% opacity and a 16px corner radius.
- **Input Fields:** Use a subtle "Sand" fill with a bottom-only border that transforms into a full 2px Forest Green border on focus.
- **Chips/Tags:** Used for categorization (e.g., "K-5", "Outdoor", "Science"). These use a pill-shape (radius 100px) and the Tertiary color palette.
- **Navigation:** The desktop sidebar should be persistent, using the Forest Green as a background with high-contrast Sand icons and text.
- **Progress Indicators:** Use a thick, 8px rounded bar in Forest Green against a Sand background, resembling a physical trail marker.