# ============================
# 📁 src/slide_generator.py
# Author: Taiwo O. Adetiloye
# ============================

import matplotlib.pyplot as plt


def create_slide(scores: dict, out_path="assets/slide_sample.pdf"):
    plt.figure(figsize=(10, 6))
    plt.title("Candidate Evaluation Summary")

    categories = ["Plausibility", "Technical Proficiency", "Communication"]
    values = [
        scores["plausibility"],
        scores["technical_proficiency"],
        scores["communication"]
    ]

    bars = plt.bar(categories, values)
    plt.ylim(0, 5)

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + 0.25, yval + 0.1, f"{yval}/5")

    plt.savefig(out_path)
    print(f"Slide saved to {out_path}")
