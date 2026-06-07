---
name: Sporty-Technical Design System
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
  on-surface-variant: '#b9cacb'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#849495'
  outline-variant: '#3b494b'
  surface-tint: '#00dbe9'
  primary: '#dbfcff'
  on-primary: '#00363a'
  primary-container: '#00f0ff'
  on-primary-container: '#006970'
  inverse-primary: '#006970'
  secondary: '#c8c6c5'
  on-secondary: '#313030'
  secondary-container: '#474746'
  on-secondary-container: '#b7b5b4'
  tertiary: '#f8f5f5'
  on-tertiary: '#303030'
  tertiary-container: '#dbd9d8'
  on-tertiary-container: '#5f5e5e'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#7df4ff'
  primary-fixed-dim: '#00dbe9'
  on-primary-fixed: '#002022'
  on-primary-fixed-variant: '#004f54'
  secondary-fixed: '#e5e2e1'
  secondary-fixed-dim: '#c8c6c5'
  on-secondary-fixed: '#1c1b1b'
  on-secondary-fixed-variant: '#474746'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: '0'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  margin: 1rem
  gutter: 0.75rem
  unit: 4px
  stack-sm: 0.5rem
  stack-md: 1rem
  stack-lg: 2rem
---

## Brand & Style

This design system is engineered for precision, speed, and reliability. It targets high-performance cyclists and professional mechanics who demand a tool that reflects the quality of their gear. The brand personality is methodical and high-velocity, prioritizing functional clarity over decorative elements.

The visual style blends **Minimalism** with **High-Contrast Bold** aesthetics. By utilizing a dark-mode-first approach, the system evokes the feel of carbon fiber, matte-finished frames, and high-end cycling computers. The UI should feel like a specialized diagnostic tool—sparse but powerful, with every element serving a specific mechanical purpose.

## Colors

The palette is anchored in a "Matte Black" ecosystem to minimize glare and maximize contrast in various lighting conditions, such as a brightly lit workshop or outdoor environments. 

- **Primary (Electric Cyan):** Reserved exclusively for active states, primary call-to-actions, and critical diagnostic data. It acts as the "ignition" color.
- **Surface Tiers:** Uses a series of deep grays to create hierarchy without relying on shadows. 
- **Accents:** High-visibility warnings utilize the primary Cyan, while status indicators for "Repair Complete" or "Optimal Health" may utilize the same hue to maintain a unified technical aesthetic.

## Typography

Typography is treated as a technical specification. We use **Space Grotesk** for headlines and labels to provide a geometric, futuristic feel that mirrors engineering blueprints. Its sharp apertures and monolinear construction evoke a sense of digital precision.

**Inter** is utilized for body copy and instructional text. Its neutral, systematic nature ensures high legibility when reading complex repair guides or torque specifications. All labels should lean toward uppercase with increased letter spacing to mimic the industrial stamping found on high-end bicycle components.

## Layout & Spacing

This design system employs a rigid **4-column fluid grid** for mobile, ensuring that all elements align to a strict 4px baseline rhythm. The layout philosophy is "Information Density"—packing data into the screen in a way that feels organized and efficient rather than cluttered.

Margins are kept tight (16px) to maximize the "workspace" on the device. Elements should span 2 or 4 columns to maintain a vertical cadence. Use vertical stacks to separate distinct repair steps or component categories, ensuring that interactive areas meet a minimum 44px hit target despite the dense visual style.

## Elevation & Depth

To maintain the "Sporty-Technical" look, this system avoids soft ambient shadows. Instead, it uses **Tonal Layers** and **Bold Borders** to define depth.

- **Base Layer:** The deepest Matte Black (#0A0A0A).
- **Surface Layer:** Dark Grey (#1A1A1A) for card backgrounds.
- **Technical Borders:** 1px solid borders in #333333 are used to define the edges of containers, mimicking the assembly lines of a bicycle frame.
- **Interactive State:** When an element is focused or active, the border shifts from muted grey to the vibrant Cyan primary color.
- **Subtle Textures:** Use a very faint noise texture or a 45-degree hairline diagonal pattern on background surfaces to evoke the feel of machined alloy or carbon weave.

## Shapes

The shape language is strictly **Sharp (0px)**. Precision engineering rarely utilizes unnecessary curves; therefore, all buttons, input fields, and cards feature hard 90-degree corners. 

In specific instances where "ergonomics" need to be signaled—such as toggle switches or progress bars—a slight chamfer effect can be used, but the overall system should lean into a rectangular, architectural silhouette. This reinforces the "Tool" metaphor and differentiates the app from softer, consumer-grade social products.

## Components

### Buttons
Primary buttons are solid Matte Black with a 2px Cyan border and Cyan uppercase text. Secondary buttons are ghost-style with a muted grey border. On tap, the primary button should invert to a solid Cyan fill with Black text to provide high-contrast tactile feedback.

### Chips & Tags
Used for component categories (e.g., "Drivetrain", "Brakes"). These are small, rectangular boxes with a thin border. Active chips utilize the Cyan accent for both border and text.

### Lists
Lists are separated by 1px horizontal dividers. Each list item should include a "technical chevron"—a sharp, minimal arrow—to indicate drill-down capability.

### Input Fields
Fields are represented as simple boxes with a bottom-only 2px border by default. Upon focus, the border expands to a full 1px box wrap in vibrant Cyan. Labels always sit above the input in "Label-Caps" style.

### Data Cards
Cards for bike stats or repair history should use the #1A1A1A background. Include a small "spec-code" or ID number in the top right corner in a tiny monospace font to enhance the technical feel.

### Additional Components
- **Progress Steppers:** Used for repair workflows, showing a linear path with sharp diamond-shaped nodes.
- **Torque Gauges:** Circular or linear meters using the Cyan accent to show "Applied Pressure" versus "Target Specification."