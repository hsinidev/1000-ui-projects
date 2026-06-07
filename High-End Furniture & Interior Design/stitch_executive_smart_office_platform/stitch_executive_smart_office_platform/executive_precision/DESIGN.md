---
name: Executive Precision
colors:
  surface: '#121316'
  surface-dim: '#121316'
  surface-bright: '#38393c'
  surface-container-lowest: '#0d0e11'
  surface-container-low: '#1a1c1e'
  surface-container: '#1f2022'
  surface-container-high: '#292a2c'
  surface-container-highest: '#343537'
  on-surface: '#e3e2e5'
  on-surface-variant: '#c4c6cf'
  inverse-surface: '#e3e2e5'
  inverse-on-surface: '#2f3033'
  outline: '#8e9198'
  outline-variant: '#43474e'
  surface-tint: '#afc8f0'
  primary: '#afc8f0'
  on-primary: '#163152'
  primary-container: '#001f3f'
  on-primary-container: '#6f88ad'
  inverse-primary: '#476083'
  secondary: '#c6c6c6'
  on-secondary: '#2f3131'
  secondary-container: '#484949'
  on-secondary-container: '#b8b8b8'
  tertiary: '#c8c6c6'
  on-tertiary: '#303030'
  tertiary-container: '#1f1f1f'
  on-tertiary-container: '#878686'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#d4e3ff'
  primary-fixed-dim: '#afc8f0'
  on-primary-fixed: '#001c3a'
  on-primary-fixed-variant: '#2f486a'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#e4e2e1'
  tertiary-fixed-dim: '#c8c6c6'
  on-tertiary-fixed: '#1b1c1c'
  on-tertiary-fixed-variant: '#474747'
  background: '#121316'
  on-background: '#e3e2e5'
  surface-variant: '#343537'
typography:
  display-lg:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '600'
    lineHeight: '1.1'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '500'
    lineHeight: '1.2'
    letterSpacing: 0.01em
  body-rt:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.6'
    letterSpacing: '0'
  data-mono:
    fontFamily: Space Grotesk
    fontSize: 14px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: Space Grotesk
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.1em
spacing:
  unit: 4px
  container-margin: 32px
  gutter: 16px
  component-padding-x: 12px
  component-padding-y: 8px
---

## Brand & Style

This design system is engineered for high-stakes executive environments where clarity, speed of thought, and professional gravitas are paramount. The brand personality is "Calculated Authority"—it is silent, powerful, and impeccably organized. The target audience consists of C-suite executives and tech professionals who require a frictionless interface that mirrors the quality of high-end hardware.

The visual style is a fusion of **Modern Corporate** and **High-Tech Minimalism**. It avoids decorative flourishes in favor of structural integrity and data density. Surfaces are treated with a metallic sheen, utilizing subtle gradients and razor-sharp edges to evoke the feeling of machined aluminum and deep-sea instrumentation. The emotional response is one of absolute control and understated luxury.

## Colors

The palette is strictly anchored in a dark-mode-first architecture to reduce eye strain during extended deep-work sessions. 

- **Primary (Deep Navy):** Used for structural grounding, primary navigation sidebars, and high-level headers. It represents the "depth" of the intelligence layer.
- **Secondary (Silver):** Reserved for high-contrast information, primary iconography, and interactive states. It provides a tactile, metallic feel.
- **Tertiary (Graphite):** The foundation for secondary surfaces, dividers, and card backgrounds. It creates subtle separation without breaking the dark aesthetic.
- **Background:** A near-black charcoal that allows the Deep Navy and Graphite layers to sit with distinct tonal separation.

## Typography

This design system utilizes two contrasting typefaces to balance technical precision with readability. 

**Space Grotesk** is used for all headlines, labels, and data points. Its geometric construction and idiosyncratic "tech" terminals reinforce the high-performance narrative. Use the uppercase "Label-Caps" style for all small UI headers and button labels to maximize the professional aesthetic.

**Inter** is utilized for all body copy and long-form descriptions. Its neutral, systematic nature ensures that dense operational text remains legible and does not compete with the technical styling of the headlines.

## Layout & Spacing

The layout philosophy follows a **Fixed-Fluid Hybrid Grid**. Core dashboard modules are arranged on a 12-column grid, but inner data visualizations use a contextual "no-grid" approach to allow for maximum information density.

A strict 4px base unit governs all dimensions. Spacing should be tight and efficient—favoring information density over excessive whitespace. Margins are generous at the edges of the screen (32px) to frame the content, while internal component spacing remains compact (8px-16px) to keep related data points within the executive's primary field of vision.

## Elevation & Depth

This design system rejects traditional soft shadows in favor of **Tonal Layers and Metallic Outlines**. 

Depth is achieved through "Stacked Graphite" surfaces. A container sitting "above" the background will not use a shadow; instead, it will use a slightly lighter Graphite hex code and a 1px solid Silver border at 10% opacity. For high-priority active states, use a "Cyan-Pulse" inner glow—a 1px inner stroke that suggests the component is energized and active.

Glassmorphism is used sparingly, only for temporary overlays (modals or dropdowns), with a heavy backdrop blur (20px) and a subtle Navy tint.

## Shapes

The shape language is **Sharp (0px)**. To convey a sense of high-end machinery and architectural precision, all corners are kept at a strict 90-degree angle. This includes buttons, cards, input fields, and the "Liquid Progress Bars."

The only exception to this rule is for status indicators (LED-style dots) which are perfect circles. All other UI elements must maintain a rectilinear profile to reinforce the minimalist, tech-professional aesthetic.

## Components

**Buttons:** Premium treatments include a "machined" effect. Primary buttons use a subtle vertical gradient from Deep Navy to Graphite, with a 1px Silver top-border to simulate a light catch on a physical edge. Text is always uppercase Space Grotesk.

**Liquid Progress Bars:** These represent ranges and quotas. They feature a dark Graphite track and a Silver fill. The fill should have a "shimmer" animation—a subtle 5% opacity highlight that moves horizontally to indicate active data processing.

**Data-Dense Visualizations:** Charts use "Wireframe" styling. Grid lines are 0.5px Silver at 15% opacity. Data points are sharp squares. No curved lines in line charts; use stepped or straight paths only.

**Input Fields:** Ghost-style inputs with no background fill, only a 1px Graphite bottom-border. On focus, the border transitions to Silver with a faint Deep Navy glow beneath the text.

**Executive Cards:** Cards should have a "Header Ribbon"—a 2px vertical Silver line on the far left of the card title to denote the primary focus area. All cards are containers with a #383838 background.