---
name: Neuro-Flow
colors:
  surface: '#131313'
  surface-dim: '#131313'
  surface-bright: '#393939'
  surface-container-lowest: '#0e0e0e'
  surface-container-low: '#1c1b1b'
  surface-container: '#201f1f'
  surface-container-high: '#2a2a2a'
  surface-container-highest: '#353534'
  on-surface: '#e5e2e1'
  on-surface-variant: '#c3c9b2'
  inverse-surface: '#e5e2e1'
  inverse-on-surface: '#313030'
  outline: '#8d937e'
  outline-variant: '#434938'
  surface-tint: '#a4d64c'
  primary: '#fefff1'
  on-primary: '#233600'
  primary-container: '#bef264'
  on-primary-container: '#4b6e00'
  inverse-primary: '#476800'
  secondary: '#c2c2f2'
  on-secondary: '#2b2d53'
  secondary-container: '#44456e'
  on-secondary-container: '#b4b4e4'
  tertiary: '#fffdff'
  on-tertiary: '#1d00a5'
  tertiary-container: '#e1deff'
  on-tertiary-container: '#534ae9'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#bff365'
  primary-fixed-dim: '#a4d64c'
  on-primary-fixed: '#131f00'
  on-primary-fixed-variant: '#354e00'
  secondary-fixed: '#e1e0ff'
  secondary-fixed-dim: '#c2c2f2'
  on-secondary-fixed: '#16173d'
  on-secondary-fixed-variant: '#42436b'
  tertiary-fixed: '#e2dfff'
  tertiary-fixed-dim: '#c3c0ff'
  on-tertiary-fixed: '#0f0069'
  on-tertiary-fixed-variant: '#3323cc'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  h1:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  data-lg:
    fontFamily: JetBrains Mono
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.02em
  body:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0.01em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 16px
  margin: 32px
---

## Brand & Style

This design system establishes a visual language at the intersection of advanced neuro-science and high-performance engineering. It is characterized by a "Cyber-Biological" aesthetic—where the raw data of the human mind meets the precision of a high-tech interface. 

The primary design style is **Glassmorphism**, utilized to create a sense of depth and focus, mirroring the layers of the human brain. The environment is dark and immersive, allowing high-contrast data visualizations and "Neural-Path" glowing elements to guide the user's eye. The emotional response should be one of clinical confidence and futuristic empowerment; the user is not just viewing data, they are monitoring a biological machine.

## Colors

The palette is anchored in **Matte Black (#121212)** to provide a void-like canvas that minimizes ocular strain during long-term monitoring. **Deep Indigo (#1A1B41)** serves as the secondary structural color, used for surfaces and containers to create a sense of atmospheric depth.

**Mint (#BEF264)** is the high-voltage primary color. It represents "signal" and "activity." It should be used for active states, data peaks, and primary call-to-actions. All primary elements should feature a subtle 5-10px outer glow (drop-shadow) of the same color to simulate the luminosity of bio-electric signals. Functional accents include a clinical red for critical data spikes and a soft blue for background processing states.

## Typography

Typography is split between human-centric readability and machine-readable precision. 

**Inter** is the primary typeface for all UI labels, headings, and instructional copy. It provides a grounded, professional feel that balances the futuristic visuals. 

**JetBrains Mono** is reserved for telemetry, EEG data streams, time-stamps, and any technical metadata. This monospaced font conveys the feeling of a real-time terminal and ensures that shifting numerical values do not cause layout jumps. Headlines should be tight and bold, while data labels should use increased letter spacing to enhance legibility in low-light environments.

## Layout & Spacing

The layout follows a **12-column fluid grid system** optimized for high-density data visualization. The spacing philosophy is modular, built on a 4px base unit to ensure alignment of technical components.

Margins and gutters are kept relatively tight (16px - 24px) to maximize the screen real estate for 3D brain models and multi-channel waveform displays. Larger 40px gaps are used only to separate major cognitive domains (e.g., separating live monitoring from historical analysis). Components should use consistent internal padding (16px) to maintain a cohesive structural rhythm across the dashboard.

## Elevation & Depth

Hierarchy is achieved through **Glassmorphism and Tonal Layering** rather than traditional shadows.

1.  **Background (Level 0):** Pure Matte Black.
2.  **Surface (Level 1):** Semi-transparent Deep Indigo (opacity 40%) with a 16px backdrop-blur. 
3.  **Active Surface (Level 2):** Semi-transparent Deep Indigo (opacity 60%) with a subtle 1px border using a 20% opacity Mint stroke.

"Neural-Path" animations should be implemented as SVG paths with CSS `filter: blur()` and `drop-shadow()` to create a sense of glowing energy moving through the layers. Depth is emphasized by the 3D Brain model which sits behind the translucent UI panels, creating a "Head-Up Display" (HUD) effect.

## Shapes

The shape language is **Precision Geometric**. Elements use a "Soft" (0.25rem) base radius to avoid the clinical harshness of 0px corners while maintaining a professional, technical edge. 

Interactive elements like buttons and chips use a higher radius for distinct identification, but never reach full pill-shape. Sliders and progress bars should have square ends to emphasize the "block-based" nature of technical data processing. Translucent cards should feature a consistent 1px stroke to define their boundaries against the dark background.

## Components

### Buttons & Inputs
*   **Primary Action:** Solid Mint (#BEF264) background with Matte Black text. Features a 10px outer glow on hover.
*   **Ghost Action:** 1px Mint stroke, transparent background, Mint text.
*   **Inputs:** Dark indigo background, 1px stroke that turns solid Mint upon focus. Use JetBrains Mono for all typed input.

### Translucent Cards
*   All data containers must use a backdrop-filter (blur 16px) and a semi-transparent Deep Indigo fill. 
*   Headers within cards should have a 1px bottom border of 10% white to separate metadata from the content.

### Data Visualizations
*   **Waveforms:** Use thin (1.5pt) Mint lines.
*   **Status Chips:** Small, rectangular labels with uppercase JetBrains Mono text. Example: `[SIGNAL: OPTIMAL]` in Mint or `[SYNC: LOSS]` in Red.
*   **Neural-Paths:** Animated glowing lines that connect related data points across different cards, simulating synaptic connections.

### 3D Perspective Brain
*   A centralized, rotatable 3D model. UI overlays should appear to float "in front" of the model using CSS perspective or Z-index layering to reinforce the HUD aesthetic.