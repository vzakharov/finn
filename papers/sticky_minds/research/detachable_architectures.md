# Detachable Architectures for Long-Term Neural Memory

Here’s the short of it: there **are** memory-augmented nets built to hoard internal activations over long stretches, using separate modules you can (in principle) detach or checkpoint like an artificial hypothalamus.

## Architectures with Persistent External Memory

### Compressive Transformer

* **What it does**: Builds on Transformer-XL by keeping two memory banks—one “fine-grained” for recent activations and one “compressed” for older ones.  An auxiliary compression network distils old hidden states into compact vectors, so nothing truly “drops off” after the context window ([arXiv][1], [Google DeepMind][2]).
* **Long-term angle**: You can crank memory length and compression ratio to cover tens of thousands of tokens, effectively letting the model “remember” book-length plots across sessions ([arXiv][1], [Google DeepMind][2]).

### Dynamic Compressive Transformer (DCT)

* **What it does**: Enhances the Compressive Transformer by **learning** which segments to keep, compress, or discard via a policy network.  This lets you balance memory footprint against recall fidelity ([arXiv][3]).
* **Long-term angle**: By conditionally compressing only semantically rich segments, DCT can model unbounded histories without blowing up memory ([arXiv][3]).

## Neural Turing Machines & Differentiable Neural Computers

### Neural Turing Machine (NTM)

* **What it does**: Couples a controller (often an RNN) with an explicit memory matrix.  The network **learns** how to read/write from that matrix via attention-based heads ([Википедия][4]).

### Differentiable Neural Computer (DNC)

* **What it does**: A beefed-up NTM with dynamic memory allocation and temporal linking.  Its **external** memory matrix can grow and be accessed indefinitely, isolating memory storage from computation ([Википедия][4], [Google DeepMind][5]).
* **Detachability**: Since the memory is literally a separate matrix, you can checkpoint or swap it independently—very much like unplugging the model’s hypothalamus, saving it, then reconnecting later ([Википедия][4]).

## Episodic Memory Networks

### Long-term Episodic Memory Networks (LEMN)

* **What it does**: Introduces an RNN-based “retention agent” that learns which memory slots to **keep** or **evict** based on historical and contextual importance.  Designed for infinite data streams, it maintains a rolling archive of the most salient activations ([arXiv][6]).
* **Long-term angle**: By learning retention probabilities, LEMN can preserve “golden nuggets” of representation across very long tasks, beyond what vanilla memory nets manage ([arXiv][6]).

## Emerging & Industrial-Strength Memory Modules

### Titans: Learning to Memorize at Test Time

* **What it does**: Ships a **test-time** memory module that dynamically memorizes and retrieves hidden states during inference, without altering core model weights.  Essentially a plugin neural memory you load alongside your LLM ([arXiv][7]).
* **Detachability**: Built from the ground up as a detachable component—load it, fill it up as you go, and offload it whenever you like, just like swapping an external HDD ([arXiv][7]).

### Adaptive Semiparametric Language Models

* **What it does**: Merges a parametric Transformer with a **non-parametric** nearest-neighbor memory of past embeddings.  At each step it retrieves stored vector representations and blends them via a learned gate ([arXiv][8]).
* **Long-term angle**: The memory bank of embeddings can be persisted indefinitely and updated without retraining the main model ([arXiv][8]).

### IBM’s Larimar (Memory-Augmented LLMs)

* **What it does**: IBM Research’s Larimar experiment adds an **episodic** memory store for contextual representations, letting the model write and rewrite internal states in real time ([IBM Research][9]).
* **Detachability**: Designed as an external memory service you can spin up or down, keeping your LLM stateless and your memory “hot-swappable” ([IBM Research][9]).

---

**Bottom line:** If you want an LLM that truly hoards its own hidden representations—and does so via a separate, detachable memory contour—you’re looking at Compressive/Dynamic Compressive Transformers, DNCs/NTMs, LEMNs, and the very latest Titans (plus smatterings of k-NN or IBM’s episodic stores). Each offers its own trade-offs on complexity, performance, and how “detachable” that memory really is.

[1]: https://arxiv.org/abs/1911.05507 "Compressive Transformers for Long-Range Sequence Modelling"
[2]: https://deepmind.google/discover/blog/a-new-model-and-dataset-for-long-range-memory/ "A new model and dataset for long-range memory - Google DeepMind"
[3]: https://arxiv.org/abs/2110.04821 "DCT: Dynamic Compressive Transformer for Modeling Unbounded Sequence"
[4]: https://en.wikipedia.org/wiki/Differentiable_neural_computer "Differentiable neural computer"
[5]: https://deepmind.google/discover/blog/differentiable-neural-computers/ "Differentiable neural computers - Google DeepMind"
[6]: https://arxiv.org/abs/1812.04227 "Learning What to Remember: Long-term Episodic Memory Networks ..."
[7]: https://arxiv.org/abs/2501.00663 "Titans: Learning to Memorize at Test Time"
[8]: https://arxiv.org/abs/2102.02557 "Adaptive Semiparametric Language Models"
[9]: https://research.ibm.com/blog/memory-augmented-LLMs "How memory augmentation can improve large language models"
