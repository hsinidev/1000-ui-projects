---
name: Global-Gala Design System
colors:
  surface: '#faf8ff'
  surface-dim: '#dad9e0'
  surface-bright: '#faf8ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f9'
  surface-container: '#efedf3'
  surface-container-high: '#e9e7ee'
  surface-container-highest: '#e3e2e8'
  on-surface: '#1a1b20'
  on-surface-variant: '#444650'
  inverse-surface: '#2f3035'
  inverse-on-surface: '#f1f0f6'
  outline: '#757682'
  outline-variant: '#c5c6d2'
  surface-tint: '#435b9f'
  primary: '#00113a'
  on-primary: '#ffffff'
  primary-container: '#002366'
  on-primary-container: '#758dd5'
  inverse-primary: '#b3c5ff'
  secondary: '#5d5f5f'
  on-secondary: '#ffffff'
  secondary-container: '#dfe0e0'
  on-secondary-container: '#616363'
  tertiary: '#2d0700'
  on-tertiary: '#ffffff'
  tertiary-container: '#501300'
  on-tertiary-container: '#d37758'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b3c5ff'
  on-primary-fixed: '#00174a'
  on-primary-fixed-variant: '#2a4386'
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#ffdbd0'
  tertiary-fixed-dim: '#ffb59e'
  on-tertiary-fixed: '#390b00'
  on-tertiary-fixed-variant: '#783018'
  background: '#faf8ff'
  on-background: '#1a1b20'
  surface-variant: '#e3e2e8'
typography:
  display-xl:
    fontFamily: Playfair Display
    fontSize: 72px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-lg:
    fontFamily: Playfair Display
    fontSize: 56px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-sm:
    fontFamily: Playfair Display
    fontSize: 24px
    fontWeight: '500'
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
    lineHeight: '1.5'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  margin-page: 80px
  gutter: 32px
  section-gap: 120px
  container-max: 1440px
---

## Brand & Style

The design system is engineered to evoke the atmosphere of an elite, high-society vernissage. It balances the weight of traditional art authority with the seamlessness of modern digital luxury. The target audience includes high-net-worth collectors, curators, and art enthusiasts who expect a "white-glove" digital experience.

The visual style is **Minimalist Luxury**, characterized by:
- **Digital Archiving:** A structural layout that treats the screen as a curated gallery wall rather than a traditional website.
- **Glassmorphism:** Using semi-transparent, frosted overlays to represent the glass cases and partitions of a physical exhibition.
- **Visual Silence:** Intentional use of negative space to direct the user's focus exclusively toward high-resolution artwork.
- **Architectural Precision:** Sharp lines and subtle shadows that mimic the lighting and geometry of modern gallery architecture.

## Colors

The palette is anchored in **Deep Royal Blue**, used sparingly for key structural elements, navigational anchors, and primary calls to action to signal prestige. **Crisp White** serves as the primary canvas, ensuring the artwork remains the focal point without chromatic interference.

**Graphite** is utilized for all primary text and fine borders, offering a softer, more sophisticated alternative to pure black. For interactive states, **Subtle Silver** and a desaturated **Light Blue** are used to provide gentle feedback that does not disrupt the visual serenity of the interface.

## Typography

This design system utilizes a high-contrast typographic pairing to reinforce the "grand" aesthetic. **Playfair Display** is reserved for headlines and large-scale editorial moments, evoking the feel of a printed exhibition catalog. Its high stroke contrast requires generous line heights to maintain elegance.

**Inter** provides the utilitarian counter-balance, used for all functional UI elements, metadata, and long-form body copy. This ensures that while the fair feels prestigious, the act of browsing and purchasing remains frictionless and accessible. All labels and metadata should use increased letter-spacing in uppercase to mimic luxury branding standards.

## Layout & Spacing

The layout follows a **Fixed Grid** model centered on the viewport. This design system utilizes a 12-column grid for standard content, but shifts to a wide 4-column grid for gallery views to maximize image size.

Spacing is intentionally expansive. **Section Gaps** are larger than standard web applications to create a sense of "breathing room" between different artist collections. Margins are fixed at 80px on desktop to frame the content like a matte around a painting. Alignment should prioritize the left axis for readability, with occasional centered "Display" moments for featured installations.

## Elevation & Depth

Hierarchy in this design system is achieved through **Glassmorphism** and **Light-source Shadows**.

1.  **The Base Layer:** Solid Crisp White (#FFFFFF).
2.  **The Overlay Layer:** Semi-transparent white (60-80% opacity) with a 20px backdrop blur and a 1px Graphite border at 10% opacity. This is used for navigation bars, filter menus, and modal dialogs.
3.  **Shadows:** Use extremely diffused "ambient" shadows (0px 20px 40px) with very low opacity (5% Graphite). This mimics the soft, indirect lighting of an art gallery.
4.  **Lines:** Horizontal and vertical dividers should be sharp, 1px lines using the Graphite color at 15% opacity, reinforcing the architectural structure.

## Shapes

To maintain the "Sharp, clean lines" requirement, the design system utilizes a **Soft (0.25rem)** roundedness. This prevents the UI from feeling "bubbly" or overly consumer-tech, while removing the aggressive harshness of true zero-radius corners.

- **Standard Elements:** 4px (0.25rem) radius for buttons and input fields.
- **Artwork Containers:** 0px radius (perfectly sharp) to treat the art as a true canvas.
- **Glass Overlays:** 8px (0.5rem) radius to differentiate UI "furniture" from the content.

## Components

### Buttons
- **Primary:** Deep Royal Blue background, white text, 4px radius. No shadow; use a subtle silver inner glow on hover.
- **Secondary:** Transparent background, 1px Graphite border, Graphite text.
- **Tertiary/Ghost:** Uppercase Inter Label with a 1px Royal Blue underline that expands on hover.

### Cards (The "Gallery Frame")
Cards should be minimalist. The image is the hero with a 0px radius. Information (Title, Artist, Price) is placed below the image using the `label-caps` and `headline-sm` typography levels. On hover, a subtle 1px border appears around the entire card.

### Inputs
Fields use a "bottom-border only" style to maintain a clean, architectural look. When focused, the bottom border transitions from light Graphite to Deep Royal Blue.

### Glass Overlays
Used for mobile menus and filter panels. They must include a high backdrop-blur (16px+) to ensure legibility of text over busy artwork backgrounds.

### Interactive Highlights
When a user selects a piece of art or an interactive element, use a 2px "Silver" border or a light blue wash (10% opacity) to signify the active state without overwhelming the art itself.