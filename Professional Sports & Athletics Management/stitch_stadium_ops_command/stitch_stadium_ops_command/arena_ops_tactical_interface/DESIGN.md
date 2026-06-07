---
name: Arena-Ops Tactical Interface
colors:
  surface: '#1d100a'
  surface-dim: '#1d100a'
  surface-bright: '#46362e'
  surface-container-lowest: '#170b06'
  surface-container-low: '#261812'
  surface-container: '#2b1c16'
  surface-container-high: '#362720'
  surface-container-highest: '#41312a'
  on-surface: '#f8ddd2'
  on-surface-variant: '#e2bfb0'
  inverse-surface: '#f8ddd2'
  inverse-on-surface: '#3d2d26'
  outline: '#a98a7d'
  outline-variant: '#5a4136'
  surface-tint: '#ffb693'
  primary: '#ffb693'
  on-primary: '#561f00'
  primary-container: '#ff6b00'
  on-primary-container: '#572000'
  inverse-primary: '#a04100'
  secondary: '#c0c6db'
  on-secondary: '#293041'
  secondary-container: '#42495a'
  on-secondary-container: '#b2b8cd'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#9a9999'
  on-tertiary-container: '#313131'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#ffdbcc'
  primary-fixed-dim: '#ffb693'
  on-primary-fixed: '#351000'
  on-primary-fixed-variant: '#7a3000'
  secondary-fixed: '#dce2f8'
  secondary-fixed-dim: '#c0c6db'
  on-secondary-fixed: '#151b2b'
  on-secondary-fixed-variant: '#404758'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#1d100a'
  on-background: '#f8ddd2'
  surface-variant: '#41312a'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.5'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1'
    letterSpacing: -0.01em
spacing:
  unit: 4px
  gutter: 16px
  margin-page: 32px
  container-padding: 20px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 24px
---

## Brand & Style
The design system is engineered for high-stakes stadium operations, where split-second decision-making and situational awareness are paramount. The brand personality is authoritative, precise, and resilient—evoking the feeling of a modern mission control center.

The style is a fusion of **Industrial Brutalism** and **High-Contrast Data Density**. It prioritizes utility over decoration, utilizing a "Glass-and-Steel" aesthetic that feels heavy and grounded yet digitally advanced. The UI must feel like a performance tool rather than a consumer application, employing rigid structures, clear information hierarchies, and aggressive visual cues for critical status changes.

## Colors
This design system utilizes a "Deep-Sea" dark mode palette to reduce eye strain during long shifts while ensuring accent colors "pop" with extreme vibrancy. 

- **Midnight Blue (#0B1221):** The primary canvas color, used for large structural areas.
- **Safety Orange (#FF6B00):** The primary action and branding color, reserved for interactive elements and high-priority states.
- **Graphite (#2D2D2D):** Used for secondary containers, borders, and input backgrounds to create subtle layering.
- **Functional Accents:** Status colors (Success, Warning, Error) use high-saturation "neon" variants to ensure they are immediately distinguishable against the dark background.

## Typography
The typography strategy relies on the technical precision of **Space Grotesk** for headings and UI labels, paired with the supreme legibility of **Inter** for data-heavy body content. 

All labels and technical readouts should favor uppercase or tabular lining figures to maintain a "gauged" look. Line heights are kept tight to maximize vertical information density without sacrificing readability. Use `label-caps` for table headers, section titles, and metadata tags to reinforce the industrial aesthetic.

## Layout & Spacing
The design system employs a **Fluid Grid** model based on a 4px baseline grid. The layout is optimized for widescreen command-center monitors, utilizing a 12-column system with tight 16px gutters to squeeze maximum utility into the viewport.

Components are "stacked" with consistent vertical rhythm. Large dashboards should use a "Dashboard Tile" approach where every element is contained within a defined module, preventing visual floating. Sidebars are docked and collapsible to prioritize the central map or data visualization area.

## Elevation & Depth
Depth is achieved through **Tonal Layering** and **Bold Borders** rather than traditional shadows. This maintains the "flat-panel" industrial feel.

- **Base Level:** Midnight Blue (#0B1221).
- **Surface Level:** Graphite (#2D2D2D) for cards and modules.
- **Interactive Level:** Safety Orange outlines or 1px solid borders.
- **Active State:** Use subtle 10% opacity fills of the accent color (e.g., an orange tint) to indicate selection.

Shadows are used sparingly and are "Hard" (0 blur, 2px offset) to mimic physical buttons or inset panels found on hardware control consoles.

## Shapes
The shape language is strictly **Sharp (0px)**. Rounded corners are avoided to maintain a rugged, hardware-inspired look. 

All buttons, input fields, and card containers must have square 90-degree angles. This reinforces the technical nature of the software and allows for seamless tiling of data modules. For decorative "tech" flourishes, use 45-degree chamfered (clipped) corners on primary call-to-action buttons or alert badges.

## Components
- **Alert Cards:** High-contrast containers with a thick (4px) left-side border keyed to status color. Backgrounds for "Critical" alerts should use a subtle pulse animation or a diagonal stripe "hazard" pattern in the header.
- **Buttons:** Sharp-edged. Primary buttons are solid Safety Orange with black text. Secondary buttons are outlined in Graphite with white text. Hover states should "invert" the colors.
- **Data Visualizations:** Use "Neon" status colors for lines and bars. Grid lines within charts must be subtle Midnight Blue variations to stay in the background.
- **Interactive Maps:** Dark-themed base layer with "Safety Orange" for active stadium sectors. Occupancy levels should be shown via high-saturation heatmaps.
- **Input Fields:** Inset appearance with Graphite background and a 1px frame. Focus state shifts the border to Safety Orange.
- **Status Chips:** Small, square badges. For example, a "LIVE" tag would be a solid red square with white monospace text.
- **Tactical Tabs:** Industrial style, appearing as physical tabs on a file folder, using high-contrast borders to indicate the active view.