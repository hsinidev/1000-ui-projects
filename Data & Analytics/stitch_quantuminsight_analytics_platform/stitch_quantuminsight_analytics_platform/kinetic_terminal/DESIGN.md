---
name: Kinetic Terminal
colors:
  surface: '#0b141c'
  surface-dim: '#0b141c'
  surface-bright: '#313a43'
  surface-container-lowest: '#060f16'
  surface-container-low: '#141c24'
  surface-container: '#182028'
  surface-container-high: '#222b33'
  surface-container-highest: '#2d363e'
  on-surface: '#dae3ee'
  on-surface-variant: '#c6c6cd'
  inverse-surface: '#dae3ee'
  inverse-on-surface: '#29313a'
  outline: '#8f9097'
  outline-variant: '#45474c'
  surface-tint: '#bec6dc'
  primary: '#bec6dc'
  on-primary: '#283041'
  primary-container: '#020817'
  on-primary-container: '#71798c'
  inverse-primary: '#565e71'
  secondary: '#f5fff4'
  on-secondary: '#00391f'
  secondary-container: '#11ffa0'
  on-secondary-container: '#007144'
  tertiary: '#c1c7d1'
  on-tertiary: '#2b3139'
  tertiary-container: '#040910'
  on-tertiary-container: '#737982'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#dbe2f8'
  primary-fixed-dim: '#bec6dc'
  on-primary-fixed: '#131c2b'
  on-primary-fixed-variant: '#3f4758'
  secondary-fixed: '#55ffa9'
  secondary-fixed-dim: '#00e38d'
  on-secondary-fixed: '#002110'
  on-secondary-fixed-variant: '#005230'
  tertiary-fixed: '#dde3ed'
  tertiary-fixed-dim: '#c1c7d1'
  on-tertiary-fixed: '#161c23'
  on-tertiary-fixed-variant: '#414750'
  background: '#0b141c'
  on-background: '#dae3ee'
  surface-variant: '#2d363e'
typography:
  h1:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  h2:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  data-display:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.05em
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 12px
    fontWeight: '600'
    lineHeight: '1.0'
    letterSpacing: 0.1em
  mono-data:
    fontFamily: monospace
    fontSize: 13px
    fontWeight: '400'
    lineHeight: '1.4'
spacing:
  unit: 4px
  gutter: 12px
  margin: 24px
  panel-padding: 16px
  density-compact: 8px
---

## Brand & Style

This design system is engineered for high-stakes analytical environments, evoking the precision and urgency of a global command center. The aesthetic leans heavily into **Technical Minimalism**, prioritizing information density over decorative whitespace. 

The visual language communicates authority and surgical accuracy. Every pixel serves a functional purpose, utilizing a "glass-box" logic where the underlying structure of the data platform is visible through crisp borders and modular arrangements. The emotional response is one of total control, transforming complex big data into a navigable, high-contrast landscape.

## Colors

The palette is anchored by **Midnight Blue** (#020817), providing a deep, non-reflective base that minimizes eye strain during prolonged monitoring sessions. **Graphite** (#2D333B) is utilized for surface layering and structural borders, creating a clear hierarchy of panels without relying on shadows.

**Neon Mint** (#00FF9F) serves as the primary action and data highlight color. Its high luminosity against the dark base ensures that critical alerts, data peaks, and active states are immediately identifiable. Neutral tones are kept cool-indexed to maintain the technical, "cold" atmosphere of a high-end data terminal.

## Typography

Typography in this design system differentiates between "Interface UI" and "Data Output." **Inter** is used for the functional UI—navigation, body text, and settings—providing a neutral, highly readable foundation. 

**Space Grotesk** is applied to headlines and labels to inject a technical, futuristic character. Its geometric construction mimics technical drafting. For high-density data tables and terminal outputs, a standard system monospaced font is used to ensure character alignment, critical for comparing numerical values across rows. All labels should lean toward uppercase with increased letter spacing to enhance the "instrument panel" feel.

## Layout & Spacing

The layout utilizes a **12-column Fluid Grid** designed for maximum screen real estate utilization. Unlike consumer apps, this design system minimizes margins to allow for multi-dashboard viewing. 

A strict 4px baseline rhythm governs all components. Information density is categorized as "High," meaning gutters are kept narrow (12px) to allow disparate data points to feel interconnected. Components should be grouped into logical "Modules" or "Cells" that can snap to the grid, creating a seamless, interlocking panel system reminiscent of a mission control deck.

## Elevation & Depth

This design system rejects shadows and soft blurs. Depth is achieved through **Tonal Layering** and **Crisp Borders**. The background is the lowest level; panels and data cards are represented by Graphite surfaces (#2D333B). 

To indicate elevation or focus, use a 1px solid border. Active or "hovered" states are indicated by changing the border color to Neon Mint or adding a subtle inner glow. High-priority information panels can use a semi-transparent Midnight Blue background with a higher opacity Graphite border to create a "glass-on-metal" look without the use of traditional elevation shadows.

## Shapes

The shape language is strictly **Sharp (0px)**. Right angles emphasize the grid-based, mathematical nature of big data visualization. 

All buttons, inputs, data cards, and decorative elements must feature hard corners. This creates a rigorous, industrial aesthetic that reinforces the brand's focus on precision. The only exception to this rule is for circular data points in visualizations (e.g., scatter plots) to ensure they remain distinguishable from the structural UI.

## Components

### Buttons
Buttons are rectangular with 1px Graphite borders. The "Primary" state features a Neon Mint border and text. On hover, the button gains a subtle Neon Mint outer stroke (0.5px) to simulate a "powered-on" effect.

### Data Chips
Small, high-contrast badges used for status or tags. They utilize a dark fill with Neon Mint text and borders. Use monospaced type for numeric chips.

### Grid Lists
Tables and lists are the core of the system. Rows are separated by 1px Graphite lines. Alternate rows can use a slightly lighter Midnight Blue tint for readability. Headers must be in all-caps Space Grotesk.

### Inputs
Terminal-style input fields with a blinking underscore cursor. The active input state is indicated by a Neon Mint bottom border. 

### Data Cards
Modular containers for charts. Each card must have a visible title bar with a monospaced "ID" or "Timestamp" in the top right corner. Neon data visualizations (lines, bars, or nodes) should glow slightly against the dark background to simulate a light-emitting display.

### Navigation
Vertical sidebars using icon-only or icon+label configurations. Active icons are rendered in Neon Mint; inactive icons are Graphite.