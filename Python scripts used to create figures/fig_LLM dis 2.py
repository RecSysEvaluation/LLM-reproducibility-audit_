import matplotlib.pyplot as plt

counts = {
    "Zero-shot prompting": 35,
    "PEFT (LoRA/adapters)": 31,
    "Embedding generation": 19,
    "Feature extractor": 10,
    "Few-shots prompting": 8,
    "Fine tuning": 6,
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

# ---------- keep Top-K and merge the rest into "Other" ----------
TOP_K = 10
items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
top = items[:TOP_K]
rest = items[TOP_K:]
other_sum = sum(v for _, v in rest)

labels = [k for k, _ in top] + (["Other"] if other_sum > 0 else [])
values = [v for _, v in top] + ([other_sum] if other_sum > 0 else [])

# Shorten labels for single column (avoid wrapping)
short = {
    "PEFT (LoRA/adapters)": "PEFT (LoRA)",
    "Chain of thought prompting": "CoT prompting",
    "Few-shots prompting": "Few-shot prompting",
    "Fine-tunig through prompting": "FT via prompting",
}
labels = [short.get(l, l) for l in labels]

# ---------- plotting tuned for single-column ----------
plt.rcParams.update({
    "font.size": 7,
    "axes.labelsize": 7,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
})

w_in = 3.3
row_h = 0.22
h_in = max(1.8, row_h * len(labels))

fig, ax = plt.subplots(figsize=(w_in, h_in))
bars = ax.barh(labels, values, height=0.6, color = "#1f77b4")

ax.invert_yaxis()
ax.set_xlabel("Number of papers")
ax.grid(axis="x", linestyle="--", linewidth=0.5, alpha=0.5)

# Put numbers INSIDE bars (cleaner than outside in narrow width)
ax.bar_label(bars, padding=1, fontsize=7)
ax.set_xlim(0, max(values) + 5)
# Tight margins for y labels
fig.subplots_adjust(left=0.50, right=0.98, top=0.98, bottom=0.18)

plt.savefig("llm_distribution.pdf", bbox_inches="tight")
plt.show()
