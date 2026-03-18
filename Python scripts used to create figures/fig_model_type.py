import matplotlib.pyplot as plt

# Data
models = [
    "Llama",
    "OpenAI",
    "Mistral",
    "Qwen",
    "DeepSeek",
    "Gemma",
    "Vicuna",
    "T5",
    "P5",
    "ChatGLM",
    "DeBERTa",
    "GRITLM",
    "Falcon",
    "Claude",
    "LLaVA",
    "PaLM",
    "BART",
    "OPT",
    "Phi"
]

counts = [36, 31, 6, 4, 2, 2, 2, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

colors = [
    '#4C78A8',  # Llama         -> open-source
    '#F58518',  # OpenAI        -> closed-source
    '#4C78A8',  # Mistral       -> open-source
    '#4C78A8',  # Qwen          -> open-source
    '#4C78A8',  # DeepSeek      -> open-source
    '#4C78A8',  # Gemma         -> open-source
    '#4C78A8',  # Vicuna        -> open-source
    '#4C78A8',  # T5            -> open-source
    '#4C78A8',  # P5            -> open-source
    '#4C78A8',  # ChatGLM       -> open-source
    '#4C78A8',  # DeBERTa       -> open-source
    '#4C78A8',  # GRITLM        -> open-source
    '#4C78A8',  # Falcon        -> open-source
    '#F58518',  # Claude        -> closed-source
    '#4C78A8',  # LLaVA         -> open-source
    '#F58518',  # PaLM          -> closed-source
    '#4C78A8',  # BART          -> open-source
    '#4C78A8',  # OPT           -> open-source
    '#4C78A8',  # Phi           -> open-source
]

# One-column friendly figure size
fig, ax = plt.subplots(figsize=(3.4, 2.4))  # good for LaTeX one-column

# Bars
bars = ax.bar(models, counts, color = colors, width=0.6)

# Value labels
for bar, value in zip(bars, counts):
    ax.text(
        bar.get_x() + bar.get_width() / 2,
        value + 0.3,
        str(value),
        ha="center",
        va="bottom",
        fontsize=6,
        color="royalblue"
    )

# Axis labels
ax.set_xlabel("Model name", fontsize=8, labelpad=4)
ax.set_ylabel("Number of times used", fontsize=8, labelpad=4)

# Limits and ticks
ax.set_ylim(0, 40)
ax.tick_params(axis='x', labelsize=6, rotation=90)
ax.tick_params(axis='y', labelsize=7)

# Remove grid
ax.grid(False)

# Clean spines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.tight_layout()

# Save for LaTeX
plt.savefig("llm_usuage_names.pdf", bbox_inches="tight")
plt.show()