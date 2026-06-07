---
name: Adventurous Chic
colors:
  surface: '#fcf9f8'
  surface-dim: '#dcd9d9'
  surface-bright: '#fcf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f6f3f2'
  surface-container: '#f0eded'
  surface-container-high: '#eae7e7'
  surface-container-highest: '#e5e2e1'
  on-surface: '#1c1b1b'
  on-surface-variant: '#594139'
  inverse-surface: '#313030'
  inverse-on-surface: '#f3f0ef'
  outline: '#8d7167'
  outline-variant: '#e1bfb4'
  surface-tint: '#a93700'
  primary: '#973100'
  on-primary: '#ffffff'
  primary-container: '#c04000'
  on-primary-container: '#ffe9e3'
  inverse-primary: '#ffb59b'
  secondary: '#4b53bc'
  on-secondary: '#ffffff'
  secondary-container: '#8991fe'
  on-secondary-container: '#1b218f'
  tertiary: '#515359'
  on-tertiary: '#ffffff'
  tertiary-container: '#6a6b71'
  on-tertiary-container: '#ededf4'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdbcf'
  primary-fixed-dim: '#ffb59b'
  on-primary-fixed: '#380d00'
  on-primary-fixed-variant: '#812800'
  secondary-fixed: '#e0e0ff'
  secondary-fixed-dim: '#bfc2ff'
  on-secondary-fixed: '#00006e'
  on-secondary-fixed-variant: '#3239a3'
  tertiary-fixed: '#e2e2e9'
  tertiary-fixed-dim: '#c5c6cd'
  on-tertiary-fixed: '#191c20'
  on-tertiary-fixed-variant: '#45474c'
  background: '#fcf9f8'
  on-background: '#1c1b1b'
  surface-variant: '#e5e2e1'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  display-md:
    fontFamily: Playfair Display
    fontSize: 36px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 22px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Be Vietnam Pro
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-lg:
    fontFamily: Be Vietnam Pro
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Be Vietnam Pro
    fontSize: 12px
    fontWeight: '500'
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
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  xxl: 64px
  container-margin: 20px
  story-gap: 0px
---

## Brand & Style

This design system embodies the spirit of "The Modern Explorer"—a persona that values the rugged freedom of the open road as much as the refinement of a five-star stay. The aesthetic is a fusion of high-contrast editorial fashion and tactile outdoor utility. It prioritizes a "mobile-first" travel companion experience, ensuring that luxury is never sacrificed for functionality while on the move.

The design style is **Tactile & High-Contrast**. It moves away from the sterile flatness of modern SaaS, instead embracing rich textures reminiscent of vintage maps, grain-heavy leather, and thick cotton paper. The "stories-style" vertical layout dominates the user experience, utilizing full-height immersive segments that feel like flipping through a high-end travel monograph.

## Colors

The palette is driven by three core pillars: Earth, Depth, and Air. 

- **Terracotta (#C04000):** Used as the primary action color. It represents the sun-baked roads and clay of the landscape. It should be used for calls to action, active states, and critical highlights.
- **Navy (#000080):** Represents the reliability of the service and the vastness of the night sky. It serves as the primary color for typography on light backgrounds and for heavy structural elements like footers or headers.
- **Silk White (#F8F8FF):** A cool, crisp neutral that provides the canvas. It is used for backgrounds to maintain a high-contrast, "chic" editorial feel.

Secondary neutrals should include a deep charcoal for body text to ensure maximum legibility against the Silk White background under various lighting conditions during travel.

## Typography

This design system utilizes a high-contrast typographic pairing to balance sophistication with utility. 

**Playfair Display** is the voice of the brand. It is used for headlines and display text to evoke a sense of heritage and luxury. Its high-contrast strokes and playful serifs provide an editorial quality.

**Be Vietnam Pro** is the workhorse. Selected for its exceptional readability on mobile devices, it handles all body copy, navigation items, and data-heavy labels. Its contemporary, open apertures ensure clarity even when the user is glancing at their phone in a moving vehicle. 

All labels and captions should utilize slightly increased letter spacing and uppercase styling to mimic the aesthetic of classic cartography.

## Layout & Spacing

The layout philosophy follows a **Vertical Story Model**. Designed for the mobile traveler, content is organized into full-screen (100vh) modules that snap into place as the user scrolls. This minimizes cognitive load and allows the photography to take center stage.

- **Grid:** A simple 4-column fluid mobile grid with 20px outside margins. On tablet and desktop, this expands to an 8-column and 12-column fixed grid respectively.
- **Rhythm:** Vertical spacing is generous, using the `xxl` (64px) unit to separate distinct content ideas, while internal component spacing remains tight (`sm` or `md`) to keep related information grouped.
- **Stories-Style:** Transitions between sections should be seamless, often using full-bleed imagery to create a cinematic flow.

## Elevation & Depth

Depth in this design system is achieved through **Tactile Layering** rather than traditional drop shadows. 

- **Subtle Textures:** Use a very fine noise overlay (2-3% opacity) on the Silk White background to simulate premium paper. Components should occasionally feature a "leather grain" CSS texture to provide physical presence.
- **Inner Shadows:** Buttons and input fields use subtle inner shadows to appear "pressed" or "embossed" into the surface, suggesting a tactile, physical control panel.
- **Layering:** Hierarchy is established by stacking "cards" with sharp, high-contrast borders (Navy on Silk White) or by using Navy-colored containers that sit "above" the Silk White base.
- **Map Overlays:** Use semi-transparent Navy layers with backdrop blurs when placing text over topographical maps or travel photography to maintain legibility.

## Shapes

The shape language is **Soft (0.25rem)**, leaning into a structured, architectural feel. 

While the "stories" containers are strictly sharp and full-bleed, internal components like buttons and cards use a subtle 4px corner radius. This choice prevents the UI from feeling too aggressive or "brutalist," maintaining a level of "chic" approachable luxury. 

Buttons that act as primary triggers may occasionally use a fully rounded (pill) shape to distinguish them from information-only cards, but this should be used sparingly to keep the design grounded.

## Components

### Buttons
Primary buttons use a Terracotta fill with Navy or White text. They feature a high-contrast 1px Navy border and a subtle inner-bevel effect to feel tactile. Hover and active states should feel "mechanical," as if clicking a physical toggle.

### Cards
Cards are the primary container for road trip "legs" or hotel details. They feature a 1px Navy border and a Silk White background. They do not use shadows; instead, they use a slight offset (2px) for a "sticker" effect when hovered or focused.

### Input Fields
Inputs are designed to resemble forms on a physical travel itinerary. They use a bottom-border-only style in Navy, with labels floating in a small, all-caps Be Vietnam Pro font above the line.

### Progress Indicators (The Route)
A custom component that visualizes road trip progress. It uses a thick, dashed Navy line (mimicking a map path) with Terracotta pins representing stops.

### Stories Navigation
A series of thin horizontal bars at the top of the screen (similar to social media stories) that indicate the user's progress through the vertical content segments.

### Tactile Chips
Used for tags like "Scenic Route" or "Luxury Stay." These should have a light Terracotta tint and a border, appearing like small stamped leather tags.