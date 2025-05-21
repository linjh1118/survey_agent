# Paper List of Terms(MoE+LLM)
- [25/05] **Scaling and Enhancing LLM-based AVSR: A Sparse Mixture of Projectors Approach**  
[[Paper](http://arxiv.org/pdf/2505.14336v1)] [[Code/Page]()] [[TLDR/Notes](#scaling-and-enhancing-llm-based-avsr--a-sparse-mixture-of-projectors-approach)]

- [25/05] **FuxiMT: Sparsifying Large Language Models for Chinese-Centric Multilingual Machine Translation**  
[[Paper](http://arxiv.org/pdf/2505.14256v1)] [[Code/Page]()] [[TLDR/Notes](#fuximt--sparsifying-large-language-models-for-chinese-centric-multilingual-machine-translation)]

- [25/05] **U-SAM: An audio language Model for Unified Speech, Audio, and Music Understanding**  
[[Paper](http://arxiv.org/pdf/2505.13880v1)] [[Code/Page](https://github.com/Honee-W/U-SAM/).)] [[TLDR/Notes](#u-sam--an-audio-language-model-for-unified-speech--audio--and-music-understanding)]

- [25/05] **EfficientLLM: Efficiency in Large Language Models**  
[[Paper](http://arxiv.org/pdf/2505.13840v1)] [[Code/Page]()] [[TLDR/Notes](#efficientllm--efficiency-in-large-language-models)]

- [25/05] **Occult: Optimizing Collaborative Communication across Experts for Accelerated Parallel MoE Training and Inference**  
[[Paper](http://arxiv.org/pdf/2505.13345v1)] [[Code/Page](https://github.com/UNITES-Lab/Occult}{https://github.com/UNITES-Lab/Occult}$.)] [[TLDR/Notes](#occult--optimizing-collaborative-communication-across-experts-for-accelerated-parallel-moe-training-and-inference)]



# TLDR/Notes
## scaling-and-enhancing-llm-based-avsr--a-sparse-mixture-of-projectors-approach
### Abstract
Audio-Visual Speech Recognition (AVSR) enhances robustness in noisy
environments by integrating visual cues. While recent advances integrate Large
Language Models (LLMs) into AVSR, their high computational cost hinders
deployment in resource-constrained settings. To address this, we propose
Llama-SMoP, an efficient Multimodal LLM that employs a Sparse Mixture of
Projectors (SMoP) module to scale model capacity without increasing inference
costs. By incorporating sparsely-gated mixture-of-experts (MoE) projectors,
Llama-SMoP enables the use of smaller LLMs while maintaining strong
performance. We explore three SMoP configurations and show that Llama-SMoP DEDR
(Disjoint-Experts, Disjoint-Routers), which uses modality-specific routers and
experts, achieves superior performance on ASR, VSR, and AVSR tasks. Ablation
studies confirm its effectiveness in expert activation, scalability, and noise
robustness.
### 🌟 论文解读 | "提升音频视觉识别效率：Llama-SMoP稀疏混合投影器方法"

### 📌 背景痛点/本文动机
音频视觉识别（AVSR）通过结合音频和视觉信息，在嘈杂环境中提高了识别的鲁棒性。然而，近年来将大型语言模型（LLM）集成到AVSR中虽然取得了显著性能提升，但这些模型的高计算成本限制了它们在资源受限环境中的应用。本文旨在解决这一问题，提出了一种名为Llama-SMoP的稀疏混合投影器方法，以在不增加推理成本的情况下扩展模型容量。

### 🚀 核心方法
💡 创新点1
本文提出了Llama-SMoP，一种高效的Multimodal LLM，它采用稀疏混合投影器（SMoP）模块来扩展模型容量，同时保持推理成本不变。通过引入稀疏门控的混合专家（MoE）投影器，Llama-SMoP使得可以使用更小的LLM，同时保持强大的性能。

💡 创新点2
本文探索了三种SMoP配置，并证明了Llama-SMoP DEDR（分离专家，分离路由器）配置在ASR、VSR和AVSR任务上实现了卓越的性能。这种配置使用模态特定的路由器和专家，能够更有效地处理不同模态的信息。

### 📈 实验结果
实验结果表明，Llama-SMoP DEDR在多种规模的Llama-based LLM上均优于先前方法，并且在ASR和VSR任务上也表现出了有效性。此外，消融研究证实了Llama-SMoP在专家激活频率、可扩展性和噪声鲁棒性方面的有效性。

### 💬 可借鉴之处
本文提出的Llama-SMoP方法为在资源受限的环境中部署LLM-based AVSR系统提供了一种有效的解决方案。通过使用SMoP模块，该方法在不牺牲性能的情况下，显著降低了计算成本，对于希望在实际应用中集成LLM的 researchers 和工程师具有很高的参考价值。此外，本文对SMoP的不同配置进行了详细探讨，为后续研究和优化提供了丰富的实验基础。

## fuximt--sparsifying-large-language-models-for-chinese-centric-multilingual-machine-translation
### Abstract
In this paper, we present FuxiMT, a novel Chinese-centric multilingual
machine translation model powered by a sparsified large language model (LLM).
We adopt a two-stage strategy to train FuxiMT. We first pre-train the model on
a massive Chinese corpus and then conduct multilingual fine-tuning on a large
parallel dataset encompassing 65 languages. FuxiMT incorporates
Mixture-of-Experts (MoEs) and employs a curriculum learning strategy for robust
performance across various resource levels. Experimental results demonstrate
that FuxiMT significantly outperforms strong baselines, including
state-of-the-art LLMs and machine translation models, particularly under
low-resource scenarios. Furthermore, FuxiMT exhibits remarkable zero-shot
translation capabilities for unseen language pairs, indicating its potential to
bridge communication gaps where parallel data are scarce or unavailable.
### 🌟 论文解读 | “FuxiMT：打造以中文为核心的稀疏化大型语言模型助力多语言机器翻译”

### 📌 背景痛点/本文动机
随着大型语言模型（LLM）的快速发展，机器翻译领域迎来了新的突破。然而，尽管中文在全球语言中占有重要地位，目前的技术进展并未能满足中文在多语言翻译方面的巨大需求。现有的LLM模型如BLOOM和LLaMA虽然具有多语言能力，但支持的语种有限，远远不能满足全球7000多种语言的需求。为此，本文提出了FuxiMT模型，一种以中文为核心，基于稀疏化大型语言模型的新型多语言机器翻译模型。

### 🚀 核心方法
💡 创新点1
FuxiMT采用了两阶段训练策略。首先在超过50亿中文标记的大规模语料库上进行了预训练，使模型深入理解中文，确保了FuxiMT的中文核心特性。随后，在包含65种语言的超过100亿句对的平行语料库上进行多语言微调。

💡 创新点2
FuxiMT引入了混合专家（Mixture-of-Experts, MoEs）机制，并在解码器堆中定期插入MoE模块。这种模块化的结构不仅提高了计算效率，还增强了模型的可扩展性。同时，采用了一种课程学习策略，逐步增加语言覆盖范围和数据复杂性，以实现跨不同资源水平的稳健性能。

### 📈 实验结果
实验结果表明，FuxiMT在低资源场景下显著优于现有基线，包括最先进的LLM和机器翻译模型。此外，FuxiMT展现出了卓越的零样本翻译能力，能够处理未见过的语言对，这表明其在平行数据稀缺或不可用的环境中架起沟通桥梁的潜力。

### 💬 可借鉴之处
FuxiMT的提出为中文多语言翻译提供了新的视角，其创新的训练策略和模型结构对于处理大规模多语言数据具有启示意义。此外，FuxiMT在低资源语言对的翻译上展现出的零样本学习能力，为多语言机器翻译的广泛应用提供了新的可能性。

## u-sam--an-audio-language-model-for-unified-speech--audio--and-music-understanding
### Abstract
The text generation paradigm for audio tasks has opened new possibilities for
unified audio understanding. However, existing models face significant
challenges in achieving a comprehensive understanding across diverse audio
types, such as speech, general audio events, and music. Furthermore, their
exclusive reliance on cross-entropy loss for alignment often falls short, as it
treats all tokens equally and fails to account for redundant audio features,
leading to weaker cross-modal alignment. To deal with the above challenges,
this paper introduces U-SAM, an advanced audio language model that integrates
specialized encoders for speech, audio, and music with a pre-trained large
language model (LLM). U-SAM employs a Mixture of Experts (MoE) projector for
task-aware feature fusion, dynamically routing and integrating the
domain-specific encoder outputs. Additionally, U-SAM incorporates a
Semantic-Aware Contrastive Loss Module, which explicitly identifies redundant
audio features under language supervision and rectifies their semantic and
spectral representations to enhance cross-modal alignment. Extensive
experiments demonstrate that U-SAM consistently outperforms both specialized
models and existing audio language models across multiple benchmarks. Moreover,
it exhibits emergent capabilities on unseen tasks, showcasing its
generalization potential. Code is available
(https://github.com/Honee-W/U-SAM/).
### 🌟 论文解读 | “U-SAM：开启语音、音频与音乐统一理解的音频语言模型”

### 📌 背景痛点/本文动机
随着大型语言模型在自然语言处理领域取得的显著成就，研究者们开始尝试将这些模型扩展到其他模态，如图像、视频和音频。音频语言模型（ALMs）作为一个新兴的研究领域，旨在通过结合音频和文本信息，实现对音频内容的深入理解。然而，现有的音频语言模型在处理不同类型的音频（如语音、一般音频事件和音乐）时面临重大挑战，且在音频和文本之间的对齐上存在不足，导致跨模态对齐较弱。本文提出了U-SAM模型，旨在解决这些问题，通过整合特定领域的音频编码器和一个预训练的大型语言模型，实现对语音、音频和音乐的统一理解。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
U-SAM引入了一个任务感知投影模块（TAPM），该模块通过混合专家（MoE）机制动态地路由和融合来自多个音频编码器的嵌入，根据相应任务生成任务自适应的特征，从而实现更深入的多模态对齐。

💡 创新点2
U-SAM还包含一个语义感知对比损失模块（SACLM），该模块在语言监督下显式识别并修正冗余的音频帧，以增强音频和文本之间的对齐。此外，U-SAM将音频任务视为开放式的文本生成任务，使其能够处理广泛的任务，并展现出在未见任务上的涌现能力。

### 📈 实验结果
本文通过广泛的实验验证了U-SAM模型在多个基准测试中的优越性能，无论是在特定领域模型还是现有音频语言模型上，U-SAM均展现出更好的结果。同时，U-SAM在未见任务上展现出的涌现能力，进一步证明了其泛化潜力。

### 💬 可借鉴之处
U-SAM模型的设计理念和方法对于音频处理领域具有很高的参考价值，特别是其任务感知的特征融合策略和语义感知对比损失的设计，为音频和文本的跨模态对齐提供了新的视角。此外，U-SAM在处理不同类型音频时的泛化能力，也为构建更通用的人工智能系统提供了启示。

## efficientllm--efficiency-in-large-language-models
### Abstract
Large Language Models (LLMs) have driven significant progress, yet their
growing parameter counts and context windows incur prohibitive compute, energy,
and monetary costs. We introduce EfficientLLM, a novel benchmark and the first
comprehensive empirical study evaluating efficiency techniques for LLMs at
scale. Conducted on a production-class cluster (48xGH200, 8xH200 GPUs), our
study systematically explores three key axes: (1) architecture pretraining
(efficient attention variants: MQA, GQA, MLA, NSA; sparse Mixture-of-Experts
(MoE)), (2) fine-tuning (parameter-efficient methods: LoRA, RSLoRA, DoRA), and
(3) inference (quantization methods: int4, float16). We define six fine-grained
metrics (Memory Utilization, Compute Utilization, Latency, Throughput, Energy
Consumption, Compression Rate) to capture hardware saturation,
latency-throughput balance, and carbon cost. Evaluating over 100
model-technique pairs (0.5B-72B parameters), we derive three core insights: (i)
Efficiency involves quantifiable trade-offs: no single method is universally
optimal; e.g., MoE reduces FLOPs and improves accuracy but increases VRAM by
40%, while int4 quantization cuts memory/energy by up to 3.9x at a 3-5%
accuracy drop. (ii) Optima are task- and scale-dependent: MQA offers optimal
memory-latency trade-offs for constrained devices, MLA achieves lowest
perplexity for quality-critical tasks, and RSLoRA surpasses LoRA efficiency
only beyond 14B parameters. (iii) Techniques generalize across modalities: we
extend evaluations to Large Vision Models (Stable Diffusion 3.5, Wan 2.1) and
Vision-Language Models (Qwen2.5-VL), confirming effective transferability. By
open-sourcing datasets, evaluation pipelines, and leaderboards, EfficientLLM
provides essential guidance for researchers and engineers navigating the
efficiency-performance landscape of next-generation foundation models.
### 🌟 论文解读 | 提升大型语言模型效率的全面研究

### 📌 背景痛点/本文动机
随着大型语言模型（LLMs）参数量的激增和上下文窗口的扩大，计算、能耗和成本变得越来越高昂。本文旨在解决这一痛点，通过引入EfficientLLM这一新型基准，对LLMs的效率技术进行全面评估。

### 🚀 核心方法
💡 创新点1：系统性研究
本文系统地探索了三个关键维度：架构预训练（包括MQA、GQA、MLA、NSA等高效注意力变体和稀疏Mixture-of-Experts）、微调（包括LoRA、RSLoRA、DoRA等参数高效方法）以及推理（包括int4、float16等量化方法）。

💡 创新点2：全面评估指标
定义了六个细粒度的评估指标（内存利用率、计算利用率、延迟、吞吐量、能耗和压缩率），以全面捕捉硬件饱和度、延迟-吞吐量平衡和碳成本。

### 📈 实验结果
本文评估了超过100种模型-技术组合，涵盖0.5B至72B参数的LLMs，得出以下核心见解：
1. 效率涉及可量化的权衡：没有一种方法在所有指标上都是最优的。例如，Mixture-of-Experts减少了FLOPs并提高了准确性，但增加了40%的VRAM；而int4量化在平均3-5%的任务分数下降下，减少了内存和能耗高达3.9倍。
2. 最优解依赖于任务和规模：MQA在受限设备上提供了最佳的内存-延迟权衡，MLA在质量关键任务上实现了最低的困惑度，RSLoRA仅在超过14B参数时才比LoRA更高效。
3. 技术具有广泛的适用性：将评估扩展到大型视觉模型和视觉语言模型，验证了在LLMs上验证的效率技术在其他模态上的有效迁移性。

### 💬 可借鉴之处
本研究为研究人员和工程师提供了一份重要的指导，帮助他们了解下一代基础模型效率-性能景观，并通过开源数据集、评估管道和排行榜，为探索效率技术的转移性和适用性提供了宝贵的资源。

## occult--optimizing-collaborative-communication-across-experts-for-accelerated-parallel-moe-training-and-inference
### Abstract
Mixture-of-experts (MoE) architectures could achieve impressive computational
efficiency with expert parallelism, which relies heavily on all-to-all
communication across devices. Unfortunately, such communication overhead
typically constitutes a significant portion of the total runtime, hampering the
scalability of distributed training and inference for modern MoE models
(consuming over $40\%$ runtime in large-scale training). In this paper, we
first define collaborative communication to illustrate this intrinsic
limitation, and then propose system- and algorithm-level innovations to reduce
communication costs. Specifically, given a pair of experts co-activated by one
token, we call them "collaborated", which comprises $2$ cases as intra- and
inter-collaboration, depending on whether they are kept on the same device. Our
pilot investigations reveal that augmenting the proportion of
intra-collaboration can accelerate expert parallelism at scale. It motivates us
to strategically optimize collaborative communication for accelerated MoE
training and inference, dubbed Occult. Our designs are capable of either
delivering exact results with reduced communication cost or controllably
minimizing the cost with collaboration pruning, materialized by modified
fine-tuning. Comprehensive experiments on various MoE-LLMs demonstrate that
Occult can be faster than popular state-of-the-art inference or training
frameworks (more than $1.5\times$ speed up across multiple tasks and models)
with comparable or superior quality compared to the standard fine-tuning. Code
is available at
$\href{https://github.com/UNITES-Lab/Occult}{https://github.com/UNITES-Lab/Occult}$.
### 🌟 论文解读 | 优化专家协作通信，加速混合专家模型训练与推理

### 📌 背景痛点/本文动机
随着大型语言模型（LLM）在多种下游任务中取得显著成功，通过增加模型参数来提升模型能力已成为常态。混合专家（MoE）架构通过稀疏性实现了参数的高效扩展。然而，MoE模型的分布式训练和推理中，跨设备通信开销巨大，通常占据总运行时间的40%以上，严重限制了可扩展性。本文针对这一痛点，提出了优化通信策略以加速MoE模型的训练和推理。

### 🚀 核心方法
💡 创新点1：提出协作通信概念
本文将MoE工作流程中的全对全通信重新定义为协作通信。给定一个token同时激活的专家对，称为“协作”，并根据它们是否位于同一设备上，分为内部协作和外部协作。

💡 创新点2：专家协作优化
通过最大化内部协作和最小化外部协作，优化通信成本。本文提出了一种新的稀疏矩阵乘法核，以减少不必要的内存分配或访问。此外，通过分析协作数据集，重新安排专家放置位置，以及提出协作剪枝策略，以可控地降低通信成本。

### 📈 实验结果
本文在各种MoE-LLM上的综合实验表明，提出的Occult方法在多个任务和模型上均能实现超过1.5倍的速度提升，同时保持或优于标准微调的质量。

### 💬 可借鉴之处
本文从系统级和算法级提出了创新的通信优化策略，不仅提高了MoE模型的训练和推理效率，还为通信密集型任务提供了有效的解决方案。此外，提出的协作通信概念为理解和优化大规模并行计算提供了新的视角。

