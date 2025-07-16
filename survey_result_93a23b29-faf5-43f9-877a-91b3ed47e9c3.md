# Paper List of Terms(Rare Disease)
- [25/06] **An Agentic System for Rare Disease Diagnosis with Traceable Reasoning**  
[[Paper](http://arxiv.org/pdf/2506.20430v1)] [[Code/Page](http://raredx.cn/doctor.)] [[TLDR/Notes](#an-agentic-system-for-rare-disease-diagnosis-with-traceable-reasoning)]

- [25/06] **Evaluating Rare Disease Diagnostic Performance in Symptom Checkers: A Synthetic Vignette Simulation Approach**  
[[Paper](http://arxiv.org/pdf/2506.19750v3)] [[Code/Page]()] [[TLDR/Notes](#evaluating-rare-disease-diagnostic-performance-in-symptom-checkers--a-synthetic-vignette-simulation-approach)]

- [25/06] **Quantitative Benchmarking of Anomaly Detection Methods in Digital Pathology**  
[[Paper](http://arxiv.org/pdf/2506.19234v1)] [[Code/Page]()] [[TLDR/Notes](#quantitative-benchmarking-of-anomaly-detection-methods-in-digital-pathology)]

- [25/06] **Benchmarking Foundation Models and Parameter-Efficient Fine-Tuning for Prognosis Prediction in Medical Imaging**  
[[Paper](http://arxiv.org/pdf/2506.18434v1)] [[Code/Page]()] [[TLDR/Notes](#benchmarking-foundation-models-and-parameter-efficient-fine-tuning-for-prognosis-prediction-in-medical-imaging)]

- [25/06] **PhenoKG: Knowledge Graph-Driven Gene Discovery and Patient Insights from Phenotypes Alone**  
[[Paper](http://arxiv.org/pdf/2506.13119v1)] [[Code/Page]()] [[TLDR/Notes](#phenokg--knowledge-graph-driven-gene-discovery-and-patient-insights-from-phenotypes-alone)]

- [25/06] **Conditional diffusion models for guided anomaly detection in brain images using fluid-driven anomaly randomization**  
[[Paper](http://arxiv.org/pdf/2506.10233v1)] [[Code/Page]()] [[TLDR/Notes](#conditional-diffusion-models-for-guided-anomaly-detection-in-brain-images-using-fluid-driven-anomaly-randomization)]

- [25/06] **CXR-LT 2024: A MICCAI challenge on long-tailed, multi-label, and zero-shot disease classification from chest X-ray**  
[[Paper](http://arxiv.org/pdf/2506.07984v1)] [[Code/Page]()] [[TLDR/Notes](#cxr-lt-2024--a-miccai-challenge-on-long-tailed--multi-label--and-zero-shot-disease-classification-from-chest-x-ray)]

- [25/05] **CaseReportBench: An LLM Benchmark Dataset for Dense Information Extraction in Clinical Case Reports**  
[[Paper](http://arxiv.org/pdf/2505.17265v1)] [[Code/Page]()] [[TLDR/Notes](#casereportbench--an-llm-benchmark-dataset-for-dense-information-extraction-in-clinical-case-reports)]

- [25/05] **Decoding Rarity: Large Language Models in the Diagnosis of Rare Diseases**  
[[Paper](http://arxiv.org/pdf/2505.17065v1)] [[Code/Page]()] [[TLDR/Notes](#decoding-rarity--large-language-models-in-the-diagnosis-of-rare-diseases)]

- [25/03] **MODIS: Multi-Omics Data Integration for Small and Unpaired Datasets**  
[[Paper](http://arxiv.org/pdf/2503.18856v1)] [[Code/Page](https://github.com/VILLOUTREIXLab/MODIS.)] [[TLDR/Notes](#modis--multi-omics-data-integration-for-small-and-unpaired-datasets)]



# TLDR/Notes
## an-agentic-system-for-rare-disease-diagnosis-with-traceable-reasoning
### Abstract
Rare diseases collectively affect over 300 million individuals worldwide, yet
timely and accurate diagnosis remains a pervasive challenge. This is largely
due to their clinical heterogeneity, low individual prevalence, and the limited
familiarity most clinicians have with rare conditions. Here, we introduce
DeepRare, the first rare disease diagnosis agentic system powered by a large
language model (LLM), capable of processing heterogeneous clinical inputs. The
system generates ranked diagnostic hypotheses for rare diseases, each
accompanied by a transparent chain of reasoning that links intermediate
analytic steps to verifiable medical evidence.
  DeepRare comprises three key components: a central host with a long-term
memory module; specialized agent servers responsible for domain-specific
analytical tasks integrating over 40 specialized tools and web-scale,
up-to-date medical knowledge sources, ensuring access to the most current
clinical information. This modular and scalable design enables complex
diagnostic reasoning while maintaining traceability and adaptability. We
evaluate DeepRare on eight datasets. The system demonstrates exceptional
diagnostic performance among 2,919 diseases, achieving 100% accuracy for 1013
diseases. In HPO-based evaluations, DeepRare significantly outperforms other 15
methods, like traditional bioinformatics diagnostic tools, LLMs, and other
agentic systems, achieving an average Recall@1 score of 57.18% and surpassing
the second-best method (Reasoning LLM) by a substantial margin of 23.79
percentage points. For multi-modal input scenarios, DeepRare achieves 70.60% at
Recall@1 compared to Exomiser's 53.20% in 109 cases. Manual verification of
reasoning chains by clinical experts achieves 95.40% agreements. Furthermore,
the DeepRare system has been implemented as a user-friendly web application
http://raredx.cn/doctor.
### 🌟 论文解读 | 用大语言模型打造可追溯推理的罕见病诊断智能系统

### 📌 背景痛点/本文动机
罕见病在全球影响超3亿人，但及时准确诊断面临诸多挑战：临床异质性强、单个疾病患病率低、医生对罕见病熟悉度有限，患者常经历漫长“诊断 Odyssey”（平均超5年转诊、误诊等）。同时，开发罕见病AI诊断系统存在多难点：需多学科知识处理复杂异质症状、病例少易过拟合、知识更新快需高效整合、诊断需透明可追溯以获临床信任。而大语言模型驱动的智能体系统为解决这些难题提供了新可能。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出DeepRare系统架构  
DeepRare是首个基于大语言模型（LLM）的罕见病诊断智能体系统，能处理异构临床输入（自由文本临床描述、结构化人类表型本体HPO术语、基因检测VCF格式结果）。系统由三层构成：核心是带记忆库的中央宿主（协调诊断流程、保留上下文）；周围是多个专用智能体服务器（负责表型提取、变异优先级排序等领域任务）；最外层是精选和网络规模的外部数据源（确保获取最新临床证据），还加入自反思诊断循环，迭代评估中间假设降低误诊和LLM幻觉风险。  

💡 创新点2：实现可追溯推理与多模态处理  
系统生成带排名的罕见病诊断假设，每个假设都有透明推理链，将分析步骤与可验证医学证据关联，支撑临床信任与AI - 人类协作。同时支持自由文本、HPO、基因检测结果等多模态输入，适配真实复杂临床场景。  

### 📈 实验结果
在8个数据集（涵盖亚欧美病例、14个医学专科、2919种疾病）评估中表现卓越：2919种疾病里1013种实现100%诊断准确率；HPO评估任务中，比15种方法（传统工具、LLM、其他智能体系统）显著更优，Recall@1达57.18%，比次优方法高23.79个百分点；多模态输入场景（109例全外显子测序病例）中Recall@1达70.60%，远超Exomiser的53.20%；临床专家手动验证推理链，一致性达95.40%，证明推理医学有效性与可追溯性。  

### 💬 可借鉴之处
1. 架构设计：模块化、可扩展的智能体系统架构，整合领域工具与动态知识源，为复杂任务（如医疗诊断）的AI系统设计提供参考，平衡推理复杂度与可追溯、适应性。  
2. 多模态与可解释性：在处理多模态异构数据及为AI输出添加可追溯推理链方面，为医疗等强监管、需信任领域的AI应用提供范式，助力人机协作。  
3. 评估维度：从准确率、多方法对比、专家验证等多维度验证系统，为同类医疗AI系统评估提供全面思路。

## evaluating-rare-disease-diagnostic-performance-in-symptom-checkers--a-synthetic-vignette-simulation-approach
### Abstract
Symptom Checkers (SCs) provide medical information tailored to user symptoms.
A critical challenge in SC development is preventing unexpected performance
degradation for individual diseases, especially rare diseases, when updating
algorithms. This risk stems from the lack of practical pre-deployment
evaluation methods. For rare diseases, obtaining sufficient evaluation data
from user feedback is difficult. To evaluate the impact of algorithm updates on
the diagnostic performance for individual rare diseases before deployment, this
study proposes and validates a novel Synthetic Vignette Simulation Approach.
This approach aims to enable this essential evaluation efficiently and at a low
cost. To estimate the impact of algorithm updates, we generated synthetic
vignettes from disease-phenotype annotations in the Human Phenotype Ontology
(HPO), a publicly available knowledge base for rare diseases curated by
experts. Using these vignettes, we simulated SC interviews to predict changes
in diagnostic performance. The effectiveness of this approach was validated
retrospectively by comparing the predicted changes with actual performance
metrics using the R-squared ($R^2$) coefficient. Our experiment, covering eight
past algorithm updates for rare diseases, showed that the proposed method
accurately predicted performance changes for diseases with phenotype frequency
information in HPO (n=5). For these updates, we found a strong correlation for
both Recall@8 change ($R^2$ = 0.83,$p$ = 0.031) and Precision@8 change ($R^2$ =
0.78,$p$ = 0.047). Our proposed method enables the pre-deployment evaluation of
SC algorithm changes for individual rare diseases. This evaluation is based on
a publicly available medical knowledge database created by experts, ensuring
transparency and explainability for stakeholders. Additionally, SC developers
can efficiently improve diagnostic performance at a low cost.
### 🌟 论文解读 | 罕见病症状检查器诊断性能评估：合成病例模拟新方法

### 📌 背景痛点/本文动机
在数字健康领域，症状检查器（SCs）能依据用户症状提供个性化医疗信息，对罕见病早期诊断也有重要意义。但SCs算法更新时，易出现特定疾病（尤其是罕见病）诊断性能意外下降的问题。原因在于缺乏实用的部署前评估方法：罕见病难从用户反馈获取足量评估数据，人工制作大量临床病例成本高且不现实，同时用病例报告构建评估数据集也存在覆盖不全面等缺陷。因此，亟需一种高效低成本的方法，在部署前评估算法更新对罕见病诊断性能的影响。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出合成病例模拟方法  
利用专家编纂的公开罕见病知识库——人类表型本体（HPO）中的疾病 - 表型注释生成合成病例。HPO包含疾病中出现的临床表型及其频率信息，基于此生成的合成病例可作为SCs输入，模拟问诊过程来预估算法更新对诊断性能的影响。  

💡 创新点2：兼顾透明可解释与成本效益及适应性  
评估依赖专家维护的公开同行评审医疗知识库，为利益相关者提供高透明度与可解释性；合成病例比传统临床病例生成成本低得多；方法不依赖SCs特定AI或算法，适配不同SCs开发者，对内部实现变更鲁棒，方便开发者使用。  

### 📈 实验结果
实验覆盖8次罕见病算法更新，结果显示：对于HPO中有表型频率信息的疾病（n = 5），该方法能准确预测性能变化。Recall@8变化的R²达0.83（p = 0.031），Precision@8变化的R²达0.78（p = 0.047），二者均有强相关性；而HPO中无频率数据的疾病（n = 3）预测误差大，凸显频率信息关键作用。另外，将HPO表型映射到SCs症状平均每病约需2小时。  

### 💬 可借鉴之处
该方法为SCs罕见病算法更新提供部署前评估途径，基于公开专家医疗知识库保障透明可解释性，还能让开发者低成本高效提升罕见病诊断性能。对医疗AI领域，尤其是症状检查类工具研发，在评估方法创新、医疗知识库利用等方面提供了新思路，为解决罕见病这类小众但关键场景的算法评估难题给出了可行方案。

## quantitative-benchmarking-of-anomaly-detection-methods-in-digital-pathology
### Abstract
Anomaly detection has been widely studied in the context of industrial defect
inspection, with numerous methods developed to tackle a range of challenges. In
digital pathology, anomaly detection holds significant potential for
applications such as rare disease identification, artifact detection, and
biomarker discovery. However, the unique characteristics of pathology images,
such as their large size, multi-scale structures, stain variability, and
repetitive patterns, introduce new challenges that current anomaly detection
algorithms struggle to address. In this quantitative study, we benchmark over
20 classical and prevalent anomaly detection methods through extensive
experiments. We curated five digital pathology datasets, both real and
synthetic, to systematically evaluate these approaches. Our experiments
investigate the influence of image scale, anomaly pattern types, and training
epoch selection strategies on detection performance. The results provide a
detailed comparison of each method's strengths and limitations, establishing a
comprehensive benchmark to guide future research in anomaly detection for
digital pathology images.
```
### 🌟 论文解读 | 数字病理中异常检测方法的定量基准测试

### 📌 背景痛点/本文动机
异常检测在工业缺陷检测等领域已被广泛研究，但在数字病理领域，病理图像具有大尺寸、多尺度结构、染色变异性和重复模式等独特特征，当前异常检测算法难以应对这些新挑战。而异常检测在数字病理中对罕见病识别、伪影检测和生物标志物发现等应用有很大潜力，因此需要对现有异常检测方法在数字病理场景下进行系统评估。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：大规模方法 benchmarking
对23种经典和前沿的异常检测方法，在合成和真实的数字病理图像上进行基准测试，这些图像具有不同的异常模式以实现全面评估。
💡 创新点2：探索关键影响因素
实验探索了数字病理中异常检测性能的关键影响因素，包括图像尺度、反向异常模式以及训练轮次选择策略等，这些在之前研究中很少被讨论。
💡 创新点3：针对性的领域分析
回顾现有异常检测方法在病理图像上的应用，结合实验结果为该领域未来研究提供有价值的见解；同时总结病理图像异常检测的领域特定特征，引入为分析量身定制的真实和合成数据集。

### 📈 实验结果
通过精心策划的5个真实与合成数字病理数据集，系统评估这些异常检测方法。实验探究图像尺度、异常模式类型和训练轮次选择策略对检测性能的影响，详细对比了每种方法的优势和局限性，建立了全面的基准以指导数字病理图像异常检测的未来研究。

### 💬 可借鉴之处
对于研究数字病理与异常检测交叉领域的学者，本文提供了不同方法在病理图像上的性能表现参考，明确了各方法适用场景；其对图像尺度、训练策略等因素的探究思路，也为后续优化异常检测算法在特定领域性能提供了可借鉴的实验设计方向；同时对病理图像领域特征的总结，有助于研究者更有针对性地改进算法以适配病理图像的独特性。
```

## benchmarking-foundation-models-and-parameter-efficient-fine-tuning-for-prognosis-prediction-in-medical-imaging
### Abstract
Artificial Intelligence (AI) holds significant promise for improving
prognosis prediction in medical imaging, yet its effective application remains
challenging. In this work, we introduce a structured benchmark explicitly
designed to evaluate and compare the transferability of Convolutional Neural
Networks and Foundation Models in predicting clinical outcomes in COVID-19
patients, leveraging diverse publicly available Chest X-ray datasets. Our
experimental methodology extensively explores a wide set of fine-tuning
strategies, encompassing traditional approaches such as Full Fine-Tuning and
Linear Probing, as well as advanced Parameter-Efficient Fine-Tuning methods
including Low-Rank Adaptation, BitFit, VeRA, and IA3. The evaluations were
conducted across multiple learning paradigms, including both extensive
full-data scenarios and more clinically realistic Few-Shot Learning settings,
which are critical for modeling rare disease outcomes and rapidly emerging
health threats. By implementing a large-scale comparative analysis involving a
diverse selection of pretrained models, including general-purpose architectures
pretrained on large-scale datasets such as CLIP and DINOv2, to
biomedical-specific models like MedCLIP, BioMedCLIP, and PubMedCLIP, we
rigorously assess each model's capacity to effectively adapt and generalize to
prognosis tasks, particularly under conditions of severe data scarcity and
pronounced class imbalance. The benchmark was designed to capture critical
conditions common in prognosis tasks, including variations in dataset size and
class distribution, providing detailed insights into the strengths and
limitations of each fine-tuning strategy. This extensive and structured
evaluation aims to inform the practical deployment and adoption of robust,
efficient, and generalizable AI-driven solutions in real-world clinical
prognosis prediction workflows.
### 🌟 论文解读 | 医疗影像预后预测中基础模型与高效参数微调的 benchmark 研究

### 📌 背景痛点/本文动机
AI 在医疗影像预后预测领域虽前景广阔，但有效应用仍具挑战。预后任务比诊断任务更复杂且研究较少，数据存在时间结构、高质量标注少等问题。传统卷积神经网络（CNNs）在处理预后任务时，存在捕捉长程依赖能力有限、全微调要求高适配性不足等局限；自监督学习催生的基础模型（FMs）在预后领域探索有限，因预后数据集样本稀缺、类别不平衡等问题，传统适配技术难应对；全微调存在可扩展性和数据效率局限，而参数高效微调（PEFT）和少样本学习（FSL）是有潜力的解决方向，但在医疗预后中相关探索不足。因此，本文旨在构建结构化基准，评估不同预训练模型与微调策略在医疗预后的表现。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：全面对比基础模型与 CNN 架构  
构建系统基准，对比 PEFT 技术与传统微调策略（如全微调 FFT、线性探测 LP），涵盖通用预训练模型（如 ResNet18）和医疗领域预训练模型（如 PubMedCLIP），聚焦预后预测任务，探究哪些策略对数据稀缺和类别不平衡更鲁棒，这两类是预后建模关键挑战。  

💡 创新点2：探索基础模型在预后任务的 PEFT 应用  
针对医疗影像中 CNN 研究多、FMs 在预后预测探索少的现状，对 FMs 开展对比评估，分析 PEFT、LP、FFT 等策略，确定在计算成本和预测性能间最优权衡的方法与架构。  

💡 创新点3：开展预后建模中的少样本学习分析  
系统分析 FSL，结合医疗场景中数据稀缺特点，探索在极少标注样本下模型泛化能力，且考虑将 PEFT 融入 FSL  pipeline 提升资源受限环境下的适配效率，为标注数据难获取的医疗 AI 应用提供方案。  

💡 创新点4：构建针对预后任务的结构化基准  
以 COVID - 19 胸部 X 光（CXR）预后为临床相关且标准化的用例，利用具有不同结果类型、样本量和不平衡程度的公共数据集，捕捉预后任务中数据集大小、类别分布变化等关键条件，为各微调策略强弱项提供详细洞见。  

### 📈 实验结果
文中通过大规模对比分析，涉及从通用大规模数据集预训练的架构（如 CLIP、DINOv2）到生物医学特定模型（如 MedCLIP、BioMedCLIP、PubMedCLIP）等多样预训练模型，评估模型在预后任务（尤其数据严重稀缺和类别不平衡下）的适配与泛化能力，明确各微调策略在不同场景下的表现，为实际临床预后预测工作流中 AI 方案部署提供依据，但原文未详细列出具体实验数值结果，重点在构建评估体系与对比分析逻辑。

### 💬 可借鉴之处
1. 基准构建思路：为特定医疗任务（如 COVID - 19 胸部 X 光预后）构建包含多模型、多策略、多数据场景的基准，可用于同类医疗 AI 任务评估体系搭建，明确不同技术路线优劣。  
2. 技术融合探索：对 PEFT、FSL 等新兴技术在医疗预后场景结合应用的探索，为解决医疗数据稀缺、标注难问题提供技术融合参考方向。  
3. 模型与策略对比维度：全面对比通用与领域特定预训练模型，以及传统与先进微调策略，这种多维度对比方式可指导后续医疗 AI 研究中模型与策略选型。

## phenokg--knowledge-graph-driven-gene-discovery-and-patient-insights-from-phenotypes-alone
### Abstract
Identifying causative genes from patient phenotypes remains a significant
challenge in precision medicine, with important implications for the diagnosis
and treatment of genetic disorders. We propose a novel graph-based approach for
predicting causative genes from patient phenotypes, with or without an
available list of candidate genes, by integrating a rare disease knowledge
graph (KG). Our model, combining graph neural networks and transformers,
achieves substantial improvements over the current state-of-the-art. On the
real-world MyGene2 dataset, it attains a mean reciprocal rank (MRR) of 24.64\%
and nDCG@100 of 33.64\%, surpassing the best baseline (SHEPHERD) at 19.02\% MRR
and 30.54\% nDCG@100. We perform extensive ablation studies to validate the
contribution of each model component. Notably, the approach generalizes to
cases where only phenotypic data are available, addressing key challenges in
clinical decision support when genomic information is incomplete.
### 🌟 论文解读 | PhenoKG：仅靠表型数据，知识图谱驱动的致病基因发现与患者洞察

### 📌 背景痛点/本文动机
罕见遗传病给全球医疗系统带来巨大挑战，全球超3亿人受其影响。在精准医疗中，从患者表型识别致病基因是难题，诊断过程漫长复杂（常被称为“诊断奥德赛”），约70%患者难以及时确诊，近半孟德尔遗传病的遗传病因不明。现有诊断流程依赖专家手动整合临床与基因组数据，且多数诊断 pipeline 需先确定候选基因列表，受限于医学知识和人力。同时，测序等技术进步后，罕见孟德尔病诊断率仍仅30 - 50%，亟需能整合多源生物医学数据、兼具可解释性与普适性的新一代模型，来解决基因组信息不全时临床决策支持的难题。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出 PhenoKG 方法，结合知识图谱与图神经网络 + Transformer。  
构建患者特异性子图：利用患者表型和罕见病知识图谱（KG）构建子图，捕捉患者 - 疾病 - 基因型的特定关系；通过图注意力网络（GATv2）生成节点嵌入，进而得到患者和基因表示，用于预测最可能的致病基因，无需或仅需少量候选基因列表就能开展预测。  

💡 创新点2：覆盖多场景且泛化性强。  
既支持有专家整理的候选基因列表（约20个基因）时的预测，也能在无候选列表（从约8000个基因中筛选）时工作，填补了基因组信息不全时临床决策支持的空白，为临床提供额外的发现层面（虽需后续验证，但理论上拓展了基因发现途径）。  

💡 创新点3：深入 ablation study 验证组件贡献。  
通过大量消融实验，明确模型各组件（如知识图谱整合、图神经网络与 Transformer 结合等）对性能的贡献，让模型设计更具可解释性与说服力。  


### 📈 实验结果
在真实世界 MyGene2 数据集上，PhenoKG 实现了性能超越：平均 reciprocal 排名（MRR）达24.64%，nDCG@100 为33.64%，超过当前最优基线模型 SHEPHERD（MRR 19.02%、nDCG@100 30.54%）。无候选列表时，模型准确率达15.15 ± 3.33%（top 排名中命中正确基因）；有候选列表时，准确率提升至83.96 ± 1.45%，验证了多场景下的有效性。  


### 💬 可借鉴之处
1. 知识图谱 + 图神经网络的融合思路：将领域知识图谱与图深度学习结合，为生物医学领域中多源异构数据的利用提供了范例，可启发其他需整合领域知识的 AI 任务（如药物研发、疾病分型等）。  
2. 多场景适配的模型设计：考虑到临床中数据完整性差异，设计支持“有无候选列表”的灵活架构，为医疗 AI 工具落地临床实际场景提供了适配不同数据条件的参考。  
3. 消融实验的严谨性：通过系统消融验证各模块价值，这种“拆解 - 验证”的实验思路，能帮助后续研究者更清晰理解模型关键组件的作用，提升研究的可复现性与可解释性。  

## conditional-diffusion-models-for-guided-anomaly-detection-in-brain-images-using-fluid-driven-anomaly-randomization
### Abstract
Supervised machine learning has enabled accurate pathology detection in brain
MRI, but requires training data from diseased subjects that may not be readily
available in some scenarios, for example, in the case of rare diseases.
Reconstruction-based unsupervised anomaly detection, in particular using
diffusion models, has gained popularity in the medical field as it allows for
training on healthy images alone, eliminating the need for large
disease-specific cohorts. These methods assume that a model trained on normal
data cannot accurately represent or reconstruct anomalies. However, this
assumption often fails with models failing to reconstruct healthy tissue or
accurately reconstruct abnormal regions i.e., failing to remove anomalies. In
this work, we introduce a novel conditional diffusion model framework for
anomaly detection and healthy image reconstruction in brain MRI. Our weakly
supervised approach integrates synthetically generated pseudo-pathology images
into the modeling process to better guide the reconstruction of healthy images.
To generate these pseudo-pathologies, we apply fluid-driven anomaly
randomization to augment real pathology segmentation maps from an auxiliary
dataset, ensuring that the synthetic anomalies are both realistic and
anatomically coherent. We evaluate our model's ability to detect pathology,
using both synthetic anomaly datasets and real pathology from the ATLAS
dataset. In our extensive experiments, our model: (i) consistently outperforms
variational autoencoders, and conditional and unconditional latent diffusion;
and (ii) surpasses on most datasets, the performance of supervised inpainting
methods with access to paired diseased/healthy images.
### 🌟 论文解读 | 基于流体驱动异常随机化的脑图像引导异常检测条件扩散模型

### 📌 背景痛点/本文动机
在脑MRI异常检测的有监督机器学习应用中，数据可用性是一大挑战，尤其是罕见病场景下，患病受试者的训练数据往往难以获取。基于重建的无监督异常检测虽可仅用健康图像训练，但现有方法存在假设不成立的问题，即训练于正常数据的模型可能无法准确重建健康组织或异常区域。此外，自动编码器存在检测异常能力不足、生成能力差等问题；扩散模型在处理大异常区域时也面临噪声水平选择难题。因此，本文旨在提出新的条件扩散模型框架，提升脑MRI异常检测与健康图像重建效果。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出含合成伪病理图像的弱监督条件扩散模型框架  
该框架将合成生成的伪病理图像整合到建模过程，以更好引导健康图像重建。通过在反向扩散过程的每个时间步纳入伪病理图像信息来训练模型，使模型在训练时能修正合成异常同时保留健康组织区域。  

💡 创新点2：流体驱动异常随机化生成伪病理  
利用流体驱动异常随机化方法增强辅助数据集的真实病理分割图，生成伪病理。将异常模式随机化建模为偏微分方程（PDE）主导的平流 - 扩散过程，通过可控速度场和边界条件确保模拟异常合理，且生成的合成异常兼具真实性与解剖学一致性。  

💡 创新点3：基于潜在扩散模型（LDM）改进  
以LDM为基础，分两阶段训练。先由编码器映射输入图像到潜在表示、解码器从潜在表示重建图像；再训练DDPM学习潜在表示分布，借助去噪模型优化目标函数，提升模型对数据分布的捕捉与去噪重建能力。  

### 📈 实验结果
在合成异常数据集和ATLAS数据集的真实病理上评估模型异常检测能力，实验表明：（i）该模型持续超越变分自动编码器、条件和无条件潜在扩散模型；（ii）在大多数数据集上，超过有配对患病/健康图像的有监督修复方法性能，展现了在3D脑图像异常检测中的高效性。  

### 💬 可借鉴之处
1. 弱监督结合合成数据的思路：在数据稀缺场景下，利用合成伪数据辅助训练，为医疗等数据难获取领域提供了数据增强与训练范式参考。  
2. 流体驱动异常随机化的生成方式：将物理过程（平流 - 扩散的PDE过程）引入异常生成，保障合成异常的合理性，这种跨学科结合生成真实数据的方法值得借鉴。  
3. 基于扩散模型改进异常检测：扩散模型在捕捉复杂数据分布上有优势，本文针对医疗图像场景改进扩散模型用于异常检测，为扩散模型在垂直领域的应用提供了实践案例。

## cxr-lt-2024--a-miccai-challenge-on-long-tailed--multi-label--and-zero-shot-disease-classification-from-chest-x-ray
### Abstract
The CXR-LT series is a community-driven initiative designed to enhance lung
disease classification using chest X-rays (CXR). It tackles challenges in open
long-tailed lung disease classification and enhances the measurability of
state-of-the-art techniques. The first event, CXR-LT 2023, aimed to achieve
these goals by providing high-quality benchmark CXR data for model development
and conducting comprehensive evaluations to identify ongoing issues impacting
lung disease classification performance. Building on the success of CXR-LT
2023, the CXR-LT 2024 expands the dataset to 377,110 chest X-rays (CXRs) and 45
disease labels, including 19 new rare disease findings. It also introduces a
new focus on zero-shot learning to address limitations identified in the
previous event. Specifically, CXR-LT 2024 features three tasks: (i) long-tailed
classification on a large, noisy test set, (ii) long-tailed classification on a
manually annotated "gold standard" subset, and (iii) zero-shot generalization
to five previously unseen disease findings. This paper provides an overview of
CXR-LT 2024, detailing the data curation process and consolidating
state-of-the-art solutions, including the use of multimodal models for rare
disease detection, advanced generative approaches to handle noisy labels, and
zero-shot learning strategies for unseen diseases. Additionally, the expanded
dataset enhances disease coverage to better represent real-world clinical
settings, offering a valuable resource for future research. By synthesizing the
insights and innovations of participating teams, we aim to advance the
development of clinically realistic and generalizable diagnostic models for
chest radiography.
### 🌟 论文解读 | CXR-LT 2024：聚焦胸部X光的长尾、多标签与零样本疾病分类挑战赛

### 📌 背景痛点/本文动机
胸部X光（CXR）是肺部疾病诊断的重要工具，但实际临床中疾病表现存在**长尾分布**（常见疾病样本多、罕见疾病样本极少）、需要同时识别**多类疾病**，且还有大量未被现有数据集覆盖的罕见病症，导致模型对新疾病的泛化能力不足。CXR-LT系列正是为解决这些问题而生的社区驱动项目，2023年的CXR-LT已提供高质量基准数据并推动了相关研究，但仍需应对“零样本学习（模型对完全没见过的疾病类别做识别）”等新挑战。因此CXR-LT 2024在此基础上进一步扩展数据、设计任务，推动肺部疾病分类技术向更贴近真实临床的方向发展。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：大规模且更全面的数据集构建  
CXR-LT 2024将数据集扩充到**377,110张胸部X光图像**，涵盖45个疾病标签（新增19种罕见病标签）。相比2023年，数据规模与疾病覆盖度大幅提升，更贴近真实临床中疾病种类繁杂、长尾分布的特点，为模型训练与评估提供了更丰富的“素材”。  

💡 创新点2：三类任务针对性解决临床难点  
本次挑战赛设计了三项任务，全面覆盖长尾学习与零样本学习痛点：  
- 任务1：在**大规模带噪声测试集**上做长尾分类——模拟真实世界中标签可能不准确、数据分布不均的场景；  
- 任务2：在**人工标注的“金标准”子集**上做长尾分类——聚焦高精度标注下的模型性能，验证算法在干净数据上的上限；  
- 任务3：对**5种完全未见过的疾病**做零样本泛化——直击临床中“新疾病无标注数据可用”的痛点，要求模型具备跨未知类别的推理能力。  

💡 创新点3：整合前沿技术方向的探索  
论文还梳理了参赛团队与领域内应对这些挑战的前沿思路，例如：用**多模态模型**辅助罕见病检测（结合图像、文本等信息弥补罕见病样本少的缺陷）；用**先进生成式方法**处理噪声标签（生成更可靠的标注或数据增强，缓解标签噪声干扰）；为零样本任务设计**新型学习策略**（让模型学会从已知类别迁移知识到未知类别）。  


### 📈 实验结果
文中虽未完全展开各任务的最终竞赛排名细节，但从任务设计逻辑与技术方向整合来看，核心在于验证：  
1. 长尾场景下，不同方法（如数据重采样、损失函数优化、多模态融合等）对多标签分类性能（以mAP为核心指标，辅以mAUROC、mF1、ECE等）的提升效果；  
2. 零样本任务中，模型对全新疾病类别的泛化能力（能否基于少量先验知识或语义信息，识别从未训练过的疾病）；  
3. 人工标注“金标准”子集与噪声测试集的对比，能反映算法在“理想-现实”场景下的鲁棒性差异。  

这些任务的评估体系（多指标结合，兼顾整体与细粒度类别性能）也为后续研究提供了“怎么衡量模型好坏”的参考框架。  


### 💬 可借鉴之处
1. **数据集建设思路**：通过持续扩充真实世界维度（疾病覆盖、样本规模）的数据集，推动领域研究更贴近临床——这对医疗AI类研究极具参考性，毕竟真实场景的数据复杂性远非小数据集能覆盖；  
2. **任务设计范式**：用“噪声测试集+金标准子集+零样本任务”的组合拳，把长尾学习、鲁棒性、泛化性等难点拆解成可量化的竞赛任务，这种“分场景拆解问题”的思路，能帮助研究者更精准地迭代算法；  
3. **技术方向启发**：多模态融合、生成式方法处理噪声、零样本学习策略等，都是AI医疗领域突破数据瓶颈的关键方向。论文整合这些前沿尝试，为后来者指明了“从哪些角度改进模型”的路径；  
4. **评估指标选择**：在长尾多标签场景下，放弃单一AUROC指标，改用mAP为主、多指标为辅的评估体系——这提醒我们：不同场景下“选对评估指标”才能真实反映模型价值，避免指标通胀带来的误导。  


CXR-LT 2024不仅是一场竞赛，更是一次“把临床痛点转化为科研问题、用大规模数据与创新任务推动技术落地”的典范实践，为胸部X光诊断乃至更广泛的医疗AI研究提供了数据集、任务设计、技术路线与评估方法的全方位参考。

## casereportbench--an-llm-benchmark-dataset-for-dense-information-extraction-in-clinical-case-reports
### Abstract
Rare diseases, including Inborn Errors of Metabolism (IEM), pose significant
diagnostic challenges. Case reports serve as key but computationally
underutilized resources to inform diagnosis. Clinical dense information
extraction refers to organizing medical information into structured predefined
categories. Large Language Models (LLMs) may enable scalable information
extraction from case reports but are rarely evaluated for this task. We
introduce CaseReportBench, an expert-annotated dataset for dense information
extraction of case reports, focusing on IEMs. Using this dataset, we assess
various models and prompting strategies, introducing novel approaches such as
category-specific prompting and subheading-filtered data integration. Zero-shot
chain-of-thought prompting offers little advantage over standard zero-shot
prompting. Category-specific prompting improves alignment with the benchmark.
The open-source model Qwen2.5-7B outperforms GPT-4o for this task. Our
clinician evaluations show that LLMs can extract clinically relevant details
from case reports, supporting rare disease diagnosis and management. We also
highlight areas for improvement, such as LLMs' limitations in recognizing
negative findings important for differential diagnosis. This work advances
LLM-driven clinical natural language processing and paves the way for scalable
medical AI applications.
### 🌟 论文解读 | CaseReportBench：面向临床病例报告密集信息抽取的大模型基准数据集

### 📌 背景痛点/本文动机
罕见病（如先天性代谢错误疾病IEM）诊断难度大，病例报告是重要诊断参考资源但在计算层面未充分利用。临床密集信息抽取需将医疗信息组织成结构化预定义类别，大语言模型（LLMs）虽有潜力从病例报告中规模化提取信息，却很少针对该任务评估。因此，本文旨在构建用于病例报告密集信息抽取的基准，聚焦IEM，探索有效LLM方法。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建CaseReportBench数据集  
打造由专家标注、针对病例报告（聚焦IEM）密集信息抽取的基准数据集，为评估大模型在该场景下表现提供基础，还公开数据集（Hugging Face）与代码（GitHub）。  

💡 创新点2：探索多样提示与数据整合策略  
评估不同提示和数据整合策略用于密集信息抽取，提出类别特定抽取提示（category - specific extraction prompting）、子标题过滤方法（subheading - filtered approach）等新技术，提升大模型密集信息抽取效果。  

💡 创新点3：开展临床评估  
对大模型抽取输出做临床评估，验证其减少人工抽取工作量潜力的同时，明确存在的挑战。  

### 📈 实验结果
零样本思维链提示较标准零样本提示优势不大；类别特定提示提升与基准的一致性；开源模型Qwen2.5 - 7B在该任务上表现优于GPT - 4o；临床评估显示大模型能提取病例报告中临床相关细节辅助罕见病诊疗，但在识别鉴别诊断关键的阴性结果等方面存在不足。  

### 💬 可借鉴之处
在医疗NLP领域，为基于大模型的临床密集信息抽取任务提供了新基准数据集与评估方法参考；提出的类别特定提示等策略为优化大模型在垂直领域信息抽取效果提供思路；公开数据集与代码利于行业后续研究复现与拓展，推动医疗AI规模化应用发展。

## decoding-rarity--large-language-models-in-the-diagnosis-of-rare-diseases
### Abstract
Recent advances in artificial intelligence, particularly large language
models LLMs, have shown promising capabilities in transforming rare disease
research. This survey paper explores the integration of LLMs in the analysis of
rare diseases, highlighting significant strides and pivotal studies that
leverage textual data to uncover insights and patterns critical for diagnosis,
treatment, and patient care. While current research predominantly employs
textual data, the potential for multimodal data integration combining genetic,
imaging, and electronic health records stands as a promising frontier. We
review foundational papers that demonstrate the application of LLMs in
identifying and extracting relevant medical information, simulating intelligent
conversational agents for patient interaction, and enabling the formulation of
accurate and timely diagnoses. Furthermore, this paper discusses the challenges
and ethical considerations inherent in deploying LLMs, including data privacy,
model transparency, and the need for robust, inclusive data sets. As part of
this exploration, we present a section on experimentation that utilizes
multiple LLMs alongside structured questionnaires, specifically designed for
diagnostic purposes in the context of different diseases. We conclude with
future perspectives on the evolution of LLMs towards truly multimodal
platforms, which would integrate diverse data types to provide a more
comprehensive understanding of rare diseases, ultimately fostering better
outcomes in clinical settings.
### 🌟 论文解读 | 解码罕见病：大语言模型在罕见病诊断中的应用

### 📌 背景痛点/本文动机
罕见病虽单个疾病患病率低，但整体影响人群规模大（全球约3.5%-5.9%人口受影响），且存在诸多研究与诊疗挑战。患者常面临漫长且复杂的诊断过程，易被误诊或延迟诊断；疾病研究方面，存在患者数据稀缺、知识碎片化、治疗研发滞后等问题。此前大语言模型（LLMs）在罕见病领域应用零散且缺乏全面刻画，因此本文旨在系统综述LLMs在罕见病诊断、疾病机制阐明及治疗策略指导等方面的应用，探索多模态整合潜力，为相关研究与实践提供指引。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：全面综述LLMs在罕见病领域应用  
回顾展示LLMs在识别提取医疗信息、模拟患者交互智能对话代理、助力精准及时诊断等方面应用的基础论文，梳理当前LLMs在罕见病分析中利用文本数据挖掘诊断、治疗和患者护理关键模式与见解的进展。  
💡 创新点2：探索多模态数据整合前景  
指出当前研究多采用文本数据，但结合基因、影像、电子健康记录等多模态数据整合是极具潜力的前沿方向，探讨其对推进个性化医疗和改善患者预后的可能。  
💡 创新点3：关注部署挑战与伦理考量  
深入讨论LLMs部署中的数据隐私、模型透明度、需强健且具包容性数据集等挑战与伦理问题，为负责任使用提供思考。  
💡 创新点4：开展特定实验探索  
设置利用多个LLMs结合为不同疾病诊断设计的结构化问卷进行实验的部分，探索诊断场景下LLMs应用方式。  

### 📈 实验结果
文中未详细呈现实验定量结果（原文中实验部分未完整展示），但从整体逻辑看，通过对文献的系统梳理（遵循PRISMA指南，从识别75篇文献到筛选后分析等流程），明确了LLMs在罕见病领域现有应用场景、多模态等发展方向价值以及面临的挑战等，为该领域后续研究和实践提供了清晰的现状地图与方向指引。  

### 💬 可借鉴之处
1. 系统综述思路：采用PRISMA指南进行文献筛选分析，为领域内系统性梳理研究现状提供了可参考的方法论，有助于后续类似主题综述类研究开展。  
2. 多维度分析视角：从应用场景、数据整合、挑战伦理、实验探索等多维度剖析LLMs与罕见病诊疗结合，能让读者全面理解该领域现状与方向，其他医疗AI交叉领域研究也可借鉴这种多维度分析框架。  
3. 前沿方向洞察：对多模态数据整合等前沿方向的强调，为科研人员和从业者指明了未来技术融合的潜力点，利于引导资源投入和研究方向选择。

## modis--multi-omics-data-integration-for-small-and-unpaired-datasets
### Abstract
A key challenge today lies in the ability to efficiently handle multi-omics
data since such multimodal data may provide a more comprehensive overview of
the underlying processes in a system. Yet it comes with challenges: multi-omics
data are most often unpaired and only partially labeled, moreover only small
amounts of data are available in some situation such as rare diseases. We
propose MODIS which stands for Multi-Omics Data Integration for Small and
unpaired datasets, a semi supervised approach to account for these particular
settings. MODIS learns a probabilistic coupling of heterogeneous data
modalities and learns a shared latent space where modalities are aligned. We
rely on artificial data to build controlled experiments to explore how much
supervision is needed for an accurate alignment of modalities, and how our
approach enables dealing with new conditions for which few data are available.
The code is available athttps://github.com/VILLOUTREIXLab/MODIS.
### 🌟 论文解读 | MODIS：小样本与非配对多组学数据的整合新方案

### 📌 背景痛点/本文动机
在理解复杂生物机制与解决诊断难题（如罕见病诊断）时，多组学数据能提供更全面视角，但处理多组学数据存在诸多挑战：数据往往是非配对的、仅部分带标签，且在罕见病等场景下数据量极少。现有多组学整合方法大多依赖大规模数据集训练，难以直接应用于样本少、模态非配对甚至部分模态缺失的罕见病等场景。因此，亟需一种能应对小样本、非配对多组学数据整合的方法，这正是本文提出MODIS的动机。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：半监督的多组学整合框架  
MODIS是面向小样本和非配对数据集的半监督多组学数据整合方法。它学习异质数据模态间的概率耦合关系，并构建一个共享潜在空间来对齐不同模态。通过这种方式，能在数据非配对、标签不完整的情况下，实现多模态的有效整合与关联。  

💡 创新点2：利用参考数据集辅助小数据集对齐  
借助大规模参考数据集（如TCGA数据库）与小目标数据集（如罕见病数据）结合训练。利用从大规模数据中学到的结构，助力小数据集中模态的对齐与翻译，以及标签分类任务，解决小样本场景下数据不足的问题。  

💡 创新点3：应对多场景需求的模型设计  
考虑到实际场景中常出现的情况（如仅单个模态数据可用、存在未标记数据、部分类别训练样本少等），MODIS设计上支持单模态样本的类别预测、利用无标签数据以及处理类别不平衡的分类问题，全面覆盖多组学小样本场景下的核心需求。  

### 📈 实验结果
论文借助人工数据构建受控实验，探索模态准确对齐所需的监督程度，以及该方法在少量数据可用的新场景下的应对能力。通过这些实验验证MODIS在小样本、非配对多组学数据整合与相关任务（如分类）中的有效性，但原文未详细展开具体实验数值结果，重点在于方法设计与实验思路的呈现。  

### 💬 可借鉴之处
1. 多模态整合思路：针对多组学这类典型多模态数据，提出的概率耦合与共享潜在空间构建方式，为其他领域（如视听多模态、文本图像多模态等）的小样本非配对数据整合提供了参考范式。  
2. 小样本场景解法：利用大规模参考数据辅助小数据集学习的策略，在医疗、小众领域等数据稀缺场景下，为模型训练与性能提升提供了可行思路，可迁移到类似数据分布不均、小样本的任务中。  
3. 半监督与多需求覆盖：在模型中兼顾半监督学习（利用无标签数据）、多模态单模态预测、类别不平衡处理等，这种全面覆盖实际场景需求的设计理念，对解决复杂现实任务有很好的借鉴意义，提醒研究者在方法设计时充分考虑真实场景的多样性约束。

