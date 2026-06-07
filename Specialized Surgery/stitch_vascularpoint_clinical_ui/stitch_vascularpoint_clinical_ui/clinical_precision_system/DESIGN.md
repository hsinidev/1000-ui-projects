---
name: Clinical Precision System
colors:
  surface: '#f9f9ff'
  surface-dim: '#cfdaf1'
  surface-bright: '#f9f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f0f3ff'
  surface-container: '#e7eeff'
  surface-container-high: '#dee8ff'
  surface-container-highest: '#d8e3fa'
  on-surface: '#111c2c'
  on-surface-variant: '#444653'
  inverse-surface: '#263142'
  inverse-on-surface: '#ebf1ff'
  outline: '#757684'
  outline-variant: '#c5c5d5'
  surface-tint: '#3e54c1'
  primary: '#001360'
  on-primary: '#ffffff'
  primary-container: '#002395'
  on-primary-container: '#8094ff'
  inverse-primary: '#bac3ff'
  secondary: '#5a5f62'
  on-secondary: '#ffffff'
  secondary-container: '#dce0e4'
  on-secondary-container: '#5e6367'
  tertiary: '#440500'
  on-tertiary: '#ffffff'
  tertiary-container: '#6a0f01'
  on-tertiary-container: '#f6765c'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dee1ff'
  primary-fixed-dim: '#bac3ff'
  on-primary-fixed: '#001159'
  on-primary-fixed-variant: '#223aa8'
  secondary-fixed: '#dfe3e7'
  secondary-fixed-dim: '#c3c7cb'
  on-secondary-fixed: '#171c1f'
  on-secondary-fixed-variant: '#43474b'
  tertiary-fixed: '#ffdad3'
  tertiary-fixed-dim: '#ffb4a5'
  on-tertiary-fixed: '#3e0500'
  on-tertiary-fixed-variant: '#852310'
  background: '#f9f9ff'
  on-background: '#111c2c'
  surface-variant: '#d8e3fa'
typography:
  headline-lg:
    fontFamily: Manrope
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Manrope
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Manrope
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-caps:
    fontFamily: Public Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: 16px
    letterSpacing: 0.05em
  data-point:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  gutter: 24px
  margin: 48px
  container-max: 1280px
---

## Brand & Style

This design system is engineered for the high-stakes environment of vascular surgery and circulatory health. The brand personality is rooted in **Clinical Authority** and **Surgical Precision**. It seeks to evoke a sense of absolute reliability, calm under pressure, and advanced technological expertise.

The style is **Modern Corporate** with a heavy emphasis on **Minimalism**. By utilizing expansive white space (the "clean room" effect), the UI eliminates cognitive load for both clinicians and patients. High-resolution medical photography—focused on microscopic precision, diagnostic clarity, and healthy circulation—acts as a secondary pillar of the visual language. Visual elements are sharp and intentional, avoiding decorative flourishes in favor of utilitarian beauty.

## Colors

The palette is anchored by **Royal Blue**, a color associated with institutional trust and venous health. This primary hue is used for critical interactive elements and navigational headers. 

**White** is the structural foundation, representing a sterile, clinical environment. **Soft Red** is utilized sparingly as a functional accent; it signifies medical urgency, arterial flow, or critical alerts without inducing panic. Neutral tones are strictly cool-greys to maintain a professional, high-tech atmosphere, avoiding any "warmth" that might appear unprofessional or muddy in a medical context.

## Typography

The typography system prioritizes legibility in high-stress diagnostic environments. **Manrope** is used for headlines to provide a modern, refined, and balanced character. Its geometric nature reflects the "precision" aspect of the brand.

**Inter** serves as the primary body face due to its exceptional performance in digital interfaces and technical data display. For specialized metadata, such as surgical parameters or patient IDs, **Public Sans** provides an institutional, official tone. Information hierarchy is enforced through generous line heights and a clear distinction between data labels (uppercase) and narrative text.

## Layout & Spacing

This design system employs a **Fixed Grid** model to ensure content remains structured and predictable. A 12-column grid is used for desktop views, with a focus on wide gutters (24px) to prevent visual clutter. 

The spacing rhythm is strictly based on a **4px base unit**. Component internal padding should favor larger increments (16px, 24px, 32px) to maintain the "Clinical & Precise" aesthetic. Alignment is predominantly left-justified to facilitate rapid scanning of medical records and surgical procedures. Large margins (48px+) are required around high-resolution photography to allow the imagery to breathe and serve as a focal point.

## Elevation & Depth

To maintain a sterile and modern feel, this design system avoids heavy shadows. Depth is primarily conveyed through **Tonal Layers** and **Low-Contrast Outlines**.

Surface-on-surface separation is achieved using subtle background shifts (e.g., a Light Grey background with White cards). Where shadows are necessary—such as for floating action buttons or modal overlays—they must be **Ambient Shadows**: extremely diffused, low-opacity (#000000 at 4-8%), with no discernible light source, creating a "lifted" rather than "projected" effect. This keeps the interface looking flat and integrated with the medical hardware it might be displayed on.

## Shapes

The shape language is **Soft (0.25rem)**. This choice strikes a balance between the "sharpness" of surgical instruments and the "approachability" required for patient trust. 

Containers use 4px corners to feel stable and architectural. Interactive elements like buttons and input fields use the same 4px radius. Circles are reserved exclusively for status indicators (pulsing circulation icons) or user avatars. Sharp 0px corners are avoided to prevent the UI from feeling aggressive or dated.

## Components

### Buttons
Primary buttons use the Royal Blue background with white text. They are rectangular with a 4px radius. Secondary buttons use a subtle "Ghost" style with a 1px border in Royal Blue. The "Urgent" button variant utilizes the Soft Red background for critical surgical alerts or emergency calls.

### Cards
Cards are the primary container for patient data and surgical summaries. They feature a 1px Light Grey border and no shadow. The header of the card should be separated by a thin horizontal rule.

### Input Fields
Fields must look "functional." They use a white background with a 1px neutral border that thickens and turns Royal Blue on focus. Labels are always positioned above the field in the `label-caps` style.

### Chips & Status Indicators
Used for "Circulation Status" or "Vascular Risk Level." These use a pill shape to distinguish them from actionable buttons. High-risk indicators use the Soft Red; stable metrics use a muted Royal Blue or Green.

### Medical Data Visualization
Charts and graphs must use thin line weights (1px-2px) and a limited palette of the primary Royal Blue and Soft Red to denote arterial vs. venous data. High-resolution medical photography should be framed in simple 4px rounded containers with clinical captions.