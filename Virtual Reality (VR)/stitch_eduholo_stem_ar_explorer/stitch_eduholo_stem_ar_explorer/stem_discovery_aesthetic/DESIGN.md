---
name: STEM Discovery Aesthetic
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
  on-surface-variant: '#42493e'
  inverse-surface: '#2e3132'
  inverse-on-surface: '#f0f1f2'
  outline: '#72796e'
  outline-variant: '#c2c9bb'
  surface-tint: '#3b6934'
  primary: '#154212'
  on-primary: '#ffffff'
  primary-container: '#2d5a27'
  on-primary-container: '#9dd090'
  inverse-primary: '#a1d494'
  secondary: '#904d00'
  on-secondary: '#ffffff'
  secondary-container: '#fd8b00'
  on-secondary-container: '#603100'
  tertiary: '#303c34'
  on-tertiary: '#ffffff'
  tertiary-container: '#47534a'
  on-tertiary-container: '#b9c6bb'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#bcf0ae'
  primary-fixed-dim: '#a1d494'
  on-primary-fixed: '#002201'
  on-primary-fixed-variant: '#23501e'
  secondary-fixed: '#ffdcc3'
  secondary-fixed-dim: '#ffb77d'
  on-secondary-fixed: '#2f1500'
  on-secondary-fixed-variant: '#6e3900'
  tertiary-fixed: '#d9e6da'
  tertiary-fixed-dim: '#bdcabe'
  on-tertiary-fixed: '#131e17'
  on-tertiary-fixed-variant: '#3e4a41'
  background: '#f8f9fa'
  on-background: '#191c1d'
  surface-variant: '#e1e3e4'
typography:
  headline-lg:
    fontFamily: Lexend
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
  headline-md:
    fontFamily: Lexend
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
  body-lg:
    fontFamily: Lexend
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Lexend
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  label-md:
    fontFamily: Lexend
    fontSize: 14px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Lexend
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.2'
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
  gutter: 24px
  margin: 32px
---

## Brand & Style

This design system is anchored in the concept of "Guided Discovery." It balances the organic, grounding reliability of nature with the high-energy spark of scientific breakthrough. The target audience spans K-12, requiring a visual language that is sophisticated enough for teenagers yet approachable and tactile for younger children.

The style is **Modern Tactile**. It utilizes clean, minimalist layouts to ensure STEM concepts remain the focus, while incorporating soft-touch UI elements that feel physical and interactive. This approach reduces cognitive load and encourages exploration. The emotional response should be one of "Curiosity and Confidence"—where the UI feels like a helpful, unobtrusive lab assistant rather than a complex piece of software.

## Colors

The palette is rooted in a deep **Forest Green**, symbolizing growth, biology, and the natural world. This is the primary driver for navigation and core structural elements. To provide a necessary energetic contrast for a STEM environment, a **Bright Orange** is used sparingly as an accent for call-to-actions, interactive hotspots, and success states.

The background is a crisp **White**, providing a laboratory-clean canvas that ensures AR overlays are easily distinguishable. A soft, minty tertiary green is used for container backgrounds to soften the interface and prevent visual fatigue during long study sessions.

## Typography

The chosen typeface for this design system is **Lexend**, specifically designed to improve reading proficiency and reduce visual stress. Its rounded terminals and open counters align perfectly with the friendly, educational aesthetic. 

Headlines are weighted heavily to provide a clear path for the eye, while body text maintains generous line height to ensure complex scientific explanations are easy to digest. Label styles utilize a slightly tighter tracking and higher weight to differentiate interactive metadata from static content.

## Layout & Spacing

This design system employs a **Fluid Grid** model with a focus on generous safe zones. Given the AR nature of the application, the layout must account for "heads-up" interaction where the periphery of the screen is primary for controls, leaving the center clear for the camera view.

The spacing rhythm is based on an 8px baseline. Large margins (32px) are used on the outer edges of the display to prevent accidental triggers during handheld use. Content modules are grouped using 24px gutters to maintain a clear visual distinction between different scientific concepts or lesson steps.

## Elevation & Depth

Visual hierarchy is established through **Ambient Shadows** and tonal layering. Rather than using harsh black shadows, this design system uses soft, diffused shadows tinted with the Primary Forest Green at very low opacities (e.g., 8-12%). This creates a "floating" effect that mimics objects resting in a three-dimensional space, which is cognitively consistent with an AR experience.

Interactive elements like cards and buttons utilize a dual-shadow approach: a tight, darker shadow to define the edge, and a wide, soft shadow to provide lift. High-priority modal content uses a semi-transparent backdrop blur to maintain the user's context of the physical environment behind the UI.

## Shapes

The shape language is characterized by **Rounded** geometry. With a standard radius of 0.5rem (8px), the UI feels safe and approachable. Larger containers and cards use a 1rem (16px) radius to emphasize their role as distinct learning modules.

Circular shapes are reserved for avatars, progress indicators, and "Scan" buttons, creating a specific visual vocabulary for "Live AR" actions. This consistent use of curves avoids the clinical coldness of sharp corners, making the STEM content feel like an inviting playground for the mind.

## Components

### Buttons
Primary buttons are solid Forest Green with White text, using a pill-shaped "rounded-xl" profile to invite tapping. Accent buttons for "Hint" or "Energy" actions use Bright Orange.

### Cards
Lesson cards feature a White background with a subtle 1px border in a pale green. They include a soft ambient shadow to lift them from the background. Headers within cards should use the Forest Green color to denote the topic.

### Input Fields
Inputs are clean with a light grey fill and a 2px bottom-border that transforms into a Forest Green border upon focus. Roundedness should match the standard component level (0.5rem).

### Chips & Tags
Used for categorizing subjects (e.g., Physics, Biology). These are semi-transparent versions of the primary color with dark green text, maintaining a "glass-like" appearance that works well over AR backgrounds.

### Progress Bars
Trackers use a thick, rounded track in light mint green with a Forest Green or Orange progress fill, depending on the urgency or completion status.

### AR Overlays
Contextual labels that appear in the camera view should use "Glassmorphism" (backdrop blur) with White text and a simple Orange pointer to link the digital label to the physical object.