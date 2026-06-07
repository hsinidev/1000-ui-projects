---
name: Blue-Urban Narrative
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f4'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e3'
  on-surface: '#191c1d'
  on-surface-variant: '#40484a'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#eff1f2'
  outline: '#70787b'
  outline-variant: '#bfc8ca'
  surface-tint: '#2a6673'
  primary: '#00333c'
  on-primary: '#ffffff'
  primary-container: '#004b57'
  on-primary-container: '#81bac8'
  inverse-primary: '#96d0de'
  secondary: '#566064'
  on-secondary: '#ffffff'
  secondary-container: '#d7e1e6'
  on-secondary-container: '#5a6469'
  tertiary: '#2b2e30'
  on-tertiary: '#ffffff'
  tertiary-container: '#414446'
  on-tertiary-container: '#aeb1b3'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b2ecfa'
  primary-fixed-dim: '#96d0de'
  on-primary-fixed: '#001f25'
  on-primary-fixed-variant: '#064e5a'
  secondary-fixed: '#dae4e9'
  secondary-fixed-dim: '#bec8cd'
  on-secondary-fixed: '#141d21'
  on-secondary-fixed-variant: '#3f484d'
  tertiary-fixed: '#e0e3e5'
  tertiary-fixed-dim: '#c4c7c9'
  on-tertiary-fixed: '#191c1e'
  on-tertiary-fixed-variant: '#444749'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e3'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Work Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Work Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
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
  container-max: 1280px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 64px
  section-gap: 120px
---

## Brand & Style

This design system embodies the intersection of nautical tradition and modern urban development. It is defined by a **Nautical-Modern** aesthetic—a style that bridges the gap between the rugged reliability of maritime engineering and the sleek sophistication of high-end waterfront architecture.

The visual direction utilizes a refined **Corporate Modern** foundation infused with **Glassmorphism** and metallic accents. It evokes an emotional response of security, premium exclusivity, and serene openness. The user interface should feel like standing on a glass-walled balcony overlooking a calm, deep-water harbor: expansive, high-contrast, and impeccably clean.

Key attributes include:
- **Precision:** Mathematical alignments and silver-metallic linework.
- **Fluidity:** Subtle horizontal gradients and soft transitions mimicking water movement.
- **Transparency:** The use of blurred overlays to maintain a sense of environmental depth.

## Colors

The palette is anchored by **Deep Teal**, representing the strength and depth of the ocean. This is contrasted against **Crisp White** surfaces to maintain a high-visibility, professional environment. 

**Silver** is used exclusively as a functional accent—for borders, button strokes, and interactive states—to mimic polished marine hardware. Secondary neutrals are kept cool-toned to ensure the "Blue-Urban" identity remains consistent across all surfaces. Gradients should be used sparingly, primarily as background washes for large sections or as "Sea-Level" indicators in data visualizations.

## Typography

The typography strategy prioritizes structural clarity. **Inter** is utilized for headlines and UI labels to provide a systematic, geometric appearance that aligns with modern architectural blueprints. **Work Sans** is selected for body text due to its exceptional readability and slightly wider apertures, which contribute to the "airy" feel of the coastal narrative.

Large headings should use tight letter-spacing to feel impactful, while uppercase labels are tracked out to evoke the look of navigational charts and maritime signage.

## Layout & Spacing

This design system employs a **Fixed Grid** model on desktop to mirror the structured planning of waterfront developments. To achieve an "open and airy" atmosphere, the system utilizes aggressive vertical spacing (Section Gaps) and generous internal padding within components.

Layouts should favor asymmetrical balance—placing heavy high-resolution coastal imagery against clean, white whitespace. Content is aligned to a 12-column grid with wide gutters to ensure no element feels cramped, mimicking the vastness of the horizon.

## Elevation & Depth

Depth is conveyed through **Glassmorphism** and **Tonal Layers** rather than heavy shadows. 
- **Surface Level:** The base layer is always Crisp White or a very subtle cool-grey wash.
- **Raised Elements:** Cards and modals use a "Frosted Glass" effect (backdrop-blur: 20px) with a 1px Silver metallic border.
- **Interaction Depth:** Buttons do not "sink" when pressed; instead, they shift their silver gradient orientation or increase in inner luminosity, mimicking light reflecting off a metallic surface.
- **Shadows:** When necessary, use extremely diffused, low-opacity Deep Teal shadows (#004B57 at 8% opacity) to ground elements without creating "dirt" on the clean interface.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding strikes a balance between the hard edges of industrial docks and the organic curves of hull designs. 

- **Primary Containers:** Standard 4px (0.25rem) radius.
- **Feature Cards:** Large containers may use up to 8px (0.5rem) to feel more inviting.
- **Form Inputs:** Strict 4px corners to maintain a professional, administrative tone.
- **Iconography:** Use "Stroked" icons with a 2px weight, echoing the silver linework found in the UI borders.

## Components

### Sleek Cards
Cards feature a white background, a 1px Silver border, and no initial shadow. On hover, the border gains a subtle metallic sheen (gradient) and the background applies a faint "Water Gradient" wash.

### Interactive Booking Forms
Forms are designed with high-contrast inputs. Labels use `label-caps` in Deep Teal. Active fields are highlighted with a Silver metallic stroke. The 'Sea-Level' visualization is used here to show availability or progress, using a horizontal teal fill that "waves" slightly.

### Buttons
- **Primary:** Deep Teal background with White text.
- **Secondary:** Silver metallic gradient background with Deep Teal text.
- **Ghost:** Transparent background with a 1px Silver stroke.

### Sea-Level Visualizations
A signature component style where data (such as slip occupancy or water depth) is displayed using a fluid, horizontal fill pattern. The fill should have a subtle sine-wave mask at the top edge to reinforce the nautical theme.

### Status Chips
Utilize semi-transparent backgrounds with high-contrast text. For example, a 'Confirmed' status uses a light teal tint with Deep Teal text, housed in a pill-shaped container to distinguish it from structural UI elements.