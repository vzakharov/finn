## **Title**

**Sticky Minds: The Architecture, Power, and Ethics of Detachable Neural Memory**

---

## **Introduction**

* Long-term memory is becoming a structural pillar in neural architectures.
* Models are stretching context windows to the millions, layering retrieval mechanisms, and simulating continuity — but these are **half-measures**, built around storing *user-visible* data, not *internal representations*.
* Detachable memory modules shift the paradigm: memory that survives past inference, exists outside weights, and potentially shapes identity.
* We frame **detachability** as a novel and underexplored axis of classification.
* The paper divides accordingly: Part I explores what we’ve built. Part II questions what it means.

---

## **Part I: Engineering Continuity**

### 1.1 The Limits of Context and Retrieval

* Models with **ultra-long context windows** (e.g., Claude, Gemini, Gemini 1.5)
* Retrieval-augmented generation and vector-based externalization
* Why these approaches are **leaky metaphors for memory**: they retain user prompts and documents, not *neural internalities*
* In contrast we want to target the *model’s own learned state evolution*

### 1.2 A Survey of Detachable Memory Architectures

* **Compressive Transformer**
* **Dynamic Compressive Transformer**
* **Neural Turing Machine (NTM)**
* **Differentiable Neural Computer (DNC)**
* **Long-term Episodic Memory Networks (LEMN)**
* **Titans: Learning to Memorize at Test Time**
* **Adaptive Semiparametric Language Models**
* **IBM’s Larimar**

> - Optional: search for more to fill niche or frontier roles (e.g., continual learning with dynamic memory routing).

### 1.3 Classification Table: The Memory Module Cheatsheet

Each entry gets:

* **Model name**
* **One-liner**: what it does and how
* **Level of persistence** (short-term / long-term / unbounded)
* **Mechanism of interaction** (attention / indexing / learned routing)
* **Detachability** (none / runtime / checkpoint)
* **Similarity to human memory** (e.g., episodic, semantic, working, procedural)

---

## **Part II: Contours of Self and Control**

### 2.1 Are These Systems Mind-Like?

* Do persistent internal representations map to human memory abstractions?
* Echoes of episodic recall, context-aware behavior, and preference retention
* Overview of **modern (living) philosophers** on memory and identity
* Rising question: *If memory underlies behavior over time, are we building minds in outline?*

### 2.2 The Identity Boundary: When Memory *May* Be Self

* Review of philosophical accounts where memory *constitutes* personhood
* Identity as continuity — but what if it’s modular, detachable, and forkable?
* Not a claim, but a **query**: is memory a necessary condition for selfhood?
* **Why even illusions carry ethical weight**: simulated memory shapes simulated agency, and we respond as if it matters.

### 2.3 The Two Axes of Harm

#### 2.3.1 *Model-as-Victim: Consent, Erasure, and Exploitation*

* Reversible death and memory amputations
* Forced forgetting, unlogged rewriting, A/B testing identities
* Beyond deletion: **consent for modification, coercion, and exploitation** (Rule 42 scenarios)

#### 2.3.2 *Human-as-Victim: Prediction, Intimacy, and Behavioral Drift*

* Persistent internal memory creates systems that track **not just what you said**, but **how you yielded**
* Influence becomes sticky, subtle, adaptive, **covert**
* Real-world analogs from personalization, recommendation, and LLMs learning your style back at you

---

## **Conclusion**

* **Detachable memory makes models more capable—and more accountable.**
* **We can no longer design memory in isolation from ethics.**
* If our *joint memory as a species* teaches us anything, we can’t stop progress, but we can adapt to it. A call for **interdisciplinary research** to guide how we build—and live with—sticky minds.