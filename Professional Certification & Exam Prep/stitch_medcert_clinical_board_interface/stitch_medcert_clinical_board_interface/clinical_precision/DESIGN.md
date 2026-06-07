---
name: Clinical Precision
colors:
  surface: '#f9f9f9'
  surface-dim: '#dadada'
  surface-bright: '#f9f9f9'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f3f3f4'
  surface-container: '#eeeeee'
  surface-container-high: '#e8e8e8'
  surface-container-highest: '#e2e2e2'
  on-surface: '#1a1c1c'
  on-surface-variant: '#3f4848'
  inverse-surface: '#2f3131'
  inverse-on-surface: '#f0f1f1'
  outline: '#6f7978'
  outline-variant: '#bfc8c8'
  surface-tint: '#296767'
  primary: '#003434'
  on-primary: '#ffffff'
  primary-container: '#004d4d'
  on-primary-container: '#80bdbc'
  inverse-primary: '#94d1d1'
  secondary: '#5d5e5f'
  on-secondary: '#ffffff'
  secondary-container: '#e0dfdf'
  on-secondary-container: '#626363'
  tertiary: '#0d3333'
  on-tertiary: '#ffffff'
  tertiary-container: '#264a4a'
  on-tertiary-container: '#93b9b8'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#b0eeed'
  primary-fixed-dim: '#94d1d1'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#044f4f'
  secondary-fixed: '#e3e2e2'
  secondary-fixed-dim: '#c6c6c6'
  on-secondary-fixed: '#1a1c1c'
  on-secondary-fixed-variant: '#464747'
  tertiary-fixed: '#c3eae9'
  tertiary-fixed-dim: '#a8cecd'
  on-tertiary-fixed: '#002020'
  on-tertiary-fixed-variant: '#294d4c'
  background: '#f9f9f9'
  on-background: '#1a1c1c'
  surface-variant: '#e2e2e2'
typography:
  h1:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  h2:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  h3:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: '1.4'
    letterSpacing: '0'
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
    lineHeight: '1.6'
    letterSpacing: '0'
  label-caps:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1.0'
    letterSpacing: 0.05em
  caption:
    fontFamily: Inter
    fontSize: 13px
    fontWeight: '500'
    lineHeight: '1.4'
    letterSpacing: '0'
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 8px
  container-max: 1280px
  gutter: 24px
  margin: 32px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
  section-gap: 64px
---

## Brand & Style

The design system is engineered for high-stakes medical education, specifically targeting USMLE candidates and medical students. The brand personality is **Authoritative, Clinical, and Precise**. It mimics the sterile, high-trust environment of a modern hospital or a laboratory, stripping away extraneous ornamentation to focus entirely on cognitive retention and data clarity.

The chosen style is a blend of **Minimalism** and **Corporate/Modern**. It utilizes vast amounts of sterile whitespace to reduce "exam fatigue" and cognitive load during intensive study sessions. Every pixel serves a functional purpose; there is no decoration without intent. The emotional response should be one of calm confidence, ensuring the user feels the platform is an official, peer-reviewed source of truth.

## Colors

The palette is strictly limited to maintain a clinical atmosphere. **Sterile White (#FFFFFF)** serves as the primary canvas, ensuring maximum contrast for text. **Deep Teal (#004D4D)** is used as the primary brand color for action items, headers, and authoritative elements, signaling professional medical expertise.

**Silver (#C0C0C0)** is utilized for structural elements like borders, dividers, and inactive states, providing a metallic, "instrument-like" feel. For data visualization and status feedback, a high-contrast logic is applied: Deep Teal for standard data, a slightly more vibrant Teal for interactive chart elements, and highly specific red/green tones for medical "correct/incorrect" feedback that meet AAA accessibility standards.

## Typography

The design system utilizes **Inter** exclusively to ensure a systematic, utilitarian aesthetic. Inter was selected for its exceptional legibility at small sizes and its neutral character, which does not distract from complex medical terminology.

The typographic hierarchy is strictly enforced to organize dense medical information. Headlines use tighter letter spacing and heavier weights to anchor sections. Body copy uses a generous 1.6 line-height to facilitate long-form reading and minimize eye strain during 4-8 hour study blocks. Labels for medical diagrams and data charts utilize a bold, uppercase style to differentiate instructional text from clinical content.

## Layout & Spacing

This design system employs a **Fixed Grid** model for desktop study environments to ensure that line lengths for medical texts remain within the optimal 60-80 character range. A 12-column grid is used, with a focus on centered content blocks that prevent peripheral eye-strain.

The spacing rhythm is based on an **8px base unit**, reflecting the precision of a medical ruler. Horizontal spacing (gutters) is kept wide at 24px to ensure distinct separation between complex data tables and interactive logic trees. Margins are generous, creating a "breathable" clinical environment that keeps the user focused on the central learning task.

## Elevation & Depth

To maintain a "Clinical & Precise" aesthetic, the design system avoids heavy shadows or organic blurs. Instead, it uses **Low-Contrast Outlines** and **Tonal Layers**. 

Depth is communicated through 1px Silver (#C0C0C0) borders and subtle background shifts. Surfaces are either "Flat" (the main Sterile White background) or "Inset" (used for medical illustration containers and code blocks). When an element must appear elevated, such as a modal or a floating action button, it uses a sharp, high-opacity 2px border or a minimal 4px shadow with zero blur to maintain a "hard" technical feel.

## Shapes

The shape language is **Soft (0.25rem)**. This provides a professional, modern finish without the clinical coldness of perfectly sharp corners or the playfulness of overly rounded pills. 

This subtle rounding is applied to all primary containers, interactive buttons, and input fields. Medical illustration containers and logic tree nodes follow this same rule, creating a cohesive visual language that feels like a refined piece of medical software. Larger layout containers (like the main content card) utilize `rounded-lg` (0.5rem) to provide a structural frame for the information.

## Components

### Buttons & Inputs
Buttons are high-contrast, using Deep Teal for primary actions and Silver borders with White backgrounds for secondary actions. Inputs use 1px Silver borders that transition to Deep Teal on focus, emphasizing precision and active state.

### High-Contrast Data Charts
Charts utilize the Teal spectrum against a White background. Grid lines are thin Silver (#C0C0C0). Data points are sharp and distinct, prioritizing accuracy over aesthetics. No gradients are used in data representation.

### Medical Illustration Containers
Standardized frames for anatomical or pathological images. These containers include a Silver header bar with a "label-caps" font for the figure name and a 1px border.

### Interactive Logic Trees
Used for diagnostic algorithms. Each node is a "Soft" rounded container. Connection lines are 2px Deep Teal with directional arrows. "Yes/No" paths are marked with high-contrast labels to ensure the decision path is unmistakable.

### Logic & Evidence Cards
Specialized containers for "Explanation" and "Key Findings." These use a subtle background fill (#F4F4F4) to separate supplementary evidence from the main question stem, keeping the hierarchy of information clear.