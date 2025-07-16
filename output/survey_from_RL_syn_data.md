# Paper List from BIB File: tmp0v9vy7jo.bib
- [25/06] **SynthRL: Scaling Visual Reasoning with Verifiable Data Synthesis**  
[[Paper](http://arxiv.org/pdf/2506.02096v1)] [[Code/Page]()] [[TLDR/Notes](#synthrl--scaling-visual-reasoning-with-verifiable-data-synthesis)]

- [25/05] **SynLogic: Synthesizing Verifiable Reasoning Data at Scale for Learning Logical Reasoning and Beyond**  
[[Paper](http://arxiv.org/pdf/2505.19641v4)] [[Code/Page](https://github.com/MiniMax-AI/SynLogic.)] [[TLDR/Notes](#synlogic--synthesizing-verifiable-reasoning-data-at-scale-for-learning-logical-reasoning-and-beyond)]

- [25/05] **Synthetic Data RL: Task Definition Is All You Need**  
[[Paper](http://arxiv.org/pdf/2505.17063v1)] [[Code/Page](https://github.com/gydpku/Data_Synthesis_RL/.)] [[TLDR/Notes](#synthetic-data-rl--task-definition-is-all-you-need)]

- [25/04] **RV-Syn: Rational and Verifiable Mathematical Reasoning Data Synthesis based on Structured Function Library**  
[[Paper](http://arxiv.org/pdf/2504.20426v1)] [[Code/Page]()] [[TLDR/Notes](#rv-syn--rational-and-verifiable-mathematical-reasoning-data-synthesis-based-on-structured-function-library)]

- [25/04] **Synthetic Data Generation & Multi-Step RL for Reasoning & Tool Use**  
[[Paper](http://arxiv.org/pdf/2504.04736v2)] [[Code/Page]()] [[TLDR/Notes](#synthetic-data-generation-&-multi-step-rl-for-reasoning-&-tool-use)]

- [25/05] **VisualSphinx: Large-Scale Synthetic Vision Logic Puzzles for RL**  
[[Paper](http://arxiv.org/pdf/2505.23977v1)] [[Code/Page]()] [[TLDR/Notes](#visualsphinx--large-scale-synthetic-vision-logic-puzzles-for-rl)]



# TLDR/Notes
## synthrl--scaling-visual-reasoning-with-verifiable-data-synthesis
### Abstract
Vision-language models (VLMs) trained via reinforcement learning with
verifiable reward (RLVR) have shown notable progress in scaling test-time
compute effectively. In this work, we investigate how synthesized RL data can
further improve RLVR. To this end, we propose \textbf{SynthRL}-a scalable and
guaranteed pipeline for automatic data scaling in reasoning-oriented RL
training. SynthRL comprises three key stages: (1) selecting seed questions with
appropriate distribution, (2) augmenting them into more challenging variants
while preserving the original answers, and (3) a guaranteed verification stage
that ensures near-perfect correctness and difficulty enhancement. Our empirical
experiments demonstrate SynthRL's scalability and effectiveness. When applied
to the MMK12 dataset, SynthRL synthesizes over 3.3K additional verifiable,
challenging questions from approximately 8K seed samples. Models trained with
our synthesized data achieve consistent gains across five out-of-domain visual
math reasoning benchmarks, with a significant improvement over baseline models
trained on seed data alone. Notably, detailed analysis reveals that the gains
are more pronounced on the most challenging evaluation samples, highlighting
SynthRL's effectiveness in eliciting deeper and more complex reasoning
patterns.
```
### 🌟 论文解读 | SynthRL：用可验证数据合成扩展视觉推理能力

### 📌 背景痛点/本文动机
在人工智能领域，基于带可验证奖励的强化学习（RLVR）训练的视觉-语言模型（VLMs），虽已在高效扩展测试时计算方面取得显著进展，但如何进一步利用合成的强化学习数据来提升 RLVR 效果仍是待探索的方向。现有的训练数据规模与质量，对于让模型掌握更复杂、更具挑战性的推理能力存在不足，因此需要一套可扩展且能保障质量的自动数据扩展 pipeline，来为面向推理的强化学习训练提供支持，这便是本文工作的出发点。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出 SynthRL  pipeline  
SynthRL 是一个用于面向推理的 RL 训练中自动数据扩展的可扩展且有保障的流程。它包含三个关键阶段，从种子问题选择到问题变体增强再到验证，形成完整的高质量数据合成链路，为模型训练提供更丰富且可靠的训练素材。  

💡 创新点2：三阶段协同工作机制  
- 阶段一：选择具有合适分布的种子问题。这一步为后续数据合成奠定基础，确保初始种子能覆盖合理的分布范围，让后续合成数据有良好的“基因”。  
- 阶段二：在保留原始答案的同时将种子问题增强为更具挑战性的变体。既保证了答案的一致性，又能让模型接触到更复杂的问题形式，锻炼推理能力。  
- 阶段三：保障型验证阶段。该阶段确保了合成后数据近乎完美的正确性以及难度的有效提升，让合成数据在质量上有可靠保障，避免引入错误数据干扰模型训练。  

### 📈 实验结果
在 MMK12 数据集上开展的实证实验有力地展现了 SynthRL 的可扩展性与有效性。从约 8K 的种子样本中，SynthRL 合成出超 3.3K 额外的可验证且有挑战性的问题。使用该合成数据训练的模型，在五个域外视觉数学推理基准测试中均实现了持续性能提升，相比仅用种子数据训练的基线模型有显著改进。更值得关注的是，详细分析表明在最具挑战性的评估样本上，性能提升更为明显，这凸显了 SynthRL 在激发模型更深入、更复杂推理模式方面的有效性。  

### 💬 可借鉴之处
- 数据合成思路：SynthRL 展示了通过合理的多阶段流程来合成高质量训练数据的范式，为其他需要数据扩展的任务（尤其是推理类任务）提供了“选择 - 增强 - 验证”的参考框架，启发研究者思考如何系统性地扩充训练数据。  
- 验证机制应用：其保障型验证阶段的设计，让我们意识到在数据合成过程中加入严格验证环节对于保证数据质量和模型训练效果的重要性，可借鉴到各类需要对合成数据质量把控的场景中。  
- 复杂推理能力提升：针对提升模型在复杂、挑战性样本上的推理表现，SynthRL 的实践证明了合理设计的数据合成方法能有效引导模型掌握更深度的推理模式，这为想要提升模型复杂任务处理能力的研究者提供了数据层面的优化思路。  
```

## synlogic--synthesizing-verifiable-reasoning-data-at-scale-for-learning-logical-reasoning-and-beyond
### Abstract
Recent advances such as OpenAI-o1 and DeepSeek R1 have demonstrated the
potential of Reinforcement Learning (RL) to enhance reasoning abilities in
Large Language Models (LLMs). While open-source replication efforts have
primarily focused on mathematical and coding domains, methods and resources for
developing general reasoning capabilities remain underexplored. This gap is
partly due to the challenge of collecting diverse and verifiable reasoning data
suitable for RL. We hypothesize that logical reasoning is critical for
developing general reasoning capabilities, as logic forms a fundamental
building block of reasoning. In this work, we present SynLogic, a data
synthesis framework and dataset that generates diverse logical reasoning data
at scale, encompassing 35 diverse logical reasoning tasks. The SynLogic
approach enables controlled synthesis of data with adjustable difficulty and
quantity. Importantly, all examples can be verified by simple rules, making
them ideally suited for RL with verifiable rewards. In our experiments, we
validate the effectiveness of RL training on the SynLogic dataset based on 7B
and 32B models. SynLogic leads to state-of-the-art logical reasoning
performance among open-source datasets, surpassing DeepSeek-R1-Distill-Qwen-32B
by 6 points on BBEH. Furthermore, mixing SynLogic data with mathematical and
coding tasks improves the training efficiency of these domains and
significantly enhances reasoning generalization. Notably, our mixed training
model outperforms DeepSeek-R1-Zero-Qwen-32B across multiple benchmarks. These
findings position SynLogic as a valuable resource for advancing the broader
reasoning capabilities of LLMs. We open-source both the data synthesis pipeline
and the SynLogic dataset at https://github.com/MiniMax-AI/SynLogic.
```
### 🌟 论文解读 | SynLogic：大规模合成可验证推理数据，助力LLM逻辑推理能力跃升

### 📌 背景痛点/本文动机
在大语言模型（LLMs）的发展进程中，强化学习（RL）已被证明能有效提升模型推理能力（如OpenAI - o1、DeepSeek R1等成果所示）。然而，开源社区的复刻工作多聚焦于数学和编码领域，通用推理能力的开发方法与资源仍待深入探索。这一缺口部分源于收集适合RL的多样且可验证推理数据的挑战。逻辑推理作为推理的基础构成要素，对通用推理能力发展至关重要。因此，如何大规模生成多样、可验证的逻辑推理数据以支撑RL训练，成为推动LLMs通用推理能力进步的关键问题，这也正是本文工作的出发点。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出SynLogic数据合成框架与数据集
SynLogic能够大规模生成涵盖35种不同逻辑推理任务的逻辑推理数据。该框架突破了以往数据收集在多样性与规模上的限制，为LLMs逻辑推理能力训练提供了丰富且多元的素材来源，覆盖多种逻辑推理场景，让模型有机会学习不同类型的逻辑思考方式。

💡 创新点2：支持可控的数据合成与可验证性设计
一方面，SynLogic支持对数据难度和数量进行灵活调整，可根据训练需求定制化生成数据，满足不同阶段、不同模型规模对训练数据的要求；另一方面，所有生成的示例都能通过简单规则验证，这为基于可验证奖励的强化学习训练创造了理想条件，解决了推理数据难以验证从而影响RL训练有效性的问题。

### 📈 实验结果
在实验中，基于7B和32B规模的模型验证了在SynLogic数据集上进行RL训练的有效性。SynLogic在开源数据集中实现了逻辑推理性能的领先，在BBEH基准上超越DeepSeek - R1 - Distill - Qwen - 32B达6个百分点；此外，将SynLogic数据与数学、编码任务数据混合训练时，不仅提升了这些领域的训练效率，还显著增强了推理泛化能力，混合训练模型在多个基准测试中超越了DeepSeek - R1 - Zero - Qwen - 32B。

### 💬 可借鉴之处
从方法层面，SynLogic的数据合成思路为解决通用推理数据稀缺、难验证问题提供了创新范式，其可控合成与可验证设计可被借鉴到其他推理类数据构建场景，助力不同领域推理数据的生成；从应用层面，证明了逻辑推理数据对LLMs通用推理能力提升的关键作用，以及跨领域数据混合训练对效率和泛化性的增益，为后续LLMs在推理能力训练方向提供了数据构建、训练策略等多维度的参考，指引研究者关注逻辑推理基础地位并探索更优训练数据组合方式。同时，开源的数据合成 pipeline 和数据集也为社区提供了直接可用的资源与研究基础，方便更多人在此之上开展工作。
```

## synthetic-data-rl--task-definition-is-all-you-need
### Abstract
Reinforcement learning (RL) is a powerful way to adapt foundation models to
specialized tasks, but its reliance on large-scale human-labeled data limits
broad adoption. We introduce Synthetic Data RL, a simple and general framework
that reinforcement fine-tunes models using only synthetic data generated from a
task definition. Our method first generates question and answer pairs from the
task definition and retrieved documents, then adapts the difficulty of the
question based on model solvability, and selects questions using the average
pass rate of the model across samples for RL training. On Qwen-2.5-7B, our
method achieves a 29.2% absolute improvement over the base model on GSM8K (+2.9
pp vs. instruction-tuned, +6.6 pp vs. Self-Instruct), 8.7% on MATH, 13.1% on
GPQA (+7.0 pp vs. SynthLLM), 8.9% on MedQA, 17.7% on CQA (law) and 13.7% on CFA
(finance). It surpasses supervised fine-tuning under the same data budget and
nearly matches RL with full human data across datasets (e.g., +17.2 pp on
GSM8K). Adding 100 human demonstrations improves the performance of GSM8K only
by 0.4 pp, showing a limited added value. By reducing human data annotation,
Synthetic Data RL enables scalable and efficient RL-based model adaptation.
Code and demos are available at https://github.com/gydpku/Data_Synthesis_RL/.
```
### 🌟 论文解读 | 仅用任务定义，Synthetic Data RL革新强化学习数据范式

### 📌 背景痛点/本文动机
强化学习（RL）是让基础模型适配特定任务的有力手段，然而其对大规模人工标注数据的依赖限制了广泛应用。获取大规模高质量的人工标注数据成本高、耗时长，这成为RL在更多场景落地的阻碍。因此，如何摆脱对大规模人工标注数据的强依赖，实现高效的基于RL的模型适配，是亟待解决的问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：基于任务定义生成合成数据  
Synthetic Data RL提出仅利用任务定义来生成合成数据进行强化学习微调的通用框架。首先从任务定义和检索到的文档中生成问答对，摆脱了对大量人工标注数据的依赖，为模型训练提供基础数据来源。  

💡 创新点2：动态调整问题难度与选择策略  
根据模型的可解性来调整问题难度，确保训练数据能适配模型当前能力；同时利用模型在样本上的平均通过率来选择问题用于RL训练，让训练数据的选择更科学合理，提升训练效率与效果。  

### 📈 实验结果
在Qwen - 2.5 - 7B模型上进行的实验显示，该方法在多个数据集上取得显著提升：GSM8K数据集上比基础模型绝对提升29.2%（比指令微调高2.9个百分点，比Self - Instruct高6.6个百分点）；MATH数据集提升8.7%；GPQA数据集提升13.1%（比SynthLLM高7.0个百分点）；MedQA提升8.9%；CQA（law）提升17.7%；CFA（finance）提升13.7%。在相同数据预算下超越有监督微调，在多个数据集上几乎能与使用完整人工数据的RL效果匹敌（如GSM8K上高17.2个百分点）。另外，添加100个人工演示仅让GSM8K性能提升0.4个百分点，说明人工数据附加值有限，凸显了合成数据方法的优势。  

### 💬 可借鉴之处
该论文提供了一种摆脱大规模人工标注数据束缚的新思路，其基于任务定义生成合成数据、动态调整难度与选择训练数据的策略，为后续强化学习在模型适配领域的研究提供了新范式。对于想要在资源有限或数据标注困难场景下进行模型优化的研究者和开发者而言，这种利用合成数据进行强化学习的方法具有很强的借鉴意义，有望推动RL更高效、可扩展地应用于各类特定任务中。同时，代码和演示的开源也方便社区进一步研究与拓展该方法。
```

## rv-syn--rational-and-verifiable-mathematical-reasoning-data-synthesis-based-on-structured-function-library
### Abstract
The advancement of reasoning capabilities in Large Language Models (LLMs)
requires substantial amounts of high-quality reasoning data, particularly in
mathematics. Existing data synthesis methods, such as data augmentation from
annotated training sets or direct question generation based on relevant
knowledge points and documents, have expanded datasets but face challenges in
mastering the inner logic of the problem during generation and ensuring the
verifiability of the solutions. To address these issues, we propose RV-Syn, a
novel Rational and Verifiable mathematical Synthesis approach. RV-Syn
constructs a structured mathematical operation function library based on
initial seed problems and generates computational graphs as solutions by
combining Python-formatted functions from this library. These graphs are then
back-translated into complex problems. Based on the constructed computation
graph, we achieve solution-guided logic-aware problem generation. Furthermore,
the executability of the computational graph ensures the verifiability of the
solving process. Experimental results show that RV-Syn surpasses existing
synthesis methods, including those involving human-generated problems,
achieving greater efficient data scaling. This approach provides a scalable
framework for generating high-quality reasoning datasets.
```
### 🌟 论文解读 | RV-Syn：基于结构化函数库的可解释、可验证数学推理数据合成新范式

### 📌 背景痛点/本文动机
大语言模型（LLMs）推理能力的提升，尤其是数学推理能力，高度依赖高质量的推理数据。现有数据合成方法（如基于标注训练集的数据增强、基于知识点/文档的直接问题生成）虽扩充了数据集，但存在两大核心痛点：**生成时难以把握问题内在逻辑**（导致合成题逻辑矛盾、推理深度不足）；**解答过程的可验证性差**（无法在合成阶段验证答案正确性，影响训练效率）。例如直接生成题可能表面合理，实际存在内部矛盾或推理漏洞，复杂多步推理题尤甚。因此，亟需一种能兼顾逻辑合理性与解答可验证性的数学推理数据合成方法。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：模仿人类出题逻辑，构建“计算图-逆生成”流程  
RV-Syn 借鉴人类教师出题思路——先明确解题步骤（计算目标）再衍生题目。具体分三步：从种子题中提取基于代码的“计算图”（每个函数对应数学操作）；构建结构化函数库（以图格式描述函数关系）；通过图感知采样组合函数生成新计算图，执行后逆生成带正确答案的新题目。这种“先有解、后有题”的方式，天然保证题目逻辑连贯性。

💡 创新点2：结构化函数库 + 可执行计算图，保障可解释与可验证  
- 结构化函数库：基于初始种子问题，整理出 Python 格式的数学操作函数集合，清晰定义函数间关系，为复杂推理提供“原子操作”级支撑。  
- 可执行计算图：生成的计算图不仅是解题逻辑的抽象，还能直接执行，既作为题目生成的“蓝图”，又能验证解题过程（执行即验证）。这让合成题从“逻辑合理性”到“答案正确性”都有迹可循。  

💡 创新点3：支持复杂推理结构生成  
传统直接生成法难处理多跳推理、迭代循环、模块化结构等复杂题型，RV-Syn 借助计算图的组合能力，自然支持这些高阶推理结构（如多步骤顺序执行、for 循环式迭代、函数调用式模块化），填补了现有方法在复杂推理数据合成上的空白。

### 📈 实验结果
论文在多个基准测试中验证 RV-Syn 性能：  
- 对比现有合成方法（含人工设计题方法），RV-Syn 在 5 个数学推理基准上平均表现更优；  
- 效率层面，仅用一半数据量就超越此前 SOTA 方法，数据规模化曲线更高效，证明其“少数据、高质量”的合成能力。  

### 💬 可借鉴之处
1. **数据合成范式迁移**：“先解后题”的逆生成思路可推广到其他需要逻辑连贯性的领域（如科学推理、代码生成），为垂直领域数据合成提供新视角；  
2. **结构化 + 可执行的设计**：将代码的结构化、可执行性融入数据合成，既解决逻辑模糊性，又实现过程可验证，这种“代码即蓝图”的思路对工具增强型 LLM 训练有参考价值；  
3. **复杂推理数据构建**：针对多跳、迭代、模块化等复杂推理场景，RV-Syn 展示了“从原子操作到复杂逻辑”的组合式构建路径，为提升 LLM 复杂任务处理能力提供数据层面的解法。  
```

## synthetic-data-generation-&-multi-step-rl-for-reasoning-&-tool-use
### Abstract
Reinforcement learning has been shown to improve the performance of large
language models. However, traditional approaches like RLHF or RLAIF treat the
problem as single-step. As focus shifts toward more complex reasoning and
agentic tasks, language models must take multiple steps of text generation,
reasoning and environment interaction before generating a solution. We propose
a synthetic data generation and RL methodology targeting multi-step
optimization scenarios. This approach, called Step-Wise Reinforcement Learning
(SWiRL), iteratively generates multi-step reasoning and tool use data, and then
learns from that data. It employs a simple step-wise decomposition that breaks
each multi-step trajectory into multiple sub-trajectories corresponding to each
action by the original model. It then applies synthetic data filtering and RL
optimization on these sub-trajectories. We evaluated SWiRL on a number of
multi-step tool use, question answering, and mathematical reasoning tasks. Our
experiments show that SWiRL outperforms baseline approaches by 21.5%, 12.3%,
14.8%, 11.1%, and 15.3% in relative accuracy on GSM8K, HotPotQA, CofCA,
MuSiQue, and BeerQA, respectively. Excitingly, the approach exhibits
generalization across tasks: for example, training only on HotPotQA (text
question-answering) improves zero-shot performance on GSM8K (a math dataset) by
a relative 16.9%.
```
### 🌟 论文解读 | 多步骤推理与工具使用：合成数据生成与分步强化学习新范式

### 📌 背景痛点/本文动机
强化学习（RL）在提升大语言模型性能方面已被证实有效，然而传统的RLHF（基于人类反馈的强化学习）或RLAIF（基于人工反馈的强化学习）等方法多聚焦于“单步决策”场景。随着研究重心向更复杂的推理任务、智能体任务转移，语言模型需要在生成最终解决方案前，完成多轮文本生成、推理以及与环境的交互。这种“多步骤”场景下，传统单步RL范式的局限性逐渐凸显——无法高效处理多轮决策链条中的优化问题。因此，如何为多步骤优化场景设计更适配的强化学习方法，成为推动复杂任务能力突破的关键方向。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出分步强化学习（SWiRL）框架  
SWiRL瞄准多步骤优化场景，采用“迭代生成多步骤推理与工具使用数据 + 从数据中学习”的双阶段思路。它将完整的多步骤轨迹（trajectory）拆解为**多个子轨迹**，每个子轨迹对应原始模型在某一步的行动决策；在此基础上，对这些子轨迹开展合成数据过滤与RL优化，让模型在多轮决策中逐步学习最优策略。

💡 创新点2：合成数据生成与子轨迹分解机制  
为了让模型在多步骤任务中充分学习，SWiRL设计了“分步分解”策略：把一条完整的多步骤交互过程拆分成若干子轨迹，每个子轨迹都能独立承载“决策 - 反馈”的学习信号。同时，配合**合成数据过滤**机制，确保用于训练的数据质量，让模型在多步骤推理、工具调用等环节中更高效地吸收有效信息，避免噪声干扰。

### 📈 实验结果
论文在多类多步骤任务（工具使用、问答、数学推理）中验证了SWiRL的效果：  
- 在数学推理任务GSM8K、多跳问答HotPotQA、CofCA、MuSiQue、BeerQA上，SWiRL相对基线方法的准确率分别提升21.5%、12.3%、14.8%、11.1%、15.3%；  
- 跨任务泛化能力突出：仅在文本问答任务HotPotQA上训练，就能让模型在数学数据集GSM8K的零样本（zero - shot）表现提升16.9%，展现了方法在任务迁移上的潜力。

### 💬 可借鉴之处
1. 多步骤任务的分解思路：面对复杂的多轮决策或交互型任务，将长轨迹拆分为子轨迹的“分步优化”思路，为处理链条式、阶段式的AI任务提供了模块化解决范式；  
2. 合成数据与RL的结合：通过合成数据生成 + 过滤的方式扩充优质训练素材，再结合强化学习优化，为数据稀缺或标注成本高的多步骤场景提供了高效的“数据 - 算法”协同思路；  
3. 跨任务泛化的启发：SWiRL展现的跨任务迁移能力，提示我们在设计训练方案时，可更关注任务间的底层推理逻辑共性，为通用智能体的训练提供了方向参考。  
```

## visualsphinx--large-scale-synthetic-vision-logic-puzzles-for-rl
### Abstract
Vision language models (VLMs) are expected to perform effective multimodal
reasoning and make logically coherent decisions, which is critical to tasks
such as diagram understanding and spatial problem solving. However, current VLM
reasoning lacks large-scale and well-structured training datasets. To bridge
this gap, we propose VisualSphinx, a first-of-its-kind large-scale synthetic
visual logical reasoning training data. To tackle the challenge of image
synthesis with grounding answers, we propose a rule-to-image synthesis
pipeline, which extracts and expands puzzle rules from seed questions and
generates the code of grounding synthesis image synthesis for puzzle sample
assembly. Experiments demonstrate that VLM trained using GRPO on VisualSphinx
benefit from logical coherence and readability of our dataset and exhibit
improved performance on logical reasoning tasks. The enhanced reasoning
capabilities developed from VisualSphinx also benefit other reasoning tasks
such as algebraic reasoning, arithmetic reasoning and geometry reasoning.
```
### 🌟 论文解读 | VisualSphinx：为强化学习打造大规模合成视觉逻辑谜题数据集

### 📌 背景痛点/本文动机
视觉语言模型（VLMs）需要具备高效的多模态推理能力与逻辑连贯决策能力，这对图表理解、空间问题解决等任务至关重要。然而，当前VLM推理领域缺少大规模且结构良好的训练数据集，限制了模型在逻辑推理任务上的性能提升。为填补这一空白，论文提出构建VisualSphinx这一大规模合成视觉逻辑推理训练数据，助力VLM在多模态逻辑推理方向的发展。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出VisualSphinx大规模合成数据集  
作为首个该类大规模合成视觉逻辑推理训练数据，VisualSphinx致力于为VLM提供充足且高质量的逻辑推理训练素材，覆盖视觉与逻辑结合的多样场景，支撑模型学习多模态下的逻辑推理模式。  

💡 创新点2：规则到图像的合成 pipeline  
面对带基础答案的图像合成挑战，设计了从种子问题中提取并扩展谜题规则，再生成用于谜题样本组装的基础合成图像代码的 pipeline。该流程实现了从抽象规则到具象图像及对应逻辑关系的转化，保障数据生成的逻辑性与一致性，为模型提供“可解释、有依据”的视觉 - 逻辑训练样本。  

### 📈 实验结果
实验表明，使用GRPO在VisualSphinx上训练的VLM，受益于数据集的逻辑连贯性与可读性，在逻辑推理任务上表现出性能提升。并且，在VisualSphinx上培养的增强推理能力，还能迁移到代数推理、算术推理、几何推理等其他推理任务中，展现了该数据集在多维度推理能力提升上的价值。  

### 💬 可借鉴之处
从数据构建角度，针对多模态逻辑推理场景，通过“规则 - 图像”合成 pipeline 生成大规模带逻辑关联数据的思路，为领域定制化数据创建提供了范式，可启发后续在医疗影像推理、工程图纸理解等垂直场景的数据集构建；从模型训练角度，验证了高质量合成数据对多模态模型推理能力的提升作用，以及能力迁移特性，为多任务学习、跨领域推理模型训练提供了数据层面的借鉴方向，让研究者重视合成数据在弥补真实数据缺口、定向增强模型能力上的潜力。
```

