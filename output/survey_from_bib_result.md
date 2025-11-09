# Paper List from BIB File: tmpou7by98y.bib
- [25/09] **ToolRM: Outcome Reward Models for Tool-Calling Large Language Models**  
[[Paper](http://arxiv.org/pdf/2509.11963v1)] [[Code/Page]()] [[TLDR/Notes](#toolrm--outcome-reward-models-for-tool-calling-large-language-models)]

- [25/10] **Synthesizing Agentic Data for Web Agents with Progressive Difficulty Enhancement Mechanisms**  
[[Paper](http://arxiv.org/pdf/2510.13913v1)] [[Code/Page]()] [[TLDR/Notes](#synthesizing-agentic-data-for-web-agents-with-progressive-difficulty-enhancement-mechanisms)]

- [25/10] **DeepAnalyze: Agentic Large Language Models for Autonomous Data Science**  
[[Paper](http://arxiv.org/pdf/2510.16872v1)] [[Code/Page]()] [[TLDR/Notes](#deepanalyze--agentic-large-language-models-for-autonomous-data-science)]

- [25/10] **Explore to Evolve: Scaling Evolved Aggregation Logic via Proactive Online Exploration for Deep Research Agents**  
[[Paper](http://arxiv.org/pdf/2510.14438v1)] [[Code/Page]()] [[TLDR/Notes](#explore-to-evolve--scaling-evolved-aggregation-logic-via-proactive-online-exploration-for-deep-research-agents)]

- [25/02] **Leveraging Large Language Models for Effective and Explainable Multi-Agent Credit Assignment**  
[[Paper](http://arxiv.org/pdf/2502.16863v1)] [[Code/Page]()] [[TLDR/Notes](#leveraging-large-language-models-for-effective-and-explainable-multi-agent-credit-assignment)]

- [24/10] **ToolFlow: Boosting LLM Tool-Calling Through Natural and Coherent Dialogue Synthesis**  
[[Paper](http://arxiv.org/pdf/2410.18447v2)] [[Code/Page]()] [[TLDR/Notes](#toolflow--boosting-llm-tool-calling-through-natural-and-coherent-dialogue-synthesis)]

- [25/04] **APIGen-MT: Agentic Pipeline for Multi-Turn Data Generation via Simulated Agent-Human Interplay**  
[[Paper](http://arxiv.org/pdf/2504.03601v4)] [[Code/Page](https://huggingface.co/collections/Salesforce/xlam-2-67ef5be12949d8dcdae354c4;)] [[TLDR/Notes](#apigen-mt--agentic-pipeline-for-multi-turn-data-generation-via-simulated-agent-human-interplay)]

- [24/09] **ToolACE: Winning the Points of LLM Function Calling**  
[[Paper](http://arxiv.org/pdf/2409.00920v2)] [[Code/Page](https://huggingface.co/Team-ACE.)] [[TLDR/Notes](#toolace--winning-the-points-of-llm-function-calling)]

- [25/10] **TOUCAN: Synthesizing 1.5M Tool-Agentic Data from Real-World MCP Environments**  
[[Paper](http://arxiv.org/pdf/2510.01179v1)] [[Code/Page]()] [[TLDR/Notes](#toucan--synthesizing-1-5m-tool-agentic-data-from-real-world-mcp-environments)]

- [25/05] **AutoData: A Multi-Agent System for Open Web Data Collection**  
[[Paper](http://arxiv.org/pdf/2505.15859v1)] [[Code/Page](https://github.com/GraphResearcher/AutoData.)] [[TLDR/Notes](#autodata--a-multi-agent-system-for-open-web-data-collection)]

- [25/10] **Agent Data Protocol: Unifying Datasets for Diverse, Effective Fine-tuning of LLM Agents**  
[[Paper](http://arxiv.org/pdf/2510.24702v1)] [[Code/Page]()] [[TLDR/Notes](#agent-data-protocol--unifying-datasets-for-diverse--effective-fine-tuning-of-llm-agents)]

- [25/08] **Cognitive Kernel-Pro: A Framework for Deep Research Agents and Agent Foundation Models Training**  
[[Paper](http://arxiv.org/pdf/2508.00414v2)] [[Code/Page](https://github.com/Tencent/CognitiveKernel-Pro)] [[TLDR/Notes](#cognitive-kernel-pro--a-framework-for-deep-research-agents-and-agent-foundation-models-training)]



# TLDR/Notes
## toolrm--outcome-reward-models-for-tool-calling-large-language-models
### Abstract
As large language models (LLMs) increasingly interact with external tools,
reward modeling for tool use has become a critical yet underexplored area.
Existing reward models, trained primarily on natural language outputs, struggle
to evaluate tool-based reasoning and execution. To quantify this gap, we
introduce FC-RewardBench, the first benchmark designed to systematically assess
reward models' performance in tool-calling scenarios. Our analysis shows that
current reward models often miss key signals of effective tool use,
highlighting the need for domain-specific modeling. To address this, we propose
a training framework for outcome-based reward models using data synthesized
from permissively licensed, open-weight LLMs. We train models ranging from 1.7B
to 14B parameters and evaluate them across seven out-of-domain benchmarks.
These models consistently outperform general-purpose baselines, achieving up to
25\% average improvement in downstream task performance and enabling
data-efficient fine-tuning through reward-guided filtering.
```
### 🌟 论文解读 | ToolRM：开启大语言模型工具调用奖励建模新篇章

### 📌 背景痛点/本文动机
大语言模型（LLMs）在人工智能领域发展迅速，随着其在现实场景中应用的深入，与外部工具交互的需求日益增长，工具调用成为关键能力。奖励模型是训练和微调LLMs的核心组件，分为过程奖励模型和结果奖励模型，其中结果奖励模型因更易训练、可扩展性强等优势而被广泛应用。然而，现有的奖励模型主要基于自然语言输出进行训练，在评估基于工具的推理和执行方面存在不足，且缺乏专门的基准来系统评估工具调用场景下奖励模型的有效性，因此需要特定领域的奖励建模。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：引入FC - RewardBench
这是首个专门用于评估工具调用任务中奖励模型的综合基准，该基准数据集来自伯克利函数调用排行榜（BFCL）版本3，包含1500个独特的用户输入以及正确和不正确的函数调用，用于量化现有奖励模型在工具调用场景下的评估差距。
💡 创新点2：提出ToolRM及训练框架
ToolRM是一组专门用于工具调用的结果奖励模型。通过从多种开源函数调用模型合成的偏好数据进行训练，提出了使用许可授权的中等规模开放权重LLMs生成的数据来训练工具调用结果奖励模型的框架。训练了参数范围从1.7B到14B的多个模型，并在七个域外基准上进行评估。

### 📈 实验结果
在FC - RewardBench上，ToolRM优于许多更大的奖励模型和作为评判的LLMs。在下游应用中，在Best - of - n设置下，ToolRM在多个基准上平均提升高达25%，并且能够实现高效的数据过滤，使用更少的数据就能得到性能更好的微调模型。

### 💬 可借鉴之处
1. **基准构建**：FC - RewardBench的构建为评估工具调用场景下的奖励模型提供了新的标准和方法，对于其他相关研究在设计评估基准方面具有借鉴意义。
2. **模型训练**：利用许可授权的开放权重LLMs生成数据来训练特定领域奖励模型的方式，为解决缺乏针对性训练数据的问题提供了新的思路。
3. **性能提升**：ToolRM在下游任务中的性能提升以及数据过滤方面的优势，展示了特定领域奖励模型在优化大语言模型工具调用能力上的潜力，为后续研究提供了方向。
``` 

## synthesizing-agentic-data-for-web-agents-with-progressive-difficulty-enhancement-mechanisms
### Abstract
Web-based 'deep research' agents aim to solve complex question - answering
tasks through long-horizon interactions with online tools. These tasks remain
challenging, as the underlying language models are often not optimized for
long-horizon reasoning and exploration. Prior work has proposed workflows for
constructing instruction-tuning datasets, often leveraging knowledge graphs.
However, such methods typically lack fine-grained control over difficulty and
quality, yielding synthetic data that falls short of capturing the complexity
required for long-horizon reasoning. Furthermore, many studies conflate data
and training effects by comparing models trained under different optimization
recipes, making it difficult to isolate and evaluate the effectiveness of the
data itself. We introduce a two-pronged data synthesis pipeline that generates
question - answer pairs by progressively increasing task complexity until a
frontier baseline web agent fails. The baseline agent plays multiple roles in
this process: attempting the questions, validating factuality, checking for
alternative answers, and enforcing filtering. To evaluate the effectiveness of
our synthesis methods, we adopt a controlled training setup based on
distillation from strong web agents. Experiments across multiple web-based
benchmarks show that our dataset - despite being smaller - enables the training
of more effective web agents than existing datasets. In particular, our data
exhibits twice the diversity in tool-use actions, allowing models trained on it
to achieve stronger performance while avoiding repetitive tool-calling
behaviors.
```
### 🌟 论文解读 | 突破数据合成难题，助力网页智能体升级

### 📌 背景痛点/本文动机
基于网页的“深度研究”智能体旨在通过与在线工具的长期交互来解决复杂的问答任务，但底层语言模型往往未针对长期推理和探索进行优化，使得这些任务极具挑战性。先前构建指令微调数据集的方法通常缺乏对难度和质量的精细控制，合成的数据难以捕捉长期推理所需的复杂性。此外，许多研究将数据和训练效果混为一谈，难以单独评估数据本身的有效性。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出名为Progressive Search（ProgSearch）的双管齐下的数据合成管道，通过迭代细化生成问答对。采用自顶向下的方法，构建事实树，沿树分支逐步整合事实来合成问答对；同时采用自底向上的方法，以固定的稀有实体为基础事实锚点，通过混淆和事实融合生成更难的问题。
💡 创新点2：引入基线网页智能体在渐进细化过程中发挥多重作用，包括作为求解器衡量问题难度、作为提问者合成问答对、作为研究员从网页提取支持事实以及作为评估者确保事实准确性和符合约束条件。

### 📈 实验结果
通过基于从强大网页智能体蒸馏的受控训练设置来评估合成方法的有效性。在多个基于网页的基准测试中，尽管本文数据集规模较小，但与现有数据集相比，能够训练出更有效的网页智能体。在Qwen3 - 8B上增益高达8%，在Qwen2.5 - 7B上增益达23%。消融研究表明，本文数据中的轨迹包含的工具调用动作比先前数据集多4倍，体现了合成问答对更高的复杂性和推理深度。经过监督微调后，在本文合成数据上训练的检查点也展示出更多样化的工具使用，直接转化为更强的基准测试性能。

### 💬 可借鉴之处
论文提出的双管齐下的数据合成管道以及利用基线智能体进行难度控制和质量验证的方法，为构建高质量的指令微调数据集提供了新的思路。在研究数据合成对模型性能的影响时，采用的受控训练设置有助于更准确地评估数据本身的有效性，这种实验设计值得借鉴。
``` 

## deepanalyze--agentic-large-language-models-for-autonomous-data-science
### Abstract
Autonomous data science, from raw data sources to analyst-grade deep research
reports, has been a long-standing challenge, and is now becoming feasible with
the emergence of powerful large language models (LLMs). Recent workflow-based
data agents have shown promising results on specific data tasks but remain
fundamentally limited in achieving fully autonomous data science due to their
reliance on predefined workflows. In this paper, we introduce DeepAnalyze-8B,
the first agentic LLM designed for autonomous data science, capable of
automatically completing the end-toend pipeline from data sources to
analyst-grade deep research reports. To tackle high-complexity data science
tasks, we propose a curriculum-based agentic training paradigm that emulates
the learning trajectory of human data scientists, enabling LLMs to
progressively acquire and integrate multiple capabilities in real-world
environments. We also introduce a data-grounded trajectory synthesis framework
that constructs high-quality training data. Through agentic training,
DeepAnalyze learns to perform a broad spectrum of data tasks, ranging from data
question answering and specialized analytical tasks to open-ended data
research. Experiments demonstrate that, with only 8B parameters, DeepAnalyze
outperforms previous workflow-based agents built on most advanced proprietary
LLMs. The model, code, and training data of DeepAnalyze are open-sourced,
paving the way toward autonomous data science.
```
### 🌟 论文解读 | DeepAnalyze：开启自主数据科学新时代

### 📌 背景痛点/本文动机
自主数据科学旨在实现从原始数据源到分析师级深度研究报告的自动化，这一直是数据科学界长期追求的核心目标。然而，该过程涉及数据准备、分析、建模、可视化和报告生成等一系列复杂且相互依赖的任务，实现起来颇具挑战。尽管强大的大语言模型（LLMs）的出现使其变得可行，但LLMs在协调复杂的多阶段数据科学流程以及处理各种结构化数据方面仍存在困难。近期基于工作流的数据代理在特定数据任务上虽有不错表现，但因依赖预定义工作流，在实现完全自主的数据科学方面存在根本局限。

### 🚀 核心方法
💡 创新点1：提出DeepAnalyze - 8B
这是首个专为自主数据科学设计的代理型大语言模型，能够自动完成从数据源到分析师级深度研究报告的端到端流程。

💡 创新点2：提出基于课程的代理训练范式
该范式模仿人类数据科学家的学习轨迹，使大语言模型能够在现实世界环境中逐步获取并整合多种能力，以应对高复杂性的数据科学任务。

💡 创新点3：引入基于数据的轨迹合成框架
用于构建高质量的训练数据，助力DeepAnalyze通过代理训练学习执行从数据问答、专业分析任务到开放式数据研究等广泛的数据任务。

### 📈 实验结果
实验表明，仅拥有80亿参数的DeepAnalyze在性能上超越了先前基于最先进专有大语言模型构建的基于工作流的代理。

### 💬 可借鉴之处
1. **模型设计思路**：DeepAnalyze的设计为开发面向特定领域的大语言模型提供了新的思路，尤其是在需要整合多种能力以处理复杂任务的场景中。
2. **训练范式**：基于课程的代理训练范式模仿人类学习轨迹，为提升模型在复杂环境中的学习和适应能力提供了借鉴，可应用于其他需要模型逐步学习和成长的领域。
3. **数据构建框架**：基于数据的轨迹合成框架对于构建高质量训练数据具有重要参考价值，有助于解决在训练模型时数据质量不高的问题。
``` 

## explore-to-evolve--scaling-evolved-aggregation-logic-via-proactive-online-exploration-for-deep-research-agents
### Abstract
Deep research web agents not only retrieve information from diverse sources
such as web environments, files, and multimodal inputs, but more importantly,
they need to rigorously analyze and aggregate knowledge for insightful
research. However, existing open-source deep research agents predominantly
focus on enhancing information-seeking capabilities of web agents to locate
specific information, while overlooking the essential need for information
aggregation, which would limit their ability to support in-depth research. We
propose an Explore to Evolve paradigm to scalably construct verifiable training
data for web agents. Begins with proactive online exploration, an agent sources
grounded information by exploring the real web. Using the collected evidence,
the agent then self-evolves an aggregation program by selecting, composing, and
refining operations from 12 high-level logical types to synthesize a verifiable
QA pair. This evolution from high-level guidance to concrete operations allowed
us to scalably produce WebAggregatorQA, a dataset of 10K samples across 50K
websites and 11 domains. Based on an open-source agent framework, SmolAgents,
we collect supervised fine-tuning trajectories to develop a series of
foundation models, WebAggregator. WebAggregator-8B matches the performance of
GPT-4.1, while the 32B variant surpasses GPT-4.1 by more than 10% on GAIA-text
and closely approaches Claude-3.7-sonnet. Moreover, given the limited
availability of benchmarks that evaluate web agents' information aggregation
abilities, we construct a human-annotated evaluation split of WebAggregatorQA
as a challenging test set. On this benchmark, Claude-3.7-sonnet only achieves
28%, and GPT-4.1 scores 25.8%. Even when agents manage to retrieve all
references, they still struggle on WebAggregatorQA, highlighting the need to
strengthen the information aggregation capabilities of web agent foundations.
```
### 🌟 论文解读 | 探索进化：深度研究智能体的信息聚合新范式

### 📌 背景痛点/本文动机
深度研究网络智能体不仅要从网络环境、文件、多模态输入等多样来源检索信息，更重要的是需严格分析和聚合知识以开展有洞察力的研究。然而，现有的开源深度研究智能体主要聚焦于提升网络智能体定位特定信息的信息搜索能力，却忽视了信息聚合这一关键需求，这限制了它们支持深入研究的能力。同时，现有的多跳问答数据集很少涉及真实的网络交互，近期的网络智能体数据集在信息来源的动态性和复杂性以及对复杂聚合的需求方面存在不足。因此，促进和评估聚合能力是网络智能体研究中一个关键但尚未充分探索的挑战。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出Explore to Evolve方法
该方法采用“探索：主动在线网络探索”和“进化：自动聚合逻辑合成”，将整个任务组合过程视为智能体驱动的流水线。智能体配备先进的网络工具，支持搜索、静态解析、动态交互、文件处理和视觉输入等功能，以支持多样化的用户场景。在主动在线探索阶段，智能体通过探索实时网络收集资源语料库；在自动聚合逻辑合成阶段，智能体利用受多跳分析和逻辑推理研究启发的高级聚合逻辑分类法，将高级聚合指导实例化并进化为具体操作，构建基于探索知识的问答对。
💡 创新点2：构建WebAggregatorQA数据集
通过上述方法，可扩展地生成了WebAggregatorQA数据集，该数据集包含跨越50K个网站和11个领域的10K个样本。同时，构建了一个人工标注的评估分割作为具有挑战性的测试集，用于评估网络智能体的信息聚合能力。
💡 创新点3：开发WebAggregator模型系列
基于开源智能体框架SmolAgents，收集监督微调轨迹，开发了一系列基础模型WebAggregator。

### 📈 实验结果
WebAggregator - 8B在性能上与GPT - 4.1相当，而32B变体在GAIA - text上超过GPT - 4.1超过10%，并接近Claude - 3.7 - sonnet的性能。在构建的具有挑战性的WebAggregatorQA基准测试上，Claude - 3.7 - sonnet仅达到28%，GPT - 4.1得分为25.8%，即使智能体成功检索到所有参考文献，在WebAggregatorQA上仍面临困难，凸显了加强网络智能体基础信息聚合能力的必要性。

### 💬 可借鉴之处
1. **数据构建方法**：Explore to Evolve方法为构建涵盖多样化信息来源和复杂聚合需求的数据集提供了新思路，可应用于其他需要构建类似数据集的研究中。
2. **模型训练与评估**：基于开源框架收集监督微调轨迹开发模型，并构建专门的评估集来评估模型在信息聚合能力方面的表现，这种训练与评估方式有助于提升模型在特定任务上的性能和针对性。
3. **关注信息聚合**：强调了信息聚合能力在网络智能体研究中的重要性，提醒研究者在开发智能体时不能忽视这一关键能力的提升。 
``` 

## leveraging-large-language-models-for-effective-and-explainable-multi-agent-credit-assignment
### Abstract
Recent work, spanning from autonomous vehicle coordination to in-space
assembly, has shown the importance of learning collaborative behavior for
enabling robots to achieve shared goals. A common approach for learning this
cooperative behavior is to utilize the centralized-training
decentralized-execution paradigm. However, this approach also introduces a new
challenge: how do we evaluate the contributions of each agent's actions to the
overall success or failure of the team. This credit assignment problem has
remained open, and has been extensively studied in the Multi-Agent
Reinforcement Learning literature. In fact, humans manually inspecting agent
behavior often generate better credit evaluations than existing methods. We
combine this observation with recent works which show Large Language Models
demonstrate human-level performance at many pattern recognition tasks. Our key
idea is to reformulate credit assignment to the two pattern recognition
problems of sequence improvement and attribution, which motivates our novel
LLM-MCA method. Our approach utilizes a centralized LLM reward-critic which
numerically decomposes the environment reward based on the individualized
contribution of each agent in the scenario. We then update the agents' policy
networks based on this feedback. We also propose an extension LLM-TACA where
our LLM critic performs explicit task assignment by passing an intermediary
goal directly to each agent policy in the scenario. Both our methods far
outperform the state-of-the-art on a variety of benchmarks, including
Level-Based Foraging, Robotic Warehouse, and our new Spaceworld benchmark which
incorporates collision-related safety constraints. As an artifact of our
methods, we generate large trajectory datasets with each timestep annotated
with per-agent reward information, as sampled from our LLM critics.
```
### 🌟 论文解读 | 利用大语言模型实现高效且可解释的多智能体功劳分配

### 📌 背景痛点/本文动机
在自动驾驶车辆协调到太空装配等众多实际场景中，学习协作行为对于使机器人实现共同目标至关重要，多智能体强化学习（MARL）中的集中训练 - 分散执行（CTDE）范式常被用于学习这种协作行为。然而，在CTDE的中央训练阶段，一个关键挑战是如何分离每个策略变化的影响，并评估每个智能体对全局任务整体成功或失败的贡献，即 “功劳分配” 问题。传统上，环境仅根据智能体是否实现共享目标提供集体奖励，CTDE训练算法需从单一奖励中确定每个智能体的贡献并更新策略。该问题一直未得到很好解决，现有方法存在诸多局限，如反馈质量低、行动影响力低以及处理复杂交互困难等。同时，人类手动检查智能体行为往往能产生比现有方法更好的功劳评估，且近期研究表明大语言模型（LLMs）在许多模式识别任务中展现出人类水平的性能，基于此，论文作者希望利用LLMs来解决多智能体功劳分配问题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出LLM - MCA方法
将功劳分配重新表述为序列改进和归因这两个模式识别问题。利用集中式的LLM奖励 - 评论家，基于场景中每个智能体的个性化贡献，对环境奖励进行数值分解，然后根据此反馈更新智能体的策略网络。

💡 创新点2：提出LLM - TACA方法
作为LLM - MCA的扩展，其中LLM评论家通过将中间目标直接传递给场景中的每个智能体策略来执行显式任务分配。

### 📈 实验结果
在多种基准测试中，包括基于等级的觅食、机器人仓库以及新提出的纳入碰撞相关安全约束的 “Spaceworld” 基准测试，LLM - MCA和LLM - TACA这两种方法均远超当前最先进的方法。此外，作为方法的产物，生成了带有每个时间步长的每个智能体奖励信息注释的大型轨迹数据集，这些信息从LLM评论家中采样得到。

### 💬 可借鉴之处
1. **问题转换思路**：将功劳分配问题转换为模式识别问题，为解决多智能体协作中的复杂问题提供了新的视角和思路，启发研究者在面对类似难以解决的问题时，尝试从其他角度进行转换和思考。
2. **模型应用**：利用大语言模型的模式识别能力来处理多智能体结构功劳分配问题，展示了大语言模型在多智能体系统中的应用潜力，为其他相关研究在模型选择和应用上提供了参考。
3. **数据集贡献**：生成的带有详细注释的大型轨迹数据集可用于未来的离线训练，为后续研究提供了宝贵的数据资源，有助于推动多智能体协作策略离线训练相关研究的发展。
``` 

## toolflow--boosting-llm-tool-calling-through-natural-and-coherent-dialogue-synthesis
### Abstract
Supervised fine-tuning (SFT) is a common method to enhance the tool calling
capabilities of Large Language Models (LLMs), with the training data often
being synthesized. The current data synthesis process generally involves
sampling a set of tools, formulating a requirement based on these tools, and
generating the call statements. However, tools sampled randomly lack relevance,
making them difficult to combine and thus reducing the diversity of the data.
Additionally, current work overlooks the coherence between turns of dialogues,
leading to a gap between the synthesized data and real-world scenarios. To
address these issues, we propose a Graph-based Sampling strategy to sample more
relevant tool combinations, and a Planned-generation strategy to create plans
that guide the synthesis of coherent dialogues. We integrate these two
strategies and enable multiple agents to synthesize the dialogue data
interactively, resulting in our tool-calling data synthesis pipeline ToolFlow.
Data quality assessments demonstrate improvements in the naturalness and
coherence of our synthesized dialogues. Finally, we apply SFT on LLaMA-3.1-8B
using 8,000 synthetic dialogues generated with ToolFlow. Results show that the
model achieves tool-calling performance comparable to or even surpassing GPT-4,
while maintaining strong general capabilities.
```
### 🌟 论文解读 | ToolFlow：开启大语言模型工具调用新境界

### 📌 背景痛点/本文动机
大语言模型（LLMs）的工具调用能力提升常采用监督微调（SFT）方法，其训练数据多为合成所得。当前数据合成过程通常是采样一组工具、基于工具制定需求并生成调用语句。然而，随机采样的工具缺乏相关性，难以组合，降低了数据多样性；同时，现有工作忽视了对话轮次间的连贯性，导致合成数据与现实场景存在差距。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：基于图的采样策略（Graph - based Sampling strategy）
考虑参数或返回值相似的工具为相关工具，构建工具图，图中节点代表工具，边表示工具对之间的相关性。采样工具时，从工具图中随机选择子图，使采样工具更易有效交互，便于生成复杂需求，提升合成工具调用需求的多样性和复杂性。
💡 创新点2：规划生成策略（Planned - Generation strategy）
在合成对话前，让LLM基于选定的工具子集创建计划，该计划勾勒出用户在对话每一轮需提出的请求。模型构建计划时专注于建立对话框架，还可将非工具调用请求纳入计划，增强对话内容多样性，促进话题间无缝过渡，提高合成对话的自然性和连贯性。

### 📈 实验结果
通过有选择地生成无相关模块的相同规模对话，对基于图的采样和规划策略进行全面消融研究。对数据质量进行评估，结果表明ToolFlow能有效提升生成对话的自然性、连贯性和多样性。使用ToolFlow生成的8000个合成对话对LLaMA - 3.1 - 8B进行监督微调，模型在保持强大通用能力的同时，工具调用性能可媲美甚至超越GPT - 4。

### 💬 可借鉴之处
在大语言模型工具调用训练数据合成方面，基于图的采样策略为选择相关工具提供了新的思路，有助于提高合成数据的多样性和复杂性；规划生成策略对于提升合成对话的自然性和连贯性效果显著，这些方法和策略为后续相关研究和实践提供了有益参考，可用于改进大语言模型工具调用能力的训练过程。
``` 

## apigen-mt--agentic-pipeline-for-multi-turn-data-generation-via-simulated-agent-human-interplay
### Abstract
Training effective AI agents for multi-turn interactions requires
high-quality data that captures realistic human-agent dynamics, yet such data
is scarce and expensive to collect manually. We introduce APIGen-MT, a
two-phase framework that generates verifiable and diverse multi-turn agent
data. In the first phase, our agentic pipeline produces detailed task
blueprints with ground-truth actions, leveraging a committee of LLM reviewers
and iterative feedback loops. These blueprints are then transformed into
complete interaction trajectories through simulated human-agent interplay. We
train a family of models -- the xLAM-2-fc-r series with sizes ranging from 1B
to 70B parameters. Our models outperform frontier models such as GPT-4o and
Claude 3.5 on $\tau$-bench and BFCL benchmarks, with the smaller models
surpassing their larger counterparts, particularly in multi-turn settings,
while maintaining superior consistency across multiple trials. Comprehensive
experiments demonstrate that our verified blueprint-to-details approach yields
high-quality training data, enabling the development of more reliable,
efficient, and capable agents. We open-source 5K synthetic data trajectories
and the trained xLAM-2-fc-r models to advance research in AI agents.
  Models at
https://huggingface.co/collections/Salesforce/xlam-2-67ef5be12949d8dcdae354c4;
Dataset at https://huggingface.co/datasets/Salesforce/APIGen-MT-5k and Website
at https://apigen-mt.github.io
```
### 🌟 论文解读 | APIGen - MT：开启多轮对话数据生成新征程

### 📌 背景痛点/本文动机
随着大语言模型（LLM）代理在各行业需求的增长，其角色已从简单聊天机器人拓展到能执行现实任务的智能体。然而，训练有效的多轮交互 AI 代理需要高质量数据来捕捉真实的人机动态，但此类数据在公共预训练语料库中稀缺，且手动收集和标注成本高昂、耗时。现有方法如 APIGen 主要关注单轮交互，无法体现现实中多轮交互的复杂性，其他涉及多轮方面的方法又缺乏人机交互，高质量多轮轨迹的验证和合成仍是难题，这严重阻碍了代理能力的提升。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出 APIGen - MT 代理数据合成管道，利用环境执行反馈和评审委员会确保生成的多轮代理数据的高质量。
💡 创新点2：开发两阶段框架。第一阶段，数据代理利用 LLM 评审委员会和迭代反馈循环生成带有真实动作的详细任务 “蓝图”，包括采样相关 API、政策、领域数据和用户角色以创建有根据的通用任务配置，并使用反向任务重组增强复杂性，通过格式/执行检查和基于反射机制的 LLM 委员会审查来验证蓝图；第二阶段，验证后的蓝图通过模拟人机交互引导生成现实的多轮对话代理轨迹，产生包含对话、动作和环境反馈的完整交互轨迹用于训练。

### 📈 实验结果
训练了一系列参数规模从 1B 到 70B 的 xLAM - 2 - fc - r 模型。在 τ - bench 和 BFCL 基准测试中，这些模型优于 GPT - 4o 和 Claude 3.5 等前沿模型，较小的模型在多轮设置中尤其超越了较大的模型，同时在多次试验中保持了卓越的一致性。

### 💬 可借鉴之处
1. **数据生成方法**：APIGen - MT 的两阶段数据生成框架为解决高质量多轮代理数据稀缺问题提供了新的思路，其利用 LLM 评审委员会和迭代反馈循环生成任务蓝图的方式，以及通过模拟人机交互生成完整交互轨迹的方法，可启发其他研究在数据生成方面的探索。
2. **模型训练与性能提升**：训练的 xLAM - 2 - fc - r 系列模型在基准测试中的出色表现表明，使用高质量合成数据能够有效提升模型在多轮交互任务中的性能，对于追求模型性能提升的研究具有借鉴意义。
3. **开源贡献**：开源 5K 高质量合成数据（APIGen - MT - 5k）和训练好的 xLAM - 2 - fc - r 系列模型，为 AI 代理领域的研究提供了宝贵的资源，促进了该领域的研究发展，这种开源精神值得学习和推广。
``` 

## toolace--winning-the-points-of-llm-function-calling
### Abstract
Function calling significantly extends the application boundary of large
language models, where high-quality and diverse training data is critical for
unlocking this capability. However, real function-calling data is quite
challenging to collect and annotate, while synthetic data generated by existing
pipelines tends to lack coverage and accuracy. In this paper, we present
ToolACE, an automatic agentic pipeline designed to generate accurate, complex,
and diverse tool-learning data. ToolACE leverages a novel self-evolution
synthesis process to curate a comprehensive API pool of 26,507 diverse APIs.
Dialogs are further generated through the interplay among multiple agents,
guided by a formalized thinking process. To ensure data accuracy, we implement
a dual-layer verification system combining rule-based and model-based checks.
We demonstrate that models trained on our synthesized data, even with only 8B
parameters, achieve state-of-the-art performance on the Berkeley
Function-Calling Leaderboard, rivaling the latest GPT-4 models. Our model and a
subset of the data are publicly available at https://huggingface.co/Team-ACE.
```
### 🌟 论文解读 | ToolACE：解锁大语言模型函数调用新高度

### 📌 背景痛点/本文动机
大语言模型（LLMs）中函数调用极大地拓展了其应用边界，高质量且多样的训练数据对于解锁这一能力至关重要。然而，收集和标注真实的函数调用数据颇具挑战，现有的合成数据生成管道产生的数据往往缺乏覆盖范围和准确性。当前工具增强的LLMs主要聚焦于简单的函数调用任务，多样性和复杂性有限，且依赖现有公共API进行任务构建，限制了零样本能力和对复杂场景（如依赖或多轮交互）的适用性。因此，需要一种新的方法来生成准确、多样且复杂的函数调用数据。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：Tool Self - Evolution Synthesis（TSS）模块
提出一种工具自我进化合成方法，通过物种形成、适应和进化三个步骤，生成具有多种数据类型和约束的API定义。该方法不依赖公共API，从预训练数据出发，通过迭代的自我进化和持续更新，扩展API池的多样性，建立了一个包含26,507个多样API的全面API池，在数量和领域覆盖上超越其他代表性工具增强LLMs。

💡 创新点2：Self - Guided Dialog Generation（SDG）模块
提出自我引导对话生成过程，让LLM作为评估器来调节复杂性。通过多智能体交互，遵循自我引导复杂化策略，生成四种类型的函数调用数据，使指令跟随数据具备足够的复杂性以培养函数调用技能。

💡 创新点3：Dual - Layer Validation Process（DLV）模块
采用双层验证系统，集成基于规则和基于模型的检查器，以保证合成数据的可执行性和一致性，确保数据准确性。

### 📈 实验结果
在BFCL和APIBank两个广泛采用的基准上进行实验，仅8B参数的模型在ToolACE合成数据上训练后，显著优于现有开源LLMs，性能可与最新的GPT - 4模型相媲美。

### 💬 可借鉴之处
1. **数据生成方法**：ToolACE的自动化数据生成管道为解决函数调用数据缺乏的问题提供了新的思路，其自我进化合成、自我引导对话生成和双层验证的方法可用于生成高质量、多样化和复杂的数据，对其他类似的数据生成任务有借鉴意义。
2. **复杂性调节**：利用LLM作为复杂性评估器来引导生成数据的复杂性，这种自我引导的方式有助于生成更符合模型学习需求的数据，可应用于其他需要调节数据复杂性的场景。
3. **多智能体协作**：通过多智能体交互生成对话数据，展示了多智能体协作在构建复杂数据方面的潜力，为相关研究提供了新的协作模式参考。
``` 

## toucan--synthesizing-1-5m-tool-agentic-data-from-real-world-mcp-environments
### Abstract
Large Language Model (LLM) agents are rapidly emerging as powerful systems
for automating tasks across domains. Yet progress in the open-source community
is constrained by the lack of high quality permissively licensed tool-agentic
training data. Existing datasets are often limited in diversity, realism, and
complexity, particularly regarding multi-tool and multi-turn interactions. To
address this gap, we introduce Toucan, the largest publicly available
tool-agentic dataset to date, containing 1.5 million trajectories synthesized
from nearly 500 real-world Model Context Protocols (MCPs). Unlike prior work,
Toucan leverages authentic MCP environments to generate diverse, realistic, and
challenging tasks with trajectories involving real tool execution. Our pipeline
first produces a broad spectrum of tool-use queries using five distinct models,
applies model-based quality filtering, and then generates agentic trajectories
with three teacher models using two agentic frameworks. Rigorous rule-based and
model-based validation ensures high-quality outputs. We also introduce three
extension mechanisms to further diversify tasks and simulate multi-turn
conversations. Models fine-tuned on Toucan outperform larger closed-source
counterparts on the BFCL V3 benchmark and push the Pareto frontier forward on
MCP-Universe Bench.
```
### 🌟 论文解读 | TOUCAN：开启工具 - 代理数据新时代

### 📌 背景痛点/本文动机
大语言模型（LLM）代理正迅速成为跨领域自动化任务的强大系统，但开源社区的发展受到缺乏高质量、许可宽松的工具 - 代理训练数据的限制。现有数据集在多样性、真实性和复杂性方面往往存在局限，特别是在多工具和多轮交互方面。目前急需能够涵盖生产环境中工具 - 代理完整交互范围的高质量数据集。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建大规模真实数据集
TOUCAN是目前最大的公开可用工具 - 代理数据集，包含从近500个真实世界的模型上下文协议（MCP）中合成的150万条轨迹。与先前依赖模拟或有限工具集的方法不同，TOUCAN利用具有2000多种工具的真实MCP环境，生成涵盖并行和多步骤工具调用以及多轮对话的多样化、现实且具有挑战性的任务。

💡 创新点2：独特的数据生成与筛选流程
数据生成管道首先使用五个不同模型生成广泛的工具使用查询，应用基于模型的质量过滤以确保相关性和难度；然后使用三个教师模型和两个代理框架生成代理轨迹，并通过严格的基于规则和基于模型的验证来确保高质量输出，包括验证工具执行和响应准确性；还引入了三种扩展机制，以进一步使任务多样化并模拟多轮对话。

### 📈 实验结果
在BFCL V3基准测试中，在TOUCAN上微调的模型优于更大的闭源模型，在单轮和多轮场景中的函数调用准确性方面表现出色；在τ - Bench和τ² - Bench上，在工具选择、执行保真度和动态用户交互下的多轮推理方面有显著改进；在MCP - Universe基准测试中，TOUCAN微调的模型在其参数类别中实现了最先进的性能，始终优于可比规模的领先模型。

### 💬 可借鉴之处
1. **数据集构建思路**：利用真实环境生成数据，为构建高质量、大规模且具有多样性的数据集提供了新的思路，有助于解决训练数据缺乏真实性和多样性的问题。
2. **数据生成与筛选流程**：多阶段的数据生成和严格的验证流程，保证了数据的质量和相关性，这种流程设计可应用于其他类似的数据生成任务中。
3. **模型微调效果**：在TOUCAN上微调模型的良好表现，证明了该数据集对提升模型在工具 - 代理任务中的性能具有显著作用，为模型训练提供了优质的数据资源参考。
``` 

## autodata--a-multi-agent-system-for-open-web-data-collection
### Abstract
The exponential growth of data-driven systems and AI technologies has
intensified the demand for high-quality web-sourced datasets. While existing
datasets have proven valuable, conventional web data collection approaches face
significant limitations in terms of human effort and scalability. Current
data-collecting solutions fall into two categories: wrapper-based methods that
struggle with adaptability and reproducibility, and large language model
(LLM)-based approaches that incur substantial computational and financial
costs. To address these challenges, we propose AutoData, a novel multi-agent
system for Automated web Data collection, that requires minimal human
intervention, i.e., only necessitating a natural language instruction
specifying the desired dataset. In addition, AutoData is designed with a robust
multi-agent architecture, featuring a novel oriented message hypergraph
coordinated by a central task manager, to efficiently organize agents across
research and development squads. Besides, we introduce a novel hypergraph cache
system to advance the multi-agent collaboration process that enables efficient
automated data collection and mitigates the token cost issues prevalent in
existing LLM-based systems. Moreover, we introduce Instruct2DS, a new benchmark
dataset supporting live data collection from web sources across three domains:
academic, finance, and sports. Comprehensive evaluations over Instruct2DS and
three existing benchmark datasets demonstrate AutoData's superior performance
compared to baseline methods. Case studies on challenging tasks such as picture
book collection and paper extraction from surveys further validate its
applicability. Our source code and dataset are available at
https://github.com/GraphResearcher/AutoData.
```
### 🌟 论文解读 | AutoData：开启自动网络数据收集新时代

### 📌 背景痛点/本文动机
数据是现代以数据为中心的智能系统的驱动力，高质量的网络源数据集需求日益增长。万维网成为大规模数据获取的默认来源，已有网络源数据推动了多领域研究。然而，传统网络数据收集方法存在显著局限：基于包装器的方法适应性和可重复性差；基于大语言模型（LLM）的方法计算和财务成本高。此外，缺乏用于评估开放网络数据收集任务模型性能的基准数据集，现有相关基准数据集多基于静态和存档网页，无法测试开放网络数据收集。因此，需要构建一个端到端的全自动开放网络数据收集系统，以兼顾覆盖范围、准确性和效率。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：新颖的多智能体系统
开发了全自动多智能体系统AutoData，由八个专业智能体和新颖的有向超图缓存系统（OHCache）组成。AutoData在中央任务管理器（MGR）下协调研究和开发两个专业智能体小组。研究小组的智能体根据输入指令浏览网页生成开发蓝图，开发小组则将蓝图转化为可执行代码并运行获取所需数据集。OHCache包括有向消息超图（将智能体间消息流建模为有向超边）、有向超边格式化器（强制结构化通信模式和超边消息积累）和本地缓存系统（存储可重用工件供智能体按需检索），以实现高效的多智能体协作。
💡 创新点2：新的基准数据集
引入新收集的基准数据集Instruct2DS，这是首个用于评估开放网络数据收集任务模型性能的基准数据集，涵盖学术、金融和体育三个领域，支持从网络源进行实时数据收集。

### 📈 实验结果
在Instruct2DS和三个现有基准数据集（SWDE、EXTENDED WSDE和HUMANEVAL）上对AutoData和基线方法进行了全面实验。结果表明，AutoData在开放网络数据收集任务中表现出优于基线方法的性能，证明了其有效性、效率和适用性。此外，针对如绘本收集和调查论文提取等具有挑战性的任务进行的案例研究，进一步验证了其适用性和即插即用的适应性。

### 💬 可借鉴之处
1. **多智能体协作模式**：AutoData的多智能体协作框架为解决复杂的数据收集任务提供了新的思路，可应用于其他需要多智能体协同的场景，如复杂的信息检索、自动化软件开发等。
2. **缓存系统设计**：OHCache的设计有效降低了基于LLM方法的令牌成本问题，对于在资源受限情况下提高系统效率具有借鉴意义，可应用于其他依赖大语言模型且对成本敏感的应用中。
3. **基准数据集构建**：Instruct2DS的构建为评估开放网络数据收集任务模型提供了标准，对于其他新兴研究领域，构建针对性的基准数据集有助于推动该领域的研究进展和模型性能评估。
``` 

## agent-data-protocol--unifying-datasets-for-diverse--effective-fine-tuning-of-llm-agents
### Abstract
Public research results on large-scale supervised finetuning of AI agents
remain relatively rare, since the collection of agent training data presents
unique challenges. In this work, we argue that the bottleneck is not a lack of
underlying data sources, but that a large variety of data is fragmented across
heterogeneous formats, tools, and interfaces. To this end, we introduce the
agent data protocol (ADP), a light-weight representation language that serves
as an "interlingua" between agent datasets in diverse formats and unified agent
training pipelines downstream. The design of ADP is expressive enough to
capture a large variety of tasks, including API/tool use, browsing, coding,
software engineering, and general agentic workflows, while remaining simple to
parse and train on without engineering at a per-dataset level. In experiments,
we unified a broad collection of 13 existing agent training datasets into ADP
format, and converted the standardized ADP data into training-ready formats for
multiple agent frameworks. We performed SFT on these data, and demonstrated an
average performance gain of ~20% over corresponding base models, and delivers
state-of-the-art or near-SOTA performance on standard coding, browsing, tool
use, and research benchmarks, without domain-specific tuning. All code and data
are released publicly, in the hope that ADP could help lower the barrier to
standardized, scalable, and reproducible agent training.
```
### 🌟 论文解读 | ADP：开启大语言模型智能体训练标准化新时代

### 📌 背景痛点/本文动机
大语言模型（LLMs）的预训练得益于丰富的互联网规模数据，但后训练阶段获取高质量特定任务数据面临挑战，尤其是在智能体应用场景中。智能体需采取顺序行动并与世界迭代交互，构建此类场景的数据集需记录和构建智能体行为轨迹，比收集静态输入 - 输出对困难得多。尽管已有多种创建智能体数据集的方法且数据集涵盖广泛任务，但大规模监督微调（SFT）在学术研究中仍较为罕见。原因并非缺乏数据，而是现有数据集格式和表示不一致，碎片化严重，难以有效组合、共享和利用。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出智能体数据协议（ADP）
ADP是一种轻量级表示语言，作为不同格式的智能体数据集与统一的下游智能体训练管道之间的“中间语言”。它以Pydantic模式实现，表达对应常见智能体用例（如通信、浏览、编码和各种工具调用）的行动和观察，并通过严格的自动验证维持高数据质量。

💡 创新点2：实现数据集转换与构建
实现了将13个现有数据集转换为ADP格式的转换器，以及从ADP到3种不同智能体架构的转换器，展示了其通用性。基于此创建并发布了最大的公开可用智能体训练数据集ADP Dataset V1，包含130万个训练轨迹。

### 📈 实验结果
使用ADP训练智能体在多个领域带来显著性能提升，包括编码（SWE - Bench Verified）、网页浏览（WebArena）、研究（GAIA）和智能体工具使用（AgentBench）等，平均性能比相应基础模型提高约20%，在标准基准测试中达到或接近当前最优水平。同时，跨任务迁移也有显著收益，在ADP数据上训练比在单个数据集上训练有明显改进。此外，ADP还支持系统的跨数据集分析，揭示公开可用数据的趋势和改进方向。

### 💬 可借鉴之处
ADP为智能体训练数据的标准化提供了有效解决方案，降低了大规模监督智能体训练的门槛，使其更具实用性和可扩展性。其通用的转换机制和高质量的数据表示方式，对于整合和利用多样化的智能体数据集具有重要参考价值。此外，公开代码和数据集的做法有助于社区的采用和新数据集的贡献，推动智能体模型微调的进一步发展。
``` 

## cognitive-kernel-pro--a-framework-for-deep-research-agents-and-agent-foundation-models-training
### Abstract
General AI Agents are increasingly recognized as foundational frameworks for
the next generation of artificial intelligence, enabling complex reasoning, web
interaction, coding, and autonomous research capabilities. However, current
agent systems are either closed-source or heavily reliant on a variety of paid
APIs and proprietary tools, limiting accessibility and reproducibility for the
research community. In this work, we present \textbf{Cognitive Kernel-Pro}, a
fully open-source and (to the maximum extent) free multi-module agent framework
designed to democratize the development and evaluation of advanced AI agents.
Within Cognitive Kernel-Pro, we systematically investigate the curation of
high-quality training data for Agent Foundation Models, focusing on the
construction of queries, trajectories, and verifiable answers across four key
domains: web, file, code, and general reasoning. Furthermore, we explore novel
strategies for agent test-time reflection and voting to enhance agent
robustness and performance. We evaluate Cognitive Kernel-Pro on GAIA, achieving
state-of-the-art results among open-source and free agents. Notably, our
8B-parameter open-source model surpasses previous leading systems such as
WebDancer and WebSailor, establishing a new performance standard for
accessible, high-capability AI agents. Code is available at
https://github.com/Tencent/CognitiveKernel-Pro
```
### 🌟 论文解读 | Cognitive Kernel - Pro：开启开源智能体研究新征程

### 📌 背景痛点/本文动机
通用人工智能体正逐渐成为下一代人工智能的基础框架，具备复杂推理、网页交互、编码和自主研究等能力。然而，当前的智能体系统要么是闭源的，要么严重依赖各种付费API和专有工具，这限制了研究社区的可访问性和可重复性。为了解决这一问题，论文提出了Cognitive Kernel - Pro，一个完全开源且（尽可能）免费的多模块智能体框架，旨在推动先进人工智能体的开发和评估的民主化。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：开源多模块智能体框架
提出Cognitive Kernel - Pro框架，采用两层多模块架构，由负责任务分解、子任务委派和信息聚合等的主智能体，以及解决主智能体分配的子任务的多个子智能体组成。主智能体和子智能体都继承自同一基类，输入为任务字符串，输出为响应字符串，中间动作以Python代码形式执行。该框架以Python代码作为动作空间，充分利用现代大语言模型的推理和代码生成潜力，强调智能体基础模型的内在能力，减少对专有工具的依赖。

💡 创新点2：全面的训练方法
引入针对Cognitive Kernel - Pro的全面训练方法，涵盖网页导航、文件处理、代码生成和推理等多个领域。构建可验证的智能体查询 - 答案对，确保高质量的训练数据。通过纳入中间过程提示和基于提示的拒绝采样来增强数据收集，显著提高收集数据的质量和相关性。

💡 创新点3：推理时间优化技术
探索推理时间优化技术，以应对网页浏览等任务中固有的随机性。提出集成重试机制和基于集成的多次运行策略的管道，提高Cognitive Kernel - Pro性能的可靠性和一致性。

### 📈 实验结果
在GAIA上对Cognitive Kernel - Pro进行评估，在开源和免费智能体中取得了领先的结果。其8B参数的开源模型超越了之前的领先系统，如WebDancer和WebSailor，为可访问的、高能力的人工智能体建立了新的性能标准。

### 💬 可借鉴之处
1. **开源理念**：Cognitive Kernel - Pro的完全开源特性为研究人员提供了一个可访问和可复用的智能体开发平台，降低了研究门槛，促进了社区内的合作与创新。
2. **训练方法**：系统地构建和优化训练数据的方法，如构建可验证的查询 - 答案对、利用中间过程提示等，对于提高智能体的性能和泛化能力具有重要的借鉴意义。
3. **架构设计**：分层多模块的智能体架构设计，既保证了智能体功能的模块化和可扩展性，又简化了特定任务训练数据的收集，为智能体的设计和开发提供了新的思路。
``` 

