# Paper List of Terms(reason+R1)
- [25/05] **J1: Incentivizing Thinking in LLM-as-a-Judge via Reinforcement Learning**  
[[Paper](http://arxiv.org/pdf/2505.10320v1)] [[Code/Page]()] [[TLDR/Notes](#j1--incentivizing-thinking-in-llm-as-a-judge-via-reinforcement-learning)]

- [25/05] **RAIDEN-R1: Improving Role-awareness of LLMs via GRPO with Verifiable Reward**  
[[Paper](http://arxiv.org/pdf/2505.10218v1)] [[Code/Page]()] [[TLDR/Notes](#raiden-r1--improving-role-awareness-of-llms-via-grpo-with-verifiable-reward)]

- [25/05] **Pre-Act: Multi-Step Planning and Reasoning Improves Acting in LLM Agents**  
[[Paper](http://arxiv.org/pdf/2505.09970v1)] [[Code/Page]()] [[TLDR/Notes](#pre-act--multi-step-planning-and-reasoning-improves-acting-in-llm-agents)]

- [25/05] **Omni-R1: Do You Really Need Audio to Fine-Tune Your Audio LLM?**  
[[Paper](http://arxiv.org/pdf/2505.09439v1)] [[Code/Page]()] [[TLDR/Notes](#omni-r1--do-you-really-need-audio-to-fine-tune-your-audio-llm-)]

- [25/05] **AM-Thinking-v1: Advancing the Frontier of Reasoning at 32B Scale**  
[[Paper](http://arxiv.org/pdf/2505.08311v1)] [[Code/Page](https://huggingface.co/a-m-team/AM-Thinking-v1}{Hugging)] [[TLDR/Notes](#am-thinking-v1--advancing-the-frontier-of-reasoning-at-32b-scale)]

- [25/05] **Learning from Peers in Reasoning Models**  
[[Paper](http://arxiv.org/pdf/2505.07787v1)] [[Code/Page](https://learning-from-peers.github.io/)] [[TLDR/Notes](#learning-from-peers-in-reasoning-models)]

- [25/05] **S-GRPO: Early Exit via Reinforcement Learning in Reasoning Models**  
[[Paper](http://arxiv.org/pdf/2505.07686v1)] [[Code/Page]()] [[TLDR/Notes](#s-grpo--early-exit-via-reinforcement-learning-in-reasoning-models)]

- [25/05] **Measuring General Intelligence with Generated Games**  
[[Paper](http://arxiv.org/pdf/2505.07215v1)] [[Code/Page]()] [[TLDR/Notes](#measuring-general-intelligence-with-generated-games)]

- [25/05] **Practical Reasoning Interruption Attacks on Reasoning Large Language Models**  
[[Paper](http://arxiv.org/pdf/2505.06643v1)] [[Code/Page]()] [[TLDR/Notes](#practical-reasoning-interruption-attacks-on-reasoning-large-language-models)]

- [25/05] **LLM-Flock: Decentralized Multi-Robot Flocking via Large Language Models and Influence-Based Consensus**  
[[Paper](http://arxiv.org/pdf/2505.06513v1)] [[Code/Page]()] [[TLDR/Notes](#llm-flock--decentralized-multi-robot-flocking-via-large-language-models-and-influence-based-consensus)]



# TLDR/Notes
## j1--incentivizing-thinking-in-llm-as-a-judge-via-reinforcement-learning
### Abstract
The progress of AI is bottlenecked by the quality of evaluation, and powerful
LLM-as-a-Judge models have proved to be a core solution. Improved judgment
ability is enabled by stronger chain-of-thought reasoning, motivating the need
to find the best recipes for training such models to think. In this work we
introduce J1, a reinforcement learning approach to training such models. Our
method converts both verifiable and non-verifiable prompts to judgment tasks
with verifiable rewards that incentivize thinking and mitigate judgment bias.
In particular, our approach outperforms all other existing 8B or 70B models
when trained at those sizes, including models distilled from DeepSeek-R1. J1
also outperforms o1-mini, and even R1 on some benchmarks, despite training a
smaller model. We provide analysis and ablations comparing Pairwise-J1 vs
Pointwise-J1 models, offline vs online training recipes, reward strategies,
seed prompts, and variations in thought length and content. We find that our
models make better judgments by learning to outline evaluation criteria,
comparing against self-generated reference answers, and re-evaluating the
correctness of model responses.


## raiden-r1--improving-role-awareness-of-llms-via-grpo-with-verifiable-reward
### Abstract
Role-playing conversational agents (RPCAs) face persistent challenges in
maintaining role consistency. To address this, we propose RAIDEN-R1, a novel
reinforcement learning framework that integrates Verifiable Role-Awareness
Reward (VRAR). The method introduces both singular and multi-term mining
strategies to generate quantifiable rewards by assessing role-specific keys.
Additionally, we construct a high-quality, role-aware Chain-of-Thought dataset
through multi-LLM collaboration, and implement experiments to enhance reasoning
coherence. Experiments on the RAIDEN benchmark demonstrate RAIDEN-R1's
superiority: our 14B-GRPO model achieves 88.04% and 88.65% accuracy on
Script-Based Knowledge and Conversation Memory metrics, respectively,
outperforming baseline models while maintaining robustness. Case analyses
further reveal the model's enhanced ability to resolve conflicting contextual
cues and sustain first-person narrative consistency. This work bridges the
non-quantifiability gap in RPCA training and provides insights into role-aware
reasoning patterns, advancing the development of RPCAs.


## pre-act--multi-step-planning-and-reasoning-improves-acting-in-llm-agents
### Abstract
The ReAct (Reasoning + Action) capability in large language models (LLMs) has
become the foundation of modern agentic systems. Recent LLMs, such as
DeepSeek-R1 and OpenAI o1/o3, exemplify this by emphasizing reasoning through
the generation of ample intermediate tokens, which help build a strong premise
before producing the final output tokens. In this paper, we introduce Pre-Act,
a novel approach that enhances the agent's performance by creating a multi-step
execution plan along with the detailed reasoning for the given user input. This
plan incrementally incorporates previous steps and tool outputs, refining
itself after each step execution until the final response is obtained. Our
approach is applicable to both conversational and non-conversational agents. To
measure the performance of task-oriented agents comprehensively, we propose a
two-level evaluation framework: (1) turn level and (2) end-to-end. Our
turn-level evaluation, averaged across five models, shows that our approach,
Pre-Act, outperforms ReAct by 70% in Action Recall on the Almita dataset. While
this approach is effective for larger models, smaller models crucial for
practical applications, where latency and cost are key constraints, often
struggle with complex reasoning tasks required for agentic systems. To address
this limitation, we fine-tune relatively small models such as Llama 3.1 (8B &
70B) using the proposed Pre-Act approach. Our experiments show that the
fine-tuned 70B model outperforms GPT-4, achieving a 69.5% improvement in action
accuracy (turn-level) and a 28% improvement in goal completion rate
(end-to-end) on the Almita (out-of-domain) dataset.


## omni-r1--do-you-really-need-audio-to-fine-tune-your-audio-llm-
### Abstract
We propose Omni-R1 which fine-tunes a recent multi-modal LLM, Qwen2.5-Omni,
on an audio question answering dataset with the reinforcement learning method
GRPO. This leads to new State-of-the-Art performance on the recent MMAU
benchmark. Omni-R1 achieves the highest accuracies on the sounds, music,
speech, and overall average categories, both on the Test-mini and Test-full
splits. To understand the performance improvement, we tested models both with
and without audio and found that much of the performance improvement from GRPO
could be attributed to better text-based reasoning. We also made a surprising
discovery that fine-tuning without audio on a text-only dataset was effective
at improving the audio-based performance.


## am-thinking-v1--advancing-the-frontier-of-reasoning-at-32b-scale
### Abstract
We present AM-Thinking-v1, a 32B dense language model that advances the
frontier of reasoning, embodying the collaborative spirit of open-source
innovation. Outperforming DeepSeek-R1 and rivaling leading Mixture-of-Experts
(MoE) models like Qwen3-235B-A22B and Seed1.5-Thinking, AM-Thinking-v1 achieves
impressive scores of 85.3 on AIME 2024, 74.4 on AIME 2025, and 70.3 on
LiveCodeBench, showcasing state-of-the-art mathematical and coding capabilities
among open-source models of similar scale.
  Built entirely from the open-source Qwen2.5-32B base model and publicly
available queries, AM-Thinking-v1 leverages a meticulously crafted
post-training pipeline - combining supervised fine-tuning and reinforcement
learning - to deliver exceptional reasoning capabilities. This work
demonstrates that the open-source community can achieve high performance at the
32B scale, a practical sweet spot for deployment and fine-tuning. By striking a
balance between top-tier performance and real-world usability, we hope
AM-Thinking-v1 inspires further collaborative efforts to harness mid-scale
models, pushing reasoning boundaries while keeping accessibility at the core of
innovation. We have open-sourced our model on
\href{https://huggingface.co/a-m-team/AM-Thinking-v1}{Hugging Face}.


## learning-from-peers-in-reasoning-models
### Abstract
Large Reasoning Models (LRMs) have the ability to self-correct even when they
make mistakes in their reasoning paths. However, our study reveals that when
the reasoning process starts with a short but poor beginning, it becomes
difficult for the model to recover. We refer to this phenomenon as the "Prefix
Dominance Trap". Inspired by psychological findings that peer interaction can
promote self-correction without negatively impacting already accurate
individuals, we propose **Learning from Peers** (LeaP) to address this
phenomenon. Specifically, every tokens, each reasoning path summarizes its
intermediate reasoning and shares it with others through a routing mechanism,
enabling paths to incorporate peer insights during inference. However, we
observe that smaller models sometimes fail to follow summarization and
reflection instructions effectively. To address this, we fine-tune them into
our **LeaP-T** model series. Experiments on AIME 2024, AIME 2025, AIMO 2025,
and GPQA Diamond show that LeaP provides substantial improvements. For
instance, QwQ-32B with LeaP achieves nearly 5 absolute points higher than the
baseline on average, and surpasses DeepSeek-R1-671B on three math benchmarks
with an average gain of 3.3 points. Notably, our fine-tuned LeaP-T-7B matches
the performance of DeepSeek-R1-Distill-Qwen-14B on AIME 2024. In-depth analysis
reveals LeaP's robust error correction by timely peer insights, showing strong
error tolerance and handling varied task difficulty. LeaP marks a milestone by
enabling LRMs to collaborate during reasoning. Our code, datasets, and models
are available at https://learning-from-peers.github.io/ .


## s-grpo--early-exit-via-reinforcement-learning-in-reasoning-models
### Abstract
As Test-Time Scaling emerges as an active research focus in the large
language model community, advanced post-training methods increasingly emphasize
extending chain-of-thought (CoT) generation length, thereby enhancing reasoning
capabilities to approach Deepseek R1-like reasoning models. However, recent
studies reveal that reasoning models (even Qwen3) consistently exhibit
excessive thought redundancy in CoT generation. This overthinking problem stems
from conventional outcome-reward reinforcement learning's systematic neglect in
regulating intermediate reasoning steps. This paper proposes Serial-Group
Decaying-Reward Policy Optimization (namely S-GRPO), a novel reinforcement
learning method that empowers models with the capability to determine the
sufficiency of reasoning steps, subsequently triggering early exit of CoT
generation. Specifically, unlike GRPO, which samples multiple possible
completions (parallel group) in parallel, we select multiple temporal positions
in the generation of one CoT to allow the model to exit thinking and instead
generate answers (serial group), respectively. For the correct answers in a
serial group, we assign rewards that decay according to positions, with lower
rewards towards the later ones, thereby reinforcing the model's behavior to
generate higher-quality answers at earlier phases with earlier exits of
thinking. Empirical evaluations demonstrate compatibility with state-of-the-art
reasoning models, including Qwen3 and Deepseek-distill models, achieving 35.4%
~ 61.1\% sequence length reduction with 0.72% ~ 6.08% accuracy improvements
across GSM8K, AIME 2024, AMC 2023, MATH-500, and GPQA Diamond benchmarks.


## measuring-general-intelligence-with-generated-games
### Abstract
We present gg-bench, a collection of game environments designed to evaluate
general reasoning capabilities in language models. Unlike most static
benchmarks, gg-bench is a data generating process where new evaluation
instances can be generated at will. In particular, gg-bench is synthetically
generated by (1) using a large language model (LLM) to generate natural
language descriptions of novel games, (2) using the LLM to implement each game
in code as a Gym environment, and (3) training reinforcement learning (RL)
agents via self-play on the generated games. We evaluate language models by
their winrate against these RL agents by prompting models with the game
description, current board state, and a list of valid moves, after which models
output the moves they wish to take. gg-bench is challenging: state-of-the-art
LLMs such as GPT-4o and Claude 3.7 Sonnet achieve winrates of 7-9% on gg-bench
using in-context learning, while reasoning models such as o1, o3-mini and
DeepSeek-R1 achieve average winrates of 31-36%. We release the generated games,
data generation process, and evaluation code in order to support future
modeling work and expansion of our benchmark.


## practical-reasoning-interruption-attacks-on-reasoning-large-language-models
### Abstract
Reasoning large language models (RLLMs) have demonstrated outstanding
performance across a variety of tasks, yet they also expose numerous security
vulnerabilities. Most of these vulnerabilities have centered on the generation
of unsafe content. However, recent work has identified a distinct
"thinking-stopped" vulnerability in DeepSeek-R1: under adversarial prompts, the
model's reasoning process ceases at the system level and produces an empty
final answer. Building upon this vulnerability, researchers developed a novel
prompt injection attack, termed reasoning interruption attack, and also offered
an initial analysis of its root cause. Through extensive experiments, we verify
the previous analyses, correct key errors based on three experimental findings,
and present a more rigorous explanation of the fundamental causes driving the
vulnerability. Moreover, existing attacks typically require over 2,000 tokens,
impose significant overhead, reduce practicality, and are easily detected. To
overcome these limitations, we propose the first practical reasoning
interruption attack. It succeeds with just 109 tokens by exploiting our newly
uncovered "reasoning token overflow" (RTO) effect to overwrite the model's
final answer, forcing it to return an invalid response. Experimental results
demonstrate that our proposed attack is highly effective. Furthermore, we
discover that the method for triggering RTO differs between the official
DeepSeek-R1 release and common unofficial deployments. As a broadened
application of RTO, we also construct a novel jailbreak attack that enables the
transfer of unsafe content within the reasoning tokens into final answer,
thereby exposing it to the user. Our work carries significant implications for
enhancing the security of RLLMs.


## llm-flock--decentralized-multi-robot-flocking-via-large-language-models-and-influence-based-consensus
### Abstract
Large Language Models (LLMs) have advanced rapidly in recent years,
demonstrating strong capabilities in problem comprehension and reasoning.
Inspired by these developments, researchers have begun exploring the use of
LLMs as decentralized decision-makers for multi-robot formation control.
However, prior studies reveal that directly applying LLMs to such tasks often
leads to unstable and inconsistent behaviors, where robots may collapse to the
centroid of their positions or diverge entirely due to hallucinated reasoning,
logical inconsistencies, and limited coordination awareness. To overcome these
limitations, we propose a novel framework that integrates LLMs with an
influence-based plan consensus protocol. In this framework, each robot
independently generates a local plan toward the desired formation using its own
LLM. The robots then iteratively refine their plans through a decentralized
consensus protocol that accounts for their influence on neighboring robots.
This process drives the system toward a coherent and stable flocking formation
in a fully decentralized manner. We evaluate our approach through comprehensive
simulations involving both state-of-the-art closed-source LLMs (e.g., o3-mini,
Claude 3.5) and open-source models (e.g., Llama3.1-405b, Qwen-Max,
DeepSeek-R1). The results show notable improvements in stability, convergence,
and adaptability over previous LLM-based methods. We further validate our
framework on a physical team of Crazyflie drones, demonstrating its practical
viability and effectiveness in real-world multi-robot systems.


