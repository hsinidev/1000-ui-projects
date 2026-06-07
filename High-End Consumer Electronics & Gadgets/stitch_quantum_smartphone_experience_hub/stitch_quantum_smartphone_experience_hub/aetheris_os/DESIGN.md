---
name: Aetheris OS
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#3a3939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#cfc2d9'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#988ca2'
  outline-variant: '#4d4356'
  surface-tint: '#dab9ff'
  primary: '#dab9ff'
  on-primary: '#470083'
  primary-container: '#8f00ff'
  on-primary-container: '#efddff'
  inverse-primary: '#8600ef'
  secondary: '#c6c4db'
  on-secondary: '#2f2f40'
  secondary-container: '#464558'
  on-secondary-container: '#b5b3c9'
  tertiary: '#00dbe9'
  on-tertiary: '#00363a'
  tertiary-container: '#007178'
  on-tertiary-container: '#88f5ff'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#efdbff'
  primary-fixed-dim: '#dab9ff'
  on-primary-fixed: '#2b0053'
  on-primary-fixed-variant: '#6500b8'
  secondary-fixed: '#e3e0f8'
  secondary-fixed-dim: '#c6c4db'
  on-secondary-fixed: '#1a1a2b'
  on-secondary-fixed-variant: '#464558'
  tertiary-fixed: '#7df4ff'
  tertiary-fixed-dim: '#00dbe9'
  on-tertiary-fixed: '#002022'
  on-tertiary-fixed-variant: '#004f54'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  display-xl:
    fontFamily: Space Grotesk
    fontSize: 64px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: 0.05em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.03em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.3'
    letterSpacing: 0.02em
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
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  margin-page: 24px
  gutter: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  safe-area-bottom: 34px
---

## Brand & Style

This design system is engineered for a flagship mobile ecosystem that prioritizes a sense of "technological luxury." The brand personality is cold, precise, and sophisticated, yet energized by vibrant, luminous accents. It targets early adopters and power users who value high-performance hardware and avant-garde aesthetics.

The visual direction is a hybrid of **Glassmorphism** and **High-Tech Minimalism**. It utilizes deep, infinite blacks to melt the software into the physical hardware, while using frosted glass layers to establish a sense of 3D depth. The emotional response is one of total immersion—a "liquid" interface that feels alive through glowing states and smooth, physics-based transitions.

## Colors

The palette is anchored in a true-black environment to maximize the contrast of OLED displays. **Midnight Black** serves as the infinite canvas. **Deep Space Blue** is used for secondary containers and surface elevations, providing a subtle shift away from total black to create structure.

**Electric Violet** is the core functional color, used for primary actions and "active" states. It should always be accompanied by a soft outer glow to simulate light emission. A tertiary **Cyan/Electric Blue** is reserved for high-priority data visualizations or specific system-critical alerts. All translucent surfaces utilize a neutral white stroke at low opacity to define edges without breaking the glass illusion.

## Typography

This design system uses a dual-font approach. **Space Grotesk** handles all headlines and labels, providing a technical, geometric edge that aligns with the "High-Tech" narrative. Headlines must use expanded letter spacing (tracking) to evoke a premium, editorial feel. 

**Inter** is utilized for all body copy and functional data to ensure maximum legibility against dark, translucent backgrounds. It remains neutral and utilitarian, allowing the display typography to command attention. Hierarchy is primarily established through font weight and tracking rather than extreme shifts in scale.

## Layout & Spacing

The layout follows a **Fluid Grid** model optimized for edge-to-edge mobile displays. A 4px base unit drives all spacing decisions, ensuring mathematical harmony. 

Containers and "cards" should span the full width of the margins minus the gutter. Large vertical gaps are encouraged to prevent the high-contrast elements from feeling cluttered. Content groups are separated by generous "breathing room" (stack-lg) to emphasize the minimalist philosophy. All navigation elements must respect the device's hardware safe areas while maintaining a 24px horizontal margin.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism** and z-axis depth rather than traditional shadows.
- **Level 0 (Base):** Midnight Black (#050505).
- **Level 1 (Surface):** Deep Space Blue (#0A0A1A) with 0% transparency.
- **Level 2 (Float):** 20% opacity white fill with a 40px backdrop blur and a 1px semi-transparent white "rim light" stroke.
- **Level 3 (Overlay):** 40% opacity white fill with a 60px backdrop blur, used for modals and system sheets.

Depth is enhanced by "Glowing Accents": primary elements cast an Electric Violet ambient glow onto the surfaces beneath them, simulating a physical light source within the UI.

## Shapes

The design system employs a **Rounded** shape language to soften the high-tech aesthetic and make it feel approachable. Standard containers use a 0.5rem (8px) radius. Larger cards and primary UI surfaces utilize `rounded-xl` (1.5rem / 24px) to mimic the physical corner radius of flagship smartphone hardware. Icons should follow a consistent geometric grid with slightly softened terminals to match the typography.

## Components

### Buttons
- **Primary:** Solid Electric Violet fill with white text. Apply a 15px outer glow (drop shadow) using the primary color at 50% opacity.
- **Secondary:** Frosted glass background (20% white, backdrop blur) with a 1px white border at 10% opacity.

### Navigation Bars
Bottom navigation bars are fully translucent (60px blur) with no solid background. Active states are indicated by a glowing dot beneath the icon and an Electric Violet tint to the icon itself.

### Cards
Cards do not use shadows. They are defined by a subtle 1px border (#FFFFFF at 12% opacity) and a Deep Space Blue background. On tap, cards should scale slightly (0.98x) to simulate physical "press" depth.

### Input Fields
Inputs are minimalist lines or ultra-subtle glass containers. The focus state is indicated by the bottom border or container outline transitioning from dim grey to a vibrant Electric Violet glow.

### Minimalist Iconography
Icons must be "Line-Art" style with a 1.5pt stroke. Use "broken paths" (small gaps in the lines) to create a more technical, schematic look. Active icons should "fill" with a gradient or gain a glow effect.