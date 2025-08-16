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
# 📘 Product Documentation with Marp

- **Author:** Technical Writer  
- **Email:** 24ds2000075@ds.study.iitm.ac.in  
- **Repo:** Markdown-based docs with version control and CI deployment

> Write once, publish everywhere.

---

## 🛠 Why Marp for Technical Docs

- **Single source of truth:** Markdown → HTML, PDF, PPTX  
- **Version-controlled:** Git diffs, pull requests, and history  
- **CI-friendly:** Auto-publish on every push  
- **Customizable:** Themes, directives, and background assets

---

## ✍️ Authoring Guidelines

- Use top-level headings for slide titles  
- Keep bullets concise and scoped per slide  
- Use directives for layout, backgrounds, and styling  
- Apply reusable theme classes like `.card` and `.lead`

---

![bg](assets/bg.jpg)

# 🌌 Scalable Documentation Platform

- **Discoverable:** Reduces support load  
- **Composable:** Embed code, diagrams, and assets  
- **Maintainable:** Treat docs like code

---

## 📐 Algorithmic Complexity Example

For a divide-and-conquer algorithm like **merge sort**:

- **Time complexity:**
  

\[
  T(n) = 2 \cdot T\left(\frac{n}{2}\right) + \Theta(n) \Rightarrow T(n) = \Theta(n \log n)
  \]



- **Space complexity:**
  

\[
  S(n) = \Theta(n)
  \]



Inline notation also works:  
The overall complexity is \( O(n \log n) \).

---

## 🎨 Custom Styling with Marp Directives

<!-- _class: lead -->
# 🎯 Clean Visuals with Theme Classes

- This slide uses `_class: lead` for larger type and simplified background  
- You can also use `.card` for callouts:

<div class="card">
  <strong>Release note:</strong> API v2.3 introduces new endpoints. See migration guide for deprecations.
</div>

---

## 📬 Contact & Collaboration

- **Email:** 24ds2000075@ds.study.iitm.ac.in  
- **Workflow:** Add slides via pull requests → CI builds and deploys

> Documentation is part of the product. Treat it like code.
