# Paper List from BIB File: tmppqmmjdk9.bib
- [24/05] **Instruction-Guided Visual Masking**  
[[Paper](http://arxiv.org/pdf/2405.19783v2)] [[Code/Page](https://github.com/2toinf/IVM.)] [[TLDR/Notes](#instruction-guided-visual-masking)]

- [25/05] **OpenThinkIMG: Learning to Think with Images via Visual Tool Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.08617v1)] [[Code/Page]()] [[TLDR/Notes](#openthinkimg--learning-to-think-with-images-via-visual-tool-reinforcement-learning)]

- [25/05] **Visual Agentic Reinforcement Fine-Tuning**  
[[Paper](http://arxiv.org/pdf/2505.14246v1)] [[Code/Page]()] [[TLDR/Notes](#visual-agentic-reinforcement-fine-tuning)]

- [25/05] **Grounded Reinforcement Learning for Visual Reasoning**  
[[Paper](http://arxiv.org/pdf/2505.23678v1)] [[Code/Page]()] [[TLDR/Notes](#grounded-reinforcement-learning-for-visual-reasoning)]

- [25/02] **MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs**  
[[Paper](http://arxiv.org/pdf/2502.17422v1)] [[Code/Page]()] [[TLDR/Notes](#mllms-know-where-to-look--training-free-perception-of-small-visual-details-with-multimodal-llms)]

- [25/05] **DeepEyes: Incentivizing "Thinking with Images" via Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.14362v2)] [[Code/Page](https://github.com/Visual-Agent/DeepEyes.)] [[TLDR/Notes](#deepeyes--incentivizing--thinking-with-images--via-reinforcement-learning)]

- [25/05] **Visual Abstract Thinking Empowers Multimodal Reasoning**  
[[Paper](http://arxiv.org/pdf/2505.20164v2)] [[Code/Page]()] [[TLDR/Notes](#visual-abstract-thinking-empowers-multimodal-reasoning)]

- [25/05] **Visual Thoughts: A Unified Perspective of Understanding Multimodal Chain-of-Thought**  
[[Paper](http://arxiv.org/pdf/2505.15510v1)] [[Code/Page]()] [[TLDR/Notes](#visual-thoughts--a-unified-perspective-of-understanding-multimodal-chain-of-thought)]

- [24/11] **ZoomEye: Enhancing Multimodal LLMs with Human-Like Zooming Capabilities through Tree-Based Image Exploration**  
[[Paper](http://arxiv.org/pdf/2411.16044v1)] [[Code/Page](https://github.com/om-ai-lab/ZoomEye}{https://github.com/om-ai-lab/ZoomEye}.)] [[TLDR/Notes](#zoomeye--enhancing-multimodal-llms-with-human-like-zooming-capabilities-through-tree-based-image-exploration)]

- [24/06] **Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models**  
[[Paper](http://arxiv.org/pdf/2406.09403v3)] [[Code/Page](https://visualsketchpad.github.io/.)] [[TLDR/Notes](#visual-sketchpad--sketching-as-a-visual-chain-of-thought-for-multimodal-language-models)]

- [25/03] **Retrieval-Augmented Perception: High-Resolution Image Perception Meets Visual RAG**  
[[Paper](http://arxiv.org/pdf/2503.01222v2)] [[Code/Page]()] [[TLDR/Notes](#retrieval-augmented-perception--high-resolution-image-perception-meets-visual-rag)]

- [25/06] **Reinforcing Spatial Reasoning in Vision-Language Models with Interwoven Thinking and Visual Drawing**  
[[Paper](http://arxiv.org/pdf/2506.09965v2)] [[Code/Page]()] [[TLDR/Notes](#reinforcing-spatial-reasoning-in-vision-language-models-with-interwoven-thinking-and-visual-drawing)]

- [25/04] **DyFo: A Training-Free Dynamic Focus Visual Search for Enhancing LMMs in Fine-Grained Visual Understanding**  
[[Paper](http://arxiv.org/pdf/2504.14920v1)] [[Code/Page](https://github.com/PKU-ICST-MIPL/DyFo_CVPR2025)] [[TLDR/Notes](#dyfo--a-training-free-dynamic-focus-visual-search-for-enhancing-lmms-in-fine-grained-visual-understanding)]

- [23/12] **V*: Guided Visual Search as a Core Mechanism in Multimodal LLMs**  
[[Paper](http://arxiv.org/pdf/2312.14135v2)] [[Code/Page](https://github.com/penghao-wu/vstar.)] [[TLDR/Notes](#v*--guided-visual-search-as-a-core-mechanism-in-multimodal-llms)]

- [24/06] **From the Least to the Most: Building a Plug-and-Play Visual Reasoner via Data Synthesis**  
[[Paper](http://arxiv.org/pdf/2406.19934v2)] [[Code/Page](https://github.com/steven-ccq/VisualReasoner.)] [[TLDR/Notes](#from-the-least-to-the-most--building-a-plug-and-play-visual-reasoner-via-data-synthesis)]

- [25/05] **Chain-of-Focus: Adaptive Visual Search and Zooming for Multimodal Reasoning via RL**  
[[Paper](http://arxiv.org/pdf/2505.15436v1)] [[Code/Page]()] [[TLDR/Notes](#chain-of-focus--adaptive-visual-search-and-zooming-for-multimodal-reasoning-via-rl)]

- [25/05] **VLM-R$^3$: Region Recognition, Reasoning, and Refinement for Enhanced Multimodal Chain-of-Thought**  
[[Paper](http://arxiv.org/pdf/2505.16192v2)] [[Code/Page]()] [[TLDR/Notes](#vlm-r$^3$--region-recognition--reasoning--and-refinement-for-enhanced-multimodal-chain-of-thought)]



# TLDR/Notes
## instruction-guided-visual-masking
### Abstract
Instruction following is crucial in contemporary LLM. However, when extended
to multimodal setting, it often suffers from misalignment between specific
textual instruction and targeted local region of an image. To achieve more
accurate and nuanced multimodal instruction following, we introduce
Instruction-guided Visual Masking (IVM), a new versatile visual grounding model
that is compatible with diverse multimodal models, such as LMM and robot model.
By constructing visual masks for instruction-irrelevant regions, IVM-enhanced
multimodal models can effectively focus on task-relevant image regions to
better align with complex instructions. Specifically, we design a visual
masking data generation pipeline and create an IVM-Mix-1M dataset with 1
million image-instruction pairs. We further introduce a new learning technique,
Discriminator Weighted Supervised Learning (DWSL) for preferential IVM training
that prioritizes high-quality data samples. Experimental results on generic
multimodal tasks such as VQA and embodied robotic control demonstrate the
versatility of IVM, which as a plug-and-play tool, significantly boosts the
performance of diverse multimodal models, yielding new state-of-the-art results
across challenging multimodal benchmarks. Code, model and data are available at
https://github.com/2toinf/IVM.
```
### 🌟 论文解读 | 多模态指令跟随新突破：Instruction-Guided Visual Masking

### 📌 背景痛点/本文动机
在当代大语言模型（LLM）中，指令跟随至关重要。但当拓展到多模态场景时，常常面临特定文本指令与图像目标局部区域不匹配的问题。为了实现更精准、细致的多模态指令跟随，解决文本指令和图像区域的对齐难题，本文提出了Instruction - guided Visual Masking（IVM）方法。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出Instruction - guided Visual Masking（IVM）模型
IVM是一种全新的通用视觉定位模型，能与诸如大语言 - 视觉模型（LMM）、机器人模型等多种多模态模型兼容。通过为与指令无关的区域构建视觉掩码，经IVM增强的多模态模型能够有效聚焦于与任务相关的图像区域，从而更好地与复杂指令对齐。
💡 创新点2：构建数据生成 pipeline 和 IVM - Mix - 1M 数据集
设计了视觉掩码数据生成 pipeline，创建了包含100万图像 - 指令对的IVM - Mix - 1M数据集，为模型训练提供了丰富的数据支撑。
💡 创新点3：提出Discriminator Weighted Supervised Learning（DWSL）学习技术
引入了一种新的学习技术DWSL用于优先IVM训练，该技术能够优先考虑高质量的数据样本，提升训练效果。

### 📈 实验结果
在通用多模态任务（如视觉问答（VQA）和具身机器人控制）上的实验结果表明了IVM的多功能性。作为即插即用工具，IVM显著提升了多种多模态模型的性能，在具有挑战性的多模态基准测试中取得了新的最先进成果。

### 💬 可借鉴之处
1. 模型兼容性思路：IVM兼容多种多模态模型的设计思路，为后续开发通用型多模态增强工具提供了参考，可思考如何让工具在不同多模态模型间高效适配。
2. 数据构建方法：其设计的视觉掩码数据生成 pipeline 和大规模数据集构建方式，对于需要大量数据支撑的多模态模型训练任务，提供了数据层面的构建范例，可学习如何高效生成针对性数据。
3. 训练技术创新：DWSL这种优先考虑高质量数据样本的训练技术，为模型训练过程中数据利用效率的提升提供了新方向，在后续模型训练优化中可借鉴该思路来处理数据样本的优先级问题。
4. 即插即用工具属性：IVM作为即插即用工具提升多模态模型性能的模式，为多模态领域工具开发提供了新的产品形态参考，可探索更多此类能快速赋能现有模型的工具型方法。
```

## openthinkimg--learning-to-think-with-images-via-visual-tool-reinforcement-learning
### Abstract
While humans can flexibly leverage interactive visual cognition for complex
problem-solving, enabling Large Vision-Language Models (LVLMs) to learn
similarly adaptive behaviors with visual tools remains challenging. A
significant hurdle is the current lack of standardized infrastructure, which
hinders integrating diverse tools, generating rich interaction data, and
training robust agents effectively. To address these gaps, we introduce
OpenThinkIMG, the first open-source, comprehensive end-to-end framework for
tool-augmented LVLMs. It features standardized vision tool interfaces, scalable
trajectory generation for policy initialization, and a flexible training
environment. Furthermore, considering supervised fine-tuning (SFT) on static
demonstrations offers limited policy generalization for dynamic tool
invocation, we propose a novel reinforcement learning (RL) framework V-ToolRL
to train LVLMs to learn adaptive policies for invoking external vision tools.
V-ToolRL enables LVLMs to autonomously discover optimal tool-usage strategies
by directly optimizing for task success using feedback from tool interactions.
We empirically validate V-ToolRL on challenging chart reasoning tasks. Our
RL-trained agent, built upon a Qwen2-VL-2B, significantly outperforms its
SFT-initialized counterpart (+28.83 points) and surpasses established
supervised tool-learning baselines like Taco and CogCom by an average of +12.7
points. Notably, it also surpasses prominent closed-source models like GPT-4.1
by +8.68 accuracy points. We hope OpenThinkIMG can serve as a foundational
framework for advancing dynamic, tool-augmented visual reasoning, helping the
community develop AI agents that can genuinely "think with images".
```
### 🌟 论文解读 | OpenThinkIMG：让大视觉语言模型借助视觉工具“像人类一样思考图像”

### 📌 背景痛点/本文动机
人类能够灵活运用交互式视觉认知来解决复杂问题，但让大视觉语言模型（LVLMs）以类似的自适应方式利用视觉工具却颇具挑战。当前缺乏标准化基础设施是一大障碍，这阻碍了多样工具的整合、丰富交互数据的生成以及鲁棒智能体的高效训练。同时，仅依靠静态演示的有监督微调（SFT），在动态工具调用时政策泛化能力有限。为填补这些空白，论文提出了相应解决方案。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出OpenThinkIMG框架  
OpenThinkIMG是首个用于工具增强型大视觉语言模型的开源、全面的端到端框架。它具备标准化视觉工具接口，能实现策略初始化的可扩展轨迹生成，还有灵活的训练环境，为工具增强LVLMs提供了基础支撑，解决了基础设施缺失的问题。

💡 创新点2：提出V - ToolRL强化学习框架  
考虑到静态演示的有监督微调对动态工具调用的策略泛化不足，提出V - ToolRL。该框架让LVLMs通过利用工具交互的反馈直接优化任务成功率，自主发现最优工具使用策略，以此训练LVLMs学习调用外部视觉工具的自适应策略。

### 📈 实验结果
在具有挑战性的图表推理任务上对V - ToolRL进行了实证验证。基于Qwen2 - VL - 2B构建的经RL训练的智能体，显著超越其SFT初始化的对应版本（提升28.83分）；平均超过像Taco和CogCom这样的有监督工具学习基线12.7分；甚至超过了如GPT - 4.1这样的知名闭源模型，准确率提升8.68分。

### 💬 可借鉴之处
1. 基础设施建设方面：OpenThinkIMG提供了标准化视觉工具接口等基础设施构建思路，为后续工具增强型视觉语言模型研究提供了可参考的框架范式，便于研究者整合工具、生成数据和训练智能体。
2. 训练方法创新：V - ToolRL针对有监督微调在动态工具调用泛化不足的问题，提出强化学习方案，为解决类似的动态场景下模型策略学习问题提供了新的思路，即利用交互反馈优化任务目标来让模型自主学习策略。
3. 实验验证角度：在图表推理任务上的全面对比实验，为验证工具增强和强化学习方法在视觉语言任务中的有效性提供了范例，后续研究在验证新方法时可借鉴这种多维度对比（与自身SFT版本、已有监督基线、闭源强模型对比）的方式。
```

## visual-agentic-reinforcement-fine-tuning
### Abstract
A key trend in Large Reasoning Models (e.g., OpenAI's o3) is the native
agentic ability to use external tools such as web browsers for searching and
writing/executing code for image manipulation to think with images. In the
open-source research community, while significant progress has been made in
language-only agentic abilities such as function calling and tool integration,
the development of multi-modal agentic capabilities that involve truly thinking
with images, and their corresponding benchmarks, are still less explored. This
work highlights the effectiveness of Visual Agentic Reinforcement Fine-Tuning
(Visual-ARFT) for enabling flexible and adaptive reasoning abilities for Large
Vision-Language Models (LVLMs). With Visual-ARFT, open-source LVLMs gain the
ability to browse websites for real-time information updates and write code to
manipulate and analyze input images through cropping, rotation, and other image
processing techniques. We also present a Multi-modal Agentic Tool Bench (MAT)
with two settings (MAT-Search and MAT-Coding) designed to evaluate LVLMs'
agentic search and coding abilities. Our experimental results demonstrate that
Visual-ARFT outperforms its baseline by +18.6% F1 / +13.0% EM on MAT-Coding and
+10.3% F1 / +8.7% EM on MAT-Search, ultimately surpassing GPT-4o. Visual-ARFT
also achieves +29.3 F1% / +25.9% EM gains on existing multi-hop QA benchmarks
such as 2Wiki and HotpotQA, demonstrating strong generalization capabilities.
Our findings suggest that Visual-ARFT offers a promising path toward building
robust and generalizable multimodal agents.
```
### 🌟 论文解读 | 解锁多模态智能新姿势：Visual-ARFT让大模型“看图思考+工具协同”

### 📌 背景痛点/本文动机
在大模型浪潮中，ClosedAI等机构的大模型（如o3）已展现出**原生智能体能力**——能用浏览器搜索、写/执行图像操作代码来实现“以图思考”。但开源社区里，纯语言类智能体能力（如函数调用）虽有进展，**真正融合图像思维的多模态智能体能力及对应评测基准**却鲜有人深入探索。LVLMs（大视觉-语言模型）要成为灵活的多模态智能体，需要突破“只会看图文、不会主动用工具处理/获取信息”的局限，这就是本文要解决的核心痛点。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：Visual-ARFT技术范式  
提出**视觉智能体强化微调（Visual Agentic Reinforcement Fine-Tuning）**，让开源LVLMs具备主动调用外部工具的智能体能力：一是**网页浏览**获取实时信息，二是**编写图像操作代码**（裁剪、旋转等处理与分析）。通过强化学习思路，让模型学会“何时该调用工具、怎么用工具、如何结合工具输出做决策”，实现“以图思考+工具协同”的灵活推理。  

💡 创新点2：MAT多模态智能体工具基准  
构建**Multi-modal Agentic Tool Bench（MAT）**评测套件，包含两大场景：  
- MAT-Search：评估模型“用工具搜索信息辅助多模态任务”的能力；  
- MAT-Coding：评估模型“编写图像操作代码并执行”的能力。  
填补了多模态智能体工具能力评测的空白，为后续研究提供统一“考场”。  


### 📈 实验结果
在自设基准MAT上，Visual-ARFT对比基线模型优势显著：  
- MAT-Coding任务：F1提升+18.6%、EM（精确匹配）提升+13.0%；  
- MAT-Search任务：F1提升+10.3%、EM提升+8.7%；  
甚至**超越GPT-4o**，证明技术在多模态工具能力上的竞争力。  

在跨领域泛化性测试（2Wiki、HotpotQA等多跳问答基准）中，Visual-ARFT也斩获F1+29.3%、EM+25.9%的增益，验证“工具协同式多模态推理”具备强泛化潜力。  


### 💬 可借鉴之处
1. **技术路线可复用**：Visual-ARFT的“强化微调+工具调用”范式，为开源LVLMs向多模态智能体进化提供了落地路径，其他研究可参考该思路扩展到音频、视频等更多模态；  
2. **评测基准价值**：MAT填补多模态智能体工具能力评测空白，后续研究可基于MAT做更细粒度的能力拆解或扩展场景；  
3. **工业落地启发**：若要让大模型在实际业务（如电商图搜、医疗影像分析）中“主动干活”，“教模型用工具”+“强化学习引导决策”是值得尝试的工程思路。  
```

## grounded-reinforcement-learning-for-visual-reasoning
### Abstract
While reinforcement learning (RL) over chains of thought has significantly
advanced language models in tasks such as mathematics and coding, visual
reasoning introduces added complexity by requiring models to direct visual
attention, interpret perceptual inputs, and ground abstract reasoning in
spatial evidence. We introduce ViGoRL (Visually Grounded Reinforcement
Learning), a vision-language model trained with RL to explicitly anchor each
reasoning step to specific visual coordinates. Inspired by human visual
decision-making, ViGoRL learns to produce spatially grounded reasoning traces,
guiding visual attention to task-relevant regions at each step. When
fine-grained exploration is required, our novel multi-turn RL framework enables
the model to dynamically zoom into predicted coordinates as reasoning unfolds.
Across a diverse set of visual reasoning benchmarks--including SAT-2 and BLINK
for spatial reasoning, V*bench for visual search, and ScreenSpot and
VisualWebArena for web-based grounding--ViGoRL consistently outperforms both
supervised fine-tuning and conventional RL baselines that lack explicit
grounding mechanisms. Incorporating multi-turn RL with zoomed-in visual
feedback significantly improves ViGoRL's performance on localizing small GUI
elements and visual search, achieving 86.4% on V*Bench. Additionally, we find
that grounding amplifies other visual behaviors such as region exploration,
grounded subgoal setting, and visual verification. Finally, human evaluations
show that the model's visual references are not only spatially accurate but
also helpful for understanding model reasoning steps. Our results show that
visually grounded RL is a strong paradigm for imbuing models with
general-purpose visual reasoning.
```
### 🌟 论文解读 | 视觉推理新范式：ViGoRL的视觉锚定强化学习

### 📌 背景痛点/本文动机
在强化学习（RL）推动语言模型在数学、编码等任务取得进展的同时，视觉推理因需引导视觉注意力、解读感知输入并将抽象推理锚定在空间证据上，面临额外复杂性。现有方法缺乏显式的视觉锚定机制，在需要细粒度探索的视觉推理任务（如空间推理、视觉搜索、网页元素定位等）中表现受限。因此，如何让模型在每一步推理中显式地将推理步骤锚定到特定视觉坐标，成为视觉推理领域亟待解决的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出ViGoRL（Visually Grounded Reinforcement Learning）框架  
ViGoRL是一种结合强化学习训练的视觉-语言模型，它显式地将每个推理步骤锚定到特定视觉坐标。受人类视觉决策过程启发，ViGoRL学习生成空间锚定的推理轨迹，在每一步引导视觉注意力到与任务相关的区域，让抽象推理有了空间维度的“落脚点”。  

💡 创新点2：多轮强化学习+动态缩放机制  
当任务需要细粒度探索时，ViGoRL的多轮RL框架允许模型在推理过程中动态地放大到预测坐标。这种机制让模型能根据推理进展，逐步聚焦到更精确的区域，特别适用于小GUI元素定位、视觉搜索等对局部细节要求高的任务。  

### 📈 实验结果
1. 多基准测试领先：在空间推理（如SAT - 2、BLINK）、视觉搜索（V*bench）、网页锚定（ScreenSpot、VisualWebArena）等多样化视觉推理基准测试中，ViGoRL持续超越有监督微调方法和缺乏显式锚定机制的传统RL基线。  
2. 细分任务突破：在V*Bench视觉搜索任务上，结合多轮RL与缩放视觉反馈的ViGoRL达到86.4%的准确率，在小GUI元素定位等任务上表现突出。  
3. 行为增强与人类评估：锚定机制还放大了区域探索、锚定子目标设定、视觉验证等其他视觉行为；人类评估显示，模型的视觉参考不仅空间准确，还能帮助理解推理步骤。  

### 💬 可借鉴之处
1. 视觉锚定范式：将抽象推理与空间证据显式锚定的思路，为通用视觉推理模型的构建提供了强范式，可启发后续视觉-语言任务中“推理-视觉”关联机制的设计。  
2. 多轮交互与动态聚焦：多轮RL结合动态缩放的机制，为需要细粒度探索的视觉任务（如界面元素交互、复杂场景搜索）提供了交互式、渐进式的解决思路，可迁移到类似需逐步聚焦的视觉场景任务中。  
3. 行为与可解释性：锚定带来的视觉行为增强（如区域探索、子目标设定）以及人类可理解的推理参考，为提升模型可解释性和行为可分析性提供了方向，在追求模型透明性的研究中值得借鉴。  
```

## mllms-know-where-to-look--training-free-perception-of-small-visual-details-with-multimodal-llms
### Abstract
Multimodal Large Language Models (MLLMs) have experienced rapid progress in
visual recognition tasks in recent years. Given their potential integration
into many critical applications, it is important to understand the limitations
of their visual perception. In this work, we study whether MLLMs can perceive
small visual details as effectively as large ones when answering questions
about images. We observe that their performance is very sensitive to the size
of the visual subject of the question, and further show that this effect is in
fact causal by conducting an intervention study. Next, we study the attention
patterns of MLLMs when answering visual questions, and intriguingly find that
they consistently know where to look, even when they provide the wrong answer.
Based on these findings, we then propose training-free visual intervention
methods that leverage the internal knowledge of any MLLM itself, in the form of
attention and gradient maps, to enhance its perception of small visual details.
We evaluate our proposed methods on two widely-used MLLMs and seven visual
question answering benchmarks and show that they can significantly improve
MLLMs' accuracy without requiring any training. Our results elucidate the risk
of applying MLLMs to visual recognition tasks concerning small details and
indicate that visual intervention using the model's internal state is a
promising direction to mitigate this risk.
```
### 🌟 论文解读 | MLLMs能否精准捕捉微小视觉细节？无训练干预方法给出新方向

### 📌 背景痛点/本文动机
近年来，多模态大语言模型（MLLMs）在视觉识别任务中取得了快速进展。然而，由于其可能被集成到诸多关键应用场景中，了解它们在视觉感知方面的局限性就变得至关重要。其中一个关键问题是：当回答关于图像的问题时，MLLMs能否像感知大的视觉对象那样有效地感知微小视觉细节？这一问题关乎MLLMs在涉及微小细节的视觉识别任务中的可靠性，也是本文研究的核心动机——探究MLLMs对微小视觉细节的感知能力、背后原因，并尝试解决其存在的不足。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：揭示视觉主体大小对MLLMs性能的因果影响
通过开展干预性研究，深入分析MLLMs在回答视觉问题时性能与视觉主体大小的关系，明确了其性能对问题中视觉主体大小十分敏感这一现象存在因果性，不是偶然因素导致，为后续针对性改进提供了基础认知。

💡 创新点2：发现MLLMs注意力模式的“知而不准”现象
研究MLLMs回答视觉问题时的注意力模式，有趣地发现即便模型给出错误答案，它们也始终“知道该看哪里”（即注意力能聚焦到对应区域）。这一发现为利用模型内部状态来改进性能提供了关键依据。

💡 创新点3：提出无训练的视觉干预方法
基于前面发现的MLLMs注意力和梯度图等内部知识，提出无需训练的视觉干预方法。该方法借助模型自身内部状态，增强其对微小视觉细节的感知能力，为提升MLLMs在微小细节视觉任务表现开辟了新路径，且无需额外训练过程，对已有模型易用性强。

### 📈 实验结果
在两个广泛使用的MLLMs（未明确提及具体模型但属于主流多模态大模型范畴）以及七个视觉问答基准测试集上对所提方法进行评估。结果显示，这些无训练的视觉干预方法能够显著提高MLLMs的准确率，有力证明了方法的有效性，说明利用模型内部状态进行视觉干预在缓解微小细节感知不足风险方面是可行且有潜力的。

### 💬 可借鉴之处
1. 研究思路上，先深入剖析模型在特定视觉任务（微小细节感知）中的局限性及背后规律（如视觉主体大小影响、注意力模式特点），这种从问题本质和模型内在机制出发的研究方式，为探索其他AI模型能力边界和改进方向提供了范例，可借鉴来分析模型在不同细分任务下的表现与内在逻辑。
2. 方法创新上，提出的无训练视觉干预方法，利用模型自身内部知识（注意力、梯度图）来增强性能，无需额外训练数据和训练过程，这种轻量级且基于模型内在状态的优化思路，对于已有部署的大模型快速提升特定能力具有参考价值，在实际工业应用或模型优化迭代中，可思考如何挖掘模型内部信息来做针对性增强。
3. 实验验证维度，选择多个主流MLLMs和多个视觉问答基准测试，保证了结果的通用性和说服力，在做相关模型改进或方法验证时，可学习这种多模型、多数据集的全面评估方式，以充分证明方法有效性。 
```

## deepeyes--incentivizing--thinking-with-images--via-reinforcement-learning
### Abstract
Large Vision-Language Models (VLMs) have shown strong capabilities in
multimodal understanding and reasoning, yet they are primarily constrained by
text-based reasoning processes. However, achieving seamless integration of
visual and textual reasoning which mirrors human cognitive processes remains a
significant challenge. In particular, effectively incorporating advanced visual
input processing into reasoning mechanisms is still an open question. Thus, in
this paper, we explore the interleaved multimodal reasoning paradigm and
introduce DeepEyes, a model with "thinking with images" capabilities
incentivized through end-to-end reinforcement learning without the need for
cold-start SFT. Notably, this ability emerges natively within the model itself,
leveraging its inherent grounding ability as a tool instead of depending on
separate specialized models. Specifically, we propose a tool-use-oriented data
selection mechanism and a reward strategy to encourage successful tool-assisted
reasoning trajectories. DeepEyes achieves significant performance gains on
fine-grained perception and reasoning benchmarks and also demonstrates
improvement in grounding, hallucination, and mathematical reasoning tasks.
Interestingly, we observe the distinct evolution of tool-calling behavior from
initial exploration to efficient and accurate exploitation, and diverse
thinking patterns that closely mirror human visual reasoning processes. Code is
available at https://github.com/Visual-Agent/DeepEyes.
```
### 🌟 论文解读 | DeepEyes：用强化学习赋能“以图思考”的多模态推理新范式

### 📌 背景痛点/本文动机
大视觉-语言模型（VLMs）在多模态理解与推理方面展现出强大能力，但目前主要受限于基于文本的推理流程。而实现类人认知过程中视觉与文本推理的无缝融合仍是重大挑战，尤其是把先进视觉输入处理有效融入推理机制这一问题尚未解决。所以本文探索交错式多模态推理范式，期望让模型具备“以图思考”能力，突破现有VLMs在推理方式上的局限。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出无需冷启动SFT的端到端强化学习激励方案  
DeepEyes不依赖冷启动的监督微调（SFT），通过端到端强化学习来激发模型“以图思考”的能力。这种能力是模型原生涌现的，借助自身固有的接地（grounding）能力当作工具，而非依赖单独的专用模型，让视觉信息处理自然融入推理过程。  

💡 创新点2：面向工具使用的数据选择机制与奖励策略  
设计了面向工具使用的数据选择机制，能针对性地筛选数据来助力模型学习工具辅助推理；同时搭配奖励策略，鼓励模型产生成功的工具辅助推理轨迹，从数据和反馈层面双管齐下，推动模型掌握高效推理方式。  

### 📈 实验结果
DeepEyes在细粒度感知和推理基准测试上取得显著性能提升，在接地（grounding）、幻觉（hallucination）以及数学推理等任务中也展现出改进效果。更有趣的是，观测到模型的工具调用行为从初始探索阶段向高效精准利用阶段的明显进化，还出现了多种贴近人类视觉推理过程的思维模式，验证了方法在多模态推理能力塑造上的有效性。  

### 💬 可借鉴之处
1. 强化学习在多模态推理中激励特殊能力（如“以图思考”）的思路，为突破纯文本推理限制提供了新范式参考，可启发后续探索类人认知式的多模态融合推理。  
2. 面向工具使用的数据选择与奖励设计策略，为模型在工具辅助类任务上的训练提供了可复用的方法论，在需要工具协作完成复杂推理的场景中具有借鉴价值。  
3. 对工具调用行为演化和类人思维模式的观测分析，为理解模型多模态推理能力形成过程提供了视角，有助于后续更深入探究模型行为机理与能力成长规律。  
```

## visual-abstract-thinking-empowers-multimodal-reasoning
### Abstract
Images usually convey richer detail than text, but often include redundant
information which potentially downgrades multimodal reasoning performance. When
faced with lengthy or complex messages, humans tend to employ abstract thinking
to convert them into simple and concise abstracts. Inspired by this cognitive
strategy, we introduce Visual Abstract Thinking (VAT), a novel thinking
paradigm that prompts Multimodal Large Language Models (MLLMs) with visual
abstract instead of explicit verbal thoughts or elaborate guidance, permitting
a more concentrated visual reasoning mechanism. Explicit thinking, such as
Chain-of-thought (CoT) or tool-augmented approaches, increases the complexity
of reasoning process via inserting verbose intermediate steps, external
knowledge or visual information. In contrast, VAT reduces redundant visual
information and encourages models to focus their reasoning on more essential
visual elements. Experimental results show that VAT consistently empowers
different models, and achieves an average gain of 17% over GPT-4o baseline by
employing diverse types of visual abstracts, demonstrating that VAT can enhance
visual reasoning abilities for MLLMs regarding conceptual, structural and
relational reasoning tasks. VAT is also compatible with CoT in
knowledge-intensive multimodal reasoning tasks. These findings highlight the
effectiveness of visual reasoning via abstract thinking and encourage further
exploration of more diverse reasoning paradigms from the perspective of human
cognition.
```
### 🌟 论文解读 | 视觉抽象思维：为多模态推理注入新活力

### 📌 背景痛点/本文动机
在多模态推理场景中，图像虽能传递比文本更丰富的细节，但也存在冗余信息，这些冗余信息可能会降低多模态推理的性能。而人类在面对冗长或复杂信息时，会运用抽象思维将其转化为简洁的抽象内容。受此认知策略启发，论文希望探索一种新的方式，让多模态大语言模型（MLLMs）能更高效地进行视觉推理，避免传统显式思维（如思维链CoT或工具增强方法）因引入冗长中间步骤、外部知识或视觉信息而增加推理复杂度的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出视觉抽象思维（VAT）范式  
引入Visual Abstract Thinking（VAT）这一新颖的思维范式，不再用显式的语言思考或复杂指导，而是以视觉抽象来提示多模态大语言模型，让模型能聚焦到更关键的视觉元素上，减少冗余视觉信息对推理的干扰，构建更集中的视觉推理机制。  

💡 创新点2：VAT与CoT的兼容性探索  
在知识密集型多模态推理任务中，验证了VAT与CoT结合的可行性，展现出该范式在不同场景下的灵活应用潜力，为多模态推理任务提供了更丰富的解决思路。  

### 📈 实验结果
实验表明VAT能持续赋能不同的模型，通过采用多种类型的视觉抽象，相比GPT - 4o基线平均提升了17%。并且在概念、结构和关系推理等任务上，VAT增强了多模态大语言模型的视觉推理能力，有力地证明了通过抽象思维进行视觉推理的有效性。  

### 💬 可借鉴之处
从人类认知角度为多模态推理范式提供了新方向，启发研究者探索更多样化的推理范式；VAT所体现的“简化冗余、聚焦关键”思路，可迁移到其他需要处理冗余信息的多模态任务中；其与CoT兼容的特性，也为现有多模态推理技术栈的优化和拓展提供了参考，让开发者在构建多模态应用时能考虑结合这种抽象思维方式来提升性能。
```

## visual-thoughts--a-unified-perspective-of-understanding-multimodal-chain-of-thought
### Abstract
Large Vision-Language Models (LVLMs) have achieved significant success in
multimodal tasks, with multimodal chain-of-thought (MCoT) further enhancing
performance and interpretability. Recent MCoT methods fall into two categories:
(i) Textual-MCoT (T-MCoT), which takes multimodal input and produces textual
output; and (ii) Interleaved-MCoT (I-MCoT), which generates interleaved
image-text outputs. Despite advances in both approaches, the mechanisms driving
these improvements are not fully understood. To fill this gap, we first reveal
that MCoT boosts LVLMs by incorporating visual thoughts, which convey image
information to the reasoning process regardless of the MCoT format, depending
only on clarity and conciseness of expression. Furthermore, to explore visual
thoughts systematically, we define four distinct forms of visual thought
expressions and analyze them comprehensively. Our findings demonstrate that
these forms differ in clarity and conciseness, yielding varying levels of MCoT
improvement. Additionally, we explore the internal nature of visual thoughts,
finding that visual thoughts serve as intermediaries between the input image
and reasoning to deeper transformer layers, enabling more advanced visual
information transmission. We hope that the visual thoughts can inspire further
breakthroughs for future MCoT research.
```
### 🌟 论文解读 | 揭秘多模态思维链背后的“视觉思维”：统一视角下的理解与探索

### 📌 背景痛点/本文动机
大视觉-语言模型（LVLMs）在多模态任务中取得了显著成功，多模态思维链（MCoT）进一步提升了模型性能与可解释性。现有的MCoT方法主要分为文本型（T-MCoT，输入多模态、输出文本）和交错型（I-MCoT，生成图文交错输出）两类。然而，这两类方法性能提升背后的驱动机制尚未被充分理解。为填补这一认知空白，论文聚焦于“视觉思维（visual thoughts）”这一核心概念，探索其在不同MCoT形式中如何发挥作用，进而推动LVLMs能力进阶。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：揭示“视觉思维”是MCoT性能提升的关键  
论文首次指出，无论MCoT采用T-MCoT还是I-MCoT形式，**视觉思维**才是性能提升的核心——它能将图像信息传递到推理过程中，且这一传递效果仅取决于表达的“清晰性”与“简洁性”，而非具体MCoT格式。这打破了对不同MCoT形式“表面差异”的关注，直指底层统一的提升逻辑。  

💡 创新点2：系统定义并分析四种视觉思维表达形式  
为深入研究视觉思维，论文明确提出四种截然不同的视觉思维表达形式，并从清晰性、简洁性维度展开全面分析。通过对比发现，不同形式在这两个维度的表现差异，会直接导致MCoT性能提升幅度的不同。这为后续针对性设计MCoT策略提供了分类依据与优化方向。  

💡 创新点3：剖析视觉思维的内在本质  
论文进一步探索视觉思维的“内部属性”，发现它在输入图像与更深层Transformer推理之间扮演“中介”角色——能让更复杂的视觉信息在模型中高效传递，支撑更深入的推理过程。这从模型内部机制层面，解释了视觉思维为何能成为MCoT的“动力源”。  


### 📈 实验结果
论文通过系列实验验证了上述结论：  
1. 不同视觉思维表达形式在清晰性、简洁性上的差异，确实对应着MCoT性能提升的不同幅度——清晰且简洁的表达形式，能更显著地推动任务表现；  
2. 对视觉思维“中介作用”的验证实验，也佐证了其在视觉信息向深层Transformer传递时的关键价值，从模型内部流程角度强化了理论说服力。  


### 💬 可借鉴之处
1. **认知升级**：跳出“T-MCoT vs I-MCoT”的形式之争，聚焦“视觉思维”这一统一视角，为多模态思维链研究提供了全新认知框架；  
2. **方法论指导**：四种视觉思维表达形式的分类与分析，为后续设计更高效的MCoT策略提供了“清晰性+简洁性”的优化锚点；  
3. **机制理解**：对视觉思维内在本质的剖析，帮助研究者从模型层级理解多模态推理的信息流动逻辑，为未来LVLMs架构优化、训练策略设计等提供了机制层面的启发。  

总之，这篇论文以“视觉思维”为线索，串联起多模态思维链的形式、效果与内在机制，为MCoT乃至整个多模态推理领域的研究打开了更具深度的探索维度。
```

## zoomeye--enhancing-multimodal-llms-with-human-like-zooming-capabilities-through-tree-based-image-exploration
### Abstract
An image, especially with high-resolution, typically consists of numerous
visual elements, ranging from dominant large objects to fine-grained detailed
objects. When perceiving such images, multimodal large language models~(MLLMs)
face limitations due to the restricted input resolution of the pretrained
vision encoder and the cluttered, dense context of the image, resulting in a
focus on primary objects while easily overlooking detailed ones. In this paper,
we propose Zoom Eye, a tree search algorithm designed to navigate the
hierarchical and visual nature of images to capture relevant information. Zoom
Eye conceptualizes an image as a tree, with each children node representing a
zoomed sub-patch of the parent node and the root represents the overall image.
Moreover, Zoom Eye is model-agnostic and training-free, so it enables any MLLMs
to simulate human zooming actions by searching along the image tree from root
to leaf nodes, seeking out pertinent information, and accurately responding to
related queries. We experiment on a series of elaborate high-resolution
benchmarks and the results demonstrate that Zoom Eye not only consistently
improves the performance of a series base MLLMs with large margin~(e.g.,
LLaVA-v1.5-7B increases by 34.57\% on $V^*$ Bench and 17.88\% on HR-Bench), but
also enables small 7B MLLMs to outperform strong large models such as GPT-4o.
Our code is available at
\href{https://github.com/om-ai-lab/ZoomEye}{https://github.com/om-ai-lab/ZoomEye}.
```
### 🌟 论文解读 | ZoomEye：为多模态大模型赋予类人“变焦观察”能力，突破高分辨率图像理解瓶颈

### 📌 背景痛点/本文动机
在处理高分辨率图像时，多模态大语言模型（MLLMs）面临着显著挑战。一方面，预训练视觉编码器的输入分辨率存在限制；另一方面，高分辨率图像中元素密集且繁杂，导致模型往往只能关注到主要物体，而容易忽略细节信息。这种“顾大失细”的问题极大限制了MLLMs对复杂图像场景的理解与响应能力，因此亟需一种能让模型像人类观察图像时“变焦查看细节”的机制来突破瓶颈。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：树形图像探索架构设计  
ZoomEye 将图像概念化为一棵“树”结构：根节点代表完整的图像，每个子节点对应父节点区域的一个“变焦子块”（zoomed sub - patch）。这种结构天然契合图像从整体到局部的层级化视觉特性，为模型探索图像信息提供了清晰的层级导航路径。  

💡 创新点2：模型无关且无训练开销的树搜索算法  
ZoomEye 是“模型无关”（model - agnostic）且“无训练”（training - free）的。它不依赖特定MLLMs的内部结构，也无需额外训练过程，能让任意MLLMs模拟人类“变焦查看”的动作——从根节点到叶节点沿着图像树搜索，主动挖掘相关信息以响应查询。这大大降低了技术落地门槛，任何现有MLLMs都能快速集成该能力。  

### 📈 实验结果
在一系列精心设计的高分辨率图像基准测试中，ZoomEye 展现出强大效能：  
- 对基础MLLMs性能提升显著，如 LLaVA - v1.5 - 7B 在 $V^*$ Bench 上性能提升 34.57%，在 HR - Bench 上提升 17.88%；  
- 让7B规模的小型MLLMs实现对GPT - 4o这类强大型模型的超越，充分验证了方法在性能增益上的幅度与跨模型优势。  

### 💬 可借鉴之处
1. 层级化结构建模思路：将复杂视觉信息以树结构组织，为处理具有层级特性的任务（不止图像，音频、文档等也可尝试）提供了结构化探索的参考范式；  
2. 无训练、模型无关的插件式增强：这种“即插即用”的设计理念，在不改变原有大模型训练与部署逻辑下提升能力，为大模型生态中工具与插件开发提供了优秀范本；  
3. 类人感知机制模拟：从人类视觉“变焦观察”中汲取灵感，为AI系统模拟人类感知与认知模式提供了新的思考角度，后续在多模态交互、人机协同等方向可延伸探索。  
```

## visual-sketchpad--sketching-as-a-visual-chain-of-thought-for-multimodal-language-models
### Abstract
Humans draw to facilitate reasoning: we draw auxiliary lines when solving
geometry problems; we mark and circle when reasoning on maps; we use sketches
to amplify our ideas and relieve our limited-capacity working memory. However,
such actions are missing in current multimodal language models (LMs). Current
chain-of-thought and tool-use paradigms only use text as intermediate reasoning
steps. In this work, we introduce Sketchpad, a framework that gives multimodal
LMs a visual sketchpad and tools to draw on the sketchpad. The LM conducts
planning and reasoning according to the visual artifacts it has drawn.
Different from prior work, which uses text-to-image models to enable LMs to
draw, Sketchpad enables LMs to draw with lines, boxes, marks, etc., which is
closer to human sketching and better facilitates reasoning. Sketchpad can also
use specialist vision models during the sketching process (e.g., draw bounding
boxes with object detection models, draw masks with segmentation models), to
further enhance visual perception and reasoning. We experiment with a wide
range of math tasks (including geometry, functions, graphs, and chess) and
complex visual reasoning tasks. Sketchpad substantially improves performance on
all tasks over strong base models with no sketching, yielding an average gain
of 12.7% on math tasks, and 8.6% on vision tasks. GPT-4o with Sketchpad sets a
new state of the art on all tasks, including V*Bench (80.3%), BLINK spatial
reasoning (83.9%), and visual correspondence (80.8%). All codes and data are in
https://visualsketchpad.github.io/.
```
### 🌟 论文解读 | 让多模态大模型拥有“视觉草稿本”：Sketchpad 开启类人推理新范式

### 📌 背景痛点/本文动机
人类在推理时常常借助绘图辅助：解几何题画辅助线、看地图做标记、用草图拓展思路并减轻工作记忆负担……但当前多模态语言模型（LMs）却缺失这类“绘图推理”能力。现有思维链（Chain-of-Thought）和工具调用范式仅依赖文本作为中间推理步骤，无法像人类一样通过“画线条、标框、做标记”等更直观的视觉手段辅助思考。为填补这一空白，论文提出 **Sketchpad** 框架，让多模态大模型拥有“视觉草稿本”并能在上面绘图推理。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：打造“视觉草稿本”，贴近人类手绘推理  
不同于以往用“文本到图像（Text-to-Image）”模型让大模型“画画”的思路，Sketchpad 让模型能直接绘制**线条、框选、标记**等更接近人类“草稿式”的视觉元素。这种方式更贴合真实推理场景（如几何题标辅助线、地图标重点），为模型提供更自然的视觉推理载体。  

💡 创新点2：融合专业视觉模型，强化感知与推理  
Sketchpad 允许在绘图过程中调用“专精视觉模型”：比如用目标检测模型画 bounding box、用分割模型画掩码（mask）等。通过整合这些工具，模型能在“画草稿”时更精准地感知视觉信息，进一步提升推理能力。  

💡 创新点3：以“视觉产物”驱动规划与推理  
模型不再只依赖文本思维链，而是**根据自己画出的视觉内容**来推进规划与推理。草稿本上的每一笔、每一个标记都成为推理过程的“中间线索”，让多模态推理更接近人类“边画边想”的认知模式。  


### 📈 实验结果
论文在**数学任务（几何、函数、图表、国际象棋等）**和**复杂视觉推理任务**中展开实验，结果显示：  
- 对比无绘图能力的强基线模型，Sketchpad 在所有任务中表现显著提升——数学任务平均增益 12.7%，视觉任务平均增益 8.6%。  
- 结合 Sketchpad 的 GPT-4o 在多个权威基准上刷新 SOTA：V*Bench 达 80.3%、BLINK 空间推理达 83.9%、视觉对应任务达 80.8%。  


### 💬 可借鉴之处
1. **认知模拟视角**：从“人类如何用绘图辅助推理”中汲取灵感，为大模型设计更贴合生物认知的推理范式，跳出纯文本思维链的局限。  
2. **工具链整合**：展示了“大模型 + 专精工具（如目标检测、分割模型）”的协作模式，为多模态工具生态构建提供参考。  
3. **任务拓展潜力**：在数学、空间推理等领域的成功，证明视觉草稿式推理对“需可视化辅助的复杂任务”有普适价值，未来可延伸到教育、设计、科研等场景。  
4. **开源生态**：项目代码与数据开源（https://visualsketchpad.github.io/），为研究者复现、改进提供了便利，推动领域快速迭代。  
```

## retrieval-augmented-perception--high-resolution-image-perception-meets-visual-rag
### Abstract
High-resolution (HR) image perception remains a key challenge in multimodal
large language models (MLLMs). To overcome the limitations of existing methods,
this paper shifts away from prior dedicated heuristic approaches and revisits
the most fundamental idea to HR perception by enhancing the long-context
capability of MLLMs, driven by recent advances in long-context techniques like
retrieval-augmented generation (RAG) for general LLMs. Towards this end, this
paper presents the first study exploring the use of RAG to address HR
perception challenges. Specifically, we propose Retrieval-Augmented Perception
(RAP), a training-free framework that retrieves and fuses relevant image crops
while preserving spatial context using the proposed Spatial-Awareness Layout.
To accommodate different tasks, the proposed Retrieved-Exploration Search
(RE-Search) dynamically selects the optimal number of crops based on model
confidence and retrieval scores. Experimental results on HR benchmarks
demonstrate the significant effectiveness of RAP, with LLaVA-v1.5-13B achieving
a 43% improvement on $V^*$ Bench and 19% on HR-Bench.
```
### 🌟 论文解读 | 高分辨率图像感知新突破：Retrieval - Augmented Perception 开启视觉RAG新思路

### 📌 背景痛点/本文动机
在多模态大语言模型（MLLMs）中，高分辨率（HR）图像感知始终是一项关键挑战。现有的方法多为专用的启发式方法，存在一定局限性。而随着针对通用大语言模型（LLMs）的长上下文技术（如检索增强生成，RAG）的发展，本文试图从增强MLLMs的长上下文能力这一最基础的思路出发，来解决高分辨率图像感知问题，这也是首次探索使用RAG来应对高分辨率感知挑战的研究。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出Retrieval - Augmented Perception（RAP）框架
RAP是一个无需训练的框架，它能够检索并融合相关的图像裁剪块，同时使用所提出的空间感知布局（Spatial - Awareness Layout）来保留空间上下文。这一框架摆脱了传统的专用启发式思路，借助RAG相关技术思路来提升高分辨率图像感知能力。
💡 创新点2：设计Retrieved - Exploration Search（RE - Search）机制
为了适应不同任务，RE - Search基于模型置信度和检索分数动态选择最优的裁剪块数量。这种动态选择机制让模型在处理不同高分辨率图像感知任务时更具灵活性和适应性。

### 📈 实验结果
在高分辨率基准测试中，RAP展现出了显著的有效性。以LLaVA - v1.5 - 13B为例，在$V^*$ Bench上实现了43%的性能提升，在HR - Bench上也有19%的性能提升，有力地证明了RAP框架在高分辨率图像感知任务中的优势。

### 💬 可借鉴之处
1. 思路创新：将针对通用LLMs的RAG技术思路迁移到多模态大语言模型的高分辨率图像感知任务中，为跨领域技术迁移提供了很好的范例，启发研究者关注不同领域技术间的联系与借鉴。
2. 无训练框架：RAP作为无训练框架，在实际应用中可以降低训练成本和资源消耗，对于资源有限或者追求快速应用新方法的场景具有借鉴意义。
3. 动态选择机制：RE - Search的动态选择裁剪块数量的机制，为处理不同任务时如何根据任务特性和模型状态来优化输入处理方式提供了参考，可应用于其他需要动态调整输入元素数量的多模态任务中。
```

## reinforcing-spatial-reasoning-in-vision-language-models-with-interwoven-thinking-and-visual-drawing
### Abstract
As textual reasoning with large language models (LLMs) has advanced
significantly, there has been growing interest in enhancing the multimodal
reasoning capabilities of large vision-language models (LVLMs). However,
existing methods primarily approach multimodal reasoning in a straightforward,
text-centric manner, where both reasoning and answer derivation are conducted
purely through text, with the only difference being the presence of multimodal
input. As a result, these methods often encounter fundamental limitations in
spatial reasoning tasks that demand precise geometric understanding and
continuous spatial tracking-capabilities that humans achieve through mental
visualization and manipulation. To address the limitations, we propose drawing
to reason in space, a novel paradigm that enables LVLMs to reason through
elementary drawing operations in the visual space. By equipping models with
basic drawing operations, including annotating bounding boxes and drawing
auxiliary lines, we empower them to express and analyze spatial relationships
through direct visual manipulation, meanwhile avoiding the performance ceiling
imposed by specialized perception tools in previous tool-integrated reasoning
approaches. To cultivate this capability, we develop a three-stage training
framework: cold-start training with synthetic data to establish basic drawing
abilities, reflective rejection sampling to enhance self-reflection behaviors,
and reinforcement learning to directly optimize for target rewards. Extensive
experiments demonstrate that our model, named VILASR, consistently outperforms
existing methods across diverse spatial reasoning benchmarks, involving maze
navigation, static spatial reasoning, video-based reasoning, and
multi-view-based reasoning tasks, with an average improvement of 18.4%.
```
### 🌟 论文解读 | 用交织思维与视觉绘图增强视觉语言模型的空间推理能力

### 📌 背景痛点/本文动机
随着大语言模型（LLMs）在文本推理方面取得显著进展，增强大视觉语言模型（LVLMs）的多模态推理能力受到越来越多关注。然而，现有方法在处理多模态推理时，主要采用以文本为中心的直接方式，推理和答案推导都纯通过文本进行，仅输入是多模态的。这使得这些方法在空间推理任务中面临根本局限，因为空间推理任务需要精确的几何理解和连续的空间跟踪能力，而人类是通过心理可视化和操作来实现这些能力的。为解决这些局限，本文提出新范式来让LVLMs在视觉空间中通过基本绘图操作进行推理。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出“绘图空间推理”新范式
让大视觉语言模型能够在视觉空间中通过基本绘图操作来推理。为模型配备包括标注边界框、绘制辅助线等基本绘图操作，使模型能通过直接视觉操作表达和分析空间关系，同时避免了之前工具集成推理方法中专业感知工具带来的性能上限问题。
💡 创新点2：三阶段训练框架
开发了三阶段训练框架来培养模型能力：首先利用合成数据进行冷启动训练以建立基本绘图能力；然后通过反射拒绝采样增强自我反思行为；最后用强化学习直接优化目标奖励。

### 📈 实验结果
在不同的空间推理基准测试中，名为VILASR的模型持续超越现有方法。这些基准测试涵盖迷宫导航、静态空间推理、基于视频的推理和基于多视图的推理任务，平均提升幅度达到18.4%。

### 💬 可借鉴之处
在处理多模态特别是空间推理任务时，可考虑引入类似的“视觉操作”范式，突破纯文本推理的局限；三阶段训练框架的设计思路，从基础能力建立到行为增强再到奖励优化，为培养模型特定复杂能力提供了分阶段推进的参考模式；针对任务瓶颈（如空间推理对几何和跟踪能力的需求），思考通过赋予模型更贴合人类认知方式（如心理可视化对应视觉绘图操作）的手段来突破性能上限，这种从人类认知借鉴解决模型局限的思路值得在其他任务场景中尝试。
```

## dyfo--a-training-free-dynamic-focus-visual-search-for-enhancing-lmms-in-fine-grained-visual-understanding
### Abstract
Humans can effortlessly locate desired objects in cluttered environments,
relying on a cognitive mechanism known as visual search to efficiently filter
out irrelevant information and focus on task-related regions. Inspired by this
process, we propose Dyfo (Dynamic Focus), a training-free dynamic focusing
visual search method that enhances fine-grained visual understanding in large
multimodal models (LMMs). Unlike existing approaches which require additional
modules or data collection, Dyfo leverages a bidirectional interaction between
LMMs and visual experts, using a Monte Carlo Tree Search (MCTS) algorithm to
simulate human-like focus adjustments. This enables LMMs to focus on key visual
regions while filtering out irrelevant content, without introducing additional
training caused by vocabulary expansion or the integration of specialized
localization modules. Experimental results demonstrate that Dyfo significantly
improves fine-grained visual understanding and reduces hallucination issues in
LMMs, achieving superior performance across both fixed and dynamic resolution
models. The code is available at https://github.com/PKU-ICST-MIPL/DyFo_CVPR2025
```
### 🌟 论文解读 | DyFo：无需训练，助力大模型实现动态聚焦的细粒度视觉理解

### 📌 背景痛点/本文动机
人类在杂乱环境中能轻松定位目标物体，依靠的是“视觉搜索”这一认知机制，高效过滤无关信息并聚焦任务相关区域。但当前大的多模态模型（LMMs）在细粒度视觉理解上存在不足，现有提升方法往往需要额外模块或数据收集，还可能因词汇扩展、整合专门定位模块带来额外训练成本，限制了模型在复杂视觉场景下精准聚焦关键区域与减少幻觉问题的能力。受人类视觉搜索机制启发，本文希望提出一种无需训练的方法来增强LMMs的细粒度视觉理解。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出DyFo（Dynamic Focus）方法  
DyFo是一种无需训练的动态聚焦视觉搜索方法，旨在增强大的多模态模型（LMMs）的细粒度视觉理解。它区别于需要额外模块或数据收集的现有方法，以更轻量化、无训练成本的方式来优化LMMs性能。  

💡 创新点2：双向交互与MCTS模拟人类聚焦  
DyFo利用LMMs和视觉专家之间的双向交互，借助蒙特卡洛树搜索（MCTS）算法模拟类人的焦点调整过程。这一过程让LMMs在过滤无关内容的同时，聚焦关键视觉区域，且不会因词汇扩展或整合专门定位模块而引入额外训练负担，在模型运行逻辑层面实现了对人类视觉搜索机制的模拟与借鉴。  

### 📈 实验结果
实验结果表明，DyFo在提升LMMs细粒度视觉理解与减少幻觉问题上效果显著，在固定分辨率和动态分辨率的模型中都实现了更优性能，验证了该方法在不同模型架构与视觉场景下的有效性与普适性。  

### 💬 可借鉴之处
1. 无训练范式的探索：DyFo采用无需训练的方式优化模型能力，为后续在不增加训练成本（如数据、算力、时间）的情况下提升多模态模型性能提供了新思路，可启发研究者关注“无训练”“即插即用”类方法的设计。  
2. 类人认知机制借鉴：从人类视觉搜索的认知机制出发设计算法，为多模态模型结合认知科学理论提供了优秀范例，后续可探索更多人类认知过程（如记忆、推理等）在AI模型优化中的应用。  
3. 双向交互与MCTS结合：其利用双向交互与MCTS模拟焦点调整的技术路线，为模型在复杂视觉信息中高效聚焦关键区域提供了可复用的技术参考，在需要视觉定位、信息过滤的多模态任务中都有潜在借鉴价值。  
4. 开源优势：代码开源（https://github.com/PKU-ICST-MIPL/DyFo_CVPR2025）方便研究者复现与二次开发，利于该方向技术生态的构建与发展。  
```

## v*--guided-visual-search-as-a-core-mechanism-in-multimodal-llms
### Abstract
When we look around and perform complex tasks, how we see and selectively
process what we see is crucial. However, the lack of this visual search
mechanism in current multimodal LLMs (MLLMs) hinders their ability to focus on
important visual details, especially when handling high-resolution and visually
crowded images. To address this, we introduce V*, an LLM-guided visual search
mechanism that employs the world knowledge in LLMs for efficient visual
querying. When combined with an MLLM, this mechanism enhances collaborative
reasoning, contextual understanding, and precise targeting of specific visual
elements. This integration results in a new MLLM meta-architecture, named Show,
sEArch, and TelL (SEAL). We further create V*Bench, a benchmark specifically
designed to evaluate MLLMs in their ability to process high-resolution images
and focus on visual details. Our study highlights the necessity of
incorporating visual search capabilities into multimodal systems. The code is
available https://github.com/penghao-wu/vstar.
```
### 🌟 论文解读 | V*：为多模态大模型注入视觉搜索“灵魂”，突破细节处理瓶颈

### 📌 背景痛点/本文动机
在人类执行复杂任务时，“看什么、怎么看”的视觉搜索能力至关重要，它能帮助我们在纷繁的视觉信息中聚焦关键细节。然而，当前的多模态大语言模型（MLLMs）却缺少这样的视觉搜索机制，面对高分辨率、视觉元素密集的图像时，很难精准捕捉重要视觉细节，这极大限制了它们在复杂视觉场景下的表现。为填补这一技术缺口，论文提出为MLLMs引入视觉搜索能力的全新思路。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出L LM引导的视觉搜索机制V*  
V* 借助大语言模型（LLM）中存储的世界知识，让多模态模型能更高效地发起“视觉查询”。不再是无差别处理图像内容，而是像人类主动搜索关键信息一样，用LLM的认知来指导视觉系统聚焦、筛选，让模型对视觉信息的处理更有“目的性”。  

💡 创新点2：构建SEAL元架构（Show, sEArch, and TelL）  
将V* 与MLLM结合后，形成了SEAL这一全新多模态大模型架构。它让多模态协作推理、上下文理解以及对特定视觉元素的精准定位都得到增强——“Show”呈现视觉内容，“sEArch”用V* 定向搜索关键细节，“TelL”再用语言完成输出，三步协作让多模态能力更智能。  

💡 创新点3：打造V*Bench专属基准测试集  
为了衡量MLLMs在高分辨率图像细节处理、视觉搜索方面的能力，论文团队专门构建了V*Bench。它为行业提供了一套针对性极强的评估标准，能清晰检验模型是否真正具备精准处理复杂视觉信息的能力。  

### 📈 实验结果
论文通过在V*Bench上的测试等实验，有力验证了：引入V* 视觉搜索机制后，多模态大模型在处理高分辨率、视觉拥挤图像时，对关键细节的聚焦和理解能力显著提升；SEAL架构也展现出更优的协作推理与上下文感知表现。这一系列实验充分说明视觉搜索能力对多模态系统的必要性，为后续技术迭代提供了有力佐证。  

### 💬 可借鉴之处
1. 机制创新角度：为多模态模型补上“视觉搜索”这一人类感知系统的关键能力，启发研究者关注“模态协作中更精细的控制逻辑”，未来可探索更多类似“让语言引导视觉聚焦”的跨模态协同范式。  
2. 架构设计角度：SEAL的“Show - sEArch - TelL”分层协作思路，为多模态大模型的模块化设计提供了新参考，不同模态不再是简单拼接，而是有分工、有引导的深度协同。  
3. 评估体系角度：V*Bench的构建凸显“针对性 benchmark 对技术方向的推动作用”，当新能力（如视觉搜索）出现时，定制化评估基准能更精准衡量进展，这为领域内打造细分场景评估工具提供了范例。  
4. 落地价值角度：让多模态模型更擅长处理复杂视觉细节，能直接赋能智能驾驶、智能安防、图像编辑等对视觉精准度要求高的下游场景，拓宽MLLMs的实用边界。  
```

## from-the-least-to-the-most--building-a-plug-and-play-visual-reasoner-via-data-synthesis
### Abstract
We explore multi-step reasoning in vision-language models (VLMs). The problem
is challenging, as reasoning data consisting of multiple steps of visual and
language processing are barely available. To overcome the challenge, we first
introduce a least-to-most visual reasoning paradigm, which interleaves steps of
decomposing a question into sub-questions and invoking external tools for
resolving sub-questions. Based on the paradigm, we further propose a novel data
synthesis approach that can automatically create questions and multi-step
reasoning paths for an image in a bottom-up manner. Our approach divides the
complex synthesis task into a few simple sub-tasks, and (almost entirely)
relies on open-sourced models to accomplish the sub-tasks. Therefore, the
entire synthesis process is reproducible and cost-efficient, and the
synthesized data is quality guaranteed. With the approach, we construct $50$k
visual reasoning examples. Then, we develop a visual reasoner through
supervised fine-tuning, which is capable of generally enhancing the reasoning
abilities of a wide range of existing VLMs in a plug-and-play fashion.
Extensive experiments indicate that the visual reasoner can consistently and
significantly improve four VLMs on four VQA benchmarks. Our code and dataset
are available at https://github.com/steven-ccq/VisualReasoner.
```
### 🌟 论文解读 | 从简到繁：用数据合成打造即插即用的视觉推理器

### 📌 背景痛点/本文动机
在视觉 - 语言模型（VLMs）中探索多步推理是极具挑战性的，原因在于包含多步视觉和语言处理的推理数据极为稀缺。现有的数据难以支撑模型进行复杂的多步视觉语言推理学习，这限制了VLMs在需要深度推理的视觉问答等任务中的表现，所以迫切需要一种方法来解决推理数据不足的问题，进而提升VLMs的多步推理能力。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出由浅入深的视觉推理范式
引入了least - to - most视觉推理范式，该范式将把一个问题分解为子问题以及调用外部工具解决子问题的步骤进行交错处理。通过这种方式，能够逐步处理复杂的视觉 - 语言推理任务，把大的推理问题拆解为可逐步解决的子问题序列，为后续的推理过程提供了清晰的逻辑框架。
💡 创新点2：新颖的数据合成方法
基于上述范式，提出了一种新颖的数据合成方法。该方法以自底向上的方式为图像自动生成问题和多步推理路径。它将复杂的合成任务分解为几个简单的子任务，并且（几乎完全）依赖开源模型来完成这些子任务。这使得整个合成过程具有可重复性且成本效益高，同时保证了合成数据的质量。利用该方法构建了5万个视觉推理示例，为模型训练提供了丰富的数据支撑。
💡 创新点3：即插即用的视觉推理器开发
通过有监督微调开发了一个视觉推理器，该推理器能够以即插即用的方式普遍增强大量现有VLMs的推理能力。这种方式不需要对现有VLMs进行大规模的结构改造，只需接入该推理器就能提升推理性能，大大提高了方法的实用性和通用性。

### 📈 实验结果
大量实验表明，该视觉推理器能够在四个VQA基准测试中持续且显著地提升四个VLMs的性能。这充分证明了所提出的方法在提升VLMs多步推理能力方面的有效性，无论是数据合成方法还是基于此训练的视觉推理器，都在实际的基准测试中展现出了优异的性能表现。

### 💬 可借鉴之处
1. 推理范式的设计思路：将复杂任务拆解为子任务并交错处理的范式，为解决其他复杂的多模态推理任务提供了思路，可借鉴这种任务分解与步骤交错的思想来处理不同领域的复杂问题。
2. 数据合成的方法：把复杂合成任务分解为简单子任务并利用开源模型完成的策略，在数据稀缺的领域中，为获取高质量训练数据提供了可参考的范例，尤其是在多模态领域，可学习这种低成本、可复现的数据集构建方式。
3. 即插即用的模型增强方式：开发即插即用的模块来增强现有模型性能的做法，对于提升已有模型在特定任务上的能力具有很好的借鉴意义，避免了对现有成熟模型进行大规模重构，节省了开发成本和时间。
```

## chain-of-focus--adaptive-visual-search-and-zooming-for-multimodal-reasoning-via-rl
### Abstract
Vision language models (VLMs) have achieved impressive performance across a
variety of computer vision tasks. However, the multimodal reasoning capability
has not been fully explored in existing models. In this paper, we propose a
Chain-of-Focus (CoF) method that allows VLMs to perform adaptive focusing and
zooming in on key image regions based on obtained visual cues and the given
questions, achieving efficient multimodal reasoning. To enable this CoF
capability, we present a two-stage training pipeline, including supervised
fine-tuning (SFT) and reinforcement learning (RL). In the SFT stage, we
construct the MM-CoF dataset, comprising 3K samples derived from a visual agent
designed to adaptively identify key regions to solve visual tasks with
different image resolutions and questions. We use MM-CoF to fine-tune the
Qwen2.5-VL model for cold start. In the RL stage, we leverage the outcome
accuracies and formats as rewards to update the Qwen2.5-VL model, enabling
further refining the search and reasoning strategy of models without human
priors. Our model achieves significant improvements on multiple benchmarks. On
the V* benchmark that requires strong visual reasoning capability, our model
outperforms existing VLMs by 5% among 8 image resolutions ranging from 224 to
4K, demonstrating the effectiveness of the proposed CoF method and facilitating
the more efficient deployment of VLMs in practical applications.
```
### 🌟 论文解读 | Chain-of-Focus：用强化学习实现多模态推理的自适应视觉搜索与缩放

### 📌 背景痛点/本文动机
视觉语言模型（VLMs）在众多计算机视觉任务中取得了令人瞩目的成绩，但现有模型的多模态推理能力尚未得到充分挖掘。在处理不同图像分辨率和问题时，如何让VLMs自适应地聚焦和放大关键图像区域以实现高效多模态推理，是当前面临的挑战。因此，本文提出Chain-of-Focus（CoF）方法来解决这一问题，提升VLMs在多模态推理任务中的表现。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出Chain-of-Focus（CoF）方法  
该方法让视觉语言模型能够基于获取的视觉线索和给定问题，自适应地聚焦并放大关键图像区域，以此实现高效的多模态推理，为VLMs在处理复杂视觉任务时提供了更智能的区域关注策略。  

💡 创新点2：设计两阶段训练 pipeline  
第一阶段是有监督微调（SFT）：构建了MM - CoF数据集，该数据集包含3K个样本，这些样本来自一个视觉智能体，该智能体可自适应识别关键区域以解决不同图像分辨率和问题下的视觉任务。利用MM - CoF数据集对Qwen2.5 - VL模型进行冷启动微调，为模型打下基础。  
第二阶段是强化学习（RL）：将结果的准确性和格式作为奖励来更新Qwen2.5 - VL模型，使模型在没有人类先验知识的情况下，进一步优化搜索和推理策略，让模型能自主地提升多模态推理能力。  

### 📈 实验结果
模型在多个基准测试中取得了显著提升。在对视觉推理能力要求较高的V*基准测试中，在从224到4K的8种图像分辨率下，该模型比现有VLMs表现好5%，充分证明了所提出的CoF方法的有效性，也为VLMs在实际应用中的更高效部署提供了助力。  

### 💬 可借鉴之处
1. 多模态任务处理思路：CoF方法为处理多模态推理任务中如何聚焦关键区域提供了创新思路，其他研究者可借鉴这种让模型自适应关注关键信息的方式，拓展到更多多模态任务场景。  
2. 两阶段训练模式：先通过有监督微调利用构建的特定数据集让模型冷启动，再用强化学习依据任务结果反馈优化模型，这种分阶段训练且结合不同训练范式优势的方式，可为模型训练流程设计提供参考。  
3. 数据集构建理念：MM - CoF数据集从自适应识别关键区域以解决视觉任务的角度构建，这种针对特定能力培养构建数据集的思路，对后续打造针对性训练数据有启发意义。
```

## vlm-r$^3$--region-recognition--reasoning--and-refinement-for-enhanced-multimodal-chain-of-thought
### Abstract
Recently, reasoning-based MLLMs have achieved a degree of success in
generating long-form textual reasoning chains. However, they still struggle
with complex tasks that necessitate dynamic and iterative focusing on and
revisiting of visual regions to achieve precise grounding of textual reasoning
in visual evidence. We introduce \textbf{VLM-R$^3$} (\textbf{V}isual
\textbf{L}anguage \textbf{M}odel with \textbf{R}egion \textbf{R}ecognition and
\textbf{R}easoning), a framework that equips an MLLM with the ability to (i)
decide \emph{when} additional visual evidence is needed, (ii) determine
\emph{where} to ground within the image, and (iii) seamlessly weave the
relevant sub-image content back into an interleaved chain-of-thought. The core
of our method is \textbf{Region-Conditioned Reinforcement Policy Optimization
(R-GRPO)}, a training paradigm that rewards the model for selecting informative
regions, formulating appropriate transformations (e.g.\ crop, zoom), and
integrating the resulting visual context into subsequent reasoning steps. To
bootstrap this policy, we compile a modest but carefully curated Visuo-Lingual
Interleaved Rationale (VLIR) corpus that provides step-level supervision on
region selection and textual justification. Extensive experiments on MathVista,
ScienceQA, and other benchmarks show that VLM-R$^3$ sets a new state of the art
in zero-shot and few-shot settings, with the largest gains appearing on
questions demanding subtle spatial reasoning or fine-grained visual cue
extraction.
```
### 🌟 论文解读 | VLM-R³：让多模态思维链更智能的区域识别、推理与优化框架

### 📌 背景痛点/本文动机
近年来，基于推理的多模态大语言模型（MLLMs）在生成长篇文本推理链方面取得了一定成果。但面对复杂任务时，它们仍难以动态且迭代地聚焦、回顾视觉区域，来实现文本推理在视觉证据上的精准锚定（grounding）。比如需要精细空间推理或提取细粒度视觉线索的任务，现有模型表现不佳。因此，如何让MLLM更智能地利用视觉区域信息辅助推理，成为亟待解决的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出VLM-R³框架  
VLM-R³（Visual Language Model with Region Recognition, Reasoning, and Refinement）为多模态大语言模型赋予三项关键能力：（i）判断“何时”需要额外视觉证据；（ii）确定在图像中“哪里”进行锚定；（iii）将相关子图像内容无缝编织到交错的思维链中。通过这三点，模型能更灵活地利用视觉区域信息支撑推理。  

💡 创新点2：Region-Conditioned Reinforcement Policy Optimization（R-GRPO）训练范式  
这是方法的核心，通过奖励机制引导模型：选择信息丰富的区域、制定合适的变换（如裁剪、缩放）、并将得到的视觉上下文整合到后续推理步骤中。这种强化学习式的训练，让模型学会主动且合理地利用视觉区域辅助推理。  

💡 创新点3：构建Visuo-Lingual Interleaved Rationale（VLIR）语料库  
为了引导R-GRPO策略的训练，团队构建了VLIR语料库。它虽规模不大，但经过精心策划，能在“区域选择”和“文本论证”层面提供步骤级监督，为模型学习如何结合视觉区域推理打下数据基础。  

### 📈 实验结果
在MathVista、ScienceQA等基准测试中，VLM-R³在零样本（zero-shot）和少样本（few-shot）设置下都达到了全新的SOTA（state-of-the-art）水平。尤其在需要微妙空间推理或细粒度视觉线索提取的问题上，模型性能提升最为显著，证明了其在复杂视觉-文本推理任务中的有效性。  

### 💬 可借鉴之处
1. 多模态推理的“主动视觉利用”思路：VLM-R³强调模型主动判断何时、何处获取视觉信息，为多模态大模型设计推理逻辑提供了“主动交互式”的新视角。  
2. 强化学习与多模态结合：R-GRPO展示了如何用强化学习范式引导模型学习视觉区域选择与推理整合，为多模态任务的策略学习提供了参考。  
3. 小而精的语料库构建：VLIR说明在特定任务上，精心设计的小规模语料也能有效引导模型学习，为数据资源有限时的多模态模型训练提供了思路。  
```

