# Paper List of Terms(Robotics+Navigation)
- [25/06] **FindingDory: A Benchmark to Evaluate Memory in Embodied Agents**  
[[Paper](http://arxiv.org/pdf/2506.15635v1)] [[Code/Page]()] [[TLDR/Notes](#findingdory--a-benchmark-to-evaluate-memory-in-embodied-agents)]

- [25/06] **Real-Time Initialization of Unknown Anchors for UWB-aided Navigation**  
[[Paper](http://arxiv.org/pdf/2506.15518v1)] [[Code/Page]()] [[TLDR/Notes](#real-time-initialization-of-unknown-anchors-for-uwb-aided-navigation)]

- [25/06] **SurfAAV: Design and Implementation of a Novel Multimodal Surfing Aquatic-Aerial Vehicle**  
[[Paper](http://arxiv.org/pdf/2506.15450v1)] [[Code/Page]()] [[TLDR/Notes](#surfaav--design-and-implementation-of-a-novel-multimodal-surfing-aquatic-aerial-vehicle)]



# TLDR/Notes
## findingdory--a-benchmark-to-evaluate-memory-in-embodied-agents
### Abstract
Large vision-language models have recently demonstrated impressive
performance in planning and control tasks, driving interest in their
application to real-world robotics. However, deploying these models for
reasoning in embodied contexts is limited by their ability to incorporate
long-term experience collected across multiple days and represented by vast
collections of images. Current VLMs typically struggle to process more than a
few hundred images concurrently, highlighting the need for more efficient
mechanisms to handle long-term memory in embodied settings. To effectively
evaluate these models for long-horizon control, a benchmark must specifically
target scenarios where memory is crucial for success. Existing long-video QA
benchmarks overlook embodied challenges like object manipulation and
navigation, which demand low-level skills and fine-grained reasoning over past
interactions. Moreover, effective memory integration in embodied agents
involves both recalling relevant historical information and executing actions
based on that information, making it essential to study these aspects together
rather than in isolation. In this work, we introduce a new benchmark for
long-range embodied tasks in the Habitat simulator. This benchmark evaluates
memory-based capabilities across 60 tasks requiring sustained engagement and
contextual awareness in an environment. The tasks can also be procedurally
extended to longer and more challenging versions, enabling scalable evaluation
of memory and reasoning. We also present baselines that integrate
state-of-the-art VLMs with low level navigation policies, assessing their
performance on these memory-intensive tasks and highlight areas for
improvement.
### 🌟 论文解读 | FindingDory：评估具身智能体记忆能力的新基准

### 📌 背景痛点/本文动机
在人工智能领域，大视觉 - 语言模型（VLMs）在规划和控制任务中展现出了令人瞩目的性能，这也推动了其在现实世界机器人领域的应用探索。然而，将这些模型部署到具身情境中进行推理时，它们整合长期经验（这些经验由数天收集的海量图像表示）的能力成为了限制因素。当前的 VLMs 通常难以同时处理几百张以上的图像，这凸显了在具身场景中需要更高效的机制来处理长期记忆。

现有的长视频问答基准忽略了诸如对象操作和导航等具身挑战，这些挑战需要低级技能和对过去交互的细粒度推理。而且，具身智能体中有效的记忆整合既涉及回忆相关历史信息，又要基于该信息执行动作，所以必须将这些方面结合起来研究，而非孤立看待。因此，为了有效评估这些模型在长时程控制中的表现，需要一个专门针对记忆对成功至关重要的场景的基准，这就是本文工作的动机。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：提出 FindingDory 基准  
在 Habitat 模拟器中引入了用于长程具身任务的新基准。该基准包含 60 个任务，这些任务评估基于记忆的能力，要求智能体在环境中持续参与并具备情境感知能力。任务还可以通过程序扩展为更长、更具挑战性的版本，从而实现对记忆和推理的可扩展评估。与依赖主观人类标注的标准 QA 数据集不同，该基准利用照片级真实感模拟实现对基于记忆的导航的自动、客观评估，任务要求智能体对过去的交互进行复杂的时空推理，而不仅仅是静态回忆。

💡 创新点2：结合前沿 VLMs 与低层次导航策略的基线  
提出了整合最先进的 VLMs 和低层次导航策略的基线，评估它们在这些内存密集型任务上的性能，并突出需要改进的领域。通过这种方式，全面评估了基于 VLM 的高层策略与低层导航策略结合后的表现，分析其在内存密集型任务中的性能和局限性。

💡 创新点3：构建系统且可扩展的评估框架  
打造了一个系统且可扩展的评估框架，其包含的指标能够为未来内存高效的具身智能体的发展提供支持。该框架下的任务设计旨在将性能与内存利用直接关联，而非简单的感知，通过精心策划场景，要求智能体必须回忆过去的交互才能成功，并且场景是动态的（智能体交互会修改场景），这使得对变化情境的推理至关重要。

### 📈 实验结果
文中通过将整合后的基线（最先进 VLMs + 低层次导航策略）在 FindingDory 基准的任务上进行测试，评估它们在这些记忆密集型任务上的性能，进而突出模型在处理长期记忆、时空推理等方面需要改进的领域。不过文中未详细披露具体的数值类实验结果对比，重点在于呈现该基准对具身智能体记忆能力评估的有效性以及基线在任务中暴露的问题，为后续研究指明方向。

### 💬 可借鉴之处
1. 基准构建思路：FindingDory 针对具身智能体长期记忆评估的空白，构建了包含多样任务且可扩展的基准，这种针对特定能力缺口构建评估基准的思路，可为其他人工智能子领域（如强化学习中特定能力评估）提供参考，即先明确领域中关键能力的评估不足，再针对性构建场景丰富、可扩展的评估体系。
2. 多组件结合评估：将高层的视觉 - 语言模型与低层导航策略结合评估的方式，为复杂智能系统的性能评估提供了思路。在实际的智能系统开发中，往往是多个模块协同工作，这种多组件结合评估能更真实地反映系统在实际任务中的表现，可借鉴到如自动驾驶系统中不同感知、决策模块结合评估等场景。
3. 动态场景与自动评估：利用照片级真实感模拟实现自动、客观评估，且场景设计为动态（智能体交互改变场景），这为评估智能体在更接近真实世界（动态变化）的环境中的能力提供了范式，可用于各类需要模拟真实环境的智能体评估任务中，减少人工标注依赖且提升评估真实性。

## real-time-initialization-of-unknown-anchors-for-uwb-aided-navigation
### Abstract
This paper presents a framework for the real-time initialization of unknown
Ultra-Wideband (UWB) anchors in UWB-aided navigation systems. The method is
designed for localization solutions where UWB modules act as supplementary
sensors. Our approach enables the automatic detection and calibration of
previously unknown anchors during operation, removing the need for manual
setup. By combining an online Positional Dilution of Precision (PDOP)
estimation, a lightweight outlier detection method, and an adaptive robust
kernel for non-linear optimization, our approach significantly improves
robustness and suitability for real-world applications compared to
state-of-the-art. In particular, we show that our metric which triggers an
initialization decision is more conservative than current ones commonly based
on initial linear or non-linear initialization guesses. This allows for better
initialization geometry and subsequently lower initialization errors. We
demonstrate the proposed approach on two different mobile robots: an autonomous
forklift and a quadcopter equipped with a UWB-aided Visual-Inertial Odometry
(VIO) framework. The results highlight the effectiveness of the proposed method
with robust initialization and low positioning error. We open-source our code
in a C++ library including a ROS wrapper.
### 🌟 论文解读 | UWB辅助导航中未知锚点的实时初始化：自动化、鲁棒性与多平台验证

### 📌 背景痛点/本文动机
在GNSS（全球导航卫星系统）受限的环境中，自主系统的定位需依赖替代方案，UWB（超宽带）技术因能通过测量距离实现定位而成为热门选择。但传统UWB辅助导航系统中，锚点（anchor）位置需人工预校准，在大规模部署等场景下既耗时又不现实。此外，现有锚点初始化决策的指标往往过于自信，易导致锚点初始位置猜测差甚至退化，影响后续导航精度。因此，本文旨在提出一套框架，实现未知UWB锚点的实时自动检测与校准，摆脱人工设置依赖，提升真实场景下的鲁棒性与适用性。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：全自动化且易集成的未知锚点初始化框架  
提出一套端到端框架，能在UWB辅助导航系统运行过程中，自动检测并可靠估计此前未知的UWB锚点位置，无需人工介入校准，可直接集成到现有导航方案中，为UWB辅助导航的“即插即用”锚点初始化提供支持。  

💡 创新点2：基于实时PDOP估计的初始化决策机制  
引入**实时位置精度衰减因子（PDOP）估计**，以“锚点最近点”为基础计算PDOP，当几何构型满足精确初始化要求（PDOP低于阈值）时触发初始化。相比传统基于线性/非线性初始猜测的决策指标，该机制更保守，能保障更优的初始化几何结构，降低初始化误差。  

💡 创新点3：轻量离群点检测+自适应鲁棒核优化的组合策略  
结合轻量级在线离群点检测方法保障数据完整性（即便在计算资源受限的平台也能高效运行），再通过自适应鲁棒核的非线性最小二乘（NLS）方法对锚点位置先做最小二乘（LS）初估、再做精修，有效缓解残余离群点与噪声波动的影响，提升估计鲁棒性。  


### 📈 实验结果
论文通过**仿真+真实世界实验**验证方法有效性：  
- 平台覆盖两类移动机器人：自动叉车（AMR）与四旋翼无人机（UAV）。其中自动叉车结合GPS与轮式里程计定位，无人机则基于开源UWB辅助视觉惯性里程计（UVIO）框架。  
- 结果表明，该方法在未知锚点初始化任务中鲁棒性强，能应对差初始化场景，且定位误差低，充分证明了框架在不同平台、不同导航方案下的适配性与可靠性。  


### 💬 可借鉴之处
1. 技术方案层面：将PDOP实时估计与鲁棒优化策略结合，为传感器（尤其是UWB）在导航中“未知锚点在线初始化”这一工程难题提供了完整且可落地的技术路径，可启发同类“传感器辅助定位中未知参考节点校准”类问题的解法设计。  
2. 工程落地层面：开源C++库（含ROS封装）降低了行业复用门槛，为科研与工业界快速验证UWB辅助导航系统的锚点自动初始化功能提供了工具链支持。  
3. 实验设计层面：同时在地面移动机器人与无人机两类平台验证，且覆盖不同基础导航方案（GPS+轮式里程计、视觉惯性里程计），这种“多平台+多基线”的验证思路，能更全面地展现方法普适性，值得同类算法验证借鉴。  

## surfaav--design-and-implementation-of-a-novel-multimodal-surfing-aquatic-aerial-vehicle
### Abstract
Despite significant advancements in the research of aquatic-aerial robots,
existing configurations struggle to efficiently perform underwater, surface,
and aerial movement simultaneously. In this paper, we propose a novel
multimodal surfing aquatic-aerial vehicle, SurfAAV, which efficiently
integrates underwater navigation, surface gliding, and aerial flying
capabilities. Thanks to the design of the novel differential thrust vectoring
hydrofoil, SurfAAV can achieve efficient surface gliding and underwater
navigation without the need for a buoyancy adjustment system. This design
provides flexible operational capabilities for both surface and underwater
tasks, enabling the robot to quickly carry out underwater monitoring
activities. Additionally, when it is necessary to reach another water body,
SurfAAV can switch to aerial mode through a gliding takeoff, flying to the
target water area to perform corresponding tasks. The main contribution of this
letter lies in proposing a new solution for underwater, surface, and aerial
movement, designing a novel hybrid prototype concept, developing the required
control laws, and validating the robot's ability to successfully perform
surface gliding and gliding takeoff. SurfAAV achieves a maximum surface gliding
speed of 7.96 m/s and a maximum underwater speed of 3.1 m/s. The prototype's
surface gliding maneuverability and underwater cruising maneuverability both
exceed those of existing aquatic-aerial vehicles.
### 🌟 论文解读 | SurfAAV：多模态水空航行器的创新设计与实现

### 📌 背景痛点/本文动机
近年来，无人水空航行器（UAAVs）因能适应复杂环境、执行多样化任务成为研究热点，这类航行器整合了自主水下航行器（AUVs）与无人机（UAVs）优势，可在水空间自由切换运动模式，在环境监测、救灾、国防等多领域有巨大潜力。但现有UAAVs在水下、水面、空中高效运动兼顾上存在不足：仿生型续航或自主跨介质能力有限；多旋翼型水下航行阻力大效率低；固定翼型水下或水面机动性欠佳；混合型也难在水面与水下快速机动，限制了大范围水域覆盖与跨水域作业能力。因此，本文旨在提出新方案，设计兼具水空高效机动能力的多模态航行器SurfAAV。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：多模态能力整合  
提出新型多模态冲浪式水空航行器SurfAAV，高效整合了水下航行、水面滑行、空中飞行能力，能灵活应对不同任务场景，比如水下监测后，可滑行起飞切换到空中模式飞往目标水域作业。  

💡 创新点2：差分推力矢量水翼设计  
设计新颖的差分推力矢量水翼，无需浮力调节系统就能实现高效水面滑行与水下航行，为水面和水下任务提供灵活操作能力，让机器人可快速开展水下监测等活动。  

💡 创新点3：控制律开发与原型验证  
给出水下、水面、空中运动的新解决方案，设计混合原型概念，开发所需控制律，并验证机器人水面滑行与滑行起飞能力，突破现有水空航行器在机动性能上的局限。  

### 📈 实验结果
SurfAAV性能表现突出，水面滑行最大速度达7.96 m/s，水下最大速度达3.1 m/s ；原型机的水面滑行机动性与水下巡航机动性均超过现有水空航行器；且实验验证了其能成功在水面滑行与滑行起飞，展现跨介质作业潜力。  

### 💬 可借鉴之处
从设计层面看，差分推力矢量水翼的无浮力调节系统设计思路，为解决水空航行器多场景高效运动难题提供了新方向，可启发后续类似跨介质机器人的结构创新；在多模态整合与控制上，其对水下、水面、空中运动模式的整体方案构建与控制律开发，为复杂环境下多任务执行的机器人系统设计提供了多场景协同的参考范式；性能验证环节也为相关水空航行器的性能评估与优化提供了实验方法与对比维度的借鉴，助力行业在跨介质机器人性能提升与场景拓展上持续探索。 

