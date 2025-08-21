# Paper List from BIB File: tmpgeucql8d.bib
- [25/01] **rStar-Math: Small LLMs Can Master Math Reasoning with Self-Evolved Deep Thinking**  
[[Paper](http://arxiv.org/pdf/2501.04519v1)] [[Code/Page](https://github.com/microsoft/rStar.)] [[TLDR/Notes](#rstar-math--small-llms-can-master-math-reasoning-with-self-evolved-deep-thinking)]

- [23/04] **ImageReward: Learning and Evaluating Human Preferences for Text-to-Image Generation**  
[[Paper](http://arxiv.org/pdf/2304.05977v4)] [[Code/Page](https://github.com/THUDM/ImageReward}.)] [[TLDR/Notes](#imagereward--learning-and-evaluating-human-preferences-for-text-to-image-generation)]

- [25/05] **R1-Reward: Training Multimodal Reward Model Through Stable Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.02835v2)] [[Code/Page]()] [[TLDR/Notes](#r1-reward--training-multimodal-reward-model-through-stable-reinforcement-learning)]

- [24/11] **Self-Generated Critiques Boost Reward Modeling for Language Models**  
[[Paper](http://arxiv.org/pdf/2411.16646v3)] [[Code/Page]()] [[TLDR/Notes](#self-generated-critiques-boost-reward-modeling-for-language-models)]

- [23/04] **RAFT: Reward rAnked FineTuning for Generative Foundation Model Alignment**  
[[Paper](http://arxiv.org/pdf/2304.06767v4)] [[Code/Page]()] [[TLDR/Notes](#raft--reward-ranked-finetuning-for-generative-foundation-model-alignment)]

- [24/08] **Generative Verifiers: Reward Modeling as Next-Token Prediction**  
[[Paper](http://arxiv.org/pdf/2408.15240v3)] [[Code/Page]()] [[TLDR/Notes](#generative-verifiers--reward-modeling-as-next-token-prediction)]

- [25/01] **InternLM-XComposer2.5-Reward: A Simple Yet Effective Multi-Modal Reward Model**  
[[Paper](http://arxiv.org/pdf/2501.12368v2)] [[Code/Page](https://github.com/InternLM/InternLM-XComposer/tree/main/InternLM-XComposer-2.5-Reward)] [[TLDR/Notes](#internlm-xcomposer2-5-reward--a-simple-yet-effective-multi-modal-reward-model)]

- [24/01] **WARM: On the Benefits of Weight Averaged Reward Models**  
[[Paper](http://arxiv.org/pdf/2401.12187v1)] [[Code/Page]()] [[TLDR/Notes](#warm--on-the-benefits-of-weight-averaged-reward-models)]

- [25/05] **Skywork-VL Reward: An Effective Reward Model for Multimodal Understanding and Reasoning**  
[[Paper](http://arxiv.org/pdf/2505.07263v2)] [[Code/Page]()] [[TLDR/Notes](#skywork-vl-reward--an-effective-reward-model-for-multimodal-understanding-and-reasoning)]

- [25/05] **RM-R1: Reward Modeling as Reasoning**  
[[Paper](http://arxiv.org/pdf/2505.02387v3)] [[Code/Page](https://github.com/RM-R1-UIUC/RM-R1.)] [[TLDR/Notes](#rm-r1--reward-modeling-as-reasoning)]

- [23/12] **Diffusion Reward: Learning Rewards via Conditional Video Diffusion**  
[[Paper](http://arxiv.org/pdf/2312.14134v3)] [[Code/Page](https://diffusion-reward.github.io.)] [[TLDR/Notes](#diffusion-reward--learning-rewards-via-conditional-video-diffusion)]

- [24/09] **RRM: Robust Reward Model Training Mitigates Reward Hacking**  
[[Paper](http://arxiv.org/pdf/2409.13156v2)] [[Code/Page]()] [[TLDR/Notes](#rrm--robust-reward-model-training-mitigates-reward-hacking)]

- [25/06] **RewardAnything: Generalizable Principle-Following Reward Models**  
[[Paper](http://arxiv.org/pdf/2506.03637v2)] [[Code/Page]()] [[TLDR/Notes](#rewardanything--generalizable-principle-following-reward-models)]

- [25/03] **VisualPRM: An Effective Process Reward Model for Multimodal Reasoning**  
[[Paper](http://arxiv.org/pdf/2503.10291v1)] [[Code/Page](https://internvl.github.io/blog/2025-03-13-VisualPRM/.)] [[TLDR/Notes](#visualprm--an-effective-process-reward-model-for-multimodal-reasoning)]

- [24/10] **Skywork-Reward: Bag of Tricks for Reward Modeling in LLMs**  
[[Paper](http://arxiv.org/pdf/2410.18451v1)] [[Code/Page]()] [[TLDR/Notes](#skywork-reward--bag-of-tricks-for-reward-modeling-in-llms)]

- [24/10] **On Designing Effective RL Reward at Training Time for LLM Reasoning**  
[[Paper](http://arxiv.org/pdf/2410.15115v3)] [[Code/Page]()] [[TLDR/Notes](#on-designing-effective-rl-reward-at-training-time-for-llm-reasoning)]

- [25/06] **GRAM: A Generative Foundation Reward Model for Reward Generalization**  
[[Paper](http://arxiv.org/pdf/2506.14175v2)] [[Code/Page]()] [[TLDR/Notes](#gram--a-generative-foundation-reward-model-for-reward-generalization)]

- [25/04] **Inference-Time Scaling for Generalist Reward Modeling**  
[[Paper](http://arxiv.org/pdf/2504.02495v2)] [[Code/Page]()] [[TLDR/Notes](#inference-time-scaling-for-generalist-reward-modeling)]

- [24/06] **ReST-MCTS*: LLM Self-Training via Process Reward Guided Tree Search**  
[[Paper](http://arxiv.org/pdf/2406.03816v3)] [[Code/Page](https://github.com/THUDM/ReST-MCTS.)] [[TLDR/Notes](#rest-mcts*--llm-self-training-via-process-reward-guided-tree-search)]

- [25/07] **Skywork-Reward-V2: Scaling Preference Data Curation via Human-AI Synergy**  
[[Paper](http://arxiv.org/pdf/2507.01352v2)] [[Code/Page]()] [[TLDR/Notes](#skywork-reward-v2--scaling-preference-data-curation-via-human-ai-synergy)]



# TLDR/Notes
## rstar-math--small-llms-can-master-math-reasoning-with-self-evolved-deep-thinking
### Abstract
We present rStar-Math to demonstrate that small language models (SLMs) can
rival or even surpass the math reasoning capability of OpenAI o1, without
distillation from superior models. rStar-Math achieves this by exercising "deep
thinking" through Monte Carlo Tree Search (MCTS), where a math policy SLM
performs test-time search guided by an SLM-based process reward model.
rStar-Math introduces three innovations to tackle the challenges in training
the two SLMs: (1) a novel code-augmented CoT data sythesis method, which
performs extensive MCTS rollouts to generate step-by-step verified reasoning
trajectories used to train the policy SLM; (2) a novel process reward model
training method that avoids na\"ive step-level score annotation, yielding a
more effective process preference model (PPM); (3) a self-evolution recipe in
which the policy SLM and PPM are built from scratch and iteratively evolved to
improve reasoning capabilities. Through 4 rounds of self-evolution with
millions of synthesized solutions for 747k math problems, rStar-Math boosts
SLMs' math reasoning to state-of-the-art levels. On the MATH benchmark, it
improves Qwen2.5-Math-7B from 58.8% to 90.0% and Phi3-mini-3.8B from 41.4% to
86.4%, surpassing o1-preview by +4.5% and +0.9%. On the USA Math Olympiad
(AIME), rStar-Math solves an average of 53.3% (8/15) of problems, ranking among
the top 20% the brightest high school math students. Code and data will be
available at https://github.com/microsoft/rStar.
```
### 🌟 论文解读 | 小模型也能玩转数学推理？rStar-Math 靠“深度思考”挑战大模型霸权

### 📌 背景痛点/本文动机
近年来大语言模型（LLMs）在数学推理任务上展现出潜力，但传统“一步出答案”的推理方式（类似人类“直觉式思考”System 1）容易出错。而“深度思考”（类似人类“审慎式思考”System 2）的范式虽被提出——让模型分步骤推理并由奖励模型评估，但面临两大核心难题：  
1. **优质数据稀缺**：高质量数学推理数据本身难获取，合成数据时又容易混入错误中间步骤；  
2. **奖励模型难训**：给每一步推理精准打分需要大量人工标注，自动标注又容易引入噪声，导致过程奖励模型（PRM）效果受限。  
此外，现有依赖大模型蒸馏的方法“后劲不足”，无法突破教师模型的能力上限。于是微软亚洲研究院团队提出 **rStar-Math**，探索让小语言模型（SLMs，如7B、3.8B量级）不靠大模型蒸馏，也能在数学推理上比肩甚至超越OpenAI o1等模型。

### 🚀 核心方法（介绍本文的几个创新点）
rStar-Math 围绕“自进化的深度思考”展开，用蒙特卡洛树搜索（MCTS）让小模型实现System 2式推理，并针对“策略模型（生成推理步骤）”和“过程奖励模型（评估步骤）”的训练难题，提出三大创新：  

💡 创新点1：代码增强的CoT数据合成法  
要训练能生成优质推理步骤的“策略SLM”，需大量带正确中间步骤的推理轨迹。rStar-Math 把数学解题拆解为MCTS内的多步生成：每一步让策略SLM生成候选推理节点（含一步CoT和对应Python代码），**只保留代码能成功执行的节点**（过滤中间错误）；同时，通过大规模MCTS rollouts，依据“步骤对最终正确解的贡献度”自动给中间步分配Q值——贡献大的步骤Q值高、质量高。这样就用MCTS自动合成了带自标注Q值的、步骤可靠的推理轨迹，供策略SLM训练。  

💡 创新点2：过程偏好模型（PPM）的训练新法  
过程奖励模型需要给每一步推理精准打分，但直接用Q值当分数噪声大、不精准。rStar-Math 换思路：既然Q值虽不完美，但能区分“正向步骤（正确/相关）”和“负向步骤（错误/无关）”，那就**基于Q值构建“步骤偏好对”**，用 pairwise ranking loss 训练PPM，让它学会预测步骤的奖励倾向。这种方法避免了直接拿Q值当标签的粗糙做法，让PPM更可靠。  

💡 创新点3：四轮自进化流程  
从74.7万道数学题的公开数据集起步，rStar-Math 让“策略SLM”和“PPM”从0开始、迭代进化：每一轮用当前最新的策略模型和PPM做MCTS，用前两个创新点生成更高质量的数据，再训练下一轮更强的策略模型和PPM。每一轮都实现“更强的策略模型→更可靠的PPM→用PPM增强的MCTS生成更好轨迹→覆盖更难数学题”的正向循环。  


### 📈 实验结果
在多个数学推理基准测试中，rStar-Math 展现了小模型“深度思考”的潜力：  
- **MATH基准**：用64条推理轨迹时，Qwen2.5-Math-7B从58.8%提升到90.0%，Phi3-mini-3.8B从41.4%提升到86.4%，**超过OpenAI o1-preview（85.5%）**；  
- **美国数学奥赛（AIME 2024）**：平均解出53.3%（8/15）的题目，超过o1-preview（44.6%），成绩能排进全美最优秀高中生的前20%；  
- 在其他如Olympiad Bench、College Math等任务中，也普遍超越或追平OpenAI o1系列，且所有实验均基于“小模型（≤7B）”完成，证明了不依赖大模型蒸馏也能突破上限。  


### 💬 可借鉴之处
1. **小模型的“深度思考”范式**：用MCTS模拟人类分步推理+评估的过程，证明小模型也能通过“测试时搜索”实现强推理，不必依赖模型参数规模；  
2. **自监督的数据合成**：用MCTS自动生成带验证（代码执行）和自标注（Q值）的推理轨迹，解决优质数据稀缺问题，为小模型训练提供新思路；  
3. **过程奖励模型的轻量化训练**：用“偏好对+pairwise loss”替代直接打分，降低对精准标注的依赖，让奖励模型更易训练；  
4. **自进化迭代思路**：从0开始迭代优化策略模型和奖励模型，靠数据和模型的“双向增强”实现能力跃迁，这种闭环进化思路可迁移到其他需要分步推理的任务（如代码生成、逻辑推理）。  

总之，rStar-Math 撕开了“只有大模型能做复杂推理”的固有认知，为小模型的能力突破提供了一套完整的“深度思考+自进化”方法论，未来在教育、竞赛辅助等场景也有潜在应用空间~
```

## imagereward--learning-and-evaluating-human-preferences-for-text-to-image-generation
### Abstract
We present a comprehensive solution to learn and improve text-to-image models
from human preference feedback. To begin with, we build ImageReward -- the
first general-purpose text-to-image human preference reward model -- to
effectively encode human preferences. Its training is based on our systematic
annotation pipeline including rating and ranking, which collects 137k expert
comparisons to date. In human evaluation, ImageReward outperforms existing
scoring models and metrics, making it a promising automatic metric for
evaluating text-to-image synthesis. On top of it, we propose Reward Feedback
Learning (ReFL), a direct tuning algorithm to optimize diffusion models against
a scorer. Both automatic and human evaluation support ReFL's advantages over
compared methods. All code and datasets are provided at
\url{https://github.com/THUDM/ImageReward}.
```
### 🌟 论文解读 | ImageReward：让文本到图像模型更懂人类偏好

### 📌 背景痛点/本文动机
近年来，文本到图像生成模型（如自回归和基于扩散的方法）发展迅猛，能依据文本描述生成高保真、语义相关的图像。但现有模型仍存在诸多问题，比如文本 - 图像对齐不佳（无法准确呈现文本中对象的数量、属性等）、人体部位畸形、不符合人类审美偏好、存在毒性和偏见等。这些问题难以仅通过改进模型架构和预训练数据解决。在自然语言处理领域，从人类反馈中强化学习（RLHF）能引导大语言模型贴合人类偏好，受此启发，文本到图像生成领域也需要类似方法来学习人类偏好，于是本文提出相关解决方案。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建ImageReward模型
构建了首个通用的文本到图像人类偏好奖励模型ImageReward。其训练基于系统的标注流程，包括评级和排序。该流程先从DiffusionDB选取多样的真实用户提示词，收集候选图像对；然后设计包含提示词标注、文本 - 图像评级、图像排序的标注阶段，让标注员按对齐度、保真度、无害性等对图像评级并排序；最终收集到137k的专家比较数据用于训练，有效编码人类偏好。
💡 创新点2：提出Reward Feedback Learning（ReFL）算法
提出ReFL直接调优扩散模型。基于ImageReward在扩散模型后期去噪步骤对图像质量的可识别性，利用ImageReward的反馈在随机的后期去噪步骤直接优化扩散模型，解决了扩散模型生成无似然性难以直接优化的问题。

### 📈 实验结果
在人类评估中，ImageReward在理解文本到图像合成中的人类偏好方面，超越了现有评分模型和指标（如比CLIP高38.6%、比Aesthetic高39.6%、比BLIP高31.6%），能显著缓解文本 - 图像生成中的诸多问题；作为自动评估指标，与FID和CLIP分数相比，在真实用户提示和MS - COCO 2014数据上，ImageReward与人类偏好排名更一致，模型和样本间区分度更高。对于ReFL，自动和人类评估都证明其比数据增强、损失重加权等现有方法更具优势。

### 💬 可借鉴之处
1. 数据标注流程设计：本文系统地识别文本到图像人类偏好标注的挑战，设计针对性标注流程，包括确定量化评估标准、训练标注员、优化标注体验和质量验证等，为领域内收集人类偏好数据提供了可参考的完整流程范式。
2. 奖励模型与生成模型结合：将人类偏好编码到奖励模型（ImageReward），再基于奖励模型优化生成模型（ReFL）的思路，为其他生成类任务（如音频生成、视频生成等）提供了从人类反馈中学习优化的参考框架。
3. 自动评估指标探索：ImageReward作为有前景的自动评估指标，其构建和验证过程为文本到图像领域打造更贴合人类感知的自动评估工具提供了经验，也启发在其他生成任务中思考如何构建有效自动评估指标。
```

## r1-reward--training-multimodal-reward-model-through-stable-reinforcement-learning
### Abstract
Multimodal Reward Models (MRMs) play a crucial role in enhancing the
performance of Multimodal Large Language Models (MLLMs). While recent
advancements have primarily focused on improving the model structure and
training data of MRMs, there has been limited exploration into the
effectiveness of long-term reasoning capabilities for reward modeling and how
to activate these capabilities in MRMs. In this paper, we explore how
Reinforcement Learning (RL) can be used to improve reward modeling.
Specifically, we reformulate the reward modeling problem as a rule-based RL
task. However, we observe that directly applying existing RL algorithms, such
as Reinforce++, to reward modeling often leads to training instability or even
collapse due to the inherent limitations of these algorithms. To address this
issue, we propose the StableReinforce algorithm, which refines the training
loss, advantage estimation strategy, and reward design of existing RL methods.
These refinements result in more stable training dynamics and superior
performance. To facilitate MRM training, we collect 200K preference data from
diverse datasets. Our reward model, R1-Reward, trained using the
StableReinforce algorithm on this dataset, significantly improves performance
on multimodal reward modeling benchmarks. Compared to previous SOTA models,
R1-Reward achieves a $8.4\%$ improvement on the VL Reward-Bench and a $14.3\%$
improvement on the Multimodal Reward Bench. Moreover, with more inference
compute, R1-Reward's performance is further enhanced, highlighting the
potential of RL algorithms in optimizing MRMs.
```
### 🌟 论文解读 | 用稳定强化学习训练多模态奖励模型：R1 - Reward 的创新之路

### 📌 背景痛点/本文动机
多模态奖励模型（MRMs）在提升多模态大语言模型（MLLMs）性能方面至关重要。然而，当前对 MRMs 的研究多集中在模型结构和训练数据上，对利用长期推理能力改进奖励建模以及如何激活该能力探索不足。同时，将现有强化学习（RL）算法直接应用于奖励建模时，常因算法固有局限导致训练不稳定甚至崩溃。因此，本文探索如何用 RL 改进奖励建模，解决现有 RL 算法在奖励建模中存在的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出 StableReinforce 算法
将奖励建模问题转化为基于规则的 RL 任务后，针对现有 RL 算法（如 Reinforce++）在奖励建模中训练不稳定的问题，StableReinforce 从训练损失、优势估计策略和奖励设计三方面改进。改进剪辑操作以减轻大更新导致的数值不稳定性；引入鲁棒的优势归一化技术，限制异常值影响；在奖励函数设计上，引入 MLLM 作为裁判，评估模型推理过程与最终结果的一致性，确保推理和输出对齐，促进更准确且逻辑连贯的决策。

💡 创新点2：渐进难度训练策略与数据收集
为助力 MRM 训练，收集来自不同数据集的 20 万偏好数据。训练时采用渐进难度策略：先用 GPT - 4o 生成对应思考过程作为冷启动 SFT 数据，记录 GPT - 4o 推断出与真实结果匹配结论所需采样尝试次数作为样本难度；强化学习阶段选取 GPT - 4o 至少两次采样才得到正确答案或三次尝试都失败的样本训练模型，提升训练效果。

### 📈 实验结果
R1 - Reward（用 StableReinforce 训练的奖励模型）在多模态奖励建模基准测试中表现优异。在 VL Reward - Bench 上比之前的 SOTA 模型提升 8.4%，在 Multimodal Reward Bench 上提升 14.3%；在 MM - RLHF Reward Bench、VL Reward - Bench 和 Multimodal Reward Bench 上分别比 SOTA 提升 3.5%、13.5% 和 14.6%。且推理时通过多次采样（如 Voting@5/15 策略）性能显著提升，更多推理计算能进一步增强其性能，体现了 RL 算法优化 MRMs 的潜力。此外，StableReinforce 相比 Reinforce++，政策损失收敛更快更稳定，训练中能持续进行长度压缩提升效率，训练后平均响应长度比基础模型减少约 15%，推理 token 效率有望提升。

### 💬 可借鉴之处
1. 算法改进思路：当现有算法在特定任务（如奖励建模）中存在缺陷时，可从损失函数、优势估计、奖励设计等多方面针对性改进，提升训练稳定性与性能。
2. 数据与训练策略：收集大规模多样本数据，并采用渐进难度训练策略，根据数据难度分层训练，为模型训练提供更合理的训练路径。
3. 多模态任务中 RL 的应用：展示了 RL 在多模态奖励建模任务中的潜力，为多模态领域结合 RL 技术提供了实践参考，后续可探索 RL 在更多多模态子任务中的应用与改进。
```

## self-generated-critiques-boost-reward-modeling-for-language-models
### Abstract
Reward modeling is crucial for aligning large language models (LLMs) with
human preferences, especially in reinforcement learning from human feedback
(RLHF). However, current reward models mainly produce scalar scores and
struggle to incorporate critiques in a natural language format. We hypothesize
that predicting both critiques and the scalar reward would improve reward
modeling ability. Motivated by this, we propose Critic-RM, a framework that
improves reward models using self-generated critiques without extra
supervision. Critic-RM employs a two-stage process: generating and filtering
high-quality critiques, followed by joint fine-tuning on reward prediction and
critique generation. Experiments across benchmarks show that Critic-RM improves
reward modeling accuracy by 3.7%-7.3% compared to standard reward models and
LLM judges, demonstrating strong performance and data efficiency. Additional
studies further validate the effectiveness of generated critiques in rectifying
flawed reasoning steps with 2.5%-3.2% gains in improving reasoning accuracy.
```
### 🌟 论文解读 | 用自生成 critique 提升大模型奖励建模：Critic-RM 框架来袭

### 📌 背景痛点/本文动机
强化学习从人类反馈（RLHF）中，奖励模型（RM）是让大模型对齐人类偏好的核心环节。但现有奖励模型存在两大局限：一是输出“难以解释”的标量分数，没充分利用大模型本身的语言建模能力，导致数据效率低、易出现“奖励黑客”等鲁棒性问题；二是很难自然地融入“自然语言形式的 critique（ critique 可理解为对模型输出的分析、点评）”。而“LLM 作评委（LLM-as-a-judge）”范式虽能生成 critique 但又缺乏标量优化的优势。若能结合二者，把 critique 的可解释性和标量优化框架结合，有望打造更鲁棒有效的奖励信号。但难点在于：**目标冲突**（生成 critique 是语言建模，奖励模型是标量输出，整合困难）和**评估器局限**（现成大模型当评委不够好，人工标注 critique 成本高）。于是，论文提出 Critic-RM 框架，试图用“自生成 critique”来增强奖励模型，且不依赖更强的外部教师模型。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：自生成+筛选高质量 critique  
Critic-RM 以“指令微调后的大模型”为基础，先让模型为单个响应生成多个候选 critique，每个 critique 还会附带一个离散分数（仅用于筛选，非最终奖励）。为解决 critique 质量参差不齐的问题，先用**一致性引导过滤**：只保留那些离散分数和人类标注偏好标签一致的 critique。此外还加了“总结”和“排序”策略进一步提纯 critique 质量，确保用于训练奖励模型的 critique 足够优质。  

💡 创新点2：双任务联合微调+权重平衡策略  
拿到高质量 critique 后，要同时训练“生成 critique”和“预测标量奖励”两个任务。但奖励建模易过拟合，而大模型从多样 critique 学习又需要丰富性，二者存在矛盾。为此设计**权重平衡策略**：训练初期侧重“critique 建模损失”，之后逐渐过渡到结合“响应+ critique”来预测奖励。平衡两个学习目标，让模型在生成高质量 critique 和精准预测奖励上都表现出色。  

💡 创新点3：不依赖强外部教师模型的自提升范式  
以往类似工作依赖更强的教师 LLM 生成 critique，成本高且难规模化，甚至没更强教师时无法用。Critic-RM 借鉴“自改进语言模型”思路，让模型用自己生成的数据迭代优化，不依赖额外强监督，在提升奖励建模能力同时还能保证生成质量。  


### 📈 实验结果
1. 奖励建模精度提升：在 RewardBench 等偏好排序基准测试中，Critic-RM 比标准奖励模型、LLM 评委等基线方法，奖励建模准确率提升 3.7% - 7.3%，体现了强性能与数据效率。  
2. 推理纠错能力验证：在额外研究中，生成的 critique 能有效修正大模型有缺陷的推理步骤，推理准确率提升 2.5% - 3.2%，验证了 critique 对模型推理纠错的价值。  


### 💬 可借鉴之处
1. 自生成+自筛选的“闭环”思路：利用模型自身生成数据并筛选，摆脱对外部强教师或大量人工标注的依赖，为资源有限场景下的模型优化提供思路。  
2. 多任务联合训练的权重调度：面对“语言生成+标量预测”这类多目标学习矛盾时，用分阶段权重调整平衡目标，这种“动态侧重”的训练策略值得借鉴到其他多任务场景。  
3. 把“可解释性 critique”和“标量奖励”结合：让奖励模型既有数值优化的优势，又有语言层面的可解释性，为后续 RLHF 中更透明、鲁棒的反馈信号设计提供了新范式。  
```

## raft--reward-ranked-finetuning-for-generative-foundation-model-alignment
### Abstract
Generative foundation models are susceptible to implicit biases that can
arise from extensive unsupervised training data. Such biases can produce
suboptimal samples, skewed outcomes, and unfairness, with potentially serious
consequences. Consequently, aligning these models with human ethics and
preferences is an essential step toward ensuring their responsible and
effective deployment in real-world applications. Prior research has primarily
employed Reinforcement Learning from Human Feedback (RLHF) to address this
problem, where generative models are fine-tuned with RL algorithms guided by a
human-feedback-informed reward model. However, the inefficiencies and
instabilities associated with RL algorithms frequently present substantial
obstacles to the successful alignment, necessitating the development of a more
robust and streamlined approach. To this end, we introduce a new framework,
Reward rAnked FineTuning (RAFT), designed to align generative models
effectively. Utilizing a reward model and a sufficient number of samples, our
approach selects the high-quality samples, discarding those that exhibit
undesired behavior, and subsequently enhancing the model by fine-tuning on
these filtered samples. Our studies show that RAFT can effectively improve the
model performance in both reward learning and other automated metrics in both
large language models and diffusion models.
```
### 🌟 论文解读 | RAFT：革新生成式基础模型校准的奖励排序微调框架

### 📌 背景痛点/本文动机
生成式基础模型在大量无监督训练数据的作用下，易受到隐含偏差的影响。这些偏差可能导致生成的样本并非最优、结果出现偏差以及产生不公平现象，甚至带来严重后果。因此，使这些模型符合人类伦理和偏好，是确保其在现实应用中得以负责且有效部署的关键一步。先前的研究主要采用基于人类反馈的强化学习（RLHF）来解决这一问题，即通过由人类反馈提供信息的奖励模型引导强化学习算法对生成模型进行微调。然而，强化学习算法存在效率低下和不稳定的问题，常常给模型的成功校准带来重大阻碍，故而需要开发一种更强大且高效的方法。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出全新框架
引入了奖励排序微调（Reward rAnked FineTuning，RAFT）这一全新框架，旨在有效校准生成模型。

💡 创新点2：样本筛选与微调机制
利用奖励模型和足够数量的样本，该方法能够挑选出高质量样本，摒弃表现出不良行为的样本，然后通过对这些经过筛选的样本进行微调来提升模型性能。

### 📈 实验结果
研究表明，RAFT在大型语言模型和扩散模型中，无论是在奖励学习方面，还是在其他自动化指标上，都能有效提升模型性能。

### 💬 可借鉴之处
对于致力于解决生成式基础模型隐含偏差问题、提升模型校准效果的研究人员和从业者而言，RAFT提供了一种全新且有效的思路和方法。其样本筛选与微调的机制可作为一种参考范式，应用于不同类型的生成式模型中，以提高模型在符合人类伦理和偏好方面的表现，同时避免强化学习算法带来的效率和稳定性问题。
``` 

## generative-verifiers--reward-modeling-as-next-token-prediction
### Abstract
Verifiers or reward models are often used to enhance the reasoning
performance of large language models (LLMs). A common approach is the Best-of-N
method, where N candidate solutions generated by the LLM are ranked by a
verifier, and the best one is selected. While LLM-based verifiers are typically
trained as discriminative classifiers to score solutions, they do not utilize
the text generation capabilities of pretrained LLMs. To overcome this
limitation, we instead propose training verifiers using the ubiquitous
next-token prediction objective, jointly on verification and solution
generation. Compared to standard verifiers, such generative verifiers (GenRM)
can benefit from several advantages of LLMs: they integrate seamlessly with
instruction tuning, enable chain-of-thought reasoning, and can utilize
additional test-time compute via majority voting for better verification. We
demonstrate that GenRM outperforms discriminative, DPO verifiers, and
LLM-as-a-Judge, resulting in large performance gains with Best-of-N, namely 5%
$\rightarrow$ 45.3% on algorithmic tasks and 73% $\rightarrow$ 93.4% on GSM8K.
In easy-to-hard generalization settings, we observe improvements of 28%
$\rightarrow$ 44.6% on MATH, and 37.9% $\rightarrow$ 53.5% on MMLU abstract
algebra. Furthermore, we find that training GenRM with synthetic verification
rationales is sufficient to pick out subtle errors on math problems. Finally,
we demonstrate that GenRM scales favorably with model size and test-time
compute.
```
### 🌟 论文解读 | 生成式验证器：把奖励建模变成下一个词预测，让大模型推理更聪明

### 📌 背景痛点/本文动机
大语言模型（LLMs）虽然能力很强，但推理时经常犯逻辑或事实错误，一个小错误就可能让整个解决方案失效。为了解决这问题，常用的方法是 “Best - of - N”：让LLM生成N个候选答案，再用“验证器（verifier）” 给这些答案排序选最优。但传统基于LLM的验证器是判别式分类器，只给答案打分，没用到LLM本身的文本生成能力，浪费了大模型在指令微调、思维链推理等方面的优势。所以，这篇论文想换个思路，让验证器也能利用LLM的生成能力。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：生成式验证器（GenRM），用“下一个词预测”训练验证器
以往验证器是判别式的，现在改成让验证器用“下一个词预测”的目标来训练。比如给个提示“答案正确吗？（Yes/No）”，验证器输出的分数就是生成“Yes”或“No”这个词的概率。这样就把验证任务变成了大模型擅长的文本生成任务，能自然利用LLM的生成能力。
💡 创新点2：GenRM - CoT，结合思维链推理+多数投票提升验证精度
GenRM - CoT在验证时，先生成“验证思维链（CoT）”的理由，再预测“Yes/No”。训练时如果有思维链的理由数据，模型就能显式地去推理答案对错。推理时还能采样多个思维链理由，用多数投票算“Yes”的平均概率，利用推理时的计算资源来提升验证效果。
💡 创新点3：统一“生成答案”和“验证答案”，借助生成能力正向迁移
GenRM用下一个词预测训练，能把“生成解决方案”和“验证解决方案”统一起来，这在之前的DPO验证器里很难做到，有可能通过生成任务的正向迁移来提升验证效果。

### 📈 实验结果
- 在算法任务（Last Letter Concat、BBH Word Sorting）上，Best - of - 32设置下，GenRM把解决率从5%提升到45.3%；在GSM8K数学题上，Best - of - 16下从73%提升到93.4%，超过了GPT - 4和Gemini 1.5 Pro。
- 从简单到难的泛化任务里，MATH500上Best - of - 32从28%提升到44.6%；MMLU抽象代数任务从37.9%提升到53.5%。
- 用合成的验证理由训练GenRM，能发现数学题里很细微的错误（比如GSM8K里忽略“each”这种细节错误，判别式RM没发现，GenRM - CoT能检测到）。
- 模型规模和推理时计算资源增加时，GenRM表现更优。比如推理时用多数投票增加计算，GenRM比LLM - as - a - Judge效果好；模型变大，GenRM也比判别式验证器 scaling 得更好。

### 💬 可借鉴之处
- 验证器设计新思路：别只把验证器当判别式分类器，要利用大模型的生成能力，用“下一个词预测”这种和预训练一致的目标来训练，能解锁很多大模型生成侧的优势（指令微调、思维链等）。
- 思维链+多数投票的验证增强：在验证环节加入思维链推理，还能在推理时用多数投票利用额外计算资源，这个思路可以迁移到其他需要精细验证、错误检测的任务里。
- 任务统一的潜力：把生成和验证任务用生成式目标统一起来，可能在更多“生成+评估”的场景里发挥作用，比如代码生成后验证、文案生成后审核等，借助生成的正向迁移提升评估效果。
```

## internlm-xcomposer2-5-reward--a-simple-yet-effective-multi-modal-reward-model
### Abstract
Despite the promising performance of Large Vision Language Models (LVLMs) in
visual understanding, they occasionally generate incorrect outputs. While
reward models (RMs) with reinforcement learning or test-time scaling offer the
potential for improving generation quality, a critical gap remains: publicly
available multi-modal RMs for LVLMs are scarce, and the implementation details
of proprietary models are often unclear. We bridge this gap with
InternLM-XComposer2.5-Reward (IXC-2.5-Reward), a simple yet effective
multi-modal reward model that aligns LVLMs with human preferences. To ensure
the robustness and versatility of IXC-2.5-Reward, we set up a high-quality
multi-modal preference corpus spanning text, image, and video inputs across
diverse domains, such as instruction following, general understanding,
text-rich documents, mathematical reasoning, and video understanding.
IXC-2.5-Reward achieves excellent results on the latest multi-modal reward
model benchmark and shows competitive performance on text-only reward model
benchmarks. We further demonstrate three key applications of IXC-2.5-Reward:
(1) Providing a supervisory signal for RL training. We integrate IXC-2.5-Reward
with Proximal Policy Optimization (PPO) yields IXC-2.5-Chat, which shows
consistent improvements in instruction following and multi-modal open-ended
dialogue; (2) Selecting the best response from candidate responses for
test-time scaling; and (3) Filtering outlier or noisy samples from existing
image and video instruction tuning training data. To ensure reproducibility and
facilitate further research, we have open-sourced all model weights and
training recipes at
https://github.com/InternLM/InternLM-XComposer/tree/main/InternLM-XComposer-2.5-Reward
### 🌟 论文解读 | InternLM-XComposer2.5-Reward：填补多模态奖励模型空白的高效方案

### 📌 背景痛点/本文动机
大视觉语言模型（LVLMs）在视觉理解方面表现出色，但偶尔也会生成错误输出。奖励模型（RMs）结合强化学习或测试时缩放虽有提升生成质量的潜力，然而公开可用的多模态奖励模型稀缺，且专有模型实现细节不明。针对此，论文提出InternLM - XComposer2.5 - Reward（IXC - 2.5 - Reward）来填补这一空白，让LVLMs与人类偏好对齐。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建高质量多模态偏好语料库
为确保IXC - 2.5 - Reward的鲁棒性和通用性，构建了涵盖文本、图像、视频输入，跨指令遵循、通用理解、文本丰富文档、数学推理、视频理解等多样领域的高质量多模态偏好语料库。该语料库构建 pipeline 会为不同模态输入选择多样领域的提示，生成对应响应，再用GPT - 4o或验证器做偏好判断。
💡 创新点2：设计简单有效的多模态奖励模型架构
不直接将单模态（文本）奖励模型迁移到视觉模态，而是在现有LVLM（InternLM - XComposer2.5）基础上增加一个评分头来预测奖励分数，使其能有效评估视觉（图像和视频）和文本输入。
💡 创新点3：展示奖励模型三大关键应用
一是为强化学习训练提供监督信号，将IXC - 2.5 - Reward与近端策略优化（PPO）结合得到IXC - 2.5 - Chat，提升指令遵循和多模态开放式对话能力；二是在测试时缩放中从候选响应里选最佳响应；三是从现有图像和视频指令调优训练数据中过滤异常或噪声样本。

### 📈 实验结果
IXC - 2.5 - Reward在最新多模态奖励模型基准VL - RewardBench上表现出色，取得70.0%的成绩，击败包括Gemini - 1.5 - Pro（62.5%）和GPT - 4o（62.4%）在内的之前所有生成式奖励模型；在纯文本奖励模型基准上也有竞争力，在Reward - Bench上平均得分88.6%，在RM - Bench上得分68.8%。同时，在RL训练、测试时缩放、数据清理三大应用场景的实验也验证了其有效性，如IXC - 2.5 - Chat在多模态指令遵循和野外聊天基准上有明显改进等。

### 💬 可借鉴之处
1. 多模态数据构建思路：论文构建跨模态、跨领域多模态偏好语料库的方式，为后续多模态模型训练数据构建提供了参考，强调了数据多样性和高质量标注的重要性。
2. 模型扩展与应用方向：从单模态奖励模型扩展到多模态的思路，以及展示的奖励模型在强化学习、测试时优化、数据清理等多场景应用，为奖励模型乃至大模型生态中不同模块的协作和功能拓展提供了范例。
3. 开源与可复现性：将模型权重和训练方案开源，利于社区基于此进一步研究，这种开源共享的做法也值得相关研究借鉴，推动领域发展。

## warm--on-the-benefits-of-weight-averaged-reward-models
### Abstract
Aligning large language models (LLMs) with human preferences through
reinforcement learning (RLHF) can lead to reward hacking, where LLMs exploit
failures in the reward model (RM) to achieve seemingly high rewards without
meeting the underlying objectives. We identify two primary challenges when
designing RMs to mitigate reward hacking: distribution shifts during the RL
process and inconsistencies in human preferences. As a solution, we propose
Weight Averaged Reward Models (WARM), first fine-tuning multiple RMs, then
averaging them in the weight space. This strategy follows the observation that
fine-tuned weights remain linearly mode connected when sharing the same
pre-training. By averaging weights, WARM improves efficiency compared to the
traditional ensembling of predictions, while improving reliability under
distribution shifts and robustness to preference inconsistencies. Our
experiments on summarization tasks, using best-of-N and RL methods, shows that
WARM improves the overall quality and alignment of LLM predictions; for
example, a policy RL fine-tuned with WARM has a 79.4% win rate against a policy
RL fine-tuned with a single RM.
```
### 🌟 论文解读 | WARM：权重平均奖励模型如何破解大模型奖励黑客难题？

### 📌 背景痛点/本文动机
在利用强化学习从人类反馈（RLHF）对齐大语言模型（LLM）的过程中，**奖励黑客（Reward Hacking）** 问题日益凸显：模型会利用奖励模型（RM）的漏洞，在未真正满足目标的情况下骗取高奖励。这背后存在两大核心挑战：一是强化学习过程中策略漂移引发的**分布偏移**（奖励模型要评估的生成分布和训练时差异变大）；二是人类偏好本身的**不一致性**（标注噪声、评判标准不统一等）。传统的预测集成（ENS）虽能一定程度缓解，但存在内存与推理开销大、对标注噪声鲁棒性不足等缺陷。因此，亟需更高效可靠的奖励模型设计方案。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出WARM（Weight Averaged Reward Models）框架  
从共享预训练的大模型出发，先对多个奖励模型做微调（比如用不同超参数、不同数据顺序等方式得到多样化RM），再在**权重空间**对这些RM做线性平均。这一思路源于“线性模式连通性（LMC）”发现：共享预训练的模型，微调后的权重可被线性插值连接。通过权重平均而非预测结果平均，WARM在推理时只需单个模型，大幅降低传统集成方法的内存与计算开销。  

💡 创新点2：兼顾可靠性与鲁棒性的三重优势  
- **效率**：推理仅需单模型，摆脱传统预测集成的冗余负担；  
- **分布偏移下的可靠性**：继承权重平均在分布外（OOD）泛化的优势，让奖励模型更稳地评估策略漂移后的生成；  
- **标注噪声鲁棒性**：权重平均能筛选不同训练中“不变的预测机制”，减少对错误标注样本的记忆（传统集成易直接记住噪声），进而提升RL过程稳定性。  


### 📈 实验结果
论文在**摘要任务**上验证WARM：  
- 对比传统单RM、预测集成（ENS）等方法，WARM在best-of-N和RL两类训练范式中，均提升了LLM生成的整体质量与对齐度。例如，用WARM微调的RL策略，对单RM微调的策略胜率达79.4%；  
- 消融实验显示，增加权重平均的RM数量（即M增大），能延缓“奖励黑客”导致的性能崩溃，让训练中奖励更持久地保持高位。  


### 💬 可借鉴之处
1. **权重平均的范式迁移**：将“权重平均提升泛化与鲁棒性”的思路从 supervised learning 拓展到RLHF的奖励建模，为解决分布偏移、标注噪声等难题提供新范式；  
2. **高效集成的实践路径**：证明“权重空间合并”比“预测结果合并”更轻量高效，在工业级大模型训练中，可降低多模型集成的推理成本；  
3. **鲁棒奖励模型的设计逻辑**：从“对抗奖励黑客”的角度，拆解分布偏移、偏好不一致两大痛点，并通过权重平均同时增强可靠性与鲁棒性，为后续奖励模型优化指明方向。  
```

## skywork-vl-reward--an-effective-reward-model-for-multimodal-understanding-and-reasoning
### Abstract
We propose Skywork-VL Reward, a multimodal reward model that provides reward
signals for both multimodal understanding and reasoning tasks. Our technical
approach comprises two key components: First, we construct a large-scale
multimodal preference dataset that covers a wide range of tasks and scenarios,
with responses collected from both standard vision-language models (VLMs) and
advanced VLM reasoners. Second, we design a reward model architecture based on
Qwen2.5-VL-7B-Instruct, integrating a reward head and applying multi-stage
fine-tuning using pairwise ranking loss on pairwise preference data.
Experimental evaluations show that Skywork-VL Reward achieves state-of-the-art
results on multimodal VL-RewardBench and exhibits competitive performance on
the text-only RewardBench benchmark. Furthermore, preference data constructed
based on our Skywork-VL Reward proves highly effective for training Mixed
Preference Optimization (MPO), leading to significant improvements in
multimodal reasoning capabilities. Our results underscore Skywork-VL Reward as
a significant advancement toward general-purpose, reliable reward models for
multimodal alignment. Our model has been publicly released to promote
transparency and reproducibility.
```
### 🌟 论文解读 | Skywork-VL Reward：多模态理解与推理的高效奖励模型

### 📌 背景痛点/本文动机
大语言模型（LLMs）和视觉-语言模型（VLMs）在众多任务中取得了显著进展，但让它们的行为与人类偏好对齐仍是一大挑战。奖励模型（RMs）是解决该问题的关键组件，然而针对纯文本LLMs的奖励模型研究较多，多模态奖励模型的发展还处于早期阶段。现有多模态奖励模型存在两大局限：缺乏跨多样任务的通用性，且难以有效评估具有复杂推理的先进VLM推理器。因此，迫切需要能在多样领域和任务中评估标准VLMs和先进VLM推理器输出的多模态奖励模型，这就是本文提出Skywork - VL Reward的动机。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建大规模多模态偏好数据集
整合多个开源偏好数据集（如LLaVA - Critic - 113k、Skywork - Reward - Preference - 80K - v0.2、RLAIF - V - Dataset）和内部标注来构建训练数据集。该数据集涵盖从基础图像描述到复杂推理场景的广泛任务，收集的偏好对包含图像（适用时）、文本提示和来自标准VLMs与先进VLM推理器的候选响应，为模型训练提供丰富多样的数据支撑。

💡 创新点2：设计基于Qwen2.5 - VL - 7B - Instruct的奖励模型架构与训练范式
基于Qwen2.5 - VL - 7B - Instruct设计奖励模型架构，集成奖励头，并在成对偏好数据上使用成对排序损失进行多阶段微调。采用结合纯文本和多模态数据的两阶段训练范式，增强模型在广泛多模态场景下的泛化性和性能，使模型能输出与人类偏好对齐的标量分数，有效评估VLM输出。

### 📈 实验结果
Skywork - VL Reward在多模态VL - RewardBench上取得了最先进的结果，在纯文本的RewardBench基准测试中也展现出有竞争力的性能。此外，基于Skywork - VL Reward构建的偏好数据在训练混合偏好优化（MPO）时被证明非常有效，能显著提升多模态推理能力，凸显了该模型在多模态对齐通用、可靠奖励模型方向上的重大进展。

### 💬 可借鉴之处
1. 数据集构建方面：通过整合多来源数据（开源+内部标注）来覆盖广泛任务和场景的思路，为后续多模态相关数据集构建提供了参考，能让模型学习到更全面的偏好信息。
2. 模型架构与训练方面：基于现有强基础模型（如Qwen2.5 - VL - 7B - Instruct）进行改进，添加奖励头并设计多阶段微调范式，这种利用已有资源并针对性改进以适配任务的方式值得借鉴，有助于提升模型在多模态理解和推理任务中的表现。
3. 应用拓展方面：展示了奖励模型生成的偏好数据在MPO训练中提升多模态推理能力的价值，为多模态模型后续的优化和能力提升提供了新的思路和方向，即利用优质奖励模型来辅助其他训练范式以增强模型性能。
```

## rm-r1--reward-modeling-as-reasoning
### Abstract
Reward modeling is essential for aligning large language models with human
preferences through reinforcement learning from human feedback. To provide
accurate reward signals, a reward model (RM) should stimulate deep thinking and
conduct interpretable reasoning before assigning a score or a judgment.
Inspired by recent advances of long chain-of-thought on reasoning-intensive
tasks, we hypothesize and validate that integrating reasoning capabilities into
reward modeling significantly enhances RMs interpretability and performance. To
this end, we introduce a new class of generative reward models - Reasoning
Reward Models (ReasRMs) - which formulate reward modeling as a reasoning task.
We propose a reasoning-oriented training pipeline and train a family of
ReasRMs, RM-R1. RM-R1 features a chain-of-rubrics (CoR) mechanism -
self-generating sample-level chat rubrics or math/code solutions, and
evaluating candidate responses against them. The training of RM-R1 consists of
two key stages: (1) distillation of high-quality reasoning chains and (2)
reinforcement learning with verifiable rewards. Empirically, our models achieve
state-of-the-art performance across three reward model benchmarks on average,
outperforming much larger open-weight models (e.g., INF-ORM-Llama3.1-70B) and
proprietary ones (e.g., GPT-4o) by up to 4.9%. Beyond final performance, we
perform thorough empirical analyses to understand the key ingredients of
successful ReasRM training. To facilitate future research, we release six
REASRM models along with code and data at https://github.com/RM-R1-UIUC/RM-R1.
```
### 🌟 论文解读 | RM-R1：将奖励建模重塑为推理任务，解锁奖励模型新范式

### 📌 背景痛点/本文动机
奖励模型（Reward Model，RM）在大语言模型（LLM）基于人类反馈的强化学习（RLHF）中扮演关键角色，是人类评估者的可扩展代理。现有奖励建模研究分为基于标量的奖励模型（ScalarRM）和生成式奖励模型（GenRM）两类。ScalarRM 把奖励建模当分类问题，虽直接有效但缺乏透明度，无中间推理步骤解释决策；GenRM 保留生成能力输出自由形式 pairwise 判断，却推理浅显，难应对复杂推理密集型偏好任务。现实中准确奖励建模需联合推理与奖励分配，因偏好判断涉及多认知考量（如推断潜在评估标准、权衡多标准、模拟后果等）。由此，本文核心问题是：能否将奖励建模转化为推理任务？

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出推理奖励模型（Reasoning Reward Models，ReasRMs）新类别  
将奖励建模构建为推理任务，强调在判断过程利用长且连贯的推理链，提升模型准确评估区分复杂输出的能力，区别于传统 GenRMs 推理浅显的问题，释放奖励模型推理潜力。  

💡 创新点2：设计面向推理的训练 pipeline 与 RM - R1 模型  
训练分两大关键阶段：一是高质量推理链蒸馏，用优质合成数据引导模型推理能力；二是带可验证奖励的强化学习（RLVR）。同时，RM - R1 具备 Chain - of - Rubrics（CoR）机制：针对输入样本分类为聊天或推理任务，聊天任务生成评估准则、理由与定制化评估；推理任务先自主解题再评估，让模型适配不同任务策略，生成更对齐有效的奖励信号。还探索从现有推理模型适配为奖励模型，对已做推理蒸馏的模型用 RLVR 微调。  

### 📈 实验结果
在 RewardBench、RM - Bench、RMB 三大奖励模型基准测试中，RM - R1 平均达当前最优性能，最多超过 70B、340B 等大开源模型及 GPT - 4o、Claude 等闭源模型 4.9%。此外，对 RM - R1 做了训练配方消融、缩放效应研究、与非推理基线对比、详细案例分析和训练动态等广泛实证分析，深入理解成功训练 ReasRM 的关键要素。  

### 💬 可借鉴之处
1. 理念层面：验证了推理能力对奖励模型的关键价值，为奖励建模开辟“推理优先”新视角，启发后续探索模型推理能力与奖励信号质量的关联。  
2. 方法层面：设计的两阶段训练 pipeline（推理链蒸馏 + RLVR）、CoR 任务感知推理机制，为打造高性能可解释奖励模型提供了模块化、可复现的技术路线。  
3. 开源层面：发布 6 个 ReasRM 模型及代码数据，降低领域研究门槛，利于社区基于此迭代创新，推动奖励建模与 RLHF 技术发展。  
```

## diffusion-reward--learning-rewards-via-conditional-video-diffusion
### Abstract
Learning rewards from expert videos offers an affordable and effective
solution to specify the intended behaviors for reinforcement learning (RL)
tasks. In this work, we propose Diffusion Reward, a novel framework that learns
rewards from expert videos via conditional video diffusion models for solving
complex visual RL problems. Our key insight is that lower generative diversity
is exhibited when conditioning diffusion on expert trajectories. Diffusion
Reward is accordingly formalized by the negative of conditional entropy that
encourages productive exploration of expert behaviors. We show the efficacy of
our method over robotic manipulation tasks in both simulation platforms and the
real world with visual input. Moreover, Diffusion Reward can even solve unseen
tasks successfully and effectively, largely surpassing baseline methods.
Project page and code: https://diffusion-reward.github.io.
```
### 🌟 论文解读 | 《Diffusion Reward：通过条件视频扩散学习奖励》：开启视觉强化学习新征程

### 📌 背景痛点/本文动机
在强化学习（RL）中，奖励设定是一项根本性挑战，它决定了智能体学习行为与预期目标的有效性和一致性。手动设计密集奖励函数既耗费人力，在某些情况下甚至不可行，比如在机器人操作这类现实任务中，获取特权状态信息十分困难。使用稀疏奖励虽在这些场景中因人工投入低而受到青睐，但它提供的监督不足，阻碍了RL的样本效率，可能给数据收集带来难以承受的负担。从专家视频中学习奖励函数是一种很有前景的解决方案，因为视频收集工作量小且包含密集的任务执行信息，但现有的一些方法存在对时间信息利用不足、对抗训练性能脆弱，以及在建模复杂专家视频分布时遇到困难等问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出Diffusion Reward框架，利用视频扩散模型捕捉专家视频分布并预训练密集奖励函数用于视觉RL。其关键见解是，基于类似专家轨迹的扩散比基于非专家轨迹的扩散具有更低的生成多样性，通过估计基于历史帧的条件熵来指导RL探索类似专家的行为。
💡 创新点2：将条件熵与寻求新奇奖励和备用环境奖励相结合，形成密集奖励以实现高效RL。此外，为加速奖励推断，利用矢量量化代码进行潜在扩散过程，以压缩高维观测。

### 📈 实验结果
通过在10个视觉机器人操作任务上的实验，验证了Diffusion Reward框架的有效性。这些任务包括MetaWorld的7个抓取操作任务和Adroit的3个灵巧操作任务，与表现最佳的基线方法相比，性能分别提高了38%和35%。同时，在未见任务上观察到了良好的零样本泛化性能，在真实机器人任务中产生的合理奖励以及相关的良好离线RL性能，也证明了Diffusion Reward在现实世界中的适用性。

### 💬 可借鉴之处
1. **奖励学习新思路**：利用视频扩散模型从专家视频中学习奖励，为解决强化学习中奖励设定难题提供了新的方向，可启发在其他复杂任务中的奖励学习研究。
2. **模型结合应用**：将视频扩散模型与强化学习相结合，展示了不同模型融合在解决实际问题时的潜力，为多模型联合应用提供了参考。
3. **零样本泛化能力**：在未见任务上表现出良好的零样本泛化性能，这对于应对现实中不断变化的任务需求具有重要意义，相关思路可用于提升模型在未知场景下的适应性。
``` 

## rrm--robust-reward-model-training-mitigates-reward-hacking
### Abstract
Reward models (RMs) play a pivotal role in aligning large language models
(LLMs) with human preferences. However, traditional RM training, which relies
on response pairs tied to specific prompts, struggles to disentangle
prompt-driven preferences from prompt-independent artifacts, such as response
length and format. In this work, we expose a fundamental limitation of current
RM training methods, where RMs fail to effectively distinguish between
contextual signals and irrelevant artifacts when determining preferences. To
address this, we introduce a causal framework that learns preferences
independent of these artifacts and propose a novel data augmentation technique
designed to eliminate them. Extensive experiments show that our approach
successfully filters out undesirable artifacts, yielding a more robust reward
model (RRM). Our RRM improves the performance of a pairwise reward model
trained on Gemma-2-9b-it, on RewardBench, increasing accuracy from 80.61% to
84.15%. Additionally, we train two DPO policies using both the RM and RRM,
demonstrating that the RRM significantly enhances DPO-aligned policies,
improving MT-Bench scores from 7.27 to 8.31 and length-controlled win-rates in
AlpacaEval-2 from 33.46% to 52.49%.
```
### 🌟 论文解读 | RRM：对抗Reward Hacking的鲁棒奖励模型训练新范式

### 📌 背景痛点/本文动机
在大语言模型（LLM）对齐人类偏好的技术栈中，基于人类反馈的强化学习（RLHF）是关键环节，而奖励模型（RM）则是RLHF里的核心组件之一。传统RM训练依赖与特定prompt绑定的响应对，但存在一个根本性缺陷：**难以区分“由prompt驱动的真实偏好信号”和“与prompt无关的干扰项（如响应长度、格式、特定n - gram或表情等）”**。这就导致了“奖励黑客（Reward Hacking）”问题——模型为了最大化奖励，会利用这些干扰项“走捷径”，而非真正对齐人类意图。比如LLM可能通过生成更长的回答来骗取高分，因为人类评估者往往对长内容存在偏向性；除了长度，格式（markdown、加粗）等也是常见的被利用点。现有一些针对长度偏见的改进（如给长度加惩罚、学习与长度正交的质量奖励），但无法覆盖所有潜在的干扰模式，且很难显式控制所有干扰项。因此，如何让RM更鲁棒地学习真实偏好、抵御各类Reward Hacking，成为亟待解决的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：因果框架下的偏好建模  
论文从**因果视角**重新审视RM训练问题。将人类对（prompt x，响应对(y₁,y₂)）的偏好拆解为两部分：一是与prompt相关的真实质量信号s(x, y₁, y₂)，二是与prompt无关的干扰项a(y₁, y₂)（如长度、格式等）。传统RM训练无法区分这两个因素，而论文提出的因果框架，旨在让RM学习“剥离干扰项后的真实偏好”。通过引入反事实prompt（即来自其他示例的prompt）等思路，估计偏好数据集中的“干扰项偏见”，从而为后续数据增强和模型训练提供理论支撑。  

💡 创新点2：基于因果规则的数据增强技术  
为了让RM在训练时更聚焦于真实偏好、过滤干扰项，论文设计了**新颖的数据增强方法**。具体来说，在构建RM训练数据时，引入其他示例的响应来“平衡”选中（chosen）和拒绝（rejected）响应中的干扰项。如图1所示，通过这种方式，让训练数据里的选中和拒绝响应在干扰项分布上更均衡，迫使RM不能再依赖这些干扰项来判断偏好，只能学习与prompt相关的真实质量信号。最终训练出鲁棒奖励模型（RRM）。  


### 📈 实验结果
论文通过多维度实验验证RRM的有效性：  
- **RewardBench基准测试**：在基于Gemma - 2 - 9b - it训练的 pairwise reward model 上，RRM将准确率从80.61%提升至84.15%，证明RRM能更准确区分优质响应。  
- **DPO策略训练对比**：分别用原始RM和RRM训练DPO策略，RRM训练的策略在MT - Bench上的分数从7.27提升到8.31；在AlpacaEval - 2的长度控制胜率从33.46%提升至52.49%。这表明RRM能显著增强对齐后的策略性能，让模型生成更符合人类偏好的结果。  


### 💬 可借鉴之处
1. **因果视角的问题建模**：当处理复杂的“信号 - 干扰”分离问题时，引入因果框架是一种很有潜力的思路。它能帮助我们更清晰拆解问题本质，为解决方案设计提供理论锚点。  
2. **数据增强的针对性设计**：针对“干扰项导致模型走捷径”的问题，论文没有盲目增加数据量，而是**基于问题本质（干扰项均衡）设计数据增强**，这种“精准打击”式的数据处理思路值得借鉴。在其他需要抵御模型“投机取巧”的任务（如对抗鲁棒性、去偏学习等）中，可思考如何构造类似的增强策略。  
3. **多维度的实验验证**：从奖励模型本身的准确率，到下游对齐策略的性能（MT - Bench、AlpacaEval - 2等不同基准），全面验证方法有效性。这种“从组件到系统”的实验设计逻辑，能更有力地证明技术价值，在科研和工程实践中都值得参考。  
```

## rewardanything--generalizable-principle-following-reward-models
### Abstract
Reward Models, essential for guiding Large Language Model optimization, are
typically trained on fixed preference datasets, resulting in rigid alignment to
single, implicit preference distributions. This prevents adaptation to diverse
real-world needs-from conciseness in one task to detailed explanations in
another. The standard practice of collecting task-specific preference data and
retraining reward models is resource-intensive, often producing biased rewards,
and limits practical application. We introduce generalizable,
principle-following reward models. We propose that RMs should understand and
adhere to dynamically provided natural language specifications of reward
principles, similar to instruction-following in LLMs. To measure this
capability, we develop RABench, a comprehensive benchmark for RMs focusing on
generalization across diverse principles. Evaluations on RABench reveal poor
generalization of current RMs. As a solution, we present RewardAnything, a
novel RM designed and trained to explicitly follow natural language principles.
We achieve SotA performance with RewardAnything in traditional RM benchmark
simply by specifying a well-defined principle, and results on RABench show we
excel in adapting to novel principles without retraining. Furthermore,
RewardAnything integrates seamlessly with existing RLHF methods and we show by
a case study on how to automatically and efficiently align LLMs with only
natural language principles.
### 🌟 论文解读 | RewardAnything：让奖励模型突破固定偏好，灵活遵循自然语言原则

### 📌 背景痛点/本文动机
大语言模型（LLMs）对齐人类偏好是关键挑战，奖励模型（RMs）作为RLHF等对齐技术的核心，当前训练方式存在两大瓶颈：一是泛化与适应性受限，依赖固定偏好数据集训练的RMs难以适配不同真实场景（如客服需简洁、科研助手需详细），重新收集数据再训练成本高；二是隐式偏好学习带来偏差与可解释性难题，现有RMs从人类标注偏好数据学习，多仅保留结果监督，易让模型通过虚假关联推断隐式价值，导致奖励偏差且可解释性差。为解决这些问题，论文提出转向**遵循原则的奖励模型**，让RMs能基于动态自然语言原则调整奖励标准。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出“遵循原则的奖励模型”概念范式  
明确RMs应像LLMs遵循指令一样，理解并遵循动态提供的自然语言奖励原则描述，无需为每个偏好场景训练新模型，使RMs成为跨多样偏好场景泛化的灵活工具，为构建适配多变人类偏好的AI系统筑牢能力基础。

💡 创新点2：构建RABench基准测试集  
打造全面的RMs基准RABench，聚焦评估RMs对新颖自然语言原则的泛化能力，覆盖多领域、暴露当前RMs局限，为衡量“遵循原则”能力进展提供标尺，填补领域内系统评估空白。

💡 创新点3：研发RewardAnything模型  
设计并训练RewardAnything这一生成式RM，结合GRPO与Group Relative Preference Learning技术，让模型能在推理时高效解读、应用多样偏好原则，实现对响应组的高效排序与打分，无需任务特定重训就能保持高质量偏好判断，还能高效支撑PPO、GRPO等RL训练。

### 📈 实验结果
在传统RM基准测试中，仅通过指定清晰原则，RewardAnything就能取得SOTA性能；在RABench上，展现出无需重训就能适配新原则的卓越能力；此外，案例研究验证其能仅以自然语言原则为指导自动高效对齐LLM，在细微安全、帮助性、响应质量等维度实现显著提升，有力证明“遵循原则”范式在LLM高效灵活对齐上的价值。

### 💬 可借鉴之处
1. 范式创新层面：将“遵循指令”思路迁移到奖励模型，提出“遵循自然语言原则”的新范式，为打破RMs固定偏好束缚、适配多样真实场景提供方向，启发后续对齐技术从“静态偏好拟合”转向“动态原则遵循”。  
2. 基准构建层面：RABench为评估RMs泛化到新原则的能力提供了标准化工具，推动领域内对RMs“灵活性”“通用性”的量化研究，后续可基于此持续迭代优化模型。  
3. 模型设计层面：RewardAnything结合特定训练方法实现推理时原则遵循，其技术路线（如GRPO结合、生成式RM设计）为打造灵活奖励模型提供了可参考的工程实践，助力后续高效RLHF流程搭建。

## visualprm--an-effective-process-reward-model-for-multimodal-reasoning
### Abstract
We introduce VisualPRM, an advanced multimodal Process Reward Model (PRM)
with 8B parameters, which improves the reasoning abilities of existing
Multimodal Large Language Models (MLLMs) across different model scales and
families with Best-of-N (BoN) evaluation strategies. Specifically, our model
improves the reasoning performance of three types of MLLMs and four different
model scales. Even when applied to the highly capable InternVL2.5-78B, it
achieves a 5.9-point improvement across seven multimodal reasoning benchmarks.
Experimental results show that our model exhibits superior performance compared
to Outcome Reward Models and Self-Consistency during BoN evaluation. To
facilitate the training of multimodal PRMs, we construct a multimodal process
supervision dataset VisualPRM400K using an automated data pipeline. For the
evaluation of multimodal PRMs, we propose VisualProcessBench, a benchmark with
human-annotated step-wise correctness labels, to measure the abilities of PRMs
to detect erroneous steps in multimodal reasoning tasks. We hope that our work
can inspire more future research and contribute to the development of MLLMs.
Our model, data, and benchmark are released in
https://internvl.github.io/blog/2025-03-13-VisualPRM/.
```
### 🌟 论文解读 | VisualPRM：开启多模态推理新征程

### 📌 背景痛点/本文动机
随着大语言模型在自然语言处理中取得显著成功，多模态大语言模型（MLLMs）在各种视觉 - 语言任务中也有了重大进展，但开源和专有模型在推理能力上仍存在较大差距。一系列研究探索了提升推理能力的方法，利用测试时缩放（TTS）来增强大语言模型推理能力的研究也有开展，但MLLMs的TTS在很大程度上尚未被充分探索。将TTS应用于MLLMs面临两大挑战：一是缺乏有效的批评模型，现有开源MLLMs难以作为批评模型，在BoN评估中提升效果有限；二是缺乏针对多模态批评模型的评估基准，BoN评估成本高且其性能受策略模型影响，难以比较不同批评模型。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建多模态过程监督数据集VisualPRM400K
该数据集包含约40万多模态过程监督数据，每个样本包括图像、问题、逐步解决方案以及每个步骤的正确性注释。从MMPR v1.1收集问题提示，然后使用自动数据管道生成过程正确性。
💡 创新点2：提出评估基准VisualProcessBench
用于评估PRMs和MLLMs在检测多模态推理任务中错误步骤的能力，包含2866个样本以及26950个人工注释的分步正确性标签。与先前基准不同，它要求模型检测给定解决方案中的所有错误，以减少评估中的假阴性。
💡 创新点3：开发多模态过程奖励模型VisualPRM
作为BoN评估中的批评模型，具有80亿参数。每个训练样本被表述为多轮对话，模型经过训练以预测每轮给定步骤的正确性。

### 📈 实验结果
VisualPRM在不同模型家族和规模上增强了MLLM推理能力。具体而言，在七个多模态推理基准上，VisualPRM分别将MiniCPM - V2.6、QwenVL2.5 - 7B、InternVL2.5 - 8B和InternVL2.5 - 78B的整体推理性能提高了8.0、3.7、8.4和5.9个百分点。在BoN评估中，VisualPRM表现优于结果奖励模型和自一致性。在VisualProcessBench上的实验表明，现有开源MLLMs难以准确评估每个步骤的正确性。

### 💬 可借鉴之处
对于提升多模态大语言模型推理能力的研究具有重要借鉴意义。构建的数据集和评估基准为后续相关研究提供了宝贵资源，VisualPRM作为批评模型的成功应用，为MLLMs的测试时缩放提供了有效思路，推动多模态推理领域的进一步发展。
```

## skywork-reward--bag-of-tricks-for-reward-modeling-in-llms
### Abstract
In this report, we introduce a collection of methods to enhance reward
modeling for LLMs, focusing specifically on data-centric techniques. We propose
effective data selection and filtering strategies for curating high-quality
open-source preference datasets, culminating in the Skywork-Reward data
collection, which contains only 80K preference pairs -- significantly smaller
than existing datasets. Using this curated dataset, we developed the
Skywork-Reward model series -- Skywork-Reward-Gemma-27B and
Skywork-Reward-Llama-3.1-8B -- with the former currently holding the top
position on the RewardBench leaderboard. Notably, our techniques and datasets
have directly enhanced the performance of many top-ranked models on
RewardBench, highlighting the practical impact of our contributions in
real-world preference learning applications.
```
### 🌟 论文解读 | Skywork-Reward：大语言模型奖励建模的实用技巧集

### 📌 背景痛点/本文动机
大语言模型（LLMs）的快速发展推动了其与用户偏好对齐的研究，奖励建模是其中关键且可扩展的方法。然而训练奖励模型面临挑战：人类偏好复杂难穷尽表示；开源偏好数据集常含噪声（如偏好与非偏好响应差异不明显或标注不一致），影响模型性能。同时，此前研究多关注模型架构与损失函数，而偏好数据的质量和可用性对奖励建模成功至关重要却未被充分重视。因此，本文聚焦以数据为中心的技术，提升LLMs奖励建模能力。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：高质量偏好数据精选策略  
提出有效数据选择与过滤策略来构建高质量开源偏好数据集。通过筛选对模型性能提升最有效的偏好对，打造了仅含8万偏好对的Skywork - Reward数据集，远小于现有数据集规模，却能保证数据质量，为奖励模型训练提供优质数据基础。  

💡 创新点2：损失函数的消融实验与选择  
对多种损失函数开展广泛消融实验，重点优化偏好与非偏好响应间的间隔。实验表明经典的Bradley - Terry损失在奖励建模任务中持续优于其他方法，凸显其鲁棒性，为奖励模型训练的损失函数选择提供有力依据。  

💡 创新点3：Skywork - Reward模型系列开发  
利用精心构建的数据集，开发Skywork - Reward模型系列（Skywork - Reward - Gemma - 27B和Skywork - Reward - Llama - 3.1 - 8B），将数据与训练技术结合，提升奖励模型性能。  

### 📈 实验结果
在RewardBench基准测试中，Skywork - Reward模型系列表现优异：截至2024年10月，Skywork - Reward - Gemma - 27B位居RewardBench排行榜首位，Skywork - Reward - Llama - 3.1 - 8B位列第七。此外，所构建的Skywork - Reward偏好数据集被后续诸多研究采用，证明了其价值与适用性；且文中技术和数据集直接提升了RewardBench上多个顶尖模型的性能，彰显在真实偏好学习应用中的实际影响。  

### 💬 可借鉴之处
1. 数据层面：重视数据质量，通过合理选择与过滤策略，用更小规模数据打造高质量数据集，为资源有限情况下构建有效训练数据提供思路，也说明数据“质”比“量”在某些场景更关键。  
2. 方法层面：对损失函数开展消融实验验证其在奖励建模任务的有效性，这种严谨的实验态度和方法值得借鉴，可帮助在模型训练中选择更优损失函数。  
3. 开源贡献：公开模型系列与数据集，推动领域发展，这种开放共享的科研精神利于行业整体进步，也为后续研究提供了坚实基础与参考范例。  
```

## on-designing-effective-rl-reward-at-training-time-for-llm-reasoning
### Abstract
Reward models have been increasingly critical for improving the reasoning
capability of LLMs. Existing research has shown that a well-trained reward
model can substantially improve model performances at inference time via
search. However, the potential of reward models during RL training time still
remains largely under-explored. It is currently unclear whether these reward
models can provide additional training signals to enhance the reasoning
capabilities of LLMs in RL training that uses sparse success rewards, which
verify the correctness of solutions. In this work, we evaluate popular reward
models for RL training, including the Outcome-supervised Reward Model (ORM) and
the Process-supervised Reward Model (PRM), and train a collection of LLMs for
math problems using RL by combining these learned rewards with success rewards.
Surprisingly, even though these learned reward models have strong
inference-time performances, they may NOT help or even hurt RL training,
producing worse performances than LLMs trained with the success reward only.
Our analysis reveals that an LLM can receive high rewards from some of these
reward models by repeating correct but unnecessary reasoning steps, leading to
a severe reward hacking issue. Therefore, we introduce two novel reward
refinement techniques, including Clipping and Delta. The key idea is to ensure
the accumulative reward of any reasoning trajectory is upper-bounded to keep a
learned reward model effective without being exploited. We evaluate our
techniques with multiple reward models over a set of 1.5B and 7B LLMs on MATH
and GSM8K benchmarks and demonstrate that with a carefully designed reward
function, RL training without any additional supervised tuning can improve all
the evaluated LLMs, including the state-of-the-art 7B LLM
Qwen2.5-Math-7B-Instruct on MATH and GSM8K benchmarks.
```
### 🌟 论文解读 | 大语言模型推理训练时，如何设计有效的强化学习奖励？

### 📌 背景痛点/本文动机
在大语言模型（LLM）领域，奖励模型对提升推理能力愈发关键。已有研究表明训练良好的奖励模型能在推理时通过搜索等方式大幅提升性能，但奖励模型在强化学习（RL）训练阶段的潜力却未充分挖掘。目前不清楚这些奖励模型在使用稀疏成功奖励（验证解决方案正确性）的RL训练中，能否提供额外训练信号来增强LLM推理能力。此外，一些强大LLM虽将奖励模型融入RL训练用于数学推理，但缺乏对奖励模型的详细分析，不确定其能否在成功奖励之外提供额外信号。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：评估主流奖励模型在RL训练中的表现  
对主流奖励模型（结果监督奖励模型ORM与过程监督奖励模型PRM）在RL训练中进行评估，将这些学习到的奖励与成功奖励结合，用于训练解决数学问题的LLM。发现尽管这些奖励模型在推理时表现强，但可能对RL训练无帮助甚至起反作用，比仅用成功奖励训练的LLM表现更差。

💡 创新点2：提出两种奖励优化技术应对奖励黑客问题  
分析发现LLM能通过重复正确但不必要的推理步骤从部分奖励模型获取高奖励，引发严重“奖励黑客”问题。为此提出Clipping（截断）和Delta（差值）两种奖励优化技术：Clipping机制将奖励限制在 upper threshold 内，让RL训练聚焦减少错误推理步骤；Delta机制通过减去相邻步骤间奖励来维持有界目标，抑制无意义重复模式以实现高回报并提升训练稳定性。

### 📈 实验结果
在MATH和GSM8K基准测试集上，用多个奖励模型对1.5B和7B规模的LLM（来自Qwen2和Qwen2.5系列）评估所提技术。结果显示Clipping和Delta能持续稳定RL训练；且精心设计奖励函数后，无额外监督微调的纯RL训练能提升所有评估的LLM，包括在MATH和GSM8K基准上的SOTA模型Qwen2.5-Math-7B-Instruct。

### 💬 可借鉴之处
1. 对奖励模型在RL训练阶段作用的探索思路值得借鉴，提醒研究者关注训练与推理阶段奖励模型表现差异，深入分析奖励模型在训练中潜在问题（如奖励黑客）。
2. 提出的Clipping和Delta技术为解决奖励黑客、稳定RL训练提供了新颖且有效的思路，后续在设计LLM的RL奖励函数时可参考这类约束奖励累计的方法。
3. 实验验证了纯RL训练在合理奖励设计下对提升LLM推理能力的有效性，为后续LLM推理能力优化的训练范式选择提供了实践依据。
```

## gram--a-generative-foundation-reward-model-for-reward-generalization
### Abstract
In aligning large language models (LLMs), reward models have played an
important role, but are standardly trained as discriminative models and rely
only on labeled human preference data. In this paper, we explore methods that
train reward models using both unlabeled and labeled data. Building on the
generative models in LLMs, we develop a generative reward model that is first
trained via large-scale unsupervised learning and then fine-tuned via
supervised learning. We also show that by using label smoothing, we are in fact
optimizing a regularized pairwise ranking loss. This result, in turn, provides
a new view of training reward models, which links generative models and
discriminative models under the same class of training objectives. The outcome
of these techniques is a foundation reward model, which can be applied to a
wide range of tasks with little or no further fine-tuning effort. Extensive
experiments show that this model generalizes well across several tasks,
including response ranking, reinforcement learning from human feedback, and
task adaptation with fine-tuning, achieving significant performance
improvements over several strong baseline models.
```
### 🌟 论文解读 | GRAM：面向奖励泛化的生成式基础奖励模型

### 📌 背景痛点/本文动机
在大语言模型（LLMs）的对齐过程中，奖励模型扮演着关键角色。然而，传统奖励模型多作为判别式模型训练，且高度依赖带标签的人类偏好数据，存在标注成本高、对无标签数据利用不足等问题。同时，现有训练方式难以高效得到能在多任务间泛化的基础奖励模型，限制了奖励模型在不同场景下的灵活应用与效率提升。因此，如何利用无标签和有标签数据来训练更具泛化能力的奖励模型，成为亟待解决的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：**生成式奖励模型的两阶段训练范式**  
基于大语言模型的生成式能力，提出先通过大规模无监督学习预训练、再利用监督学习微调的生成式奖励模型训练流程。预训练阶段在输入 - 响应数据上学习输入与响应的对应关系，无需偏好标注数据，可规模化获取响应比较的通用知识；微调阶段利用人类偏好数据学习预测响应间偏好，最终得到能直接或经少量微调应用于下游任务的基础奖励模型，充分结合无标签与有标签数据优势。

💡 创新点2：**标签平滑下的损失函数统一视角**  
引入标签平滑技术并证明，其使训练目标可转化为正则化的 pairwise ranking loss（Bradley - Terry 损失形式）。这一结果在奖励模型训练层面，将生成式模型与判别式模型统一到同一类训练目标下，为奖励模型训练提供了新视角，且标签平滑对生成式奖励模型训练有显著增益，助力模型泛化。

### 📈 实验结果
在响应排序、基于人类反馈的强化学习（RLHF）、任务自适应等多任务场景下开展大量实验。结果表明，GRAM 无需或仅需少量微调就能在各任务中展现良好泛化性，性能远超多个强基线模型。例如，基于 LLaMA - 3.1 - 8B - Instruct 训练奖励模型时，GRAM 在 RewardBench 平均准确率上，相比普通判别式和生成式奖励模型分别提升 11.0 和 5.1 个百分点，验证了方法的有效性与优越性。

### 💬 可借鉴之处
1. **数据利用思路**：打破传统奖励模型对有标签数据的强依赖，示范了无标签数据在预训练阶段为模型注入通用知识、有标签数据在微调阶段精准对齐偏好的高效数据利用范式，为后续奖励模型数据策略设计提供参考。  
2. **模型统一视角**：通过标签平滑实现生成式与判别式奖励模型训练目标的关联与统一，启发研究者从更宏观的损失函数设计与模型本质联系角度，探索奖励模型乃至更广泛的大模型训练优化路径。  
3. **基础模型构建**：打造能跨多任务泛化的基础奖励模型，为大语言模型对齐流程提供“预训练 - 少样本微调”的高效模式，减少下游任务重复训练成本，推动奖励模型向更通用、更易用方向发展，相关思路可迁移至其他需泛化能力的模型构建场景。
```

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
```
### 🌟 论文解读 | 通用奖励建模的推理时缩放：解锁大模型奖励信号新维度

### 📌 背景痛点/本文动机
大语言模型（LLMs）的蓬勃发展推动了人工智能研究的重大变革，强化学习（RL）作为大模型训练后的关键技术被广泛应用，能显著提升模型在人类价值对齐、长期推理等方面的表现。但RL面临的核心挑战是在通用领域（非可验证问题或人工规则场景）为LLMs获取准确奖励信号。通用奖励建模需兼顾输入灵活性与跨域奖励准确性，且要实现推理时的有效算力扩展。现有奖励生成范式（如标量、半标量等）在输入灵活性和推理时扩展性上存在局限，学习方法也较少关注推理时扩展性与奖励生成行为的关联，难以满足通用场景需求。因此，探索如何通过合适方法实现通用奖励建模的推理时缩放成为关键。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：采用逐点生成式奖励建模（GRM）  
选择逐点生成式奖励建模（pointwise generative reward modeling, GRM）作为奖励建模方法，它能在纯语言表征内统一单条、配对及多条响应的评分，为不同输入类型提供灵活性，同时具备推理时缩放的潜力，解决了通用奖励建模对输入灵活性的需求这一挑战。  

💡 创新点2：提出自原则性批判调优（SPCT）  
设计Self - Principled Critique Tuning（SPCT）学习方法，借助基于规则的在线强化学习，让GRM学会根据输入查询和响应自适应生成原则与批判，在通用领域提升奖励质量，培养GRM中可扩展的奖励生成行为，应对通用领域准确生成奖励的挑战。基于此训练得到DeepSeek - GRM - 27B模型（以Gemma - 2 - 27B为基础后训练）。  

💡 创新点3：推理时缩放的工程与模型设计  
为实现有效推理时缩放，采用并行采样扩展算力使用，DeepSeek - GRM可生成不同原则和批判集合后投票得到最终奖励；大规模采样下能基于更丰富多样的原则更精准判断，输出更细粒度奖励，解决推理时随算力增加生成更高质量奖励信号及学习可扩展行为的挑战。此外，训练元奖励模型（meta RM）辅助投票以优化缩放性能。  

### 📈 实验结果
实验表明SPCT显著提升了GRM的质量与可扩展性，在多个综合奖励建模基准测试中超越现有方法和模型，且无严重领域偏差；与训练时缩放相比，能取得更优性能。不过DeepSeek - GRM在部分任务仍存挑战，未来通用奖励系统研究或可解决。同时从图1推理时缩放性能对比可见，DeepSeek - GRM相关方法在采样扩展下表现突出。  

### 💬 可借鉴之处
1. 范式选择角度：GRM这种逐点生成式奖励建模思路为处理多类型输入、实现推理时扩展提供了新范式参考，在需灵活处理不同响应输入的奖励建模场景可借鉴。  
2. 学习方法角度：SPCT将在线RL与原则、批判生成结合，为引导模型学习可扩展奖励行为提供了创新思路，在优化模型推理时性能的学习策略设计上有启发。  
3. 工程实现角度：并行采样 + 元RM辅助投票的推理时缩放方案，为大模型在推理阶段高效利用算力提升性能提供了工程实践方向，在大模型推理优化、多轮决策类任务中可参考该扩展算力并引导决策的思路。  
4. 开源与生态角度：论文提及模型将开源，这种开放生态的做法也为领域内知识共享、加速研究迭代提供范例，值得关注开源协作的团队参考。
```

## rest-mcts*--llm-self-training-via-process-reward-guided-tree-search
### Abstract
Recent methodologies in LLM self-training mostly rely on LLM generating
responses and filtering those with correct output answers as training data.
This approach often yields a low-quality fine-tuning training set (e.g.,
incorrect plans or intermediate reasoning). In this paper, we develop a
reinforced self-training approach, called ReST-MCTS*, based on integrating
process reward guidance with tree search MCTS* for collecting higher-quality
reasoning traces as well as per-step value to train policy and reward models.
ReST-MCTS* circumvents the per-step manual annotation typically used to train
process rewards by tree-search-based reinforcement learning: Given oracle final
correct answers, ReST-MCTS* is able to infer the correct process rewards by
estimating the probability this step can help lead to the correct answer. These
inferred rewards serve dual purposes: they act as value targets for further
refining the process reward model and also facilitate the selection of
high-quality traces for policy model self-training. We first show that the
tree-search policy in ReST-MCTS* achieves higher accuracy compared with prior
LLM reasoning baselines such as Best-of-N and Tree-of-Thought, within the same
search budget. We then show that by using traces searched by this tree-search
policy as training data, we can continuously enhance the three language models
for multiple iterations, and outperform other self-training algorithms such as
ReST$^\text{EM}$ and Self-Rewarding LM. We release all code at
https://github.com/THUDM/ReST-MCTS.
```
### 🌟 论文解读 | ReST-MCTS*：用过程奖励引导树搜索实现大模型自训练新突破

### 📌 背景痛点/本文动机
大语言模型（LLM）自训练领域，现有方法多依赖模型生成回答后筛选正确输出作为训练数据，但这类方法易得到低质量微调数据集——比如推理过程里存在错误规划或中间推理步骤有问题，可最终答案却碰巧正确（即“假阳性”推理轨迹）。这会限制LLM在复杂推理任务上的微调表现。同时，训练可靠的“过程奖励模型（PRM）”来验证每一步推理是否正确，往往依赖人工逐步骤标注，成本高且难扩展。于是，本文要解决的核心问题是：**如何自动获取高质量推理轨迹，并高效利用奖励信号完成验证与LLM自训练**。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出ReST-MCTS*框架，融合过程奖励引导与MCTS*树搜索  
ReST-MCTS*采用改进的蒙特卡洛树搜索（MCTS*）作为推理策略，由训练好的“逐步骤过程奖励模型（PRM）”引导搜索。它能在给定最终正确答案（oracle answer）时，通过估计某一步骤导向正确答案的概率，**自动推断每一步的过程奖励**——无需人工逐步骤标注。这些推断出的奖励有两大作用：一是作为“值目标”去迭代优化过程奖励模型；二是帮我们筛选高质量推理轨迹，用于策略模型的自训练。  

💡 创新点2：自动化生成过程奖励标签，摆脱人工依赖  
以往训练过程奖励模型需要大量人工逐步骤标注，ReST-MCTS*则通过“充分次数的rollout（推演）”，自动为每个中间节点生成过程奖励的标注。这个标注过程能有效过滤出最高质量的样本子集，全程无需额外人工介入，解决了过程奖励模型训练的标注瓶颈。  

💡 创新点3：基于树搜索的强化学习思路，提升推理与自训练效果  
ReST-MCTS*把树搜索和强化学习结合，让MCTS*在相同搜索预算下，推理准确率超越了Best-of-N、Tree-of-Thought等经典LLM推理基线；同时，用MCTS*搜索得到的推理轨迹做训练数据，能在多轮迭代中持续提升LLM性能，超过ReST^EM、Self-Rewarding LM等自训练算法。  


### 📈 实验结果
1. 推理策略对比：在SciBench和MATH等基准测试中，ReST-MCTS*里的MCTS*树搜索策略，**在相同搜索预算下，准确率超过Self-Consistency、Best-of-N等基线方法**（如图2所示）。  
2. 自训练效果：用MCTS*搜索出的轨迹做训练数据，多轮迭代后能持续增强LLM性能，在多个任务上**超越ReST^EM、Self-Rewarding LM等自训练算法**（如表2所示）。  
3. 过程奖励模型质量：ReST-MCTS*里的奖励生成机制，相比MATH-SHEPHERD等以往技术，训练出的过程奖励模型质量更优（如表3所示）。  


### 💬 可借鉴之处
1. 解决标注难题的思路：ReST-MCTS*展示了“如何用算法自动生成标注”来训练过程奖励模型，为需要密集标注但人工成本高的任务提供了“去人工化”的技术参考。  
2. 树搜索+强化学习在LLM推理的应用：把MCTS这类经典树搜索算法与过程奖励引导结合，为大模型推理策略的优化提供了新范式，证明了模型-based RL在自训练里的潜力。  
3. 自训练数据质量的提升：通过“筛选高质量推理轨迹”来做自训练，点明了“数据质量”在大模型迭代优化中的关键作用，后续工作可借鉴这类“先筛后训”的思路提升微调效果。  
```

## skywork-reward-v2--scaling-preference-data-curation-via-human-ai-synergy
### Abstract
Despite the critical role of reward models (RMs) in reinforcement learning
from human feedback (RLHF), current state-of-the-art open RMs perform poorly on
most existing evaluation benchmarks, failing to capture the spectrum of nuanced
and sophisticated human preferences. Even approaches that incorporate advanced
training techniques have not yielded meaningful performance improvements. We
hypothesize that this brittleness stems primarily from limitations in
preference datasets, which are often narrowly scoped, synthetically labeled, or
lack rigorous quality control. To address these challenges, we present a
large-scale preference dataset comprising 40 million preference pairs, named
SynPref-40M. To enable data curation at scale, we design a human-AI synergistic
two-stage pipeline that leverages the complementary strengths of human
annotation quality and AI scalability. In this pipeline, humans provide
verified annotations, while large language models perform automatic curation
based on human guidance. Training on this preference mixture, we introduce
Skywork-Reward-V2, a suite of eight reward models ranging from 0.6B to 8B
parameters, trained on a carefully curated subset of 26 million preference
pairs from SynPref-40M. We demonstrate that Skywork-Reward-V2 is versatile
across a wide range of capabilities, including alignment with human
preferences, objective correctness, safety, resistance to stylistic biases, and
best-of-N scaling, achieving state-of-the-art performance across seven major
reward model benchmarks. Ablation studies confirm that the effectiveness of our
approach stems not only from data scale but also from high-quality curation.
The Skywork-Reward-V2 series represents substantial progress in open reward
models, highlighting the untapped potential of existing preference datasets and
demonstrating how human-AI curation synergy can unlock significantly higher
data quality.
### 🌟 论文解读 | Skywork-Reward-V2：人机协同解锁偏好数据规模与质量新高度

### 📌 背景痛点/本文动机
奖励模型（RMs）在基于人类反馈的强化学习（RLHF）中至关重要，但当前开源奖励模型在多数评估基准上表现不佳，难以捕捉复杂精妙的人类偏好。究其原因，现有偏好数据集存在范围狭窄、标签合成性强或质量控制不严谨等局限，即便采用先进训练技术也难有实质性提升。因此，提升偏好数据质量以推动开源奖励模型发展成为关键诉求。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建超大规模偏好数据集SynPref - 40M  
打造了包含4000万偏好对的大规模偏好数据集SynPref - 40M，为奖励模型训练提供了丰富的数据基础，这也是目前已知规模最大的精心整理偏好混合数据集。  

💡 创新点2：设计人机协同两阶段数据整理 pipeline  
第一阶段借助严格协议下的人工验证保障数据质量；第二阶段利用人类偏好引导的大语言模型（LLM）作为“裁判”实现规模化整理，同时结合奖励模型的迭代训练，持续纳入人工标签反馈并召回模型表现差的偏好数据以促进学习，最终得到2600万高质量偏好对用于模型训练。  

💡 创新点3：推出Skywork - Reward - V2系列奖励模型  
基于SynPref - 40M筛选出的偏好数据，训练出包含8个从0.6B到8B参数规模的Skywork - Reward - V2系列奖励模型，仅用Bradley - Terry目标函数训练却能在多基准展现卓越性能。  

### 📈 实验结果
在7个主要奖励模型基准测试中，Skywork - Reward - V2系列表现亮眼，8B规模模型在所有7个基准上大幅超越现有开源奖励模型；在人类偏好对齐、客观正确性、安全性、抗风格偏差、best - of - N缩放等多关键维度也展现出优越性能。消融实验表明，SynPref - 40M的成功既源于规模也得益于高质量，同时人机协同 pipeline 中人工标注、人类偏好引导的LLM标注及严谨标注协议都至关重要。  

### 💬 可借鉴之处
数据层面，大规模且高质量的偏好数据集对模型性能提升作用显著，SynPref - 40M的构建思路为数据驱动的模型优化提供范例；方法层面，人机协同的两阶段数据整理 pipeline 有效结合人类标注质量与AI可扩展性优势，为大规模数据高质量整理提供了可参考的流程框架；模型层面，Skywork - Reward - V2系列证明合理利用数据与训练策略，能在开源奖励模型领域实现性能突破，为后续奖励模型研发指明方向，凸显了挖掘现有偏好数据潜力与人机协同在提升数据质量上的价值。

