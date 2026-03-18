import matplotlib.pyplot as plt
counts = {
    "Zero-shot prompting": 35,
    "PEFT (LoRA/adapters)": 31,
    "Embedding generation": 19,
    "Feature extractor": 10,
    "Few-shots prompting": 8,
    "Fine tuning (FT)": 6,
    "Explainer": 5,
    "One-shot prompting": 4,
    "Chain of thought prompting": 4,
    "Data augmentation": 3,
    "Reranker": 3,
    "Instruction prompting": 2,
    "Evaluator": 2,
    "Summarizer": 2,
    "Fine-tunig through prompting": 1,
    "QA-style prompting": 1,
    "RL policy learner": 1,
}

# Sort
items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
labels = [k for k, _ in items]
values = [v for _, v in items]

# Shorten labels (DO NOT wrap in single column)
short = {
    "PEFT (LoRA/adapters)": "PEFT (LoRA)",
    "Chain of thought prompting": "CoT prompting",
    "Few-shots prompting": "Few-shot prompting",
    "Fine-tunig through prompting": "FT via prompting",
    "QA-style prompting": "QA prompting",
}
labels = [short.get(l, l) for l in labels]

plt.rcParams.update({
    "font.size": 7,
    "axes.labelsize": 7,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
})

w_in = 3.3
row_h = 0.25          # make it taller so rows don't collide
h_in = max(2.4, row_h * len(labels))

fig, ax = plt.subplots(figsize=(w_in, h_in))
bars = ax.barh(labels, values, height=0.55)

ax.invert_yaxis()
ax.set_xlabel("Number of papers (multi-label)")
ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.5)

# Put values inside (less clutter)
ax.bar_label(bars, padding=1, fontsize=7)

# Critical: give space for y labels (this is what usually fixes "messy")
fig.subplots_adjust(left=0.55, right=0.98, top=0.99, bottom=0.12)

plt.savefig("llm_usage_single_column_all.pdf", bbox_inches="tight")
plt.savefig("llm_usage_single_column_all.png", dpi=300, bbox_inches="tight")
plt.show()







