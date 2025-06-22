# Paper List of Terms(Vision Language Model+Game)
- [25/06] **An Open-Source Software Toolkit & Benchmark Suite for the Evaluation and Adaptation of Multimodal Action Models**  
[[Paper](http://arxiv.org/pdf/2506.09172v2)] [[Code/Page]()] [[TLDR/Notes](#an-open-source-software-toolkit-&-benchmark-suite-for-the-evaluation-and-adaptation-of-multimodal-action-models)]

- [25/06] **PromptVFX: Text-Driven Fields for Open-World 3D Gaussian Animation**  
[[Paper](http://arxiv.org/pdf/2506.01091v1)] [[Code/Page]()] [[TLDR/Notes](#promptvfx--text-driven-fields-for-open-world-3d-gaussian-animation)]

- [25/05] **Vision Language Models are Biased**  
[[Paper](http://arxiv.org/pdf/2505.23941v1)] [[Code/Page]()] [[TLDR/Notes](#vision-language-models-are-biased)]

- [25/05] **VideoGameBench: Can Vision-Language Models complete popular video games?**  
[[Paper](http://arxiv.org/pdf/2505.18134v2)] [[Code/Page]()] [[TLDR/Notes](#videogamebench--can-vision-language-models-complete-popular-video-games-)]

- [25/05] **VideoGameQA-Bench: Evaluating Vision-Language Models for Video Game Quality Assurance**  
[[Paper](http://arxiv.org/pdf/2505.15952v1)] [[Code/Page](https://asgaardlab.github.io/videogameqa-bench/)] [[TLDR/Notes](#videogameqa-bench--evaluating-vision-language-models-for-video-game-quality-assurance)]

- [25/05] **Code2Logic: Game-Code-Driven Data Synthesis for Enhancing VLMs General Reasoning**  
[[Paper](http://arxiv.org/pdf/2505.13886v1)] [[Code/Page](https://github.com/tongjingqi/Code2Logic.)] [[TLDR/Notes](#code2logic--game-code-driven-data-synthesis-for-enhancing-vlms-general-reasoning)]

- [25/05] **G1: Bootstrapping Perception and Reasoning Abilities of Vision-Language Model via Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.13426v1)] [[Code/Page](https://github.com/chenllliang/G1)] [[TLDR/Notes](#g1--bootstrapping-perception-and-reasoning-abilities-of-vision-language-model-via-reinforcement-learning)]

- [25/05] **DSADF: Thinking Fast and Slow for Decision Making**  
[[Paper](http://arxiv.org/pdf/2505.08189v1)] [[Code/Page]()] [[TLDR/Notes](#dsadf--thinking-fast-and-slow-for-decision-making)]

- [25/05] **Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.03792v2)] [[Code/Page](https://github.com/langfengQ/CoSo.)] [[TLDR/Notes](#towards-efficient-online-tuning-of-vlm-agents-via-counterfactual-soft-reinforcement-learning)]

- [25/04] **Metropolis-Hastings Captioning Game: Knowledge Fusion of Vision Language Models via Decentralized Bayesian Inference**  
[[Paper](http://arxiv.org/pdf/2504.09620v1)] [[Code/Page]()] [[TLDR/Notes](#metropolis-hastings-captioning-game--knowledge-fusion-of-vision-language-models-via-decentralized-bayesian-inference)]



# TLDR/Notes
## an-open-source-software-toolkit-&-benchmark-suite-for-the-evaluation-and-adaptation-of-multimodal-action-models
### Abstract
Recent innovations in multimodal action models represent a promising
direction for developing general-purpose agentic systems, combining visual
understanding, language comprehension, and action generation. We introduce
MultiNet - a novel, fully open-source benchmark and surrounding software
ecosystem designed to rigorously evaluate and adapt models across vision,
language, and action domains. We establish standardized evaluation protocols
for assessing vision-language models (VLMs) and vision-language-action models
(VLAs), and provide open source software to download relevant data, models, and
evaluations. Additionally, we provide a composite dataset with over 1.3
trillion tokens of image captioning, visual question answering, commonsense
reasoning, robotic control, digital game-play, simulated
locomotion/manipulation, and many more tasks. The MultiNet benchmark,
framework, toolkit, and evaluation harness have been used in downstream
research on the limitations of VLA generalization.
### 🌟 论文解读 | MultiNet：多模态动作模型评估与适配的开源工具集与基准套件

### 📌 背景痛点/本文动机
在机器学习领域，多模态动作模型（结合视觉理解、语言理解与动作生成）是构建通用智能体系统的重要方向。然而当前这类模型存在诸多局限：一方面，现有 Vision - Language - Action（VLA）模型多针对机器人操作等狭窄领域设计与评估，在多模态语言理解任务和更广泛泛化能力上的有效性缺乏验证；另一方面，社区缺少专门为这类通用模型大规模训练与全面评估打造的开源基准，多数基准聚焦特定领域且闭源。因此，打造能推动通用动作模型发展与评估的生态系统成为迫切需求，这也正是 MultiNet 诞生的动机。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：大规模通用数据集发布
整合了视觉 - 语言理解、语言处理、强化学习、机器人学等多领域的丰富数据源，涵盖 OBELICS（超大规模图文网页数据）、DataComp - 1B（图像 - 文本对）、各类 VQA 数据集（如 A - OKVQA、VQA - V2 等），还有强化学习与机器人任务相关数据集（如 DM Lab、ALE Atari、Meta - World 等）以及语言能力训练评估数据集（如 Fineweb - edu、HellaSwag 等），为通用模型训练评估提供海量多元数据支撑。

💡 创新点2：开源数据处理 SDK 提供
推出开源软件工具包，方便用户获取整合后的数据集，还能将来自众多来源的控制数据（强化学习和机器人学数据）标准化为通用易访问格式，降低数据使用门槛。

💡 创新点3：系统的评估框架搭建
构建标准化且合理的评估方法，包含测试分割与精心设计的指标，能让社区便捷评估前沿 Vision - Language Models（VLMs）和 VLA 模型在熟悉与新颖领域（如真实机器人任务、程序生成游戏环境）的泛化能力。

💡 创新点4：开源适配前沿模型
对最先进的 VLMs 和 VLAs 进行开源适配，使它们能在 MultiNet 的数据格式和多样领域（甚至训练时未见过的领域）有效运行，加速通用 AI 系统构建进程。

💡 创新点5：深度实验与分析开展
利用 MultiNet 的基准、框架、评估工具和模型适配能力，对主流 VLMs、VLAs 和新兴通用模型性能进行评估与分析，为模型改进提供依据。

### 📈 实验结果
文中未详细展开实验结果数值呈现，但提到 MultiNet 的基准、框架、工具包和评估 harness 已被用于 VLA 泛化局限性的下游研究，说明其在推动多模态动作模型研究上已具备实际应用价值，能为相关研究提供有效支撑以挖掘模型性能与不足。

### 💬 可借鉴之处
1. 数据生态构建思路：通过整合多领域多模态数据打造大规模通用数据集，为通用 AI 模型训练提供充足“养分”，这种跨领域数据聚合思路值得在需要多元数据支撑的研究中借鉴。
2. 开源工具链打造：从数据获取、处理到模型适配、评估都提供开源工具，降低研究门槛，推动社区协作，这种开源生态构建方式对领域发展有很强推动作用，其他领域打造研究基础设施时可参考。
3. 标准化评估体系：建立标准化评估协议与方法，让不同模型在统一标准下对比，利于清晰认知模型能力边界，在需要对模型进行公平对比评估的场景中，这种标准化思路很关键。

## promptvfx--text-driven-fields-for-open-world-3d-gaussian-animation
### Abstract
Visual effects (VFX) are key to immersion in modern films, games, and AR/VR.
Creating 3D effects requires specialized expertise and training in 3D animation
software and can be time consuming. Generative solutions typically rely on
computationally intense methods such as diffusion models which can be slow at
4D inference. We reformulate 3D animation as a field prediction task and
introduce a text-driven framework that infers a time-varying 4D flow field
acting on 3D Gaussians. By leveraging large language models (LLMs) and
vision-language models (VLMs) for function generation, our approach interprets
arbitrary prompts (e.g., "make the vase glow orange, then explode") and
instantly updates color, opacity, and positions of 3D Gaussians in real time.
This design avoids overheads such as mesh extraction, manual or physics-based
simulations and allows both novice and expert users to animate volumetric
scenes with minimal effort on a consumer device even in a web browser.
Experimental results show that simple textual instructions suffice to generate
compelling time-varying VFX, reducing the manual effort typically required for
rigging or advanced modeling. We thus present a fast and accessible pathway to
language-driven 3D content creation that can pave the way to democratize VFX
further.
### 🌟 论文解读 | PromptVFX：文本驱动的开放世界3D高斯动画特效框架

### 📌 背景痛点/本文动机
在现代电影、游戏和AR/VR领域，视觉特效（VFX）是沉浸感的关键。但传统创建3D特效需专业3D动画软件知识与训练，耗时费力。生成式方案常依赖如扩散模型这类计算密集型方法，在4D推理时速度慢。同时，现有结合大模型的方案仍依赖物理模拟或扩散训练循环，无法实时编辑。为真正普及3D动画，需一个快速直观、支持开放式文本指令且能即时反馈的系统，PromptVFX应运而生。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：将3D动画重构为场预测任务  
PromptVFX把3D动画重新定义为对3D高斯溅射（Gaussian Splatting）的时变变换任务，提出文本驱动框架，推断作用于3D高斯的时变4D流场。无需生成新几何或启动物理模拟器，通过对高斯溅射场景施加时变场，直接改变单个高斯的中心位置、颜色和不透明度等参数来实现特效，自然支持实时渲染。  

💡 创新点2：无训练的4D动画生成流程  
采用零样本工作流，借助大语言模型（LLM）和视觉 - 语言模型（VLM）解析自然语言指令。把自然语言指令分解为动画阶段，由LLM生成变换函数，再用视觉语言模型反馈优化，无需针对每个场景训练，就能实现如依据“让花瓶先橙色发光再爆炸”这类指令的动画效果。  

💡 创新点3：实时交互编辑体验  
直接更新高斯参数，省去了网格提取、扩散循环或物理模拟器等开销。在消费级设备甚至网页浏览器上，能在一分钟内完成动画生成，让用户即时看到文本指令带来的效果，无论新手还是专家都能轻松为体素场景制作动画。  

### 📈 实验结果
实验展示了对不同场景和用户指令的处理效果，简单文本指令就能生成引人入胜的时变VFX。与现有文本驱动3D动画方法对比（如图1所示），PromptVFX能在数秒内生成高质量动画，而其他依赖扩散或物理模拟的方法需多30倍时间。同时，在涵盖输入输出、编辑能力、系统属性等多维度的方法对比表（表1）中，PromptVFX是唯一同时满足所有特性且支持用户交互细化的方法。  

### 💬 可借鉴之处
从技术创新看，其将3D动画与场预测结合、利用大模型实现零样本4D动画生成的思路，为3D内容生成领域提供了新范式，摆脱对传统耗时模拟和训练的依赖；从应用普及角度，实时交互、开放式文本指令的设计，降低了3D动画创作门槛，为VFX民主化铺路，让更广泛受众能参与3D内容创作；在工程实现上，直接操作高斯参数实现实时渲染的方式，为实时图形编辑类应用提供了高效交互的参考方向。 

## vision-language-models-are-biased
### Abstract
Large language models (LLMs) memorize a vast amount of prior knowledge from
the Internet that help them on downstream tasks but also may notoriously sway
their outputs towards wrong or biased answers. In this work, we test how the
knowledge about popular subjects hurt the accuracy of vision language models
(VLMs) on standard, objective visual tasks of counting and identification. We
find that state-of-the-art VLMs are strongly biased (e.g, unable to recognize a
fourth stripe has been added to a 3-stripe Adidas logo) scoring an average of
17.05% accuracy in counting (e.g., counting stripes in an Adidas-like logo)
across 7 diverse domains from animals, logos, chess, board games, optical
illusions, to patterned grids. Insert text (e.g., "Adidas") describing the
subject name into the counterfactual image further decreases VLM accuracy. The
biases in VLMs are so strong that instructing them to double-check their
results or rely exclusively on image details to answer improves counting
accuracy by only +2 points, on average. Our work presents an interesting
failure mode in VLMs and an automated framework for testing VLM biases. Code
and data are available at: vlmsarebiased.github.io.
### 🌟 论文解读 | 揭示视觉语言模型中的偏见：VLMs在客观视觉任务上的表现缺陷

### 📌 背景痛点/本文动机
大语言模型（LLMs）从互联网中记忆了海量先验知识，这些知识虽有助于下游任务，但也可能导致输出存在错误或偏见。视觉语言模型（VLMs）因预训练方式（基于纯文本或多模态数据），可能从文本语料继承强偏见，而此前关于VLM偏见的研究多针对含偏向性陈述的人工是非题，未明确图像和文本提示对错误答案的影响，也未探究偏见对客观视觉任务的作用。本文旨在评估LLMs对常见主题的知识如何给VLMs在目标视觉问题（计数、识别等）上的准确性带来负面影响。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出VLMBias框架  
利用前沿图像编辑器、VLMs和图像处理库，自动化枚举和生成带偏见的主题、问题与反事实图像，涵盖动物、标志、旗帜、国际象棋棋子、游戏棋盘、视错觉、图案网格7个领域，还手动审查图像保证质量。  
💡 创新点2：全面测试多类视觉任务与VLMs  
针对计数、识别等客观视觉任务，测试5个主流VLMs（如Gemini - 2.5 Pro、GPT - 4.1等），探究在反事实图像下模型表现，还研究添加主题名称文本、引导模型仅依赖图像细节等操作对结果的影响。  

### 📈 实验结果
1. 原始未修改图像上，所有5个VLMs对VLMBias主题的识别和计数问题准确率达100%；但面对反事实图像时表现差，如给2腿、4腿动物加额外腿后，计数准确率分别低至1.01%、2.50%。  
2. 知名品牌标志、旗帜等修改视觉元素后，VLMs计数准确率极低，汽车标志反事实图像上准确率仅0.44%；视错觉任务中，模型能识别原知名错觉名称，却无法察觉修改后图形变化，准确率接近随机；图案网格任务因无互联网先验信息，模型也表现不佳。  
3. 识别类是非题中VLMs同样表现挣扎；给反事实图像加主题名称文本，计数准确率再降2 - 6个点；引导模型仅依赖图像细节或二次检查，计数准确率平均仅提升2个点左右，凸显偏见之强。  

### 💬 可借鉴之处
1. 提出的VLMBias框架为测试VLM偏见提供了自动化方案，后续研究可基于此拓展更多测试场景与任务，深入分析VLM偏见来源与机制。  
2. 对多领域、多任务、多模型的测试方式，为评估AI模型在真实场景下的鲁棒性提供了全面范例，可指导其他模型评估工作设计更丰富的实验。  
3. 关于文本提示、引导策略对VLM偏见影响的研究，为优化VLM prompting策略提供了实证依据，助力后续提升模型在实际应用中应对偏见的能力。

## videogamebench--can-vision-language-models-complete-popular-video-games-
### Abstract
Vision-language models (VLMs) have achieved strong results on coding and math
benchmarks that are challenging for humans, yet their ability to perform tasks
that come naturally to humans--such as perception, spatial navigation, and
memory management--remains understudied. Real video games are crafted to be
intuitive for humans to learn and master by leveraging innate inductive biases,
making them an ideal testbed for evaluating such capabilities in VLMs. To this
end, we introduce VideoGameBench, a benchmark consisting of 10 popular video
games from the 1990s that VLMs directly interact with in real-time.
VideoGameBench challenges models to complete entire games with access to only
raw visual inputs and a high-level description of objectives and controls, a
significant departure from existing setups that rely on game-specific
scaffolding and auxiliary information. We keep three of the games secret to
encourage solutions that generalize to unseen environments. Our experiments
show that frontier vision-language models struggle to progress beyond the
beginning of each game. We find inference latency to be a major limitation of
frontier models in the real-time setting; therefore, we introduce
VideoGameBench Lite, a setting where the game pauses while waiting for the LM's
next action. The best performing model, Gemini 2.5 Pro, completes only 0.48% of
VideoGameBench and 1.6% of VideoGameBench Lite. We hope that the formalization
of the human skills mentioned above into this benchmark motivates progress in
these research directions.
### 🌟 论文解读 | VideoGameBench：用经典游戏挑战视觉语言模型的“人类级”能力

### 📌 背景痛点/本文动机
视觉-语言模型（VLMs）在编程、数学等对人类有挑战的任务上取得了亮眼成绩，但在**感知、空间导航、记忆管理**这类人类天生就擅长的能力上，研究仍不充分。而90年代的经典电子游戏是为人类“直觉学习”设计的——利用了人类先天的归纳偏好（比如空间感知、记忆留存），因此成为评估VLMs这类能力的理想测试床。于是，论文团队提出了VideoGameBench，试图用真实电子游戏场景，检验VLMs是否能接近人类在这类“自然任务”上的表现。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建真实复杂的游戏基准测试集  
VideoGameBench包含10款90年代流行游戏（涵盖Game Boy掌机和PC DOS平台），要求模型仅通过**原始视觉输入** + **高层级的目标与控制说明**来实时交互通关。相比过往“网格世界”“纯文字游戏”类基准，它的环境更复杂、更贴近真实人类交互场景，且是首批聚焦90年代电子游戏的AI基准之一。  

💡 创新点2：强调泛化性与无辅助评估  
测试集中保留3款“秘密游戏”，专门检验模型对未见过环境的泛化能力；同时**不允许任何游戏专属脚手架、辅助信息（如路径提示、视觉覆盖层）**，只给原始画面和基础控制说明，彻底考验模型“裸奔”解决问题的能力。  

💡 创新点3：解决实时性痛点的Lite版本 + 新颖进度评估法  
考虑到前沿模型推理延迟在实时游戏中是硬伤，团队推出VideoGameBench Lite——游戏在等待模型动作时暂停，消除延迟干扰。此外，还提出**基于YouTube通关视频时间戳 + 感知哈希**的进度检测方法：爬取游戏通关视频，用时间戳标注“里程碑-画面帧”对，再通过感知哈希匹配模型实际游戏画面，判断进度。这套方法让后续扩展新游戏任务更便捷。  


### 📈 实验结果
前沿VLMs在VideoGameBench上表现极差：即便是表现最好的Gemini 2.5 Pro，在标准VideoGameBench上仅完成**0.48%**的游戏进度，在消除延迟的Lite版本中也只完成**1.6%**。且多数模型在“鼠标移动、基础导航”等简单练习游戏中也表现拉胯，说明当前VLMs距离人类“自然掌握游戏”的能力还有极大差距。  


### 💬 可借鉴之处
1. **任务设计视角**：把“人类天生擅长的感知/空间/记忆任务”转化为“电子游戏通关”这样的具象化基准，为评估AI与人类归纳偏好的对齐度提供了新思路。  
2. **基准构建思路**：用“真实复杂环境+泛化测试+无辅助约束”的组合拳，逼迫模型暴露能力短板；Lite版本则通过“暂停机制”分离“实时性”这一变量，让实验更具解释力。  
3. **评估方法论**：基于YouTube通关视频的进度检测法，为“如何量化AI在开放任务中的表现”提供了可复用的技术路线，降低了后续构建类似游戏/交互类基准的门槛。  


这篇论文用“复古游戏”这一趣味载体，撕开了当前VLMs在“类人感知与交互”能力上的遮羞布，也为未来研究指明了“补全人类级归纳偏好”的方向——毕竟，连《塞尔达》《超级马里奥》的开头都过不了，谈“类人智能”还太早~

## videogameqa-bench--evaluating-vision-language-models-for-video-game-quality-assurance
### Abstract
With video games now generating the highest revenues in the entertainment
industry, optimizing game development workflows has become essential for the
sector's sustained growth. Recent advancements in Vision-Language Models (VLMs)
offer considerable potential to automate and enhance various aspects of game
development, particularly Quality Assurance (QA), which remains one of the
industry's most labor-intensive processes with limited automation options. To
accurately evaluate the performance of VLMs in video game QA tasks and
determine their effectiveness in handling real-world scenarios, there is a
clear need for standardized benchmarks, as existing benchmarks are insufficient
to address the specific requirements of this domain. To bridge this gap, we
introduce VideoGameQA-Bench, a comprehensive benchmark that covers a wide array
of game QA activities, including visual unit testing, visual regression
testing, needle-in-a-haystack tasks, glitch detection, and bug report
generation for both images and videos of various games. Code and data are
available at: https://asgaardlab.github.io/videogameqa-bench/
### 🌟 论文解读 | VideoGameQA-Bench：为游戏质量保障评估视觉语言模型

### 📌 背景痛点/本文动机
全球电子游戏产业规模持续扩张，预计到2028年市值将达2570亿美元，但游戏开发中保障视觉质量与一致性的QA流程仍高度依赖人工，耗时、昂贵且易出错。视觉语言模型（VLMs）虽为游戏QA自动化带来希望，然而现有基准测试要么侧重复杂数学或文本推理、忽视游戏QA核心视觉理解任务，要么仅覆盖QA任务的狭窄方面，无法全面评估VLMs在多样QA场景下的表现。因此，打造贴合游戏QA场景的标准化基准成为关键。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建VideoGameQA - Bench基准  
针对真实游戏开发场景，设计涵盖9类不同任务、包含4786个问题的VideoGameQA - Bench。任务覆盖视觉单元测试、回归测试、UI验证、视频“大海捞针”找 glitch、 glitch检测等，包含2236个基于图像和1200个基于视频的样本，素材来自超800款游戏与9个合成游戏场景。  
💡 创新点2：全面覆盖游戏QA活动类型  
将游戏视觉QA任务抽象为三类并对应设计任务：验证场景完整性（如视觉单元、回归测试）、无参考点的glitch检测（依靠常识）、 glitch报告生成；细分出图像与视频维度下的各类子任务，如针对游戏中常见的clipping问题设计参数化clipping检测任务等，全方位考察VLMs在游戏QA各环节能力。

### 📈 实验结果
1. VLMs在多模态基准表现不错且能做OCR，但在精确场景理解（识别精细细节）与解析复杂UI元素上表现差；  
2. 前沿VLMs在图像glitch检测（最高82.8%）、视频glitch检测（最高78.1%）有不错表现，但面对身体姿态、复杂物体clipping、常识推理类glitch仍吃力；  
3. 视觉回归测试对VLMs而言依旧是极富挑战的任务；  
4. 在视频中定位特定glitch时刻（检测+精准定位）仍具难度；  
5. 前沿VLMs能为约50%真实glitch生成有用bug报告，提供准确描述性总结。  

### 💬 可借鉴之处
1. 填补领域空白：首次针对性构建游戏QA方向VLMs评估基准，为该领域后续模型研发、优化提供了标准化评估工具与参考依据；  
2. 任务设计思路：从真实产业流程中抽象任务类型并转化为模型可评估的形式，这种贴合产业实际场景的基准构建思路，可为其他垂直领域（如影视制作QA、工业设计视觉检测等）打造AI评估基准提供借鉴；  
3. 实验分析价值：对VLMs在各游戏QA子任务上的表现优劣分析，能指导后续模型改进方向（如强化精细视觉理解、常识融合等），也让产业界清晰知晓当前技术在游戏QA自动化上的能力边界与潜力点。

## code2logic--game-code-driven-data-synthesis-for-enhancing-vlms-general-reasoning
### Abstract
Visual-language Chain-of-Thought (CoT) data resources are relatively scarce
compared to text-only counterparts, limiting the improvement of reasoning
capabilities in Vision Language Models (VLMs). However, high-quality
vision-language reasoning data is expensive and labor-intensive to annotate. To
address this issue, we leverage a promising resource: game code, which
naturally contains logical structures and state transition processes.
Therefore, we propose Code2Logic, a novel game-code-driven approach for
multimodal reasoning data synthesis. Our approach leverages Large Language
Models (LLMs) to adapt game code, enabling automatic acquisition of reasoning
processes and results through code execution. Using the Code2Logic approach, we
developed the GameQA dataset to train and evaluate VLMs. GameQA is
cost-effective and scalable to produce, challenging for state-of-the-art
models, and diverse with 30 games and 158 tasks. Surprisingly, despite training
solely on game data, VLMs demonstrated out of domain generalization,
specifically Qwen2.5-VL-7B improving performance by 2.33\% across 7 diverse
vision-language benchmarks. Our code and dataset are available at
https://github.com/tongjingqi/Code2Logic.
### 🌟 论文解读 | Code2Logic：用游戏代码驱动数据合成，提升视觉语言模型推理能力

### 📌 背景痛点/本文动机
视觉语言模型（VLMs）在图像描述、视觉问答等基础任务上取得了不错进展，但面对需要多步推理的复杂视觉任务时仍存在不足。关键原因在于**高质量多模态推理数据稀缺**，限制了模型推理能力提升。当前构建这类数据的方法，要么依赖人工标注（存在数据少或成本高问题），要么用神经网络自动合成（推理准确性难保证）、符号引擎（领域特定性强、迁移成本高），现有方案难以同时满足规模、质量、低成本的需求。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出Code2Logic框架，利用游戏代码生成多模态推理数据  
游戏天然包含清晰规则、状态转移逻辑与因果推理链，且代码易验证正确性。Code2Logic借助大语言模型（LLMs）实现三步核心流程：  
- 用LLMs把“非形式化的游戏逻辑”转化为可执行代码；  
- 结合LLM辅助人类设计QA模板，从代码里提取推理模式；  
- 再用LLMs开发数据引擎程序，复用核心游戏代码、规模化实例化模板，产出最终数据样本。通过这套流程，把游戏代码里的隐式推理转化为显式的多模态推理数据样本。  

💡 创新点2：构建GameQA数据集用于VLMs训练与评估  
基于Code2Logic生成了GameQA数据集，它有三大优势：  
- **成本低且可扩展**：代码一旦搭建，能以极低计算开销生成大量样本，比人工标注成本低很多；  
- **挑战性强**：现有顶尖模型在GameQA测试集上准确率不足50%；  
- **规模大且多样**：涵盖30种游戏、158个任务、3万道题，覆盖3D空间理解、模式识别匹配、多步推理、策略规划等认知技能，还按问题复杂度和图像复杂度做了细分。  


### 📈 实验结果
在模型泛化性测试上，仅用游戏数据训练的VLMs展现出跨领域能力：  
- 对训练时没见过的游戏类型，Qwen2.5 - VL - 7B性能提升3.83%；  
- 在7个不同的视觉 - 语言基准测试中，整体性能提升2.33%。  
这说明GameQA训练数据能有效增强模型在多场景下的推理能力，验证了Code2Logic方法的价值。  


### 💬 可借鉴之处
1. **数据合成思路创新**：把游戏代码这类“天然含逻辑结构”的资源引入多模态推理数据构建，为解决数据稀缺问题提供了全新视角——挖掘领域内隐含逻辑的“现成资源”，用LLMs转化为模型可用数据；  
2. **流程可复用性**：Code2Logic的“LLM辅助代码生成→模板设计→规模化实例化”流程，可迁移到其他有“规则/逻辑可编码”的领域（如教育题、模拟仿真场景），为垂直领域多模态数据构建提供参考；  
3. **数据集价值**：GameQA不仅用于训练，还能评估模型复杂推理能力，这种“既训又测”且覆盖多认知维度的数据集建设思路，对推动VLMs推理研究有借鉴意义。  

## g1--bootstrapping-perception-and-reasoning-abilities-of-vision-language-model-via-reinforcement-learning
### Abstract
Vision-Language Models (VLMs) excel in many direct multimodal tasks but
struggle to translate this prowess into effective decision-making within
interactive, visually rich environments like games. This ``knowing-doing'' gap
significantly limits their potential as autonomous agents, as leading VLMs
often performing badly in simple games. To address this, we introduce VLM-Gym,
a curated reinforcement learning (RL) environment featuring diverse visual
games with unified interfaces and adjustable, compositional difficulty,
specifically designed for scalable multi-game parallel training. Leveraging
VLM-Gym, we train G0 models using pure RL-driven self-evolution, which
demonstrate emergent perception and reasoning patterns. To further mitigate
challenges arising from game diversity, we develop G1 models. G1 incorporates a
perception-enhanced cold start prior to RL fine-tuning. Our resulting G1 models
consistently surpass their teacher across all games and outperform leading
proprietary models like Claude-3.7-Sonnet-Thinking. Systematic analysis reveals
an intriguing finding: perception and reasoning abilities mutually bootstrap
each other throughout the RL training process. Source code including VLM-Gym
and RL training are released at https://github.com/chenllliang/G1 to foster
future research in advancing VLMs as capable interactive agents.
### 🌟 论文解读 | G1：用强化学习赋能视觉语言模型的感知与推理能力

### 📌 背景痛点/本文动机
视觉语言模型（VLMs）在诸多直接的多模态任务中表现出色，但在像游戏这类交互式、视觉信息丰富的环境里，却难以将自身能力转化为有效的决策，存在“知与行”的差距，这极大限制了它们作为自主智能体的潜力，即便顶尖VLMs在简单游戏中表现也不佳。同时，现有针对VLMs在交互式游戏中强化学习训练的有效且可扩展框架缺失，感知与推理能力在其中能带来的潜在收益也不明晰。为解决这些问题，论文开展了相关研究。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出VLM - Gym强化学习环境  
打造了包含多种视觉游戏（如2048、Shisen - Sho等）的强化学习环境VLM - Gym，具备可扩展环境（支持多游戏状态、多游戏同时并行执行，助力多任务强化学习研究与大规模批量训练）、并行动作（支持对同一观测并行采样多个动作并计算对应奖励，为适配基础模型的先进RL算法提供支持）、组合式难度（各游戏难度在感知复杂度、推理深度等多维度可调且能组合，便于研究VLMs在RL场景下的泛化能力）等关键特性。  

💡 创新点2：训练G0与G1模型  
利用VLM - Gym，通过纯强化学习驱动自进化训练出G0模型，G0展现出了emergent的感知与推理模式；为应对游戏多样性带来的挑战，进一步提出G1模型，在强化学习微调前融入感知增强的冷启动以及来自教师模型的知识蒸馏，提升模型在各游戏中的表现。  

### 📈 实验结果
G0模型在训练中表现出有效的感知与推理模式，游戏表现大幅提升，如在Shisen - Sho游戏中分数从1.9提升到12.8，且超过OpenAI - o1、Qwen2.5VL - 72B等强多模态模型；G1模型在所有游戏中都超越了其教师模型，还显著超过了如Claude - 3.7 - Sonnet - Thinking这样的顶尖专有模型。此外，通过对G0和G1感知与推理准确率的解耦分析，发现感知和推理能力在RL训练过程中相互引导提升。  

### 💬 可借鉴之处
1. 环境构建层面：VLM - Gym的设计思路为打造针对特定模型（如VLMs）的强化学习训练环境提供了参考，其可扩展、支持并行动作与组合难度调节等特性，对于需要在多任务、复杂交互场景下训练的模型环境构建很有启发。  
2. 模型训练层面：利用强化学习实现模型自进化以及结合感知增强冷启动和知识蒸馏来提升模型在复杂多样任务中表现的思路，可为提升其他类型模型在交互式、多任务场景下的能力提供借鉴。  
3. 研究视角层面：对感知和推理能力在训练过程中相互作用的分析，为后续研究模型能力之间的关联与协同提升提供了新的思考角度。  
4. 开源贡献层面：论文开源了VLM - Gym和RL训练等代码，为该领域后续研究提供了便利，这种开源促进研究发展的模式值得学习。

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
### 🌟 论文解读 | DSADF：快慢思维双系统赋能决策智能

### 📌 背景痛点/本文动机
强化学习（RL）智能体在明确定义的环境中表现出色，但依赖试错交互的特性使其在动态场景下泛化能力不足。尽管已有研究尝试用大语言模型（LLMs）或视觉语言模型（VLMs）辅助RL提升泛化性，却存在RL智能体与基础模型协作不流畅、陌生环境决策不合理、效率瓶颈等问题。如何充分发挥基础模型推理能力与RL快速响应能力并增强二者互动，仍是待解难题。为此，论文受卡尼曼“快思考（System 1）与慢思考（System 2）”理论启发，探索在复杂世界中平衡直觉与深度推理以实现灵活决策的路径。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出双系统自适应决策框架（DSADF）  
DSADF整合两个互补模块：System 1由RL智能体与记忆空间构成，负责快速直观决策；System 2由VLM驱动，开展深度分析推理。借由双系统协作，充分发挥各自优势实现高效自适应决策。

💡 创新点2：双系统协作机制设计  
System 2利用基础模型强大推理能力，从指令提示中提取线索，将长周期初始任务拆解为可管理的单步任务，让RL智能体聚焦单步任务求解以提升学习与执行效率；同时VLM依据历史步骤持续更新记忆模块，评估RL对不同单步任务的熟练度，测试时精准分配任务，还能基于目标和观测生成目标导向指令助力RL能力提升。

### 📈 实验结果
在视频游戏环境Crafter和Housekeep中开展实证研究，验证了DSADF的有效性。实验里双系统协同工作，在长周期任务与未见过的任务场景下，决策能力均有显著提升，展现出在效率与泛化性上的优异表现。

### 💬 可借鉴之处
1. 跨领域理论迁移：将认知科学中“快慢思考”理论引入强化学习与基础模型结合的研究，为解决智能体泛化和协作难题提供新视角，启发后续跨学科融合类研究思路拓展。  
2. 模块化协作范式：DSADF的双系统模块化设计，清晰划分快速响应与深度推理职能并构建互动机制，为多智能体或多模型协作完成复杂任务提供了可参考的架构范式，便于后续研究者在此基础上优化模块交互逻辑等。  
3. 任务拆解与动态适配：借助VLM做任务拆解、记忆更新与指令生成，让RL专注单步优势领域，这种“分解 - 适配 - 提升”的思路，对处理长周期、稀疏奖励等强化学习难点任务具有借鉴价值，可指导类似复杂任务分解与智能体能力适配方案设计。 

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


