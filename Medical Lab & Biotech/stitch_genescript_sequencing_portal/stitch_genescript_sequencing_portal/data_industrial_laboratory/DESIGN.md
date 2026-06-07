---
name: Data-Industrial Laboratory
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
  secondary: '#c6c6c7'
  on-secondary: '#2f3131'
  secondary-container: '#454747'
  on-secondary-container: '#b4b5b5'
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
  secondary-fixed: '#e2e2e2'
  secondary-fixed-dim: '#c6c6c7'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#454747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c5'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474746'
  background: '#131313'
  on-background: '#e5e2e1'
  surface-variant: '#353534'
typography:
  headline-xl:
    fontFamily: spaceGrotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: spaceGrotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: 0em
  body-lg:
    fontFamily: inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: 0em
  body-md:
    fontFamily: inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
    letterSpacing: 0.01em
  data-mono:
    fontFamily: inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: spaceGrotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  base: 4px
  unit-x1: 8px
  unit-x2: 16px
  unit-x4: 32px
  unit-x8: 64px
  gutter: 1px
  margin-edge: 24px
---

## Brand & Style
The brand personality is rooted in absolute precision, clinical transparency, and high-throughput efficiency. This design system targets geneticists, bioinformaticians, and lab technicians who require a high-density information environment that remains legible under pressure.

The aesthetic follows a **Data-Industrial** style, blending the structural rigidity of architectural blueprints with the sleekness of modern clinical software. It utilizes a dark-mode-first approach to reduce eye strain during prolonged analysis, punctuated by high-energy accents that simulate the glow of laboratory equipment and digital sequencing readouts. The emotional response is one of total reliability and surgical accuracy.

## Colors
The palette is hyper-focused on contrast and functionality. **Deep Charcoal (#121212)** serves as the monolithic foundation, representing the void of raw data. **DNA Helix-Cyan (#00F0FF)** is the active primary agent, used exclusively for interactive states, data highlights, and successful sequence matches. **Pure White (#FFFFFF)** provides high-contrast legibility for critical findings. 

A supplementary **Industrial Grey (#2A2A2A)** is used for grid lines and structural containers to create a sense of mechanical depth without the use of soft shadows.

## Typography
Typography is treated as a technical instrument. **Space Grotesk** is utilized for headlines and structural labels to provide a geometric, futuristic edge that mirrors scientific nomenclature. **Inter** is the workhorse for all body copy and data tables, chosen for its exceptional legibility and neutral tone.

For genomic sequences and technical values, this design system emphasizes a tabular-numeric setting in Inter, ensuring that long strings of ACGT bases align perfectly in columns for manual inspection and comparison.

## Layout & Spacing
The layout is governed by a **fixed-modular grid** that resembles a laboratory bench or a microplate. Elements are separated by 1px "gutters" that act as hairline borders, creating a clear sense of compartmentalization.

The rhythm is strictly based on a 4px baseline, ensuring that every data cell, button, and terminal readout aligns to a rigorous technical standard. White space is not "empty" but is instead filled with a subtle dot-grid pattern (opacity 5%) to maintain the feeling of a drafting workspace.

## Elevation & Depth
In this design system, depth is achieved through **Tonal Layering** and **Low-contrast Outlines** rather than organic shadows. 

The primary canvas is the darkest value. Active workspaces sit one tier higher (#1A1A1A). Modals or overlays are defined by a sharp 1px border in Cyan or White with a backdrop blur to simulate a glass interface on a backlit console. No soft drop shadows are allowed; if an element needs to feel elevated, it should use a subtle outer glow of the primary Cyan to suggest light emission from a high-tech screen.

## Shapes
The shape language is strictly **Sharp (0px)**. Every UI element—from buttons and input fields to cards and sequence blocks—features 90-degree angles. This reinforces the clinical, industrial nature of the laboratory environment and facilitates the tight, grid-based packing of complex genomic data.

## Components
- **Buttons:** Rectangular with a 1px stroke. Primary buttons are solid Cyan with Black text. Secondary buttons are Black with a White stroke and White text. Hover states trigger a subtle "flicker" effect or a weight increase in the stroke.
- **Inputs:** Technical fields with a 1px bottom border only, turning into a full box on focus. Micro-labels are always present in the top-left in uppercase Space Grotesk.
- **Data Chips:** Small, high-contrast badges for "Pathogenic," "Benign," or "Variant." These use saturated background colors with black text for instant identification.
- **Sequence Viewers:** Horizontal scrolling containers using monospaced Inter, featuring a 1px vertical scanning line that moves with the cursor.
- **Charts:** Linework-only. No fills. Sparklines use the primary Cyan, while axis lines use 1px White strokes at 20% opacity.
- **Cards:** Minimalist containers defined by 1px borders (#2A2A2A). Titles are always separated by a horizontal rule.