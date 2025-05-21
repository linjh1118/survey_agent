# Paper List of Terms(Medical+RL)
- [25/05] **s3: You Don't Need That Much Data to Train a Search Agent via RL**  
[[Paper](http://arxiv.org/pdf/2505.14146v1)] [[Code/Page]()] [[TLDR/Notes](#s3--you-don-t-need-that-much-data-to-train-a-search-agent-via-rl)]

- [25/05] **Toward Effective Reinforcement Learning Fine-Tuning for Medical VQA in Vision-Language Models**  
[[Paper](http://arxiv.org/pdf/2505.13973v1)] [[Code/Page]()] [[TLDR/Notes](#toward-effective-reinforcement-learning-fine-tuning-for-medical-vqa-in-vision-language-models)]

- [25/05] **Disentangling Reasoning and Knowledge in Medical Large Language Models**  
[[Paper](http://arxiv.org/pdf/2505.11462v1)] [[Code/Page]()] [[TLDR/Notes](#disentangling-reasoning-and-knowledge-in-medical-large-language-models)]

- [25/05] **Patho-R1: A Multimodal Reinforcement Learning-Based Pathology Expert Reasoner**  
[[Paper](http://arxiv.org/pdf/2505.11404v1)] [[Code/Page](https://github.com/Wenchuan-Zhang/Patho-R1.)] [[TLDR/Notes](#patho-r1--a-multimodal-reinforcement-learning-based-pathology-expert-reasoner)]

- [25/04] **Reason Like a Radiologist: Chain-of-Thought and Reinforcement Learning for Verifiable Report Generation**  
[[Paper](http://arxiv.org/pdf/2504.18453v1)] [[Code/Page]()] [[TLDR/Notes](#reason-like-a-radiologist--chain-of-thought-and-reinforcement-learning-for-verifiable-report-generation)]



# TLDR/Notes
## s3--you-don-t-need-that-much-data-to-train-a-search-agent-via-rl
### Abstract
Retrieval-augmented generation (RAG) systems empower large language models
(LLMs) to access external knowledge during inference. Recent advances have
enabled LLMs to act as search agents via reinforcement learning (RL), improving
information acquisition through multi-turn interactions with retrieval engines.
However, existing approaches either optimize retrieval using search-only
metrics (e.g., NDCG) that ignore downstream utility or fine-tune the entire LLM
to jointly reason and retrieve-entangling retrieval with generation and
limiting the real search utility and compatibility with frozen or proprietary
models. In this work, we propose s3, a lightweight, model-agnostic framework
that decouples the searcher from the generator and trains the searcher using a
Gain Beyond RAG reward: the improvement in generation accuracy over naive RAG.
s3 requires only 2.4k training samples to outperform baselines trained on over
70x more data, consistently delivering stronger downstream performance across
six general QA and five medical QA benchmarks.
### 🌟 论文解读 | “少量数据训练搜索代理，s3框架引领RL新篇章”

### 📌 背景痛点/本文动机
随着检索增强生成（Retrieval-Augmented Generation, RAG）系统的兴起，大型语言模型（LLM）能够在推理过程中访问外部知识。然而，现有的方法要么使用仅关注搜索的指标（如NDCG）来优化检索，忽略下游任务的实际效用，要么通过微调整个LLM来同时进行推理和检索，导致检索与生成紧密耦合，限制了搜索的实际效用和与冻结或专有模型的兼容性。本文旨在解决这一问题，提出了一种新的轻量级、模型无关的框架s3，通过强化学习（RL）来训练搜索代理，而无需微调生成模型。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
本文提出了s3框架，该框架将搜索代理与生成模型解耦，仅通过强化学习来训练搜索代理。这种方法使用了一种新颖的奖励信号——超过RAG的增益（Gain Beyond RAG, GBR），该信号量化了检索到的上下文对生成准确性的改善。

💡 创新点2
s3框架在仅有2.4k训练样本的情况下，就能超过基于超过70倍数据训练的基线，这在六个通用问答和五个医疗问答基准测试中一致表现出更强大的下游性能。

### 📈 实验结果
实验结果表明，s3框架在六个通用问答和五个医疗问答基准测试中，使用比基线少70倍的数据，平均得分显著提高。这证明了s3框架在少量数据下训练搜索代理的有效性。

### 💬 可借鉴之处
本文提出的s3框架为如何通过强化学习有效训练搜索代理提供了新的视角，特别是其创新的GBR奖励信号和模型解耦的训练方法，对于提高检索增强生成系统的性能具有重要作用。此外，s3框架在少量数据上的高效性能，对于资源受限的场景尤其有价值。

## toward-effective-reinforcement-learning-fine-tuning-for-medical-vqa-in-vision-language-models
### Abstract
Recently, reinforcement learning (RL)-based tuning has shifted the trajectory
of Multimodal Large Language Models (MLLMs), particularly following the
introduction of Group Relative Policy Optimization (GRPO). However, directly
applying it to medical tasks remains challenging for achieving clinically
grounded model behavior. Motivated by the need to align model response with
clinical expectations, we investigate four critical dimensions that affect the
effectiveness of RL-based tuning in medical visual question answering (VQA):
base model initialization strategy, the role of medical semantic alignment, the
impact of length-based rewards on long-chain reasoning, and the influence of
bias. We conduct extensive experiments to analyze these factors for medical
MLLMs, providing new insights into how models are domain-specifically
fine-tuned. Additionally, our results also demonstrate that GRPO-based RL
tuning consistently outperforms standard supervised fine-tuning (SFT) in both
accuracy and reasoning quality.
### 🌟 论文解读 | "强化学习微调助力医学视觉问答：迈向临床精准的AI之路"

### 📌 背景痛点/本文动机
随着强化学习（RL）在多模态大型语言模型（MLLMs）中的应用，尤其是群相对策略优化（GRPO）的引入，AI领域取得了显著进展。然而，将这一技术应用于医学视觉问答（VQA）任务时，如何确保模型的输出符合临床期望仍然是一个挑战。本文旨在探索如何通过RL微调策略，使医学MLLMs的响应更贴近临床实际需求。

### 🚀 核心方法
💡 创新点1：初始化策略的选择
本文对比了从零开始训练与基于指令微调的模型在医学VQA任务中的表现。结果显示，尽管从零开始训练可以鼓励更多的推理探索，但缺乏指令微调带来的医学知识和语言流畅性。

💡 创新点2：医学语义对齐
为了提高模型推理路径与目标任务的匹配度，本文引入了一种医学语义对齐奖励，通过参考预先定义的专家LLMs的判断，鼓励模型响应与这些判断相匹配。

💡 创新点3：长度基奖励对长链推理的影响
本文探讨了仅依赖长度基奖励（如扩展链奖励（ECR）和正确性加权长度奖励（CWR））是否有助于医学VQA中的有意义的长形式推理。结果显示，这种方法往往导致回答冗长且准确性较低。

💡 创新点4：医学MLLMs中的偏差
本文通过实施Dr.GRPO方法，评估了问题级归一化对模型行为的影响，发现这种方法可以减少因归一化导致的偏差，提高回答的准确性和效率。

💡 创新点5：SFT与GRPO-based RL微调的比较
本文比较了标准监督微调（SFT）与GRPO-based RL微调在医学VQA任务中的效果。结果显示，GRPO-based RL微调在准确性和推理质量上均优于SFT。

### 📈 实验结果
本文在PMC-VQA基准数据集上进行了大量实验，结果表明GRPO-based RL微调在医学VQA任务中表现优于传统微调方法，如SFT。

### 💬 可借鉴之处
本文提供了对医学MLLMs进行RL微调的系统分析，重点关注初始化策略、医学语义对齐、长度基奖励的影响以及偏差相关行为。这些发现为如何在医学VQA任务中实现RL微调提供了宝贵的实践见解，并突显了GRPO-based RL微调在开发更高效、更符合临床需求的医学MLLMs方面的潜力。

## disentangling-reasoning-and-knowledge-in-medical-large-language-models
### Abstract
Medical reasoning in large language models (LLMs) aims to emulate clinicians'
diagnostic thinking, but current benchmarks such as MedQA-USMLE, MedMCQA, and
PubMedQA often mix reasoning with factual recall. We address this by separating
11 biomedical QA benchmarks into reasoning- and knowledge-focused subsets using
a PubMedBERT classifier that reaches 81 percent accuracy, comparable to human
performance. Our analysis shows that only 32.8 percent of questions require
complex reasoning. We evaluate biomedical models (HuatuoGPT-o1, MedReason, m1)
and general-domain models (DeepSeek-R1, o4-mini, Qwen3), finding consistent
gaps between knowledge and reasoning performance. For example, m1 scores 60.5
on knowledge but only 47.1 on reasoning. In adversarial tests where models are
misled with incorrect initial reasoning, biomedical models degrade sharply,
while larger or RL-trained general models show more robustness. To address
this, we train BioMed-R1 using fine-tuning and reinforcement learning on
reasoning-heavy examples. It achieves the strongest performance among similarly
sized models. Further gains may come from incorporating clinical case reports
and training with adversarial and backtracking scenarios.
### 🌟 论文解读 | "精准区分医学大语言模型中的推理与知识：迈向更可靠的医疗AI"

### 📌 背景痛点/本文动机
在医学领域，大型语言模型（LLM）试图模拟临床医生在解读病人数据和做出诊断决策时的认知过程。然而，现有的评估标准如MedQA-USMLE、MedMCQA和PubMedQA等，往往将需要医学推理的问题与仅通过事实回忆即可解决的问题混合在一起。这使得评估LLM的真正推理能力变得具有挑战性。本文旨在解决这一问题，通过分离出专注于推理和专注于知识的问题，以更准确地评估LLM在医学推理方面的表现。

### 🚀 核心方法
💡 创新点1
本文使用PubMedBERT分类器，将11个生物医学问答基准测试中的问题分为推理型和知识型。该分类器达到了与人类表现相当的水平（约81%的准确率）。

💡 创新点2
通过对生物医学模型（如HuatuoGPT-o1、MedReason、m1）和通用领域模型（如DeepSeek-R1、o4-mini、Qwen3）的评估，发现模型在知识和推理方面的表现存在一致性差距。为了提高模型的推理能力，本文训练了BioMed-R1模型，通过精细调整和基于推理重示例的强化学习，使其在同等规模模型中表现出最强的性能。

### 📈 实验结果
实验表明，只有32.8%的问题需要复杂的推理，而大多数问题集中在事实理解上。在对抗性测试中，生物医学模型在接收到错误初始推理的情况下表现急剧下降，而较大或基于强化学习的通用模型则显示出更强的鲁棒性。经过训练的BioMed-R1模型在同等规模模型中取得了最强的综合和对抗性表现。

### 💬 可借鉴之处
本文的研究对于医学LLM的发展具有重要指导意义，它不仅揭示了现有评估标准的不足，还提供了通过分离推理和知识问题来评估模型的新方法。此外，通过对抗性测试和强化学习来提高模型的鲁棒性和可靠性，为未来的医学AI研究提供了新的思路。

## patho-r1--a-multimodal-reinforcement-learning-based-pathology-expert-reasoner
### Abstract
Recent advances in vision language models (VLMs) have enabled broad progress
in the general medical field. However, pathology still remains a more
challenging subdomain, with current pathology specific VLMs exhibiting
limitations in both diagnostic accuracy and reasoning plausibility. Such
shortcomings are largely attributable to the nature of current pathology
datasets, which are primarily composed of image description pairs that lack the
depth and structured diagnostic paradigms employed by real world pathologists.
In this study, we leverage pathology textbooks and real world pathology experts
to construct high-quality, reasoning-oriented datasets. Building on this, we
introduce Patho-R1, a multimodal RL-based pathology Reasoner, trained through a
three-stage pipeline: (1) continued pretraining on 3.5 million image-text pairs
for knowledge infusion; (2) supervised fine-tuning on 500k high-quality
Chain-of-Thought samples for reasoning incentivizing; (3) reinforcement
learning using Group Relative Policy Optimization and Decoupled Clip and
Dynamic sAmpling Policy Optimization strategies for multimodal reasoning
quality refinement. To further assess the alignment quality of our dataset, we
propose PathoCLIP, trained on the same figure-caption corpus used for continued
pretraining. Comprehensive experimental results demonstrate that both PathoCLIP
and Patho-R1 achieve robust performance across a wide range of
pathology-related tasks, including zero-shot classification, cross-modal
retrieval, Visual Question Answering, and Multiple Choice Question. Our project
is available at the Patho-R1 repository:
https://github.com/Wenchuan-Zhang/Patho-R1.
### 🌟 论文解读 | 路径学诊断新篇章：Patho-R1多模态强化学习推理专家

### 📌 背景痛点/本文动机
随着视觉语言模型（VLMs）在医学领域的广泛应用，病理学作为现代临床诊断的金标准，其AI辅助系统的构建却面临着巨大挑战。现有的病理学特定VLMs在诊断准确性和推理合理性方面存在局限，主要因为现有的病理学数据集主要由缺乏深度和结构化诊断范式的图像描述对组成。本文旨在解决这一痛点，提出了一种新的多模态强化学习推理框架，以提升病理学AI系统的性能。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
本文利用病理学教材和真实世界病理学专家的知识，构建了高质量、面向推理的数据集。这一数据集的构建为训练具有深度推理能力的模型奠定了基础。

💡 创新点2
介绍了Patho-R1，一种基于多模态强化学习的病理学推理器。Patho-R1通过三阶段训练流程进行训练：首先是继续在350万图像-文本对上进行预训练以注入知识；其次是在50万高质量链式思维样本上进行监督微调以激励推理；最后是采用组相对策略优化和分离剪辑与动态采样策略优化进行强化学习，以精炼多模态推理质量。

### 📈 实验结果
实验结果表明，PathoCLIP和Patho-R1在一系列病理学相关任务上均取得了稳健的性能，包括零样本分类、跨模态检索、视觉问答和多项选择题。这些结果证明了所提出的数据集和模型的有效性。

### 💬 可借鉴之处
本文提出的综合数据集构建流程能够以最小的人工努力生成高质量的结构化微调数据，这对于其他医学领域的AI系统开发具有借鉴意义。此外，Patho-R1模型的成功展示了强化学习在提升语言模型推理能力方面的潜力，为未来医学AI系统的发展提供了新的思路。

## reason-like-a-radiologist--chain-of-thought-and-reinforcement-learning-for-verifiable-report-generation
### Abstract
Radiology report generation is critical for efficiency but current models
lack the structured reasoning of experts, hindering clinical trust and
explainability by failing to link visual findings to precise anatomical
locations. This paper introduces BoxMed-RL, a groundbreaking unified training
framework for generating spatially verifiable and explainable radiology
reports. Built on a large vision-language model, BoxMed-RL revolutionizes
report generation through two integrated phases: (1) In the Pretraining Phase,
we refine the model via medical concept learning, using Chain-of-Thought
supervision to internalize the radiologist-like workflow, followed by spatially
verifiable reinforcement, which applies reinforcement learning to align medical
findings with bounding boxes. (2) In the Downstream Adapter Phase, we freeze
the pretrained weights and train a downstream adapter to ensure fluent and
clinically credible reports. This framework precisely mimics radiologists'
workflow, compelling the model to connect high-level medical concepts with
definitive anatomical evidence. Extensive experiments on public datasets
demonstrate that BoxMed-RL achieves an average 7% improvement in both METEOR
and ROUGE-L metrics compared to state-of-the-art methods. An average 5%
improvement in large language model-based metrics further underscores
BoxMed-RL's robustness in generating high-quality radiology reports.
### 🌟 论文解读 | “BoxMed-RL：革新医学报告生成，实现像放射科医生一样的推理”

### 📌 背景痛点/本文动机
随着医学影像在临床决策中的重要作用日益凸显，自动化医学报告生成成为提高效率的关键。然而，现有的模型往往缺乏专家式的结构化推理，未能将视觉发现与精确的解剖位置联系起来，导致临床信任度和解释性不足。本文旨在解决这一问题，提出了一种能够生成空间可验证且解释性强的放射学报告的统一训练框架BoxMed-RL。

### 🚀 核心方法
💡 创新点1
BoxMed-RL框架的第一阶段是预训练阶段，通过医学概念学习和链式思维监督来细化模型，使模型内部化放射科医生的推理流程。随后，通过空间可验证的强化学习，将医学发现与边界框对齐。

💡 创新点2
在下游适配器阶段，模型预训练的权重被冻结，并训练一个下游适配器以确保生成的报告流畅且具有临床可信度。这一框架精确模拟了放射科医生的流程，迫使模型将高级医学概念与确切的解剖证据联系起来。

### 📈 实验结果
在公共数据集上的大量实验表明，BoxMed-RL在METEOR和ROUGE-L指标上平均提高了7%，在大型语言模型基准上平均提高了5%，这进一步证明了BoxMed-RL在生成高质量放射学报告方面的稳健性。

### 💬 可借鉴之处
本文提出的BoxMed-RL框架在医学报告生成领域具有显著的创新性，不仅提高了报告的解释性和临床信任度，还为医学影像分析和自然语言处理结合的领域提供了新的视角和方法。特别是其空间可验证的学习策略和模拟放射科医生推理流程的设计思路，对于其他医学AI应用同样具有启发意义。

