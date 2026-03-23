# 📊 Nature Communications 研究报告 (2026-03-16)

> 生成时间: 2026-03-16 18:32:54
> 数据源: Nature Communications

> ⚠️ **注意**: 该数据源不支持PDF下载，仅提供评分和摘要翻译，无深度分析

## 📌 配置信息

### 关键词列表（共 8 个，总权重 8.0）

| 关键词 | 权重 | 类型 |
|--------|------|------|
| medical image analysis | 1.0 | 主要 |
| medical image segmentation | 1.0 | 主要 |
| deep learning medical imaging | 1.0 | 主要 |
| AI for diagnosis | 1.0 | 主要 |
| prognosis prediction | 1.0 | 主要 |
| surgical planning | 1.0 | 主要 |
| multimodal medical imaging | 1.0 | 主要 |
| foundation models medical imaging | 1.0 | 主要 |

### 评分设置

- **每个关键词最大分**: 10
- **及格分公式**: 5.0 + 3.0 × 总权重
- **当前及格分**: 29.0

## 📈 论文统计

- **总抓取**: 48 篇
- **及格论文**: 0 篇 (0.0%)

---

## 📋 所有论文列表

### 1. ❌ An international multi-centre study to develop and validate federated learning-based prognostic models for anal cancer

**作者**: Stelios Theophanous, Per-Ivar Lønne, Ananya Choudhury, Maaike Berbée, Charlotte L. Deijen, Andre Dekker, Matthew Field, Maria Antonietta Gambacorta, Alexandra Gilbert, Marianne Grønlie Guren, Rashmi Jadon, Rohit Kochhar, Dieter Martin, Ahmed Allam Mohamed, R. Muirhead, Oriol Parés, Łukasz Raszewski, Rajarshi Roy, Andrew Scarsbrook, D. Sebag-Montefiore
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70297-3](https://doi.org/10.1038/s41467-026-70297-3)

**评分**: 20.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 5.0/10 | 5.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 5.0/10 | 5.0 |
| prognosis prediction | 1.0 | 10.0/10 | 10.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文专注于使用联邦学习开发肛门癌预后模型，与'prognosis prediction'高度相关（10分），与'AI for diagnosis'有一定关联（5分），因为AI用于预后预测可视为诊断支持的一部分。与'medical image analysis'有间接关联（5分），因为肿瘤体积等特征可能来自医学影像，但论文未明确讨论影像分析技术。其他关键词（segmentation, deep learning imaging, surgical planning, multimodal imaging, foundation models）在标题和摘要中均未提及，评分为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Federated multivariable Cox models trained across 14 centres and externally validated in two additional centres achieve consistent calibration and discrimination during leave-one-centre-out and external validation, demonstrating that federated learning enables robust, privacy-preserving prognostic modelling for rare cancers using real-world data, supporting international collaboration without data sharing.

!!! tip deepseek-chat TL;DR

    该研究通过国际多中心合作，利用联邦学习开发并验证了肛门癌的预后模型，发现肿瘤分期、体积、性别等因素与生存率相关，证明了联邦学习在罕见癌症预后建模中的可行性和隐私保护优势。

<details open>
<summary>摘要翻译</summary>

> 摘要：精准肿瘤学的发展依赖于获取高质量数据以服务于日益细分的患者亚群。国际atomCAT联盟以肛门癌这一罕见癌症为例，探讨了联邦学习在支持该领域的潜力。本研究显示，基于14个中心（1428例患者）数据训练的联邦多变量Cox模型，并在另外两个中心（277例患者）进行外部验证，在留一中心交叉验证和外部验证中均表现出稳定的校准度和区分度（一致性指数c-indices为0.68-0.79）。较低的T分期、无淋巴结转移、较小的肿瘤体积、女性、较年轻年龄以及基于丝裂霉素或顺铂的化疗与改善的总生存期相关。较低的T分期、较小的肿瘤体积和女性性别与改善的局部区域控制相关，而无淋巴结转移和较小肿瘤体积则与更好的无远处转移生存相关。这些发现表明，联邦学习能够利用真实世界数据为罕见癌症构建稳健且保护隐私的预后模型，在无需共享数据的前提下支持国际合作。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Precision oncology relies on access to high-quality data for increasingly smaller patient subgroups. The international atomCAT consortium investigates the potential of federated learning to support this, using anal cancer as a rare cancer exemplar. Here, we show that federated multivariable Cox models trained across 14 centres (1428 patients) and externally validated in two additional centres (277 patients) achieve consistent calibration and discrimination during leave-one-centre-out and external validation (c-indices 0.68-0.79). Lower T stage, absence of nodal involvement, smaller tumour volume, female sex, younger age, and mitomycin- or cisplatin-based chemotherapy are associated with improved overall survival. Lower T stage, smaller tumour volume, and female sex are associated with improved locoregional control, while absence of nodal involvement and smaller tumour volume are associated with better freedom from distant metastases. These findings demonstrate that federated learning enables robust, privacy-preserving prognostic modelling for rare cancers using real-world data, supporting international collaboration without data sharing.

</details>
<br>

**关键词**: federated learning, prognostic models, anal cancer, multivariable Cox models, overall survival, locoregional control, rare cancers, privacy-preserving

---

### 2. ❌ Dopaminergic processes predict temporal distortions in event memory

**作者**: Erin Morrow, Ringo Huang, David Clewett
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-69950-8](https://doi.org/10.1038/s41467-026-69950-8)

**评分**: 5.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 2.0/10 | 2.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 3.0/10 | 3.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文研究记忆的时间扭曲与多巴胺系统活动的关系，使用fMRI和眼动追踪技术。与医学影像分析领域仅有微弱关联（关键词1得2分），因为使用了fMRI这一医学影像技术，但研究焦点是认知神经科学而非临床决策支持。关键词7得3分，因为论文结合了fMRI（医学影像）和眼动追踪（行为数据），属于多模态数据融合，但并非针对医学影像本身的多模态融合。其他关键词（2-6,8）得0分，因为论文不涉及医学影像分割、深度学习、疾病诊断/预后、手术规划或基础模型，这些是临床AI应用的核心内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过fMRI和眼动追踪发现，多巴胺系统活动对事件边界的敏感性预测了记忆中时间扭曲的程度，有助于将连续经验分割为不同的情景记忆。

<details open>
<summary>摘要翻译</summary>

> 摘要  我们的记忆并非简单地记录时间——它们会扭曲时间，拉伸或压缩过去以反映经验的结构。本研究结合功能磁共振成像（fMRI；n = 32）与眼动追踪技术（n = 28），旨在检验已知影响编码与时间知觉的多巴胺系统激活是否会扩展情境性事件之间的时间记忆表征。参与者在编码物品序列时聆听随时间重复但偶尔变化的音调，这些变化形成了显著的事件边界。研究发现，音调切换显著激活了腹侧被盖区（ventral tegmental area, VTA），且该反应的强度能够预测跨越切换点的物品对在记忆中的时间拉伸程度。在更长的时间尺度上，眨眼频率的增加同样预示着记忆中对时间的更大拉伸，但仅针对跨越事件边界的物品对。这些结果表明，多巴胺过程对事件结构敏感，并参与了记忆时间的扭曲机制，这可能有助于将连续经验分割为不同的情景记忆。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Our memories do not simply keep time — they distort it, stretching and compressing the past to reflect the structure of experience. Here, we combined functional magnetic resonance imaging (fMRI; n = 32) with eye-tracking ( n = 28) to test whether activation of the dopaminergic system, known to influence encoding and time perception, expands mnemonic representations of time between contextually distinct events. Participants encoded item sequences while listening to tones that typically repeated over time, but occasionally changed, creating salient event boundaries. We found that tone switches significantly activated the ventral tegmental area (VTA), and the magnitude of these responses predicted greater time dilation between item pairs spanning those switches. At a longer timescale, increased blinking also predicted greater time dilation in memory, but only for boundary-spanning item pairs. Together, these findings suggest that dopaminergic processes are sensitive to event structure and contribute to distortions of remembered time that may help segment continuous experience into distinct episodic memories.

</details>
<br>

**关键词**: dopaminergic processes, temporal distortions, event memory, fMRI, eye-tracking, ventral tegmental area, time dilation, event boundaries

---

### 3. ❌ Learning data-efficient coarse-grained molecular dynamics from forces and noise

**作者**: Aleksander E. P. Durumeric, Yaoyi Chen, Aldo S. Pasos-Trejo, Frank Noé, Cecilia Clementi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70818-0](https://doi.org/10.1038/s41467-026-70818-0)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究分子动力学模拟的机器学习方法，专注于分子建模、粗粒化模型和生成扩散模型，完全不涉及医学图像分析、临床诊断、手术规划或任何医疗应用。所有关键词均与医学影像无关，因此相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种结合生成扩散模型和力匹配的机器学习方法，显著降低了构建准确粗粒化分子动力学模型所需的数据量，从而扩展了其在大型生物分子系统中的应用。

<details open>
<summary>摘要翻译</summary>

> 摘要：分子动力学模拟对于阐明生物分子功能至关重要，但全原子模型的计算成本常常限制其应用范围。机器学习粗粒化模型通过简化分子表示同时保持近原子级精度，为此提供了解决方案。然而，当前MLCG模型的训练需要从参考原子分子动力学模拟中获取大量带力场标签的样本构象。本研究通过将MLCG模型的训练与生成式扩散模型原理相结合，突破了这一限制。我们证明，通过将传统力匹配方法与去噪目标函数相整合，能够重建分子系综的高维精确分布。该框架在构建物理一致且稳定的力场的同时，将原子级数据需求降低了多达两个数量级。通过对多种蛋白质折叠类型和尺度体系的验证，我们的研究在分子动力学模拟与现代生成式学习之间建立了桥梁，显著降低了构建精确MLCG模型的计算成本，并拓展了其在大规模生物分子体系中的适用性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Molecular dynamics (MD) simulations are essential for elucidating biomolecular function, yet the computational cost of all-atom models often limits their reach. Machine-learned coarse-grained (MLCG) models offer a solution by simplifying the representation while maintaining near-atomistic accuracy. However, the training of MLCG models currently requires vast amounts of force-labeled sample conformations from reference atomistic MD. Here, we overcome this limitation by unifying the training of MLCG models with the principles of generative diffusion models. We demonstrate that accurate high-dimensional distributions of molecular ensembles can be recovered by integrating traditional force-matching with denoising objectives. This framework enables the construction of physically consistent and stable force fields while reducing atomistic data requirements by up to two orders of magnitude. Validated across diverse protein folds and scales, our work establishes a bridge between molecular dynamics simulation and modern generative learning, substantially lowering the computational cost of constructing accurate MLCG models and broadening their applicability to large biomolecular systems.

</details>
<br>

**关键词**: molecular dynamics, coarse-grained models, machine learning, diffusion models, force matching, biomolecular simulation, data-efficient training, generative learning

---

### 4. ❌ Modifying muscle metabolic dysregulation in inclusion body myositis with pioglitazone: a single-arm trial

**作者**: Brittany L. Adler, Michael R. Bene, Cissy Zhang, Conrad Say, Pratik Khare, Christopher Mecoli, Eleni Tiniakou, Julie J. Paik, Tae Chung, Erika Darrah, Thomas Lloyd, Ruben Pagkatipunan, Megan McGowan, Albert Mears, Hilary J. Vernon, Lisa Christopher-Stine, Anne Le, Jemima Albayda
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70262-0](https://doi.org/10.1038/s41467-026-70262-0)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文是一项关于皮格列酮治疗包涵体肌炎的临床试验，研究内容聚焦于药物干预对肌肉代谢通路的影响和临床功能评估，完全不涉及医学影像分析、深度学习、AI诊断、手术规划或多模态影像融合等主题。所有评分关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Preliminary evidence that pioglitazone modulates muscle metabolism and warrants further investigation in IBM is provided, as a phase 1 trial with a limited cohort.

!!! tip deepseek-chat TL;DR

    这项单臂1期临床试验评估了皮格列酮对包涵体肌炎患者肌肉代谢的影响，发现药物能调节代谢通路并可能减缓部分患者的临床功能下降。

<details open>
<summary>摘要翻译</summary>

> 摘要 这项单臂、开放标签的1期试验评估了PPARγ激动剂吡格列酮在包涵体肌炎（IBM）患者中的应用。经过16周的观察（导入）期后，受试者每日接受45毫克吡格列酮治疗，为期32周。主要结局指标是治疗16周后与导入期相比，肌肉中PPARGC1A表达及相关代谢通路的变化。在入组的16名参与者中，13人开始服用吡格列酮并完成了至少一次治疗中评估；该试验因COVID-19大流行而提前终止。基线时，与对照组相比，肌肉代谢组学显示出广泛的代谢异常。吡格列酮逆转了部分异常特征，增加了PPARGC1A表达（p = 0.099）并调节了肌肉中的下游通路，包括增强氧化磷酸化。临床结局总体未见变化，但一部分代谢反应良好的亚组在IBM功能评定量表（IBM-FRS）和改良计时起立行走测试（m-TUG）中显示出较慢的衰退速度。报告的不良反应包括肌痛和心力衰竭加重。作为一项受试者队列有限的1期试验，这些发现提供了初步证据，表明吡格列酮可调节肌肉代谢，值得在IBM中进行进一步研究。本研究由Ira T. Discovery基金以及Peter and Carmen Lucia Buck基金会肌炎探索基金资助。临床试验注册号：NCT03440034。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract This single-arm, open-label phase 1 trial evaluated the PPARγ agonist pioglitazone in patients with inclusion body myositis (IBM). After a 16-week observation (lead-in) period, participants received pioglitazone 45 mg daily for 32 weeks. The primary outcome was the change in PPARGC1A expression and related metabolic pathways in muscle after 16 weeks of treatment compared with the lead-in period. Of the 16 enrolled participants, 13 initiated pioglitazone and completed at least one on-treatment assessment; the trial was terminated early due to the COVID-19 pandemic. At baseline, muscle metabolomics revealed broad metabolic abnormalities compared with controls. Pioglitazone reversed elements of this signature, increasing PPARGC1A expression ( p = 0.099) and modulating downstream pathways in muscle, including enhanced oxidative phosphorylation. Clinical outcomes were unchanged overall, but a subset with favorable metabolic responses showed slower decline in the IBM-Functional Rating Score (IBM-FRS) and Modified Timed Up and Go (m-TUG). Reported adverse effects included myalgia and heart failure exacerbation. As a phase 1 trial with a limited cohort, these findings provide preliminary evidence that pioglitazone modulates muscle metabolism and warrants further investigation in IBM. This study was supported by the Ira T. Discovery Fund and the Peter and Carmen Lucia Buck Foundation Myositis Discovery Fund. Clinical Trials Registration: NCT03440034.

</details>
<br>

**关键词**: inclusion body myositis, pioglitazone, clinical trial, muscle metabolism, PPARGC1A, IBM-FRS, metabolomics, phase 1 trial

---

### 5. ❌ Extensive enhancer crosstalk controls PPARG2 activation during adipogenesis

**作者**: Anna Cetnarowska, Mette Hyldahl, Marcus Nygård, Hesam Dashti, Bo Mølholm Hansen, Laura Kristine Holm, Kaja Madsen, Maria S. Madsen, Vallari Shukla, Esra Durmaz Mitchell, Alexander Rauch, Jesper Grud Skat Madsen, Melina Claussnitzer, Susanne Mandrup
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70401-7](https://doi.org/10.1038/s41467-026-70401-7)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究是关于脂肪生成过程中PPARG2基因激活的增强子调控机制，属于分子生物学、基因组学和表观遗传学领域，与医学影像分析、深度学习、AI诊断、手术规划等关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The regulatory mechanisms of the highly connected enhancer community driving activation of the PPARG locus during adipocyte differentiation of human mesenchymal stem cells are deciphered and it is shown that the super-enhancer constituent E + 102 plays a dual role in cis crosstalk and feedback activation and is obligate for activation of PPARG expression.

!!! tip deepseek-chat TL;DR

    该研究揭示了脂肪生成过程中多个增强子通过协同作用调控PPARG2基因激活的分子机制。

**关键词**: PPARG2, adipogenesis, enhancer crosstalk, gene regulation, transcription, epigenetics, fat cell differentiation

---

### 6. ❌ Revealing multiscale competing processes in the solid-state synthesis of single-crystalline layered oxide positive electrodes

**作者**: Zhichen Xue, Tianxiao Sun, Sreevishnu Oruganti, Xiaojing Huang, Dilworth Y. Parkinson, Yong S. Chu, P. Pianetta, Mingyuan Ge, Yijin Liu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70607-9](https://doi.org/10.1038/s41467-026-70607-9)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究固态合成单晶层状氧化物正极材料的多尺度竞争过程，属于材料科学和电化学领域，与医学影像分析、人工智能临床决策支持等关键词完全无关。论文使用同步辐射X射线成像等技术研究材料合成机制，不涉及任何医学影像、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究揭示了固态合成单晶层状氧化物正极材料过程中的多尺度竞争机制，通过同步辐射X射线成像等技术阐明了晶体生长、相变和缺陷形成的动态过程。

**关键词**: solid-state synthesis, single-crystalline layered oxide, positive electrodes, multiscale competing processes, synchrotron X-ray imaging, crystal growth, phase transformation, defect formation

---

### 7. ❌ Generic logic block based on bias-gated 2D MoS2 transistors

**作者**: Xiaofu Wei, Zhangyi Chen, Kuanglei Chen, Jinsen Shang, Li Gao, He Jiang, Huihui Yu, Mengyu Hong, Xiankun Zhang, Zheng Zhang, Yue Zhang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70712-9](https://doi.org/10.1038/s41467-026-70712-9)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究专注于基于二维MoS2晶体管的通用逻辑块设计，属于纳米电子学、半导体器件和集成电路领域，与医学图像分析、人工智能临床决策支持等医疗领域完全无关。所有关键词均涉及医疗应用，而论文研究的是基础电子器件，因此所有相关度评分为0。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了基于偏置门控二维MoS2晶体管的通用逻辑块设计，实现了可重构的逻辑功能，为未来低功耗电子器件提供了新方案。

**关键词**: 2D MoS2 transistors, bias-gated transistors, generic logic block, reconfigurable logic, low-power electronics, semiconductor devices, nanoscale electronics, logic circuits

---

### 8. ❌ Sustained hydrogen peroxide production via MXene-functionalized supramolecular docking

**作者**: Jiaxun Sun, Yuanming Zhang, Wanheng Lu, Wei Li Ong, Xinglong Pan, Wentao Song, Zhonghua Li, Zhaosheng Li, Ghim Wei Ho
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70693-9](https://doi.org/10.1038/s41467-026-70693-9)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究聚焦于材料科学和化学工程领域，具体研究MXene功能化超分子对接用于持续过氧化氢生产，涉及电催化、光催化、材料合成和能源转换，与医学影像分析、人工智能临床决策支持、疾病诊断预测、手术规划等医疗AI主题完全无关。所有关键词均未在论文内容中出现或相关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种MXene功能化超分子对接策略，实现了高效、持续的过氧化氢电催化生产，在宽pH范围和实际水样中表现出优异性能。

**关键词**: MXene, supramolecular docking, hydrogen peroxide production, electrocatalysis, photocatalysis, sustainable synthesis, wide pH range, practical water samples

---

### 9. ❌ Both genome instability and replicative senescence stem from the shortest telomere in telomerase-negative cells

**作者**: Prisca Berardi, Veronica Martinez-Fernandez, Anaïs Rat, Fernando R. Rosas Bringas, Pascale Jolivet, Rachel Langston, Stefano Mattarocci, Alexandre Maes, Théo Aspert, Bechara Zeinoun, Karine Casier, Hinke G. Kazemier, Gilles Charvin, Marie Doumic, Michael Chang, Maria Teresa Teixeira
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70352-z](https://doi.org/10.1038/s41467-026-70352-z)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是酵母细胞中端粒缩短与复制性衰老、基因组不稳定性的分子机制，属于基础生物学和遗传学领域。所有评分关键词均涉及医学影像分析、人工智能临床决策支持等应用医学领域，与论文的分子生物学研究内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究揭示了在端粒酶缺失的酵母细胞中，单个最短端粒达到临界长度后会触发复制性衰老，并通过非相互易位导致基因组不稳定性，从而连接了衰老起始与基因组不稳定之间的机制。

<details open>
<summary>摘要翻译</summary>

> 摘要 在端粒酶缺失的情况下，端粒缩短会触发复制性衰老——这是一种肿瘤抑制机制，同时也与致癌性基因组不稳定性相关。然而，连接这两种看似对立力量的确切机制仍不甚明了。为直接研究衰老、端粒动态与基因组不稳定性之间复杂的相互作用，我们在酿酒酵母中开发了一套系统，用于在端粒酶缺失条件下生成并追踪具有精确长度的端粒。通过单端粒与单细胞分析结合数学模型，我们确定了端粒功能失调的阈值长度。在大多数细胞中，单个最短端粒低于该阈值是触发复制性衰老起始的必要且充分条件。在群体水平上，波动实验证实罕见的基因组不稳定性主要发生在最短端粒的顺式作用区域，表现为依赖Pol32的非相互易位，这种易位导致最短端粒重新延长，并可能实现衰老的短暂逃逸。因此，在端粒酶阴性细胞中，最短端粒向功能失调状态的转换及其后续处理，构成了复制性衰老起始、基因组不稳定性与衰老后生存启动之间的机制性联系。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract In the absence of telomerase, telomere shortening triggers replicative senescence, a tumor suppressor mechanism that is also associated with oncogenic genomic instability. Yet, the precise mechanism that connects these seemingly opposing forces remains poorly understood. To directly study the complex interplay between senescence, telomere dynamics, and genomic instability, we develop a system in Saccharomyces cerevisiae to generate and track telomeres of precise length in the absence of telomerase. Using single-telomere and single-cell analyses combined with mathematical modeling, we identify a threshold length at which telomeres switch into dysfunction. A single shortest telomere below the threshold length is necessary and sufficient to trigger the onset of replicative senescence in a majority of cells. At population level, fluctuation assays establish that rare genomic instability arises predominantly in cis to the shortest telomere as Pol32-dependent non-reciprocal translocations that result in re-elongation of the shortest telomere and likely transient escape from senescence. The switch of the shortest telomere into dysfunction and subsequent processing in telomerase-negative cells thus serves as the mechanistic link between replicative senescence onset, genomic instability and the initiation of post-senescence survival.

</details>
<br>

**关键词**: telomere shortening, replicative senescence, genomic instability, telomerase-negative cells, Saccharomyces cerevisiae, single-telomere analysis, non-reciprocal translocations, post-senescence survival

---

### 10. ❌ A topographical organization in the primary olfactory cortex

**作者**: Shira Taragin, Or Bashan, Tal Dalal, Katya Belelovsky, Rafi Haddad
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70356-9](https://doi.org/10.1038/s41467-026-70356-9)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是初级嗅觉皮层的拓扑组织，属于基础神经科学领域，涉及神经解剖学、电生理学和神经回路功能。所有评分关键词均聚焦于医学影像分析、人工智能临床决策支持、疾病诊断/预后、手术规划等应用导向的医疗技术，与论文的基础神经科学研究内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Results indicate that the primary olfactory cortex adheres to an organizational principle based on how it processes glomerular inputs, and this similarity principle aligned with an increase in odor-tuning similarity of nearby neurons in both awake and anesthetized mice.

!!! tip deepseek-chat TL;DR

    该研究揭示了初级嗅觉皮层中气味信息处理的拓扑组织模式，通过实验证明了不同气味在皮层中的空间表征具有系统性结构。

**关键词**: primary olfactory cortex, topographical organization, odor representation, neural coding, sensory processing, olfactory system, spatial mapping

---

### 11. ❌ Topologically reconstructing Pancharatnam-Berry phase via encircling exceptional point for chiral spin-orbit interaction steering

**作者**: Qinghong Lyu, Qiuchen Yan, Wenjuan Zhao, Saisai Chu, Xiaoyong Hu, Qihuang Gong
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70782-9](https://doi.org/10.1038/s41467-026-70782-9)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究属于物理学和光学领域，涉及Pancharatnam-Berry相位、奇异点环绕和手性自旋轨道相互作用调控，与医学图像分析、临床决策支持等医疗AI主题完全无关。所有关键词均未在内容中体现，因此相关度评分均为0。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过环绕奇异点拓扑重构Pancharatnam-Berry相位，实现了手性自旋轨道相互作用的调控。

**关键词**: Pancharatnam-Berry phase, exceptional point, chiral spin-orbit interaction, topological reconstruction, optical steering, singularity, non-Hermitian physics, phase manipulation

---

### 12. ❌ Global coincident bursts of high frequency oscillations across the human cortex coordinate large-scale memory processing

**作者**: Sathwik Prathapagiri, Jan Cimbálník, Jesús S. García-Salinas, Marina Galanina, Lenka Jurkovicova, Pavel Daniel, Martin Kojan, Róbert Román, Martin Pail, Wojciech Fortuna, Monika Sluzewska-Niedzwiedz, Pawel Tabakow, Andrzej Czyzewski, Milan Brazdil, Michal T. Kucewicz
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70633-7](https://doi.org/10.1038/s41467-026-70633-7)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究人类大脑皮层高频振荡与记忆处理的关系，使用颅内记录分析癫痫患者数据，属于神经科学/认知神经科学领域。所有评分关键词均针对医学影像分析、AI临床决策支持（CT/MRI/超声影像分割、疾病诊断/预后、手术规划、多模态融合等），而本文完全不涉及医学影像处理、AI模型开发或临床应用，因此所有关键词相关度为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A general role of global coincident high frequency oscillations in organizing large-scale information processing across the brain necessary especially, but not exclusively, for memory functions is suggested.

!!! tip deepseek-chat TL;DR

    该研究通过分析癫痫患者的颅内记录，发现大脑皮层全局同步的高频振荡爆发在记忆编码和回忆阶段协调大规模信息处理，尤其对记忆功能至关重要。

<details open>
<summary>摘要翻译</summary>

> 摘要：已知高频伽马波与波纹频率范围内的振荡在记忆编码与提取过程中协调海马及新皮质局部神经元集群。本研究旨在探究记忆处理不同阶段中，这些快速振荡放电在感觉皮层与联合皮层区域的时空动态特征及其全局协调作用。我们通过癫痫患者在进行单词列表即时自由回忆任务时的颅内记录，检测到单个高频振荡爆发事件。研究发现，视觉处理区与高阶处理区之间存在持续同步爆发活动，其在回忆前达到峰值，并在单词编码期间增强。这种全局协同爆发受记忆处理调节，涉及约半数记录电极触点位点，并聚类为多个连续爆发事件序列。我们的结果表明，全局同步高频振荡在大脑大规模信息组织过程中具有普遍作用，这种作用对记忆功能尤为重要，但不仅限于此。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Oscillations in the high gamma and ripple frequency ranges are known to coordinate local hippocampal and neocortical neuronal assemblies during memory encoding and recall. Here, we explored spatiotemporal dynamics and the role of global coordination of these fast oscillatory discharges across the sensory and associational cortical areas in distinct phases of memory processing. Individual bursts of high frequency oscillations were detected in intracranial recordings from epilepsy patients remembering word lists for immediate free recall. We found constant coincident bursting across visual and higher order processing areas, peaking before recall and elevated during encoding of words. This global co-bursting was modulated by memory processing, engaged approximately half of the recorded electrode contact sites, and clustered into a sequence of multiple consecutive bursting events. Our results suggest a general role of global coincident high frequency oscillations in organizing large-scale information processing across the brain necessary especially, but not exclusively, for memory functions.

</details>
<br>

**关键词**: high frequency oscillations, memory processing, intracranial recordings, epilepsy patients, global coordination, cortical areas, coincident bursting, large-scale information processing

---

### 13. ❌ Multisite atomic-chlorine-passivation stabilizes perovskite interfaces for efficient H2O2 photosynthesis from seawater

**作者**: Genping Meng, Shuai Wei, Ning Li, Yuhui Yin, Bin Dong, Shihao Sun, Guowen Hu, Hao Wang, Baodui Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-15
**DOI**: [10.1038/s41467-026-70503-2](https://doi.org/10.1038/s41467-026-70503-2)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要表明该研究属于材料科学和化学工程领域，专注于钙钛矿材料界面稳定化及其在海水光催化产过氧化氢中的应用。所有评分关键词均涉及医学影像分析、人工智能医疗应用、疾病诊断预测等医学领域，而该论文完全不涉及任何医学、影像学或临床相关内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过多部位氯原子钝化策略稳定钙钛矿界面，实现了高效的海水光催化产过氧化氢。

**关键词**: perovskite interfaces, atomic-chlorine-passivation, H2O2 photosynthesis, seawater, multisite stabilization, photocatalysis, perovskite materials

---

### 14. ❌ Dopamine and serotonin inversely modulate D2 medium spiny neurons to regulate cocaine reward

**作者**: Daniel F. Cardozo Pinto, Michaela Y. Guo, Matthew B. Pomrenze, Wade Morishita, Mona X. Li, Larry Zweifel, Neir Eshel, Robert C. Malenka
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70519-8](https://doi.org/10.1038/s41467-026-70519-8)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是神经科学领域，具体探讨多巴胺和血清素对D2中型多棘神经元在可卡因奖赏调节中的相反作用机制，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或基础模型等主题。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that DA and 5HT inversely modulate D2-MSN activity to regulate cocaine reward, identifying a key circuit mechanism underlying the opponent behavioral effects of these important neuromodulators.

!!! tip deepseek-chat TL;DR

    该研究揭示了多巴胺和血清素通过相反地调节D2中型多棘神经元的活动，共同调控可卡因诱导的奖赏行为。

**关键词**: dopamine, serotonin, D2 medium spiny neurons, cocaine reward, neural modulation, reward behavior, nucleus accumbens

---

### 15. ❌ Jagged-mediated lateral induction patterns Notch3 signaling within adult neural stem cell populations

**作者**: Sara Ortica, Miguel Martínez Herrera, Louis Degroux, Bastian Rochette, Nicolas Dray, Laure Bally-Cuif
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70478-0](https://doi.org/10.1038/s41467-026-70478-0)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文研究的是斑马鱼成年端脑中Notch3信号通路如何调控神经干细胞静息态和干性，属于基础神经生物学和发育生物学领域。论文使用分子生物学、遗传学和成像技术（如原位测量核转位），但完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或医学影像基础模型等主题。所有关键词均与医学影像和临床AI应用相关，而该论文专注于基础细胞信号机制研究，因此所有关键词相关度均为0。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究揭示了在斑马鱼成年端脑中，Notch3信号通过整合Dla介导的侧向抑制和Jag1b介导的侧向诱导来控制神经干细胞的静息态、干性及其时空动态。

<details open>
<summary>摘要翻译</summary>

> 摘要 在成体大脑中，Notch3信号通路促进神经干细胞（NSC）的静息态与干性维持。目前尚不清楚Notch3信号水平如何被调控，以及其如何与神经干细胞的这些命运决定相关联。本研究直接测量了Notch3胞内片段（N3ICD）的核转位，并对斑马鱼成体端脑神经干细胞中的Notch3信号进行了原位定量分析。我们发现，Notch3信号水平与神经干细胞的静息程度和干性水平相匹配。在物理空间上，Notch3信号呈模式化分布，高信号水平环绕着N3ICD低表达的细胞，而这些低表达细胞同时表达deltaA（dla）配体。另一种在所有神经干细胞中均表达的配体jagged1b（jag1b），能够激活Notch3信号并维持干性因子Sox2的表达。最后，降低jag1b水平虽能维持Notch3信号水平在空间上的结构化分布，但会减弱其差异性。我们提出，Notch3信号整合了Dla介导的侧向抑制与Jag1b介导的侧向诱导，共同调控成体神经干细胞的静息态、干性及其时空动态。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract In the adult brain, Notch3 signaling promotes neural stem cell (NSC) quiescence and stemness. It remains unknown how Notch3 signaling levels are controlled and relate to these NSC decisions. Here we directly measure the nuclear translocation of the Notch3 intracellular fragment (N3ICD) and quantify Notch3 signaling in NSCs of the zebrafish adult telencephalon in situ. We report that Notch3 signaling levels match NSC quiescence and stemness levels. In physical space, Notch3 signaling is patterned and high signaling levels surround N3ICD low cells, which also express the deltaA (dla ) ligand. Another ligand, jagged1b ( jag1b ), expressed in all NSCs, activates Notch3 signaling and sustains expression of the stemness factor Sox2. Finally, lowering jag1b preserves the structured distribution of Notch3 signaling levels in space but attenuates their variance. We propose that Notch3 signaling integrates Dla-mediated lateral inhibition and Jag1b-mediated lateral induction to control quiescence and stemness and their spatiotemporal dynamics in adult NSCs.

</details>
<br>

**关键词**: Notch3 signaling, neural stem cells, quiescence, stemness, zebrafish adult telencephalon, lateral inhibition, lateral induction, Sox2

---

### 16. ❌ Control of lysosome function by the GTPase-activating protein TBC1D9B and its binding partner TMEM55B

**作者**: Valentin Duhay, Miaomiao Tian, Klaudia Kosieradzka, Michael Ebner, Wen‐Ting Lo, Michael I. Krauss, Henner-Linus Sprengel, Matthias Voss, Mara Riechmann, Jeffrey N. Savas, Michael Schwake, Volker Haucke, Markus Damme
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70345-y](https://doi.org/10.1038/s41467-026-70345-y)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文研究的是细胞生物学中溶酶体功能的分子调控机制，具体涉及TBC1D9B和TMEM55B蛋白对ARL8B GTPase活性的调控及其对溶酶体分布、自噬和细胞营养响应的影响。所有评分关键词均属于医学影像分析与人工智能临床决策支持领域，而论文完全不涉及医学影像、深度学习、AI诊断、手术规划或多模态数据融合等内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The GTPase-activating Tre-2/Bub2/Cdc16 (TBC) domain protein TBC1D9B is identified as a critical negative regulator of ARL8B function and unravels a key role for TBC1D9B in controlling lysosome function by serving as a negative regulator of ARL8 activity.

!!! tip deepseek-chat TL;DR

    该研究发现TBC1D9B通过与TMEM55B结合并激活ARL8B的GTPase活性，作为ARL8的关键负调控因子来控制溶酶体功能，其缺失会导致溶酶体分散、自噬缺陷和细胞营养响应受损。

<details open>
<summary>摘要翻译</summary>

> 摘要 溶酶体是高度动态的细胞器，具有双重拮抗功能：既作为大分子降解的终端分解代谢站，又作为合成代谢生长信号传导的核心代谢决策中心。溶酶体功能障碍与多种人类疾病相关。溶酶体的生理功能与通过驱动蛋白激活型小GTP酶ARL8的活性来控制溶酶体位置和动态密切相关。然而，ARL8的活性如何被调控仍知之甚少。本研究鉴定出GTP酶激活蛋白Tre-2/Bub2/Cdc16（TBC）结构域蛋白TBC1D9B是ARL8B功能的关键负调控因子。我们证明TBC1D9B与溶酶体膜蛋白TMEM55B相关联，直接结合ARL8B-GTP，并刺激其GTP酶活性。敲除TBC1D9B或其结合伙伴TMEM55B会导致溶酶体分散、自噬流缺陷，并损害细胞对营养供应限制的适应性降解反应。这些由TBC1D9B缺失引起的溶酶体表型，在细胞中同时敲低ARL8时会被消除。综上所述，我们的数据揭示了TBC1D9B通过作为ARL8活性的负调控因子，在控制溶酶体功能中发挥关键作用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Lysosomes are highly dynamic organelles that serve antagonistic functions as terminal catabolic stations for the degradation of macromolecules and as central metabolic decision centers for anabolic growth signaling. Lysosome dysfunction is implicated in various human diseases. The physiological roles of lysosomes are linked to the control of lysosome position and dynamics via the activity of the kinesin-activating small GTPase ARL8. How the activity of ARL8 is regulated remains poorly understood. Here, we identify the GTPase-activating Tre-2/Bub2/Cdc16 (TBC) domain protein TBC1D9B as a critical negative regulator of ARL8B function. We demonstrate that TBC1D9B is associated with the lysosomal membrane protein TMEM55B, directly binds to ARL8B-GTP, and stimulates its GTPase activity. Knockout of TBC1D9B or its binding partner TMEM55B causes lysosome dispersion, defective autophagic flux, and impairs the adaptive degradative response of cells to limiting nutrient supply. These lysosomal phenotypes of TBC1D9B loss are occluded by concomitant depletion of ARL8 in cells. Collectively, our data unravel a key role for TBC1D9B in controlling lysosome function by serving as a negative regulator of ARL8 activity.

</details>
<br>

**关键词**: lysosome function, TBC1D9B, TMEM55B, ARL8B GTPase, autophagic flux, nutrient response, GTPase-activating protein, lysosome dispersion

---

### 17. ❌ Cortical representation of multidimensional handwriting movement and implications for neuroprostheses

**作者**: Zebin Wang, Guangxiang Xu, Bowen Yu, Kedi Xu, Junming Zhu, Gang Pan, Jianmin Zhang, Yueming Wang, Yaoyao Hao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70536-7](https://doi.org/10.1038/s41467-026-70536-7)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是手写运动的皮层表征及其在神经假体中的应用，属于神经科学、运动控制和脑机接口领域，与给定的医学影像分析、AI诊断、手术规划等关键词完全无关。论文未涉及医学影像处理、深度学习医学成像、多模态医学影像融合或基础模型在医学影像中的应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过分析手写运动的皮层表征，揭示了大脑如何编码多维手写运动，为开发更精确的神经假体提供了理论基础。

**关键词**: cortical representation, handwriting movement, neuroprostheses, brain-computer interface, motor control, neural decoding, multidimensional movement

---

### 18. ❌ Vacuum-induced interfacial compaction for scalable fabrication of high-performance organic solar cells

**作者**: S.T. Wang, Rui Ding, Ziyang Zhang, Yawei Liu, Jiarui Wang, Jiali Weng, Yao Zhao, Jianqi Zhang, Zihao Xu, Zheng Tang, Y. Cai, Yang Huang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70579-w](https://doi.org/10.1038/s41467-026-70579-w)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究有机太阳能电池的制造工艺（真空诱导界面压实策略），属于材料科学和可再生能源领域。所有评分关键词均涉及医学影像分析和人工智能在医疗决策中的应用，与论文主题完全无关。论文未涉及任何医学影像、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文针对有机太阳能电池因形态和界面问题导致的性能限制，提出了一种真空诱导界面压实策略，实现了大面积可扩展的高性能器件制造。

<details open>
<summary>摘要翻译</summary>

> 有机太阳能电池在下一代光伏技术中前景广阔，但其实际应用受到固有的形态与界面限制的阻碍，这些限制影响了器件性能与稳定性。本文提出一种真空诱导界面致密化策略，通过促进致密堆叠、抑制界面空隙并提升整体界面完整性，无需传统热退火或溶剂退火即可形成光滑、致密且强粘附的多层薄膜。基于此策略制备的刚性器件实现了20.51%的功率转换效率，柔性器件效率达19.13%，且成品率较高。值得注意的是，采用该方法制备的活性面积为1.0 cm²的器件及面积为15.7 cm²的组件分别实现了19.04%和17.48%的效率。当组件面积进一步扩大至67.2 cm²时，仍能保持15.37%的高效率。这些结果表明，真空诱导界面致密化策略为制备耐用、高性能有机太阳能电池提供了一条可行路径。有机太阳能电池长期受限于形态与界面问题，导致效率与稳定性下降。本研究提出的真空诱导致密化方法构建了致密光滑的界面，实现了大面积可扩展的高性能器件制备。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Organic solar cells hold great promise for next-generation photovoltaics, yet their practical deployment is impeded by intrinsic morphological and interfacial limitations that compromise device performance and stability. Herein, we introduce a vacuum-induced interfacial compaction strategy that forms smooth, compact, and strongly adhered multilayer films without conventional thermal or solvent annealing, by promoting dense stacking, suppressing interfacial voids, and improving overall interfacial integrity. Consequently, corresponding devices achieve power conversion efficiencies of 20.51% for rigid and 19.13% for flexible devices, together with a high yield. Notably, device with an active area of 1.0 cm2 and a module with an area of 15.7 cm2 fabricated with this strategy deliver efficiencies of 19.04% and 17.48%, respectively. Upon further scaling the module area to 67.2 cm2, a high efficiency of 15.37% is still attained. These results establish the vacuum-induced interfacial compaction strategy as a feasible route toward durable, high-performance organic solar cells. Organic solar cells face morphological and interfacial limits that reduce efficiency and stability. The authors present a vacuum-induced compaction method that builds dense, smooth interfaces, delivering large area-scalable high-performance devices.

</details>
<br>

**关键词**: organic solar cells, vacuum-induced interfacial compaction, morphological limitations, interfacial integrity, power conversion efficiency, large-area fabrication, device stability, multilayer films

---

### 19. ❌ Joint control of precipitation and CO2 on global long-term patterns of plant nitrogen availability

**作者**: Songbo Tang, Yixin Qiao, Jianyang Xia, Erqian Cui
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70358-7](https://doi.org/10.1038/s41467-026-70358-7)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究植物氮可用性的全球长期模式及其驱动因素（CO2和降水），属于生态学、环境科学和植物生理学领域。研究使用机器学习分析全球叶片稳定氮同位素数据，与医学影像分析、医学影像分割、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像、医学影像基础模型等关键词完全无关。论文未涉及任何医学影像、临床决策支持或医疗应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    本研究利用机器学习分析全球叶片稳定氮同位素数据（1980-2020），发现植物氮可用性先下降后稳定，主要驱动因素从CO2转变为降水。

<details open>
<summary>摘要翻译</summary>

> 植物氮素可利用性严重制约植物生长，进而限制陆地碳汇能力。越来越多的证据表明近期植物氮素可利用性呈下降趋势，但这一趋势的全球一致性及其驱动机制尚不明确。本研究基于全球37,268组叶片稳定氮同位素观测数据及辅助气候资料，运用四种机器学习算法重建了植物氮素可利用性的时空轨迹（1980–2020）。首先发现叶片稳定氮同位素（foliar stable nitrogen isotopes）存在高度空间异质性，主要与年均温相关。进一步分析表明，叶片稳定氮同位素值在1980年代普遍下降，随后在44%的陆地区域保持稳定。此外，叶片稳定氮同位素时序变化的主导驱动因子从CO₂（1980–1988）转变为降水（1989–2020）。这些模式共同揭示了植物氮素可利用性的分异轨迹，并凸显了过去数十年间降水对陆地氮循环的影响日益增强。植物氮素可利用性制约生态系统生产力，但其年代际动态尚不明确。本研究通过全球叶片δ¹⁵N数据（1980–2020）与机器学习方法表明，氮素可利用性呈现先下降后稳定的趋势，其主导驱动因子从大气CO₂转为降水。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Plant nitrogen availability critically limits plant growth and thus constrains terrestrial carbon sequestration. Growing evidence points to a recent decline in plant nitrogen availability, yet the global consistency of this trend and its underlying drivers remain unclear. Here, we reconstruct the spatiotemporal trajectory of plant nitrogen availability (1980–2020) using four machine-learning algorithms applied to a global database of 37,268 foliar stable nitrogen isotopes measurements and ancillary climate data. We first find high spatial heterogeneity in foliar stable nitrogen isotopes, primarily linked to mean annual temperature. Then, we discover that foliar stable nitrogen isotopes declined primarily during the 1980s, and subsequently remained stable across 44% of land areas. Moreover, the dominant driver in temporal variations of foliar stable nitrogen isotopes shifts from CO2 (1980–1988) to precipitation (1989–2020). These patterns collectively reveal divergent plant nitrogen availability trajectories and highlight the increasing role of precipitation in shaping terrestrial nitrogen cycles over the past decades. Plant nitrogen availability constrains ecosystem productivity, yet its decadal-scale dynamics remain unclear. Using global foliar δ¹⁵N data (1980–2020) and machine learning, this study suggests that nitrogen availability initially declined and then stabilized, as the dominant driver shifted from atmospheric CO2 to precipitation.

</details>
<br>

**关键词**: plant nitrogen availability, foliar stable nitrogen isotopes, machine learning, global patterns, CO2, precipitation, terrestrial ecosystems, decadal dynamics

---

### 20. ❌ Unpacking sources of transmission in HIV prevention trials with deep-sequence pathogen data

**作者**: Lerato E Magosi, Eric Tchetgen Tchetgen, Vlad Novitsky, Molly Pretorius Holme, Janet Moore, Pam Bachanas, Refeletswe Lebelonyane, Christophe Fraser, Sikhulile Moyo, Kathleen E. Hurwitz, Tendani Gaolathe, Ravi Goyal, Joseph Makhema, Shahin Lockman, Max Essex, Victor De Gruttola, Marc Lipsitch
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70203-x](https://doi.org/10.1038/s41467-026-70203-x)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是HIV预防试验中的传播源分析，使用深度测序病原体数据和统计方法评估不同感染源的相对贡献。研究领域属于传染病流行病学、公共卫生和生物统计学，与医学影像分析、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像或医学影像基础模型完全无关。所有关键词均未在标题或摘要中出现，论文内容也未涉及任何医学影像技术或AI医学影像应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The results suggest that the impact of the BCPP trial intervention was curtailed by sources of transmission outside the trial area and could be considerably larger if applied nationally and recommend that the impact of sources of transmission beyond the reach of the intervention be considered when designing and evaluating interventions to inform public health programs.

!!! tip deepseek-chat TL;DR

    该研究开发了一种使用深度测序病原体数据的统计方法，评估HIV预防试验中不同感染源的贡献，发现在博茨瓦纳联合预防项目中，90%的新感染来自试验区域外的个体，全国推广干预措施可使传播减少59%。

<details open>
<summary>摘要翻译</summary>

> 摘要 为制定有效的艾滋病预防策略以指导公共卫生政策，必须明确预防研究中的主要感染源。为此，我们开发了一种统计方法，利用深度（或下一代）测序的病原体数据，评估传染病预防社区随机试验中不同感染源的相对贡献。我们将此方法应用于博茨瓦纳综合预防项目（BCPP），估计在接受综合预防（包括普遍艾滋病检测与治疗）的社区中，90% [95%置信区间（CI）：80–94] 的新发感染源自试验区域外社区的个体。根据模型估算，若将BCPP干预措施推广至全国所有社区，试验社区内接受干预者的传播风险将相对降低59% [3–87]，超过仅对试验社区实施干预时观察到的30%降幅。我们的结果表明，BCPP试验干预的效果受到试验区域外传播源的限制，若在全国范围内应用，其影响可能显著增强。我们建议，在设计和评估干预措施以为公共卫生规划提供依据时，应考虑干预范围之外的传播源的影响。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract To develop effective HIV prevention strategies to guide public health policy the main sources of infection in HIV prevention studies must be identified. Accordingly, we devised a statistical approach that estimates the relative contribution of different sources of infection in community-randomized trials of infectious disease prevention using deep- (or next generation) sequenced pathogen data. We applied this approach to the Botswana Combination Prevention Project (BCPP) and estimated that 90% [95% Confidence Interval (CI): 80–94] of new infections in communities that received combination prevention (including universal HIV test-and-treat) originated from individuals residing in communities outside the trial area. We estimate from our model that the relative benefit of providing the BCPP intervention to all communities nationwide would be a 59% [3–87] reduction in transmissions to recipients in trial communities, exceeding the 30% reduction observed when providing the BCPP intervention to trial communities only. Our results suggest that the impact of the BCPP trial intervention was curtailed by sources of transmission outside the trial area and could be considerably larger if applied nationally. We recommend that the impact of sources of transmission beyond the reach of the intervention be considered when designing and evaluating interventions to inform public health programs.

</details>
<br>

**关键词**: HIV prevention, transmission sources, deep-sequence pathogen data, community-randomized trials, statistical modeling, Botswana Combination Prevention Project, public health policy, infection origin

---

### 21. ❌ Catalytic enantioselective synthesis of azahelicenes via cascade Pictet-Spengler reaction and dehydrogenative aromatization

**作者**: Tianren Qin, Wansen Xie, Xiaoyu Yang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70617-7](https://doi.org/10.1038/s41467-026-70617-7)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要描述的是有机化学合成领域的研究，具体涉及azahelicenes的催化对映选择性合成方法，通过级联Pictet-Spengler反应和脱氢芳构化实现。这与医学图像分析、人工智能临床决策支持、深度学习医学成像、疾病诊断/预后预测、手术规划、多模态医学成像或医学成像基础模型等主题完全无关。所有关键词均与论文内容无任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种通过级联Pictet-Spengler反应和脱氢芳构化实现azahelicenes催化对映选择性合成的新方法。

**关键词**: catalytic enantioselective synthesis, azahelicenes, cascade reaction, Pictet-Spengler reaction, dehydrogenative aromatization, organic synthesis, asymmetric catalysis

---

### 22. ❌ Photoinduced radical-mediated atomic dispersion of noble metal nanoparticles

**作者**: Xiang Chen, Qingfei Zhao, Jingyuan Zhang, Kehan Zhou, Xufang Qian, ZhenFeng BIAN
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70742-3](https://doi.org/10.1038/s41467-026-70742-3)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是光诱导贵金属纳米颗粒原子级分散的催化化学方法，属于材料科学、化学工程和催化领域。所有评分关键词均涉及医学影像分析、人工智能辅助临床决策等医疗健康领域，与论文的化学催化主题完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种光诱导氯自由基在室温下将贵金属纳米颗粒分散为单原子催化剂的新方法，显著提升了工业催化剂的加氢反应活性。

<details open>
<summary>摘要翻译</summary>

> 将贵金属纳米颗粒转化为原子级分散催化剂，是提高金属利用率和再生团聚催化剂活性的长期目标。然而，传统方法通常需要高温、特定气氛或复杂的化学过程。我们提出了一种在环境条件下实现贵金属纳米颗粒原子级分散的新型光诱导策略。实验和密度泛函理论计算表明，氯自由基（•Cl）与•O2-共同促进了Pd-Pd键的断裂。形成的中间体[PdCl4]2-通过静电相互作用吸附在TiO2上，并在脱氯后稳定形成单原子Pd1-N2O1结构。该方法适用于多种贵金属（Pd、Pt、Rh）和不同的氧化物载体（TiO2和WO3），并在苯乙烯加氢反应中，将商用Pd/C和工业废料Pd/C催化剂的活性分别显著提高了17.8倍和26倍。这一方法为推进催化技术提供了一种简单、绿色且可持续的解决方案。将金属纳米颗粒转化为单原子催化剂仍具挑战。这种光驱动方法利用氯自由基在室温下分散贵金属，极大地提升了工业催化剂的活性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The transformation of noble metal nanoparticles into atomically dispersed catalysts has been a long-standing goal to enhance metal utilization and regenerate the activity of agglomerated catalysts. Traditional methods, however, often require high temperatures, specific atmospheres, or complex chemical processes. We present a novel photoinduced strategy for atomic dispersion of noble metal nanoparticles under ambient conditions. Experimental and density functional theory calculations reveal that chlorine radicals (•Cl), together with •O2-, promote Pd-Pd bond cleavage. The intermediate [PdCl4]2- species formed adsorbs onto TiO2 via electrostatic interactions and, upon dechlorination, stabilizes into a single-atom Pd1-N2O1 structure. This method is applicable to various noble metals (Pd, Pt, Rh) and different oxide supports (TiO2 and WO3), and significantly enhances the catalytic activity of both commercial Pd/C and industrial waste Pd/C catalysts by 17.8-fold and 26-fold, respectively, in the hydrogenation of styrene. This approach offers a simple, green, and sustainable solution for advancing catalytic technologies. Converting metal nanoparticles into single-atom catalysts remains a challenge. This light-driven method uses chlorine radicals to disperse noble metals at room temperature, dramatically boosting the activity of industrial catalysts.

</details>
<br>

**关键词**: photoinduced radical, atomic dispersion, noble metal nanoparticles, single-atom catalysts, chlorine radicals, catalytic activity enhancement, hydrogenation, Pd/C catalyst

---

### 23. ❌ Frazzled/DCC directs spatial progenitor integration ensuring steady-state intestinal turnover

**作者**: Lisa Zipper, P. Ramon-Cañellas, Filiz Akkas-Gazzoni, Tobias Reiff
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70704-9](https://doi.org/10.1038/s41467-026-70704-9)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文研究果蝇肠道稳态的细胞机制，涉及Netrin-B/Frazzled信号通路指导肠母细胞迁移以替换衰老肠细胞，属于发育生物学和细胞生物学领域。论文完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或基础模型等主题，与所有评分关键词均无关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that a conserved axonal guidance cue directs enteroblasts (EB), the immediate ISC daughters, to selectively replace worn-out adjacent and remote EC with identical frequency, establishing spatially directed EB migration and integration as essential for intestinal homeostasis.

!!! tip deepseek-chat TL;DR

    该研究揭示了果蝇肠道稳态中，衰老肠细胞表达的Netrin-B通过Frazzled/DCC受体引导肠母细胞定向迁移和整合，从而确保远程肠细胞的替换机制。

<details open>
<summary>摘要翻译</summary>

> 摘要 成年上皮器官通过干细胞增殖与局部细胞间信号介导的衰老上皮细胞替换之间的紧密耦合，实现持续稳态更新1,2。与多数真核生物上皮组织类似，成年果蝇中肠的吸收性肠上皮细胞（EC）呈六边形蜂巢状排列。在EC的三细胞连接处，肠道干细胞（ISC）呈分散分布，使得约三分之二的EC可直接由相邻ISC更新。然而，剩余三分之一远离ISC的EC的替换机制尚不明确。本研究揭示，一种保守的轴突导向信号能引导肠母细胞（EB，即ISC的直接子代细胞）以相同频率选择性替换衰老的相邻及远端EC。衰老EC表达Netrin-B配体，可吸引依赖Frazzled/DCC受体的EB伪足形成，并引导EB向表达Netrin-B的EC迁移。我们新开发的"Hamelin"检测法证实了EB向Netrin-B源的Frazzled依赖性迁移，并提示中肠前体细胞具有侵袭性行为——它们可跨越器官边界进入后肠。综上，我们确立了空间导向的EB迁移与整合对肠道稳态至关重要，并为近期将保守的Netrins与Frazzled/DCC信号通路作为转移治疗靶点的研究提供了首次机制性证据支持。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Adult epithelial organs undergo continual steady-state turnover that is achieved by tight coupling of stem cell production with replacement of worn-out epithelial cells by local intercellular signalling 1,2 . Like many eukaryotic epithelia, absorptive enterocytes (EC) of the adult Drosophila midgut are arranged in a hexagonal, honeycomb-like pattern. On tricellular nexuses of EC, intestinal stem cells (ISC) are scattered in a way so that around two thirds of EC can be renewed directly by adjacent ISC. However, the mechanism for replacement of the remaining third of remotely located EC is unknown. Here, we show that a conserved axonal guidance cue directs enteroblasts (EB), the immediate ISC daughters, to selectively replace worn-out adjacent and remote EC with identical frequency. Worn-out EC express Netrin-B ligands that attract Frazzled/DCC-receptor dependent EB protrusions and subsequent EB migration towards the Netrin-B expressing EC. Our newly developed ‘Hamelin’ assay confirms Frazzled-dependent EB migration towards Netrin-B sources and hints to invasive progenitor behaviour as midgut progenitors cross the organ boundary into the hindgut. Together, we establish spatially directed EB migration and integration as essential for intestinal homeostasis and provide first mechanistic support for recent findings resuscitating conserved Netrins and Frazzled/DCC-signalling as therapeutic target in metastasis.

</details>
<br>

**关键词**: intestinal homeostasis, Netrin-B, Frazzled/DCC, enteroblast migration, cell replacement, Drosophila midgut, progenitor integration, tricellular nexus

---

### 24. ❌ Predator-driven microbial feedback loops promote plant health

**作者**: Gen Li, Ting Liu, Huiyu Chuai, Huiping Ma, Zhen Yang, Yangchu Xu, Huixin Li, Qirong Shen, Feng Hu, Stefan Geisen, Alexandre Jousset, Zhong Wei, Shane Hogle
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70413-3](https://doi.org/10.1038/s41467-026-70413-3)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究土壤微生物组、线虫捕食与植物健康的关系，属于农业生态学、微生物生态学领域。所有评分关键词均涉及医学影像分析、AI医疗诊断等医学信息学内容，与论文研究的农业生态学主题完全无关。论文未涉及任何医学影像、深度学习、疾病诊断、手术规划或医学数据融合相关内容。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An animal-mediated pathway of microbiome assembly that enhances resistance to pathogen invasion and provides a trophically informed framework for designing stable, disease-suppressive microbiomes in agriculture is revealed.

!!! tip deepseek-chat TL;DR

    该研究揭示了线虫捕食通过重组微生物组形成反馈回路来抑制土壤病原体、促进植物健康的机制，为设计稳定的农业病害抑制微生物组提供了理论框架。

<details open>
<summary>摘要翻译</summary>

> 自上而下的营养级联作用是微生物组动态的关键驱动因素，但其结果难以预测，且对病原体控制的后果尚不明确。我们通过将不同复杂度的合成细菌群落与田间研究及微观实验相结合，以检验食微生物线虫是否会重组微生物组从而抑制土传病害。田间研究表明，健康植物周围存在更强的线虫-微生物关联；微观实验证实，线虫的存在能产生稳定的抑制效果，而仅含微生物的群落在病原体入侵下会崩溃。线虫的捕食行为消耗了非偏好性细菌类群，并富集了变形菌门内代谢功能多样的类群，从而提升了群落水平的拮抗潜力，并促进了与病原体抑制相关的互补性资源利用互作，产生的抑制效果超越了个体或成对效应。一个由线虫捕食者、植物病原体以及两种功能互补的植物相关细菌构成的最小四组分反馈回路，解释了这一涌现性结果。综上所述，这些结果揭示了一条动物介导的微生物组组装途径，该途径能增强对病原体入侵的抵抗力，并为农业中设计稳定、具有病害抑制功能的微生物组提供了一个基于营养级联关系的理论框架。自上而下的营养级联作用是微生物组动态的关键驱动因素，但难以预测。本研究作者证明，线虫驱动的微生物组变化通过一个涉及线虫和细菌的反馈回路，增强了病原体抑制并促进了植物健康。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Top-down trophic interactions are major drivers of microbiome dynamics, yet their outcomes are difficult to predict and their consequences for pathogen control remain unclear. We combine synthetic bacterial communities of varying complexity with field studies and microcosm assays to test whether microbivorous nematodes reorganize microbiomes to suppress soilborne disease. Field studies show stronger nematode-microbe associations around healthy plants, and microcosm assays confirm that nematode presence produces stable suppression, whereas microbe-only communities collapse under pathogen invasion. Nematode predation depletes non-preferred bacterial taxa and enriches metabolically versatile taxa within Proteobacteria, increasing community-level antagonistic potential and promoting complementary resource-use interactions linked to pathogen inhibition, yielding suppression beyond individual or pairwise effects. A minimal four-component feedback loop linking a nematode predator, plant pathogens, and two plant-associated bacteria with complementary functions accounts for the emergent outcome. Together, these results reveal an animal-mediated pathway of microbiome assembly that enhances resistance to pathogen invasion and provide a trophically informed framework for designing stable, disease-suppressive microbiomes in agriculture. Top-down trophic interactions are critical drivers of microbiome dynamics but are difficult to predict. Here, the authors demonstrate that nematode-driven shifts in microbiomes enhance pathogen suppression and promote plant health through a feedback loop involving nematodes and bacteria.

</details>
<br>

**关键词**: microbiome dynamics, nematode predation, pathogen suppression, plant health, soilborne disease, trophic interactions, feedback loop, disease-suppressive microbiomes

---

### 25. ❌ MFF budding from mitochondria regulates melanosome size and maturation

**作者**: Ana Paula Magalhães Rebelo, Aurora Maracani, Samuele Greco, Federica Dal Bello, Lucia Santorelli, Marco Gerdol, Alberto Pallavicini, Tomáš Knedlík, Sara Schiavon, Luca Scorrano, Philip S. Goff, Christian Frezza, Elena V. Sviderskaya, Paolo Grumati, Marta Giacomello
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70572-3](https://doi.org/10.1038/s41467-026-70572-3)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文研究的是细胞生物学中黑色素体成熟与线粒体分裂因子MFF的分子机制，涉及细胞器相互作用、蛋白质运输和肌动蛋白组装等基础生物学过程。论文完全不涉及医学影像分析、深度学习、AI诊断、手术规划、多模态医学影像或医疗AI模型等主题。所有关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that the mitochondrial fission factor protein (MFF) is involved in melanosome fission, and it is shown that MFF interacts with regulators of the ARP2/3 complex, which drives F-actin nucleation.

!!! tip deepseek-chat TL;DR

    该研究发现线粒体分裂因子MFF通过调控ARP2/3复合物依赖的肌动蛋白组装介导黑色素体分裂，从而调节黑色素体大小和成熟过程。

<details open>
<summary>摘要翻译</summary>

> 黑素体是溶酶体相关细胞器，负责合成与储存黑色素。其成熟过程受线粒体相互作用的调控，并涉及通过管状运输和分裂事件实现的蛋白质输出与循环机制，这些机制目前尚未明确。本研究证实线粒体分裂因子蛋白（MFF）参与黑素体分裂过程。MFF在线粒体与黑素体之间转运，并定位于黑素体分裂位点。下调MFF（而非动力相关蛋白1[DRP1]）会导致黑素体增大、细胞内黑色素积累以及黑素体腔内分解代谢增强，表明MFF依赖的黑素体分裂是其成熟的必要条件。研究发现MFF与驱动F-肌动蛋白成核的ARP2/3复合体调节因子相互作用。在富含MFF的膜收缩部位，肌动蛋白丝在黑素体间聚集，而沉默ARP2/3亚基会重现黑素体尺寸增大的表型。MFF通过ARP2/3复合体调控肌动蛋白依赖的黑素体分裂，这揭示了MFF在线粒体外调控黑素体稳态的功能。黑素体成熟依赖于尚未明晰的分裂机制。本研究表明，线粒体分裂因子MFF通过定位于分裂位点、在线粒体与黑素体间转运以及调控ARP2/3依赖的肌动蛋白组装，介导黑素体分裂过程。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Melanosomes are lysosome-related organelles that produce and accumulate melanin. Their maturation is regulated through interactions with mitochondria and involves the export and recycling of proteins via tubular transport and fission events whose mechanisms are unknown. Here, we demonstrate that the mitochondrial fission factor protein (MFF) is involved in melanosome fission. MFF is trafficked between mitochondria and melanosomes and locates at melanosome fission events. Upon downregulation of MFF, but not of dynamin-related protein 1 (DRP1), melanosomes enlarge, intracellular melanin accumulates, and melanosomal lumenal catabolism increases, indicating that MFF-dependent melanosome fission is required for their maturation. We show that MFF interacts with regulators of the ARP2/3 complex, which drives F-actin nucleation. Actin filaments accumulate between melanosomes at MFF-enriched membrane constriction sites, and silencing of ARP2/3 subunits mimics the increase in melanosome size. MFF regulates actin-dependent fission of melanosomes via the ARP2/3 complex, indicating an extramitochondrial function for MFF in the regulation of melanosome homeostasis. Melanosome maturation depends on poorly understood fission processes. Here, the authors demonstrate that the mitochondrial fission factor MFF mediates melanosome division by localising to division sites, trafficking between mitochondria and melanosomes and regulating ARP2/3-dependent actin assembly.

</details>
<br>

**关键词**: melanosome, mitochondrial fission factor (MFF), actin assembly, ARP2/3 complex, organelle fission, melanin accumulation, melanosome maturation, intracellular trafficking

---

### 26. ❌ Noradrenaline causes a spread of association in the hippocampal cognitive map

**作者**: Renée S. Koolschijn, Prakriti Parthasarathy, Michael Browning, Xenia Przygodda, Liliana Capitão, William T. Clarke, Tim P. Vogels, Jill X. O’Reilly, Helen C. Barron
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70659-x](https://doi.org/10.1038/s41467-026-70659-x)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是神经科学领域，具体探讨去甲肾上腺素对海马认知地图中关联扩散的影响，采用药理学干预和神经网络建模方法。所有评分关键词均涉及医学影像分析、AI诊断、手术规划等临床应用方向，而该论文完全不涉及医学影像处理、疾病诊断或临床决策支持，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究发现去甲肾上腺素通过改变突触可塑性导致海马认知地图中的关联扩散，从而在行为上表现为过度泛化。

<details open>
<summary>摘要翻译</summary>

> 摘要 哺乳动物大脑利用认知地图组织关于世界中实体及其相互关系的知识。在形成认知地图时，必须在扩展地图以进行新颖推断与存储过往经验的真实副本之间做出必要的权衡。然而，控制这种权衡的神经机制仍不明确。通过采用结合人类药理学干预与神经网络建模的跨尺度研究方法，我们发现神经调节物质去甲肾上腺素能引发跨海马认知地图的显著“关联扩散”。这种神经层面的关联扩散可通过突触可塑性变化来解释，该变化能预测行为中的过度泛化现象。因此，学习过程中升高的去甲肾上腺素会扩大认知地图中可塑性的“平滑核”，使得原本不相关的记忆相互链接并发生扭曲。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract The mammalian brain organises knowledge about entities in the world and relationships between them using cognitive maps. When forming a cognitive map, there is a necessary trade-off between extending the map to make novel inferences, and storing a veridical copy of past experience. However, the neural mechanisms that control this trade-off remain unknown. Using a cross-scale approach that combines a pharmacological intervention in humans with neural network modelling, we show that the neuromodulator noradrenaline elicits a significant ‘spread of association’ across hippocampal cognitive maps. This neural spread of association can be explained by changes in synaptic plasticity that predict overgeneralisation in behaviour. Thus, elevated noradrenaline during learning increases the ‘smoothing kernel’ for plasticity across the cognitive map, allowing disparate memories to become linked and distorted.

</details>
<br>

**关键词**: noradrenaline, hippocampal cognitive map, spread of association, synaptic plasticity, overgeneralization, neural network modeling, pharmacological intervention

---

### 27. ❌ TYK2 mediates neuroinflammation in Alzheimer’s disease brains with TDP-43 pathology

**作者**: Laura E. König, Steve Rodriguez, Clemens Hug, Shayda Daneshvari, Alexander Chung, Mark Appleman, Max Tsai, Gary A. Bradshaw, Aslı Şahin, Yuyu Song, George Zhou, Robyn J. Eisert, Federica Piccioni, Christine Marques, Sharon Powley, James Yarmolinsky, Brian J. Wainger, Sudeshna Das, Marian Kalocsay, Abbas Dehghan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70243-3](https://doi.org/10.1038/s41467-026-70243-3)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究阿尔茨海默病和ALS中的神经炎症机制，聚焦于TYK2介导的干扰素信号通路、TDP-43病理和药物干预，未涉及医学影像分析、分割、深度学习、AI诊断、预后预测、手术规划、多模态影像或基础模型等主题。所有关键词与论文内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The spatial coincidence of cdsRNA and pTDP-43 inclusions in human postmortem tissue with Alzheimer's disease pathology, and upregulated interferon response genes in affected regions are reported.

!!! tip deepseek-chat TL;DR

    该研究发现TYK2介导的神经炎症是TDP-43相关阿尔茨海默病和C9ORF72-ALS的共同机制，并证实TYK2抑制剂deucravacitinib能挽救cdsRNA诱导的毒性。

<details open>
<summary>摘要翻译</summary>

> 摘要 神经炎症是阿尔茨海默病与肌萎缩侧索硬化症等神经退行性疾病的病理特征。细胞质双链RNA会触发人类神经细胞的I型干扰素反应并导致细胞死亡，该现象已在C9ORF72基因突变型ALS患者神经元中被发现。本研究报道了在阿尔茨海默病病理的人体尸检组织中，细胞质双链RNA与磷酸化TDP-43包涵体存在空间共定位现象，且受累脑区干扰素应答基因表达上调。在人类TDP-43 G298S诱导多能干细胞来源的皮层神经元模型中，同样观察到细胞质双链RNA的积累。我们采用隐蔽外显子检测作为TDP-43错误定位的替代指标，证实FDA批准的JAK抑制剂巴瑞替尼和鲁索替尼（通过阻断干扰素信号通路发挥作用）仅在对隐蔽外显子表达升高的脑组织具有保护作用。CRISPR筛选显示TYK2为关键靶点，敲低TYK2及选择性TYK2抑制剂氘可来昔替尼均能挽救细胞质双链RNA诱导的神经毒性。本研究揭示了TDP-43相关阿尔茨海默病与C9ORF72-ALS存在平行的神经炎症机制，该机制依赖于TYK2——一个潜在的疾病修饰靶点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Neuroinflammation is a pathological feature of neurodegenerative diseases like Alzheimer’s disease and ALS. Cytoplasmic dsRNA (cdsRNA) triggers a type-I interferon response in human neural cells, leading to their death, and is found in neurons of C9ORF72 -ALS patients. Here, we report the spatial coincidence of cdsRNA and pTDP-43 inclusions in human postmortem tissue with Alzheimer’s disease pathology, and upregulated interferon response genes in affected regions. CdsRNA also accumulates in a human TDP-43 G298S iPSC cortical neuronal model. We use cryptic exon detection as a proxy for TDP-43 mislocalization and demonstrate that FDA-approved JAK inhibitors baricitinib and ruxolitinib, which block interferon signaling, show protective effects only in brains with elevated cryptic exon expression. A CRISPR screen reveals TYK2 as a top hit, and TYK2 knockdown and the selective TYK2 inhibitor deucravacitinib rescue cdsRNA-induced toxicity. We find parallel neuroinflammatory mechanisms, dependent on TYK2 - a potential disease-modifying target - for TDP-43-associated Alzheimer’s disease and C9ORF72 -ALS.

</details>
<br>

**关键词**: neuroinflammation, Alzheimer's disease, TDP-43 pathology, TYK2, interferon signaling, cdsRNA, JAK inhibitors, deucravacitinib

---

### 28. ❌ DIS3 mutations enhance AID-driven translocations during B-cell activation, promoting transformation to multiple myeloma

**作者**: Tomasz M. Kuliński, Olga Gewartowska, Mélanie Mahé, Karolina Kasztelan, Nina Durys, Anna Stroynowska-Czerwińska, Marta Jedynak-Slyvka, Ewelina P. Owczarek, Debadeep Chaudhury, Marcin Nowotny, Aleksandra Pękowska, Bertrand Séraphin, Andrzej Dziembowski
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70386-3](https://doi.org/10.1038/s41467-026-70386-3)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究DIS3基因突变在B细胞活化中如何增强AID驱动的染色体易位，促进多发性骨髓瘤转化，属于分子生物学、癌症遗传学和免疫学领域。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等，与论文的分子机制研究完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that the clinically relevant DIS3 G766R variant causes chromosomal translocations in B-cells, characterized by aberrant AID activity signatures, which facilitates transformation in multiple myeloma without broadly affecting B-cell physiology.

!!! tip deepseek-chat TL;DR

    该研究发现DIS3基因突变通过增强AID酶活性导致染色体易位，从而驱动多发性骨髓瘤的发生。

<details open>
<summary>摘要翻译</summary>

> 摘要 DIS3是一种关键的核糖核酸降解酶，对免疫球蛋白类别转换重组至关重要，它能促进活化诱导胞苷脱氨酶在DNA双链上的活性，从而诱导双链DNA断裂。在体细胞超突变过程中，AID依赖性损伤主要发生在非模板DNA链上。损害DIS3外切核糖核酸酶活性的显性突变在多发性骨髓瘤中常见，但其在致癌中的作用尚不明确。本研究通过敲入小鼠模型发现，临床相关的DIS3 G766R变异会导致B细胞染色体易位，其特征是异常的AID活性特征。这些小鼠会发展为降植烷诱导的浆细胞瘤，模拟早期多发性骨髓瘤。在临床多发性骨髓瘤样本中，DIS3突变与IGH易位及驱动基因中AID驱动的损伤相关。机制上，突变的DIS3在染色质结合RNA上积累，特别是在异常的AID靶点处，促进DNA双链突变。这导致AID依赖性双链DNA断裂增加，促进微同源介导的致癌重排。易位特异性地发生在功能完整的类别转换重组过程中。DIS3 G766R突变不会破坏活化B细胞的染色质结构，但利用空间邻近性使增强子和原癌基因永久并置，促进转化。因此，功能获得性DIS3突变增强了AID的混杂性，驱动IGH易位和多发性骨髓瘤发展，而不广泛影响B细胞生理功能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract DIS3, a key nuclear RNA-degrading enzyme, is essential for immunoglobulin class switch recombination (CSR), promoting activation-induced cytidine deaminase (AID) activity on both DNA strands to induce double-strand DNA breaks. During somatic hypermutation, AID-dependent lesions predominantly occur on the non-template DNA strand. Dominant mutations impairing DIS3 exoribonucleolytic activity are common in multiple myeloma (MM), but their role in carcinogenesis remains unclear. Here we show, using a knock-in mouse model, that the clinically relevant DIS3 G766R variant causes chromosomal translocations in B-cells, characterized by aberrant AID activity signatures. The mice develop pristane-induced plasmacytomas, modeling early-stage MM. In clinical MM samples, DIS3 mutations correlate with IGH translocations and AID-driven lesions in driver genes. Mechanistically, mutated DIS3 accumulates on chromatin-bound RNA, particularly at aberrant AID target sites, promoting mutations on both DNA strands. This results in increased AID-dependent double-strand DNA breaks, fostering microhomology-mediated oncogenic rearrangements. Translocations occur specifically during CSR, which remains functionally intact. The DIS3 G766R mutation does not disrupt chromatin architecture in activated B cells but exploits spatial proximity to permanently juxtapose enhancers and proto-oncogenes, facilitating transformation. Thus, gain-of-function DIS3 mutations enhance AID promiscuity, driving IGH translocations and MM development without broadly affecting B-cell physiology.

</details>
<br>

**关键词**: DIS3 mutation, AID activity, chromosomal translocations, multiple myeloma, B-cell activation, class switch recombination, oncogenic rearrangements, gain-of-function

---

### 29. ❌ EPInformer: scalable and integrative prediction of gene expression from promoter-enhancer sequences with multimodal epigenomic profiles

**作者**: Jiecong Lin, Zhijian Li, Yajie Zhao, Ruibang Luo, Luca Pinello
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70535-8](https://doi.org/10.1038/s41467-026-70535-8)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究专注于计算生物学和基因组学领域，具体研究基因表达预测、启动子-增强子序列分析和多模态表观基因组学数据整合。所有评分关键词均涉及医学影像分析、AI临床决策支持、疾病诊断/预后、手术规划等医学影像应用领域，而该论文完全不涉及医学影像数据（如CT、MRI、超声）、医学图像分割、疾病诊断或手术规划等内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    EPInformer is presented, a scalable deep-learning framework for predicting gene expression by integrating promoter-enhancer interactions with their sequences, epigenomic profiles, and chromatin contacts that outperforms existing gene expression prediction models in rigorous cross-chromosome validation.

!!! tip deepseek-chat TL;DR

    该研究开发了EPInformer模型，通过整合多模态表观基因组学数据从启动子-增强子序列预测基因表达，实现了可扩展且准确的基因表达预测。

**关键词**: gene expression prediction, promoter-enhancer sequences, multimodal epigenomic profiles, EPInformer, scalable prediction, integrative prediction, computational genomics, deep learning model

---

### 30. ❌ High-Fidelity quantum teleportation mediated by hole transfer in an acceptor–donor–radical molecular triad

**作者**: Junhang Duan, Shunta Nakamura, Chelsie L. Greene, Samuel B. Tyndall, Ryan M. Young, Matthew D. Krzyaniak, Michael R. Wasielewski
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70654-2](https://doi.org/10.1038/s41467-026-70654-2)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究是关于量子信息科学中的量子隐形传态，通过分子三合体中的空穴转移实现高保真度传输。研究领域属于物理化学、量子计算和分子电子学，与医学图像分析、人工智能临床决策支持、深度学习医学成像、疾病诊断/预后预测、手术规划、多模态医学成像或医学成像基础模型完全无关。所有关键词均得0分，因为论文内容与医学图像分析领域无任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了量子信息传输中保真度不足的问题，通过设计一种受体-供体-自由基分子三合体，利用空穴转移机制实现了高保真度的量子隐形传态。

**关键词**: quantum teleportation, hole transfer, acceptor-donor-radical triad, molecular triad, high-fidelity, quantum information, molecular electronics, spin dynamics

---

### 31. ❌ Highly ionic-dispersed oxygen electrode for reversible proton ceramic electrochemical cells

**作者**: Xiaoyu Wang, Zhaohui Cai, Zeping Chen, Donliang Liu, Wanqing Chen, JianQiu Zhu, Wenhuai Li, Xixi Wang, Linjuan Zhang, Wei Wang, Chuan Zhou, Wei Zhou, Zongping Shao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70738-z](https://doi.org/10.1038/s41467-026-70738-z)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是可逆质子陶瓷电化学电池（R-PCECs）的氧电极材料，属于材料科学、电化学和能源技术领域，涉及多元素微掺杂钙钛矿材料、原子探针层析成像、密度泛函理论计算、质子传导性和热机械稳定性等。所有评分关键词均与医学影像分析、人工智能、疾病诊断、手术规划等医学领域相关，而本文完全不涉及医学、影像或临床决策支持，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了可逆质子陶瓷电化学电池中氧电极质子传导性不足和热机械稳定性差的问题，通过开发多元素微掺杂钙钛矿材料，降低了质子吸附/扩散能垒，提高了电池性能和长期稳定性。

<details open>
<summary>摘要翻译</summary>

> 摘要 可逆质子陶瓷电化学电池（R-PCECs）商业化的主要挑战在于其氧电极在水蒸气存在的空气中质子电导率不足以及热机械稳定性较差。本文报道了一种多元素微掺杂的BaCoO3-δ基钙钛矿材料，通过在离子亚结构中引入无序性以最大化氧-水反应活性。原子探针断层扫描和密度泛函理论计算表明，钙钛矿氧化物中均匀的离子分布降低了质子吸附/扩散能垒。此外，热驱动的温和氧释放可被有益的质子吸收进一步抵消，从而提高了氧电极的热机械耐久性。基于此材料制备的R-PCECs在600°C下实现了1.56 W cm-2的峰值功率密度，并在1.3 V电压下达到2.0 A cm-2的电解电流密度，同时展现出超过780小时的长期稳定性，其在燃料电池模式和电解模式下的衰减率分别为19.3 μV h-1和16.9 μV h-1。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract The key challenges for commercializing reversible proton ceramic electrochemical cells (R-PCECs) are the insufficient proton conductivity and inferior thermomechanical stability of oxygen electrodes in air with water vapor. We report a multielement micro-doped BaCoO 3-δ -based perovskite material, in which disorder is induced in the ionic substructure to maximize the oxygen-water reaction activity. Atom probe tomography and density functional theory calculations reveal that reduced proton adsorption/diffusion energy barriers are triggered by homogeneous ion distributions in the perovskite oxide. Moreover, the thermally driven mild oxygen release can be further offset by beneficial proton uptake, thereby increasing the thermomechanical durability of the oxygen electrode. The resulting R-PCECs obtain a peak power density of 1.56 W cm -2 and an electrolysis current density of 2.0 A cm -2 @1.3 V at 600 °C while demonstrating long-term stability exceeding 780 hours, with degradation rates of 19.3 and 16.9 μV h -1 in fuel cell and electrolysis modes, respectively.

</details>
<br>

**关键词**: reversible proton ceramic electrochemical cells, oxygen electrode, perovskite material, proton conductivity, thermomechanical stability, atom probe tomography, density functional theory, long-term stability

---

### 32. ❌ Solvation sheath reorganization enables fast ion transfer kinetics in lithium-ion battery

**作者**: Menglu Li, Di Lu, Jinze Wang, Shuoqing Zhang, Ling Lv, Baochen Ma, Heng Zhu, Long Li, S. Yang, Zirui Li, Yuefei Wu, Jiacheng Qi, Liwu Fan, R. Li, Lixin Chen, Tao Deng, Xiulin Fan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70570-5](https://doi.org/10.1038/s41467-026-70570-5)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究锂离子电池电解质的离子传输动力学，通过调控溶剂化结构改善离子传输性能，属于能源材料与电化学领域。所有评分关键词均涉及医学影像分析、人工智能辅助诊断、手术规划等医疗健康领域，与论文的电池电解质研究完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了锂离子电池在极端条件下离子传输缓慢的问题，通过重新设计电解质溶剂化结构，实现了电池在-40°C低温下的稳定循环和快速充电性能。

<details open>
<summary>摘要翻译</summary>

> 传统电解质中离子传输动力学的局限性，尤其在极端工况下，源于欠佳的溶剂化结构和低效的电荷载流子利用。本文提出一种战略性电解质设计，通过调控分子间相互作用和溶剂分子体积来重构锂离子配位几何结构，从根本上克服了这些传输限制。通过引入具有低偶极矩和小分子尺寸的优化调节剂，广泛的阴离子聚集被有效解离为紧凑的离子传导域，同时增加了自由电荷载流子数量并提升了离子迁移率。在此原理指导下，采用二氯甲烷（85.11 Å，2.36 Debye）设计的电解质展现出锂离子在相邻配位点间的快速跃迁（乙腈配位点间为152.3 ps，FSI-配位点间为115.7 ps）。该电解质实现了1.0 Ah 4.5 V石墨负极（3.13 mAh cm-2）||LiNi0.8Mn0.1Co0.1O2正极（2.85 mAh cm-2）软包电池的稳定循环，在-40 °C下可释放0.87 Ah容量，显著优于在此温度下丧失可逆容量的商用碳酸酯基电解质。本研究确立了快速离子传输电解质的基础设计原则，为极端场景下新一代锂离子电池的发展开辟了道路。缓慢的离子传输限制了锂离子电池在快速充电和低温下的性能。本工作建立了一个基于分子间相互作用和分子体积的电解质设计框架，以重塑锂离子溶剂化结构，使锂离子电池能够在-50 °C和6 C倍率下稳定运行。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The limitations of ion transport kinetics in conventional electrolytes, particularly under extreme operating conditions, arise from suboptimal solvation structures and inefficient charge carrier utilization. Here, we present strategic electrolyte design that reconfigures Li⁺ coordination geometry by modulating intermolecular interactions and solvent molecule volume, fundamentally overcoming these transport constraints. By incorporating an optimized moderator with a low dipole moment and small molecular size, extensive anion aggregation is effectively disrupted into compact ion conduction domains, simultaneously increasing the number of free charge carriers and enhancing ion mobility. Guided by this principle, the designed electrolyte with dichloromethane (85.11 Å, 2.36 Debye) exhibits rapid Li+ hopping between adjacent coordination sites (152.3 ps for acetonitrile and 115.7 ps for FSI-). This electrolyte enables stable cycling of 1.0 Ah 4.5 V graphite (3.13 mAh cm-2)||LiNi0.8Mn0.1Co0.1O2 (2.85 mAh cm-2) pouch cells, delivering 0.87 Ah at −40 °C, surpassing commercial carbonate-based electrolytes, which fail to retain reversible capacity at this temperature. This study establishes fundamental principles for fast ion-transport electrolytes, paving the way for next-generation Li-ion batteries under extreme scenarios. Slow ion transport limits Li-ion battery performance under fast charging and low temperature. This work establishes an electrolyte design framework based on intermolecular interactions and molecule volume to reshape Li+ solvation structure, enabling Li-ion battery to operate stably at −50 °C and 6 C

</details>
<br>

**关键词**: lithium-ion battery, electrolyte design, solvation structure, ion transport kinetics, low-temperature performance, fast charging, dichloromethane electrolyte, extreme conditions

---

### 33. ❌ Biological traits predict species’ time-varying responses to multiple global change drivers

**作者**: Takehiro Sasaki, Yuki Iwachido, Orlando Lam-Gordillo, Katie M. Cook, Emily J. Douglas, Rebecca V. Gladstone-Gallagher, Barry L. Greenfield, Sarah F. Hailes, Kamryn Carter, Naohiro I. Ishii, Yoshiki Takayama, Shinji Shimode, Maiko Kagami, Judi E. Hewitt, Simon F. Thrush, Andrew M. Lohrer
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70606-w](https://doi.org/10.1038/s41467-026-70606-w)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是生态学领域，关注全球变化驱动因素对河口大型无脊椎动物物种动态的影响，使用非线性时间序列分析生物性状与环境响应之间的关系。所有评分关键词均涉及医学影像分析、人工智能医疗应用、手术规划等医学领域，与论文的生态学研究内容完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work uses nonlinear time series analysis of a multi-decadal, high-resolution dataset encompassing climate, freshwater, and sediment variables, alongside estuarine macroinvertebrate abundance to introduce a framework that links biological traits to long-term environmental responses, providing a predictive basis for trait-sensitivity relationships.

!!! tip deepseek-chat TL;DR

    该研究通过分析多年代河口生态数据，发现生物性状（如体型、移动性、寿命）能够预测物种对全球变化驱动因素（如气候变暖）的时变敏感性，为理解物种动态响应提供了预测框架。

<details open>
<summary>摘要翻译</summary>

> 全球变化的多种驱动因素正导致世界范围内生物多样性的快速丧失。然而，由于现实生态系统中生态响应具有动态和状态依赖的特性，预测物种的变化轨迹仍具挑战性。本研究利用非线性时间序列分析方法，对一套涵盖数十年、高分辨率的气候、淡水与沉积物变量以及河口大型底栖无脊椎动物丰度的数据集进行分析。我们的分析表明，包括体型大小、活动能力和寿命在内的关键生物性状，能够预测物种对特定环境驱动因素时变敏感性的均值与变异性。体型较小或活动能力较低的物种对气候变暖持续表现出负响应。物种敏感性的时间变异性——这一在以往物种环境响应研究中常被忽视的方面——与寿命密切相关，寿命较短的物种随时间波动更为剧烈。这些发现并不总是与受控实验室或短期野外实验的结果一致，凸显了物种在多种全球变化驱动因素作用下形成的复杂且状态依赖的响应特性。我们提出了一个将生物性状与长期环境响应相联系的框架，为性状-敏感性关系提供了预测基础。全球变化正在改变世界各地的生物多样性，但物种的响应随时间而变化且难以预测。本研究表明，关键生物性状能够预测河口大型底栖无脊椎动物如何响应多种全球变化驱动因素。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Multiple drivers of global change are causing rapid biodiversity loss worldwide. However, predicting species’ trajectories remains challenging due to the dynamic and state-dependent nature of ecological responses in real-world ecosystems. Here, we leverage nonlinear time series analysis of a multi-decadal, high-resolution dataset encompassing climate, freshwater, and sediment variables, alongside estuarine macroinvertebrate abundance. Our analysis shows that key biological traits, including body size, mobility, and lifespan predict the mean and variability of the time-varying sensitivity of species to specific environmental drivers. Species with smaller body sizes or lower mobility exhibit consistently negative responses to warming. The temporal variability of species sensitivity, an aspect often overlooked in previous studies of species’ environmental responses, is strongly associated with lifespan, with shorter-lived species showing greater fluctuations over time. These findings did not always align with results from controlled laboratory or short-term field experiments, highlighting the complex, state-dependent responses of species shaped by multiple drivers of global change. We introduce a framework that links biological traits to long-term environmental responses, providing a predictive basis for trait–sensitivity relationships. Global change is altering biodiversity worldwide, yet species’ responses vary over time and remain difficult to predict. This study shows that key biological traits predict how estuarine macroinvertebrates respond to multiple global change drivers.

</details>
<br>

**关键词**: global change drivers, biological traits, species sensitivity, time-varying responses, estuarine macroinvertebrates, nonlinear time series analysis, trait-sensitivity relationships, biodiversity prediction

---

### 34. ❌ Cell type-specific enhancers regulate IL-22 expression in innate and adaptive type 3 lymphoid cells

**作者**: Ankita Saini, Leone S. Hopkins, Vanida A. Serna, Matthew McCullen, Nicholas G Selner, Bishan Bhattarai, José Luís Fachi, Rebecca A. Glynn, Katharina E. Hayer, Craig H. Bassing, Marco Colonna, Eugene M. Oltz
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70636-4](https://doi.org/10.1038/s41467-026-70636-4)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文研究免疫学中IL-22细胞因子的转录调控机制，涉及增强子E22-1和E22-2在先天性和适应性3型淋巴细胞中的特异性功能，与感染（Citrobacter rodentium）和自身免疫疾病（银屑病）相关。所有评分关键词均聚焦于医学影像分析、人工智能辅助诊断、手术规划等临床决策支持技术，而本文完全属于基础免疫学研究，未涉及任何医学影像、AI模型、诊断预测或手术相关内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is concluded that Th17/22 and ILC3 cells use distinct cis-elements to differentially regulate IL-22 expression, while orchestrating homeostatic protection and pathogen defense in barrier tissues.

!!! tip deepseek-chat TL;DR

    该研究发现了两个增强子E22-1和E22-2，它们通过不同的转录调控机制特异性调节3型淋巴细胞中IL-22的表达，从而影响肠道感染防御和银屑病发病过程。

<details open>
<summary>摘要翻译</summary>

> IL-22是3型淋巴细胞（包括辅助性T细胞17/22（Th17/22）和3型固有淋巴细胞（ILC3））的特征性细胞因子，在屏障组织中介导上皮稳态及保护性病原体应答。一旦失调，IL-22可驱动慢性炎症性疾病，但调控其表达的转录元件尚不明确。本研究鉴定出两个增强子E22-1和E22-2，二者在3型淋巴细胞中具有不同的Il22表达调控能力。这两个增强子对于防御啮齿柠檬酸杆菌感染以及IL-22介导的银屑病发生均不可或缺。E22-2特异性参与ILC3中IL-22的表达调控，而E22-1同时在Th17/22和ILC3中发挥作用。E22-2的ILC3特异性归因于其存在多个Runx3结合位点且缺乏功能性RORγt基序。我们的结论是：Th17/22与ILC3细胞通过不同的顺式作用元件差异调控IL-22表达，从而协同维持屏障组织的稳态保护与病原体防御功能。在健康的屏障组织中，3型淋巴细胞通过表达IL-22维持保护性免疫平衡，而IL-22失调则导致疾病发生。本研究将E22-1和E22-2鉴定为在健康与疾病状态下调控IL-22表达的增强子，其中E22-2特异性调控ILC3中的IL-22表达。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> IL-22, a signature cytokine for type 3 lymphoid cells, including T helper 17/22 (Th17/22) and type 3 innate lymphoid cells (ILC3), mediates epithelial homeostasis and protective pathogen responses in barrier tissues. Upon dysregulation, IL-22 can drive chronic inflammatory diseases, yet little is known about transcriptional elements modulating its expression. Here, we identify two enhancers, E22-1 and E22-2, with distinct capacities for regulating Il22 expression in type 3 lymphoid cells. Both enhancers are necessary for protection from Citrobacter rodentium infection and for the onset of IL-22-mediated psoriasis. E22-2 is specifically required for IL-22 expression in ILC3s, while E22-1 functions in both Th17/22 and ILC3. The ILC3 specificity of E22-2 is attributed to the presence of multiple Runx3 sites and the lack of a functional RORγt motif. We conclude that Th17/22 and ILC3 cells use distinct cis-elements to differentially regulate IL-22 expression, while orchestrating homeostatic protection and pathogen defense in barrier tissues. In healthy barrier tissues, type 3 lymphoid cells express IL-22 to maintain a protective immune balance, while IL-22 dysregulation contributes to disease. Here, the authors identify E22-1 and E22-2 as enhancers regulating IL-22 expression in health and disease; with E22-2 being restricted to IL-22 regulation in ILC3s.

</details>
<br>

**关键词**: IL-22, type 3 lymphoid cells, enhancers, transcriptional regulation, Citrobacter rodentium infection, psoriasis, ILC3, Th17/22

---

### 35. ❌ Comparison of state-of-the-art error-correction coding for sequence-based DNA data storage

**作者**: Andreas L. Gimpel, Alex Remschak, Wendelin J. Stark, Reinhard Heckel, Robert N. Grass
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70548-3](https://doi.org/10.1038/s41467-026-70548-3)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究DNA数据存储中的纠错编码技术，涉及生物信息学、数据存储和编码理论，与医学影像分析、深度学习医疗影像、AI诊断、预后预测、手术规划、多模态医疗影像、医疗影像基础模型等关键词完全无关。论文未涉及任何医学影像、临床决策支持或医疗AI相关内容。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This study demonstrates the maturity of error-correction coding, defines its current state-of-the-art, and establishes best practices for codec benchmarking.

!!! tip deepseek-chat TL;DR

    该论文通过实验比较了六种DNA数据存储纠错编码的性能，发现现有编码技术可实现高达117 EB/g的存储密度，并验证了43 EB/g和13 EB/g的实际存储能力。

<details open>
<summary>摘要翻译</summary>

> 摘要 迄今为止，DNA数据存储领域已实现了多种采用不同纠错方法的编解码器。然而，尚无研究系统性地对这些编解码器的实现进行基准测试，以确立其当前的最先进水平。本研究通过计算机模拟与体外实验，比较了文献中六种代表性编解码器的性能。在独立测试中，这些编解码器可容忍高达14%的错误率和65%的序列丢失。在现实条件下，我们进一步证实，利用现有编解码器及当前的合成与测序技术，存储密度高达117 EB g −1 是可行的。通过实验验证，我们使用材料沉积合成法实现了43 EB g −1 的数据存储密度，并利用电化学合成法实现了13 EB g −1 的数据存储密度，二者均采用了文献中的现有编解码器。本研究不仅逼近了DNA数据存储的物理极限，还展示了纠错编码技术的成熟度，定义了其当前的最先进水平，并为编解码器的基准测试确立了最佳实践。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Many codecs with different error-correction approaches have been implemented for DNA data storage to date. However, no studies have systematically benchmarked codec implementations to establish their current state-of-the-art. Here, we use in silico and in vitro experiments to compare the performance of six representative codecs from literature. In isolation, these codecs can tolerate error rates up to 14% and a sequence loss of 65%. Under realistic conditions, we further establish that storage densities as high as 117 EB g −1 are feasible using existing codecs and current synthesis and sequencing technologies. Verifying our results experimentally, we demonstrate data storage at 43 EB g −1 using synthesis by material deposition and 13 EB g −1 using electrochemical synthesis, employing existing codecs from literature. Besides closing in on the physical limits of DNA data storage, this study thus demonstrates the maturity of error-correction coding, defines its current state-of-the-art, and establishes best practices for codec benchmarking.

</details>
<br>

**关键词**: DNA data storage, error-correction coding, codec benchmarking, storage density, synthesis technologies, sequencing technologies, in silico experiments, in vitro experiments

---

### 36. ❌ Complex marine ecological response during the Eocene-Oligocene revealed by global foraminiferal record

**作者**: Zhengbo Lu, Ke Xue, Yiying Deng, Junxuan Fan, Peiyue Fang, Bridget S. Wade, Laia Alegret, Michael J. Benton, Yuchang Wu, Chao Qian, XuDong Hou, Yukun Shi, Peter M. Sadler, Huiqing Xu, Zhi-Hua Zhou, Shuzhong Shen
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70541-w](https://doi.org/10.1038/s41467-026-70541-w)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究古生物学和地球科学，使用AI算法分析有孔虫化石记录，以重建始新世-渐新世过渡期的全球物种丰富度历史。所有评分关键词均涉及医学影像分析和临床决策支持，与论文主题完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究使用人工智能算法分析高分辨率全球有孔虫化石记录，揭示了始新世-渐新世过渡期海洋生物多样性的复杂生态响应模式，表明不同生态群对有孔虫对气候变化的反应存在显著差异。

<details open>
<summary>摘要翻译</summary>

> 摘要  始新世-渐新世过渡期是地球气候转向当前冰室状态的关键转折点。目前对海洋生物圈在此过渡期间如何响应的认识尚不明确，在低时间分辨率的全球汇编资料中，其仅呈现为一次简单的灭绝脉冲。本研究设计了一种受人工智能启发的元启发式算法，利用丰富的有孔虫化石记录，以推算出的约29,000年分辨率，构建了跨越始新世-渐新世过渡期的高分辨率全球物种丰富度历史。所揭示的多样性动态十分复杂，且生态特征各异的各类有孔虫群组均表现出不同模式。浮游有孔虫和浅水大型底栖有孔虫在经历了长期减少后，于晚始新世过渡早期阶段呈现出稳定的多样性水平；而深水小型底栖有孔虫在同一时期显著辐射演化，随后衰退。在早渐新世初期，随着南极洲首次形成大陆规模的冰盖，浮游有孔虫和大型有孔虫遭遇了重大的物种损失，而小型底栖有孔虫的多样性保持稳定，随后随着早渐新世的推进加速下降。这些发现揭示了复杂且具有生态分异的环境-生命过程，表明高分辨率时间数据对于解析生物对重大环境变化的生态响应至关重要。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract The Eocene–Oligocene transition was the crucial turning point when Earth’s climate shifted to its current icehouse state. Understanding how the marine biosphere responded during this transition is not well-constrained, appearing as a simple extinction pulse in low temporal resolution global compendia. Here we design an artificial-intelligence-inspired metaheuristics algorithm to construct a high-resolution global species richness history across the Eocene–Oligocene transition for the rich foraminifera fossil record with an imputed ~29,000-year resolution. The revealed diversity dynamics are complex and differ for each foraminiferal group with distinct ecology. Planktonic and shallow-water larger benthic foraminifera show steady diversity levels in the early phases of the transition in the latest Eocene after a long-term reduction, while the deeper-water small benthic foraminifera radiate notably and then decline over the same interval. In the earliest Oligocene, the planktonic and larger foraminifera suffer major species losses coincident with the first continental-scale ice sheet formed on Antarctica, while small benthic foraminifera diversity holds steady, followed by an accelerating lowering as the early Oligocene proceeds. These findings reveal complicated and ecologically differentiated environment-life processes, indicating the importance of high-resolution temporal data for dissecting out ecological responses to major environmental changes.

</details>
<br>

**关键词**: Eocene-Oligocene transition, foraminifera, species richness, artificial intelligence algorithm, marine biosphere response, high-resolution temporal data, ecological differentiation, climate change

---

### 37. ❌ Global literature review and survey of implementation constraints on natural climate solutions

**作者**: Timm Kroeger, James T. Erbaugh, Zhixian Luo, Hilary Brumberg, Waverly Eichhorst, Margaret Hegwood, Anna LoPresti, Priya Shyamsundar, Peter W. Ellis, Lauren E. Oakes, Dow Martin, Pedro H. S. Brancalion, Mieke Bourne, Arundhati Jagadish, Kemen Austin, Andrew Kinzer, Marcos Sanjuán, Lisa McCullough, Marta Echavarria
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70482-4](https://doi.org/10.1038/s41467-026-70482-4)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是自然气候解决方案（Natural Climate Solutions）的实施约束，属于环境科学、气候变化和政策研究领域，与医学影像分析、人工智能临床决策支持等医疗领域完全无关。论文内容涉及全球调查、约束映射、政策协调等，没有任何医学影像、深度学习、疾病诊断、手术规划或医疗数据融合的内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过全球调查和文献综述，识别了自然气候解决方案实施中的46种约束，发现社会行为、知识和政府组织是最常见的约束类别，缺乏政策协调或实施能力是最主要的障碍，导致其减缓潜力远未充分发挥。

<details open>
<summary>摘要翻译</summary>

> 摘要：自然气候解决方案——即通过对土地和水域进行保护、恢复和改善管理以减少温室气体排放——具有巨大的气候变化减缓潜力。然而，由于缺乏关于实施挑战的全面信息，阻碍了自然气候解决方案的采纳以及近期减缓目标的实现。通过一项针对自然气候解决方案项目的全球调查以及对近期研究的系统性综述，我们绘制了涵盖八大类别的46项制约因素，从137个国家（覆盖联合国22个分区中的20个）的501项研究和项目中，获得了15,572条具有地理参照的路径-制约观测数据。社会行为类、知识类以及政府组织类是最常被报告的制约类别，而缺乏政策协调或实施能力是最常被观测到的制约因素，也是各实施路径和分区中最频繁位列首位的制约因素。尽管存在广泛的共性，但首要制约因素及类别的排序在不同分区和不同实施路径中分别存在差异。我们发现，项目通常面临多样化的挑战组合。若缺乏赋能性支持措施，自然气候解决方案在近期的减缓成效可能远低于其生物物理潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Natural Climate Solutions – protection, restoration, and improved management of lands and waters that reduce greenhouse gasses – have large climate change mitigation potential. However, lack of comprehensive information on implementation challenges hinders the adoption of Natural Climate Solutions and the delivery of near-term mitigation. Using a global survey of Natural Climate Solutions projects and a systematic review of recent studies, we map 46 constraints in eight categories, yielding 15,572 geo-referenced pathway-constraint observations from 501 studies and projects in 137 countries covering 20 of 22 United Nations subregions. Social-behavioral, Knowledge, and Government-Organizational are the most-reported constraint categories, and lack of policy coordination or implementation capacity the most-observed constraint and most frequently top-ranking constraint for pathways and subregions. Despite broad congruence, top constraint and category rankings vary among subregions and pathways, respectively. We find that projects generally encounter diverse sets of challenges. Without enabling efforts, near-term mitigation from Natural Climate Solutions may remain well below its biophysical potential.

</details>
<br>

**关键词**: Natural Climate Solutions, implementation constraints, climate change mitigation, global survey, policy coordination, restoration, greenhouse gas reduction, land management

---

### 38. ❌ Synergistic surface modification of Cu with schiff-base networks for high selectivity and durability in CO2-to-C2H4 electroreduction

**作者**: Wangjing Xie, Tingting Tian, Shengnan Yue, Hualong Gu, Ningning Shi, Dechao Chen, C. S. Praveen, Xing Tao Huang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70595-w](https://doi.org/10.1038/s41467-026-70595-w)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确表明该研究属于电化学催化领域，专注于铜表面改性用于二氧化碳电还原制乙烯，完全不涉及医学图像分析、人工智能诊断、手术规划或任何医疗相关主题。所有关键词均与论文内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过席夫碱网络协同改性铜表面，实现了二氧化碳电还原制乙烯的高选择性和耐久性。

**关键词**: CO2 electroreduction, ethylene production, copper surface modification, Schiff-base networks, electrocatalysis, selectivity, durability, C2H4

---

### 39. ❌ Ferroelectricity-modulated asymmetric van der Waals heterostructure for ultralow-power neuromorphic synapse and logic-in-memory operations

**作者**: Jiake Zhi, Yao Wen, Jiajie Chen, Chuanyang Cai, Shoufeng Yang, Hao Zhu, Ruiqing Cheng, Lei Yin, Shiheng Liang, Jun He
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70668-w](https://doi.org/10.1038/s41467-026-70668-w)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是基于铁电调制非对称范德华异质结构的超低功耗神经形态突触和存内逻辑运算，属于纳米电子学、神经形态计算和材料科学领域。论文内容完全不涉及医学图像分析、临床决策支持、疾病诊断、手术规划或任何医疗应用，与所有评分关键词均无关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了利用铁电调制非对称范德华异质结构实现超低功耗神经形态突触和存内逻辑运算，为下一代神经形态计算硬件提供了新材料方案。

**关键词**: ferroelectricity, van der Waals heterostructure, neuromorphic synapse, logic-in-memory, ultralow-power, asymmetric structure, neuromorphic computing

---

### 40. ❌ Chlorine radical-mediated electrochemical propylene epoxidation from seawater

**作者**: Ming Cheng, Xiaoxian Sun, Peng Zhang, Ailijiang Tuerdi, Zhaoling Li, Shijie Xiong, Jintong Lan, Xiao Liu, Jinlong Gong
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70733-4](https://doi.org/10.1038/s41467-026-70733-4)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究是关于电化学催化海水中的丙烯环氧化反应，属于化学工程、电化学和催化领域，与医学图像分析、人工智能、临床决策支持等医疗AI主题完全无关。所有评分关键词均涉及医疗AI技术，而论文研究的是化工过程，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种氯自由基介导的电化学方法，利用海水中的氯离子高效催化丙烯环氧化生成环氧丙烷，实现了高选择性和电流效率。

**关键词**: electrochemical catalysis, propylene epoxidation, seawater utilization, chlorine radicals, epoxypropane production, electrocatalytic synthesis, chloride oxidation

---

### 41. ❌ Decoding correlated errors in quantum LDPC codes

**作者**: Arshpreet Singh Maan, Francisco Miguel Garcia Herrero, Alexandru Paler, Valentin Savin
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**arXiv链接**: [https://arxiv.org/abs/2510.14060](https://arxiv.org/abs/2510.14060)
**DOI**: [10.1038/s41467-026-70556-3](https://doi.org/10.1038/s41467-026-70556-3)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题为'Decoding correlated errors in quantum LDPC codes'，摘要内容未提供，但从标题可明确判断该论文研究量子纠错码中的相关错误解码问题，属于量子计算和编码理论领域，与医学图像分析、人工智能临床决策支持等所有给定关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This approach is a graph augmentation and rewiring for inference (GARI) method, which modifies the correlated detector error model by eliminating 4-cycles involving Y-type errors, while preserving the equivalence of the decoding problem.

!!! tip deepseek-chat TL;DR

    该论文研究量子低密度奇偶校验码中相关错误的解码问题，提出了改进的解码方法以提升量子纠错性能。

**关键词**: quantum LDPC codes, correlated errors, decoding, quantum error correction, coding theory, quantum computing

---

### 42. ❌ Molecular mechanism underlying regulation of chalcone synthase by chalcone isomerase-like protein

**作者**: Song Wang, Li-Ying Ma, Zhou-Geng Xu, Riga Wu, Ji-Ping Qu, Jie Hao, Chen-Jing Hu, Zhiyu Chen, Miaolian Ma, Wenyi Zhang, Tengyu Xie, Jing-Jing Xu, Mu-Lan Zhu, Ai-Xia Cheng, Peng Zhang, Jia-Wei Wang, Fang Yu, Jianxu Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70563-4](https://doi.org/10.1038/s41467-026-70563-4)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是植物分子生物学中查尔酮合酶（chalcone synthase）的调控机制，涉及蛋白质相互作用和基因表达调控，与医学影像分析、深度学习、AI诊断、手术规划等医疗AI领域完全无关。所有关键词均未在标题或摘要中出现，相关度为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The crystal structure of the CHS-CHIL complex is reported, revealing that CHIL modulates CHS function by gating the substrate-binding pocket entrance through its β-hairpin region, establishing a conserved binding-conformational regulation paradigm that governs metabolic flux into the flavonoid biosynthetic pathway and provides practical strategies for enhancing flavonoid production and composition in crops.

!!! tip deepseek-chat TL;DR

    该研究揭示了查尔酮异构酶样蛋白（chalcone isomerase-like protein）通过蛋白质相互作用调控查尔酮合酶（chalcone synthase）活性的分子机制。

**关键词**: chalcone synthase, chalcone isomerase-like protein, molecular mechanism, protein interaction, gene regulation, plant biology, enzyme activity

---

### 43. ❌ Turn-on luminescence from molecular rotor realignment in metal-organic framework thin films

**作者**: Jan C. Fischer, Tong Zhou, Philipp Sievers, Nils W. Rosemann, Elizabeth Coetsee, Dmitry Busko, Yang Li, Honghan Ji, Diethelm Johannsmann, Lingju Guo, Pengfei Duan, Bryce S. Richards, Ian A. Howard, Tonghan Zhao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70551-8](https://doi.org/10.1038/s41467-026-70551-8)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究金属有机框架薄膜中分子转子重排引发的发光增强现象，属于材料科学、化学物理和传感器领域。所有评分关键词均涉及医学影像分析和人工智能临床决策支持，与论文的化学材料、光物理传感研究内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了金属有机框架薄膜中庞大连接体受控旋转的挑战，发现溶剂蒸发产生的内部应力能使连接体发色团重新排列，从而产生50倍的发光增强，为实时监测溶剂挥发的纳米级传感平台奠定了基础。

<details open>
<summary>摘要翻译</summary>

> 金属有机框架（MOF）中亚单元的运动为纳米尺度传感提供了独特机遇。然而，实现大体积连接体的可控部分旋转仍是一项重大挑战。本研究中，当孔内溶剂流动使连接体发色团定向排列时，MOF薄膜的发光强度增强了50倍。此类MOF薄膜可通过简易的滴涂法在各种基底上制备。该MOF结构由含可旋转发色团的锌配位层构成，各层之间通过柱状分子分隔。掠入射广角X射线散射分析证实了高度取向薄膜的形成。当挥发性有机化合物（如乙醇）沉积后，随着溶剂接近完全蒸发，其发光强度显著增强。光物理表征与石英晶体微天平测量表明，该现象由蒸发最后阶段MOF孔道尺度产生的内部应力驱动。这种应力可在分子尺度上导致MOF发色团的重新排列。因此，这种动态开启型发光行为为能够实时指示溶剂挥发的纳米级平台奠定了基础。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Sub-unit motion within metal-organic frameworks (MOFs) offers unique opportunities for nanoscale sensing. However, achieving controlled partial rotation of bulky linkers remains a significant challenge. In this study, a 50-fold luminescence enhancement is observed from a MOF thin film when intra-pore solvent flow orients the linker chromophores. These MOF thin films can be prepared via a facile drop-casting method on various substrates. The MOFs structure consists of zinc-coordinated layers containing rotatable chromophores, separated by pillar molecules. Grazing-incidence wide-angle X-ray scattering analysis confirms the formation of highly oriented films. The deposition of a volatile organic compound, such as ethanol, triggers a significant enhancement in luminescence as the solvent nears complete evaporation. Photophysical characterization and quartz crystal microbalance measurements reveal that this phenomenon is driven by internal stress on the MOF’s pore level generated during the final stages of evaporation. This stress can result in a realignment of the MOF chromophores at the molecular scale. Consequently, this dynamic turn-on luminescence behavior establishes a foundation for nanoscale platforms capable of indicating solvent volatilization in real time.

</details>
<br>

**关键词**: metal-organic frameworks, luminescence enhancement, molecular rotor realignment, thin films, solvent evaporation sensing, chromophore orientation, internal stress, nanoscale sensing

---

### 44. ❌ AcrIIA7 hijacks tracrRNA to block CRISPR-Cas system

**作者**: So Yeon Lee, Hyun Ho Park
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70749-w](https://doi.org/10.1038/s41467-026-70749-w)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是CRISPR-Cas9系统的抑制机制，具体探讨了AcrIIA7蛋白如何通过劫持tracrRNA来阻断Cas9功能。该研究属于分子生物学、结构生物学和基因编辑领域，与医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或医学影像基础模型等主题完全无关。所有关键词均与论文内容无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    These findings provide the first structural insight into tracrRNA-targeted anti-CRISPR activity and highlight RNA-RNA interaction interfaces as vulnerable nodes in CRISPR-Cas immunity.

!!! tip deepseek-chat TL;DR

    该研究揭示了AcrIIA7蛋白通过特异性结合并劫持tracrRNA，阻止其与crRNA配对，从而抑制Cas9核糖核蛋白复合物形成和CRISPR-Cas9系统功能的分子机制。

<details open>
<summary>摘要翻译</summary>

> CRISPR–Cas9系统通过一种双RNA引导的DNA切割机制，为宿主提供针对外源遗传元件的适应性免疫。该系统的功能依赖于由Cas9核酸内切酶、CRISPR来源的RNA（crRNA）及反式激活CRISPR RNA（tracrRNA）共同组成的核糖核蛋白（RNP）复合物的精确组装。目前已有约100种能够抑制CRISPR–Cas系统的抗CRISPR蛋白被发现，其作用机制正逐步被阐明。然而，包括AcrIIA7在内的许多抗CRISPR蛋白的抑制机制仍不清楚。本研究解析了AcrIIA7的结构，并揭示了一种此前未知的Cas9抑制机制。结构分析与生化实验表明，AcrIIA7特异性结合tracrRNA，阻止其与crRNA结合，从而阻断有活性的Cas9 RNP复合物的形成。这种“劫持tracrRNA”的机制代表了一种独特的CRISPR抑制策略：抗CRISPR蛋白靶向Cas9激活所必需的RNA支架，而非直接与Cas9蛋白相互作用。我们的研究首次从结构层面揭示了靶向tracrRNA的抗CRISPR活性，并指出RNA–RNA相互作用界面是CRISPR–Cas免疫系统中的脆弱节点。CRISPR–Cas9免疫依赖于形成Cas9–crRNA–tracrRNA核糖核蛋白复合物。本研究表明，AcrIIA7通过结合tracrRNA并阻碍其与crRNA配对，从而阻断这一过程。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The CRISPR–Cas9 system provides adaptive immunity against invading genetic elements through a dual-RNA-guided DNA cleavage mechanism. This system relies on the precise assembly of a ribonucleoprotein (RNP) complex composed of the Cas9 endonuclease, a CRISPR-derived RNA (crRNA), and a trans-activating CRISPR RNA (tracrRNA). Around 100 anti-CRISPR proteins that inhibit CRISPR–Cas systems have been identified, and the mechanisms by which they act are increasingly being elucidated. However, the inhibitory mechanisms of many Acrs, including AcrIIA7, remain poorly understood. Here, we present the structure of AcrIIA7 and uncover a previously unrecognized mechanism by which it inhibits Cas9 function. Structural and biochemical analyses reveal that AcrIIA7 specifically binds to tracrRNA, preventing its association with crRNA and thereby blocking formation of the active Cas9 RNP complex. This tracrRNA hijacking mechanism represents a unique strategy for CRISPR inhibition, in which an anti-CRISPR protein targets an RNA scaffold essential for Cas9 activation rather than interacting directly with the Cas9 protein. Our findings provide the first structural insight into tracrRNA-targeted anti-CRISPR activity and highlight RNA–RNA interaction interfaces as vulnerable nodes in CRISPR–Cas immunity. CRISPR–Cas9 immunity relies on forming a Cas9–crRNA–tracrRNA ribonucleoprotein complex. Here, the authors show that AcrIIA7 blocks this process by binding tracrRNA, preventing its pairing with crRNA.

</details>
<br>

**关键词**: CRISPR-Cas9, AcrIIA7, tracrRNA, anti-CRISPR, ribonucleoprotein complex, RNA hijacking, Cas9 inhibition, structural biology

---

### 45. ❌ Prefusion-stabilized Hantaan virus glycoprotein nucleic acid vaccine elicits potent neutralizing antibody responses via germinal center activation

**作者**: Wei Ye, Yamei Dang, Yuan Wang, Qiqi Yang, Hui Zhang, Chuantao Ye, Jing Wei, Jiawei Pei, Xuemin Pei, Du Jiang, Xiaojing Yang, Xiaolei Jin, Hongwei Ma, He Liu, Liang Zhang, Linfeng Cheng, Yangchao Dong, Yingfeng Lei, Zhikai Xu, Yun Zhang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70285-7](https://doi.org/10.1038/s41467-026-70285-7)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是汉坦病毒疫苗开发，属于病毒学/免疫学领域，涉及核酸疫苗、中和抗体、生发中心激活等主题。所有评分关键词均与医学影像分析、人工智能、诊断、预后、手术规划等相关，而论文完全不涉及医学影像、AI技术或临床决策支持系统。论文内容与评分关键词领域完全不同，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Preference-stabilized glycoprotein-based nucleic acid vaccines expressing a prefusion-stabilized HTNV glycoprotein mRNA-LNP are promising candidates for advanced orthohantavirus vaccine development.

!!! tip deepseek-chat TL;DR

    该研究评估了表达预融合稳定汉坦病毒糖蛋白的核酸疫苗在小鼠中的免疫效果，发现DNA和mRNA-LNP版本均能通过强烈激活生发中心引发强效中和抗体反应，并保护小鼠免受高剂量病毒攻击，其中mRNA-LNP疫苗在异源加强免疫中表现最优。

<details open>
<summary>摘要翻译</summary>

> 摘要：旧世界正汉坦病毒（包括汉坦病毒，HTNV）在欧亚大陆引起肾综合征出血热（HFRS）。现有的灭活疫苗常诱导较低水平的中和抗体且保护期短。我们在雌性BALB/c小鼠中评估了表达预融合稳定化HTNV糖蛋白的核酸疫苗。无论是DNA版本还是mRNA-LNP（脂质纳米颗粒递送的mRNA）版本，均通过强烈激活生发中心，诱发了强效的中和抗体，保护小鼠抵御高剂量HTNV攻击。我们进一步测试了异源初免-加强免疫方案，即用灭活疫苗完成初次免疫的小鼠接受不同加强针。所有加强针均提高了中和抗体滴度，但只有预融合稳定化糖蛋白mRNA-LNP疫苗能将滴度提升至其自身完整初次免疫程序所达到的水平。这证明了该免疫原在开发下一代疫苗方面的优越性，及其独特能力：能有效召回由次优灭活疫苗诱导的记忆B细胞。因此，基于预融合稳定化糖蛋白的核酸疫苗是开发先进正汉坦病毒疫苗的有力候选策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Old World orthohantaviruses , including Hantaan virus (HTNV), cause hemorrhagic fever with renal syndrome (HFRS) in Eurasia. Available inactivated vaccines often induce low neutralizing antibodies and short-term protection. We evaluated nucleic acid vaccines expressing a prefusion-stabilized HTNV glycoprotein in female BALB/c mice. Both DNA and mRNA-LNP versions elicited robust neutralizing antibodies by strongly activating germinal centers, which protected mice against high-dose HTNV challenge. We further tested heterologous prime-boost regimens, where mice primed with inactivated vaccine received different boosters. All boosters increased neutralizing titers, but only the prefusion-stabilized glycoprotein mRNA-LNP vaccine raised titers to the level achieved by its own full primary vaccination course. This demonstrates the immunogen’s superiority in developing next-generation vaccines and its unique ability to potently recall memory B cells induced by suboptimal inactivated vaccines. Thus, prefusion-stabilized glycoprotein-based nucleic acid vaccines are promising candidates for advanced orthohantavirus vaccine development.

</details>
<br>

**关键词**: Hantaan virus, nucleic acid vaccine, prefusion-stabilized glycoprotein, neutralizing antibodies, germinal center activation, heterologous prime-boost, mRNA-LNP vaccine, orthohantavirus vaccine development

---

### 46. ❌ Experimental mechanician for plate lattice metamaterial discovery

**作者**: Songtao Hu, Haoran Li, Wei Lü, Tian Xie, Xijia Ding, Xiantong Zhang, Xi Shi, Zhike Peng, Xiaobao Cao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70675-x](https://doi.org/10.1038/s41467-026-70675-x)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是机械超材料（板格点阵）的优化发现，涉及机器人平台、多目标主动学习和机器学习框架，用于识别轻质高强度的结构。所有评分关键词均与医学影像分析、AI临床决策支持相关，而论文完全不涉及医学、医疗影像、疾病诊断或手术规划，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一个集成机器人平台和机器学习框架的自优化实验系统（ExMech），用于自动发现轻质高强度的板格点阵超材料，在压缩和剪切屈服强度方面实现了显著提升。

<details open>
<summary>摘要翻译</summary>

> 板格超材料相较于传统桁架格栅具有更高的强度-重量比效率。然而，当设计参数增多且目标多元时，其优化过程极具挑战性。本文提出一种实验力学智能系统（ExMech），用于识别轻质高强的板格结构。ExMech集成了用于标准化数据生成的机器人平台，以及一个用于引导探索结构-性能关系的多目标主动学习框架。该系统在三个变量、三个目标的空间中对板-桁架混合格栅进行优化，仅通过25次迭代便确立了帕累托前沿，显著减少了实验工作量。帕累托最优组合在保持轻量化指标不变的前提下，其压缩屈服强度和剪切屈服强度分别提升了15.6%和12.0%。当优先考虑强度时，该系统实现了158.5%和194.8%的性能提升，同时重量仅增加13.2%。通过分析变量-目标关系与失效模式，我们能够识别出结构效率更高的组合。所发现的格栅结构在可调压缩-剪切性能的3D打印鞋垫中得到了验证。本研究展示了一种用于板格结构发现的自优化实验方法，加速了新型力学超材料的研发。作者设计了一套自优化实验系统，通过集成机器人平台与机器学习框架，实现了轻质高强板格超材料的自动发现。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Plate lattice metamaterials offer higher strength-to-weight efficiency than traditional truss lattices. Their optimization, however, is challenging when having more parameters and multiple objectives. Here, we present an experimental mechanician (ExMech) to identify lightweight and high-strength plate lattices. ExMech integrates a robotic platform for standardized data generation and a multi-objective active learning framework for guided exploration of structure–property relationships. It optimizes plate–truss hybrid lattices in a three-variable, three-objective space. It establishes the Pareto front in 25 iterations, reducing experimental workload significantly. Pareto-optimal combinations show 15.6% and 12.0% improvements in compressive and shear yield strength respectively without compromising lightweight metrics. When prioritizing strength, it yields 158.5% and 194.8% improvements with a 13.2% increase in weight. By analyzing variable-objective relationships and failure patterns, we could identify more structurally efficient combinations. The discovered lattices are demonstrated in compression–shear tunable 3D-printed midsoles. This study illustrates a self-optimizing experimentation approach for plate lattice discovery, accelerating the discovery of new mechanical metamaterials. Here, the authors design a self-optimizing experimental system for the automatic discovery of lightweight and high‑strength plate‑lattice metamaterials, integrating a robotic platform with a machine learning framework.

</details>
<br>

**关键词**: plate lattice metamaterials, multi-objective active learning, robotic platform, structure-property relationships, lightweight high-strength, mechanical metamaterials, self-optimizing experimentation, 3D-printed midsoles

---

### 47. ❌ Optimizing global genomic surveillance for early detection of emerging SARS-CoV-2 variants

**作者**: Haogao Gu, Jifan Li, Wanying Sun, Mengting Li, Kathy Leung, Joseph T. Wu, Hsiang-Yu Yuan, Maggie H. Wang, Bingyi Yang, Matthew R. McKay, Ning Ning, Leo L. M. Poon
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70664-0](https://doi.org/10.1038/s41467-026-70664-0)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究专注于全球基因组监测、SARS-CoV-2变异株的早期检测和基因组数据分析，属于生物信息学、流行病学和病毒基因组学领域。研究内容涉及基因组序列分析、监测策略优化和公共卫生应用，与医学影像分析、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像以及医学影像基础模型等关键词完全无关。所有关键词均未在论文内容中体现，因此相关度评分为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A multiple-strain metapopulation model of global SARS-CoV-2 transmission is developed and calibrate using extensive epidemiological, phylogenetic, and high-resolution air travel data to provide a quantitative framework for strengthening global genomic surveillance through targeted, complementary strategies that preserve local capacity while improving preparedness for future pandemics.

!!! tip deepseek-chat TL;DR

    该研究通过优化全球基因组监测策略，实现了对新兴SARS-CoV-2变异株的早期检测，并提出了改进监测效率的方法。

**关键词**: genomic surveillance, SARS-CoV-2 variants, early detection, genome sequencing, public health, epidemiology, bioinformatics

---

### 48. ❌ Single-cell and spatial profiling reveal cDC2A-CXCL13+CD8+ T-epithelial cell crosstalk and cytotoxicity through TNFRSF9 in cutaneous and mucosal lichen planus

**作者**: Rundong Jiang, Rachael Bogle, Xianying Xing, Joseph Kirma, Jennifer Fox, Paul W. Harms, Tran Do, Allison C. Billi, J. Michelle Kahlenberg, R. Modlin, Rosane M. B. Teles, Julie West, Aaron R. Mangold, H. Zhang, Martin A. Schneider, Sandro Bruno, Ben Roediger, Georg Martiny-Baron, Lam C. Tsoi, Feriel Hacini-Rachinel
**期刊/来源**: nature_communications
**发布日期**: 2026-03-14
**DOI**: [10.1038/s41467-026-70506-z](https://doi.org/10.1038/s41467-026-70506-z)

**评分**: 0.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 0.0/10 | 0.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是扁平苔藓的免疫微环境，使用单细胞RNA测序、空间转录组学和蛋白质组学等分子生物学技术，聚焦于免疫细胞相互作用和分子机制。所有评分关键词均涉及医学影像分析、AI诊断、手术规划等计算机视觉和人工智能在医疗影像中的应用领域，而本文完全不涉及任何医学影像处理、AI模型开发或影像数据分析内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A critical role is revealed for cDC2A in driving CXCL13+CD8+ T-epithelial cytotoxicity in cutaneous and mucosal LP through TNFRSF9, which enhances their cytotoxic responses in the skin.

!!! tip deepseek-chat TL;DR

    该研究通过单细胞和空间多组学分析揭示了在皮肤和黏膜扁平苔藓中，cDC2A细胞通过分泌IL-15驱动CXCL13+CD8+ T细胞上调TNFRSF9表达，从而增强上皮细胞毒性的关键免疫机制。

<details open>
<summary>摘要翻译</summary>

> 扁平苔藓（Lichen planus, LP）是一种皮肤与黏膜的慢性炎症性疾病，以T细胞浸润和角质形成细胞凋亡为特征，但其免疫微环境仍不甚明确。通过对28例患者及18例健康对照样本进行单细胞RNA测序、空间转录组学和蛋白质组学分析，我们发现皮肤与黏膜LP中CXCL13+CD8+ T细胞的干扰素（IFN）及细胞毒性特征均显著升高，而毛发扁平苔藓中则未出现此现象。表达TNF与IFNG的T细胞通过配体-受体相互作用在空间上与上皮细胞紧密关联，并与炎症程度相关。我们鉴定出cDC2A细胞是关键驱动因素，其邻近CXCL13+CD8+ T细胞分布，是IL-15的主要来源。CXCL13+CD8+ T细胞表达TNFRSF9（4-1BB），该分子可增强其在皮肤中的细胞毒性反应。总之，我们的数据揭示了cDC2A细胞通过TNFRSF9驱动皮肤与黏膜LP中CXCL13+CD8+ T–上皮细胞毒性作用的关键机制。扁平苔藓的免疫微环境尚未被充分认识。通过分析患者与健康对照样本的转录组学与蛋白质组学数据，本研究表明cDC2A分泌的IL-15介导CXCL13+CD8+ T细胞上调TNFRSF9表达，进而促进皮肤与黏膜LP的上皮细胞毒性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Lichen planus (LP) is a chronic inflammatory disease of the skin and mucous membranes, marked by T cell infiltration and keratinocyte apoptosis. However, its immune microenvironment remains poorly understood. Using single-cell RNA sequencing, spatial transcriptomics, and proteomics on samples from 28 patients and 18 healthy controls, we identify elevated interferon (IFN) and cytotoxic signatures in CXCL13+CD8+ T cells in both cutaneous and mucosal LP, but not in lichen planopilaris. T cells expressing TNF and IFNG are spatially linked to epithelial cells through ligand-receptor interactions, correlating with inflammation. We identify cDC2A cells as key contributors, proximal to CXCL13+CD8+ T cells, serving as a major source of IL-15. CXCL13+CD8+ T cells express TNFRSF9 (4-1BB), which enhances their cytotoxic responses in the skin. In summary, our data reveal a critical role for cDC2A in driving CXCL13+CD8+ T–epithelial cytotoxicity in cutaneous and mucosal LP through TNFRSF9. The immune microenvironment of lichen planus remains poorly understood. By analyzing transcriptomics and proteomics data on samples from patients and healthy controls, the authors here show that cDC2A secreted IL-15 mediates CXCL13+CD8+ T to upregulate TNFRSF9 expression which contributes to epithelial cytotoxicity in cutaneous and mucosal LP.

</details>
<br>

**关键词**: lichen planus, single-cell RNA sequencing, spatial transcriptomics, CXCL13+CD8+ T cells, cDC2A cells, TNFRSF9, epithelial cytotoxicity, immune microenvironment

---

## Token 消耗统计

- **总计**: 588,617 tokens（输入 408,336 / 输出 180,281）
