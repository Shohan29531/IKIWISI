# IKIWISI: An Interactive Visual Pattern Generator

> “I Know It When I See It” — a visual, human-centered tool for evaluating the reliability of Vision–Language Models (VLMs) **when ground truth is unavailable**.

[![Conference](https://img.shields.io/badge/DIS'25-Funchal%2C%20Portugal-blue)](https://doi.org/10.1145/3715336.3735754)
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![Python](https://img.shields.io/badge/python-3.13%2B-blue.svg)]()
[![Backend](https://img.shields.io/badge/backend-Dash%20%2B%20Plotly-orange.svg)]()

---

## Overview

**IKIWISI** is an interactive, human-in-the-loop framework that lets users *see* how well vision-language models align with human perception.  
By transforming model outputs into binary heatmaps (✅ green = object present, ❌ red = object absent), IKIWISI allows users to intuitively audit model reliability through visual patterns rather than abstract metrics.

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

---

## System Architecture

| Layer | Technology | Description |
|--------|-------------|-------------|
| **Frontend** | Plotly Dash + Bootstrap | Interactive visualization dashboard |
| **Backend** | Python (multithreaded server) | Handles model orchestration and caching |
| **Supported Models** | GPV-1 • BLIP • GPT-4V • Ground Truth • Random | Easily extensible via dropdown |
| **Hardware (Ref. Implementation)** | AMD EPYC (16-core) • 128 GB RAM • 4× NVIDIA A6000 GPUs | Supports parallel inference |

---

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

# Then open your browser at http://127.0.0.1:8050/
(change the port number as needed)

## Evaluation

IKIWISI was validated through an IRB-approved user study (N = 15) with participants from both AI and non-AI backgrounds.
Key findings:

- Users’ reliability ratings strongly correlated (R² = 0.83 – 0.90) with ground-truth F₁-scores

- Participants reached consistent conclusions after inspecting < 15 % of heatmap cells

- Distinct visual patterns (outliers, uniform rows, checkerboards) shaped user trust and speed of judgment

IKIWISI demonstrates that humans can visually audit model reliability — bridging quantitative evaluation and perceptual understanding.


## Citation

If you use IKIWISI in academic work, please cite:

@inproceedings{islam2025ikiwisi,
  title={IKIWISI: An Interactive Visual Pattern Generator for Evaluating the Reliability of Vision-Language Models Without Ground Truth},
  author={Islam, Md Touhidul and Kabir, Imran and Reza, Md Alimoor and Billah, Syed Masum},
  booktitle={Proceedings of the 2025 ACM Designing Interactive Systems Conference},
  pages={999--1019},
  year={2025}
}
