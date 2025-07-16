# Paper List of Terms(Rare Disease+RL)
- [23/10] **REMEDI: REinforcement learning-driven adaptive MEtabolism modeling of primary sclerosing cholangitis DIsease progression**  
[[Paper](http://arxiv.org/pdf/2310.01426v1)] [[Code/Page]()] [[TLDR/Notes](#remedi--reinforcement-learning-driven-adaptive-metabolism-modeling-of-primary-sclerosing-cholangitis-disease-progression)]



# TLDR/Notes
## remedi--reinforcement-learning-driven-adaptive-metabolism-modeling-of-primary-sclerosing-cholangitis-disease-progression
### Abstract
Primary sclerosing cholangitis (PSC) is a rare disease wherein altered bile
acid metabolism contributes to sustained liver injury. This paper introduces
REMEDI, a framework that captures bile acid dynamics and the body's adaptive
response during PSC progression that can assist in exploring treatments. REMEDI
merges a differential equation (DE)-based mechanistic model that describes bile
acid metabolism with reinforcement learning (RL) to emulate the body's
adaptations to PSC continuously. An objective of adaptation is to maintain
homeostasis by regulating enzymes involved in bile acid metabolism. These
enzymes correspond to the parameters of the DEs. REMEDI leverages RL to
approximate adaptations in PSC, treating homeostasis as a reward signal and the
adjustment of the DE parameters as the corresponding actions. On real-world
data, REMEDI generated bile acid dynamics and parameter adjustments consistent
with published findings. Also, our results support discussions in the
literature that early administration of drugs that suppress bile acid synthesis
may be effective in PSC treatment.
### 🌟 论文解读 | REMEDI：强化学习驱动的原发性硬化性胆管炎疾病进展自适应代谢建模

### 📌 背景痛点/本文动机
原发性硬化性胆管炎（PSC）是一种罕见且复杂的肝病，胆汁酸代谢改变会导致肝损伤，目前缺乏有效药物，探索治疗方法的关键障碍是缺少能捕捉疾病动态、身体对疾病响应及治疗效果的模型。开发该模型面临三大挑战：一是缺乏PSC期间的胆汁酸代谢模型；二是对身体针对疾病的自适应响应了解有限；三是受影响器官的直接测量数据缺乏且纵向数据不足。因此，本文旨在开发基于机器学习、聚焦胆汁酸代谢动态及其与身体双向交互的PSC进展模型，以助力治疗评估与药物研发。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：构建针对PSC的降阶胆汁酸代谢模型  
基于健康个体的微分方程（DE）胆汁酸代谢模型，开发出能捕捉PSC相关动态的降阶模型，并结合临床领域知识扩展模型以体现胆管阻塞这一PSC病理特征。该降阶模型在保留相关动态的同时大幅降低计算成本。  

💡 创新点2：利用强化学习（RL）模拟身体对疾病的自适应响应  
假设身体是智能体，通过进化学会调节自身以维持关键代谢事件的稳态。在PSC中，身体调节胆汁酸代谢酶来维持稳态，这些酶对应降阶模型中DE的参数。RL智能体在疾病进展中持续更新这些参数，以最大化促进稳态和生成贴近真实胆汁酸谱的奖励函数，将胆汁酸DE构成的环境、“稳态”奖励函数、DE参数调制分别对应强化学习中的环境、奖励、动作，结合DE近似身体对疾病的适应并实现PSC进展的动态建模。  

💡 创新点3：结合现实数据特点处理数据难题  
考虑到PSC患者有长期部分成功的适应期，假设现实世界的横断面数据是在该“稳定”期收集，促使RL智能体生成贴近数据的稳定轨迹，应对数据纵向性不足等问题。  

### 📈 实验结果
在验证方面取得多项成果：降阶胆汁酸模型捕捉到文献中更详细模型的相关动态且计算成本大幅降低；纳入胆管阻塞模拟了临床和动物研究中观察到的PSC病理生理学；在真实PSC数据上，REMEDI生成的胆汁酸动态和参数适应与文献一致；对两种PSC临床试验药物的模拟评估显示，REMEDI有潜力解释药物在生物学上观察到的行为。  

### 💬 可借鉴之处
一是首次基于临床领域知识开发出PSC中胆汁酸代谢的数学模型，为该疾病代谢研究提供新工具；二是提供了一个计算机模拟测试平台来评估胆汁酸调节疗法的效果，结合全面临床数据可确定PSC的最优干预措施；三是REMEDI用RL估计时变DE参数的方法原则上可扩展到其他有基于时变参数DE模型的疾病（如HIV），其利用RL模拟自适应行为的策略为多种稳态生物系统建模带来希望，为跨疾病领域的建模方法提供了创新思路与借鉴方向。

