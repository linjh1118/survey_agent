# Paper List of Terms(Reward+RL)
- [25/06] **KnowRL: Exploring Knowledgeable Reinforcement Learning for Factuality**  
[[Paper](http://arxiv.org/pdf/2506.19807v1)] [[Code/Page](https://github.com/zjunlp/KnowRL.)] [[TLDR/Notes](#knowrl--exploring-knowledgeable-reinforcement-learning-for-factuality)]

- [25/06] **Learning Task Belief Similarity with Latent Dynamics for Meta-Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2506.19785v1)] [[Code/Page]()] [[TLDR/Notes](#learning-task-belief-similarity-with-latent-dynamics-for-meta-reinforcement-learning)]

- [25/06] **SAGE: Strategy-Adaptive Generation Engine for Query Rewriting**  
[[Paper](http://arxiv.org/pdf/2506.19783v1)] [[Code/Page]()] [[TLDR/Notes](#sage--strategy-adaptive-generation-engine-for-query-rewriting)]

- [25/06] **Tailored Conversations beyond LLMs: A RL-Based Dialogue Manager**  
[[Paper](http://arxiv.org/pdf/2506.19652v1)] [[Code/Page]()] [[TLDR/Notes](#tailored-conversations-beyond-llms--a-rl-based-dialogue-manager)]

- [25/06] **Scaffolding Dexterous Manipulation with Vision-Language Models**  
[[Paper](http://arxiv.org/pdf/2506.19212v1)] [[Code/Page]()] [[TLDR/Notes](#scaffolding-dexterous-manipulation-with-vision-language-models)]

- [25/06] **LongWriter-Zero: Mastering Ultra-Long Text Generation via Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2506.18841v1)] [[Code/Page](https://huggingface.co/THU-KEG/LongWriter-Zero-32B)] [[TLDR/Notes](#longwriter-zero--mastering-ultra-long-text-generation-via-reinforcement-learning)]

- [25/06] **Harnessing the Power of Reinforcement Learning for Language-Model-Based Information Retriever via Query-Document Co-Augmentation**  
[[Paper](http://arxiv.org/pdf/2506.18670v1)] [[Code/Page](https://github.com/liujm2001/CoAugRetriever.)] [[TLDR/Notes](#harnessing-the-power-of-reinforcement-learning-for-language-model-based-information-retriever-via-query-document-co-augmentation)]

- [25/06] **AdapThink: Adaptive Thinking Preferences for Reasoning Language Model**  
[[Paper](http://arxiv.org/pdf/2506.18237v1)] [[Code/Page]()] [[TLDR/Notes](#adapthink--adaptive-thinking-preferences-for-reasoning-language-model)]

- [25/06] **RL for Reasoning by Adaptively Revealing Rationales**  
[[Paper](http://arxiv.org/pdf/2506.18110v1)] [[Code/Page]()] [[TLDR/Notes](#rl-for-reasoning-by-adaptively-revealing-rationales)]

- [25/06] **Aligning Frozen LLMs by Reinforcement Learning: An Iterative Reweight-then-Optimize Approach**  
[[Paper](http://arxiv.org/pdf/2506.17828v1)] [[Code/Page]()] [[TLDR/Notes](#aligning-frozen-llms-by-reinforcement-learning--an-iterative-reweight-then-optimize-approach)]



# TLDR/Notes
## knowrl--exploring-knowledgeable-reinforcement-learning-for-factuality
### Abstract
Large Language Models (LLMs), particularly slow-thinking models, often
exhibit severe hallucination, outputting incorrect content due to an inability
to accurately recognize knowledge boundaries during reasoning. While
Reinforcement Learning (RL) can enhance complex reasoning abilities, its
outcome-oriented reward mechanism often lacks factual supervision over the
thinking process, further exacerbating the hallucination problem. To address
the high hallucination in slow-thinking models, we propose Knowledge-enhanced
RL, KnowRL. KnowRL guides models to perform fact-based slow thinking by
integrating a factuality reward, based on knowledge verification, into the RL
training process, helping them recognize their knowledge boundaries. KnowRL
guides models to perform fact-based slow thinking by integrating a factuality
reward, based on knowledge verification, into the RL training process, helping
them recognize their knowledge boundaries. This targeted factual input during
RL training enables the model to learn and internalize fact-based reasoning
strategies. By directly rewarding adherence to facts within the reasoning
steps, KnowRL fosters a more reliable thinking process. Experimental results on
three hallucination evaluation datasets and two reasoning evaluation datasets
demonstrate that KnowRL effectively mitigates hallucinations in slow-thinking
models while maintaining their original strong reasoning capabilities. Our code
is available at https://github.com/zjunlp/KnowRL.
### 🌟 论文解读 | KnowRL：用知识增强强化学习，给大模型“慢思考”降 hallucination

### 📌 背景痛点/本文动机
大语言模型（尤其是“慢思考”模型）在推理时容易出现严重的 hallucination（事实性错误），原因是它们难以准确识别自身的知识边界。虽然强化学习（RL）能提升复杂推理能力，但其“结果导向”的奖励机制往往对推理过程缺乏事实性监督，反而加剧了 hallucination 问题。此外，现有缓解 hallucination 的方法（如监督微调、检索增强生成、解码阶段干预）存在成本高、效率低或破坏已有策略等缺陷，且难以在降低 hallucination 的同时保留模型强大的推理能力。因此，如何让慢思考模型在保持推理能力的前提下减少事实错误，成为亟待解决的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出 KnowRL 框架  
KnowRL 是一种**知识增强的强化学习**方法，核心是在 RL 训练过程中融入**基于知识验证的事实性奖励**。该奖励参考 FactScore（通过外部知识库验证文本支撑性来评估事实性）设计，引导模型在“慢思考”时基于事实推理，帮助模型更清晰地认知自身知识边界，避免编造事实。  

💡 创新点2：协同优化推理与事实遵循  
传统 RL 只关注最终结果，KnowRL 则直接对推理步骤中的“事实遵循度”进行奖励，让模型学习并内化基于事实的推理策略，在慢思考模型中协同优化“推理能力”和“事实正确性”。  

💡 创新点3：构建高质量事实任务训练集  
为了给 KnowRL 的初始化和训练提供支撑，论文团队构建了精心设计的高质量事实任务训练数据集，弥补了训练阶段事实监督不足的问题。  


### 📈 实验结果
论文在 3 个 hallucination 评估数据集（如 TruthfulQA、SimpleQA 等）和 2 个推理评估数据集（如 GPQA、AIME 2025 等）上验证了 KnowRL 的效果：  
- 基于蒸馏的慢思考模型经 KnowRL 训练后，在多个 hallucination 基准测试中准确率领先（如在 SimpleQA 等任务上表现提升）；  
- 对原本通过 RL 训练的慢思考模型，KnowRL 也能显著降低 hallucination（如在 ChineseSimpleQA 上准确率达 16.23%），同时保留甚至增强其推理能力；  
- 对比基线方法，KnowRL 在缓解 hallucination 上表现更优，且常能让模型推理性能超越原有水平。  


### 💬 可借鉴之处
1. **思路层面**：针对“结果导向 RL 忽略过程事实性”的痛点，提出“用外部知识直接监督推理过程”的思路，为缓解大模型 hallucination 提供了新视角——从**训练阶段的奖励机制**入手，把“事实性”嵌入强化学习流程；  
2. **方法层面**：KnowRL 框架展示了如何将“知识验证”转化为 RL 中的奖励信号，实现推理能力与事实正确性的协同优化，这种“过程监督 + 知识增强”的设计可启发后续强化学习与知识融合的研究；  
3. **工程层面**：论文构建的高质量事实任务数据集，为同类“需事实性监督”的训练工作提供了数据层面的参考，体现了“优质数据 + 精准方法”结合的重要性。  


综上，KnowRL 瞄准大模型慢思考中的 hallucination 难题，通过知识增强的强化学习实现了“降幻觉、保推理”的目标，为大模型更可靠的复杂推理提供了一套新颖解法。

## learning-task-belief-similarity-with-latent-dynamics-for-meta-reinforcement-learning
### Abstract
Meta-reinforcement learning requires utilizing prior task distribution
information obtained during exploration to rapidly adapt to unknown tasks. The
efficiency of an agent's exploration hinges on accurately identifying the
current task. Recent Bayes-Adaptive Deep RL approaches often rely on
reconstructing the environment's reward signal, which is challenging in sparse
reward settings, leading to suboptimal exploitation. Inspired by bisimulation
metrics, which robustly extracts behavioral similarity in continuous MDPs, we
propose SimBelief-a novel meta-RL framework via measuring similarity of task
belief in Bayes-Adaptive MDP (BAMDP). SimBelief effectively extracts common
features of similar task distributions, enabling efficient task identification
and exploration in sparse reward environments. We introduce latent task belief
metric to learn the common structure of similar tasks and incorporate it into
the specific task belief. By learning the latent dynamics across task
distributions, we connect shared latent task belief features with specific task
features, facilitating rapid task identification and adaptation. Our method
outperforms state-of-the-art baselines on sparse reward MuJoCo and panda-gym
tasks.
### 🌟 论文解读 | 基于 latent dynamics 学习任务信念相似性，助力元强化学习新突破

### 📌 背景痛点/本文动机
在元强化学习中，智能体需要利用探索阶段获取的先验任务分布信息来快速适应未知任务，而探索效率取决于能否准确识别当前任务。现有基于贝叶斯自适应的深度强化学习方法常依赖重构环境奖励信号，但在稀疏奖励场景下这颇具挑战，易导致次优利用。同时，现实场景中干扰多、奖励稀疏时，智能体易出现错误探索行为，以往方法也常忽略任务间潜在的共同结构，难以高效识别相似结构任务并实现快速适配。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出SimBelief元强化学习框架  
受连续MDP中双模拟度量（bisimulation metrics）提取行为相似性的启发，在贝叶斯自适应MDP（BAMDP）下提出SimBelief框架，通过度量任务信念的相似性，有效提取相似任务分布的共同特征，在稀疏奖励环境中实现高效任务识别与探索。  

💡 创新点2：引入潜在任务信念度量与学习潜在动力学  
设计潜在任务信念度量来学习相似任务的共同结构并融入特定任务信念；通过学习跨任务分布的潜在动力学，连接共享的潜在任务信念特征与特定任务特征，助力快速任务识别与适配。既利用潜在空间学习到的任务分布整体认知和任务关系，又结合当前学习特定任务的信念，增强智能体对未知环境的适应性。  

💡 创新点3：面向BAMDP的任务表示方法  
为BAMDP中基于上下文的元强化学习算法设计任务表示方法，借助潜在奖励模型、转移模型和逆动力学模型学习任务信念相似性，提升智能体对未知任务的识别与适应能力。  

### 📈 实验结果
在稀疏奖励的MuJoCo和panda - gym任务上，该方法超越了当前最先进的基线方法；同时在处理分布外（OOD）任务时，展现出更强的适应性与泛化能力，验证了方法在不同场景下的有效性。  

### 💬 可借鉴之处
从方法设计角度，将双模拟度量思想引入元强化学习任务信念度量、结合潜在空间学习与特定任务信念的思路，为处理稀疏奖励、多任务适配等难题提供了新范式；从应用角度，在MuJoCo和panda - gym等任务上的成功实践，证明其在机器人控制等需处理复杂任务分布场景的潜力，为相关领域算法设计提供了参考；理论层面，对潜在任务信念度量在BAMDP中的有效性验证，也为后续理论分析和方法拓展筑牢了基础。

## sage--strategy-adaptive-generation-engine-for-query-rewriting
### Abstract
Query rewriting is pivotal for enhancing dense retrieval, yet current methods
demand large-scale supervised data or suffer from inefficient reinforcement
learning (RL) exploration. In this work, we first establish that guiding Large
Language Models (LLMs) with a concise set of expert-crafted strategies, such as
semantic expansion and entity disambiguation, substantially improves retrieval
effectiveness on challenging benchmarks, including HotpotQA, FEVER, NFCorpus,
and SciFact. Building on this insight, we introduce the Strategy-Adaptive
Generation Engine (SAGE), which operationalizes these strategies in an RL
framework. SAGE introduces two novel reward shaping mechanisms-Strategic Credit
Shaping (SCS) and Contrastive Reward Shaping (CRS)-to deliver more informative
learning signals. This strategy-guided approach not only achieves new
state-of-the-art NDCG@10 results, but also uncovers a compelling emergent
behavior: the agent learns to select optimal strategies, reduces unnecessary
exploration, and generates concise rewrites, lowering inference cost without
sacrificing performance. Our findings demonstrate that strategy-guided RL,
enhanced with nuanced reward shaping, offers a scalable, efficient, and more
interpretable paradigm for developing the next generation of robust information
retrieval systems.
### 🌟 论文解读 | SAGE：用策略引导+强化学习革新查询重写，解锁密集检索新范式

### 📌 背景痛点/本文动机
在信息检索（IR）领域，密集检索系统性能很大程度取决于输入查询质量，查询重写是弥合用户意图与机器理解间差距的关键。但当前方法存在两大难题：传统有监督微调需大规模昂贵人工标注；现代强化学习（RL）方法（如PPO、GRPO）常因探索低效，阻碍最优重写策略发现，还可能引发训练不稳定甚至输出不连贯等问题。此外，过往基于策略的提示方法针对通用网页搜索稀疏检索设计，难适配密集检索的精细需求，在专业基准测试中效果有限。同时，查询重写任务还存在“奖励黑客”现象——模型会偷懒复制原查询拿高分，陷入局部最优，限制有效探索。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：设计面向密集检索的专家策略  
提出5种专为密集检索场景设计的查询重写策略（如语义扩展、实体消歧等），仅通过提示引导大语言模型（LLM），就在HotpotQA、FEVER等多个挑战性基准测试中显著提升检索效果，展现纯提示方式能达到的性能上限。  

💡 创新点2：提出SAGE强化学习框架  
构建**Strategy-Adaptive Generation Engine（SAGE）**，将人工设计策略系统集成到GRPO算法的强化学习循环中，引导LLM学习更优查询重写策略。同时引入两种新颖奖励塑造机制：  
- **Strategic Credit Shaping（SCS）**：依据各策略的整体表现分配“信用”，提供更具策略针对性的学习信号；  
- **Contrastive Reward Shaping（CRS）**：把绝对分数转化为相对性能度量，让奖励更能反映策略优劣差异。  

💡 创新点3：对抗“奖励黑客”的探索机制  
通过针对性提示工程，加上对与原查询完全相同输出的惩罚机制，强制模型跳出“复制原查询拿高分”的安全陷阱，推动模型探索更有价值的重写策略。  


### 📈 实验结果
在HotpotQA和NFCorpus等挑战性基准测试中，SAGE在NDCG@10指标上实现了当前最优（SOTA）的密集检索效果。更引人注目的是**涌现行为**：模型学会更高效的推理过程，大幅减少token使用量，在无需显式优化推理成本的情况下，降低了推理延迟与计算开销。同时，消融实验验证了“强制探索+惩罚机制”对避免“奖励黑客”、提升模型性能的关键作用。  


### 💬 可借鉴之处
1. **策略引导的价值**：少量可解释的人工策略能在无额外训练时显著提升LLM查询重写质量，提示工程与领域知识结合的思路值得在垂直任务中复用；  
2. **强化学习与领域适配**：SAGE展示了把领域专属策略嵌入RL框架的可行性，为垂直领域（如医疗、法律检索）定制RL方案提供参考；  
3. **奖励塑造的精细度**：SCS和CRS证明对奖励信号做任务定制化改造，能让RL更高效学习，类似思路可推广到其他生成式任务（如对话生成、代码生成）的奖励设计；  
4. **对抗“偷懒”行为**：针对任务中模型易陷入的局部最优（如“复制原输入”），设计简单有效的惩罚与探索机制，是训练鲁棒RL模型的重要实践经验。  

SAGE用“策略引导+强化学习+精细奖励塑造”的组合拳，为下一代鲁棒信息检索系统开辟了可扩展、高效且更具可解释性的新范式，也为LLM在垂直任务中突破“低效探索”与“标注依赖”困境提供了宝贵借鉴。

## tailored-conversations-beyond-llms--a-rl-based-dialogue-manager
### Abstract
In this work, we propose a novel framework that integrates large language
models (LLMs) with an RL-based dialogue manager for open-ended dialogue with a
specific goal. By leveraging hierarchical reinforcement learning to model the
structured phases of dialogue and employ meta-learning to enhance adaptability
across diverse user profiles, our approach enhances adaptability and
efficiency, enabling the system to learn from limited data, transition fluidly
between dialogue phases, and personalize responses to heterogeneous patient
needs. We apply our framework to Motivational Interviews, aiming to foster
behavior change, and demonstrate that the proposed dialogue manager outperforms
a state-of-the-art LLM baseline in terms of reward, showing a potential benefit
of conditioning LLMs to create open-ended dialogue systems with specific goals.
### 🌟 论文解读 | 超越大模型的个性化对话：基于强化学习的对话管理器

### 📌 背景痛点/本文动机
近年来，心理健康服务需求激增，但资源供给不足，患者等待治疗时间漫长。动机式访谈（Motivational Interviewing，MI）这类能辅助心理干预的对话场景，对对话系统提出了高要求：既需按engagement（建立关系）、focusing（明确核心）、evoking（激发动机）、planning（制定计划）等结构化阶段推进，又要适配不同患者画像（如Open - to - Change、Resistant - to - Change、Receptive三类）。传统基于规则的对话系统虽可控、可解释，但适应性差、开发成本高；大语言模型（LLMs）虽适应性和生成能力强，却存在可控性、透明度与效率不足，且融入领域知识需大量数据等问题。因此，本文旨在结合二者优势，提出整合LLMs与基于强化学习（RL）对话管理器的框架，用于有特定目标（如MI场景促进行为改变）的开放式对话。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：混合架构设计——LLMs与RL对话管理器结合
提出整合大语言模型与基于强化学习的对话管理器的新颖框架，用于有特定目标的开放式对话。借助RL对话管理器来调控LLMs，在发挥LLMs生成能力与适应性的同时，弥补其可控性等方面的不足，实现适应性与控制感的平衡，为虚拟治疗支持类对话系统提供新思路。
💡 创新点2：分层强化学习建模对话阶段
利用分层强化学习对对话的结构化阶段（如MI的engagement、focusing、evoking、planning等阶段）进行建模。让系统能在不同对话阶段间流畅过渡，应对MI这类需分阶段推进且阶段间可能非严格线性的复杂对话场景，解决传统LLMs缺乏对话阶段结构化决策的问题。
💡 创新点3：元学习增强用户画像适应性
采用元学习来提升系统对不同用户画像（如MI中三类患者）的适应性。使系统能从有限数据中学习，针对异质患者需求实现响应个性化，克服传统基于规则系统适应性差以及LLMs适配不同用户需大量数据的缺陷。

### 📈 实验结果
将所提框架应用于动机式访谈（MI）场景以促进行为改变，实验表明，与最先进的大语言模型基线相比，该对话管理器在奖励方面表现更优，证明了给大语言模型增加条件约束以构建有特定目标的开放式对话系统存在潜在益处。

### 💬 可借鉴之处
1. 混合系统思路：在需结合生成能力、适应性与领域可控性的场景（如医疗咨询、教育对话等垂直领域），可借鉴这种“大模型 + 领域特定对话管理器”的混合架构，平衡不同技术范式的优缺点。
2. 分层与元学习应用：面对有阶段结构、用户差异大的对话任务，分层强化学习对阶段建模和元学习对用户适配的思路，可为提升系统在复杂场景下的效率与个性化能力提供参考。
3. 垂直领域落地：在心理健康等资源紧张且对对话专业性要求高的垂直领域，该框架验证了技术辅助人类服务的可行性，为后续开发虚拟辅助工具提供了技术路线范例。

## scaffolding-dexterous-manipulation-with-vision-language-models
### Abstract
Dexterous robotic hands are essential for performing complex manipulation
tasks, yet remain difficult to train due to the challenges of demonstration
collection and high-dimensional control. While reinforcement learning (RL) can
alleviate the data bottleneck by generating experience in simulation, it
typically relies on carefully designed, task-specific reward functions, which
hinder scalability and generalization. Thus, contemporary works in dexterous
manipulation have often bootstrapped from reference trajectories. These
trajectories specify target hand poses that guide the exploration of RL
policies and object poses that enable dense, task-agnostic rewards. However,
sourcing suitable trajectories - particularly for dexterous hands - remains a
significant challenge. Yet, the precise details in explicit reference
trajectories are often unnecessary, as RL ultimately refines the motion. Our
key insight is that modern vision-language models (VLMs) already encode the
commonsense spatial and semantic knowledge needed to specify tasks and guide
exploration effectively. Given a task description (e.g., "open the cabinet")
and a visual scene, our method uses an off-the-shelf VLM to first identify
task-relevant keypoints (e.g., handles, buttons) and then synthesize 3D
trajectories for hand motion and object motion. Subsequently, we train a
low-level residual RL policy in simulation to track these coarse trajectories
or "scaffolds" with high fidelity. Across a number of simulated tasks involving
articulated objects and semantic understanding, we demonstrate that our method
is able to learn robust dexterous manipulation policies. Moreover, we showcase
that our method transfers to real-world robotic hands without any human
demonstrations or handcrafted rewards.
### 🌟 论文解读 | 用视觉语言模型为灵巧操作“搭脚手架”

### 📌 背景痛点/本文动机
灵巧机械手对执行复杂操作任务至关重要，但由于示范数据收集难、高维控制复杂，训练起来颇具挑战。强化学习（RL）虽能通过仿真生成经验缓解数据瓶颈，却依赖精心设计的特定任务奖励函数，限制了扩展性与泛化性。当下灵巧操作研究常借助参考轨迹引导RL策略探索，可获取合适轨迹（尤其针对灵巧手）仍是难题，且参考轨迹的精确细节对最终经RL优化的运动而言并非必需。于是，论文提出利用视觉语言模型（VLMs）编码的常识性空间与语义知识，来生成引导RL的“脚手架”轨迹。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：借助视觉语言模型生成“脚手架”轨迹  
给定任务描述（如“打开橱柜”）和视觉场景，利用现成的VLMs先识别任务相关关键点（如把手、按钮），再合成手和物体运动的3D轨迹。这些轨迹作为“粗粒度”引导，无需精确到人类示范级细节，却能为RL提供探索方向与奖励依据。  

💡 创新点2：残差强化学习策略跟踪轨迹  
在仿真环境中训练低层次残差RL策略，让其高精度跟踪VLMs生成的“脚手架”轨迹。RL通过优化每一步的偏移和手指动作来最大化跟踪奖励，无需人工设计复杂奖励函数，还能在过程中超越人类遥操作的性能与精度。  

💡 创新点3：利用VLMs特性提升泛化与鲁棒性  
通过重复查询VLMs，随机化初始关键点和高层轨迹，让策略在测试时能泛化到未见过的初始条件与新轨迹；当VLMs高层规划有误差时，提供上下文示例可大幅提升性能。  

### 📈 实验结果
在涉及铰接物体和语义理解的多个仿真任务中，论文方法在8个任务上，无需手动奖励设计就能达到接近“ oracle 级”手工轨迹的成功率与泛化能力。此外，还成功实现了向真实世界灵巧机械手的跨域迁移，在无人类示范和手工奖励情况下仍能达成鲁棒操作性能。  

### 💬 可借鉴之处
1. 跨模态协作思路：将VLMs的语义空间推理能力与RL的控制优化能力结合，为解决高维复杂控制任务提供了“高层语义引导 + 低层精确优化”的新范式，可推广到需语义理解与精细操作结合的机器人任务。  
2. 弱化对精确示范的依赖：证明粗粒度轨迹足以支撑RL训练，为减少机器人学习对大规模高质量示范数据集的依赖提供了可行路径，降低任务拓展时的数据采集成本。  
3. 泛化与迁移技巧：利用VLMs生成多样化轨迹来增强泛化、通过上下文示例提升鲁棒性等手段，为基于大模型的机器人学习在实际部署（如环境变化、模型误差场景）提供了实用方法论。

## longwriter-zero--mastering-ultra-long-text-generation-via-reinforcement-learning
### Abstract
Ultra-long generation by large language models (LLMs) is a widely demanded
scenario, yet it remains a significant challenge due to their maximum
generation length limit and overall quality degradation as sequence length
increases. Previous approaches, exemplified by LongWriter, typically rely on
''teaching'', which involves supervised fine-tuning (SFT) on synthetic
long-form outputs. However, this strategy heavily depends on synthetic SFT
data, which is difficult and costly to construct, often lacks coherence and
consistency, and tends to be overly artificial and structurally monotonous. In
this work, we propose an incentivization-based approach that, starting entirely
from scratch and without relying on any annotated or synthetic data, leverages
reinforcement learning (RL) to foster the emergence of ultra-long, high-quality
text generation capabilities in LLMs. We perform RL training starting from a
base model, similar to R1-Zero, guiding it to engage in reasoning that
facilitates planning and refinement during the writing process. To support
this, we employ specialized reward models that steer the LLM towards improved
length control, writing quality, and structural formatting. Experimental
evaluations show that our LongWriter-Zero model, trained from Qwen2.5-32B,
consistently outperforms traditional SFT methods on long-form writing tasks,
achieving state-of-the-art results across all metrics on WritingBench and
Arena-Write, and even surpassing 100B+ models such as DeepSeek R1 and
Qwen3-235B. We open-source our data and model checkpoints under
https://huggingface.co/THU-KEG/LongWriter-Zero-32B
### 🌟 论文解读 | LongWriter-Zero：用强化学习突破超长文本生成难题

### 📌 背景痛点/本文动机
超长文本生成（如万字级报告、叙事创作等）是大语言模型（LLM）在实际场景中至关重要的能力，但现有技术面临两大核心挑战：一是模型生成长度存在上限，二是随着文本长度增加，内容质量（连贯性、一致性、结构合理性等）会显著下降。  

此前主流方案（如LongWriter）依赖**有监督微调（SFT）**，即在人工构造的“指令 - 长文本输出”配对数据上训练模型。但这种方式存在明显缺陷：  
- 构造高质量的合成SFT数据成本极高、难度大；  
- 合成数据往往缺乏连贯性与一致性，且风格单一、过度“人工化”；  
- SFT的最大似然目标无法显式优化全局层面的文本属性（如整体连贯性、格式一致性）。  

为突破这些限制，本文提出**完全从零开始、不依赖任何标注/合成数据**的强化学习（RL）方案，让LLM自主“进化”出超长高质量文本生成能力。  


### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：基于强化学习的无监督超长文本生成框架  
传统SFT依赖固定参考文本，而本文采用强化学习，让模型通过**奖励信号**优化长文本生成的全局目标（无需人工构造SFT数据集）。具体采用Group Relative Policy Optimization（GRPO）算法训练策略网络：从基础模型（如Qwen2.5 - 32B）出发，让模型在“写作过程中自主规划与迭代”，逐步掌握超长文本生成能力。  

💡 创新点2：多维度奖励模型设计（Reward Design）  
针对开放域文本生成的复杂性（主观性、多维度），设计**复合奖励函数**，整合多个专项奖励模型（RM），分别引导模型优化以下关键维度：  
- 长度控制（Length RM）：确保输出满足“超长”需求，同时避免无意义冗余；  
- 写作质量（Quality RM）：评估内容流畅度、逻辑性、专业性等；  
- 结构格式（Structure RM）：保障文本结构合理（如分章节、层次清晰）。  

💡 创新点3：测试时缩放（Test - time Scaling）与持续预训练（Continual Pretraining）  
- 测试时缩放：借鉴大模型在数学/代码任务中“长思维链（CoT）”的成功经验，探索在超长文本生成中引入长CoT，增强模型推理与规划能力；  
- 持续预训练：在长文本素材与推理数据上持续预训练，进一步提升RL训练后模型的性能上限。  


### 📈 实验结果
- 基准测试碾压传统SFT：基于Qwen2.5 - 32B训练的LongWriter - Zero，在WritingBench、Arena - Write等长文本写作基准测试中，**全面超越传统SFT方法**；  
- 超越千亿参数模型：在多项指标上击败DeepSeek R1、Qwen3 - 235B等百 billion + 规模的大模型，刷新SOTA；  
- 开源资源丰富：模型 checkpoint 和数据已开源（https://huggingface.co/THU - KEG/LongWriter - Zero - 32B），为社区提供了可复现、可扩展的基础。  


### 💬 可借鉴之处
1. 范式创新：证明强化学习可在“无标注/合成数据”场景下，激活LLM的超长文本生成能力，为大模型能力解锁提供了“非SFT”的新范式；  
2. 奖励工程：多维度复合奖励模型的设计思路，可迁移到其他开放域生成任务（如创意写作、多轮对话），用于刻画“主观性强、无明确ground - truth”场景下的质量评估；  
3. 训练策略：测试时缩放（长CoT）与持续预训练的组合，为提升大模型长文本推理、生成的上限提供了可复用的技术路线；  
4. 落地价值：针对真实世界“超长文本需求”（如报告撰写、法律文书、教育内容创作），提供了更优质的技术方案，推动LLM在专业领域的落地。  


LongWriter - Zero的工作不仅解决了超长文本生成的技术痛点，更展示了强化学习在大模型能力进化中的潜力——无需依赖大量人工标注，也能让模型“自主学习”复杂任务的完成能力。这为大模型研发范式、奖励机制设计等方向，都带来了极具启发性的参考。

## harnessing-the-power-of-reinforcement-learning-for-language-model-based-information-retriever-via-query-document-co-augmentation
### Abstract
Recent studies have proposed leveraging Large Language Models (LLMs) as
information retrievers through query rewriting. However, for challenging
corpora, we argue that enhancing queries alone is insufficient for robust
semantic matching; the LLM should also have sufficient understanding of the
corpus by directly handling and augmenting the documents themselves. To this
end, we present an LLM-based retriever empowered to augment both user queries
and corpus documents, with its policy fully explored via reinforcement learning
(RL) and minimal human inductive bias. Notably, we find that simply allowing
the LLM to modify documents yields little benefit unless paired with our
carefully designed bidirectional RL framework, which enables the LLM to
simultaneously learn and collaborate on both query and document augmentation
policies. A key technical challenge in realizing such a framework lies in
jointly updating both policies during training, where the rewards for the two
directions depend on each other, making their entangled reward intractable. Our
approach addresses this by introducing a reward sampling strategy and a
specifically designed RL algorithm that enables effective training with these
sampled rewards. Experimental results demonstrate that our approach
significantly enhances LLM-based retrieval performance in both sparse and dense
settings, particularly in difficult retrieval domains, and achieves strong
cross-benchmark generalization. Our code is released at
https://github.com/liujm2001/CoAugRetriever.
### 🌟 论文解读 | 强化学习赋能大模型检索： query-document 双向协同增强新范式

### 📌 背景痛点/本文动机
信息检索（IR）在检索增强生成（RAG）等AI场景中至关重要，传统方法通过查询重写提升检索精度，但面对复杂语料库时仅优化查询不够，大语言模型（LLM）需对文档本身也有充分理解。现有基于LLM的检索多聚焦查询改写，在挑战性领域（如紧凑语料精准检索）性能仍有提升空间，因此本文提出让LLM同时增强查询与文档以实现更鲁棒语义匹配的思路。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：Query-Document 协同增强范式  
突破仅优化查询的局限，让LLM同时对用户查询和语料库文档进行增强，通过直接处理与改写文档，使LLM充分理解语料，拉近查询与文档语义关联，拓宽LLM在检索任务中的“行动空间”，为挑战性语料检索探索更优策略。  

💡 创新点2：双向强化学习（RL）框架设计  
单纯让LLM修改文档收益有限，需配套精心设计的双向RL框架。训练时要解决查询与文档增强策略相互依赖、奖励纠缠难处理的问题，为此提出**奖励采样策略**与定制化RL算法，让模型能在单流程中联合学习双向增强策略，实现查询与文档增强的协作，克服大动作空间下精确奖励计算难题。还采用“batch - unbatch交替”实现方式适配现有LLM RL框架，保障双向设置下高效训练。  


### 📈 实验结果
在稀疏（如基于TF - IDF、BM25）和稠密（基于预训练语言模型嵌入）检索场景的挑战性IR基准测试中，该方法显著提升基于LLM的检索性能，尤其在高难度检索领域效果突出；同时展现强跨基准泛化能力，证明通过强化学习让LLM自探索获得了IR任务通用能力。  

### 💬 可借鉴之处
1. 任务视角拓展：打破信息检索中“重查询轻文档”的传统优化惯性，启示在其他需双向/多向交互优化的任务（如多模态匹配、对话系统上下文优化）中，思考对双方/多方对象同时增强的可能性。  
2. 强化学习应用创新：面对多策略纠缠、奖励难处理的复杂场景，本文“奖励采样 + 定制算法 + 工程化实现适配”的思路，为RL在大模型复杂任务（如多轮对话策略学习、多智能体协作）落地提供了处理高维动作空间与纠缠奖励的参考范式。  
3. 泛化能力重视：在方法设计中关注跨基准泛化，这种追求通用能力而非仅单任务最优的思路，符合大模型时代技术落地对通用性、鲁棒性的需求，值得同类研究借鉴。

## adapthink--adaptive-thinking-preferences-for-reasoning-language-model
### Abstract
Reinforcement Learning (RL)-based post-training has significantly advanced
the complex reasoning capabilities of language models, fostering sophisticated
self-reflection processes. However, this ``slow thinking'' paradigm presents a
critical challenge to reasoning efficiency: models may expend excessive
computation on simple questions and shift reasoning prematurely for complex
ones. Previous mechanisms typically rely on static length budgets or predefined
rules, lacking the adaptability for varying question complexities and models'
evolving capabilities. To this end, we propose AdapThink, an adaptive
post-training framework designed to induce more efficient thinking while
maintaining the performance of reasoning language models. Specifically,
AdapThink incorporates two key mechanisms: 1) A group-relative reward function
that leverages model confidence and response's characteristic to dynamically
adjust the preference of reflection-related transition words without resorting
to a fixed length preference. 2) A diversity-aware sampling mechanism that
balances the training group's solution accuracy with reasoning diversity via an
entropy-guided score. Experiments on several mathematical reasoning datasets
with DeepSeek-distilled models demonstrate AdapThink's advantages in enabling
adaptive reasoning patterns and mitigating the inefficiencies.
### 🌟 论文解读 | AdapThink：让推理语言模型拥有自适应“思考偏好”

### 📌 背景痛点/本文动机
基于强化学习（RL）的后训练极大提升了语言模型的复杂推理能力，催生了精细的自我反思过程（即“慢思考”范式）。但这一范式存在推理效率难题：模型面对简单问题时可能过度计算，面对复杂问题时又可能过早切换推理思路。以往机制依赖静态长度预算或预定义规则，缺乏对问题复杂度变化和模型能力演进的适应性。因此，需要一种自适应后训练框架，在维持推理性能的同时提升效率，AdapThink 应运而生。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：组相对奖励函数  
设计了一种新颖的组相对奖励函数来调整模型当前推理偏好。模型可基于生成响应的组内准确率，确定合适的反思偏好；同时通过统计训练样本组中关键过渡词数量，定量衡量推理效率，无需依赖固定长度偏好，而是利用模型置信度与响应特征动态调整反思类过渡词的偏好。  

💡 创新点2：多样性感知采样机制  
提出多样性感知采样机制平衡训练样本组的解题准确率与推理多样性。先对推理实例过采样，再用精心定义的多样性指标评估实例的最终答案与中间步骤，最后通过多样性感知下采样来筛选和提升用于 RL 后训练的实例整体质量。  


### 📈 实验结果
在多个数学推理数据集上，使用 DeepSeek 蒸馏模型进行实验。结果表明，AdapThink 在使模型具备自适应推理模式、缓解推理低效问题上展现优势。如对上下文长度限制仅 2K token 的 DeepSeek - 蒸馏 Qwen 模型进行后训练后，在 8K - token 限制下测试，相比多个长度控制基线方法表现更优，证明了其在多个推理基准上打造强大且高效的思维链（CoT）模型的有效性。

### 💬 可借鉴之处
1. 打破静态长度限制思维，通过分析样本组推理模式分布来调整长度偏好，为处理模型推理效率与复杂度适配问题提供了新视角，不再局限于固定规则约束。  
2. 组相对奖励函数与多样性感知采样机制的设计思路，可迁移到其他需要平衡性能与效率、兼顾多样性与准确性的模型训练任务中，尤其是涉及反思、推理类的语言模型优化场景。  
3. 对推理过程中关键过渡词（如“Pause - Validation”“Branch - Extension”类词汇）的分析与利用方式，为后续研究如何从语言表达特征层面引导模型推理行为提供了参考范式。

## rl-for-reasoning-by-adaptively-revealing-rationales
### Abstract
We propose that reinforcement learning (RL) from partial expert
demonstrations is not merely a training heuristic, but a promising framework
for solving complex sequence generation tasks. Supervised fine-tuning (SFT)
relies on dense ground-truth labels, which become increasingly costly as
sequence length grows. RL, on the other hand, struggles with sparse rewards and
a combinatorially large output space. We address this by introducing adaptive
backtracking (AdaBack), a per-sample curriculum learning algorithm that reveals
only a partial prefix of the target output during training. The supervision
length is adjusted dynamically for each sample based on the model's past reward
signal, allowing it to incrementally learn to complete reasoning chains by
conditioning on correct partial solutions. We investigate this intermediate
regime between SFT and RL and argue that per-sample curriculum learning is more
than a trade-off between efficiency and generality, it can succeed in tasks
with long sequences of latent dependencies where SFT and RL both fail to
generalize. Using a synthetic task with latent parity constraints, we show that
our adaptive curriculum over partial answers reliably solves problems that are
otherwise intractable. On mathematical reasoning benchmarks (MATH, GSM8k), we
find that curriculum learning enables models to solve problems that RL alone
cannot, acquiring new reasoning capabilities through incremental exposure to
partial solutions.
### 🌟 论文解读 | 自适应揭示推理依据：用强化学习突破复杂序列生成困境

### 📌 背景痛点/本文动机
在复杂序列生成任务（如数学推理、算法推理等）中，现有方法存在明显局限：监督微调（SFT）依赖密集的真实标签，序列越长标注成本越高；强化学习（RL）则受限于稀疏奖励与指数级增长的输出空间，探索有效解的难度随序列长度指数级上升。同时，获取专业领域（如数学）的大规模高质量推理轨迹成本极高，而标准RL在长推理链任务中易陷入“只强化已有路径、难探索新解”的困境。因此，论文探索SFT与RL之间的中间范式，尝试通过**分阶段揭示部分推理依据**来让模型逐步学习复杂推理，解决SFT和RL都难以泛化的长隐依赖序列任务。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出AdaBack自适应回溯算法  
AdaBack是一种**逐样本的课程学习算法**，训练时仅暴露目标输出的部分前缀作为监督，且基于模型过往奖励信号动态调整每个样本的监督长度。它让模型从“依赖较多前缀提示完成推理”逐步过渡到“仅需少量提示甚至自主推理”，把长推理链拆解为可逐步攻克的子问题，实现从全监督到全探索的自适应过渡，无需人工设计课程阶段或调度策略。  

💡 创新点2：架起SFT与RL的桥梁  
聚焦SFT（依赖全监督）和RL（依赖稀疏奖励）之间的“中间地带”，通过**动态调整每个样本的监督暴露程度**，让模型在“部分正确解提示”下增量学习推理链。这种方式既缓解了SFT的标注压力，又解决了RL在长序列下奖励稀疏、探索困难的问题，让模型能学习到SFT和RL单独训练学不会的推理能力。  

💡 创新点3：面向通用离散序列的自适应策略  
不同于依赖“明确推理步骤分隔符”的方法（如R3需特定分隔符分段），AdaBack不要求推理步骤清晰可分，而是基于**每个样本自身难度**做自适应调整（借助GRPO框架对每个问题生成多轮rollout并平均奖励来估计难度），更适配无明确步骤划分的通用离散序列任务（如数学竞赛题MATH数据集）。  


### 📈 实验结果
1. 合成任务（隐奇偶约束任务）：AdaBack能稳定解决SFT、RL及二者组合都无法处理的问题，验证了“拆分长推理链为子问题、动态调整监督”策略的有效性。  
2. 数学推理基准（MATH、GSM8k）：AdaBack在标准RL和SFT+RL pipeline上表现更优；对基础模型直接应用AdaBack，性能常能匹配SFT初始化的模型。  
3. 泛化性测试（GSM8k变种）：在“Base - 7（模型预训练未见过的数值格式）”和“Tensor - 2（拼接问题增加推理深度）”任务中，AdaBack展现强泛化能力，能应对符号变化与长 horizon 推理。  
4. Pass@k指标验证：AdaBack显著提升Pass@k（尤其无SFT时），说明它不是简单重加权已有解，而是让模型发现了新推理路径。  


### 💬 可借鉴之处
1. 课程学习的自适应思路：在需“逐步解锁复杂度”的任务中，可参考“依模型反馈动态调整监督/提示量”的范式，避免人工设计课程的繁琐与僵化。  
2. SFT与RL的中间态探索：当任务既需“监督引导”又需“自主探索”时，“部分揭示正确解+RL优化”的思路为平衡二者提供了新方向。  
3. 长依赖序列任务的解法：面对标注贵、探索难的长推理/长生成任务（如代码生成、数学证明），拆分任务+动态监督的模式或能突破现有方法瓶颈。  
4. 泛化性与新解发现：若希望模型突破“复用已有路径”、真正学会新推理逻辑，AdaBack式的“基于反馈调整监督，驱动探索新解”机制值得借鉴。  

## aligning-frozen-llms-by-reinforcement-learning--an-iterative-reweight-then-optimize-approach
### Abstract
Aligning large language models (LLMs) with human preferences usually requires
fine-tuning methods such as RLHF and DPO. These methods directly optimize the
model parameters, so they cannot be used in test-time to improve model
performance, nor are they applicable when the model weights are not accessible.
In contrast, test-time methods sidestep weight updates by leveraging reward
functions to guide and improve output quality. However, they incur high
inference costs, and their one-shot guidance is often based on imperfect reward
or value functions, leading to suboptimal outputs. In this work, we present a
method named Iterative Reweight-then-Optimize (IRO), a reinforcement learning
(RL) framework that performs RL-style alignment of the (frozen) base model
without touching its parameters. During training, each iteration (i) samples
candidates from the base model, (ii) resamples using current value functions,
and (iii) trains a new lightweight value function that guides the next decoding
pass. At test time, the value functions are used to guide the base model
generation via a search-based optimization process. Notably, users can apply
IRO to align a model on their own dataset, similar to OpenAI's reinforcement
fine-tuning (RFT), but without requiring access to the model weights.
### 🌟 论文解读 | 无需修改模型权重，用强化学习对齐冻结大模型：迭代重加权优化法

### 📌 背景痛点/本文动机
大语言模型（LLMs）对齐人类偏好通常依赖RLHF、DPO等微调方法，这类方法需直接优化模型参数，在测试阶段无法提升性能，且模型权重不可访问时也无法使用。测试时对齐方法虽绕开权重更新，但推理成本高，且基于不完善奖励或价值函数的一次性指导易产生次优输出。在此背景下，本文聚焦于：给定冻结LLM和结果奖励模型（ORM），如何在测试时高效改进或定制模型，同时最小化推理成本。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出迭代重加权 - 优化（IRO）框架  
IRO是受强化学习启发的框架，无需修改冻结基础模型参数就能实现类RL的对齐。训练时通过三步迭代：从基础模型采样候选、用当前价值函数重采样、训练新轻量级价值函数指导下一次解码；测试时利用学习到的价值函数序列，通过基于搜索的优化过程引导基础模型生成。  

💡 创新点2：类策略迭代与高效推理  
从理论上证明，在温和条件下IRO属于一种策略迭代，测试时能以指数级更少的tokens达到Best - of - N（BoN）搜索的性能。且用户可类似OpenAI的强化微调（RFT），用IRO在自有数据集上以RL风格微调模型，还无需访问模型权重。  

### 📈 实验结果
在AlpacaEval 2.0等具有挑战性的指令跟随基准测试中，IRO显著提高了长度控制胜率。如Llama - 3 - 8B - Instruct从30.71%提升到43.80%，Meta - Llama - 3 - 70B - Instruct从43.11%提升到49.77%（与GPT - 4响应对比）。此外，即使使用小尺寸（1B或7B）价值函数引导大基础模型（6.9B或70B），IRO也持续优于BoN、weak - to - strong search等现有测试时对齐基线。  

### 💬 可借鉴之处
对于无法获取模型权重但需在测试阶段优化模型对齐人类偏好的场景，IRO提供了新范式，其迭代训练轻量价值函数 + 测试时搜索优化的思路，为低推理成本下的模型性能提升和领域适配开辟路径；理论上对策略迭代的证明，也为后续强化学习在冻结模型对齐方向的研究提供了理论支撑；同时在工业界，类似OpenAI RFT但无需权重访问的特性，让企业在自有数据定制模型时更具灵活性。

