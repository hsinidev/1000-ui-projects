---
name: Aero-Compute
colors:
  surface: '#131315'
  surface-dim: '#131315'
  surface-bright: '#39393b'
  surface-container-lowest: '#0e0e10'
  surface-container-low: '#1b1b1d'
  surface-container: '#1f1f21'
  surface-container-high: '#2a2a2c'
  surface-container-highest: '#353437'
  on-surface: '#e4e2e4'
  on-surface-variant: '#c4c7c9'
  inverse-surface: '#e4e2e4'
  inverse-on-surface: '#303032'
  outline: '#8e9194'
  outline-variant: '#434749'
  surface-tint: '#c1c7cb'
  primary: '#d9dfe3'
  on-primary: '#2b3135'
  primary-container: '#bdc3c7'
  on-primary-container: '#4a5054'
  inverse-primary: '#595f63'
  secondary: '#ffffff'
  on-secondary: '#003828'
  secondary-container: '#36ffc4'
  on-secondary-container: '#007255'
  tertiary: '#e0dde1'
  on-tertiary: '#303033'
  tertiary-container: '#c4c1c5'
  on-tertiary-container: '#504f52'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dde3e7'
  primary-fixed-dim: '#c1c7cb'
  on-primary-fixed: '#161c20'
  on-primary-fixed-variant: '#41484b'
  secondary-fixed: '#36ffc4'
  secondary-fixed-dim: '#00e1ab'
  on-secondary-fixed: '#002116'
  on-secondary-fixed-variant: '#00513c'
  tertiary-fixed: '#e4e1e5'
  tertiary-fixed-dim: '#c8c6ca'
  on-tertiary-fixed: '#1b1b1e'
  on-tertiary-fixed-variant: '#47464a'
  background: '#131315'
  on-background: '#e4e2e4'
  surface-variant: '#353437'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  mono-label:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.1em
  data-point:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
spacing:
  unit: 4px
  gutter: 16px
  margin: 32px
  container-max: 1440px
  grid-columns: '12'
---

## Brand & Style

This design system embodies the "Mechanical-Tech" aesthetic, targeting power users, engineers, and digital architects who demand performance and precision. The brand personality is unapologetically technical, high-performance, and industrial. It avoids soft, consumer-grade aesthetics in favor of a "Workstation-as-an-Instrument" philosophy.

The visual style is a hybrid of **Brutalist structural integrity** and **Tactile Industrialism**. It utilizes hard edges, visible grid structures, and subtle metallic noise textures to evoke the feeling of machined components. The emotional response should be one of absolute reliability, precision engineering, and premium computational power. High-density information displays and functional ornamentation—such as coordinate markers and technical metadata—reinforce the engineering-grade DNA of the system.

## Colors

The palette is rooted in an industrial, high-contrast spectrum.
- **Brushed Steel (Primary):** A range of cool, metallic greys used for primary text, icons, and structural outlines. It represents the raw material of the workstation.
- **Neon Mint (Secondary):** A piercing, high-vibrancy green used exclusively for "Active" states, critical status indicators, and interactive highlights. It represents the energy flowing through the machine.
- **Graphite & Deep Darks (Tertiary/Neutral):** Deep, textured blacks and dark greys form the foundation. These are not flat hex codes but should ideally incorporate a fine grain or subtle noise to mimic bead-blasted metal or carbon fiber.

The interface defaults to a high-contrast dark mode to reduce eye strain during long engineering sessions and to make the Neon Mint accents pop with technical clarity.

## Typography

Typography follows a strict hierarchy designed for readability under high data density.
- **Headlines:** Use **Space Grotesk** for its aggressive, geometric terminals and technical rhythm. It should be used for product titles and major section headers.
- **Interface & Body:** **Inter** is utilized for its exceptional legibility and utilitarian feel. It handles complex data tables and technical specifications with neutral efficiency.
- **Labels & Metadata:** All labels should use the "mono-label" style (Inter Bold, Uppercase, Tracking +10%) to mimic the etched serial numbers found on industrial hardware. 

All numerical data should use tabular lining to ensure columns of figures align perfectly in data-heavy visualizations.

## Layout & Spacing

This design system employs a **Fixed Grid** model based on a 4px baseline shift. All layouts must conform to a 12-column grid with rigid 16px gutters. 

Spacing is intentionally tight to maximize information density, mirroring the control panel of a high-end CNC machine or a flight deck. Elements are grouped into "modules" with 1px Brushed Steel borders. Negative space is used not for "breathability" but as a functional separator to distinguish between distinct data processing streams. Alignment is absolute; no element should exist outside the established grid lines.

## Elevation & Depth

Hierarchy is achieved through **Tonal Layering** and **Bold Borders** rather than traditional shadows. 
- **Tier 1 (Base):** Deepest Graphite background.
- **Tier 2 (Modules/Panels):** Surface grey with 1px solid borders in Brushed Steel.
- **Tier 3 (Active/Pop-outs):** Slightly lighter grey with a subtle 1px inner glow in Neon Mint to indicate focus.

Instead of ambient shadows, use "inset" shadows or "beveled" edges via CSS linear gradients to simulate the physical depth of a recessed metal panel. Backdrop blurs (10px - 20px) may be used for transient overlays (modals) to maintain context while isolating the task.

## Shapes

The shape language is defined by **Zero-Radius Hard Edges**. In this design system, there are no rounded corners. Every button, input field, card, and modal is a sharp-edged rectangle. 

This reinforces the "Industrial/Mechanical" theme, suggesting parts that have been machined from solid blocks of material. For specific call-to-actions, a 45-degree "clipped corner" (chamfer) can be used to indicate a specialized mechanical function, but organic curves are strictly prohibited.

## Components

- **Buttons:** Rectangular with a 1px Brushed Steel border. The "Primary" state fills the border with Neon Mint text and a subtle Neon Mint outer glow on hover. "Danger" states use a high-vis signal orange, but remain strictly rectangular.
- **Chips/Status Tags:** Small, mono-spaced text blocks. For active status, use a "Pulse" dot in Neon Mint next to the label.
- **Inputs:** Dark recessed boxes (inset shadows) with Graphite backgrounds. The cursor and bottom-border activate in Neon Mint upon focus.
- **Data Visualizations:** Line charts should use 1px Neon Mint strokes with no smoothing (stark angles). Grids behind charts should be visible and rendered in a low-opacity Brushed Steel.
- **Cards/Modules:** Used as the primary container. Every card must feature a "Technical Header" containing a title and a pseudo-hexadecimal ID (e.g., `0x-AF44`) in the top right corner.
- **Additional Components:** "Terminal Console" (a dedicated area for real-time system logs), "Telemetry Gauges" (linear progress bars representing CPU/GPU load), and "Grid Overlays" (toggleable layout markers for the user).