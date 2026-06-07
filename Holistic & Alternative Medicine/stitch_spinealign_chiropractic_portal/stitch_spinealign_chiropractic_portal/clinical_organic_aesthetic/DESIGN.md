---
name: Clinical-Organic Aesthetic
colors:
  surface: '#f3faff'
  surface-dim: '#c5deeb'
  surface-bright: '#f3faff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#e6f6ff'
  surface-container: '#d9f2ff'
  surface-container-high: '#d3ecf9'
  surface-container-highest: '#cde6f4'
  on-surface: '#051e28'
  on-surface-variant: '#3f4945'
  inverse-surface: '#1c333e'
  inverse-on-surface: '#e0f4ff'
  outline: '#707975'
  outline-variant: '#bfc9c4'
  surface-tint: '#29695b'
  primary: '#00342b'
  on-primary: '#ffffff'
  primary-container: '#004d40'
  on-primary-container: '#7ebdac'
  inverse-primary: '#94d3c1'
  secondary: '#4c616c'
  on-secondary: '#ffffff'
  secondary-container: '#cfe6f2'
  on-secondary-container: '#526772'
  tertiary: '#2d2e2b'
  on-tertiary: '#ffffff'
  tertiary-container: '#434441'
  on-tertiary-container: '#b2b1ad'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#afefdd'
  primary-fixed-dim: '#94d3c1'
  on-primary-fixed: '#00201a'
  on-primary-fixed-variant: '#065043'
  secondary-fixed: '#cfe6f2'
  secondary-fixed-dim: '#b4cad6'
  on-secondary-fixed: '#071e27'
  on-secondary-fixed-variant: '#354a53'
  tertiary-fixed: '#e4e2de'
  tertiary-fixed-dim: '#c8c6c3'
  on-tertiary-fixed: '#1b1c1a'
  on-tertiary-fixed-variant: '#474744'
  background: '#f3faff'
  on-background: '#051e28'
  surface-variant: '#cde6f4'
typography:
  headline-xl:
    fontFamily: Newsreader
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: Newsreader
    fontSize: 32px
    fontWeight: '500'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Newsreader
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
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
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  button:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '600'
    lineHeight: '1'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 48px
  xl: 80px
  container-max: 1200px
  gutter: 24px
---

## Brand & Style
This design system embodies a "Clinical-Organic" aesthetic, specifically tailored for a holistic chiropractic environment. It balances the precision of medical expertise with the softness of natural wellness. The brand personality is professional, empathetic, and restorative. 

The visual style follows a **Modern Minimalist** approach with tactile elements. By prioritizing generous whitespace and a structured layout, the UI reduces cognitive load, inducing a sense of calm in patients. The objective is to evoke an emotional response of safety and relief, positioning the center as a sanctuary of alignment and health.

## Colors
The palette is rooted in nature and professional stability. 
- **Deep Teal (#004D40):** Used for primary actions, branding, and core structural elements to convey depth and restorative health.
- **Slate (#455A64):** Utilized for secondary text and icons, providing a grounded, professional contrast that is easier on the eyes than pure black.
- **Warm White (#FDFBF7):** The foundation of the interface. This off-white shade prevents the "sterile" feeling of pure white, adding an organic warmth to the clinical setting.
- **Functional Accents:** Subtle variations of Slate are used for borders and disabled states to maintain a soft, low-contrast environment.

## Typography
The typography strategy employs a high-contrast pairing to signify both tradition and modernity. 
- **Headlines:** **Newsreader** provides a literary, authoritative serif that communicates years of expertise and a holistic, "human" touch. Use it for page titles and section headers to establish trust.
- **UI Elements & Body:** **Manrope** is used for all functional elements. Its modern, refined, and balanced geometric shapes ensure maximum legibility for clinical information and patient data. 
- **Hierarchy:** Ensure generous line heights (1.5+) for body copy to enhance readability for patients who may be experiencing discomfort or stress.

## Layout & Spacing
The layout follows a **Fixed Grid** model to project stability and order. A 12-column system is used for desktop layouts, while mobile transitions to a single-column stack with 20px side margins.

Spacing is used intentionally to create "breathing room." Large vertical gaps (Level XL) should separate major sections to prevent the interface from feeling cluttered. Content blocks within cards should use the MD (24px) spacing unit for internal padding to maintain a consistent rhythm.

## Elevation & Depth
Depth in this design system is achieved through **Ambient Shadows** and tonal layering rather than harsh borders. 
- **Surface Strategy:** Use the Warm White base as the primary background. 
- **Shadows:** Shadows should be extremely diffused (Blur: 30px-40px) with very low opacity (5%-8%) and a subtle tint of Deep Teal. This creates an "organic lift" that feels like the element is resting gently on a soft surface.
- **Interactions:** Hover states on interactive cards should see a slight increase in shadow spread and a subtle vertical shift (-2px) to provide tactile feedback.

## Shapes
The shape language is defined by "Softened Geometry." 
- **Corner Radius:** A standard radius of 0.5rem (8px) is applied to most UI components, while primary cards and containers use 1rem (16px) to emphasize the "organic" and approachable nature of the brand.
- **Icons:** Use icons with rounded terminals and medium stroke weights to match the Manrope typeface and the soft corner radius of the containers.

## Components
- **Buttons:** Primary CTAs are solid Deep Teal with white Manrope text. They should feel substantial with generous horizontal padding. Secondary buttons use a Slate outline (1px) with a transparent background.
- **Cards:** These are the primary vessel for information. They feature 16px rounded corners, the ambient shadow defined in Elevation, and a 1px stroke in a very light tint of Slate to provide definition against the Warm White background.
- **Input Fields:** Use a subtle background fill (a 5% tint of Slate) with a bottom-only border or a light all-around stroke. Focus states should transition the border to Deep Teal.
- **Chips/Badges:** Small, pill-shaped elements used for treatment categories (e.g., "Massage Therapy," "Adjustment"). These use a low-saturation Teal background with Deep Teal text.
- **Appointment Scheduler:** A custom component featuring a clean calendar grid with soft-rounded date pickers, emphasizing clarity and ease of use for the patient.