---
name: Serene Dignity
colors:
  surface: '#faf9f8'
  surface-dim: '#dadad9'
  surface-bright: '#faf9f8'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f4f3f2'
  surface-container: '#eeeeed'
  surface-container-high: '#e9e8e7'
  surface-container-highest: '#e3e2e1'
  on-surface: '#1a1c1c'
  on-surface-variant: '#504444'
  inverse-surface: '#2f3130'
  inverse-on-surface: '#f1f0ef'
  outline: '#827473'
  outline-variant: '#d4c2c2'
  surface-tint: '#7c5454'
  primary: '#7c5454'
  on-primary: '#ffffff'
  primary-container: '#d4a3a3'
  on-primary-container: '#5c3939'
  inverse-primary: '#edbaba'
  secondary: '#645d53'
  on-secondary: '#ffffff'
  secondary-container: '#e8ded1'
  on-secondary-container: '#686257'
  tertiary: '#5e5e5e'
  on-tertiary: '#ffffff'
  tertiary-container: '#b0afaf'
  on-tertiary-container: '#424243'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdad9'
  primary-fixed-dim: '#edbaba'
  on-primary-fixed: '#2f1314'
  on-primary-fixed-variant: '#613d3d'
  secondary-fixed: '#ebe1d4'
  secondary-fixed-dim: '#cfc5b9'
  on-secondary-fixed: '#1f1b13'
  on-secondary-fixed-variant: '#4c463c'
  tertiary-fixed: '#e4e2e2'
  tertiary-fixed-dim: '#c7c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#464747'
  background: '#faf9f8'
  on-background: '#1a1c1c'
  surface-variant: '#e3e2e1'
typography:
  h1:
    fontFamily: Noto Serif
    fontSize: 40px
    fontWeight: '400'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  h2:
    fontFamily: Noto Serif
    fontSize: 32px
    fontWeight: '400'
    lineHeight: '1.3'
  h3:
    fontFamily: Noto Serif
    fontSize: 24px
    fontWeight: '400'
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
    lineHeight: '1.6'
  label-caps:
    fontFamily: Manrope
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  cta:
    fontFamily: Manrope
    fontSize: 16px
    fontWeight: '500'
    lineHeight: '1.2'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1140px
  gutter: 24px
  margin-mobile: 20px
  section-gap: 80px
  stack-sm: 12px
  stack-md: 24px
---

## Brand & Style
The brand personality centers on quiet strength and unwavering support. This design system serves families navigating one of life’s most difficult transitions; therefore, the UI must act as a calm presence rather than a digital tool. The style is a refined **Minimalism** that prioritizes cognitive ease and emotional regulation.

Visuals are characterized by high whitespace—giving the content "room to breathe"—and a complete absence of high-intensity triggers like flashing elements or urgent marketing overlays. The emotional response is one of safety, professionalism, and profound respect for the individual’s journey. Transitions are intentionally slowed to a linear or soft ease-in-out to prevent jarring the user's focus.

## Colors
This design system utilizes a palette rooted in natural, soothing tones. 

- **Primary (Rose):** A muted, dusty rose used for key actions and gentle emphasis. It represents compassion and humanity.
- **Secondary (Sand):** Used for large surface areas and containers to provide warmth without the sterile feel of pure white.
- **Neutral (Soft Grey):** Applied to typography and secondary iconography to maintain high legibility while avoiding the harshness of pure black.
- **Background:** A very light "off-white" sand hue to reduce eye strain during prolonged reading.

Color application should be sparse. Functional colors, such as those for "Immediate Support," use a deeper, more grounded version of the primary rose to signal importance without inducing panic.

## Typography
The typography strategy pairs the timeless authority of **Noto Serif** with the modern clarity of **Manrope**. 

Headlines use Noto Serif to evoke a sense of tradition, heritage, and calm expertise. Line heights are generous to ensure that even users under high stress can parse information without feeling overwhelmed. Body text uses Manrope at a slightly larger-than-standard base size (18px for primary reading) to accommodate senior family members and those with visual fatigue. All-caps are reserved strictly for small labels to maintain a gentle tone; never use all-caps for instructional text.

## Layout & Spacing
This design system employs a **Fixed Grid** for desktop to ensure content remains centered and focused, preventing eye-scanning fatigue. On mobile, the system shifts to a fluid model with wide margins (20px) to prevent accidental taps.

Spacing is used as a functional tool to separate concepts. Large vertical gaps (80px+) between sections are encouraged to prevent information density. For mobile users in distress, the layout must prioritize a "Clear Path" architecture: one primary thought or action per screen view.

## Elevation & Depth
In alignment with the minimalist and respectful aesthetic, this design system avoids heavy shadows or complex 3D effects. Depth is communicated through **Tonal Layers** and **Low-Contrast Outlines**.

- **Surface Tiers:** Backgrounds are the lightest sand hue. Content cards use a pure white or a slightly deeper sand tone to create a subtle stack.
- **Soft Outlines:** Buttons and inputs use a 1px border in a slightly darker shade of the background color rather than a shadow.
- **Focus States:** When an element is active, use a soft, diffused 8px glow in the primary Rose color (10% opacity) rather than a sharp focus ring.

## Shapes
The shape language is consistently **Rounded**. Sharp corners are avoided to maintain a "soft" psychological profile. Standard UI elements like cards and input fields use a 0.5rem radius, while larger containers or featured imagery should utilize a 1rem radius. This curviness suggests approachability and gentleness, echoing the "Grace" in the brand's identity.

## Components
Consistent component styling ensures the interface feels predictable and safe.

- **Primary Buttons:** Solid Rose background with white Manrope text. No shadows; use soft rounded corners (0.5rem).
- **Secondary Buttons:** Transparent background with a Sand-colored border.
- **Immediate Support Button (Mobile):** A persistent, anchored bar at the bottom of the viewport. It should be slightly taller than standard buttons, using the deeper Rose status color for visibility, providing a "One-Tap to Call" functionality.
- **Cards:** Low-elevation. Use a 1px border in a muted Sand tone rather than a shadow. Padding within cards should be generous (min 24px).
- **Input Fields:** Soft grey labels placed above the field. The fields themselves have a light sand background to indicate "fillable" space without looking like a blank void.
- **Progress Indicators:** For intake forms, use a soft horizontal line. Avoid "step numbers" which can feel clinical; use descriptive, gentle labels like "Understanding your needs."
- **Empty States:** Use soft, hand-drawn style iconography or high-quality photography of nature (stones, water, petals) to maintain the serene atmosphere.