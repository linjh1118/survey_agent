# Paper List of Terms(RL+Medical)
- [25/06] **Stable CDE Autoencoders with Acuity Regularization for Offline Reinforcement Learning in Sepsis Treatment**  
[[Paper](http://arxiv.org/pdf/2506.15019v1)] [[Code/Page]()] [[TLDR/Notes](#stable-cde-autoencoders-with-acuity-regularization-for-offline-reinforcement-learning-in-sepsis-treatment)]

- [25/06] **CAPO: Reinforcing Consistent Reasoning in Medical Decision-Making**  
[[Paper](http://arxiv.org/pdf/2506.12849v1)] [[Code/Page]()] [[TLDR/Notes](#capo--reinforcing-consistent-reasoning-in-medical-decision-making)]

- [25/06] **Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback**  
[[Paper](http://arxiv.org/pdf/2506.12323v1)] [[Code/Page]()] [[TLDR/Notes](#doctor-approved--generating-medically-accurate-skin-disease-images-through-ai-expert-feedback)]

- [25/06] **Palpation Alters Auditory Pain Expressions with Gender-Specific Variations in Robopatients**  
[[Paper](http://arxiv.org/pdf/2506.11906v1)] [[Code/Page]()] [[TLDR/Notes](#palpation-alters-auditory-pain-expressions-with-gender-specific-variations-in-robopatients)]

- [25/06] **RARL: Improving Medical VLM Reasoning and Generalization with Reinforcement Learning and LoRA under Data and Hardware Constraints**  
[[Paper](http://arxiv.org/pdf/2506.06600v2)] [[Code/Page]()] [[TLDR/Notes](#rarl--improving-medical-vlm-reasoning-and-generalization-with-reinforcement-learning-and-lora-under-data-and-hardware-constraints)]

- [25/06] **Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains**  
[[Paper](http://arxiv.org/pdf/2506.02126v1)] [[Code/Page]()] [[TLDR/Notes](#knowledge-or-reasoning--a-close-look-at-how-llms-think-across-domains)]

- [25/06] **MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning**  
[[Paper](http://arxiv.org/pdf/2506.00555v2)] [[Code/Page]()] [[TLDR/Notes](#mmedagent-rl--optimizing-multi-agent-collaboration-for-multimodal-medical-reasoning)]

- [25/05] **Learning optimal treatment strategies for intraoperative hypotension using deep reinforcement learning**  
[[Paper](http://arxiv.org/pdf/2505.21596v1)] [[Code/Page]()] [[TLDR/Notes](#learning-optimal-treatment-strategies-for-intraoperative-hypotension-using-deep-reinforcement-learning)]

- [25/05] **DoctorAgent-RL: A Multi-Agent Collaborative Reinforcement Learning System for Multi-Turn Clinical Dialogue**  
[[Paper](http://arxiv.org/pdf/2505.19630v1)] [[Code/Page](https://github.com/JarvisUSTC/DoctorAgent-RL)] [[TLDR/Notes](#doctoragent-rl--a-multi-agent-collaborative-reinforcement-learning-system-for-multi-turn-clinical-dialogue)]

- [25/05] **Improving Medical Reasoning with Curriculum-Aware Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.19213v1)] [[Code/Page]()] [[TLDR/Notes](#improving-medical-reasoning-with-curriculum-aware-reinforcement-learning)]



# TLDR/Notes
## stable-cde-autoencoders-with-acuity-regularization-for-offline-reinforcement-learning-in-sepsis-treatment
### Abstract
Effective reinforcement learning (RL) for sepsis treatment depends on
learning stable, clinically meaningful state representations from irregular ICU
time series. While previous works have explored representation learning for
this task, the critical challenge of training instability in sequential
representations and its detrimental impact on policy performance has been
overlooked. This work demonstrates that Controlled Differential Equations (CDE)
state representation can achieve strong RL policies when two key factors are
met: (1) ensuring training stability through early stopping or stabilization
methods, and (2) enforcing acuity-aware representations by correlation
regularization with clinical scores (SOFA, SAPS-II, OASIS). Experiments on the
MIMIC-III sepsis cohort reveal that stable CDE autoencoder produces
representations strongly correlated with acuity scores and enables RL policies
with superior performance (WIS return $> 0.9$). In contrast, unstable CDE
representation leads to degraded representations and policy failure (WIS return
$\sim$ 0). Visualizations of the latent space show that stable CDEs not only
separate survivor and non-survivor trajectories but also reveal clear acuity
score gradients, whereas unstable training fails to capture either pattern.
These findings highlight practical guidelines for using CDEs to encode
irregular medical time series in clinical RL, emphasizing the need for training
stability in sequential representation learning.


## capo--reinforcing-consistent-reasoning-in-medical-decision-making
### Abstract
In medical visual question answering (Med-VQA), achieving accurate responses
relies on three critical steps: precise perception of medical imaging data,
logical reasoning grounded in visual input and textual questions, and coherent
answer derivation from the reasoning process. Recent advances in general
vision-language models (VLMs) show that large-scale reinforcement learning (RL)
could significantly enhance both reasoning capabilities and overall model
performance. However, their application in medical domains is hindered by two
fundamental challenges: 1) misalignment between perceptual understanding and
reasoning stages, and 2) inconsistency between reasoning pathways and answer
generation, both compounded by the scarcity of high-quality medical datasets
for effective large-scale RL. In this paper, we first introduce Med-Zero-17K, a
curated dataset for pure RL-based training, encompassing over 30 medical image
modalities and 24 clinical tasks. Moreover, we propose a novel large-scale RL
framework for Med-VLMs, Consistency-Aware Preference Optimization (CAPO), which
integrates rewards to ensure fidelity between perception and reasoning,
consistency in reasoning-to-answer derivation, and rule-based accuracy for
final responses. Extensive experiments on both in-domain and out-of-domain
scenarios demonstrate the superiority of our method over strong VLM baselines,
showcasing strong generalization capability to 3D Med-VQA benchmarks and
R1-like training paradigms.


## doctor-approved--generating-medically-accurate-skin-disease-images-through-ai-expert-feedback
### Abstract
Paucity of medical data severely limits the generalizability of diagnostic ML
models, as the full spectrum of disease variability can not be represented by a
small clinical dataset. To address this, diffusion models (DMs) have been
considered as a promising avenue for synthetic image generation and
augmentation. However, they frequently produce medically inaccurate images,
deteriorating the model performance. Expert domain knowledge is critical for
synthesizing images that correctly encode clinical information, especially when
data is scarce and quality outweighs quantity. Existing approaches for
incorporating human feedback, such as reinforcement learning (RL) and Direct
Preference Optimization (DPO), rely on robust reward functions or demand
labor-intensive expert evaluations. Recent progress in Multimodal Large
Language Models (MLLMs) reveals their strong visual reasoning capabilities,
making them adept candidates as evaluators. In this work, we propose a novel
framework, coined MAGIC (Medically Accurate Generation of Images through
AI-Expert Collaboration), that synthesizes clinically accurate skin disease
images for data augmentation. Our method creatively translates expert-defined
criteria into actionable feedback for image synthesis of DMs, significantly
improving clinical accuracy while reducing the direct human workload.
Experiments demonstrate that our method greatly improves the clinical quality
of synthesized skin disease images, with outputs aligning with dermatologist
assessments. Additionally, augmenting training data with these synthesized
images improves diagnostic accuracy by +9.02% on a challenging 20-condition
skin disease classification task, and by +13.89% in the few-shot setting.


## palpation-alters-auditory-pain-expressions-with-gender-specific-variations-in-robopatients
### Abstract
Diagnostic errors remain a major cause of preventable deaths, particularly in
resource-limited regions. Medical training simulators, including robopatients,
play a vital role in reducing these errors by mimicking real patients for
procedural training such as palpation. However, generating multimodal feedback,
especially auditory pain expressions, remains challenging due to the complex
relationship between palpation behavior and sound. The high-dimensional nature
of pain sounds makes exploration challenging with conventional methods. This
study introduces a novel experimental paradigm for pain expressivity in
robopatients where they dynamically generate auditory pain expressions in
response to palpation force, by co-optimizing human feedback using machine
learning. Using Proximal Policy Optimization (PPO), a reinforcement learning
(RL) technique optimized for continuous adaptation, our robot iteratively
refines pain sounds based on real-time human feedback. This robot initializes
randomized pain responses to palpation forces, and the RL agent learns to
adjust these sounds to align with human preferences. The results demonstrated
that the system adapts to an individual's palpation forces and sound
preferences and captures a broad spectrum of pain intensity, from mild
discomfort to acute distress, through RL-guided exploration of the auditory
pain space. The study further showed that pain sound perception exhibits
saturation at lower forces with gender specific thresholds. These findings
highlight the system's potential to enhance abdominal palpation training by
offering a controllable and immersive simulation platform.


## rarl--improving-medical-vlm-reasoning-and-generalization-with-reinforcement-learning-and-lora-under-data-and-hardware-constraints
### Abstract
The growing integration of vision-language models (VLMs) in medical
applications offers promising support for diagnostic reasoning. However,
current medical VLMs often face limitations in generalization, transparency,
and computational efficiency-barriers that hinder deployment in real-world,
resource-constrained settings. To address these challenges, we propose a
Reasoning-Aware Reinforcement Learning framework, \textbf{RARL}, that enhances
the reasoning capabilities of medical VLMs while remaining efficient and
adaptable to low-resource environments. Our approach fine-tunes a lightweight
base model, Qwen2-VL-2B-Instruct, using Low-Rank Adaptation and custom reward
functions that jointly consider diagnostic accuracy and reasoning quality.
Training is performed on a single NVIDIA A100-PCIE-40GB GPU, demonstrating the
feasibility of deploying such models in constrained environments. We evaluate
the model using an LLM-as-judge framework that scores both correctness and
explanation quality. Experimental results show that RARL significantly improves
VLM performance in medical image analysis and clinical reasoning, outperforming
supervised fine-tuning on reasoning-focused tasks by approximately 7.78%, while
requiring fewer computational resources. Additionally, we demonstrate the
generalization capabilities of our approach on unseen datasets, achieving
around 27% improved performance compared to supervised fine-tuning and about 4%
over traditional RL fine-tuning. Our experiments also illustrate that diversity
prompting during training and reasoning prompting during inference are crucial
for enhancing VLM performance. Our findings highlight the potential of
reasoning-guided learning and reasoning prompting to steer medical VLMs toward
more transparent, accurate, and resource-efficient clinical decision-making.
Code and data are publicly available.


## knowledge-or-reasoning--a-close-look-at-how-llms-think-across-domains
### Abstract
Recent advances in reasoning-enhanced Large Language Models such as
OpenAI-o1/3 and DeepSeek-R1 have significantly improved performance on complex
tasks. However, the quality and transparency of their internal reasoning
processes remain underexplored. This work moves beyond the final-answer
accuracy and investigates step-by-step reasoning in the medical and
mathematical domains by explicitly decomposing the thinking trajectories into
two parts: knowledge and reasoning. Specifically, we introduce a fine-grained
evaluation framework that judges: (1) the correctness of knowledge used
(measured by Knowledge Index (KI)) and (2) the quality of reasoning (measured
by Information Gain (InfoGain)). Using this framework, we study R1-distilled
and base Qwen models trained with supervised fine-tuning (SFT) and/or
reinforcement learning (RL) in the medical and math domains. Three intriguing
findings emerge: (1) The general reasoning abilities in R1-distilled models do
not transfer effectively to the medical domain through either SFT or RL. (2)
SFT raises final-answer accuracy in both domains, but often at the cost of
reasoning quality: InfoGain drops by 38.9% on average compared with untrained
models; In the medical domain, however, SFT remains crucial because domain
knowledge is indispensable. (3) RL enhances medical reasoning by pruning
inaccurate or irrelevant knowledge from reasoning paths, thereby improving both
reasoning accuracy and knowledge correctness.


## mmedagent-rl--optimizing-multi-agent-collaboration-for-multimodal-medical-reasoning
### Abstract
Medical Large Vision-Language Models (Med-LVLMs) have shown strong potential
in multimodal diagnostic tasks. However, existing single-agent models struggle
to generalize across diverse medical specialties, limiting their performance.
Recent efforts introduce multi-agent collaboration frameworks inspired by
clinical workflows, where general practitioners (GPs) and specialists interact
in a fixed sequence. Despite improvements, these static pipelines lack
flexibility and adaptability in reasoning. To address this, we propose
MMedAgent-RL, a reinforcement learning (RL)-based multi-agent framework that
enables dynamic, optimized collaboration among medical agents. Specifically, we
train two GP agents based on Qwen2.5-VL via RL: the triage doctor learns to
assign patients to appropriate specialties, while the attending physician
integrates the judgments from multi-specialists and its own knowledge to make
final decisions. To address the inconsistency in specialist outputs, we
introduce a curriculum learning (CL)-guided RL strategy that progressively
teaches the attending physician to balance between imitating specialists and
correcting their mistakes. Experiments on five medical VQA benchmarks
demonstrate that MMedAgent-RL not only outperforms both open-source and
proprietary Med-LVLMs, but also exhibits human-like reasoning patterns.
Notably, it achieves an average performance gain of 20.7% over supervised
fine-tuning baselines.


## learning-optimal-treatment-strategies-for-intraoperative-hypotension-using-deep-reinforcement-learning
### Abstract
Traditional methods of surgical decision making heavily rely on human
experience and prompt actions, which are variable. A data-driven system
generating treatment recommendations based on patient states can be a
substantial asset in perioperative decision-making, as in cases of
intraoperative hypotension, for which suboptimal management is associated with
acute kidney injury (AKI), a common and morbid postoperative complication. We
developed a Reinforcement Learning (RL) model to recommend optimum dose of
intravenous (IV) fluid and vasopressors during surgery to avoid intraoperative
hypotension and postoperative AKI. We retrospectively analyzed 50,021 surgeries
from 42,547 adult patients who underwent major surgery at a quaternary care
hospital between June 2014 and September 2020. Of these, 34,186 surgeries were
used for model training and 15,835 surgeries were reserved for testing. We
developed a Deep Q-Networks based RL model using 16 variables including
intraoperative physiologic time series, total dose of IV fluid and vasopressors
extracted for every 15-minute epoch. The model replicated 69% of physician's
decisions for the dosage of vasopressors and proposed higher or lower dosage of
vasopressors than received in 10% and 21% of the treatments, respectively. In
terms of IV fluids, the model's recommendations were within 0.05 ml/kg/15 min
of the actual dose in 41% of the cases, with higher or lower doses recommended
for 27% and 32% of the treatments, respectively. The model resulted in a higher
estimated policy value compared to the physicians' actual treatments, as well
as random and zero-drug policies. AKI prevalence was the lowest in patients
receiving medication dosages that aligned with model's decisions. Our findings
suggest that implementation of the model's policy has the potential to reduce
postoperative AKI and improve other outcomes driven by intraoperative
hypotension.


## doctoragent-rl--a-multi-agent-collaborative-reinforcement-learning-system-for-multi-turn-clinical-dialogue
### Abstract
Large language models (LLMs) have demonstrated excellent capabilities in the
field of biomedical question answering, but their application in real-world
clinical consultations still faces core challenges. Existing systems rely on a
one-way information transmission mode where patients must fully describe their
symptoms in a single round, leading to nonspecific diagnostic recommendations
when complaints are vague. Traditional multi-turn dialogue methods based on
supervised learning are constrained by static data-driven paradigms, lacking
generalizability and struggling to intelligently extract key clinical
information. To address these limitations, we propose DoctorAgent-RL, a
reinforcement learning (RL)-based multi-agent collaborative framework that
models medical consultations as a dynamic decision-making process under
uncertainty. The doctor agent continuously optimizes its questioning strategy
within the RL framework through multi-turn interactions with the patient agent,
dynamically adjusting its information-gathering path based on comprehensive
rewards from the Consultation Evaluator. This RL fine-tuning mechanism enables
LLMs to autonomously develop interaction strategies aligned with clinical
reasoning logic, rather than superficially imitating patterns in existing
dialogue data. Notably, we constructed MTMedDialog, the first English
multi-turn medical consultation dataset capable of simulating patient
interactions. Experiments demonstrate that DoctorAgent-RL outperforms existing
models in both multi-turn reasoning capability and final diagnostic
performance, demonstrating practical value in assisting clinical consultations.
https://github.com/JarvisUSTC/DoctorAgent-RL


## improving-medical-reasoning-with-curriculum-aware-reinforcement-learning
### Abstract
Recent advances in reinforcement learning with verifiable, rule-based rewards
have greatly enhanced the reasoning capabilities and out-of-distribution
generalization of VLMs/LLMs, obviating the need for manually crafted reasoning
chains. Despite these promising developments in the general domain, their
translation to medical imaging remains limited. Current medical reinforcement
fine-tuning (RFT) methods predominantly focus on close-ended VQA, thereby
restricting the model's ability to engage in world knowledge retrieval and
flexible task adaptation. More critically, these methods fall short of
addressing the critical clinical demand for open-ended, reasoning-intensive
decision-making. To bridge this gap, we introduce \textbf{MedCCO}, the first
multimodal reinforcement learning framework tailored for medical VQA that
unifies close-ended and open-ended data within a curriculum-driven RFT
paradigm. Specifically, MedCCO is initially fine-tuned on a diverse set of
close-ended medical VQA tasks to establish domain-grounded reasoning
capabilities, and is then progressively adapted to open-ended tasks to foster
deeper knowledge enhancement and clinical interpretability. We validate MedCCO
across eight challenging medical VQA benchmarks, spanning both close-ended and
open-ended settings. Experimental results show that MedCCO consistently
enhances performance and generalization, achieving a 11.4\% accuracy gain
across three in-domain tasks, and a 5.7\% improvement on five out-of-domain
benchmarks. These findings highlight the promise of curriculum-guided RL in
advancing robust, clinically-relevant reasoning in medical multimodal language
models.


