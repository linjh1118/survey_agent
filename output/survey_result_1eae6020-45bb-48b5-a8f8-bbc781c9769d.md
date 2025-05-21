# Paper List of Terms(VLM+GRPO)
- [25/05] **Visionary-R1: Mitigating Shortcuts in Visual Reasoning with Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.14677v1)] [[Code/Page]()] [[TLDR/Notes](#visionary-r1--mitigating-shortcuts-in-visual-reasoning-with-reinforcement-learning)]

- [25/05] **FlightGPT: Towards Generalizable and Interpretable UAV Vision-and-Language Navigation with Vision-Language Models**  
[[Paper](http://arxiv.org/pdf/2505.12835v1)] [[Code/Page]()] [[TLDR/Notes](#flightgpt--towards-generalizable-and-interpretable-uav-vision-and-language-navigation-with-vision-language-models)]

- [25/04] **LR-IAD:Mask-Free Industrial Anomaly Detection with Logical Reasoning**  
[[Paper](http://arxiv.org/pdf/2504.19524v1)] [[Code/Page](https://github.com/LilaKen/LR-IAD.)] [[TLDR/Notes](#lr-iad-mask-free-industrial-anomaly-detection-with-logical-reasoning)]

- [25/04] **AnomalyR1: A GRPO-based End-to-end MLLM for Industrial Anomaly Detection**  
[[Paper](http://arxiv.org/pdf/2504.11914v1)] [[Code/Page]()] [[TLDR/Notes](#anomalyr1--a-grpo-based-end-to-end-mllm-for-industrial-anomaly-detection)]

- [25/04] **PathVLM-R1: A Reinforcement Learning-Driven Reasoning Model for Pathology Visual-Language Tasks**  
[[Paper](http://arxiv.org/pdf/2504.09258v2)] [[Code/Page]()] [[TLDR/Notes](#pathvlm-r1--a-reinforcement-learning-driven-reasoning-model-for-pathology-visual-language-tasks)]

- [25/03] **Reason-RFT: Reinforcement Fine-Tuning for Visual Reasoning**  
[[Paper](http://arxiv.org/pdf/2503.20752v2)] [[Code/Page](https://tanhuajie.github.io/ReasonRFT)] [[TLDR/Notes](#reason-rft--reinforcement-fine-tuning-for-visual-reasoning)]



# TLDR/Notes
## visionary-r1--mitigating-shortcuts-in-visual-reasoning-with-reinforcement-learning
### Abstract
Learning general-purpose reasoning capabilities has long been a challenging
problem in AI. Recent research in large language models (LLMs), such as
DeepSeek-R1, has shown that reinforcement learning techniques like GRPO can
enable pre-trained LLMs to develop reasoning capabilities using simple
question-answer pairs. In this paper, we aim to train visual language models
(VLMs) to perform reasoning on image data through reinforcement learning and
visual question-answer pairs, without any explicit chain-of-thought (CoT)
supervision. Our findings indicate that simply applying reinforcement learning
to a VLM -- by prompting the model to produce a reasoning chain before
providing an answer -- can lead the model to develop shortcuts from easy
questions, thereby reducing its ability to generalize across unseen data
distributions. We argue that the key to mitigating shortcut learning is to
encourage the model to interpret images prior to reasoning. Therefore, we train
the model to adhere to a caption-reason-answer output format: initially
generating a detailed caption for an image, followed by constructing an
extensive reasoning chain. When trained on 273K CoT-free visual question-answer
pairs and using only reinforcement learning, our model, named Visionary-R1,
outperforms strong multimodal models, such as GPT-4o, Claude3.5-Sonnet, and
Gemini-1.5-Pro, on multiple visual reasoning benchmarks.
### 🌟 论文解读 | "Visionary-R1：利用强化学习削弱视觉推理中的捷径学习"

### 📌 背景痛点/本文动机
长久以来，让AI模型具备通用推理能力一直是人工智能领域的一个难题。尽管最近大型语言模型（LLMs）如DeepSeek-R1的研究表明，通过强化学习技术如GRPO，可以使得预训练的LLMs通过简单的问题-答案对发展出推理能力，但在视觉语言模型（VLMs）上进行推理，尤其是没有显式链式思维（CoT）监督的情况下，仍然是一个挑战。当前研究中的视觉推理模型往往依赖于复杂的多阶段训练流程，这些流程既计算昂贵又耗时，并且这些模型高度依赖从专有模型如GPT-4o中提取的标记链式思维推理数据，这限制了可扩展性和开放性。本文旨在通过仅使用强化学习和配对的视觉问题-答案数据，来降低训练VLMs进行视觉推理的开发成本。

### 🚀 核心方法
💡 创新点1
本文提出了Visionary-R1，一个基于强化学习的框架，该框架通过在推理之前强制进行视觉理解来削弱捷径学习。具体来说，模型被训练遵循一个结构化的“描述-推理-回答”输出格式，首先生成图像的详细描述，然后进行推理并给出答案。

💡 创新点2
为了确保描述的准确性，研究者在描述令牌上施加了辅助监督，通过从AI反馈中学习强化学习。这种描述奖励与标准的准确性和格式奖励相结合，用于策略优化。这种方法使得模型产生的推理令牌更长、更有意义，从而在未见数据上展现出更好的泛化性能。

### 📈 实验结果
研究者编译了一个包含11个流行问题-答案数据集的综合数据集，涵盖了场景理解、图表分析、数学问题解决和文档处理等领域，总计272.6K个无CoT的问题-答案对。训练后，Visionary-R1在MathVista、MathVision、MMStar和MMBench等多个具有挑战性的视觉推理基准上进行了评估。结果显示，Visionary-R1优于GPT-4o、Claude3.5-Sonnet和Gemini-1.5-Pro等强大的多模态模型。

### 💬 可借鉴之处
本文不仅揭示了GRPO直接应用于VLMs时由于捷径学习而失效的问题，还提出了一种简单有效的基于强化学习的模型，该模型在推理之前先进行图像理解，从而提高了推理能力的泛化性。此外，通过实验证明了即使仅使用问题-答案对，Visionary-R1也能在具有挑战性的视觉推理基准上击败强大的多模态模型，这为未来视觉推理模型的研究提供了一个新的视角和方法。

## flightgpt--towards-generalizable-and-interpretable-uav-vision-and-language-navigation-with-vision-language-models
### Abstract
Unmanned Aerial Vehicle (UAV) Vision-and-Language Navigation (VLN) is vital
for applications such as disaster response, logistics delivery, and urban
inspection. However, existing methods often struggle with insufficient
multimodal fusion, weak generalization, and poor interpretability. To address
these challenges, we propose FlightGPT, a novel UAV VLN framework built upon
Vision-Language Models (VLMs) with powerful multimodal perception capabilities.
We design a two-stage training pipeline: first, Supervised Fine-Tuning (SFT)
using high-quality demonstrations to improve initialization and structured
reasoning; then, Group Relative Policy Optimization (GRPO) algorithm, guided by
a composite reward that considers goal accuracy, reasoning quality, and format
compliance, to enhance generalization and adaptability. Furthermore, FlightGPT
introduces a Chain-of-Thought (CoT)-based reasoning mechanism to improve
decision interpretability. Extensive experiments on the city-scale dataset
CityNav demonstrate that FlightGPT achieves state-of-the-art performance across
all scenarios, with a 9.22\% higher success rate than the strongest baseline in
unseen environments. Our implementation is publicly available.
### 🌟 论文解读 | FlightGPT：迈向通用性和可解释性的无人机视觉与语言导航

### 📌 背景痛点/本文动机
无人机视觉与语言导航（UAV VLN）在灾难响应、物流配送和城市检查等应用中至关重要。然而，现有的方法在多模态融合不足、泛化能力弱和决策可解释性差等方面存在挑战。本文提出了FlightGPT，一种基于视觉语言模型（VLMs）的无人机VLN新框架，旨在解决这些问题。

### 🚀 核心方法
💡 创新点1
FlightGPT采用基于VLMs的多模态融合，有效整合视觉和文本输入，增强多模态感知和理解能力。

💡 创新点2
设计了两阶段训练流程：首先是监督微调（SFT），利用高质量演示来优化初始化和结构化推理；然后是组相对策略优化（GRPO）算法，通过考虑目标准确性、推理质量和格式符合性的复合奖励来增强泛化和适应性。

💡 创新点3
引入了基于链式思维（CoT）的推理机制，通过显式的“思考”/“回答”标签形成CoT推理过程，提高决策的可解释性。

### 📈 实验结果
在大型城市环境基准CityNav上的广泛实验表明，FlightGPT在所有场景中均实现了最先进的性能，比在未见环境中表现最强的基线高出9.22%的成功率。

### 💬 可借鉴之处
FlightGPT的提出为无人机VLN领域带来了新的视角，其创新的多模态融合策略、两阶段训练流程以及CoT推理机制为提高无人机导航系统的泛化能力、适应性和可解释性提供了有效途径。此外，论文在真实城市环境基准上的实验验证了方法的有效性，为相关领域的研究提供了有价值的参考。

## lr-iad-mask-free-industrial-anomaly-detection-with-logical-reasoning
### Abstract
Industrial Anomaly Detection (IAD) is critical for ensuring product quality
by identifying defects. Traditional methods such as feature embedding and
reconstruction-based approaches require large datasets and struggle with
scalability. Existing vision-language models (VLMs) and Multimodal Large
Language Models (MLLMs) address some limitations but rely on mask annotations,
leading to high implementation costs and false positives. Additionally,
industrial datasets like MVTec-AD and VisA suffer from severe class imbalance,
with defect samples constituting only 23.8% and 11.1% of total data
respectively. To address these challenges, we propose a reward function that
dynamically prioritizes rare defect patterns during training to handle class
imbalance. We also introduce a mask-free reasoning framework using Chain of
Thought (CoT) and Group Relative Policy Optimization (GRPO) mechanisms,
enabling anomaly detection directly from raw images without annotated masks.
This approach generates interpretable step-by-step explanations for defect
localization. Our method achieves state-of-the-art performance, outperforming
prior approaches by 36% in accuracy on MVTec-AD and 16% on VisA. By eliminating
mask dependency and reducing costs while providing explainable outputs, this
work advances industrial anomaly detection and supports scalable quality
control in manufacturing. Code to reproduce the experiment is available at
https://github.com/LilaKen/LR-IAD.
### 🌟 论文解读 | 无遮挡工业异常检测的逻辑推理新方法

### 📌 背景痛点/本文动机
工业异常检测（IAD）对于确保产品质量至关重要，它通过识别缺陷来保障产品品质。传统方法如特征嵌入和重建-based方法需要大量数据集，并且难以扩展。现有的视觉语言模型（VLMs）和多模态大型语言模型（MLLMs）虽然解决了一些限制，但依赖于掩码注释，导致实施成本高昂和误报率高。此外，工业数据集如MVTec-AD和VisA存在严重的类别不平衡问题，缺陷样本分别只占总数据的23.8%和11.1%。针对这些挑战，本文提出了一种新的奖励函数，动态优先处理训练中的罕见缺陷模式，以解决类别不平衡问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
本文提出了一种新的奖励函数，该函数在训练过程中动态优先处理罕见的缺陷模式，有效解决了工业数据集中的类别不平衡问题，避免了过度拟合到主要类别。

💡 创新点2
本文引入了一种无遮挡推理框架，利用链式思维（CoT）和组相对策略优化（GRPO）机制，使异常检测能够直接从原始图像进行，无需注释的掩码。这种方法为缺陷定位生成了可解释的逐步解释。

### 📈 实验结果
本文的方法在MVTec-AD数据集上比之前的最佳方法提高了36%的准确性，在VisA数据集上提高了16%。这些结果表明，该方法在无遮挡推理和提供可解释输出方面取得了显著的进展，为工业异常检测和制造质量控制的扩展提供了支持。

### 💬 可借鉴之处
本文的方法不仅提高了异常检测的准确性，还通过消除对掩码的依赖和降低成本，为工业质量控制在实际应用中提供了新的思路。此外，该方法生成的可解释输出增强了模型决策的透明度，有助于提高用户对模型的信任度。论文中提出的动态优先处理罕见缺陷模式的奖励函数和基于链式思维的无遮挡推理框架，对于解决工业数据集中的类别不平衡问题和降低实施成本具有很高的参考价值。

## anomalyr1--a-grpo-based-end-to-end-mllm-for-industrial-anomaly-detection
### Abstract
Industrial Anomaly Detection (IAD) poses a formidable challenge due to the
scarcity of defective samples, making it imperative to deploy models capable of
robust generalization to detect unseen anomalies effectively. Traditional
approaches, often constrained by hand-crafted features or domain-specific
expert models, struggle to address this limitation, underscoring the need for a
paradigm shift. We introduce AnomalyR1, a pioneering framework that leverages
VLM-R1, a Multimodal Large Language Model (MLLM) renowned for its exceptional
generalization and interpretability, to revolutionize IAD. By integrating MLLM
with Group Relative Policy Optimization (GRPO), enhanced by our novel Reasoned
Outcome Alignment Metric (ROAM), AnomalyR1 achieves a fully end-to-end solution
that autonomously processes inputs of image and domain knowledge, reasons
through analysis, and generates precise anomaly localizations and masks. Based
on the latest multimodal IAD benchmark, our compact 3-billion-parameter model
outperforms existing methods, establishing state-of-the-art results. As MLLM
capabilities continue to advance, this study is the first to deliver an
end-to-end VLM-based IAD solution that demonstrates the transformative
potential of ROAM-enhanced GRPO, positioning our framework as a forward-looking
cornerstone for next-generation intelligent anomaly detection systems in
industrial applications with limited defective data.
### 🌟 论文解读 | "AnomalyR1：引领工业异常检测新篇章"

### 📌 背景痛点/本文动机
工业异常检测（IAD）面临着巨大的挑战，主要是因为缺陷样本的稀缺性，这要求模型必须具备强大的泛化能力，以有效检测未见过的异常。传统的工业异常检测方法通常受限于手工特征或特定领域的专家模型，难以突破这一局限。因此，本文提出了AnomalyR1框架，旨在利用多模态大型语言模型（MLLM）的卓越泛化能力和解释性，为工业异常检测带来革命性的改变。

### 🚀 核心方法
💡 创新点1
AnomalyR1框架基于VLM-R1，这是一种多模态大型语言模型，以其出色的泛化能力和解释性而闻名。通过将MLLM与组相对策略优化（GRPO）相结合，并引入新颖的理由结果对齐度量（ROAM），AnomalyR1实现了一个完全端到端的解决方案，能够自主处理图像和领域知识输入，进行推理分析，并生成精确的异常定位和掩码。

💡 创新点2
本文提出的ROAM是一种创新的奖励框架，它专门为工业异常检测任务设计，能够迭代地引导模型通过工业产品图像的推理过程，逐步提高异常检测的准确性。此外，AnomalyR1在最新的多模态IAD基准测试MMAD上取得了最先进（SOTA）的性能，证明了其卓越的多模态推理和泛化能力。

### 📈 实验结果
AnomalyR1框架在MMAD基准测试中表现出了卓越的性能，使用一个紧凑的30亿参数模型超过了现有的方法，确立了其在工业异常检测领域的领先地位。该框架在数据稀缺的条件下，通过仅使用2-5个每类的工业物品图像即可实现足够性能的鲁棒少量样本学习。

### 💬 可借鉴之处
本文的研究为工业异常检测领域提供了以下几个可借鉴之处：
1. 利用MLLM进行端到端的工业异常检测，这是一种相对较新的方法，与传统的依赖复杂专家模型或预训练视觉文本编码器的方法有显著区别。
2. 通过GRPO增强的VLM-R1构建的AnomalyR1框架，为数据稀缺条件下的工业异常检测提供了有效的解决方案。
3. ROAM奖励框架的创新设计，为改进GRPO训练方法在工业异常检测任务中的性能提供了重要支持。
4. 在最新的多模态IAD基准测试中取得SOTA性能，展示了AnomalyR1框架在多模态推理和泛化方面的潜力。

## pathvlm-r1--a-reinforcement-learning-driven-reasoning-model-for-pathology-visual-language-tasks
### Abstract
The diagnosis of pathological images is often limited by expert availability
and regional disparities, highlighting the importance of automated diagnosis
using Vision-Language Models (VLMs). Traditional multimodal models typically
emphasize outcomes over the reasoning process, compromising the reliability of
clinical decisions. To address the weak reasoning abilities and lack of
supervised processes in pathological VLMs, we have innovatively proposed
PathVLM-R1, a visual language model designed specifically for pathological
images. We have based our model on Qwen2.5-VL-7B-Instruct and enhanced its
performance for pathological tasks through meticulously designed post-training
strategies. Firstly, we conduct supervised fine-tuning guided by pathological
data to imbue the model with foundational pathological knowledge, forming a new
pathological base model. Subsequently, we introduce Group Relative Policy
Optimization (GRPO) and propose a dual reward-driven reinforcement learning
optimization, ensuring strict constraint on logical supervision of the
reasoning process and accuracy of results via cross-modal process reward and
outcome accuracy reward. In the pathological image question-answering tasks,
the testing results of PathVLM-R1 demonstrate a 14% improvement in accuracy
compared to baseline methods, and it demonstrated superior performance compared
to the Qwen2.5-VL-32B version despite having a significantly smaller parameter
size. Furthermore, in out-domain data evaluation involving four medical imaging
modalities: Computed Tomography (CT), dermoscopy, fundus photography, and
Optical Coherence Tomography (OCT) images: PathVLM-R1's transfer performance
improved by an average of 17.3% compared to traditional SFT methods. These
results clearly indicate that PathVLM-R1 not only enhances accuracy but also
possesses broad applicability and expansion potential.
### 🌟 论文解读 | PathVLM-R1：推动病理视觉语言任务推理的强化学习模型

### 📌 背景痛点/本文动机
在医学病理诊断中，准确分析病理切片对于临床决策至关重要。然而，专业病理学家的水平参差不齐，且诊断需求不断增长，导致医疗人力资源压力增大。为了缓解地区间的诊断和治疗水平差异，研究人员开始开发视觉语言模型以辅助病理图像的诊断。当前，大多数视觉语言模型依赖于端到端的训练和监督微调，这些模型往往倾向于记忆和模仿数据中的模式，缺乏透明和可信的推理能力。

### 🚀 核心方法
💡 创新点1
本文提出了PathVLM-R1，这是一种专门为病理图像设计的视觉语言模型，具有推理能力。该模型基于Qwen2.5-VL-7B-Instruct，并通过精心设计的后训练策略提升了其在病理任务上的性能。首先，通过病理数据指导的监督微调，使模型具备了基本的病理知识，形成了新的病理基础模型。

💡 创新点2
本文引入了组相对策略优化（GRPO）并提出了一种双奖励驱动的强化学习优化方法。这种方法通过跨模态过程奖励和结果准确度奖励，严格约束推理过程的逻辑监督和结果的准确性，形成了一个“过程-结果”的闭环监督。最终，通过GRPO实现了跨模态过程奖励和结果准确度奖励的整合，确保了过程合理性和结果准确性的平衡。

### 📈 实验结果
在病理图像问答任务中，PathVLM-R1的测试结果显示，与基线方法相比，准确度提高了14%。此外，尽管参数规模较小，PathVLM-R1的性能仍优于Qwen2.5-VL-32B版本。在涉及四种医学成像模态（计算机断层扫描、皮肤镜检查、眼底摄影和光学相干断层扫描图像）的跨域数据评估中，PathVLM-R1的迁移性能平均提高了17.3%，明显优于传统的监督微调方法。

### 💬 可借鉴之处
PathVLM-R1不仅提高了准确性，而且具有广泛的适用性和扩展潜力。本文的方法为医学视觉语言模型的推理能力提升提供了新的思路，特别是通过引入双奖励机制，将医学中对过程解释性和结果准确性的需求转化为可学习的双奖励信号，为医学诊断领域提供了有效的模型优化策略。此外，PathVLM-R1在训练参数和样本数量上的高效性，也为类似研究提供了参考。

## reason-rft--reinforcement-fine-tuning-for-visual-reasoning
### Abstract
Visual reasoning abilities play a crucial role in understanding complex
multimodal data, advancing both domain-specific applications and artificial
general intelligence (AGI). Existing methods improve VLM reasoning via
Chain-of-Thought (CoT) supervised fine-tuning, using meticulously annotated
training data to enhance visual reasoning capabilities. However, this training
paradigm may lead to overfitting and cognitive rigidity, restricting the
model's ability to transfer visual reasoning skills across domains and limiting
its real-world applicability. To address these limitations, we propose
Reason-RFT, a novel reinforcement fine-tuning framework that significantly
enhances generalization capabilities in visual reasoning tasks. Reason-RFT
introduces a two-phase training framework for visual reasoning: (1) Supervised
Fine-Tuning (SFT) with curated Chain-of-Thought (CoT) data activates the
reasoning potential of Vision-Language Models (VLMs), followed by (2) Group
Relative Policy Optimization (GRPO)-based reinforcement learning that generates
multiple reasoning-response pairs, significantly enhancing generalization in
visual reasoning tasks. To evaluate Reason-RFT's visual reasoning capabilities,
we reconstructed a comprehensive dataset spanning visual counting, structure
perception, and spatial transformation. Experimental results demonstrate
Reasoning-RFT's three key advantages: (1) Performance Enhancement: achieving
state-of-the-art results across multiple tasks, outperforming most mainstream
open-source and proprietary models; (2) Generalization Superiority:
consistently maintaining robust performance across diverse tasks and domains,
outperforming alternative training paradigms; (3) Data Efficiency: excelling in
few-shot learning scenarios while surpassing full-dataset SFT baselines.
Project website: https://tanhuajie.github.io/ReasonRFT
### 🌟 论文解读 | Reason-RFT：提升视觉推理能力的新框架

### 📌 背景痛点/本文动机
视觉推理能力对于理解复杂的多种模态数据和推动人工通用智能（AGI）的发展至关重要。现有的方法通常通过链式思维（Chain-of-Thought，CoT）监督微调来提升视觉语言模型（VLMs）的推理能力，这种方法依赖于精心标注的训练数据。然而，这种训练范式可能导致模型过拟合和认知僵化，限制了模型在不同领域之间转移视觉推理技能的能力，以及其在现实世界中的应用。为了克服这些限制，本文提出了Reason-RFT，一个新颖的强化微调框架，旨在显著提升视觉推理任务的泛化能力。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
Reason-RFT引入了一个两阶段的训练框架：首先，通过使用精心挑选的CoT数据进行监督微调（SFT），激活VLMs的推理潜力；其次，通过基于组相对策略优化（GRPO）的强化学习，生成多个推理-响应对，显著提升视觉推理任务的泛化能力。

💡 创新点2
为了评估Reason-RFT的视觉推理能力，作者重构了一个全面的数据集，涵盖视觉计数、结构感知和空间转换三个核心领域，作为评估视觉认知、几何理解和跨任务泛化的基准。

### 📈 实验结果
实验结果表明Reason-RFT具有三个关键优势：
1. 性能提升：在多个任务上达到最先进的性能，超过大多数主流的开源和专有模型；
2. 泛化优势：在多种任务和领域上保持稳健的性能，超过其他训练范式；
3. 数据效率：在少量样本学习场景中表现出色，同时超过全数据集SFT基线。

### 💬 可借鉴之处
本文提出的Reason-RFT框架为视觉推理任务提供了一种新的训练范式，通过结合监督微调和强化学习的互补优势，有效提升了VLMs的视觉推理能力。此外，论文中重构的数据集为评估视觉推理模型提供了一个全面的基准，有助于未来研究的进一步发展。

