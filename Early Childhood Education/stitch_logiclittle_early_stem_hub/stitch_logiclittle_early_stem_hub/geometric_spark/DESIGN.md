---
name: Geometric Spark
colors:
  surface: '#f8f9fa'
  surface-dim: '#d9dadb'
  surface-bright: '#f8f9fa'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f4f5'
  surface-container: '#edeeef'
  surface-container-high: '#e7e8e9'
  surface-container-highest: '#e1e3e4'
  on-surface: '#191c1d'
  on-surface-variant: '#434656'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#737688'
  outline-variant: '#c3c5d9'
  surface-tint: '#004dea'
  primary: '#0041c8'
  on-primary: '#ffffff'
  primary-container: '#0055ff'
  on-primary-container: '#e3e6ff'
  inverse-primary: '#b6c4ff'
  secondary: '#565f69'
  on-secondary: '#ffffff'
  secondary-container: '#d7e1ec'
  on-secondary-container: '#5a646d'
  tertiary: '#00576a'
  on-tertiary: '#ffffff'
  tertiary-container: '#007189'
  on-tertiary-container: '#c1eeff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dce1ff'
  primary-fixed-dim: '#b6c4ff'
  on-primary-fixed: '#001551'
  on-primary-fixed-variant: '#0039b3'
  secondary-fixed: '#dae4ef'
  secondary-fixed-dim: '#bec8d3'
  on-secondary-fixed: '#131d25'
  on-secondary-fixed-variant: '#3e4851'
  tertiary-fixed: '#b4ebff'
  tertiary-fixed-dim: '#3cd7ff'
  on-tertiary-fixed: '#001f27'
  on-tertiary-fixed-variant: '#004e5f'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 40px
    fontWeight: '700'
    lineHeight: 48px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 34px
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-bold:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
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
  lg: 40px
  xl: 64px
  margin-mobile: 20px
  gutter-mobile: 16px
---

## Brand & Style

This design system is engineered for early childhood cognitive development, balancing high-energy engagement with a structured, academic foundation. The brand personality is "The Playful Laboratory"—a space that feels both infinitely creative and scientifically precise. The target audience includes children aged 3-6 and their parents/educators, requiring a dual-layer emotional response: excitement and curiosity for the child, and trust and clarity for the adult.

The visual style is a hybrid of **Minimalism** and **Tactile/Skeuomorphism**. By stripping away unnecessary decorative clutter (Minimalism), we focus the child's attention on STEM problem-solving tasks. By applying "squishy" physical metaphors to interactive elements (Tactile), we leverage a child's natural urge to touch and manipulate objects, making the digital experience feel like a physical toy kit. High-contrast geometric patterns are used as rhythmic backdrops to reinforce spatial logic.

## Colors

The palette is anchored by "Electric Blue," a high-vibrancy primary shade that signals action and intelligence. This is complemented by "Silver" (Secondary), used primarily for structural borders and metallic accents that give the UI a "high-tech tool" feel. 

- **Electric Blue:** Used for primary actions, progress indicators, and key STEM milestones.
- **White:** The dominant background color to ensure maximum "breathing room" and focus.
- **Silver:** Applied to inactive states, secondary containers, and geometric line-work.
- **Cyan Spark:** A tertiary accent for success states and interactive hints.

The design utilizes high-contrast ratios between Electric Blue and White to ensure elements remain legible for developing eyes and under various lighting conditions common in mobile usage.

## Typography

This design system uses a strategic pairing of two sans-serifs. **Space Grotesk** is used for headlines; its geometric quirks and technical "lab" feel align with the STEM theme while maintaining high readability. **Lexend** is used for all body text and UI labels; specifically designed to reduce visual stress and improve reading proficiency, it is the ideal choice for early learners.

Type scales are generous to accommodate mobile-first interactions. Large headings provide clear signposting, while the body text maintains a rhythmic vertical flow to prevent cognitive overload.

## Layout & Spacing

The layout follows a **fluid grid** model optimized for mobile touch targets. A 4-column grid is used for handheld devices, expanding to 8 columns for tablets. 

The spacing rhythm is based on an 8px baseline. Large internal paddings (24px+) are prioritized to prevent accidental taps, crucial for the 3-6 age demographic. Elements are grouped using generous "islands" of whitespace, ensuring that each problem-solving task is visually isolated from navigation or secondary controls.

## Elevation & Depth

Hierarchy is achieved through a combination of **Tactile Soft Shadows** and **Tonal Layers**. 

1. **The Base:** A flat, clean White or Light Silver surface.
2. **Interactive Elements:** These use a distinctive "pressable" look. A soft, slightly saturated shadow (using a tint of Electric Blue) is cast downwards, suggesting the button is physically raised. When tapped, the shadow disappears and the element shifts 2px down to simulate a physical click.
3. **Containers:** Cards use low-contrast Silver outlines rather than heavy shadows to maintain the "Clean & Modern" aesthetic without feeling cluttered.
4. **Overlays:** Modals use a backdrop blur (Glassmorphism) with 80% opacity to keep the context of the lesson visible while focusing on the specific prompt.

## Shapes

The shape language is strictly **Geometric**. While corners are rounded to ensure a "friendly" and safe feel, they are not fully circular (pill-shaped) to maintain the modern, structured STEM aesthetic. 

Primary buttons and cards use a 16px (rounded-lg) corner radius. Smaller UI elements like chips or input fields use a 8px (base) radius. Abstract geometric patterns—triangles, hexagons, and circles—are used as background watermarks to reinforce the STEM narrative and provide visual texture without distracting from the content.

## Components

- **Tactile Buttons:** Large, high-contrast buttons in Electric Blue. Use a "3D" effect where the bottom border is 4px darker than the surface to invite pressing.
- **Progress Hexagons:** Instead of traditional bars, use a series of geometric hexagons that "fill" with Electric Blue as the child completes tasks.
- **Stem Chips:** Used for categorizing activities (e.g., "Logic," "Math"). These use a Silver background with Electric Blue text and no shadows.
- **Problem Cards:** White containers with a 2px Silver border. They house the primary interaction and should never contain more than one primary action.
- **Interactive Trays:** Bottom-sheet components that slide up for tool selection, using a light Frost/Glassmorphism effect to maintain a sense of space.
- **Instructional Labels:** Large, clear Lexend type on a subtle Silver background to differentiate "Teacher/System" voice from "Play" elements.