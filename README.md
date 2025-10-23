<h3 align="center">👁️‍🗨️ IKIWISI: An Interactive Visual Pattern Generator for Evaluating the Reliability of Vision–Language Models Without Ground Truth</h3>

<p align="center">
  <strong><em>“I Know It When I See It”</em> — a visual, human-centered tool for evaluating the reliability of Vision–Language Models (VLMs) when ground truth is unavailable.</strong>
</p>

<p align="center">
  <a href="https://doi.org/10.1145/3715336.3735754">
    <img src="https://img.shields.io/badge/DIS'25-Funchal%2C%20Portugal-1e90ff?style=flat-square" alt="DIS 2025 Badge">
  </a>
  <img src="https://img.shields.io/badge/%F0%9F%8F%85%20Best%20Paper%20Honorable%20Mention-ff69b4?style=flat-square&logo=acm" alt="Best Paper Honorable Mention">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Python-3.13%2B-blue.svg?style=flat-square" alt="Python 3.13+">
  <img src="https://img.shields.io/badge/Backend-Dash%20%2B%20Plotly-orange.svg?style=flat-square" alt="Backend">
</p>

<p align="center">
  <strong style="color:#ff69b4;">🏅 ACM DIS 2025 — Best Paper Honorable Mention</strong><br>
  <em>Funchal, Portugal · July 2025</em>
</p>

---

<p align="center">
  <img src="assets/ikiwisi_teaser.png" alt="IKIWISI teaser figure" width="800"/>
</p>

<p align="center">
  <em>Figure: The IKIWISI interface enables users to evaluate Vision–Language Models through visual patterns — model and video selection (A–C), keyframes (D), object selection (E), and a binary heatmap (F) that captures presence (green) and absence (red) of objects over time. Users can click to inspect, correct, and rate models interactively.</em>
</p>

---

## Overview

**IKIWISI** (“I Know It When I See It”) is an interactive, human-in-the-loop framework that enables users to *see* how well vision–language models align with human perception.  
By transforming model outputs into binary heatmaps (✅ green = object present, ❌ red = object absent), IKIWISI allows users to visually audit model reliability through intuitive perceptual patterns rather than abstract metrics.

IKIWISI introduces the concept of a **“cognitive audit interface”** — a new paradigm for assessing how closely AI model perception aligns with human commonsense understanding.


---

## Features

| Feature | Description |
|----------|-------------|
| **Binary Heatmaps** | Instantly visualize model predictions across frames and objects. |
| **Spy Objects** | Add intentionally absent (“adversarial”) objects to detect model hallucinations. |
| **Interactive Corrections** | Click any cell to flip predictions and observe emerging reliability patterns. |
| **Model Comparison** | Evaluate BLIP, GPV-1, GPT-4V, Ground Truth, and Random baselines side-by-side. |
| **Accessible Design** | Color-blind mode (white/black), click-to-zoom, and large-text interface. |
| **User Feedback Integration** | Rate model performance and record qualitative insights directly in-app. |



## Quick Start

```bash
# 1️⃣ Clone the repository
git clone https://github.com/yourusername/IKIWISI.git
cd IKIWISI

# 2️⃣ Create and activate the environment
conda create -n ikiwisi python=3.13
conda activate ikiwisi

# 3️⃣ Install dependencies
pip install dash dash-bootstrap-components dash-draggable plotly pandas numpy natsort pillow scikit-learn

# 4️⃣ Launch the app
python dashboard_for_study_v3.py
```

Then open your browser at http://127.0.0.1:8050/
(change the port number as needed)

## Evaluation

IKIWISI was validated through an IRB-approved user study (N = 15) with participants from both AI and non-AI backgrounds.
Key findings:

- Users’ reliability ratings strongly correlated (R² = 0.83 – 0.90) with ground-truth F₁-scores
- Participants reached consistent conclusions after inspecting < 15 % of heatmap cells
- Distinct visual patterns (outliers, uniform rows, checkerboards) shaped user trust and speed of judgment

IKIWISI demonstrates that humans can visually audit model reliability — bridging quantitative evaluation and perceptual understanding.


## Citation

To cite IKIWISI, please use:

```
@inproceedings{islam2025ikiwisi,
  title={IKIWISI: An Interactive Visual Pattern Generator for Evaluating the Reliability of Vision-Language Models Without Ground Truth},
  author={Islam, Md Touhidul and Kabir, Imran and Reza, Md Alimoor and Billah, Syed Masum},
  booktitle={Proceedings of the 2025 ACM Designing Interactive Systems Conference},
  pages={999--1019},
  year={2025}
}
```
