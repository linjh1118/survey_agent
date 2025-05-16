# Paper List of Terms(VLM+Games)
- [25/05] **DSADF: Thinking Fast and Slow for Decision Making**  
[[Paper](http://arxiv.org/pdf/2505.08189v1)] [[Code/Page]()] [[TLDR/Notes](#dsadf--thinking-fast-and-slow-for-decision-making)]

- [25/05] **Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.03792v1)] [[Code/Page](https://github.com/langfengQ/CoSo.)] [[TLDR/Notes](#towards-efficient-online-tuning-of-vlm-agents-via-counterfactual-soft-reinforcement-learning)]

- [25/04] **mrCAD: Multimodal Refinement of Computer-aided Designs**  
[[Paper](http://arxiv.org/pdf/2504.20294v1)] [[Code/Page]()] [[TLDR/Notes](#mrcad--multimodal-refinement-of-computer-aided-designs)]

- [25/04] **Metropolis-Hastings Captioning Game: Knowledge Fusion of Vision Language Models via Decentralized Bayesian Inference**  
[[Paper](http://arxiv.org/pdf/2504.09620v1)] [[Code/Page]()] [[TLDR/Notes](#metropolis-hastings-captioning-game--knowledge-fusion-of-vision-language-models-via-decentralized-bayesian-inference)]

- [25/04] **BlenderGym: Benchmarking Foundational Model Systems for Graphics Editing**  
[[Paper](http://arxiv.org/pdf/2504.01786v1)] [[Code/Page]()] [[TLDR/Notes](#blendergym--benchmarking-foundational-model-systems-for-graphics-editing)]

- [25/03] **Cultivating Game Sense for Yourself: Making VLMs Gaming Experts**  
[[Paper](http://arxiv.org/pdf/2503.21263v1)] [[Code/Page]()] [[TLDR/Notes](#cultivating-game-sense-for-yourself--making-vlms-gaming-experts)]

- [25/03] **MetaSpatial: Reinforcing 3D Spatial Reasoning in VLMs for the Metaverse**  
[[Paper](http://arxiv.org/pdf/2503.18470v1)] [[Code/Page](https://github.com/PzySeere/MetaSpatial.)] [[TLDR/Notes](#metaspatial--reinforcing-3d-spatial-reasoning-in-vlms-for-the-metaverse)]

- [25/03] **GTR: Guided Thought Reinforcement Prevents Thought Collapse in RL-based VLM Agent Training**  
[[Paper](http://arxiv.org/pdf/2503.08525v1)] [[Code/Page]()] [[TLDR/Notes](#gtr--guided-thought-reinforcement-prevents-thought-collapse-in-rl-based-vlm-agent-training)]

- [25/03] **GFlowVLM: Enhancing Multi-step Reasoning in Vision-Language Models with Generative Flow Networks**  
[[Paper](http://arxiv.org/pdf/2503.06514v2)] [[Code/Page]()] [[TLDR/Notes](#gflowvlm--enhancing-multi-step-reasoning-in-vision-language-models-with-generative-flow-networks)]

- [25/03] **AVA: Attentive VLM Agent for Mastering StarCraft II**  
[[Paper](http://arxiv.org/pdf/2503.05383v4)] [[Code/Page](https://github.com/camel-ai/VLM-Play-StarCraft2.)] [[TLDR/Notes](#ava--attentive-vlm-agent-for-mastering-starcraft-ii)]



# TLDR/Notes
## dsadf--thinking-fast-and-slow-for-decision-making
### Abstract
Although Reinforcement Learning (RL) agents are effective in well-defined
environments, they often struggle to generalize their learned policies to
dynamic settings due to their reliance on trial-and-error interactions. Recent
work has explored applying Large Language Models (LLMs) or Vision Language
Models (VLMs) to boost the generalization of RL agents through policy
optimization guidance or prior knowledge. However, these approaches often lack
seamless coordination between the RL agent and the foundation model, leading to
unreasonable decision-making in unfamiliar environments and efficiency
bottlenecks. Making full use of the inferential capabilities of foundation
models and the rapid response capabilities of RL agents and enhancing the
interaction between the two to form a dual system is still a lingering
scientific question. To address this problem, we draw inspiration from
Kahneman's theory of fast thinking (System 1) and slow thinking (System 2),
demonstrating that balancing intuition and deep reasoning can achieve nimble
decision-making in a complex world. In this study, we propose a Dual-System
Adaptive Decision Framework (DSADF), integrating two complementary modules:
System 1, comprising an RL agent and a memory space for fast and intuitive
decision making, and System 2, driven by a VLM for deep and analytical
reasoning. DSADF facilitates efficient and adaptive decision-making by
combining the strengths of both systems. The empirical study in the video game
environment: Crafter and Housekeep demonstrates the effectiveness of our
proposed method, showing significant improvements in decision abilities for
both unseen and known tasks.
### 🌟 论文解读 | 双系统自适应决策框架：快思与慢思的决策艺术

### 📌 背景痛点/本文动机
尽管强化学习（RL）代理在明确定义的环境中表现出色，但在动态设置中，由于依赖试错交互，它们往往难以泛化其学到的策略。近期研究尝试应用大型语言模型（LLMs）或视觉语言模型（VLMs）来提升RL代理的泛化能力，但这些方法往往缺乏RL代理与基础模型之间的无缝协调，导致在不熟悉的环境中做出不合理的决策和效率瓶颈。本文旨在解决这一问题，提出了双系统自适应决策框架（DSADF），以实现更高效的决策和泛化。

### 🚀 核心方法
💡 创新点1
本文受到Kahneman的快思（系统1）和慢思（系统2）理论的启发，提出了一种双系统自适应决策框架（DSADF）。该框架整合了两个互补模块：系统1由RL代理和内存空间组成，负责快速直观的决策；系统2由VLM驱动，负责深入分析性推理。

💡 创新点2
DSADF通过结合系统1和系统2的优势，实现了高效自适应的决策。系统2利用基础模型的强大推理能力，从指令提示中提取线索，将长期任务分解为可管理的单步任务，使RL代理能够专注于解决每个单步任务，显著提高其学习和执行效率。

### 📈 实验结果
本文在两个视频游戏环境Crafter和Housekeep中进行了实证研究，这些环境具有长期任务和RL代理未见过的任务。实验结果表明，系统1和系统2协同工作，表现出色，无论是在效率还是泛化能力上都有显著提升。

### 💬 可借鉴之处
本文提出的DSADF框架为RL代理在动态环境中的决策提供了新的视角和方法，特别是如何结合快速反应能力和深入推理能力，对于提高RL代理的泛化能力和决策效率具有借鉴意义。此外，本文的实证研究为双系统框架在实际应用中的有效性提供了证据。

## towards-efficient-online-tuning-of-vlm-agents-via-counterfactual-soft-reinforcement-learning
### Abstract
Online fine-tuning vision-language model (VLM) agents with reinforcement
learning (RL) has shown promise for equipping agents with multi-step,
goal-oriented capabilities in dynamic environments. However, their open-ended
textual action space and non-end-to-end nature of action generation present
significant challenges to effective online exploration in RL, e.g., explosion
of the exploration space. We propose a novel online fine-tuning method,
Counterfactual Soft Reinforcement Learning (CoSo), better suited to the textual
output space of VLM agents. Compared to prior methods that assign uniform
uncertainty to all tokens, CoSo leverages counterfactual reasoning to
dynamically assess the causal influence of individual tokens on post-processed
actions. By prioritizing the exploration of action-critical tokens while
reducing the impact of semantically redundant or low-impact tokens, CoSo
enables a more targeted and efficient online rollout process. We provide
theoretical analysis proving CoSo's convergence and policy improvement
guarantees, and extensive empirical evaluations supporting CoSo's
effectiveness. Our results across a diverse set of agent tasks, including
Android device control, card gaming, and embodied AI, highlight its remarkable
ability to enhance exploration efficiency and deliver consistent performance
gains. The code is available at https://github.com/langfengQ/CoSo.
### 🌟 论文解读 | “迈向高效在线微调：VLM智能体在Counterfactual Soft RL框架下的探索优化”

### 📌 背景痛点/本文动机
随着大型视觉语言模型（VLM）在决策制定智能体中的应用日益广泛，如何将这些模型通过在线微调适应动态环境，成为当前研究的热点。然而，VLM智能体在采用强化学习（RL）进行在线微调时，面临着文本动作空间的开放性和动作生成非端到端性的挑战，导致探索空间爆炸和探索效率低下。本文旨在解决这一问题，提出了一种新的在线微调方法，以提升VLM智能体的探索效率和性能。

### 🚀 核心方法
💡 创新点1：本文提出了Counterfactual Soft Reinforcement Learning（CoSo）方法，该方法通过利用反事实推理动态评估单个令牌对后处理动作的因果影响，从而在动作关键的令牌上优先进行探索，减少语义冗余或低影响令牌的影响。

💡 创新点2：CoSo方法在软RL基础上引入了因果加权的熵正则化优化，这不仅减少了冗余的探索空间，还使得VLM智能体的文本输出探索与最终解析动作的探索更加一致。

### 📈 实验结果
本文在多个智能体任务上进行了广泛的实证评估，包括Android设备控制、卡牌游戏和具身AI任务。结果显示，采用CoSo方法的智能体在所有任务上都展现了显著的性能提升，平均性能增益分别为Android设备控制12.3%，卡牌游戏9.3%，具身AI任务16.7%。

### 💬 可借鉴之处
本文的方法为VLM智能体的在线微调提供了一种新的思路，特别是在处理开放性文本动作空间时，如何通过反事实推理和熵正则化优化探索过程，对于提升智能体在动态环境中的适应性和效率具有重要借鉴意义。此外，论文提供的理论分析和实验验证，也为相关领域的研究者提供了宝贵的参考资源。

## mrcad--multimodal-refinement-of-computer-aided-designs
### Abstract
A key feature of human collaboration is the ability to iteratively refine the
concepts we have communicated. In contrast, while generative AI excels at the
\textit{generation} of content, it often struggles to make specific
language-guided \textit{modifications} of its prior outputs. To bridge the gap
between how humans and machines perform edits, we present mrCAD, a dataset of
multimodal instructions in a communication game. In each game, players created
computer aided designs (CADs) and refined them over several rounds to match
specific target designs. Only one player, the Designer, could see the target,
and they must instruct the other player, the Maker, using text, drawing, or a
combination of modalities. mrCAD consists of 6,082 communication games, 15,163
instruction-execution rounds, played between 1,092 pairs of human players. We
analyze the dataset and find that generation and refinement instructions differ
in their composition of drawing and text. Using the mrCAD task as a benchmark,
we find that state-of-the-art VLMs are better at following generation
instructions than refinement instructions. These results lay a foundation for
analyzing and modeling a multimodal language of refinement that is not
represented in previous datasets.
### 🌟 论文解读 | "mrCAD：迈向多模态协同设计新篇章"

### 📌 背景痛点/本文动机
在人工智能领域，生成式AI在内容创造方面表现出色，但在根据用户指示进行具体修改时却往往力不从心。为了弥补人类与机器在编辑方式上的差距，本文提出了mrCAD数据集，这是一个在计算机辅助设计（CAD）环境下的多模态指令交流游戏。通过分析人类玩家之间的交流，该研究旨在探索和建模一种在先前数据集中未得到体现的多模态 refinement 语言。

### 🚀 核心方法
💡 创新点1
本文设计了一个独特的mrCAD任务，其中玩家通过多轮交流，使用文本、绘图或两者的组合来指导对方创建和修改CAD设计。这个设置不仅产生了自然的多模态交互，还涉及到上下文依赖，即 refinement 指令需要在前一轮创建的内容的背景下进行解释。

💡 创新点2
mrCAD数据集的构建采用了众包方法，收集了6082个交流游戏，共15163个指令执行轮次。数据集中的CAD设计来源于SketchGraphs数据集，这些设计是通过简单的曲线（如直线、圆和弧）组合而成的丰富语义对象，需要玩家在上下文中进行解析。

### 📈 实验结果
通过使用mrCAD任务作为基准，研究发现，现有的最先进的视觉语言模型（VLMs）在遵循生成指令方面表现较好，但在遵循refinement指令方面存在明显差距。这表明，模型在处理需要上下文理解和多模态交流的任务时，仍然面临挑战。

### 💬 可借鉴之处
mrCAD数据集和基准为理解和建模人类在多模态 refinement 交流中的行为提供了一个宝贵的资源。它不仅揭示了人类在生成和refinement指令中使用多模态语言的不同之处，还为开发能够更好地理解和执行复杂修改指令的人工智能模型提供了新的研究方向。此外，mrCAD的众包数据收集方法和评估环境也为未来相关研究提供了可借鉴的范例。

## metropolis-hastings-captioning-game--knowledge-fusion-of-vision-language-models-via-decentralized-bayesian-inference
### Abstract
We propose the Metropolis-Hastings Captioning Game (MHCG), a method to fuse
knowledge of multiple vision-language models (VLMs) by learning from each
other. Although existing methods that combine multiple models suffer from
inference costs and architectural constraints, MHCG avoids these problems by
performing decentralized Bayesian inference through a process resembling a
language game. The knowledge fusion process establishes communication between
two VLM agents alternately captioning images and learning from each other. We
conduct two image-captioning experiments with two VLMs, each pre-trained on a
different dataset. The first experiment demonstrates that MHCG achieves
consistent improvement in reference-free evaluation metrics. The second
experiment investigates how MHCG contributes to sharing VLMs' category-level
vocabulary by observing the occurrence of the vocabulary in the generated
captions.
### 🌟 论文解读 | “MHCG：图像字幕新策略，视觉语言模型知识融合的艺术”

### 📌 背景痛点/本文动机
在当前的图像字幕生成领域，虽然视觉语言模型（VLMs）已经取得了显著的进步，但单个模型往往受限于其训练数据和架构，难以全面捕捉图像的丰富信息。传统的多模型融合方法往往面临推理成本高和架构限制的问题。因此，本文提出了Metropolis-Hastings Captioning Game（MHCG）方法，旨在通过学习相互之间的知识来融合多个视觉语言模型的优势，从而提高图像字幕生成的质量。

### 🚀 核心方法
💡 创新点1
MHCG采用了一种类似语言游戏的方式，通过两个VLM代理交替地为图像生成字幕，并在过程中相互学习。这种方法实现了去中心化的贝叶斯推理，有效避免了传统多模型融合方法中的推理成本和架构限制。

💡 创新点2
知识融合过程不仅提高了图像字幕的生成质量，还促进了VLM代理之间在类别级别词汇表的共享。通过观察生成字幕中词汇的出现情况，实验验证了MHCG在促进模型间知识共享方面的有效性。

### 📈 实验结果
本文通过两个图像字幕生成实验来验证MHCG的有效性。第一个实验表明，MHCG在无需参考的评价指标上实现了持续的改进。第二个实验则通过观察生成字幕中词汇的出现，展示了MHCG如何帮助VLM代理共享类别级别的词汇表。

### 💬 可借鉴之处
MHCG方法为图像字幕生成领域提供了一种新颖的知识融合策略，不仅提高了生成字幕的质量，还通过模型间的交互学习促进了知识共享。这种方法对于开发更高效、更智能的多模型融合系统具有启示意义，值得相关领域的研究者和开发者关注和借鉴。

## blendergym--benchmarking-foundational-model-systems-for-graphics-editing
### Abstract
3D graphics editing is crucial in applications like movie production and game
design, yet it remains a time-consuming process that demands highly specialized
domain expertise. Automating this process is challenging because graphical
editing requires performing a variety of tasks, each requiring distinct skill
sets. Recently, vision-language models (VLMs) have emerged as a powerful
framework for automating the editing process, but their development and
evaluation are bottlenecked by the lack of a comprehensive benchmark that
requires human-level perception and presents real-world editing complexity. In
this work, we present BlenderGym, the first comprehensive VLM system benchmark
for 3D graphics editing. BlenderGym evaluates VLM systems through code-based 3D
reconstruction tasks. We evaluate closed- and open-source VLM systems and
observe that even the state-of-the-art VLM system struggles with tasks
relatively easy for human Blender users. Enabled by BlenderGym, we study how
inference scaling techniques impact VLM's performance on graphics editing
tasks. Notably, our findings reveal that the verifier used to guide the scaling
of generation can itself be improved through inference scaling, complementing
recent insights on inference scaling of LLM generation in coding and math
tasks. We further show that inference compute is not uniformly effective and
can be optimized by strategically distributing it between generation and
verification.
### 🌟 论文解读 | "BlenderGym：推动视觉语言模型在3D图形编辑领域的突破"

### 📌 背景痛点/本文动机
3D图形编辑在电影制作和游戏设计等领域至关重要，但这一过程耗时且需要高度专业的领域知识。尽管近年来视觉语言模型（VLMs）在自动化编辑过程中显示出强大的潜力，但它们的发展和评估却受到缺乏一个全面评估标准的限制。现有的评估方法要么覆盖范围有限，要么缺乏可靠、经济的量化指标。为此，本文提出了BlenderGym，一个针对3D图形编辑的VLM系统全面评估基准。

### 🚀 核心方法
💡 创新点1
本文提出了BlenderGym，这是一个首个针对3D图形编辑的VLM系统评估基准。它通过代码基础的3D场景重建任务来评估VLM系统，涵盖了对象放置、光照调整、程序性材料编辑、混合形状操作和程序性几何编辑五大关键任务。

💡 创新点2
利用BlenderGym，本文研究了推理时间扩展技术如何影响VLM在图形编辑任务上的表现。研究发现，不仅VLM作为生成器时可以从推理时间扩展中受益，作为验证器引导生成的VLM同样可以从推理时间扩展中获得提升。此外，推理计算的效果并不是均匀的，通过战略性地在生成和验证之间分配计算资源，可以优化效果。

### 📈 实验结果
本文评估了闭源和开源的先进VLM系统在BlenderGym上的表现，并发现即使是先进的VLM系统，在面对对于人类Blender用户相对简单的任务时也显得力不从心。实验结果还揭示了，当计算资源增加时，将更多的资源分配给验证器可以带来更大的收益。

### 💬 可借鉴之处
BlenderGym为3D图形编辑领域提供了一个全面的评估框架，有助于推动视觉语言模型在该领域的发展。它不仅提供了一个固定的起始-目标场景对来量化编辑结果，还展示了如何通过推理时间扩展技术来优化VLM的性能。这些发现对于3D图形编辑的自动化以及视觉语言模型的应用都具有重要价值。

## cultivating-game-sense-for-yourself--making-vlms-gaming-experts
### Abstract
Developing agents capable of fluid gameplay in first/third-person games
without API access remains a critical challenge in Artificial General
Intelligence (AGI). Recent efforts leverage Vision Language Models (VLMs) as
direct controllers, frequently pausing the game to analyze screens and plan
action through language reasoning. However, this inefficient paradigm
fundamentally restricts agents to basic and non-fluent interactions: relying on
isolated VLM reasoning for each action makes it impossible to handle tasks
requiring high reactivity (e.g., FPS shooting) or dynamic adaptability (e.g.,
ACT combat). To handle this, we propose a paradigm shift in gameplay agent
design: instead of directly controlling gameplay, VLM develops specialized
execution modules tailored for tasks like shooting and combat. These modules
handle real-time game interactions, elevating VLM to a high-level developer.
Building upon this paradigm, we introduce GameSense, a gameplay agent framework
where VLM develops task-specific game sense modules by observing task execution
and leveraging vision tools and neural network training pipelines. These
modules encapsulate action-feedback logic, ranging from direct action rules to
neural network-based decisions. Experiments demonstrate that our framework is
the first to achieve fluent gameplay in diverse genres, including ACT, FPS, and
Flappy Bird, setting a new benchmark for game-playing agents.
### 🌟 论文解读 | 让VLM成为游戏高手：自主培养游戏感的智能体

### 📌 背景痛点/本文动机
在人工智能领域，开发能够在没有API访问权限的情况下流畅进行第一人称或第三人称游戏的游戏智能体，一直是人工通用智能（AGI）的一个关键挑战。现有的基于视觉语言模型（VLM）的方法虽然能够通过视觉理解游戏屏幕来进行交互，但其暂停-计划的范式限制了智能体进行高反应性或动态适应性的任务。本文针对这一痛点，提出了一个全新的游戏智能体设计范式。

### 🚀 核心方法
💡 创新点1
本文提出了一个范式转变：VLM不再直接控制游戏，而是开发专门针对任务（如射击和战斗）的执行模块。这些模块能够处理实时游戏交互，将VLM提升为高级开发者。

💡 创新点2
基于这一新范式，本文引入了GameSense框架，VLM通过观察任务执行并利用视觉工具和神经网络训练管道来开发任务特定的游戏感模块（GSM）。这些模块封装了动作-反馈逻辑，从直接的动作规则到基于神经网络的决策。

### 📈 实验结果
实验结果表明，GameSense框架是第一个在多种游戏类型（包括ACT、FPS和Flappy Bird）中实现流畅游戏玩的智能体，为游戏玩法的智能体设定了新的基准。

### 💬 可借鉴之处
本文不仅指出了现有VLM游戏智能体方法的局限性，还提出了一种新的解决方案，即通过VLM培养专门的游戏感模块来提升智能体的实时性能和适应能力。这一方法对于开发无需API访问即可在多样化游戏环境中表现优异的智能体具有重要的借鉴意义。

## metaspatial--reinforcing-3d-spatial-reasoning-in-vlms-for-the-metaverse
### Abstract
We present MetaSpatial, the first reinforcement learning (RL)-based framework
designed to enhance 3D spatial reasoning in vision-language models (VLMs),
enabling real-time 3D scene generation without the need for hard-coded
optimizations. MetaSpatial addresses two core challenges: (i) the lack of
internalized 3D spatial reasoning in VLMs, which limits their ability to
generate realistic layouts, and (ii) the inefficiency of traditional supervised
fine-tuning (SFT) for layout generation tasks, as perfect ground truth
annotations are unavailable. Our key innovation is a multi-turn RL-based
optimization mechanism that integrates physics-aware constraints and rendered
image evaluations, ensuring generated 3D layouts are coherent, physically
plausible, and aesthetically consistent. Methodologically, MetaSpatial
introduces an adaptive, iterative reasoning process, where the VLM refines
spatial arrangements over multiple turns by analyzing rendered outputs,
improving scene coherence progressively. Empirical evaluations demonstrate that
MetaSpatial significantly enhances the spatial consistency and formatting
stability of various scale models. Post-training, object placements are more
realistic, aligned, and functionally coherent, validating the effectiveness of
RL for 3D spatial reasoning in metaverse, AR/VR, digital twins, and game
development applications. Our code, data, and training pipeline are publicly
available at https://github.com/PzySeere/MetaSpatial.
### 🌟 论文解读 | "MetaSpatial：赋予视觉语言模型以3D空间推理能力，开启实时三维场景生成新篇章"

### 📌 背景痛点/本文动机
随着虚拟现实和增强现实技术的快速发展，三维场景生成变得越来越重要。然而，现有的视觉语言模型（VLMs）在生成真实布局方面存在两大挑战：一是缺乏内部化的3D空间推理能力，导致生成的场景布局不够真实；二是传统的监督微调（SFT）方法在布局生成任务上的效率低下，因为完美的地面真实标注是不可用的。本文旨在解决这些问题，提出了一种基于强化学习（RL）的框架MetaSpatial，以增强VLMs的3D空间推理能力，实现无需硬编码优化的实时3D场景生成。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
MetaSpatial引入了一种多轮次的强化学习优化机制，该机制整合了物理感知约束和渲染图像评估，确保生成的3D布局具有连贯性、物理可行性和审美一致性。

💡 创新点2
MetaSpatial采用了一种自适应的迭代推理过程，其中VLM通过分析渲染输出来逐步改进空间布局，从而提高场景的连贯性。

### 📈 实验结果
本文的实证评估表明，MetaSpatial显著提高了各种规模模型的空闻一致性和格式稳定性。经过训练后，物体的放置更加真实、对齐和功能上连贯，验证了RL在3D空间推理方面的有效性。

### 💬 可借鉴之处
本文提出的方法为3D场景生成提供了一种新的视角，即通过强化学习而非固定的标注来优化空间布局。这种方法不仅提高了场景生成的质量，还减少了后处理的负担，对于元宇宙、AR/VR、数字孪生和游戏开发等领域具有潜在的应用价值。此外，论文中提出的多轮次推理策略和三级的评估机制为类似任务提供了可借鉴的思路。

## gtr--guided-thought-reinforcement-prevents-thought-collapse-in-rl-based-vlm-agent-training
### Abstract
Reinforcement learning with verifiable outcome rewards (RLVR) has effectively
scaled up chain-of-thought (CoT) reasoning in large language models (LLMs).
Yet, its efficacy in training vision-language model (VLM) agents for
goal-directed action reasoning in visual environments is less established. This
work investigates this problem through extensive experiments on complex card
games, such as 24 points, and embodied tasks from ALFWorld. We find that when
rewards are based solely on action outcomes, RL fails to incentivize CoT
reasoning in VLMs, instead leading to a phenomenon we termed thought collapse,
characterized by a rapid loss of diversity in the agent's thoughts,
state-irrelevant and incomplete reasoning, and subsequent invalid actions,
resulting in negative rewards. To counteract thought collapse, we highlight the
necessity of process guidance and propose an automated corrector that evaluates
and refines the agent's reasoning at each RL step. This simple and scalable GTR
(Guided Thought Reinforcement) framework trains reasoning and action
simultaneously without the need for dense, per-step human labeling. Our
experiments demonstrate that GTR significantly enhances the performance and
generalization of the LLaVA-7b model across various visual environments,
achieving 3-5 times higher task success rates compared to SoTA models with
notably smaller model sizes.
### 🌟 论文解读 | "GTR：引导思维强化学习，防止视觉语言模型训练中的思维崩溃"

### 📌 背景痛点/本文动机
随着大型语言模型（LLM）和视觉语言模型（VLM）的快速发展，机器理解和处理文本与图像的能力显著增强。然而，如何训练VLM代理在动态视觉环境中根据感知信息推断正确动作序列，以完成特定目标，仍然是一个挑战。本文针对强化学习（RL）训练中VLM代理面临的“思维崩溃”问题进行了深入研究，提出了一个有效的解决方案。

### 🚀 核心方法
💡 创新点1
本文发现，当仅基于动作结果来设计奖励时，RL无法激励VLM中的链式思维（CoT）推理，反而会导致“思维崩溃”现象。这种现象表现为代理思维的多样性迅速丧失，推理与状态无关且不完整，进而导致无效动作和负面奖励。

💡 创新点2
为了对抗思维崩溃，本文强调了过程指导的必要性，并提出了一个简单可扩展的GTR（引导思维强化）框架。该框架通过自动评估和细化代理在每个RL步骤中的推理，同时优化代理的思维和动作。GTR框架不依赖于细致的人工标注或额外训练，提供了更丰富的过程监督，同时保持了RLVR的灵活性。

### 📈 实验结果
本文将GTR应用于训练LLaVA-7b模型，并在24点纸牌游戏和ALFWorld的具身任务中进行了实验。结果显示，GTR显著提高了LLaVA-7b模型在各种视觉环境下的性能和泛化能力，相比现有最先进方法，任务成功率提高了3-5倍，且模型尺寸更小。

### 💬 可借鉴之处
本文提出的GTR框架为训练VLM代理提供了一种新的思路，特别是对于需要复杂推理的动态视觉环境。GTR框架的设计理念和方法对于其他类似问题的解决具有借鉴意义，包括但不限于自动思维校正、格式奖励和重复惩罚、工具使用的准确性以及通过模仿学习方法减轻分布偏移等。

## gflowvlm--enhancing-multi-step-reasoning-in-vision-language-models-with-generative-flow-networks
### Abstract
Vision-Language Models (VLMs) have recently shown promising advancements in
sequential decision-making tasks through task-specific fine-tuning. However,
common fine-tuning methods, such as Supervised Fine-Tuning (SFT) and
Reinforcement Learning (RL) techniques like Proximal Policy Optimization (PPO),
present notable limitations: SFT assumes Independent and Identically
Distributed (IID) data, while PPO focuses on maximizing cumulative rewards.
These limitations often restrict solution diversity and hinder generalization
in multi-step reasoning tasks. To address these challenges, we introduce a
novel framework, GFlowVLM, a framework that fine-tune VLMs using Generative
Flow Networks (GFlowNets) to promote generation of diverse solutions for
complex reasoning tasks. GFlowVLM models the environment as a non-Markovian
decision process, allowing it to capture long-term dependencies essential for
real-world applications. It takes observations and task descriptions as inputs
to prompt chain-of-thought (CoT) reasoning which subsequently guides action
selection. We use task based rewards to fine-tune VLM with GFlowNets. This
approach enables VLMs to outperform prior fine-tuning methods, including SFT
and RL. Empirical results demonstrate the effectiveness of GFlowVLM on complex
tasks such as card games (NumberLine, BlackJack) and embodied planning tasks
(ALFWorld), showing enhanced training efficiency, solution diversity, and
stronger generalization capabilities across both in-distribution and
out-of-distribution scenarios.
### 🌟 论文解读 | GFlowVLM：利用生成流网络提升视觉语言模型的多步推理能力

### 📌 背景痛点/本文动机
视觉语言模型（VLMs）在顺序决策任务中通过特定任务的微调显示了有希望的进展。然而，常见的微调方法，如监督微调（SFT）和强化学习技术（如近端策略优化PPO），存在明显的局限性。SFT假设数据是独立同分布的，而PPO专注于最大化累积奖励。这些限制通常限制了解决方案的多样性，阻碍了多步推理任务中的泛化。为了解决这些挑战，本文提出了一个新颖的框架GFlowVLM，它使用生成流网络（GFlowNets）来微调VLMs，以促进复杂推理任务中多样化解决方案的生成。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
GFlowVLM框架将环境建模为非马尔可夫决策过程，这使其能够捕捉到对现实世界应用至关重要的长期依赖关系。它将观察和任务描述作为输入，以激发链式思维（CoT）推理，进而指导动作选择。

💡 创新点2
GFlowVLM使用基于任务的奖励来微调VLM与GFlowNets。这种方法使VLMs在多步推理任务中超越之前的微调方法，包括SFT和RL。GFlowVLM通过隐式地将推理表示为树结构，增强了多样化复杂推理序列的学习效率。

### 📈 实验结果
实证结果显示，GFlowVLM在诸如纸牌游戏（NumberLine、BlackJack）和具身规划任务（ALFWorld）等复杂任务中表现出色，显示出增强的训练效率、解决方案多样性和更强的泛化能力，适用于分布内和分布外场景。

### 💬 可借鉴之处
本文提出的GFlowVLM框架为处理多模态、顺序推理任务提供了一种新的视角，特别是对于那些需要长期依赖关系捕捉的复杂规划环境。GFlowNets与VLM的集成不仅提高了模型在多步推理任务中的性能，还展示了在强化学习领域之外的应用潜力。此外，GFlowVLM在实验中展现出的高效训练和泛化能力，为未来相关研究提供了有价值的参考。

## ava--attentive-vlm-agent-for-mastering-starcraft-ii
### Abstract
We introduce Attentive VLM Agent (AVA), a multimodal StarCraft II agent that
aligns artificial agent perception with the human gameplay experience.
Traditional frameworks such as SMAC rely on abstract state representations that
diverge significantly from human perception, limiting the ecological validity
of agent behavior. Our agent addresses this limitation by incorporating RGB
visual inputs and natural language observations that more closely simulate
human cognitive processes during gameplay. The AVA architecture consists of
three integrated components: (1) a vision-language model enhanced with
specialized self-attention mechanisms for strategic unit targeting and
battlefield assessment, (2) a retrieval-augmented generation system that
leverages domain-specific StarCraft II knowledge to inform tactical decisions,
and (3) a dynamic role-based task distribution system that enables coordinated
multi-agent behavior. The experimental evaluation in our proposed AVACraft
environment, which contains 21 multimodal StarCraft II scenarios, demonstrates
that AVA powered by foundation models (specifically Qwen-VL and GPT-4o) can
execute complex tactical maneuvers without explicit training, achieving
comparable performance to traditional MARL methods that require substantial
training iterations. This work establishes a foundation for developing
human-aligned StarCraft II agents and advances the broader research agenda of
multimodal game AI. Our implementation is available at
https://github.com/camel-ai/VLM-Play-StarCraft2.
### 🌟 论文解读 | "AVA：引领星际争霸II智能体新纪元"

### 📌 背景痛点/本文动机
在多智能体强化学习（MARL）领域，星际争霸II已成为一个重要的基准测试环境。然而，现有的研究框架如SMAC等，通常依赖于与人类感知有较大差异的抽象状态表示，这限制了智能体行为的生态效度。本文旨在通过引入一种新的多模态智能体AVA，使智能体的感知方式更接近于人类的游戏体验。

### 🚀 核心方法
💡 创新点1
本文提出了AVACraft环境，它重新设计了观察空间，使其与人类的认知过程保持一致。这个环境包含了RGB视觉输入和自然语言描述，使得智能体能够以类似于人类玩家的方式处理战场信息，从而促进更直观的战略决策。

💡 创新点2
AVA架构由三个集成的组件构成：（1）一种增强的自我关注机制的视觉语言模型，用于战略单位定位和战场评估；（2）一种检索增强的生成系统，利用领域特定的星际争霸II知识来指导战术决策；（3）一种动态角色分配系统，实现协调的多智能体行为。

### 📈 实验结果
在AVACraft环境中，通过21个多模态星际争霸II场景的实验评估表明，AVA在未经过显式训练的情况下，能够执行复杂的战术机动，其性能与需要大量训练迭代的传统MARL方法相当。

### 💬 可借鉴之处
本文为开发与人类感知对齐的星际争霸II智能体奠定了基础，并推动了多模态游戏AI研究的广泛议程。研究中的方法和技术，如多模态感知、视觉语言模型的自我关注机制以及动态角色分配系统，对于未来智能体设计和游戏AI研究具有很高的参考价值。

