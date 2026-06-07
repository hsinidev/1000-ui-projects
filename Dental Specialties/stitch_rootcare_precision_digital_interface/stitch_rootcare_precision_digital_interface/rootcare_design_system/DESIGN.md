---
name: RootCare Design System
colors:
  surface: '#f7fafc'
  surface-dim: '#d7dadc'
  surface-bright: '#f7fafc'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f1f4f6'
  surface-container: '#ebeef0'
  surface-container-high: '#e5e9eb'
  surface-container-highest: '#e0e3e5'
  on-surface: '#181c1e'
  on-surface-variant: '#43474e'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eef1f3'
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
  tertiary: '#00070b'
  on-tertiary: '#ffffff'
  tertiary-container: '#00222e'
  on-tertiary-container: '#688b9c'
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
  tertiary-fixed: '#c3e8fb'
  tertiary-fixed-dim: '#a7ccde'
  on-tertiary-fixed: '#001f29'
  on-tertiary-fixed-variant: '#274b5a'
  background: '#f7fafc'
  on-background: '#181c1e'
  surface-variant: '#e0e3e5'
typography:
  h1:
    fontFamily: Manrope
    fontSize: 40px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  label-sm:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  base: 8px
  container-max: 1200px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
---

## Brand & Style

The brand identity centers on the intersection of medical mastery and patient serenity. As a specialized endodontics practice, the visual language must communicate extreme precision (the "high-tech" aspect) while simultaneously lowering the patient’s cortisol levels (the "calm" aspect). 

The design style is **Clinical Minimalism**. It leverages expansive white space to suggest a sterile, organized environment, but softens the edges with a "calm-centric" palette to avoid appearing cold or intimidating. The UI avoids unnecessary ornamentation, favoring structural clarity and high-quality typography to establish trust. Elements of **Glassmorphism** are used sparingly to represent the "advanced" nature of the practice—specifically through translucent overlays that mimic the layering of biological and technological data.

## Colors

The palette is anchored by **Deep Navy (#001F3F)**, a color of profound authority and traditional medical reliability. This is contrasted by **Soft Silver (#C0C0C0)**, which provides a high-tech, metallic precision to the interface.

To achieve the "Calm-Centric" requirement, the system introduces a spectrum of muted tones:
- **Tertiary Slate Blue:** Used for secondary actions and subtle iconography.
- **Surface Grays:** A range of cool-toned neutrals (#F4F7F9) replaces pure white for backgrounds to reduce eye strain and screen glare.
- **Subdued Accents:** Soft blues are utilized for success states and progress indicators, ensuring the interface feels supportive rather than demanding.

## Typography

This design system utilizes a dual-font strategy to balance character with utility. 

**Manrope** is used for all headings. Its modern, geometric construction feels advanced and progressive, while its open apertures keep it feeling accessible. **Inter** is the workhorse for all body copy and UI labels, chosen for its exceptional legibility in clinical contexts where technical data must be read without error.

Letter spacing is slightly tightened on large headings for a "premium" feel and slightly widened on small labels to ensure clarity against the Soft Silver backgrounds.

## Layout & Spacing

The layout follows a **Fixed Grid** model for desktop views to maintain a sense of containment and control, centering the user's focus. A 12-column system is used with generous 24px gutters to allow the UI to "breathe."

The spacing rhythm is strictly based on an 8px baseline grid. This mathematical consistency reinforces the "precision" of the endodontic specialty. Large padding values (often 64px or 80px) are used between sections to enforce a calm, unhurried user journey.

## Elevation & Depth

To maintain a "high-tech" yet "clinical" feel, the design system avoids heavy, dark shadows. Instead, it utilizes **Tonal Layering** and **Glassmorphism**.

1.  **Surface Tiers:** Backgrounds use a light neutral, while cards and primary containers use pure white to appear "lifted."
2.  **Soft Silver Outlines:** Instead of shadows, 1px borders in Soft Silver or semi-transparent Navy are used to define boundaries.
3.  **The "Surgical" Glow:** For high-tech elements (like interactive tooth charts or imaging), a very subtle, diffused glow in a calm blue is used to indicate "active" states, simulating light passing through medical-grade materials.

## Shapes

The shape language is **Soft (0.25rem)**. This subtle rounding of corners bridges the gap between the sharpness of clinical tools and the softness of human-centric care.

- **Primary Buttons:** Use a slightly higher roundedness (0.5rem) to feel more inviting to the touch.
- **Data Containers:** Maintain the standard 0.25rem radius to feel structural and precise.
- **Interactive States:** Changes in shape are avoided; instead, depth or color shifts indicate interactivity to maintain a stable, "calm" environment.

## Components

### Buttons
Primary buttons use the Deep Navy background with white text, emphasizing decisiveness. Secondary buttons utilize a Soft Silver ghost style with a Navy border. All buttons feature a subtle 200ms transition on hover.

### Cards
Cards are the primary container for patient data and service information. They should have a white background, a 1px Soft Silver border, and no shadow. On hover, the border may darken to Deep Navy to indicate focus.

### Input Fields
Inputs are minimalist, featuring only a bottom border in Soft Silver that transforms into a Deep Navy border upon focus. Labels remain visible above the field in the `label-sm` typography style.

### Chips & Tags
Used for medical categories (e.g., "Diagnostic," "Surgical"). These use the "Calm-Centric" muted blues and grays with low-contrast text to ensure they provide information without competing for visual attention.

### Specialist Components
- **Imaging Viewer:** A dark-mode specific container within the light-mode UI for viewing X-rays or 3D scans, emphasizing high-tech precision.
- **Progress Stepper:** A thin, linear indicator using Soft Silver for incomplete steps and Deep Navy for completed ones, mapping the patient's treatment journey.