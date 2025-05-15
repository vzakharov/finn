# Existing Academic Surveys of Neural Memory

## Summary

There **are** several recent surveys covering broad memory-augmented neural architectures and AI long-term memory, but **none** focus narrowly on detachable, persistent memory modules for hidden-state storage (your “artificial hypothalamus”). Key overviews include:

* **MANN Survey (Dec 2023):** A comprehensive look at memory-augmented networks like NTMs, DNCs, Hopfield nets, Memformer, etc. ([arXiv][1])
* **SALM Survey (Nov 2024):** Maps human long-term memory theory to AI, proposing a Self-Adaptive Long-term Memory framework ([arXiv][2])
* **LLM-Era Memory Survey (Apr 2025):** Classifies memory in LLM-driven systems along object/form/time dimensions ([arXiv][3])

However, none zero in on **persistent external modules** that hoard internal representations across sessions—so there’s room for a targeted state-of-the-art review in that niche.

---

## Major Surveys

### 1. Survey on Memory-Augmented Neural Networks

Savya Khosla et al. provide a deep dive into MANN architectures—Neural Turing Machines, Differentiable Neural Computers, Hopfield-style memories, Memformer, and more—linking cognitive memory types (sensory, short-term, long-term) to AI applications in NLP, vision, multimodal learning, and retrieval ([arXiv][1]).

### 2. Human-inspired Perspectives: A Survey on AI Long-term Memory

Zihong He et al. systematically review AI long-term memory through the lens of human episodic, semantic, and procedural memory, then propose the SALM cognitive architecture for adaptive, theory-grounded long-term memory in AI ([arXiv][2]).

### 3. From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs

This very recent arXiv paper classifies LLM memory across three dimensions—object (personal vs system), form (parametric vs non-parametric), and time (short vs long term)—and synthesizes insights on how human memory informs retrieval-augmented generation and persistent user profiling ([arXiv][3]).

---

## Related Overviews

* **Memorization in Deep Learning: A Survey** explores memorization and forgetting across DNNs, highlighting privacy, generalization, and one-shot learning phenomena ([arXiv][4]).
* **Memory-Augmented Graph Neural Networks: A Brain-Inspired Review** catalogs memory modules in GNNs, proposing a taxonomy based on psychology and neuroscience principles ([arXiv][5]).
* **A Short Survey on Memory-Based Reinforcement Learning** reviews RL algorithms that incorporate external memories to improve sample efficiency and decision-making ([arXiv][6]).
* **Metalearned Neural Memory** treats memory as a learnable function, leveraging metalearning to update a neural memory module in one shot ([arXiv][7]).

---

## Gap Analysis & Opportunity

Despite this rich landscape, **no** survey specifically dissects **detachable** memory contours that store **internal representations** (hidden activations) separately from core model weights. Research papers on these modules include:

* **Compressive Transformers**: extend Transformer-XL with two banks (detailed + compressed memories) to archive past activations indefinitely ([arXiv][8]).
* **Differentiable Neural Computers**: marry a controller RNN with a dynamic external memory matrix that can be checkpointed or swapped at will ([Википедия][9]).
* **Long-term Episodic Memory Networks (LEMN)**: employ an RNN-based retention agent to learn which memory entries to keep or evict over unbounded streams ([arXiv][10]).
* **Titans: Learning to Memorize at Test Time**: introduce a plug-in neural memory that adapts its parameters via gradient-based memorization during inference ([arXiv][11]).
* **Retentive Networks**: successor to Transformer architectures that separate short-term attention from a long-term memory branch for extended context ([arXiv][12]).

A **dedicated survey** comparing these modules’ detachability, compression vs fidelity trade-offs, memory management policies, and integration strategies would fill a clear gap and guide future “artificial hypothalamus” designs.

[1]: https://arxiv.org/abs/2312.06141 "Survey on Memory-Augmented Neural Networks: Cognitive Insights to AI Applications"
[2]: https://arxiv.org/html/2411.00489v1 "Human-inspired Perspectives: A Survey on AI Long-term Memory"
[3]: https://arxiv.org/html/2504.15965 "A Survey on Memory Mechanisms in the Era of LLMs - arXiv"
[4]: https://arxiv.org/html/2406.03880v1 "Memorization in deep learning: A survey - arXiv"
[5]: https://arxiv.org/abs/2209.10818 "Memory-Augmented Graph Neural Networks: A Brain-Inspired Review"
[6]: https://arxiv.org/abs/1904.06736 "A Short Survey On Memory Based Reinforcement Learning"
[7]: https://arxiv.org/abs/1907.09720 "Metalearned Neural Memory"
[8]: https://arxiv.org/abs/1911.05507 "Compressive Transformers for Long-Range Sequence Modelling"
[9]: https://en.wikipedia.org/wiki/Differentiable_neural_computer "Differentiable neural computer"
[10]: https://arxiv.org/abs/1812.04227 "Learning What to Remember: Long-term Episodic Memory Networks for Learning from Streaming Data"
[11]: https://arxiv.org/abs/2501.00663 "Titans: Learning to Memorize at Test Time"
[12]: https://arxiv.org/pdf/2502.10297 "[PDF] arXiv:2502.10297v1 [cs.LG] 14 Feb 2025"