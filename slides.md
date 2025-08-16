---
marp: true
theme: iitm
themeSet:
  - ./theme-iitm.css
size: 16:9
paginate: true
footer: "Page $slide / $total • © 2025"
math: mathjax
---

<!-- _class: lead -->
# Product documentation as code with Marp

- **Author:** Technical Writer  
- **Email:** 24ds2000075@ds.study.iitm.ac.in  
- **Repo:** Version-controlled Markdown → export to HTML/PDF/PPTX

> Document once, ship everywhere.

---

## Why Marp for product docs

- **Single source:** Author in Markdown; render to multiple formats.
- **Versioning:** Review changes via Git diffs and PRs.
- **Automation:** CI can publish HTML/PDF on every release.
- **Styling:** Custom theme for consistent brand look.

---

## Authoring conventions

- **Structure:** Use top-level headings for slide titles; concise bullets.
- **Directives:** Per-slide YAML directives configure backgrounds, classes, and layout.
- **Reusable styles:** Theme class names (e.g., `.card`, `.lead`) keep slides consistent.

> Tip: Keep each concept scoped to one slide.

---

<!-- _background: 'data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900"><rect width="100%" height="100%" fill="%230b1020"/><circle cx="80%" cy="10%" r="400" fill="%2314203b"/></svg>' -->

# A platform that scales with your product

- **Trusted:** Clear, discoverable docs reduce support load.
- **Composable:** Embed code, diagrams, and assets.

---

## Algorithmic complexity (example)

For a divide-and-conquer routine like merge sort:

- **Time:**  
  

\[
  T(n) = 2\,T\!\left(\frac{n}{2}\right) + \Theta(n) \Rightarrow T(n) = \Theta(n \log n)
  \]



- **Space:**  
  

\[
  S(n) = \Theta(n)
  \]



Inline notation still works: overall complexity is \(O(n \log n)\).

---

## Custom styling via directives

<!-- _class: lead -->
# Clean, consistent visuals

- **Slide class:**  
  This slide uses `_class: lead` to apply larger type and a simplified background.

- **Card component:**
  <div class="card">
    <strong>Release note:</strong> New API endpoints are GA in v2.3. See migration guide for deprecations.
  </div>

---

## Contact

- **Questions:** 24ds2000075@ds.study.iitm.ac.in
- **Hand-off:** Add new slides in PRs; CI will rebuild artifacts.

> Docs are part of the product—treat them like code. 
