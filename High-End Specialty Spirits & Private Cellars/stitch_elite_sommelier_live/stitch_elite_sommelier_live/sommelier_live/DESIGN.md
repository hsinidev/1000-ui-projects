---
name: Sommelier-Live
colors:
  surface: '#faf9fc'
  surface-dim: '#dbd9dd'
  surface-bright: '#faf9fc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f6'
  surface-container: '#efedf0'
  surface-container-high: '#e9e7eb'
  surface-container-highest: '#e3e2e5'
  on-surface: '#1a1c1e'
  on-surface-variant: '#43474e'
  inverse-surface: '#2f3033'
  inverse-on-surface: '#f2f0f3'
  outline: '#74777f'
  outline-variant: '#c4c6cf'
  surface-tint: '#476083'
  primary: '#000613'
  on-primary: '#ffffff'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#afc8f0'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#110200'
  on-tertiary: '#ffffff'
  tertiary-container: '#391303'
  on-tertiary-container: '#b5785f'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#ffdbce'
  tertiary-fixed-dim: '#fdb69a'
  on-tertiary-fixed: '#351002'
  on-tertiary-fixed-variant: '#6b3a25'
  background: '#faf9fc'
  on-background: '#1a1c1e'
  surface-variant: '#e3e2e5'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
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
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  section-desktop: 80px
  section-mobile: 40px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 20px
---

## Brand & Style

The design system is engineered to evoke the atmosphere of an exclusive private tasting room—refined, hushed, and deeply personal. It bridges the gap between digital convenience and the tactile heritage of high-end viticulture. The brand target is the affluent enthusiast who values expertise and human connection over algorithmic recommendations.

The aesthetic utilizes **Soft-UI (Neumorphism-lite)** to create a sense of physical depth and luxury. By using subtle highlights and recessed shadows, UI elements appear to be gently pressed into or extruded from a "Silk White" surface. This tactile approach, combined with generous white space and high-end imagery (macro photography of wine textures, condensation on crystal, and vineyard soils), creates a serene, premium environment.

## Colors

The palette is minimalist and high-contrast to emphasize clarity and prestige. 

- **Silk White (#F9F9F9):** The primary canvas color. It is softer than pure white, reducing eye strain and providing a luxurious, paper-like foundation for soft-UI shadows.
- **Navy (#001F3F):** Used for primary typography, deep-action buttons, and brand-heavy moments. It represents authority and the "Blue Chip" nature of elite wine collections.
- **Silver (#C0C0C0):** Used for borders, subtle shadows, and secondary iconography. It adds a metallic, refined finish to the interface.
- **Support Colors:** Functional states (Success/Error) should be muted—think a deep vineyard green and a dried-grape burgundy—to maintain the sophisticated tone.

## Typography

This design system utilizes a high-contrast typographic pairing to signal both heritage and modern efficiency.

**Playfair Display** is reserved for headlines and editorial moments. Its high-contrast strokes reflect the elegance of wine labels and classic cellar catalogs. For display sizes, tighter letter-spacing is encouraged to maintain a "prestige fashion" feel.

**Inter** provides the functional backbone of the UI. It is used for all body copy, navigation, and technical data (e.g., vintage years, alcohol percentages). Its neutrality ensures that the interface remains legible and does not compete with the decorative serif headlines. Use the **Label-Caps** style for small metadata and section headers to add a structured, catalogued appearance.

## Layout & Spacing

The layout philosophy follows a **Fixed Grid** on desktop (12 columns, 1200px max-width) to create a centered, intentional reading experience reminiscent of a luxury magazine. On mobile, a fluid 4-column grid is used.

**White Space as a Luxury Asset:** 
Large vertical gaps (`section-desktop`) are intentional. Content should never feel crowded. Negative space is treated as a design element that directs focus toward high-end imagery and the wine experts themselves. 

The spacing rhythm is based on an 8px scale. Layouts should favor asymmetrical compositions when displaying wine bottles or vineyard photography to create a dynamic, editorial feel.

## Elevation & Depth

This design system utilizes **Neumorphism-lite** to achieve a tactile, premium feel without the visual clutter of traditional skeuomorphism.

- **Soft Extrusion:** Elements like cards and buttons use two shadows: a light shadow (White, #FFFFFF) on the top-left and a soft dark shadow (Silver, #C0C0C0, at 30% opacity) on the bottom-right.
- **Concave States:** Active buttons or input fields use internal shadows (inset) to appear "pressed" into the Silk White surface.
- **Tonal Depth:** Instead of heavy drop shadows, depth is communicated through 1px borders in Silver (#C0C0C0) with 50% transparency, creating a "glass-on-silk" effect. 
- **Backdrop Blur:** Modal overlays use a subtle 8px blur to keep the background context visible while focusing the user on the elite consulting interaction.

## Shapes

The shape language is "Soft" (`0.25rem` base), striking a balance between the precision of a professional service and the organic nature of wine. 

- **Cards & Containers:** Use `rounded-lg` (0.5rem) to maintain a modern, approachable feel.
- **Buttons:** Primary buttons should be slightly more rounded (`rounded-xl` / 0.75rem) to invite interaction.
- **Imagery:** Wine bottle photography and sommelier profiles should use sharp or very subtly rounded corners to maintain a "framed" gallery appearance.
- **Decorative Elements:** Use thin, horizontal Silver lines to separate sections, mimicking the ruled lines of a sommelier’s tasting notebook.

## Components

**Buttons:** 
- *Primary:* Navy background with Silk White text. Subtle outer glow on hover.
- *Secondary:* Silk White background with Navy text and a "Soft-UI" extruded shadow effect.

**Input Fields:**
- Minimalist design with a 1px Silver bottom border. When focused, the field transitions to a "pressed" Neumorphic state with an internal shadow.

**Cards (The "Vintage Card"):**
- A Silk White surface with a `0.5rem` radius. It features a refined 1px Silver border and a soft-UI shadow. These are used for featuring specific wine bottles or Sommelier profiles.

**Sommelier Live-Status Indicator:**
- A custom component featuring a pulsating soft-glow Navy dot next to a sommelier’s name, indicating real-time availability for consultation.

**Lists & Data:**
- Tasting notes and wine specs are displayed in Inter (Body-md) with generous line height. Use Silver dividers between items to maintain a clean, organized hierarchy.

**Navigation:**
- A fixed top bar in Silk White with 80% opacity and a backdrop blur. Navigation links use `Label-Caps` for a sophisticated, structured feel.