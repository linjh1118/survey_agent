# Paper List of Terms(Game)
- [25/06] **The Effect of State Representation on LLM Agent Behavior in Dynamic Routing Games**  
[[Paper](http://arxiv.org/pdf/2506.15624v1)] [[Code/Page]()] [[TLDR/Notes](#the-effect-of-state-representation-on-llm-agent-behavior-in-dynamic-routing-games)]

- [25/06] **Multi-Agent, Multi-Scale Systems with the Koopman Operator**  
[[Paper](http://arxiv.org/pdf/2506.15589v1)] [[Code/Page]()] [[TLDR/Notes](#multi-agent--multi-scale-systems-with-the-koopman-operator)]

- [25/06] **Controller Synthesis for Parametric Timed Games**  
[[Paper](http://arxiv.org/pdf/2506.15532v1)] [[Code/Page]()] [[TLDR/Notes](#controller-synthesis-for-parametric-timed-games)]

- [25/06] **Co-Creative Learning via Metropolis-Hastings Interaction between Humans and AI**  
[[Paper](http://arxiv.org/pdf/2506.15468v1)] [[Code/Page]()] [[TLDR/Notes](#co-creative-learning-via-metropolis-hastings-interaction-between-humans-and-ai)]

- [25/06] **Hunyuan3D 2.1: From Images to High-Fidelity 3D Assets with Production-Ready PBR Material**  
[[Paper](http://arxiv.org/pdf/2506.15442v1)] [[Code/Page]()] [[TLDR/Notes](#hunyuan3d-2-1--from-images-to-high-fidelity-3d-assets-with-production-ready-pbr-material)]



# TLDR/Notes
## the-effect-of-state-representation-on-llm-agent-behavior-in-dynamic-routing-games
### Abstract
Large Language Models (LLMs) have shown promise as decision-makers in dynamic
settings, but their stateless nature necessitates creating a natural language
representation of history. We present a unifying framework for systematically
constructing natural language "state" representations for prompting LLM agents
in repeated multi-agent games. Previous work on games with LLM agents has taken
an ad hoc approach to encoding game history, which not only obscures the impact
of state representation on agents' behavior, but also limits comparability
between studies. Our framework addresses these gaps by characterizing methods
of state representation along three axes: action informativeness (i.e., the
extent to which the state representation captures actions played); reward
informativeness (i.e., the extent to which the state representation describes
rewards obtained); and prompting style (or natural language compression, i.e.,
the extent to which the full text history is summarized).
  We apply this framework to a dynamic selfish routing game, chosen because it
admits a simple equilibrium both in theory and in human subject experiments
\cite{rapoport_choice_2009}. Despite the game's relative simplicity, we find
that there are key dependencies of LLM agent behavior on the natural language
state representation. In particular, we observe that representations which
provide agents with (1) summarized, rather than complete, natural language
representations of past history; (2) information about regrets, rather than raw
payoffs; and (3) limited information about others' actions lead to behavior
that more closely matches game theoretic equilibrium predictions, and with more
stable game play by the agents. By contrast, other representations can exhibit
either large deviations from equilibrium, higher variation in dynamic game play
over time, or both.


## multi-agent--multi-scale-systems-with-the-koopman-operator
### Abstract
The Koopman Operator (KO) takes nonlinear state dynamics and ``lifts'' those
dynamics to an infinite-dimensional functional space of observables in which
those dynamics are linear. Computational applications typically use a
finite-dimensional approximation to the KO. The KO can also be applied to
controlled dynamical systems, and the linearity of the KO then facilitates
analysis and control calculations. In principle, the potential benefits
provided by the KO, and the way that it facilitates the use of game theory via
its linearity, would suggest it as a powerful approach for dealing with
multi-agent control problems. In practice, though, there has not been much work
in this space: most multi-agent KO work has treated those agents as different
components of a single system rather than as distinct decision-making entities.
This paper develops a KO formulation for multi-agent systems that structures
the interactions between decision-making agents and extends this formulation to
systems in which the agents have hierarchical control structures and time scale
separated dynamics. We solve the multi-agent control problem in both cases as
both a centralized optimization and as a general-sum game theory problem. The
comparison of the two sets of optimality conditions defining the control
solutions illustrates how coupling between agents can create differences
between the social optimum and the Nash equilibrium.


## controller-synthesis-for-parametric-timed-games
### Abstract
We present a (semi)-algorithm to compute winning strategies for parametric
timed games. Previous algorithms only synthesized constraints on the clock
parameters for which the game is winning. A new definition of (winning)
strategies is proposed, and ways to compute them. A transformation of these
strategies to (parametric) timed automata allows for building a controller
enforcing them. The feasibility of the method is demonstrated by an
implementation and experiments for the Production Cell case study.


## co-creative-learning-via-metropolis-hastings-interaction-between-humans-and-ai
### Abstract
We propose co-creative learning as a novel paradigm where humans and AI,
i.e., biological and artificial agents, mutually integrate their partial
perceptual information and knowledge to construct shared external
representations, a process we interpret as symbol emergence. Unlike traditional
AI teaching based on unilateral knowledge transfer, this addresses the
challenge of integrating information from inherently different modalities. We
empirically test this framework using a human-AI interaction model based on the
Metropolis-Hastings naming game (MHNG), a decentralized Bayesian inference
mechanism. In an online experiment, 69 participants played a joint attention
naming game (JA-NG) with one of three computer agent types (MH-based,
always-accept, or always-reject) under partial observability. Results show that
human-AI pairs with an MH-based agent significantly improved categorization
accuracy through interaction and achieved stronger convergence toward a shared
sign system. Furthermore, human acceptance behavior aligned closely with the
MH-derived acceptance probability. These findings provide the first empirical
evidence for co-creative learning emerging in human-AI dyads via MHNG-based
interaction. This suggests a promising path toward symbiotic AI systems that
learn with humans, rather than from them, by dynamically aligning perceptual
experiences, opening a new venue for symbiotic AI alignment.


## hunyuan3d-2-1--from-images-to-high-fidelity-3d-assets-with-production-ready-pbr-material
### Abstract
3D AI-generated content (AIGC) is a passionate field that has significantly
accelerated the creation of 3D models in gaming, film, and design. Despite the
development of several groundbreaking models that have revolutionized 3D
generation, the field remains largely accessible only to researchers,
developers, and designers due to the complexities involved in collecting,
processing, and training 3D models. To address these challenges, we introduce
Hunyuan3D 2.1 as a case study in this tutorial. This tutorial offers a
comprehensive, step-by-step guide on processing 3D data, training a 3D
generative model, and evaluating its performance using Hunyuan3D 2.1, an
advanced system for producing high-resolution, textured 3D assets. The system
comprises two core components: the Hunyuan3D-DiT for shape generation and the
Hunyuan3D-Paint for texture synthesis. We will explore the entire workflow,
including data preparation, model architecture, training strategies, evaluation
metrics, and deployment. By the conclusion of this tutorial, you will have the
knowledge to finetune or develop a robust 3D generative model suitable for
applications in gaming, virtual reality, and industrial design.


