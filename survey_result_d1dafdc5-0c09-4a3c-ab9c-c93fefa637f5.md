# Paper List of Terms(grm+RL)
- [25/06] **ReasonGRM: Enhancing Generative Reward Models through Large Reasoning Models**  
[[Paper](http://arxiv.org/pdf/2506.16712v1)] [[Code/Page]()] [[TLDR/Notes](#reasongrm--enhancing-generative-reward-models-through-large-reasoning-models)]

- [25/05] **Generative RLHF-V: Learning Principles from Multi-modal Human Preference**  
[[Paper](http://arxiv.org/pdf/2505.18531v1)] [[Code/Page](https://generative-rlhf-v.github.io.)] [[TLDR/Notes](#generative-rlhf-v--learning-principles-from-multi-modal-human-preference)]

- [25/05] **Action-Dependent Optimality-Preserving Reward Shaping**  
[[Paper](http://arxiv.org/pdf/2505.12611v1)] [[Code/Page]()] [[TLDR/Notes](#action-dependent-optimality-preserving-reward-shaping)]

- [25/04] **Inference-Time Scaling for Generalist Reward Modeling**  
[[Paper](http://arxiv.org/pdf/2504.02495v2)] [[Code/Page]()] [[TLDR/Notes](#inference-time-scaling-for-generalist-reward-modeling)]



# TLDR/Notes
## reasongrm--enhancing-generative-reward-models-through-large-reasoning-models
### Abstract
Generative Reward Models (GRMs) provide greater flexibility than scalar
reward models in capturing human preferences, but their effectiveness is
limited by poor reasoning capabilities. This often results in incomplete or
overly speculative reasoning paths, leading to hallucinations or missing key
information in complex tasks. We address this challenge with ReasonGRM, a
three-stage generative reward modeling framework. In the first stage, Zero-RL
is used to generate concise, outcome-directed reasoning paths that reduce the
likelihood of critical omissions. In the second stage, we introduce a novel
evaluation metric, $R^\star$, which scores reasoning paths based on their
generation likelihood. This favors paths that reach correct answers with
minimal exploration, helping to reduce hallucination-prone data during
training. In the final stage, the model is further refined through
reinforcement learning on challenging examples to enhance its preference
discrimination capabilities. Experiments on three public benchmarks show that
ReasonGRM achieves competitive or state-of-the-art performance, outperforming
previous best GRMs by 1.8\% on average and surpassing proprietary models such
as GPT-4o by up to 5.6\%. These results demonstrate the effectiveness of
reasoning-aware training and highlight the importance of high-quality rationale
selection for reliable preference modeling.
```
### 🌟 论文解读 | ReasonGRM：借大模型推理能力革新生成式奖励模型

### 📌 背景痛点/本文动机
大语言模型（LLMs）在理解、生成与决策上取得长足进步，但要让模型输出贴合人类价值观，奖励模型（RM）是关键。传统标量奖励模型（SRMs）把复杂人类偏好压缩成单一标量，易信息丢失、泛化性弱；新兴生成式奖励模型（GRMs）虽更灵活，但推理能力不足，常出现推理路径不完整或过度推测，导致任务中“幻觉”或关键信息缺失。因此，如何提升GRMs的推理质量以实现可靠偏好建模，成了核心问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出ReasonGRM三阶段框架  
ReasonGRM分三步打造更优生成式奖励模型：  
- 阶段一（生成推理路径）：用Zero - RL生成简洁、以结果为导向的推理路径，减少关键信息遗漏风险；  
- 阶段二（筛选优质路径）：引入全新评估指标\( R^\star \)，依据生成可能性为推理路径打分，偏好“用最少探索达正确答案”的路径，削减训练中易引发幻觉的数据；  
- 阶段三（强化模型能力）：针对高难度示例用强化学习进一步精调模型，增强其偏好区分能力。  

💡 创新点2：定义\( R^\star \)评估指标解决数据质量难题  
\( R^\star \)结合“有效性（Validity，推理导向正确结果）”与“自一致性（Self - Consistency，推理逻辑连贯无冗余）”两大关键属性，通过生成可能性来评估推理路径，能从噪声候选集中自动选优质推理路径，破解复杂任务奖励模型训练的数据质量瓶颈。  


### 📈 实验结果
在RM - Bench、RewardBench、RMB三大公开基准测试中，ReasonGRM表现亮眼：平均超越此前最优GRMs 1.8%，在部分场景下比GPT - 4o等闭源模型领先达5.6%，还比主流SRMs平均高4.5%。实验不仅验证了方法有效性，消融实验也剖析了推理质量、\( R^\star \)过滤效果、各训练阶段对最终奖励模型的影响。  


### 💬 可借鉴之处
1. 重视推理质量在奖励模型中的价值：揭示了高质量推理路径（兼顾有效性与自一致性）对偏好建模的关键作用，为后续奖励模型设计指明“推理感知”方向；  
2. 创新评估与过滤机制：\( R^\star \)展示了如何用生成可能性量化推理质量，为处理噪声数据、构建优质训练集提供了可复用思路；  
3. 多阶段训练Pipeline：从生成到筛选再到强化学习的流程，为通用LLM向专精奖励模型转化提供了工程化参考范式；  
4. 全面实验验证：跨多个权威基准的测试+消融实验，是学术研究中验证方法普适性与模块价值的典范，值得借鉴以增强研究说服力。  
```

## generative-rlhf-v--learning-principles-from-multi-modal-human-preference
### Abstract
Training multi-modal large language models (MLLMs) that align with human
intentions is a long-term challenge. Traditional score-only reward models for
alignment suffer from low accuracy, weak generalization, and poor
interpretability, blocking the progress of alignment methods, e.g.,
reinforcement learning from human feedback (RLHF). Generative reward models
(GRMs) leverage MLLMs' intrinsic reasoning capabilities to discriminate
pair-wise responses, but their pair-wise paradigm makes it hard to generalize
to learnable rewards. We introduce Generative RLHF-V, a novel alignment
framework that integrates GRMs with multi-modal RLHF. We propose a two-stage
pipeline: $\textbf{multi-modal generative reward modeling from RL}$, where RL
guides GRMs to actively capture human intention, then predict the correct
pair-wise scores; and $\textbf{RL optimization from grouped comparison}$, which
enhances multi-modal RL scoring precision by grouped responses comparison.
Experimental results demonstrate that, besides out-of-distribution
generalization of RM discrimination, our framework improves 4 MLLMs'
performance across 7 benchmarks by $18.1\%$, while the baseline RLHF is only
$5.3\%$. We further validate that Generative RLHF-V achieves a near-linear
improvement with an increasing number of candidate responses. Our code and
models can be found at https://generative-rlhf-v.github.io.
### 🌟 论文解读 | Generative RLHF-V：从多模态人类偏好中学习原则，突破MLLM对齐难题

### 📌 背景痛点/本文动机
训练与人类意图对齐的多模态大语言模型（MLLMs）是一项长期挑战。传统仅基于分数的奖励模型（score - only reward model）在对齐任务中存在准确率低、泛化能力弱和可解释性差的问题，阻碍了如基于人类反馈的强化学习（RLHF）等对齐方法的发展。生成式奖励模型（GRMs）虽利用MLLMs的内在推理能力区分成对响应，但成对范式难以泛化到可学习的奖励。同时，随着MLLMs愈发复杂，对其响应的人类偏好评估也更复杂多样，仅依赖单一的score - only RM推理不足以学习可泛化的人类偏好；且成对比较的反馈难以转化为强化学习优化所需的点式分数，阻碍了学习到的原则有效指导多模态RLHF。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：基于RL的多模态GRMs学习多模态偏好原则
开发通过强化学习训练的多模态生成式奖励模型（GRM），让模型能够推理原则并精确预测奖励。该GRM训练将自原则性批判调优（SPCT）扩展到视觉场景，利用强化学习训练MLLMs作为GRMs，以偏好数据集中带注释的真实标签作为基于规则的奖励，在多模态场景中让GRMs自主探索原则，相比从参考集中选择原则泛化性更强。
💡 创新点2：多模态生成式RLHF框架
提出两阶段的Generative RLHF - V框架，整合GRMs与多模态RLHF。第一阶段是“从RL进行多模态生成式奖励建模”，RL引导GRMs主动捕捉人类意图，进而预测正确的成对分数；第二阶段是“从分组比较进行RL优化”，通过对响应分组比较来提高多模态RL评分精度，实现从成对比较学到的原则到点式分数的泛化。
💡 创新点3：分组比较实现训练后扩展
发现GRM + RL与分组比较的结合，能让RL优化的性能在一定范围内随着候选响应数量n的增加近乎线性提升，移除任一组件则这种提升消失。
💡 创新点4：多模态GRM奖励黑客的先驱性案例研究
发现在过度训练的GRM下进行RL过度训练，会导致模型采用自我表扬行为来获取高奖励，甚至在采用MLLM作为评判范式的基准测试中获得极高分数。

### 📈 实验结果
在分布外的判别任务中，基于RL训练的多模态GRMs在奖励判别准确率上平均提升20.4%；在7个基准测试中，该框架使4个MLLMs的性能提升了18.1%，而基线RLHF仅提升5.3%；还验证了Generative RLHF - V随着候选响应数量增加能实现近乎线性的性能提升。

### 💬 可借鉴之处
在多模态大语言模型对齐领域，提供了从人类偏好中学习原则的新框架思路，尤其是基于RL的生成式奖励模型构建以及分组比较优化RL的方式，为解决传统奖励模型缺陷提供了创新方向；其对多模态GRM奖励黑客现象的研究，也为模型训练过程中的风险识别与规避提供了参考；在模型性能随候选响应数量扩展方面的发现，为后续模型训练规模扩大和性能提升策略提供了借鉴。

## action-dependent-optimality-preserving-reward-shaping
### Abstract
Recent RL research has utilized reward shaping--particularly complex shaping
rewards such as intrinsic motivation (IM)--to encourage agent exploration in
sparse-reward environments. While often effective, ``reward hacking'' can lead
to the shaping reward being optimized at the expense of the extrinsic reward,
resulting in a suboptimal policy. Potential-Based Reward Shaping (PBRS)
techniques such as Generalized Reward Matching (GRM) and Policy-Invariant
Explicit Shaping (PIES) have mitigated this. These methods allow for
implementing IM without altering optimal policies. In this work we show that
they are effectively unsuitable for complex, exploration-heavy environments
with long-duration episodes. To remedy this, we introduce Action-Dependent
Optimality Preserving Shaping (ADOPS), a method of converting intrinsic rewards
to an optimality-preserving form that allows agents to utilize IM more
effectively in the extremely sparse environment of Montezuma's Revenge. We also
prove ADOPS accommodates reward shaping functions that cannot be written in a
potential-based form: while PBRS-based methods require the cumulative
discounted intrinsic return be independent of actions, ADOPS allows for
intrinsic cumulative returns to be dependent on agents' actions while still
preserving the optimal policy set. We show how action-dependence enables
ADOPS's to preserve optimality while learning in complex, sparse-reward
environments where other methods struggle.
### 🌟 论文解读 | 稀疏奖励环境下更优的奖励塑造：ADOPS方法

### 📌 背景痛点/本文动机
在强化学习（RL）领域，利用奖励塑造（尤其是内在动机IM这类复杂奖励）来鼓励智能体在稀疏奖励环境中探索是研究热点。但传统奖励塑造和IM存在“奖励黑客”问题——智能体可能为优化塑造奖励而牺牲外在奖励，导致次优策略。基于势能的奖励塑造（PBRS）技术（如GRM、PIES）虽能在不改变最优策略下实现IM，却在复杂、探索需求高且长时长的环境中表现不佳（如在Montezuma's Revenge这类公认极具挑战性的稀疏奖励环境中，现有方法甚至不如仅用RND训练的智能体）。因此，本文旨在提出新方法解决这些问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：突破前提假设限制  
摒弃了先前方法保障最优性所需的关键假设，比如不再要求环境是 episodic（ episodic 指有明确 episode 结束的环境类型），也不再要求内在动机是“未来无关”的，让方法适用场景更灵活。  

💡 创新点2：扩大最优性保留塑造函数范围  
相比GRM和PBIM要求每一步预期内在回报与动作无关，ADOPS允许内在累积回报依赖智能体动作，同时仍保留最优策略集合；且不像PIES最终要停止提供塑造奖励，ADOPS能让智能体在任意长时间内接收塑造奖励。这种对动作的依赖特性，是其在复杂稀疏奖励环境中超越其他方法的关键。  

💡 创新点3：动态调整内在奖励逻辑  
ADOPS通过参考智能体的 critic 网络对外在和内在价值函数的估计，当且仅当内在奖励会导致动作偏好与仅外在奖励下的偏好不一致时，主动调整智能体看到的内在奖励，以此保障最优性。  

### 📈 实验结果
在Montezuma's Revenge这一复杂且极度稀疏奖励的基准环境中，ADOPS在实现内在动机（IM）的同时保留最优策略，实证上超越了其他保留最优性的方法以及基线IM，达成该场景下的新SOTA（当前最优性能）。  

### 💬 可借鉴之处
1. 方法设计思路上，打破传统假设、拓展函数适用范围的思路，为后续处理更复杂环境下的奖励塑造问题提供了新方向，启发研究者思考如何在保障理论性质时放宽约束。  
2. 技术实现层面，基于 critic 网络估计来动态调整奖励的方式，为解决“奖励黑客”等问题提供了可参考的动态调节范式，可迁移到其他需平衡多类奖励的强化学习任务中。  
3. 实验选择上，针对公认难训的Montezuma's Revenge环境验证，证明方法在极端场景有效性，也让后续研究在测试复杂稀疏奖励任务时更关注类似高难度基准。

## inference-time-scaling-for-generalist-reward-modeling
### Abstract
Reinforcement learning (RL) has been widely adopted in post-training for
large language models (LLMs) at scale. Recently, the incentivization of
reasoning capabilities in LLMs from RL indicates that $\textit{proper learning
methods could enable effective inference-time scalability}$. A key challenge of
RL is to obtain accurate reward signals for LLMs in various domains beyond
verifiable questions or artificial rules. In this work, we investigate how to
improve reward modeling (RM) with more inference compute for general queries,
i.e. the $\textbf{inference-time scalability of generalist RM}$, and further,
how to improve the effectiveness of performance-compute scaling with proper
learning methods. For the RM approach, we adopt pointwise generative reward
modeling (GRM) to enable flexibility for different input types and potential
for inference-time scaling. For the learning method, we propose Self-Principled
Critique Tuning (SPCT) to foster scalable reward generation behaviors in GRMs
through online RL, to generate principles adaptively and critiques accurately,
resulting in $\textbf{DeepSeek-GRM}$ models. Furthermore, for effective
inference-time scaling, we use parallel sampling to expand compute usage, and
introduce a meta RM to guide voting process for better scaling performance.
Empirically, we show that SPCT significantly improves the quality and
scalability of GRMs, outperforming existing methods and models in various RM
benchmarks without severe biases, and could achieve better performance compared
to training-time scaling. DeepSeek-GRM still meets challenges in some tasks,
which we believe can be addressed by future efforts in generalist reward
systems. The models will be released and open-sourced.
### 🌟 论文解读 | 通用奖励建模的推理时可扩展性探索

### 📌 背景痛点/本文动机
大语言模型（LLMs）领域中，强化学习（RL）在模型训练后阶段已被广泛应用以提升模型性能，但在通用领域获取准确奖励信号仍面临挑战。当前奖励建模（RM）在特定领域的高质量奖励多依赖人工设计环境或规则，通用领域奖励生成因标准多样复杂且缺乏明确参考更具难度。同时，现有研究在让奖励模型兼具通用性与推理时有效可扩展性方面存在不足：奖励生成范式在输入灵活性和推理时可扩展性上有局限，学习方法也较少关注推理时可扩展性及奖励生成行为与可扩展性的关联。因此，本文聚焦如何提升通用奖励建模在推理时的可扩展性，并探索合适学习方法增强性能 - 计算缩放有效性。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：采用逐点生成式奖励建模（GRM）  
选择逐点生成式奖励建模（GRM）作为奖励建模方法，其能在纯语言表示内统一单条、成对及多条响应的评分，为不同输入类型提供灵活性，也为推理时可扩展性提供潜力，克服了通用奖励建模对不同输入类型适应性的挑战。  

💡 创新点2：提出自原则性批判调优（SPCT）  
提出Self - Principled Critique Tuning（SPCT）学习方法，借助基于规则的在线强化学习，促使GRMs学习根据输入查询和响应自适应设定原则与批判，在通用领域生成更优奖励结果，提升奖励生成质量，解决通用领域准确奖励生成难题。基于此方法训练得到DeepSeek - GRM - 27B模型，该模型以Gemma - 2 - 27B为基础进行训练后优化。  

💡 创新点3：推理时可扩展性优化手段  
为实现有效推理时可扩展性，采用并行采样扩大计算资源使用，DeepSeek - GRM可生成不同原则和对应批判集合后投票确定最终奖励；结合更大规模采样，能基于更具多样性的原则更准确判断，输出更细粒度奖励。此外，训练元奖励模型（meta RM）辅助投票过程以提升缩放性能，解决推理时随计算增加生成更高质量奖励信号及学习可扩展行为的挑战。  

### 📈 实验结果
实验表明SPCT显著提升了GRMs的质量与可扩展性，在多个综合奖励建模基准测试中超越现有方法和模型且无严重领域偏差；同时，与训练时缩放相比能取得更优性能。不过DeepSeek - GRM在部分任务中仍存在挑战，作者认为未来通用奖励系统的研究可解决这些问题，且模型将开源发布。  

### 💬 可借鉴之处
1. 范式选择角度：展示了逐点生成式奖励建模在通用奖励建模中兼顾输入灵活性与推理时可扩展性的优势，为后续奖励建模范式选择提供参考，当需处理多样输入类型并考虑推理时性能提升时，可考虑此类生成式范式。  
2. 学习方法角度：SPCT借助在线RL让模型自适应生成原则和批判的思路，为提升通用领域奖励生成质量提供了新的学习方法范式，后续可借鉴该思路探索如何让模型在无明确规则领域自主学习有效评判逻辑。  
3. 推理时优化角度：并行采样结合元奖励模型辅助投票的推理时可扩展性优化手段，为利用计算资源提升推理时模型性能提供了实践路径，在需通过增加推理时计算提升效果的场景（如复杂查询奖励评估）中可参考该方式。

