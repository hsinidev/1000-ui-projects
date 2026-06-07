---
name: Terra & Bloom
colors:
  surface: '#fff8f4'
  surface-dim: '#e1d8d2'
  surface-bright: '#fff8f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fbf2eb'
  surface-container: '#f5ece5'
  surface-container-high: '#f0e7df'
  surface-container-highest: '#eae1da'
  on-surface: '#1f1b17'
  on-surface-variant: '#444841'
  inverse-surface: '#34302b'
  inverse-on-surface: '#f8efe8'
  outline: '#747870'
  outline-variant: '#c4c8be'
  surface-tint: '#52634a'
  primary: '#52634a'
  on-primary: '#ffffff'
  primary-container: '#899b7f'
  on-primary-container: '#23321d'
  inverse-primary: '#b9ccae'
  secondary: '#7b5737'
  on-secondary: '#ffffff'
  secondary-container: '#fecea6'
  on-secondary-container: '#795636'
  tertiary: '#675d4d'
  on-tertiary: '#ffffff'
  tertiary-container: '#a19482'
  on-tertiary-container: '#362d20'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#d5e8c9'
  primary-fixed-dim: '#b9ccae'
  on-primary-fixed: '#111f0c'
  on-primary-fixed-variant: '#3b4b34'
  secondary-fixed: '#ffdcc1'
  secondary-fixed-dim: '#ecbd96'
  on-secondary-fixed: '#2e1500'
  on-secondary-fixed-variant: '#604022'
  tertiary-fixed: '#f0e0cc'
  tertiary-fixed-dim: '#d3c4b1'
  on-tertiary-fixed: '#221a0e'
  on-tertiary-fixed-variant: '#4f4537'
  background: '#fff8f4'
  on-background: '#1f1b17'
  surface-variant: '#eae1da'
typography:
  headline-xl:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '600'
    lineHeight: '1.2'
  headline-lg:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  gutter: 24px
  margin-mobile: 16px
  margin-desktop: 48px
  container-max: 1280px
---

## Brand & Style

The brand personality for this design system is rooted in the Montessori philosophy: serene, professional, and deeply nurturing. It seeks to evoke an emotional response of "calm competence," providing educators and parents with a digital environment that feels as tactile and grounded as a physical classroom. 

The chosen style is **Modern Tactile**. This movement blends clean, minimalist layouts with realistic textures and organic forms. By incorporating subtle paper grains and wood-inspired accents, the UI moves away from "cold technology" toward a "digital toolset" that feels human-made. High whitespace and a muted, nature-inspired palette ensure that the interface remains unobtrusive, allowing the focus to remain on the child’s development rather than the software itself.

## Colors

The palette is derived from natural elements found in a traditional Montessori environment. 

- **Sage Green (Primary):** Used for primary actions and progress indicators, representing growth and tranquility.
- **Warm Wood (Secondary):** Used for accents, highlights, and tactile elements like buttons to provide a sense of stability and warmth.
- **Cream (Background):** A soft, low-blue-light alternative to pure white, reducing eye strain for long-term use.
- **Earthy Neutral:** Used for typography and iconography to maintain high legibility without the harshness of pure black.

Use a "Paper" neutral for card backgrounds (#FCFAF7) to create a subtle distinction from the main cream background.

## Typography

This design system utilizes a sophisticated pairing to balance institutional authority with a gentle touch. 

- **Headings:** **Noto Serif** provides a literary, classic feel. It should be used for page titles and section headers to give the system an editorial, professional quality.
- **UI & Body:** **Plus Jakarta Sans** is used for all functional text. Its soft, rounded terminals and open apertures ensure high legibility and a friendly, approachable character.

Maintain generous line heights (1.6 for body text) to ensure the interface feels spacious and unhurried.

## Layout & Spacing

The layout philosophy follows a **Fluid Grid** model with an 8px rhythmic unit. The system prioritizes "breathability" over information density, mimicking the open floor plans of Montessori classrooms.

- **Grid:** A 12-column fluid system for desktop, transitioning to a 4-column system for mobile.
- **Rhythm:** Use multiples of 8px for all padding and margins. 
- **White Space:** Increase vertical spacing between sections (using 64px or 80px) to prevent the UI from feeling cluttered or overwhelming.
- **Margins:** Generous outer margins (48px on desktop) help center the user's focus on the content.

## Elevation & Depth

Hierarchy is established through **Ambient Shadows** and **Tonal Layers** rather than sharp borders.

- **Surface Tiers:** Use a three-tier system. The base is the Cream background. The second tier consists of Paper-colored containers for content. The third tier includes floating elements like modals or dropdowns.
- **Shadows:** Shadows should be extremely soft and diffused, using a hint of the secondary color (Warm Wood) in the shadow tint to maintain a natural look. Avoid pure gray shadows.
- **Textures:** Apply a subtle noise/grain texture (opacity 2-3%) to large background surfaces and a wood-grain overlay to primary buttons and headers to reinforce the organic aesthetic.

## Shapes

The shape language is defined by high corner radii and organic curves. 

- **Base Radius:** Standard UI elements (inputs, small buttons) use a 0.5rem (8px) radius.
- **Large Containers:** Cards and content sections use a `rounded-xl` (1.5rem / 24px) radius to soften the layout.
- **Interactive Elements:** Highly interactive or "child-centered" elements (like chips or specialized action buttons) should lean toward pill shapes to evoke the feel of wooden blocks or pebbles.

## Components

- **Buttons:** Primary buttons feature a "Warm Wood" fill with white text and a very subtle inner glow to suggest a 3D, tactile quality. Secondary buttons use a Sage Green outline with a 2px stroke.
- **Cards:** Cards should have a "Paper" background (#FCFAF7), a 1px soft border (#E8D9C5), and a wide, soft shadow.
- **Inputs:** Text fields use a Cream fill slightly darker than the background, with a Sage Green focus ring. Labels are always positioned above the field for clarity.
- **Chips:** Used for student tags or categories. These should be pill-shaped with Sage Green backgrounds at 15% opacity and dark green text.
- **Checkboxes & Radios:** Use custom organic shapes; instead of sharp squares, checkboxes should have a generous 4px corner radius.
- **Progress Indicators:** Use Sage Green for "growth" metrics. Use a thick, rounded bar style that mimics a physical slider.
- **Additional Components:**
    - **Observation Log:** A specialized card component with a "notepaper" texture for educators to record daily insights.
    - **Milestone Badges:** Circular, wood-textured icons used to celebrate child achievements.