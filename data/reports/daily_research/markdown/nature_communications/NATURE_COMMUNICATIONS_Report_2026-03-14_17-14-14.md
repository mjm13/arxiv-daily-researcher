# 📊 Nature Communications 研究报告 (2026-03-14)

> 生成时间: 2026-03-14 17:14:14
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

- **总抓取**: 69 篇
- **及格论文**: 0 篇 (0.0%)

---

## 📋 所有论文列表

### 1. ❌ Multimodal framework for the joint analysis of single-cell RNA and T cell receptor sequencing data predicts T cell response to cancer immunotherapy

**作者**: Chujun He, Matthew Amodio, Orr Ashenberg, Kai W. Wucherpfennig, Ramnik J. Xavier, Caroline Uhler
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70505-0](https://doi.org/10.1038/s41467-026-70505-0)

**评分**: 10.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 2.0/10 | 2.0 |
| prognosis prediction | 1.0 | 8.0/10 | 8.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是单细胞RNA和T细胞受体测序数据的多模态整合分析，用于预测癌症免疫治疗中T细胞的反应。这与医学影像分析、医学影像分割、深度学习医学影像、手术规划、多模态医学影像、基础模型医学影像等关键词完全无关（评分为0）。论文使用AI方法（TRIM模型）进行预测，与'AI for diagnosis'有一定关联但非核心（评分为2）。论文明确提到T细胞状态具有预后价值，并预测治疗反应和疾病进展，与'prognosis prediction'高度相关（评分为8）。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The TCR-RNA Integrating Model (TRIM), a multi-modal variational autoencoder framework that integrates RNA-TCR data and predicts T cell clonality and transcriptional states, is presented, demonstrating its utility in modeling multimodal T cell data and predicting T cell response to treatment and disease progression.

!!! tip deepseek-chat TL;DR

    该研究开发了一个多模态变分自编码器框架TRIM，通过整合单细胞RNA和T细胞受体测序数据，预测T细胞对癌症免疫治疗的反应和疾病进展。

<details open>
<summary>摘要翻译</summary>

> T细胞状态在不同癌症类型中具有预后价值。近期技术已能实现单细胞分辨率下T细胞RNA与T细胞受体（TCR）序列的联合分析。本文提出TCR-RNA整合模型（TRIM），这是一个整合RNA-TCR数据并预测T细胞克隆性与转录状态的多模态变分自编码器框架。TRIM能够学习基于患者、组织来源和治疗时间点的数据共享表征。我们将TRIM应用于三个独立数据集，这些数据包含检查点抑制剂治疗前后采集的T细胞，样本来源包括头颈鳞状细胞癌和结直肠癌患者的血液与肿瘤活检组织，以及一个泛癌数据集中的肿瘤与癌旁组织。在所有场景中，TRIM均能基于治疗前血液或正常组织中的T细胞，准确预测肿瘤内T细胞的克隆扩增和转录状态，证明了其在建模多模态T细胞数据、预测T细胞对治疗的反应及疾病进展方面的实用价值。当前技术已能在单细胞层面同步分析T细胞RNA与TCR序列。本研究通过分析治疗前血液或组织中的T细胞，开发了TCR-RNA整合模型（TRIM），用于预测检查点抑制剂治疗后肿瘤内T细胞的特征。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> T cell states are prognostic in different cancer types. Recent technologies enable joint profiling of T cell RNA and T cell receptor (TCR) sequences at single-cell resolution. Here we present the TCR-RNA Integrating Model (TRIM), a multi-modal variational autoencoder framework that integrates RNA-TCR data and predicts T cell clonality and transcriptional states. TRIM learns a shared representation of the data conditioned on patient, tissue source, and treatment timepoint. We applied TRIM to three independent datasets that included T cells collected before and after checkpoint inhibitor treatment, sourced either from blood and tumor biopsies in patients with head and neck squamous cell carcinoma and colorectal cancer, or from tumor and adjacent tissue in a pan-cancer dataset. In all settings, TRIM accurately predicted intra-tumor T cell clonal expansion and transcriptional status based on T cells from blood or normal tissue before treatment, demonstrating its utility in modeling multimodal T cell data and predicting T cell response to treatment and disease progression. Recent technologies enable joint profiling of T cell RNA and T cell receptor (TCR) sequences at single-cell resolution. The authors here develop a TCR-RNA Integrating Model (TRIM) to predict intra tumor T cell signature post checkpoint inhibitor treatment by analyzing T cells from blood or tissues before treatment.

</details>
<br>

**关键词**: single-cell RNA sequencing, T cell receptor sequencing, multimodal integration, variational autoencoder, cancer immunotherapy, T cell response prediction, prognostic modeling, checkpoint inhibitor treatment

---

### 2. ❌ Label-free mass and size characterization of few-kDa biomolecules by hierarchical vision transformer augmented nanofluidic scattering microscopy

**作者**: Henrik Klein Moberg, Bohdan Yeroshenko, Joachim Fritzsche, David Albinsson, Barbora Špačková, Daniel Midtvedt, Giovanni Volpe, Christoph Langhammer
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70514-z](https://doi.org/10.1038/s41467-026-70514-z)

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

**评分理由**: 论文研究的是纳米流体散射显微镜结合分层视觉变换器（hierarchical vision transformer）来表征小分子生物分子（如胰岛素）的质量和尺寸，属于单分子生物物理学和光学显微镜领域。虽然使用了深度学习模型（vision transformer），但应用场景是纳米流体通道中的单分子散射数据分析，而非医学影像分析（CT、MRI、超声等）、疾病诊断、预后预测、手术规划或多模态医学影像。论文未涉及医学图像分割、临床决策支持或医疗AI模型的泛化性。因此，与所有给定关键词均无直接关联，相关度均为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work pushes the limit of nanofluidic scattering microscopy to below the theoretical limit set by the Cramér-Rao Lower Bound, which enables quantitative label-free single-molecule microscopy for biologically relevant families of sub-10-kDa molecules, such as cytokines, chemokines and peptide hormones.

!!! tip deepseek-chat TL;DR

    该研究通过结合超小纳米流体通道和分层视觉变换器分析，将无标记单分子散射显微镜的检测极限推至约6 kDa分子量和1.5 nm流体动力学半径，实现了对胰岛素等亚10-kDa生物分子的定量表征。

<details open>
<summary>摘要翻译</summary>

> 摘要：纳米流体散射显微技术通过分析分子与纳米通道产生的可见光散射干涉，实现了在亚波长纳米流道中对单分子的无标记表征。该方法通过追踪分子的扩散轨迹确定其流体动力学半径，并沿轨迹分析散射强度以测定分子量。然而，采用标准分析算法时，该技术仅限于表征大于≈60 kDa的蛋白质。本研究通过使用超小纳米流道并结合分层视觉变换器进行数据分析，将检测极限提升一个数量级，达到分子量低于≈6 kDa、流体动力学半径小于≈1.5 nm的范围——我们以肽类激素胰岛素为例验证了这一突破。当使用克拉默-拉奥下界（Cramér–Rao Lower Bound）设定的理论极限进行基准测试时，我们发现足够长的分子轨迹可使测量结果逼近该极限。这一进展使得针对生物相关的亚10-kDa分子家族（如细胞因子、趋化因子和肽类激素）进行定量无标记单分子显微观测成为可能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Nanofluidic scattering microscopy characterizes single molecules in subwavelength nanofluidic channels label-free, using the interference of visible light scattered by the molecule and nanochannel. It determines a molecule’s hydrodynamic radius by tracking its diffusion trajectory and its molecular weight by analyzing its scattering intensity along that trajectory. However, using standard analysis algorithms, it is limited to characterization of proteins larger than ≈ 60 kDa. Here, we push this limit by one order of magnitude to below ≈ 6 kDa molecular weight and ≈ 1.5 nm hydrodynamic radius — as we exemplify on the peptide hormone insulin — by using ultrasmall nanofluidic channels and by analyzing the data with a hierarchical vision transformer. When we benchmark this approach against the theoretical limit set by the Cramér–Rao Lower Bound, we find that it can be approached with sufficiently long molecular trajectories. This enables quantitative label-free single-molecule microscopy for biologically relevant families of sub-10-kDa molecules, such as cytokines, chemokines and peptide hormones.

</details>
<br>

**关键词**: nanofluidic scattering microscopy, single-molecule characterization, hierarchical vision transformer, label-free biomolecule analysis, hydrodynamic radius, molecular weight, sub-10-kDa molecules, Cramér–Rao Lower Bound

---

### 3. ❌ The evolutionary consequences of behavioural plasticity

**作者**: Carlos A. Botero
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70632-8](https://doi.org/10.1038/s41467-026-70632-8)

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

**评分理由**: 论文标题《The evolutionary consequences of behavioural plasticity》和摘要内容表明，该研究属于进化生物学和行为生态学领域，探讨行为可塑性（如学习、文化传播）对物种进化的影响。所有评分关键词均聚焦于医学影像分析、人工智能辅助临床决策等医疗技术领域，与论文的生物学进化主题完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The results indicate that this fast-acting form of plasticity enhances persistence under suboptimal conditions and facilitates the accumulation of genetic variation within populations, and suggest that behavioural plasticity may more broadly influence the evolutionary trajectories of individual lineages.

!!! tip deepseek-chat TL;DR

    该研究探讨了行为可塑性（如学习和文化传播）如何影响物种的进化轨迹，发现行为可塑性能够缓冲环境变化的选择压力，从而改变遗传进化的方向和速率。

**关键词**: behavioural plasticity, evolutionary consequences, learning, cultural transmission, environmental variation, genetic evolution, adaptive evolution

---

### 4. ❌ Structure of a pH-sensitive pentameric ligand-gated ion channel from the Sarcoptes scabies mite

**作者**: Jessica Matos Kleiz-Ferreira, Marijke Brams, Peter J. Harrison, Casey I. Gallagher, Mieke Nys, Ysaline Donze, Andrew Quigley, Daniel Bertrand, Chris Ulens
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70575-0](https://doi.org/10.1038/s41467-026-70575-0)

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

**评分理由**: 论文研究的是疥螨来源的pH敏感型五聚体配体门控离子通道的结构解析，属于结构生物学和神经药理学领域，与医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态影像或基础模型等关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解析了疥螨来源的pH敏感型五聚体配体门控离子通道的冷冻电镜结构，揭示了其独特的pH门控机制和潜在的药物靶点特性。

**关键词**: pentameric ligand-gated ion channel, pH-sensitive, Sarcoptes scabies, cryo-EM structure, ion channel, structural biology, neuropharmacology, drug target

---

### 5. ❌ Data-driven intelligent carbonization unifies diverse biomass into high-performance hard carbon negative electrodes

**作者**: Junfeng Cui, Yi Rao, Jianbao Gao, Hao Zhang, Cheng Lin, Jiale Zhao, Jiawen Zeng, Chun Fang, Zhiqiang Wang, Jinyu Wen, Bo Song, Yunhui Huang, Haiping Yang, Jia Xie, Yao Yao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70411-5](https://doi.org/10.1038/s41467-026-70411-5)

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

**评分理由**: 论文标题和摘要表明该研究聚焦于材料科学和能源存储领域，具体涉及生物质碳化制备高性能硬碳负极材料，与医学图像分析、人工智能临床决策支持等医疗领域完全无关。所有评分关键词均属于医疗AI范畴，而论文内容是关于电池电极材料的化学工程研究，两者领域完全不同，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过数据驱动的智能碳化方法，将多样化的生物质统一转化为高性能硬碳负极材料，用于钠离子电池，实现了优异的电化学性能。

**关键词**: data-driven carbonization, biomass conversion, hard carbon negative electrodes, sodium-ion batteries, electrochemical performance, intelligent carbonization, high-performance electrodes, biomass-derived carbon

---

### 6. ❌ Recycling senescent cell lipids for targeted senotherapy

**作者**: Xiaoxiao Ji, Xinzi He, Honglu Cai, Peng Tang, Hao Zhou, Jiajie Wang, Yifan Wu, Jinfeng Zhou, Zhang Lin, Kaicheng Xu, Changjian Lin, Xiaoyong Wu, Kanbin Wang, Wangmi Liu, Gang Feng, Shigui Yan, Guangyao Jiang, Zihao Qu, Yiying Qi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70486-0](https://doi.org/10.1038/s41467-026-70486-0)

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

**评分理由**: 论文标题和摘要均未提供，无法评估具体内容。根据标题《Recycling senescent cell lipids for targeted senotherapy》判断，该研究聚焦于衰老细胞脂质回收和靶向衰老治疗，属于细胞生物学、衰老研究和治疗学领域，与给定的医学影像分析、深度学习、AI诊断、手术规划等关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work exploits SnCs' lipid metabolic signature to develop a senotherapeutic strategy that circumvents potential side effects associated with direct SnCs clearance and repurposes these traditionally harmful cells as functional resources, establishing a shift in the philosophy of senescence therapy.

!!! tip deepseek-chat TL;DR

    该研究探索了回收衰老细胞脂质用于靶向衰老治疗的策略，但具体方法和结果未在摘要中说明。

**关键词**: senescent cells, lipids, senotherapy, targeted therapy, cellular senescence, aging, lipid recycling, therapeutic strategy

---

### 7. ❌ A hydro-topological strategy enables self-regulating biofilms for sustainable wastewater treatment

**作者**: Yong Fang, Zhiqiang Zhang, Boru Xue, Ying Liu, Kuichuan Sheng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70682-y](https://doi.org/10.1038/s41467-026-70682-y)

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

**评分理由**: 论文研究的是废水处理中的生物膜反应器技术，具体涉及V型载体的水拓扑设计策略，以实现生物膜自调节和高效营养物去除。所有评分关键词均与医学影像分析、人工智能临床决策支持相关，而论文完全不涉及医学影像、疾病诊断、手术规划或任何医疗领域内容。因此，所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文针对移动床生物膜反应器载体堵塞问题，提出了一种V型载体水拓扑设计策略，实现了生物膜自调节和高效营养物去除，在低温高负荷条件下仍保持稳定性能。

<details open>
<summary>摘要翻译</summary>

> 摘要 移动床生物膜反应器（MBBR）是现代废水处理的核心技术，但其性能常受填料堵塞的制约，这会显著降低整体处理效率并削弱该技术的环境效益。本文提出一种V型填料的水力拓扑设计策略，该策略能够实现生物膜的自我调控，从而同时控制生物膜厚度并实现连续水力剪切诱导的自清洁。在一个处理实际市政污水超过500天的纯生物膜系统中，V型填料即使在低温（9.1 °C）和高负荷条件下，也能实现稳定高效的营养物去除。关键在于，与传统的K3填料相比，其单位生物量的硝化速率提高了3.2倍，而生物膜生物量却降低了44%，这表明通过优化的生态位设计，处理效率与生物量数量实现了解耦。这项工作为生物膜反应器设计确立了一个新范式，将填料从被动的微生物附着基质转变为微生物生态系统的主动调节者，对可持续水处理基础设施具有深远意义。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract The moving bed biofilm reactor (MBBR) is a cornerstone technology in modern wastewater treatment, yet its performance is often hindered by carrier clogging, which significantly reduces overall treatment efficiency and undermines the technology’s environmental benefits. Here, we introduce a V-carrier hydro-topological design strategy that enables biofilm self-regulation, allowing simultaneous control of biofilm thickness and continuous hydraulic shear-induced self-cleaning. In a pure biofilm system treating real municipal wastewater for over 500 days, the V-carrier achieves stable and efficient nutrient removal even under low-temperature (9.1 °C) and high-loading conditions. Crucially, it achieves a 3.2-fold higher unit biomass nitrification rate with a biofilm biomass 44% lower than a conventional K3 carrier, demonstrating that treatment efficiency is decoupled from biomass quantity through optimal ecological niche design. This work establishes a paradigm for biofilm reactor design, transforming carriers from passive substrates into active regulators of microbial ecosystems, with profound implications for sustainable water infrastructure.

</details>
<br>

**关键词**: biofilm reactor, wastewater treatment, V-carrier, hydro-topological design, self-regulation, nutrient removal, moving bed biofilm reactor, sustainable water infrastructure

---

### 8. ❌ Microglial cathepsin B is necessary for neuronal efferocytosis in zebrafish and mice during brain development

**作者**: Nicholas J. Silva, Sarah R. Anderson, Supriya A. Mula, Caroline C. Escoubas, Haruna Nakajo, Anna V. Molofsky
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70350-1](https://doi.org/10.1038/s41467-026-70350-1)

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

**评分理由**: 论文研究的是大脑发育过程中小胶质细胞通过溶酶体蛋白酶cathepsin B介导神经元清除的细胞生物学机制，使用斑马鱼和小鼠模型，涉及遗传学、活体成像和行为学分析。所有评分关键词均聚焦于医学影像分析、深度学习、AI诊断、手术规划等临床决策支持技术，而本论文完全不涉及医学影像处理、AI算法开发或临床应用，属于基础神经发育生物学研究，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究发现小胶质细胞的溶酶体蛋白酶cathepsin B在斑马鱼和小鼠大脑发育过程中对神经元清除至关重要，其缺失会导致吞噬功能受损和行为异常。

<details open>
<summary>摘要翻译</summary>

> 摘要：在发育中的大脑内，半数新生神经元通过胞葬作用——即凋亡细胞的吞噬清除——被移除。小胶质细胞是大脑常驻的专业吞噬细胞，在神经环路发育中扮演重要角色，其中包括作为胞葬作用的主要执行者。尽管小胶质细胞识别潜在吞噬对象的机制已被广泛研究，但对于高效消化所必需的溶酶体机制则定义尚不明确。本研究表明，在斑马鱼和小鼠脑中，神经元更新率较高的脑区内，小胶质细胞中的溶酶体蛋白酶组织蛋白酶B（cathepsin B）含量丰富。在斑马鱼和小鼠中，组织蛋白酶B的基因破坏会导致小胶质细胞内积累未消化的死亡细胞。对斑马鱼的活体成像研究以及对培养的小鼠小胶质细胞的观察显示，其吞噬事件减少，总体吞噬能力下降。我们在两种模型中也观察到了行为损伤。这些数据揭示了小胶质细胞组织蛋白酶B在脊椎动物大脑发育中的作用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Half of all newborn neurons in the developing brain are removed via efferocytosis - the phagocytic clearance of apoptotic cells. Microglia are brain-resident professional phagocytes that play important roles in neural circuit development including as primary effectors of efferocytosis. While the mechanisms through which microglia recognize potential phagocytic cargo are widely studied, the lysosomal mechanisms that are necessary for efficient digestion are less well defined. Here we show that the lysosomal protease cathepsin B is enriched in microglia located in brain regions where neuronal turnover is high in both zebrafish and mouse. Genetic disruption of cathepsin B in zebrafish and mice had an accumulation of microglia containing undigested dead cells. Live imaging studies in zebrafish and in cultured mouse microglia revealed fewer phagocytic events and reduced overall phagocytosis. We also observed behavioral impairments in both models. These data reveal a role for microglial cathepsin B in vertebrate brain development.

</details>
<br>

**关键词**: microglia, cathepsin B, efferocytosis, brain development, zebrafish, mouse, phagocytosis, neuronal turnover

---

### 9. ❌ The COP1-ADA2b module mediates light regulation of DNA double-strand break repair in Arabidopsis

**作者**: Li Chen, Liman Diao, Jiaqi Ruan, Yanli Deng, Kai Zhang, Yan Guan, Ling Li, Min Liang, Lina Peng, Jiayi Shi, Xin Zhang, Minqing Liu, Yupeng Li, Zhilei Mao, Wenxiu Wang, Hong-Quan Yang, Tongtong Guo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70673-z](https://doi.org/10.1038/s41467-026-70673-z)

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

**评分理由**: 论文标题和摘要显示该研究聚焦于植物生物学（拟南芥）中光调控DNA双链断裂修复的分子机制，涉及COP1-ADA2b模块的功能分析。所有评分关键词均与医学影像分析、人工智能临床决策支持、疾病诊断/预后、手术规划等医学领域直接相关，而本文研究内容属于基础植物分子生物学，与医学影像或临床AI无任何关联。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Findings reveal a pivotal role for the COP1-ADA2b module in CRYs- and phyA/phyB-mediated light regulation of DSB repair and suggest the antagonistic regulation of ADA2b stability by photoreceptors and COP1 may dynamically calibrate DNA repair activity to maintain genome stability and optimize plant growth according to the fluctuating light conditions.

!!! tip deepseek-chat TL;DR

    该研究揭示了在拟南芥中，COP1-ADA2b模块通过调控组蛋白乙酰化和染色质可及性，介导光信号对DNA双链断裂修复的调控机制。

**关键词**: Arabidopsis, DNA double-strand break repair, light regulation, COP1-ADA2b module, histone acetylation, chromatin accessibility, plant molecular biology

---

### 10. ❌ Hypusination of the translation factor eIF5A regulates mitochondrial tRNA processing to promote prostate cancer aggressiveness

**作者**: Michel Kahi, Abigail Mazzu′, Ludovic Batistic, Marc Pujalte-Martin, Victor Tiroille, Anne Vincent, Joseph Murdaca, Loïc Trapani, Paraskevi Kousteridou, Oumayma Benaceur, Amine Belaïd, Marie Irondelle, Emilie Thomas, Christelle Boscagli, Pierre Bertrand, Heather S. Carr, Frédéric Larbret, Émilie Baudelet, Stéphane Audebert, Didier F. Pisani
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70566-1](https://doi.org/10.1038/s41467-026-70566-1)

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

**评分理由**: 论文研究的是前列腺癌的分子生物学机制，具体探讨eIF5A蛋白的hypusination修饰如何通过调控线粒体tRNA加工来促进前列腺癌的侵袭性。研究内容完全属于分子生物学、细胞生物学和癌症生物学领域，使用的方法包括分子生物学实验、细胞培养、基因表达分析等。所有评分关键词均涉及医学影像分析、人工智能、深度学习在医疗影像中的应用、手术规划等，与论文的分子机制研究完全无关。论文未涉及任何医学影像数据、AI模型、诊断预测系统或手术相关技术。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究发现eIF5A蛋白的hypusination修饰通过调控线粒体tRNA加工促进前列腺癌的侵袭性，揭示了新的分子机制和治疗靶点。

**关键词**: eIF5A, hypusination, mitochondrial tRNA processing, prostate cancer, cancer aggressiveness, translation factor, molecular mechanism, therapeutic target

---

### 11. ❌ Strong interplay between polar and structural topologies

**作者**: Rujian Jiang, Mei‐Xiong Zhu, Su-Zhen Liu, Yu-Ting Chen, Desheng Ma, Yanpeng Feng, Min-Jie Zou, Meng-Jiao Han, Chi Hou Lei, Yu-Jia Wang, Yun-Long Tang, Yin-Lian Zhu, Xiuliang Ma
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70515-y](https://doi.org/10.1038/s41467-026-70515-y)

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

**评分理由**: 论文标题《Strong interplay between polar and structural topologies》和摘要内容表明，该研究聚焦于凝聚态物理或材料科学领域，具体探讨极性拓扑结构与结构拓扑之间的相互作用，属于基础物理研究范畴。所有评分关键词均涉及医学影像分析、人工智能医疗应用等临床医学领域，与论文的物理材料研究方向完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究揭示了极性拓扑结构与结构拓扑在材料中的强相互作用机制及其对材料物理性质的影响。

**关键词**: polar topology, structural topology, topological structures, material properties, condensed matter physics, interplay mechanism

---

### 12. ❌ Catalytic Proximal Protein Oligomerization as an Anti-Tumor Strategy Targeting WDR5

**作者**: Yizheng Fang, Li Jiang, Feifan Wang, Yihui Zhou, Jie Cen, Yuxin Yang, Haiyang Wang, Qi Chen, Yushen Lin, Tingting Wang, Hongxia Xu, Yongping Yu, Chengliang Zhu, Qiaojun He, Bo Yang, Chun Zhou, Wenteng Chen, Longhua Tang, Ji Cao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-13
**DOI**: [10.1038/s41467-026-70409-z](https://doi.org/10.1038/s41467-026-70409-z)

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

**评分理由**: 论文研究的是通过催化近端蛋白质寡聚化靶向WDR5的抗肿瘤策略，属于化学生物学、药物发现和癌症治疗领域。论文内容涉及蛋白质相互作用、小分子抑制剂设计和抗肿瘤活性评估，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态影像或基础模型等关键词。所有关键词与论文主题完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Nanopore sensing enabled rapid identification of WZ-1, a selective WDR5 oligomerization inducer, from the in-house compound library and validates CaPPO as a promising small-molecule design strategy for therapeutic development.

!!! tip deepseek-chat TL;DR

    该研究开发了一种通过催化近端蛋白质寡聚化靶向WDR5的小分子抑制剂，在体外和体内实验中显示出抗肿瘤活性。

**关键词**: WDR5, protein oligomerization, anti-tumor strategy, small molecule inhibitor, cancer therapy, targeted therapy, chemical biology

---

### 13. ❌ Endogenous VEGF signaling acts as a guardian of human primed pluripotency

**作者**: Xu Wu, Chunsheng Wen, Chaonan Zhu, Huiyuan Jiao, Chenge Xin, Haokun Jiang, Ran Tong, Yuwei Huang, Yuan Yuan, Min Shao, Hanzhi Zhao, Junjie Gu, Qiong Wu, Feng Zhang, Han Wang, Yifan Zhou, Bing Liao, Lingjie Li, Ying Jin, Hui Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70526-9](https://doi.org/10.1038/s41467-026-70526-9)

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

**评分理由**: 论文研究的是干细胞生物学中VEGF信号通路对人类原始多能性的调控机制，属于基础生命科学研究，与医学影像分析、人工智能、临床决策支持等关键词完全无关。论文内容涉及分子生物学、细胞信号传导和干细胞功能，没有涉及任何医学影像技术、AI算法、疾病诊断或手术规划相关内容。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work uncovers a pivotal VEGF-dependent network maintaining primed pluripotency, providing valuable insights into integrated pluripotency and lineage regulation by signaling cascades and transcription factors.

!!! tip deepseek-chat TL;DR

    该研究发现内源性VEGF信号通路在维持人类原始多能干细胞状态中起关键保护作用，揭示了VEGF通过调控特定信号网络来防止多能性退化的分子机制。

**关键词**: VEGF signaling, human pluripotency, primed pluripotent stem cells, endogenous signaling, stem cell maintenance, molecular regulation, cellular signaling pathways, developmental biology

---

### 14. ❌ Dual-stiffness nanoparticles for compartment-specific drug delivery in stroke

**作者**: Hui Liu, Juanjuan Zheng, Yaosheng Li, Rouxuan Wang, Zefeng Yang, Yunfei Dong, Yuankai Sun, Zhiwei Du, Liang Pei, Xiaoyu Qiu, Bo Zhao, Lu Li, Jiahe Wu, Xuejin Li, Xinchi Jiang, Chun-Xia Zhao, Jianqing Gao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70340-3](https://doi.org/10.1038/s41467-026-70340-3)

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

**评分理由**: 论文研究的是用于缺血性卒中治疗的纳米颗粒药物递送系统，重点关注纳米颗粒刚度对生物分布的影响以及外周-中枢协同治疗策略。论文内容完全属于纳米医学、药物递送和生物材料领域，不涉及任何医学影像分析、深度学习、AI诊断、预后预测、手术规划或多模态影像。所有关键词均与论文主题无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This mechano-guided delivery strategy achieves synergistic "peripheral-central" intervention via a single administration, establishing a paradigm for precision nanomedicine, with broad potential in treating multi-compartment pathologies.

!!! tip deepseek-chat TL;DR

    该研究针对缺血性卒中治疗中外周和中枢病理分隔的挑战，开发了一种基于双刚度纳米颗粒的空间分层药物递送策略，通过刚度依赖的生物分布实现外周免疫系统和中枢神经系统的协同治疗。

<details open>
<summary>摘要翻译</summary>

> 缺血性卒中面临外周免疫系统与中枢神经系统中动态且区室化的双重病理挑战。本研究突破传统整体治疗策略，开发了一种空间分层给药方法，通过组合使用双刚度纳米颗粒实现区室特异性治疗。利用刚度依赖性生物分布特性，刚性纳米颗粒优先靶向外周免疫细胞，递送抗炎药物以减轻全身炎症并阻止免疫细胞向脑内浸润；与此同时，软性纳米颗粒因能避免免疫摄取，可高效穿透血脑屏障，递送神经保护剂并修复受损的神经微环境。机制研究表明，这种选择性分布源于纳米颗粒刚度依赖的膜能量学与竞争性血清蛋白吸附之间的相互作用。这种力学引导的递送策略通过单次给药实现了“外周-中枢”协同干预，为精准纳米医学建立了新范式，在治疗多区室病理领域具有广泛潜力。缺血性卒中涉及复杂的外周与中枢病理过程。本文作者开发了一种采用双刚度纳米颗粒的空间分层策略，实现区室特异性药物递送，提供了协同治疗新范式。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Ischemic stroke presents a dual therapeutic challenge, involving dynamic and compartmentalized pathology in both the peripheral immune system and the central nervous system. Departing from conventional holistic treatment strategies, we developed a spatially tiered drug delivery approach using a combination of dual-stiffness nanoparticles (NPs) for compartment-specific therapy. Exploiting stiffness-dependent biodistribution, stiff NPs preferentially targeted peripheral immune cells, delivering anti-inflammatory agents to attenuate systemic inflammation and prevent immune cell infiltration into the brain. In parallel, soft NPs, shielded from immune uptake, efficiently penetrated the brain to deliver neuroprotectants and restore the damaged neural microenvironment. Mechanistic studies indicate that this selective distribution arises from the interplay between NP stiffness-dependent membrane energetics and competitive serum protein adsorption. This mechano-guided delivery strategy achieves synergistic “peripheral-central” intervention via a single administration, establishing a paradigm for precision nanomedicine, with broad potential in treating multi-compartment pathologies. Ischemic stroke involves complex peripheral and central pathologies. Here, authors develop a spatially tiered strategy using dual stiffness nanoparticles for compartment-specific drug delivery, offering a synergistic treatment paradigm.

</details>
<br>

**关键词**: ischemic stroke, nanoparticles, drug delivery, compartment-specific therapy, stiffness-dependent biodistribution, peripheral-central intervention, precision nanomedicine, dual-stiffness nanoparticles

---

### 15. ❌ Volatile resorption expedites eruption onset in large silicic systems

**作者**: Franziska Keller, Meredith Townsend, Juliana Troch, Christian Huber
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70206-8](https://doi.org/10.1038/s41467-026-70206-8)

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

**评分理由**: 该论文研究火山喷发机制，属于地球科学/火山学领域，与医学图像分析、人工智能、临床决策支持等主题完全无关。论文内容涉及岩浆房模型、挥发物再吸收、火山喷发触发机制等地质过程，未提及任何医学成像、深度学习、疾病诊断或手术规划相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究发现火山系统中挥发物再吸收（而非传统认为的挥发物出溶）能加速岩浆房增压，从而可能提前触发大规模硅质火山喷发。

<details open>
<summary>摘要翻译</summary>

> 摘要：硅质破火山口形成喷发是地球上最危险的自然现象之一，但其触发机制仍不甚明了。虽然挥发分出溶被广泛认为是大型硅质系统中潜在的喷发驱动因素，但我们发现，与直觉相反，挥发分再吸收反而能比出溶更快地促进岩浆房增压。通过热力学-机械岩浆房模型，我们证明再吸收是快速补给系统中的常见过程，由压力升高和晶体熔融驱动。阿苏-4喷发提供了一个可能发生挥发分再吸收的自然案例，模型预测在补给速率大于10^-2.4 km³/年时会出现再吸收。通过降低岩浆整体压缩性，再吸收会放大增压效应，驱动岩浆房失稳并可能加速喷发起始。本文提出，挥发分再吸收是一种既能适应又能促进岩浆房快速增压的自然过程，对大规模硅质系统的失稳至关重要。在监测信号中识别其特征可为即将发生的喷发提供早期预警。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Silicic caldera-forming eruptions are among the most hazardous natural phenomena on Earth, yet their triggering mechanisms remain poorly understood. While volatile exsolution is widely recognized as a potential eruption driver in large silicic systems, we find that volatile resorption can, counterintuitively, promote chamber pressurization faster than volatile exsolution. Using a thermo-mechanical magma chamber model, we show that resorption is a common process in rapidly recharged systems, driven by pressure increase and crystal melting. The Aso-4 eruption offers a natural case where volatile resorption may have occurred, with model results predicting resorption at recharge rates &gt;10 -2.4 km 3 /yr. Through reducing bulk magma compressibility, resorption amplifies pressurization, driving chamber destabilization and potentially expediting eruption onset. Here, we propose that volatile resorption is a natural process both accommodating and promoting rapid chamber pressurization, fundamental to destabilizing large-scale silicic systems. Detecting its signatures in monitoring signals could provide early warning of imminent eruption.

</details>
<br>

**关键词**: silicic caldera-forming eruptions, volatile resorption, magma chamber pressurization, eruption triggering mechanisms, thermo-mechanical model, Aso-4 eruption, chamber destabilization, early warning

---

### 16. ❌ Pan-tumor activity of olomorasib, a next-generation KRAS G12C inhibitor in KRAS G12C-mutant advanced solid tumors: a first-in-human study

**作者**: Yonina R. Murciano-Goroff, Antoine Hollebecque, Rebecca S. Heist, Philippe A. Cassier, Ji‐Youn Han, So Yeon Kim, Joshua K. Sabari, Diego Tosi, Adrian G. Sacher, Timothy F. Burns, T. Shimizu, Natraj Reddy Ammakkanavar, Alexander Spira, Carlos Gomez-Roca, A. Patnaik, Rasha Cosman, J. Nicholas Bodor, Misako Nagasaka, Arthur Xintian You, Samuel McNeely
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-69943-7](https://doi.org/10.1038/s41467-026-69943-7)

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

**评分理由**: 该论文是一项关于新型KRAS G12C抑制剂olomorasib的首次人体临床试验，研究内容为药物剂量、安全性、耐受性和抗肿瘤活性评估。论文完全不涉及医学影像分析、分割、深度学习、AI诊断、预后预测、手术规划、多模态影像或基础模型等主题。所有关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Among 168 efficacy-evaluable patients, the ORR and median PFS were both higher in non-CRC solid tumors compared to CRC, including in patients with NSCLC who previously received a KRAS G12C inhibitor.

!!! tip deepseek-chat TL;DR

    这项首次人体临床试验评估了新型KRAS G12C抑制剂olomorasib在KRAS G12C突变晚期实体瘤患者中的安全性、耐受性和抗肿瘤活性，结果显示该药物耐受性良好，在非结直肠癌肿瘤中显示出更高的客观缓解率和中位无进展生存期。

<details open>
<summary>摘要翻译</summary>

> 摘要 这项多中心、首次人体1期研究（NCT04956640）评估了奥洛莫拉西（LY3537982），这是一种旨在低绝对暴露水平下增强靶点占位的下一代KRAS G12C抑制剂。研究共报告了195例患者的数据：1a期剂量递增部分（n = 112）评估了奥洛莫拉西单药治疗（50、100、150或200 mg，每日两次）在KRAS G12C突变晚期实体瘤患者中的应用；其主要目的是基于剂量限制性毒性确定2期推荐剂量。未发生剂量限制性毒性，150 mg每日两次被选定为2期推荐剂量。1b期剂量扩展部分（n = 83）的主要目的是评估奥洛莫拉西在特定KRAS G12C突变肿瘤类型中的安全性和耐受性。奥洛莫拉西耐受性良好，治疗相关不良事件主要为1-2级，3级事件少见；未发生4/5级治疗相关不良事件。次要研究目的评估了奥洛莫拉西的抗肿瘤活性。在168例可评估疗效的患者中，非结直肠癌实体瘤（包括既往接受过KRAS G12C抑制剂治疗的非小细胞肺癌患者）的客观缓解率和中位无进展生存期均高于结直肠癌患者。在未经治疗的活性脑转移患者中观察到了颅内缓解。这可能支持下一代KRAS G12C抑制剂具有克服早期药物局限性的潜力，并为联合疗法的进一步研究提供了依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract This multicenter, first-in-human Phase 1 study (NCT04956640) evaluated olomorasib (LY3537982), a next-generation KRAS G12C inhibitor designed to enhance target occupancy at low absolute exposures. In total, data from 195 patients are reported: Phase 1a dose escalation ( n = 112) assessed olomorasib monotherapy at 50, 100, 150 or 200 mg BID across KRAS G12C-mutant advanced solid tumors; the primary objective was to determine the recommended Phase 2 dose (RP2D) based on dose-limiting toxicities (DLTs). No DLTs occurred, and 150 mg BID was selected as the RP2D. The primary objective for the Phase 1b dose expansion ( n = 83) was to evaluate the safety and tolerability of olomorasib in specific KRAS G12C-mutant tumor types. Olomorasib was well tolerated, with predominantly grade 1–2 treatment-related adverse events (TRAEs) and infrequent grade 3 TRAEs; no grade 4/5 TRAEs occurred. Secondary objectives evaluated the antitumor activity of olomorasib. Among 168 efficacy-evaluable patients, the ORR and median PFS were both higher in non-CRC solid tumors compared to CRC, including in patients with NSCLC who previously received a KRAS G12C inhibitor. Intracranial responses were observed in patients with untreated, active brain metastases. This may support the potential of next-generation KRAS G12C inhibitors to overcome limitations of earlier agents and justify further investigation of combination therapy.

</details>
<br>

**关键词**: KRAS G12C inhibitor, olomorasib, first-in-human study, advanced solid tumors, dose escalation, safety and tolerability, antitumor activity, brain metastases

---

### 17. ❌ Twisted atomic magnetic tunnel junctions with multiple nonvolatile states

**作者**: Yuliang Chen, Kartik Samanta, Alexander J. Healey, Chi Fang, Haojie Zhang, Naafis Ahnaf Shahed, David A. Broadway, Arthur Ernst, Evgeny Y. Tsymbal, Stuart S. P. Parkin
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70239-z](https://doi.org/10.1038/s41467-026-70239-z)

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

**评分理由**: 论文研究的是二维磁性隧道结（MTJs）在原子尺度上的多态非易失性存储，属于凝聚态物理、材料科学和自旋电子学领域。所有评分关键词均涉及医学影像分析、人工智能临床决策支持等医疗健康应用，与论文的物理器件研究完全无关。论文未提及任何医学影像、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过构建二维扭曲磁性隧道结，在原子尺度实现了多态非易失性磁信息存储，并展示了不同状态间的可控切换。

<details open>
<summary>摘要翻译</summary>

> 摘要：磁隧道结作为自旋电子学的核心器件，近年来借助二维磁体实现了快速发展。特别是基于扭曲二维反铁磁体构建的磁隧道结，将非易失性磁信息存储推向了原子尺度极限。本文展示了具有多重非易失性态的二维扭曲磁隧道结。通过扭曲单个铁磁CrSBr单层与单个反铁磁CrSBr双层形成非对称磁隧道结结构，该器件在2K温度零磁场条件下呈现出两种截然不同的态，其隧道磁阻率高达700%。通过引入第二层CrSBr单层构建第二个扭曲界面，可在零磁场下实现四种非易失性态。更重要的是，利用磁场可实现四种状态中任意状态之间的相互切换。我们进一步展示了由三个扭曲反铁磁CrSBr双层构成的全反铁磁磁隧道结，该结构同样呈现多重非易失性态。本研究表明，通过在原子极限尺度集成多个扭曲界面，可在单一器件中实现多态磁信息的存储。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Magnetic tunnel junctions (MTJs), a key spintronic device, have shown rapid development recently using two-dimensional (2D) magnets. In particular, MTJs formed from twisted 2D antiferromagnets (AFMs) push nonvolatile magnetic information storage to the atomic limit. Here we demonstrate 2D twisted MTJs with multiple distinct nonvolatile states. Asymmetric MTJ structures formed by twisting a single ferromagnetic CrSBr monolayer and a single antiferromagnetic CrSBr bilayer exhibit two distinct states with up to 700% tunneling magnetoresistance in zero magnetic field at 2 K. By adding a second CrSBr monolayer to form a second twisted interface, four nonvolatile states can be accessed in zero magnetic field. More importantly, any one state among the four states can be switched to any other using magnetic fields. We further demonstrate all-antiferromagnetic MTJs with three twisted antiferromagnetic CrSBr bilayers that exhibit multiple nonvolatile states. Our work shows that it is possible to store multiple-state magnetic information in a single device by integrating several twisted interfaces in the atomic limit.

</details>
<br>

**关键词**: magnetic tunnel junctions, twisted 2D magnets, nonvolatile states, tunneling magnetoresistance, CrSBr, antiferromagnets, atomic limit, spintronic device

---

### 18. ❌ Thermal detection of single photons using Dirac fermions

**作者**: Bevin Huang, Ethan G. Arnault, Woochan Jung, Caleb Fried, B. Jordan Russell, Kenji Watanabe, Takashi Taniguchi, Erik A. Henriksen, Dirk Englund, Gil-Ho Lee, Kin Chung Fong
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70648-0](https://doi.org/10.1038/s41467-026-70648-0)

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

**评分理由**: 论文研究的是利用石墨烯中狄拉克费米子的热特性检测单光子，属于量子物理、纳米技术和光子探测器领域。所有评分关键词均围绕医学影像分析、AI临床决策支持、疾病诊断/预后、手术规划等医疗应用，而该论文完全不涉及医学影像、医疗数据、疾病或临床应用，因此所有关键词相关度均为0。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了利用石墨烯中狄拉克费米子的热特性检测单近红外光子的方法，在原理验证实验中实现了87%的量子效率和极低暗计数，展示了石墨烯测辐射热计在探测中红外至微波波段低能光子方面的潜力。

<details open>
<summary>摘要翻译</summary>

> 摘要 单光子探测在量子科学、量子网络、生物学及先进成像领域至关重要。为探测光子携带的微小能量量子，传统机制依赖于半导体带隙或超导带隙的能量激发，这限制了其在低能量光子探测中的应用。本文中，我们利用石墨烯中狄拉克费米子的热学特性实现了近红外单光子探测。通过利用狄拉克电子在电荷中性点附近极低的热容，我们采用混合约瑟夫森结观测到高达约2 K的温度上升。在此原理验证实验中，我们实现了87%（75%）的本征量子效率，暗计数率低于每秒（每周）1次，达到了2 × 10⁻²² W/√Hz的有效噪声等效功率。最高工作温度为1.2 K。我们的研究结果凸显了石墨烯辐射热计在探测中红外至微波波段低能量光子方面的潜力，为远红外空间科学研究、暗物质搜寻的潜在应用以及拓展更宽电磁频谱的量子技术开辟了新路径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Detecting single photons is a crucial process in quantum science, quantum networking, biology, and advanced imaging. To detect the small quantum of energy carried in a photon, conventional mechanisms rely on energy excitation across either a semiconductor bandgap or superconducting gap that hinders their applications to low-energy photons. Here, we detect single near-infrared photons using the thermal properties of Dirac fermions in graphene. By exploiting the extremely low heat capacity of Dirac electrons near its charge neutrality point, we observe a temperature rise up to ~ 2 K using a hybrid Josephson junction. In this proof-of-principle experiment, we achieve an intrinsic quantum efficiency of 87% (75%) with dark count &lt; 1 per second (per week), reaching an effective noise equivalent power of 2 × 10 −22 W/ $$\sqrt{{{{\rm{Hz}}}}}$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:msqrt> <mml:mrow> <mml:mi>Hz</mml:mi> </mml:mrow> </mml:msqrt> </mml:math> . The highest operation temperature is 1.2 K. Our results highlight the potential of graphene bolometers for detecting lower-energy photons from the mid-IR to microwave regimes, opening pathways to study space science in far-infrared regime, to potential applications in dark matter searches, and to advance quantum technologies across a broader electromagnetic spectrum.

</details>
<br>

**关键词**: single photon detection, graphene bolometer, Dirac fermions, quantum efficiency, near-infrared photons, Josephson junction, low-energy photon detection, thermal detection

---

### 19. ❌ Patterns and determinants of mitogenomic evolution in Bilateria

**作者**: Ivan Jakovlić, Yi-Wen Ma, Tong Ye, Rui Han, Xiang Liu, Chuan‐Yu Xiang, Hong Zou, Jin Zhang, Rui Song, Wen-Xiang Li, Gui-Tang Wang, Yindong Tong, Fei Liu, Benhe Zeng, Jinsong Chen, Dong Zhang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70576-z](https://doi.org/10.1038/s41467-026-70576-z)

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

**评分理由**: 论文研究的是双侧动物线粒体基因组的进化模式，属于进化生物学和基因组学领域，与医学图像分析、人工智能临床决策支持等关键词完全无关。论文内容涉及线粒体基因组结构、进化速率、选择压力等生物学问题，未提及任何医学成像、深度学习、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Evidence is provided that purifying selection mediated by locomotory capacity and species ecology is a major driver of mitogenomic architectural evolution, but other variables are required to fully explain the observed patterns.

!!! tip deepseek-chat TL;DR

    该研究通过分析超过10,000个双侧动物线粒体基因组，发现运动能力和寄生生活方式是线粒体基因组结构进化速率差异的主要驱动因素，但其他变量仍需考虑以完全解释观察到的模式。

<details open>
<summary>摘要翻译</summary>

> 部分动物的线粒体基因组结构在超过五亿年间几乎保持不变，而其他谱系则表现出种内变异。这种差异背后的驱动因素尚不明确。我们分析了超过10,000个两侧对称动物线粒体基因组，以检验运动能力和寄生生活方式是否能解释结构进化速率的变异，并尝试回答其他多个进化问题。双链（基因分布于两条链上）结构是大多数主要辐射类群（门及以上等级）最可能的祖先状态。我们发现了二十余次向单链结构的转变，以及状态逆转的证据（见于环节动物门和软体动物门）。基因重排速率与序列进化速率呈正相关（r = 0.69），二者在单链线粒体基因组、寄生类群及运动能力较低的物种中均有所提升。后两类群中单链结构和GC偏斜逆转的发生率更高。线粒体基因组大小与进化速率呈负相关，而有效种群规模与所有测试的进化变量均无关联。在两侧对称动物中，恒温动物的进化速率慢于变温动物，但在脊索动物门中则更快。本研究证明，由运动能力和物种生态介导的纯化选择是线粒体基因组结构进化的主要驱动力，但要完全解释观察到的模式仍需其他变量。两侧对称动物的线粒体基因组在结构重排速率上表现出高度变异，本研究为此差异提供了证据，表明由运动能力和物种生态介导的纯化选择是线粒体基因组结构进化的关键驱动因素。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Mitochondrial genomes of some animals remained almost unchanged architecturally for over half a billion of years, while other lineages exhibit conspecific variability. The drivers underlying this disparity remain unknown. We analyse over 10,000 bilaterian mitogenomes to test whether locomotory capacity and parasitic lifestyle can explain the variability in architectural evolutionary rates, and attempt to answer multiple other evolutionary questions. Double-stranded (genes on both strands) architecture is the most likely ancestral state for most major radiations (phylum and above). We identify over twenty transitions to single-stranded architectures, and the evidence of state-reversals (in Annelida and Mollusca). Gene order rearrangement and sequence evolution rates are positively correlated (r = 0.69), and both are increased in single-stranded mitogenomes, parasites, and species with low locomotory capacity. The latter two categories exhibit increased prevalence of single-strandedness and GC skew inversions. Mitogenome size is negatively correlated with evolutionary rates, whereas the effective population size is decoupled from all tested evolutionary variables. Endotherms exhibit slower evolutionary rates than ectotherms in Bilateria, but faster in Chordata. Here, we provide evidence that purifying selection mediated by locomotory capacity and species ecology is a major driver of mitogenomic architectural evolution, but other variables are required to fully explain the observed patterns. Mitochondrial genomes of bilateral animals exhibit high variability in architectural rearrangement rates, but the reason for this disparity remains unknown. This study provides evidence that purifying selection mediated by locomotory capacity and species ecology is a major driver of mitogenomic architectural evolution.

</details>
<br>

**关键词**: mitochondrial genomes, Bilateria, architectural evolution, locomotory capacity, parasitic lifestyle, gene order rearrangement, purifying selection, evolutionary rates

---

### 20. ❌ Proteostasis failure and mitochondrial dysfunction contribute to chromosomal instability-induced microcephaly

**作者**: Amanda González-Blanco, Adrián Acuña-Higaki, David Boettger, Jery Joy, Marco Milán
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70521-0](https://doi.org/10.1038/s41467-026-70521-0)

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

**评分理由**: 论文研究的是马赛克杂色非整倍体（MVA）导致小头畸形的细胞机制，使用果蝇模型探索染色体不稳定性、蛋白质稳态失败和线粒体功能障碍之间的关系。所有评分关键词均涉及医学影像分析、人工智能、深度学习、诊断、预后、手术规划等临床决策支持技术，而该论文完全属于基础细胞生物学和遗传学研究领域，未涉及任何医学影像、AI技术或临床决策支持相关内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Evidence is presented that loss of stemness plays an important role in MVA and results in a reduced number of neurons and glial cells, and overexpression of Radical Oxygen Species scavengers, mitochondria chaperones and apoptosis inhibition are identified as genetic interventions capable of dampening the deleterious effects of aneuploidy on brain size.

!!! tip deepseek-chat TL;DR

    该研究使用果蝇模型揭示了染色体不稳定性导致小头畸形的机制，发现蛋白质稳态失败和线粒体功能障碍是复杂非整倍体损害神经干细胞干性的关键因素，并确定了通过抗氧化剂、线粒体伴侣蛋白和抑制凋亡可以减轻这种有害影响。

<details open>
<summary>摘要翻译</summary>

> 嵌合型杂色非整倍体（Mosaic variegated aneuploidy, MVA）是一种导致小头畸形的罕见人类先天性疾病，其特征为广泛的染色体数目异常，其病因源于参与精确有丝分裂染色体分离的基因发生突变。为阐明该疾病的细胞机制，本研究通过特异性敲低神经干细胞（neural stem cell, NSC）区室中单个纺锤体组装检查点（spindle assembly checkpoint, SAC）基因，构建了一种小头畸形果蝇模型。我们提供的证据表明，干细胞特性丧失——即神经干细胞身份与增殖能力受损——在MVA中起重要作用，并导致神经元和胶质细胞数量减少。研究发现，干细胞特性丧失源于随时间积累的、多条染色体增减失衡（而非染色体不稳定性直接诱导的DNA损伤或简单非整倍体产生）所导致。我们揭示了蛋白质稳态失衡和线粒体功能障碍在复杂非整倍体对干细胞特性（一种高能耗细胞状态）产生负面影响中的作用。通过遗传干预手段，如过表达活性氧清除剂、线粒体伴侣蛋白及抑制细胞凋亡，可减轻非整倍体对大脑尺寸的有害影响。嵌合型杂色非整倍体作为一种诱发小头畸形的罕见人类疾病，由高水平染色体不稳定性引起。作者在该疾病的果蝇模型中揭示了蛋白质稳态失衡与线粒体功能障碍的关键作用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Mosaic variegated aneuploidy (MVA), a rare human congenital disorder that causes microcephaly, is characterized by extensive abnormalities in chromosome number and results from mutations in genes involved in accurate mitotic chromosome segregation. To characterize the cellular mechanisms underlying this disease, here we generated a Drosophila model of microcephaly caused by the depletion of a single spindle assembly checkpoint (SAC) gene in the neural stem cell (NSC) compartment. We present evidence that loss of stemness - compromised identity and proliferative capacity of NSCs- plays an important role in MVA and results in a reduced number of neurons and glial cells. We show that loss of stemness arises from the accumulation over time of an unbalanced number of gains and losses of more than one chromosome, rather than a direct consequence of chromosomal instability-induced DNA damage or the production of simple aneuploidies. We unravel a contribution of proteostasis failure and mitochondrial dysfunction to the negative impact of complex aneuploidies on stemness, a highly energy demanding cellular state. We identify overexpression of Radical Oxygen Species scavengers, mitochondria chaperones and apoptosis inhibition as genetic interventions capable of dampening the deleterious effects of aneuploidy on brain size. Mosaic variegated aneuploidy, a rare human disease that induces microcephaly, is caused by high levels of chromosomal instability. Authors unravel a major contribution of proteostasis failure and mitochondria dysfunction in a Drosophila model of this disease.

</details>
<br>

**关键词**: mosaic variegated aneuploidy, microcephaly, chromosomal instability, proteostasis failure, mitochondrial dysfunction, neural stem cells, Drosophila model, aneuploidy

---

### 21. ❌ Exon inclusion signatures enable accurate estimation of splicing factor activity

**作者**: Miquel Anglada-Girotto, Carolina Segura-Morales, Daniel F. Moakley, Chaolin Zhang, Samuel Miravet-Verde, Andrea Califano, Luis Serrano
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-69642-3](https://doi.org/10.1038/s41467-026-69642-3)

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

**评分理由**: 论文研究的是RNA剪接因子活性估计方法，属于计算生物学/生物信息学领域，与医学影像分析、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像、基础模型医学影像等关键词完全无关。论文使用RNA-seq数据和网络分析方法，不涉及任何医学影像数据或技术。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种通过外显子包含特征来准确估计剪接因子活性的方法，并应用于癌症分析，发现了与患者生存和癌症特征相关的剪接程序。

<details open>
<summary>摘要翻译</summary>

> 剪接因子通过控制信使RNA中外显子的纳入，塑造转录组和蛋白质组的多样性。其催化活性受到多层级调控，使得单一组学测量难以确定哪些剪接因子是表型背后的驱动因素。本文提出，剪接因子活性（定义为剪接因子调控外显子纳入的能力）可以从外显子纳入特征的变化中进行估算。为验证这一假设，我们系统评估了构建剪接因子→外显子网络及估算剪接因子活性的方法。研究发现，将基于RNA-seq扰动构建的网络与VIPER（通过富集调控子分析进行蛋白质活性的虚拟推断）方法相结合，能准确捕捉受多调控层级影响的剪接因子活性。该方法将剪接因子调控整合为仅源自外显子纳入特征的单一评分，从而实现对异质性条件的功能性解读。作为概念验证，我们识别出反复出现的癌症剪接程序，揭示了传统方法遗漏的与致癌基因样及肿瘤抑制因子样剪接因子的关联。这些程序与患者生存率及关键癌症特征（起始、增殖和免疫逃逸）密切相关。总之，我们证明剪接因子活性可以从外显子纳入变化中准确估算，从而以最低数据需求实现对剪接调控的全面分析。剪接因子决定基因如何拼接成RNA，但其活性难以测量。本研究通过系统评估网络方法，证明外显子纳入特征可推断剪接因子活性，进而揭示与生存率和癌症特征相关的癌症程序。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Splicing factors control exon inclusion in messenger RNAs, shaping transcriptome and proteome diversity. Their catalytic activity is regulated by multiple layers, making single-omic measurements on their own fall short in identifying which splicing factors underlie a phenotype. Here, we posit that splicing factor activity, defined as a splicing factor’s ability to modulate exon inclusion, can be estimated from changes in exon inclusion signatures. To test this hypothesis, we benchmark methods for constructing splicing factor→exon networks and estimating splicing factor activity. We find that combining RNA-seq perturbation-based networks with VIPER (Virtual Inference of Protein Activity by Enriched Regulon analysis) accurately captures splicing factor activity as modulated by multiple regulatory layers. This approach integrates splicing factor regulation into a single score derived solely from exon inclusion signatures, allowing functional interpretation of heterogeneous conditions. As a proof of concept, we identify recurrent cancer splicing programs, revealing associations with oncogenic- and tumor suppressor-like splicing factors missed by conventional methods. These programs correlate with patient survival and key cancer hallmarks: initiation, proliferation, and immune evasion. Altogether, we show splicing factor activity can be accurately estimated from exon inclusion changes, enabling comprehensive analyses of splicing regulation with minimal data requirements. Splicing factors shape how genes are stitched into RNA, but their activity is hard to measure. Here, the authors benchmark network methods and show exon-inclusion signatures infer splicing factor activity, uncovering cancer programs linked to survival and hallmarks.

</details>
<br>

**关键词**: splicing factor activity, exon inclusion signatures, RNA-seq, VIPER, cancer splicing programs, patient survival, network analysis, transcriptome regulation

---

### 22. ❌ ctDNA and tumor-based biomarkers of giredestrant response in acelERA breast cancer

**作者**: Ann Collier, Stephanie Hilz, Alejandro Chibly, Chunzhe Duan, Lincoln W. Pasquina, Xiaopeng Sun, Mariana Chavez-MacGregor, Aditya Bardia, Miguel Martín, Elgene Lim, Joohyuk Sohn, Pablo Diego Pérez-Moreno, Tharu M. Fernando, Heather M. Moore
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70335-0](https://doi.org/10.1038/s41467-026-70335-0)

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

**评分理由**: 论文研究的是乳腺癌内分泌治疗反应的生物标志物分析，主要涉及ctDNA基因组学、肿瘤ER转录活性和液体活检，完全不涉及医学影像分析、分割、深度学习、AI诊断、预后预测、手术规划、多模态成像或基础模型等关键词。所有关键词与论文内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is found that following first-line therapy, the ctDNA genomic landscape is diverse and influenced by CDK4/6 inhibitor exposure, and ER activity in ESR1-mutant tumors remains comparable to early breast cancer but is reduced in most non-mutant cases.

!!! tip deepseek-chat TL;DR

    该研究通过分析ctDNA基因组学和肿瘤ER转录活性，确定了能够有效分层预测乳腺癌患者对内分泌治疗（包括giredestrant）反应的生物标志物，为个性化治疗提供了框架。

<details open>
<summary>摘要翻译</summary>

> 摘要 雌激素受体阳性（ER+）晚期乳腺癌的内分泌治疗（ET）耐药常与ESR1突变相关，但不同突变亚型对口服选择性雌激素受体降解剂（SERD）的反应存在差异。通过对acelERA乳腺癌研究（NCT04576455）的生物标志物分析，我们发现肿瘤ER转录活性、循环肿瘤DNA（ctDNA）基因组学特征及其动态变化能有效分层预测包括giredestrant在内的ET疗效。研究发现，在一线治疗后，ctDNA基因组图谱呈现高度异质性，且受CDK4/6抑制剂暴露史影响。尽管存在这种复杂性，ESR1突变肿瘤的ER活性仍与早期乳腺癌相当，但在多数非突变病例中则有所降低。这种持续存在的ER活性与giredestrant的临床获益相关。此外，早期ctDNA清除可识别治疗应答者，而低ER活性与高ctDNA负荷的结合能预测快速临床进展。这些发现为通过整合液体活检与组织标志物来个性化制定未来乳腺癌治疗方案提供了理论框架。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Endocrine therapy (ET) resistance in estrogen receptor positive (ER+) advanced breast cancer is often linked to ESR1 mutations, yet responses to oral selective ER degraders vary within mutant subgroups. Through a biomarker analysis of acelERA Breast Cancer (NCT04576455), we show that tumor ER transcriptional activity as well as circulating tumor DNA (ctDNA) genomics and dynamics effectively stratify response to ET, including giredestrant. We find that following first-line therapy, the ctDNA genomic landscape is diverse and influenced by CDK4/6 inhibitor exposure. Despite this complexity, ER activity in ESR1 -mutant tumors remains comparable to early breast cancer but is reduced in most non-mutant cases. This maintained ER activity is associated with giredestrant benefit. Furthermore, early ctDNA clearance identifies responding patients, and the combination of low ER activity and high ctDNA burden predicts rapid clinical progression. These findings provide a framework for personalizing future breast cancer therapies by integrating liquid biopsies with tissue-based signatures.

</details>
<br>

**关键词**: breast cancer, endocrine therapy, ctDNA, ESR1 mutations, biomarkers, giredestrant, liquid biopsy, ER transcriptional activity

---

### 23. ❌ The REDD1–NF-κB–miRNAs–eNOS/SIRT1 axis mediates obesity-induced endothelial cell senescence and hypertension

**作者**: Yoon Kyung Choi, Dong-Keon Lee, Minsik Park, Junyoung Byeon, Woo-Young Nam, Tin Pou Lai, Kyu Nam Kim, Okhwa Kim, Sungwoo Ryoo, Jeong-Hyung Lee, Young-Guen Kwon, Ji‐Yoon Kim, Young-Myeong Kim
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70601-1](https://doi.org/10.1038/s41467-026-70601-1)

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

**评分理由**: 论文研究肥胖诱导的内皮细胞衰老和高血压的分子机制，聚焦于REDD1-NF-κB-miRNAs-eNOS/SIRT1信号轴，属于分子生物学、心血管疾病和代谢综合征领域。所有评分关键词均涉及医学影像分析、人工智能、深度学习、诊断、预后、手术规划、多模态成像和基础模型，但论文未涉及任何医学影像技术、AI算法或临床决策支持系统，完全属于基础生物医学研究，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Findings identify a REDD1-atypical NF-κB-miRNAs-eNOS/SIRT1 axis as a critical mediator of obesity-induced vascular dysfunction and a promising therapeutic target.

!!! tip deepseek-chat TL;DR

    该研究发现肥胖通过上调REDD1蛋白激活非典型NF-κB信号通路，诱导miR-155-5p和miR-214-3p表达，从而抑制eNOS和SIRT1，导致内皮细胞衰老和高血压，阻断该通路可改善肥胖小鼠的血管和肾功能。

<details open>
<summary>摘要翻译</summary>

> 血管功能障碍，包括内皮细胞（EC）衰老和高血压，是代谢综合征的典型特征，但其潜在机制尚不明确。本研究发现，代谢应激会上调发育与DNA损伤应答调节蛋白1（REDD1），从而驱动血管功能障碍。REDD1的过表达（而非无法激活非典型NF-κB的REDD1KK219/220AA突变体）通过NF-κB依赖性诱导miR-155-5p和miR-214-3p，促进内皮细胞衰老和高血压。这些微小RNA（miRNAs）在人和小鼠内皮细胞中抑制内皮型一氧化氮合酶（eNOS）和SIRT1的表达。在肥胖雄性小鼠中，REDD1和miR-214-3p表达上调，而eNOS和SIRT1表达下调，导致内皮细胞衰老、肾功能障碍和高血压。这一表型在缺失Redd1、内皮细胞特异性缺失Redd1或miR-214-3p的小鼠，以及表达Redd1KK219/220AA的小鼠中得到缓解，但通过IKKβ抑制仅能部分改善。这些发现确立了REDD1–非典型NF-κB–miRNAs–eNOS/SIRT1轴是肥胖诱导血管功能障碍的关键介导因子，也是一个有前景的治疗靶点。本研究表明，肥胖会增加应激蛋白REDD1，从而驱动血管老化和高血压。REDD1激活了一条非典型NF-κB信号通路及相关微小RNA，进而关闭保护血管的基因。阻断该通路可改善肥胖小鼠的血管和肾功能，这揭示了一个潜在的治疗靶点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Vascular dysfunction, including endothelial cell (EC) senescence and hypertension, is a hallmark of metabolic syndrome, yet its underlying mechanisms remain unclear. Here, we show that metabolic stress upregulates regulated in development and DNA damage response 1 (REDD1), driving vascular dysfunction. Overexpression of REDD1, but not the REDD1KK219/220AA mutant, which cannot activate atypical NF-κB, promotes EC senescence and hypertension through NF-κB-dependent induction of miR-155-5p and miR-214-3p. These miRNAs suppress endothelial nitric oxide synthase (eNOS) and SIRT1 expression in human and mouse ECs. In obese male mice, REDD1 and miR-214-3p are upregulated, whereas eNOS and SIRT1 are downregulated, contributing to EC senescence, renal dysfunction, and hypertension. This phenotype is alleviated in mice lacking Redd1, EC-specific Redd1, or miR-214-3p, and in mice expressing Redd1KK219/220AA, but only partially by IKKβ inhibition. These findings identify a REDD1–atypical NF-κB–miRNAs–eNOS/SIRT1 axis as a critical mediator of obesity-induced vascular dysfunction and a promising therapeutic target. This study found that obesity increases the stress protein REDD1, which drives vascular ageing and high blood pressure. REDD1 activates an atypical NF-κB signaling pathway and microRNAs that switch off genes protecting blood vessels. Blocking this pathway improves vascular and kidney function in obese mice, highlighting a potential therapeutic target.

</details>
<br>

**关键词**: REDD1, endothelial cell senescence, hypertension, obesity, NF-κB, miRNAs, eNOS/SIRT1, vascular dysfunction

---

### 24. ❌ Discovery and engineering of bacterial P450s for C-14 hydroxylation in ent-kaurane diterpenoids

**作者**: Xiaoxu Lin, Zhixi Xiao, Xingwang Xu, Xiaowei Zhang, Xingming Pan, Chenxi Zhu, Chenxi He, Li Feng, Fang-Ru Li, Hui-Min Xu, Zhe Wang, Ninghua Tan, Liao-Bin Dong
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70157-0](https://doi.org/10.1038/s41467-026-70157-0)

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

**评分理由**: 该论文研究的是利用计算化学方法（CHS策略）发现和改造细菌P450酶，用于天然产物ent-kaurane二萜的C-14羟基化修饰，属于合成生物学、酶工程和天然产物化学领域。论文内容完全不涉及医学影像分析、深度学习、疾病诊断、预后预测、手术规划、多模态医学影像或医学影像基础模型。所有关键词均与论文主题无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了ent-kaurane二萜类化合物C-14位羟基化修饰的难题，通过计算引导的策略发现并改造了细菌P450酶，显著提高了目标产物的产量，并获得了具有强细胞毒性的衍生物。

<details open>
<summary>摘要翻译</summary>

> 对映-贝壳杉烷二萜（*ent*-KTs）是一类结构多样的天然产物，以其抗肿瘤和抗炎生物活性而著称。C-14位羟基修饰对于增强其活性至关重要，然而引入该官能团仍是一个重大挑战。本研究提出了一种计算血红素引导的位点特异性（CHS）策略，用以鉴定三种可用于C-14羟基化的细菌P450酶（CYP260A1、CYP105N1和CYP154C5）。通过进一步的计算引导的酶工程和氧化还原伴侣筛选，获得了CYP260A1 L162V变体与CamA/CamB的组合，在大肠杆菌中实现了(14R,16R)-*ent*-贝壳杉-14,16-二醇（2）的产量提高了52倍，达到84.2 mg/L。底物范围测试揭示了影响反应活性的官能团。构效关系研究表明，C-14羟基与C15–C16迈克尔受体之间存在协同效应，从而产生了一个具有强细胞毒性（IC50HCT116 = 1.4 μM）的高效衍生物（27）。本研究展示了一个结合CHS引导的P450发现与计算酶工程的框架，以推进*ent*-KT的修饰。C-14羟基对于对映-贝壳杉烷二萜（*ent*-KTs）的功能至关重要。本文中，作者报告了用于*ent*-KTs C-14羟基化的细菌P450酶的发现与工程化改造。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> ent-Kaurane diterpenoids (ent-KTs) represent a structurally diverse class of natural products renowned for their antitumor and anti-inflammatory bioactivities. The C-14 hydroxyl modification is crucial for enhancing their potency; however, introducing this functional group remains a considerable challenge. Here, we present a computational heme-guided site-specific (CHS) strategy to identify three bacterial P450s (CYP260A1, CYP105N1, and CYP154C5) for C-14 hydroxylation. Further computationally guided enzyme engineering and redox partner screening identify the CYP260A1 L162V variant paired with CamA/CamB, achieving a 52-fold increase in production titer and a yield of 84.2 mg/L of (14R,16R)-ent-kauran-14,16-diol (2) in Escherichia coli. Substrate scope test reveals functional groups affecting reactivity. Structure-activity relationship studies demonstrate the synergistic effect between the C-14 hydroxyl and C15–C16 Michael acceptor, resulting in a potent derivative (27) with strong cytotoxicity (IC50HCT116 = 1.4 μM). This study demonstrates a framework combining CHS-guided P450 discovery and computational enzyme engineering to advance ent-KT modifications. C-14 hydroxyl group is critical for the function of ent-kaurane diterpenoids (ent-KTs). Here, the authors report discovery and engineering of bacterial P450s for C-14 hydroxylation in ent-KTs.

</details>
<br>

**关键词**: ent-kaurane diterpenoids, C-14 hydroxylation, bacterial P450s, computational enzyme engineering, CYP260A1, structure-activity relationship, cytotoxicity

---

### 25. ❌ Dual-metal-doped perovskite adsorbents for efficient removal of humic acid

**作者**: Lekai Zhao, Qiang Li, Shuang Han, Xiao Ma, Ming Zhou, Qiuyue Wang, Shasha Feng, Ze‐Xian Low, Zhaoxiang Zhong, Weihong Xing
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70286-6](https://doi.org/10.1038/s41467-026-70286-6)

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

**评分理由**: 论文研究的是用于水处理的钙钛矿吸附剂材料，主题为环境工程和材料科学，涉及双金属掺杂、吸附性能、再生能力等。所有评分关键词均属于医学影像分析和人工智能医疗领域，与论文内容完全无关。论文未涉及任何医学影像、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种钛/钴双金属掺杂的钙钛矿吸附剂，能够高效去除水中的腐殖酸，并通过磁性和Fenton活性设计实现了材料的易回收和原位再生。

<details open>
<summary>摘要翻译</summary>

> 腐植酸（Humic Acid, HA）作为一种天然物质的复杂有机化合物，其本身无害，但在水体氯化消毒过程中会形成具有致癌性的消毒副产物，如三卤甲烷和卤代乙酸，对水生生物及人类健康构成严重威胁。本研究提出一种B位双金属掺杂策略，用于制备铁磁性钙钛矿型吸附剂，以实现腐植酸的高效快速降解。钙钛矿氧化物（特别是LaFeO₃）因其独特的晶体结构、可调控性及固有的铁磁性被选为基体材料。通过在B位掺杂Ti和Co，我们构建了一种双功能钙钛矿吸附剂，该材料展现出快速的腐植酸吸附速率，吸附容量高达381 mg·g⁻¹，同时能够通过原位再生或磁性回收进行芬顿再生。计算模拟从分子层面揭示了钙钛矿吸附剂与腐植酸之间的相互作用机制。本研究结果凸显了钙钛矿材料作为高效、可再生有机化合物催化吸附剂的潜力，为其在可持续水修复应用中的发展开辟了道路。Ti/Co双掺杂LaFeO₃钙钛矿可快速去除水体中的腐植酸，其兼具磁性与芬顿活性的设计使其易于回收，并可通过H₂O₂实现快速原位再生，从而保障长期稳定的循环使用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Humic acid (HA), a complex organic compound of natural matter, is harmless on its own but can form carcinogenic disinfection byproducts, such as trihalomethanes and haloacetic acids, during water chlorination and disinfection processes, posing serious risks to aquatic organisms and human health. We present a B-site dual-metal-doping strategy to fabricate ferromagnetic perovskite-type adsorbents for rapid and efficient HA degradation. Perovskite oxides, specifically LaFeO3, were selected for their unique crystal structure, tunability, and inherent ferromagnetic properties. By doping Ti and Co at the B-site, we created a bifunctional perovskite absorbent that exhibits a rapid HA adsorption rate with a high adsorption capacity of 381 mg g-1, while also enabling regeneration in situ or magnetic recovery for Fenton regeneration. Computational simulations provide molecular-level insights into the interactions between the perovskite adsorbent and HA. Our findings reveal the potential of perovskite materials as highly effective, regenerable catalytic adsorbents for organic compounds, paving the way for their development in sustainable water remediation applications. Ti/Co dual-doped LaFeO₃ perovskite rapidly removes humic acid from water, and its magnetic, Fenton-active design enables easy recovery and quick in situ regeneration with H₂O₂ for stable long-term reuse.

</details>
<br>

**关键词**: perovskite adsorbent, humic acid removal, dual-metal doping, magnetic recovery, Fenton regeneration, water remediation, LaFeO3, adsorption capacity

---

### 26. ❌ Synthesis of monodisperse InSb colloidal quantum dots by monomer concentration control for short-wave infrared photodetectors

**作者**: Lucheng Peng, Miguel Dosil, Debranjan Mandal, Hao Wu, Aditya Malla, Gerasimos Konstantatos
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70367-6](https://doi.org/10.1038/s41467-026-70367-6)

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

**评分理由**: 该论文研究的是InSb胶体量子点的合成方法及其在短波红外光电探测器中的应用，属于材料科学、纳米技术和光电器件领域。论文内容完全不涉及医学图像分析、人工智能、疾病诊断、手术规划或任何医疗应用。所有关键词均与医学影像或临床决策支持相关，而本文专注于量子点材料合成和光电性能，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文开发了一种通过单体浓度控制合成单分散InSb胶体量子点的方法，实现了从950到1900 nm的可调谐窄尺寸分布和尖锐激子吸收峰，并基于此制备了在1500 nm和1580 nm波长处分别达到22%和19%外量子效率的短波红外光电探测器。

<details open>
<summary>摘要翻译</summary>

> 摘要：InSb胶体量子点兼具低体相带隙（0.17 eV）与大激子玻尔半径的特性，使其能在量子限域范围内实现短波红外波段的吸收，同时具备强共价键结合、互补金属氧化物半导体工艺兼容性以及符合有害物质限制标准的优势。然而，现有的一锅法与热注入法所制备的量子点存在尺寸分布宽、激子吸收弱的问题；连续注入法虽能改善光谱特性，但仅能制备小尺寸量子点（激子峰波长&lt;1.2 μm）。本研究提出一种单体浓度调控合成策略，可制备尺寸分布窄的InSb量子点，其激子吸收峰可调范围覆盖950至1900纳米，且展现出迄今最尖锐的激子吸收特征。其单分散特性使得重空穴-轻空穴分裂效应在吸收光谱中得以清晰显现。基于这些高质量纳米晶体，我们研制出短波红外光电探测器，在1500纳米和1580纳米波长处分别实现了22%和19%的外量子效率，拓展了III-V族胶体量子点光电探测器在该光谱范围的应用边界。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract InSb colloidal quantum dots combine a low bulk bandgap (0.17 eV) with a large exciton Bohr radius, enabling access to short-wave infrared wavelength within the quantum confinement regime, alongside strong covalent bonding, complementary metal-oxide semiconductor compatibility, and restriction of hazardous substances compliance. However, prior one-pot and hot-injection approaches yield broad size distributions and weak excitonic absorption, while continuous-injection methods improve spectral features but are restricted to small dot sizes (&lt;1.2 μm excitonic peaks). Here, we introduce a monomer-concentration-controlled approach that produces narrow-size-dispersed InSb quantum dots tunable from 950 to 1900 nm with the sharpest excitonic absorption peaks reported to date. Their monodisperse nature allowed the emergence of heavy hole-light hole splitting evident in their optical absorption spectra. Leveraging these high-quality nanocrystals, we demonstrate short-wave infrared photodetectors achieving external quantum efficiencies of 22% at 1500 nm and 19% at 1580 nm, extending the spectral reach of III-V colloidal quantum dot photodetectors at this wavelength range.

</details>
<br>

**关键词**: InSb colloidal quantum dots, monomer concentration control, monodisperse synthesis, short-wave infrared photodetectors, exciton absorption peaks, external quantum efficiency, III-V quantum dots, nanocrystal synthesis

---

### 27. ❌ Twist-induced orbital chirality in a photonic laser

**作者**: Kristina Frizyuk, Costantino De Angelis
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70408-0](https://doi.org/10.1038/s41467-026-70408-0)

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

**评分理由**: 论文《Twist-induced orbital chirality in a photonic laser》研究的是光子学领域，具体涉及扭曲双层光子膜结构、非厄米耦合和手性激光发射，属于物理光学和光子学范畴。所有评分关键词均围绕医学影像分析、人工智能医疗应用、疾病诊断/预后、手术规划等临床医学主题，与论文的光子学物理研究完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过将两个非手性光子膜组合成扭曲双层结构，打破了镜像对称性并诱导了反向旋转集体模式之间的非厄米耦合，从而实现了手性激光发射。

<details open>
<summary>摘要翻译</summary>

> 将两个非手性光子膜组合成扭转双层结构会打破镜面对称性，并诱导反向旋转集体模式之间的非厄米耦合，从而使激光发射产生手性特征。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The combination of two achiral photonic membranes into a twisted bilayer breaks mirror symmetry and induces non-Hermitian coupling between counter-rotating collective modes, making laser emission chiral.

</details>
<br>

**关键词**: photonic laser, twisted bilayer, mirror symmetry breaking, non-Hermitian coupling, chiral emission, collective modes, achiral photonic membranes

---

### 28. ❌ A Soft-Robotic Biomimetic Benchtop Model for Esophageal Motility Simulation

**作者**: Seán Kilroy, Neelesh A. Patankar, Walter W. Chan, Giovanni Traverso, Eoin D. O’Cearbhaill
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70260-2](https://doi.org/10.1038/s41467-026-70260-2)

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

**评分理由**: 论文标题和摘要描述了一种用于食管运动模拟的软机器人仿生台架模型，属于生物医学工程和医疗器械领域，与医学图像分析、深度学习、AI诊断、预后预测、手术规划、多模态成像或基础模型等关键词完全无关。论文未涉及任何医学图像处理或AI算法，而是专注于物理模拟装置的开发。

</details>
<br>

!!! info Semantic Scholar TL;DR

    RoboGullet is presented, a biomimetic soft-robotic model with independent localized longitudinal and circumferential muscle actuation, enabling, for the first time, simulation of both normal and diseased esophageal motility, advancing understanding of esophageal motility and its therapeutic interventions.

!!! tip deepseek-chat TL;DR

    该研究开发了一种软机器人仿生台架模型，用于模拟食管运动，以评估食管疾病诊断设备（如测压导管）的性能。

**关键词**: soft-robotic, biomimetic, benchtop model, esophageal motility, simulation, manometry catheter, esophageal disorders, diagnostic device

---

### 29. ❌ Retraction Note: NIR-light-mediated spatially selective triggering of anti-tumor immunity via upconversion nanoparticle-based immunodevices

**作者**: Hongqian Chu, Jian Zhao, Yongsheng Mi, Zhenghan Di, Lele Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70557-2](https://doi.org/10.1038/s41467-026-70557-2)

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

**评分理由**: 论文标题和摘要表明这是一篇关于近红外光介导的免疫治疗研究，涉及上转换纳米颗粒和抗肿瘤免疫，属于纳米医学和免疫治疗领域。所有评分关键词均聚焦于医学影像分析、深度学习、AI诊断、手术规划等方向，与论文内容无直接关联。论文未涉及医学影像处理、AI模型开发或临床决策支持系统。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究探讨了利用近红外光激活上转换纳米颗粒免疫装置实现空间选择性抗肿瘤免疫的方法，但论文已被撤稿。

**关键词**: NIR-light, upconversion nanoparticles, anti-tumor immunity, immunodevices, spatially selective triggering, retraction note

---

### 30. ❌ Conducting polymer-stabilized nanozymes alleviate sepsis-induced myocardial injury by inhibiting iron accumulation and lipid peroxidation

**作者**: Tingting Wu, Ying Liu, Wei Wang, Rong Sun, Yanyan Wang, Jiangpeng Pan, Jingfei Zhu, Kelong Fan, Qiuran Xu, Wei Jiang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70385-4](https://doi.org/10.1038/s41467-026-70385-4)

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

**评分理由**: 论文研究的是利用导电聚合物稳定的纳米酶通过抑制铁积累和脂质过氧化来减轻脓毒症引起的心肌损伤，属于生物材料、纳米医学和心血管疾病治疗领域。所有评分关键词均涉及医学影像分析、人工智能、深度学习、诊断预测、手术规划等方向，而该论文完全不涉及医学影像处理、AI算法或临床决策支持技术，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A library of conductive polypyrrole-polythiophene copolymer-stabilized nanozymes is developed by coordinating different metal ions within the copolymer framework, which provides a potential foundation for the development of therapeutic agents for severe cardiomyopathy and related conditions.

!!! tip deepseek-chat TL;DR

    该论文研究了导电聚合物稳定的纳米酶通过抑制铁积累和脂质过氧化来减轻脓毒症引起的心肌损伤，并验证了其治疗效果。

**关键词**: conducting polymer-stabilized nanozymes, sepsis-induced myocardial injury, iron accumulation, lipid peroxidation, myocardial protection, nanozyme therapy, cardiovascular disease

---

### 31. ❌ Cortical-limbic circuit dynamics of approach-avoidance conflict in humans

**作者**: Brooke R. Staveland, Julia Marie Oberschulte, Barbara Berger, Tamas Minarik, Olivia Kim McManus, Jon T. Willie, Peter Brunner, Mohammad Dastjerdi, Jack J. Lin, Elizabeth L. Johnson, Michelle Paff, Ming Hsu, Robert T. Knight
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70287-5](https://doi.org/10.1038/s41467-026-70287-5)

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

**评分理由**: 论文研究人类大脑皮层-边缘回路在趋避冲突决策中的神经机制，使用颅内脑电图（iEEG）记录和分析神经振荡活动。研究内容属于认知神经科学、神经生理学和决策神经科学领域，与医学影像分析、人工智能临床决策支持等关键词完全无关。论文未涉及任何医学影像（如CT、MRI、超声）的获取、处理、分割或分析，也未使用深度学习、AI诊断、预后预测、手术规划、多模态融合或基础模型等技术。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究使用颅内脑电图揭示了人类前额叶-边缘回路通过θ振荡和高频活动介导趋避冲突决策的神经机制。

<details open>
<summary>摘要翻译</summary>

> 摘要：在日常生活中，选择趋近或回避是常见行为，而过度回避是焦虑障碍的核心特征。本研究利用颅内脑电图技术，界定了一个支持趋近与回避行为的前额叶-边缘神经环路。术前癫痫患者（n = 20）完成了一项基于街机游戏《吃豆人》（Pac-Man）设计的趋避冲突决策任务，在该任务中患者需权衡获取奖励与遭受幽灵攻击导致的损失。研究发现，在趋近行为期间，包括海马体、杏仁核、眶额皮层和前扣带皮层在内的边缘环路θ波功率增强，而在回避行为期间该功率下降。该环路与外侧前额叶皮层之间的θ波连接性在趋近时增强，在回避时减弱。网络连接性可预测患者持续趋近的时间长度，增强的同步性会延长趋近时间。当面临迫近威胁时，该系统会切换至外侧前额叶皮层高频活动的持续增强状态。这些结果证明，一个由θ振荡和高频活动介导的分布式前额叶-边缘环路，构成了人类趋避冲突的神经基础。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Choosing to approach or avoid is common in everyday life and excessive avoidance is a cardinal feature of anxiety disorders. We use intracranial EEG to define a prefrontal-limbic circuit supporting approach and avoidance. Presurgical epilepsy patients (n = 20) performed an approach-avoidance conflict decision-making task inspired by the arcade game Pac-Man, where patients trade off rewards against losses from ghost attack. During approach, theta power increases across a limbic circuit including the hippocampus, amygdala, orbitofrontal cortex and anterior cingulate cortex, which drops during avoidance. Theta connectivity between this circuit and lateral prefrontal cortex increases during approach and falls during avoidance. Network connectivity tracks how long patients approach, with enhanced synchronicity extending approach times. During imminent threat, the system switches to sustained increase in high-frequency activity in the lateral prefrontal cortex. The results provide evidence of a distributed prefrontal-limbic circuit, mediated by theta oscillations and high frequency activity, underlying approach-avoidance conflict in humans.

</details>
<br>

**关键词**: approach-avoidance conflict, intracranial EEG, prefrontal-limbic circuit, theta oscillations, decision-making, epilepsy patients, neural connectivity, high-frequency activity

---

### 32. ❌ Impaired $$\alpha$$-Synuclein aggregate clearance in neuronal cells drive their spread to microglia through tunneling nanotubes

**作者**: Ranabir Chakraborty, Francesca Palese, Philippa Samella, Veronica Testa, Jara Montero-Muñoz, Sylvie Syan, Takashi Nonaka, Masato Hasegawa, Antonella Consiglio, Chiara Zurzolo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-69930-y](https://doi.org/10.1038/s41467-026-69930-y)

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

**评分理由**: 论文研究的是细胞生物学和神经退行性疾病机制，具体探讨α-突触核蛋白聚集体通过隧道纳米管在神经元和小胶质细胞间的转移机制，以及自噬功能障碍在此过程中的作用。所有评分关键词均涉及医学影像分析、人工智能在医疗影像中的应用、疾病诊断/预后、手术规划等临床技术领域，而该论文完全属于基础细胞生物学研究，未涉及任何医学影像技术、AI模型、临床诊断或手术相关内容，因此所有关键词相关度均为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Dysfunctional autophagy in neurons as a key driver outsourcing α-Syn aggregates to microglia is highlighted, and perturbing aggregate clearance via autophagy inhibition enhances TNT-mediated transfer of α-Syn from neuronal cells to microglia.

!!! tip deepseek-chat TL;DR

    该研究发现神经元自噬功能障碍导致α-突触核蛋白聚集体清除受损，从而通过隧道纳米管将这些聚集体转移至自噬能力更强的小胶质细胞进行降解。

<details open>
<summary>摘要翻译</summary>

> 摘要 隧道纳米管（Tunneling Nanotubes, TNTs）在细胞间通讯中发挥着关键作用，能够在相互连接的细胞间长距离运输分子货物。先前研究已证明，α-突触核蛋白（α-Synuclein, α-Syn）聚集体能够高效、定向地从神经元转移至小胶质细胞，而内体运输和溶酶体处理被确定为α-Syn内化后的主要事件。通过使用人类神经元和小胶质细胞系，我们发现小胶质细胞表现出更高的溶酶体周转率，尤其是通过溶酶体自噬（lysophagy）；相反，在暴露于α-Syn后，神经元溶酶体的降解能力受损，自噬流也发生障碍，导致聚集体清除能力下降。这种对α-Syn聚集体的反应在人类诱导多能干细胞（iPSC）分化的神经元和小胶质细胞中同样存在。此外，通过抑制自噬来干扰聚集体清除，会增强TNT介导的α-Syn从神经元细胞向小胶质细胞的转移。与含有α-Syn的神经元共培养的小胶质细胞会上调自噬流，从而有效降解转移而来的聚集体。这些结果突显了神经元自噬功能失调是促使α-Syn聚集体外排至小胶质细胞的关键驱动因素。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Tunneling nanotubes (TNTs) play a crucial role in intercellular communication, enabling transfer of molecular cargoes over long distances between connected cells. Previous studies have demonstrated efficient, directional transfer of $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Synuclein ( $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Syn) aggregates from neurons to microglia, with endosomal trafficking and lysosomal processing identified as the primary events following $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Syn internalization. Using human neuronal and microglial cell lines, we show that microglia exhibit higher lysosomal turnover, particularly through lysophagy, whereas neuronal lysosomes display compromised degradative capacity and impaired autophagic flux upon $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Syn exposure, resulting in compromised aggregate clearance. Such a response to $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Syn aggregates is also conserved in human iPSC-derived neurons and microglia. Moreover, perturbing aggregate clearance via autophagy inhibition enhances TNT-mediated transfer of $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Syn from neuronal cells to microglia. Microglia co-cultured with $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Syn-containing neurons upregulate autophagy flux, enabling efficient degradation of the transferred aggregates. These results highlight dysfunctional autophagy in neurons as a key driver outsourcing $$\alpha$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:mi>α</mml:mi> </mml:math> -Syn aggregates to microglia.

</details>
<br>

**关键词**: α-synuclein aggregates, tunneling nanotubes, neuronal autophagy dysfunction, microglial clearance, lysosomal degradation, intercellular transfer, neurodegenerative disease, cell-to-cell communication

---

### 33. ❌ XA-Novo: high-throughput mass spectrometry-based de novo sequencing technology for monoclonal antibodies and antibody mixtures

**作者**: Yueting Xiong, Wenbin Jiang, Jin Xiao, Qingfang Bu, Jingyi Wang, Zhenjian Jiang, Ling Luo, Xiaoqing Chen, Yijie Qiu, Yangtao Wu, Fan Liu, Rongshan Yu, Ningshao Xia, Quan Yuan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70496-y](https://doi.org/10.1038/s41467-026-70496-y)

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

**评分理由**: 论文XA-Novo专注于质谱抗体测序技术，研究领域为蛋白质组学、抗体工程和药物发现。论文内容涉及质谱数据解析、抗体序列重建和功能验证，与评审要求的医学影像分析、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像、基础模型医学影像等关键词完全无关。所有关键词评分为0分，因为论文研究的是抗体测序的生物信息学方法，而非医学影像或临床决策支持系统。

</details>
<br>

!!! info Semantic Scholar TL;DR

    XA-Novo is presented, an accurate and high-throughput de novo sequencing solution that integrates a single-pot multi-enzymatic gradient digestion method with a beam search-based assembler (Fusion) to reconstruct full-length antibody sequences directly from bottom-up mass spectrometry data.

!!! tip deepseek-chat TL;DR

    该论文开发了XA-Novo质谱从头测序技术，解决了抗体序列重建的技术难题，实现了高精度、高通量的抗体测序，并验证了其功能等效性，加速了抗体研究和药物开发。

<details open>
<summary>摘要翻译</summary>

> 基于质谱的从头测序技术对抗体序列的解析至关重要，但其仍面临技术挑战。本文提出XA-Novo——一种准确且高通量的从头测序解决方案，该方法将单管多酶梯度消化策略与基于束搜索的序列组装算法（Fusion）相结合，能够直接从自下而上的质谱数据中重建全长抗体序列。通过对多种来源的已知特征抗体进行基准测试，证明XA-Novo在鉴定灵敏度、序列完整性和重建准确性方面均优于商业解决方案。此外，XA-Novo成功重建了六种序列未知的免疫治疗抗体，体外/体内实验验证了这些生成的抗体表现出与商业对应物同等的功能。更重要的是，在区分混合的COVID-19中和抗体时，XA-Novo实现了超过99.54%的准确序列覆盖率，其性能超越了目前报道的针对单一抗体测序的组装工具。总体而言，XA-Novo建立了一个可靠、可扩展且广泛适用的标准化抗体测序工作流程，从而加速基础抗体研究及治疗性抗体开发。XA-Novo是一种仅依赖质谱的从头抗体测序流程，可从单一样本或混合物中重建全长抗体，为抗体研究和药物发现实现了快速的序列恢复与功能性重表达。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Elucidating antibody sequences by mass spectrometry-based de novo sequencing is essential but remains technically challenging. Here we present XA-Novo, an accurate and high-throughput de novo sequencing solution that integrates a single-pot multi-enzymatic gradient digestion method with a beam search-based assembler (Fusion) to reconstruct full-length antibody sequences directly from bottom-up mass spectrometry data. Benchmarking across well-characterized antibodies from multiple species demonstrates that XA-Novo outperforms commercial solutions in identification sensitivity, sequence completeness, and reconstruction accuracy. Furthermore, XA-Novo successfully reconstructs six immunotherapeutic antibodies with unknown sequences, and in vitro/vivo assays validate that these generated antibodies exhibit functionality equivalent to their commercial counterparts. Moreover, XA-Novo achieves over 99.54% accurate sequence coverage in distinguishing mixed COVID-19 neutralizing antibodies, exceeding the performance of current assemblers reported for single-antibody sequencing. Overall, XA-Novo establishes a reliable, scalable, and broadly applicable workflow for routine antibody sequencing, thereby accelerating both fundamental antibody research and therapeutic antibody development. XA-Novo is a mass spectrometry–only de novo antibody sequencing workflow that reconstructs full-length antibodies from single samples or mixtures, enabling rapid sequence recovery and functional re-expression for antibody research and drug discovery.

</details>
<br>

**关键词**: de novo sequencing, mass spectrometry, antibody sequencing, monoclonal antibodies, beam search assembler, COVID-19 neutralizing antibodies, therapeutic antibody development, high-throughput workflow

---

### 34. ❌ Design of miniprotein inhibitors targeting complement C9 to block membrane attack complex assembly

**作者**: Min Li, Ningning Wang, Xiaoyan Fu, Gege Wei, Ze Zhang, Yanghan Yu, Tianshui Xue, Yifei Zhao, Jinheng Pan, Dongfeng WANG, Meifang Liu, Y. Li, Jinbao Tang, Longxing Cao, Zhaocheng Jian, Shujuan Liang, Bowen Yu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70667-x](https://doi.org/10.1038/s41467-026-70667-x)

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

**评分理由**: 论文研究的是利用深度学习设计靶向补体C9的微型蛋白抑制剂来阻断膜攻击复合物组装，属于计算生物学、蛋白质工程和免疫治疗领域。虽然使用了深度学习方法，但所有评分关键词都聚焦于医学影像分析（CT/MRI/超声影像处理、分割、诊断、预后、手术规划等），而本文完全不涉及医学影像数据或应用。论文内容与医学影像分析领域无直接关联，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An in vivo acute hemolysis inhibition assay reveals that the C9 mini-protein inhibitors remain effective against hemolysis even 8 minutes after complement activation, outperforming the complement C5 inhibitor eculizumab.

!!! tip deepseek-chat TL;DR

    该研究利用深度学习从头设计靶向补体C9的微型蛋白抑制剂，成功阻断膜攻击复合物组装，并在体内实验中显示出优于现有药物的溶血抑制效果，为补体异常激活相关疾病提供了新的治疗策略。

<details open>
<summary>摘要翻译</summary>

> 膜攻击复合物（MAC）的异常形成与一系列急慢性免疫疾病存在内在关联。补体C9插入细胞膜是MAC形成的最终步骤及动力学瓶颈。然而，目前针对阻断C9形成MAC的研究仍较为有限。鉴于其宽阔、平坦且极性的功能界面，补体C9成为理性药物设计中极具挑战性的靶点。本研究采用基于深度学习的蛋白质支架生成、序列设计与复合物结构预测方法，从头设计了能够特异性阻断可溶性补体C9膜插入的微型蛋白抑制剂。通过部分扩散策略，将微型蛋白抑制剂的结合亲和力进一步优化至700 pM。利用X射线晶体学与生物化学研究验证了设计的准确性及结合特异性。体内急性溶血抑制实验表明，即使在补体激活8分钟后，C9微型蛋白抑制剂仍能有效抑制溶血，其效果优于补体C5抑制剂依库珠单抗。这种从头设计的C9微型蛋白抑制剂可为预防和治疗与补体异常激活相关的急性或慢性免疫疾病提供一种潜在的治疗策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The abnormal formation of the membrane attack complex (MAC) is intrinsically linked to a range of acute and chronic immune diseases. The insertion of complement C9 into the membrane is the final step and kinetic bottleneck of MAC formation. However, research on blocking the MAC formation of C9 is currently limited. Given its broad, flat, and polar functional interface, complement C9 is a challenging target for rational design. Here, we utilize deep learning-based methods for protein scaffold generation, sequence design, and complex structure prediction to de novo design mini-protein inhibitors that specifically block the membrane insertion of soluble complement C9. The binding affinity of the mini-protein inhibitor is further optimized to 700 pM via partial diffusion. Design accuracy and binding specificity are verified through X-ray crystallography and biochemical studies. An in vivo acute hemolysis inhibition assay reveals that the C9 mini-protein inhibitors remain effective against hemolysis even 8 minutes after complement activation, outperforming the complement C5 inhibitor eculizumab. The de novo designed C9 mini-protein inhibitors can offer an optional therapeutic approach for the prevention and treatment of acute or chronic immune diseases associated with abnormal complement activation.

</details>
<br>

**关键词**: membrane attack complex, complement C9, miniprotein inhibitors, deep learning design, protein engineering, acute hemolysis inhibition, immune diseases, therapeutic approach

---

### 35. ❌ Chiral orbital lasing in a twisted bilayer metasurface

**作者**: Mingjin Wang, Ning Lv, Zixuan Zhang, Ye Chen, Jiahao Si, Jingxuan Chen, C. G. Tang, Xuefan Yin, Zhen Liu, Dongxu Xin, Zhaozheng Yi, Wanhua Zheng, Yuri Kivshar, Chao Peng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-69665-w](https://doi.org/10.1038/s41467-026-69665-w)

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

**评分理由**: 论文研究的是光子学领域的扭曲双层超表面中的手性轨道激光现象，属于物理光学和纳米光子学范畴。所有评分关键词均针对医学影像分析和临床AI应用，而论文内容完全不涉及医学影像、疾病诊断、手术规划或医疗AI模型。论文摘要中提到的"diagnostics"是指光学诊断技术的一般应用潜力，并非特指医学诊断。因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过设计和制造扭曲双层半导体超表面结构，实现了基于轨道角动量的手性轨道激光，并验证了其在宽光谱范围内的单模激光发射特性。

<details open>
<summary>摘要翻译</summary>

> 摘要 手性是物理学中的基本概念，是非线性光学、量子物理和拓扑光子学中诸多现象的核心。光子携带自旋角动量时具有本征手性，而当光子与镜面对称性破缺的结构相互作用时，轨道角动量可诱导出手性。本文中，我们通过利用扭曲双层光子结构的固有结构手性，观测到其产生的轨道手性激光。我们设计并制备了一种由两个半导体薄膜超表面构成的莫尔型光学结构。通过对扭曲双层结构进行光学泵浦，我们在250纳米的宽光谱范围内实现了单模激光发射。该激光发射展现出轨道手性特征，其源于顺时针与逆时针旋转的集体导模共振之间的螺旋与非厄米耦合，这一特性通过偏振分辨成像与自干涉测量得以验证。从扭曲光子结构中观测到的轨道手性激光，可推动手性光在诊断、光学操控及光通信等领域的多样化应用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Chirality is a fundamental concept in physics, core to many phenomena in nonlinear optics, quantum physics and topological photonics. Photons are intrinsically chiral when carrying spin angular momentum, whereas orbital angular momentum can induce chirality when photons interact with structures with broken mirror symmetry. Here, we observe orbital chiral lasing from a twisted bilayer photonic structure, by leveraging its inherent structural chirality. We design and fabricate a Moiré-type optical structure consisting of two semiconductor membrane metasurfaces. By optically pumping the twisted bilayer, we achieve single-mode lasing over a broad spectral range of 250 nm. The lasing emission exhibits chiral orbital characteristics, arising from helical and non-Hermitian couplings between collective guided resonances rotating clockwise and counterclockwise and confirmed by polarization-resolved imaging and self-interference measurements. The observed chiral orbital lasing from a twisted photonic structure can contribute to diverse applications of chiral light in diagnostics, optical manipulation and communication with light.

</details>
<br>

**关键词**: chiral lasing, orbital angular momentum, twisted bilayer metasurface, Moiré structure, photonic structure, non-Hermitian coupling, guided resonances, polarization-resolved imaging

---

### 36. ❌ Global error signal guides local optimization in mismatch calculation

**作者**: John Hongyu Meng, Xiao-Jing Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70354-x](https://doi.org/10.1038/s41467-026-70354-x)

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

**评分理由**: 论文标题和摘要未提供，无法评估论文内容与给定关键词的相关性。所有关键词均基于医学影像分析、人工智能临床决策支持等主题，但缺乏论文信息，无法判断任何相关性，因此所有关键词评分为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work shows that the network model, endowed with both positive and negative prediction error neurons, accounts for the salient physiological observations of motor-visual and motor-auditory mismatch responses in mice, and predicts how disrupting inhibition impairs mismatch computation in specific ways.

!!! tip deepseek-chat TL;DR

    无法总结，因为论文摘要未提供。

---

### 37. ❌ Urban forestry for cooler cities faces three critical hurdles

**作者**: Thami Croeser, Mohammad Matiur Rahman, Arnab K. Ghosh
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70723-6](https://doi.org/10.1038/s41467-026-70723-6)

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

**评分理由**: 论文研究城市林业（城市树木）对缓解城市热岛效应的作用，属于城市规划、环境科学和城市生态学领域。所有评分关键词均涉及医学影像分析、人工智能在医疗诊断/预后/手术规划中的应用，与论文主题完全无关。论文未涉及任何医学影像、深度学习、AI诊断或医疗相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了城市树木在热适应中常因树木不健康、种植密度不足和过早移除而未能有效降温的问题，并提出了三个关键前提条件。

<details open>
<summary>摘要翻译</summary>

> 城市树木能够保护居民免受极端高温影响，但植树项目很少在最需要遮荫的区域提供足够的树冠覆盖。我们综合相关证据，指出在热适应中有效利用树木的三个鲜少被满足的前提条件。城市森林是应对高温的关键工具，但其实际效能往往因以下三个原因未能充分发挥：树木必须保持健康（避免缺水或土壤条件限制），需进行高密度种植，并需精心保护以防止过早移除，方能在城市环境中实现有效的降温效果。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Urban trees can protect city residents from extreme heat, but tree planting programs seldom provide sufficient shade where it is most needed. We synthesize evidence highlighting three rarely fulfilled prerequisites for the effective use of trees in heat adaptation. Urban forests are a critical tool for heat adaptation, but often underperform for three reasons. Trees must be healthy (not thirsty or soil-constrained), densely planted, and carefully protected from premature removal to deliver effective cooling in urban settings.

</details>
<br>

**关键词**: urban forestry, urban trees, heat adaptation, cooling, tree planting, urban heat, shade, urban forests

---

### 38. ❌ Quantitative corrosion framework for anti-corrosive passivation design to extend calendar life in lithium metal batteries

**作者**: Song Kyu Kang, Seochan Hong, Minho Kim, Jae-Hong Lim, Minguk Kwak, Jong-Heon Lim, Nayeon Kim, Sehun Choi, Yeji Park, Kyu-Young Park, Won Bae Kim
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70585-y](https://doi.org/10.1038/s41467-026-70585-y)

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

**评分理由**: 论文研究的是锂金属电池的腐蚀机制和抗腐蚀钝化层设计，属于材料科学和电化学领域，与医学图像分析、人工智能临床决策支持等医疗领域完全无关。所有关键词均涉及医疗影像、疾病诊断、手术规划等医疗应用，而本文专注于电池材料、腐蚀动力学、电化学性能等，两者研究领域完全不同，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究针对锂金属电池中锂腐蚀导致日历寿命缩短的问题，提出了一个定量腐蚀框架，并设计了一种双层抗腐蚀钝化层，显著提升了电池的高倍率性能和循环稳定性。

<details open>
<summary>摘要翻译</summary>

> 活性锂金属易发生腐蚀，这严重限制了其在储能领域的日历寿命和实用性。尽管腐蚀引发的性能衰减至关重要，但目前对其认知仍主要停留在定性层面，缺乏清晰的机理理解。本文提出了一个定量集成且经实验验证的框架，该框架将锂腐蚀与界面相生长动力学及界面形貌演化相关联。在此模型指导下，我们合理设计了一种由嵌入锂银合金-氟化物界面相的聚丙烯酸锂构成的双层抗腐蚀钝化层。外层富含聚合物的层可抵抗溶胀并阻挡腐蚀，而底层的富LiAg/LiF界面相则增强了界面传输动力学。原位X射线显微成像揭示，日历老化后的锂区域特别容易发生加速腐蚀，这会加剧枝晶形成，而该钝化层能有效抑制此过程。因此，全电池在10 C（6分钟）倍率下表现出133 mAh g−1的高倍率容量，并在0.5 C（120分钟）下循环400次后仍保持74.6%的容量，库仑效率高于99.9%。在用于日历寿命评估的四小时静置协议下，全电池在200次循环后仍保持75.1%的容量，进一步的软包电池测试显示在640次循环后容量保持率为85.5%。本研究为理解腐蚀动力学提供了见解，并为设计提升锂金属电池日历寿命的钝化策略提供了指导。活性锂金属易腐蚀，但其行为目前主要被定性理解，机理认识有限。本文作者提出了一个将锂腐蚀与界面相生长及形貌演化相联系的定量框架，并以此指导了双层钝化层的设计策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Reactive lithium metal renders it prone to corrosion, which severely limits calendar life and practicality in energy storage. Despite its importance, corrosion-induced degradation remains largely qualitative and lacks a clear mechanistic understanding. Here, we present a quantitatively integrated and experimentally validated framework that correlates lithium corrosion with interphase growth kinetics and interfacial morphological evolution. Guided by this model, a bi-layered anti-corrosive passivation layer composed of lithium polyacrylate embedded with lithium silver alloy-fluoride interphase is rationally designed. The outer polymer-rich layer resists swelling and blocks corrosion, while the underlying LiAg/LiF-rich interphase enhances interfacial transport kinetics. Operando X-ray microscopy reveals that calendar-aged lithium regions are particularly vulnerable to accelerated corrosion, which intensifies dendritic formation and is effectively suppressed by the passivation layer. Consequently, full-cells show a high-rate capacity of 133 mAh g−1 at 10 C (6 min) and retain 74.6% capacity after 400 cycles at 0.5 C (120 min), with Coulombic efficiency above 99.9%. Under a four-hour rest protocol for calendar life evaluation, full-cells maintain 75.1% capacity after 200 cycles, and further pouch cell testing shows 85.5% capacity after 640 cycles. This study offers insights into corrosion dynamics and informs the design of passivation strategies for improving calendar life in lithium metal batteries. Reactive lithium metal readily corrodes, but its behavior is mainly understood qualitatively with limited mechanistic insight. Here, authors present a quantitative framework linking lithium corrosion to interphase growth and morphology evolution, guiding a bi-layered passivation design strategy.

</details>
<br>

**关键词**: lithium metal batteries, corrosion, passivation layer, calendar life, interphase growth, electrochemical performance, operando X-ray microscopy

---

### 39. ❌ Elucidating genetic backgrounds of myasthenia gravis in Japanese by genome-wide association studies and multi-omics analyses of thymoma

**作者**: Hiroyuki Ueda, Tomoya Kubota, Risa Goto, Akari Suzuki, Takafumi Ojima, Kotaro Ogawa, Kyuto Sonehara, Shinichi Namba, Tatsuhiko Naito, Qingbo Wang, Shingo Konno, Makoto Samukawa, Naoki Kawaguchi, Takashi Kimura, Takamichi Sugimoto, Hiroyuki Murai, Takemori Yamawaki, Kenichi Kaida, Daiki Tokuyasu, Manato Yasuda
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70376-5](https://doi.org/10.1038/s41467-026-70376-5)

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

**评分理由**: 论文研究重症肌无力的遗传背景，通过全基因组关联研究、多组学分析和单细胞转录组学等方法，属于遗传学、免疫学和基因组学领域。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等，与论文内容完全无关，因此所有关键词评分为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The study unveils genetics of MG distinctly across disease subtypes, and involvement of TERT in its pathogenesis, and pleiotropic effects on lung cancer, hematological traits, and telomere length are identified.

!!! tip deepseek-chat TL;DR

    本研究通过全基因组关联研究和多组学分析揭示了日本人群重症肌无力的遗传背景，发现了TERT基因座与疾病风险和治疗反应的相关性，并识别了不同亚型中HLA基因的特定关联。

<details open>
<summary>摘要翻译</summary>

> 重症肌无力（MG）是一种以神经肌肉传递障碍和运动症状为特征的自身免疫性疾病。其遗传背景尚不明确，尤其是在欧洲人群已报道的特定亚型之外。本研究对涵盖所有疾病亚型的1,434例日本MG患者和42,913例对照进行了全基因组关联分析（GWAS），新发现了TERT基因座与MG的关联（比值比[OR] = 1.31，P = 1.7×10-10）。亚型分层GWAS显示，该信号在全身型MG（gMG；OR = 1.38，P = 1.6×10-12）、抗乙酰胆碱受体抗体阳性全身型MG（g-AChR-Ab(+)MG；OR = 1.49，P = 2.1×10-15）以及胸腺瘤相关全身型MG（g-TAMG；OR = 1.92，P = 1.1×10-15）中更为显著。对主要组织相容性复合体（MHC）区域的精细定位揭示了HLA-DRB1与晚发型全身型MG（g-LOMG）以及HLA-A与早发型全身型MG（g-EOMG）的不同关联。MG风险相关的TERT先导变异rs2736099与较差的治疗反应相关，尤其是在g-AChR-Ab(+)MG和g-EOMG中（P < 0.0042）。基于生物样本库的表型组全关联分析发现该变异对肺癌、血液学特征和端粒长度存在多效性影响。单细胞转录组学和免疫组织化学分析在胸腺瘤样本中发现了未成熟淋巴细胞特异性的TERT表达。全长转录组学分析揭示了rs2736099-A等位基因对TERT表达的等位特异性降低效应。我们的研究揭示了MG遗传学特征在不同疾病亚型间的差异，并阐明了TERT在其发病机制中的作用。重症肌无力是一种以神经肌肉传递障碍为特征的自身免疫性疾病。其遗传背景尚不明确，尤其是在欧洲人群已报道的特定亚型之外。本研究作者在一个日本队列中对涵盖所有疾病亚型的MG进行了全基因组关联分析。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Myasthenia gravis (MG) is an autoimmune disorder characterized by impaired neuromuscular transmission and motor symptoms. Its genetic background remains unclear, particularly beyond specific subtypes reported in European populations. Here, we perform a genome-wide association study (GWAS) of 1,434 MG cases covering all disease subtypes and 42,913 controls of Japanese, which newly identify the TERT locus (odds ratio [OR] = 1.31, P = 1.7×10-10). Subtype-stratified GWASs show stronger signals for generalized MG (gMG; OR = 1.38, P = 1.6×10-12), anti AChR antibody-positive gMG (g-AChR-Ab(+)MG; OR= 1.49, P = 2.1×10-15), and thymoma-associated gMG (g-TAMG; OR = 1.92, P = 1.1×10-15). Fine-mapping of the major histocompatibility complex region reveal distinct associations of HLA-DRB1 with late onset gMG (g-LOMG) and HLA-A with early onset gMG (g-EOMG). The MG risk TERT lead variant rs2736099 is associated with poor treatment response, especially in g-AChR-Ab(+)MG and g-EOMG (P < 0.0042). The biobank-based phenome-wide association study identify pleiotropic effects on lung cancer, hematological traits, and telomere length. Single cell transcriptomics and immunohistochemistry identified immature lymphocyte-specific TERT expression in thymoma specimens. Full-length transcriptomics reveal allele-specific decreasing effect of rs2736099-A on TERT expression. Our study unveils genetics of MG distinctly across disease subtypes, and involvement of TERT in its pathogenesis. Myasthenia gravis is an autoimmune disorder characterized by impaired neuromuscular transmission. Its genetic background remains unclear, particularly beyond specific subtypes reported in European populations. Here the authors perform a genome-wide association study covering all disease subtypes in a Japanese cohort.

</details>
<br>

**关键词**: myasthenia gravis, genome-wide association study, TERT, HLA, thymoma, Japanese population, multi-omics analysis, single cell transcriptomics

---

### 40. ❌ Microgravity-activated high-performance van der Waals InSe ferroelectric semiconductor

**作者**: Rong Jin, Fengrui Sui, Yilun Yu, Beituo Liu, Min Jin, Xuechao Liu, Jiawen Dai, Yufan Zheng, Shujing Jia, Ruijuan Qi, Fangyu Yue, Junhao Chu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70520-1](https://doi.org/10.1038/s41467-026-70520-1)

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

**评分理由**: 论文研究微重力环境下生长的范德华InSe铁电半导体材料的晶体结构、电学和光学性能，属于材料科学、凝聚态物理和半导体器件领域。所有评分关键词均涉及医学影像分析、人工智能辅助临床决策等医疗应用，与论文的物理材料研究主题完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了在中国空间站微重力环境下生长的范德华InSe半导体材料，发现微重力条件消除了层间堆垛缺陷，激活了其本征滑动铁电性，并显著提升了其作为场效应晶体管和非线性近红外光源的性能。

<details open>
<summary>摘要翻译</summary>

> 地球难以复现的空间微重力环境被认为对晶体生长具有积极影响，尤其对层间滑动能垒较低的范德华层状材料而言。本研究对中国空间站微重力环境下培育的范德华InSe半导体进行了结构与光电性能分析。原子级微观结构分析表明，该独特环境能有效消除柔性InSe晶体中天然存在的堆垛层错，直接激活其本征滑动铁电性并展现出优异的保持稳定性。据此制备的铁电半导体场效应晶体管呈现出显著的非易失性存储窗口、高开关比和卓越的载流子迁移率。更重要的是，该材料还能实现优异的放大自发辐射，为近红外非线性光源提供极低的光子激发阈值。这些发现不仅为制备InSe等高质量范德华层状单晶提供了非常规策略，更凸显了其在融合存储与传感功能的下一代发射器集成计算架构中的潜力。本研究聚焦于中国空间站生长的范德华InSe晶体，证实微重力生长条件可消除InSe层间堆垛缺陷，激活其本征滑动铁电性并增强超线性发射特性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The space microgravity environment, scarcely attainable on Earth, is considered to have a positive effect on crystal growth, especially the van der Waals layered materials with low interlayer sliding energy barriers. Here, we investigate the structure and optical/electrical properties of van der Waals InSe semiconductor cultivated in microgravity environment on China space station. Atomic-level microstructure analyses reveal that this unique environment can successfully annihilate the naturally-existing stacking faults in flexible InSe, directly activating the intrinsic sliding ferroelectricity with excellent retention stability. The corresponding ferroelectric semiconductor field-effect transistors present obviously large non-volatile memory window, high on/off ratio and excellent mobility. More essentially, they can also give superior amplified spontaneous emission with exceptionally low excitation thresholds of photons for near infrared nonlinear light sources. These findings not only present an unconventional strategy for achieving high-quality van der Waals layered single crystals like InSe but also highlight their potential for next-generation emitter-integrated computing architectures combining memory and sensor functions. This work studies van der Waals InSe crystals grown on China space station. Microgravity growth condition annihilates interlayer stacking-faults in InSe, activates its intrinsic sliding ferroelectricity and enhances the super linear emission property.

</details>
<br>

**关键词**: microgravity, van der Waals InSe, sliding ferroelectricity, ferroelectric semiconductor, field-effect transistors, nonlinear light sources, amplified spontaneous emission, space station crystal growth

---

### 41. ❌ Interfacial configurational entropy tuning strategy enabling liquid alloys for efficient depolymerization of polyolefin waste

**作者**: Chaoping Xu, Haoyu Yan, Pengxuan Wang, Jun You Li, Haihao Wen, Xiaonan Wang, Jiaming Ma, Qian Zhang, Xiao Zhang, Dawei Tang, Bo Jiang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70325-2](https://doi.org/10.1038/s41467-026-70325-2)

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

**评分理由**: 论文研究的是塑料废物回收的化学催化过程，具体涉及液态合金催化剂用于聚烯烃废物的高效解聚，完全不涉及医学图像分析、人工智能、疾病诊断、手术规划或任何医疗健康相关主题。所有评分关键词均与医学影像和临床决策支持相关，而论文内容属于材料科学、化学工程和可持续技术领域，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了聚烯烃塑料废物难以高效解聚回收的问题，通过开发一种界面构型熵调控策略的液态合金催化剂，实现了在常压下将聚烯烃废物高效转化为轻质烯烃，并构建了光伏驱动的解聚系统以实现稳定运行。

<details open>
<summary>摘要翻译</summary>

> 塑料废弃物的积累构成了全球性环境危机，对生态系统造成严重威胁。解聚技术为塑料废弃物的闭环回收提供了一条前景广阔的路径。然而，化学性质稳定的聚烯烃的解聚仍具挑战性，且难以实现高轻质烯烃产率与稳定性。本文提出一种针对液态合金催化剂的界面构型熵调控策略，通过诱导活性位点的界面富集并优化电子结构，开发出一种具有中熵特性的四元GaInNiSn催化剂。该催化剂可在常压、不消耗共反应物的条件下，将聚烯烃回收转化为轻质烯烃，时空产率达到181.5 mmol gcat⁻¹ h⁻¹。机理研究表明，在动态的Ga界面内形成了Niδ⁻–Snδ⁺活性位点，能够活化C–H键以促进β-断裂。进一步构建了光伏驱动的解聚系统，在120小时内维持52.8 L h⁻¹的轻质烯烃产出。本研究为高效、可持续的塑料废弃物资源化利用提供了有力工具。将耐久的聚烯烃分解为可重复使用的结构单元仍十分困难。本文设计的液态合金催化剂能够将实际废弃物高效转化为轻质烯烃，并实现高产率与稳定性，即使在太阳能驱动的运行条件下亦能保持性能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Accumulation of plastic waste presents a global environmental crisis, posing severe threats to ecosystems. Depolymerization offers a promising route for closed-loop recycling of plastic waste. Nevertheless, depolymerizing chemically stable polyolefins remains challenging, yet fails to achieve high light olefin yields and stability. Herein, we propose an interfacial configurational entropy tuning strategy for liquid alloy catalysts, inducing active site interfacial enrichment and optimizing electronic structure. With this strategy, a quaternary GaInNiSn catalyst with medium entropy is developed for recycling polyolefins into light olefins under atmospheric pressure without co-reactant consumption, achieving a space-time yield of 181.5 mmol gcat⁻1 h⁻1. Mechanistic insights reveal that Niδ⁻–Snδ+ active sites form within the dynamic Ga interface, enabling C–H bond activation to promote β-scission. Furthermore, a photovoltaics-driven depolymerization system is constructed, maintaining light olefin output of 52.8 L h⁻1 over 120 hours. Our work unlocks a potent tool for efficient and sustainable plastic waste utilization. Breaking down durable polyolefins into reusable building blocks remains difficult. A tailored liquid alloy catalyst converts real waste into light olefins with high yield and stability, even under solar-powered operation.

</details>
<br>

**关键词**: liquid alloy catalyst, polyolefin depolymerization, interfacial configurational entropy, light olefins, plastic waste recycling, photovoltaics-driven system, GaInNiSn catalyst, β-scission

---

### 42. ❌ Polarity-tunable field-free room-temperature spin orbit torque switching via topological symmetry breaking in an all-vdW heterostructure for spin logic applications

**作者**: Fei Gao, Zili Wang, Runyu Zhao, Jing Li, Xiaoyue Song, Peiyuan Yu, Yun Sun, Weiran Xie, Guodong Wei, Yuan Yao, Jin Zou, Jie Zhang, Shucheng Xing, Roberto Mantovan, Zongxia Guo, N. Jaouen, Wei Zhao, Tianxiao Nie
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70590-1](https://doi.org/10.1038/s41467-026-70590-1)

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

**评分理由**: 该论文研究二维范德华异质结中的自旋轨道力矩开关，属于凝聚态物理、材料科学和自旋电子学领域，与医学图像分析、人工智能临床决策支持等医疗AI主题完全无关。论文内容涉及分子束外延生长、磁性各向异性、自旋电子器件等物理材料概念，未提及任何医学成像、疾病诊断、手术规划或医疗数据相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了在室温无外场条件下实现极性可调的自旋轨道力矩开关的挑战，通过在Bi2Te3/Fe4GeTe2全范德华异质结中利用界面耦合和面内磁各向异性打破反演对称性，实现了低电流密度下的可重构布尔逻辑功能。

<details open>
<summary>摘要翻译</summary>

> 二维铁磁材料因其原子级平整表面和灵活的界面调控能力，在推动低功耗、高集成度自旋电子器件发展方面具有巨大潜力。然而，在晶圆级范德华异质结中实现室温、无外场且极性可调的自旋轨道矩翻转仍面临重大挑战。本研究通过分子束外延生长了全范德华Bi<sub>2</sub>Te<sub>3</sub>/Fe<sub>4</sub>GeTe<sub>2</sub>异质结，并展示了其中极性可调的无外场自旋轨道矩翻转。界面耦合在Bi<sub>2</sub>Te<sub>3</sub>/Fe<sub>4</sub>GeTe<sub>2</sub>界面诱导出垂直磁各向异性，而Fe<sub>4</sub>GeTe<sub>2</sub>剩余的面内磁各向异性分量打破了反演对称性，从而实现了无外场翻转。通过调控面内分量的方向，可在较低电流密度（约1.55×10<sup>6</sup> A/cm<sup>2</sup>）下实现不同极性的磁翻转。这使得单个器件能够实现16种可重构布尔逻辑功能，为高能效二维自旋电子存储与逻辑系统开辟了新路径。我们的研究结果凸显了全范德华自旋轨道矩器件通过可扩展的室温电控方式革新自旋电子学的潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Two-dimensional ferromagnetic materials hold great promise for advancing low-power, high-integrated spintronic devices due to their atomic flat surfaces and versatile interfacial modulation. However, achieving a combination of room-temperature, field-free spin-orbit torque switching with tunable polarity in wafer-scale vdW heterostructures remains a significant challenge. Here, we demonstrate polarity-tunable, field-free spin-orbit torque switching in an all-vdW Bi<sub>2</sub>Te<sub>3</sub>/Fe<sub>4</sub>GeTe<sub>2</sub> heterostructure, grown by molecular beam epitaxy. Interfacial coupling induces perpendicular magnetic anisotropy in Bi<sub>2</sub>Te<sub>3</sub>/Fe<sub>4</sub>GeTe<sub>2</sub> interface, while the rest in-plane magnetic anisotropy component of Fe<sub>4</sub>GeTe<sub>2</sub> breaks the inversion symmetry, enabling field-free switching. By modulating the direction of in-plane component, magnetic switching with different polarity could be achieved at low current density (~1.55×10<sup>6</sup> A/cm<sup>2</sup>). This allows for 16 reconfigurable Boolean logic functions in a single device, paving a pathway for energy-efficient 2D spintronic memory and logic systems. Our findings highlight the potential of all-vdW spin-orbit torque devices to revolutionize spintronics with scalable, room-temperature electronic control.

</details>
<br>

**关键词**: spin-orbit torque switching, vdW heterostructure, perpendicular magnetic anisotropy, field-free switching, spintronic devices, Boolean logic functions, room-temperature operation, 2D ferromagnetic materials

---

### 43. ❌ A genetic toolkit for the human gut bacterium Mediterraneibacter gnavus identifies capsular polysaccharides as a competitive colonization factor

**作者**: Nozomu Obana, Gaku Nakato, Nobuhiko Nomura, Shinji Fukuda
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-69022-x](https://doi.org/10.1038/s41467-026-69022-x)

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

**评分理由**: 论文研究的是肠道细菌Mediterraneibacter gnavus的遗传工具开发及其荚膜多糖在肠道定植和炎症调节中的作用，属于微生物学、遗传学和肠道菌群研究领域。所有评分关键词均涉及医学影像分析、人工智能、深度学习、诊断、预后、手术规划等，与论文内容完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This study constructed mutants for six of the eight sortase-encoding genes in M. gnavus ATCC 29149 and identified those involved in the surface presentation of capsular polysaccharide (CPS) and superantigen-like proteins and demonstrated that CPS production is crucial for competitive colonization in germ-free mouse intestines.

!!! tip deepseek-chat TL;DR

    该研究开发了针对人类肠道细菌Mediterraneibacter gnavus的遗传工具，并发现其荚膜多糖对肠道竞争性定植至关重要，且与炎症活动呈负相关，提示其在疾病发病机制中的作用。

<details open>
<summary>摘要翻译</summary>

> 摘要：地中海拟杆菌（Mediterraneibacter gnavus）是一种人类肠道共生细菌，其在多种疾病（如活动性炎症性肠病[IBD]）患者中的丰度常会升高。然而，由于缺乏遗传修饰系统，控制其肠道定植和致病性的遗传因素仍不明确。本研究为地中海拟杆菌开发了多种遗传工具，包括穿梭载体、诱导型启动子、荧光报告基因以及基因破坏和缺失系统。利用这些工具，我们在地中海拟杆菌ATCC 29149菌株的八个分选酶编码基因中，成功构建了其中六个的突变体，并鉴定了那些参与荚膜多糖（CPS）和超抗原样蛋白表面呈递的基因。我们还发现了一个与分选酶基因相邻的CPS生物合成基因簇，并证明CPS的产生对于在无菌小鼠肠道中的竞争性定植至关重要。值得注意的是，CPS的产生与炎症活性呈负相关，且携带CPS基因簇的菌株在健康个体中的普遍性高于克罗恩病患者。这些发现表明，CPS有助于调节炎症和致病过程。本研究凸显了精确基因修饰系统在揭示肠道细菌定植和致病性遗传决定因素方面的潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Mediterraneibacter gnavus is a human symbiotic gut bacterium whose abundance often increases in patients with various diseases, such as active inflammatory bowel disease (IBD). However, the genetic factors governing its gut colonization and pathogenicity remain elusive due to the lack of genetic modification systems. In this study, we developed several genetic tools for M. gnavu s, including a shuttle vector, an inducible promoter, fluorescent reporters, and systems for gene disruption and deletion. Using these genetic tools, we constructed mutants for six of the eight sortase-encoding genes in M. gnavus ATCC 29149 and identified those involved in the surface presentation of capsular polysaccharide (CPS) and superantigen-like proteins. We also identified a CPS biosynthetic gene cluster adjacent to the sortase gene and demonstrated that CPS production is crucial for competitive colonization in germ-free mouse intestines. Notably, CPS production was inversely correlated with inflammatory activity, and CPS cluster-positive strains were more prevalent in healthy individuals than in Crohn’s disease patients. These findings suggest that CPS contributes to the modulation of inflammation and pathogenesis. This study highlights the potential of precise gene-modification systems to uncover genetic determinants of intestinal colonization and pathogenesis in gut bacteria.

</details>
<br>

**关键词**: Mediterraneibacter gnavus, genetic toolkit, capsular polysaccharide, gut colonization, inflammatory bowel disease, sortase genes, competitive colonization, pathogenesis

---

### 44. ❌ Megakaryocyte and platelet thrombospondin-1 regulates matrix remodeling by stabilizing basement membrane COL6A1 in lung injury

**作者**: Hernán F. Peñaloza, Atish Gheware, Ananya Gupta, Donovan Watza, Anupam Kumari, Shekina Gonzalez-Ferrer, Zeyu Xiong, Xingan Wang, Gregory A. Gibson, Pooja Bhojraj, Rick van der Geest, Jae-Sung Kim, Bo‐Ram Jin, Mélia Magnen, William G. Bain, Mohammadreza Tabary, Liwen Zhang, Arpad Somogy, Tomasz W. Kamiński, Prithu Sundd
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70489-x](https://doi.org/10.1038/s41467-026-70489-x)

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

**评分理由**: 论文研究的是肺损伤中巨核细胞/血小板来源的TSP1蛋白对细胞外基质稳定的分子机制，使用的方法包括活体显微镜、多光子共聚焦成像和蛋白质组学。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等人工智能和影像技术领域，而该论文完全不涉及这些技术，属于基础医学和分子生物学研究，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Findings indicate Mgk/plt-derived TSP1 represents a key mechanism of matrix stabilization by protecting the basement membrane from neutrophil-mediated proteolytic damage, regulating injury severity and Mgk numbers at the alveolar interface.

!!! tip deepseek-chat TL;DR

    该研究发现巨核细胞/血小板来源的血小板反应蛋白-1（TSP1）通过稳定基底膜蛋白COL6A1来保护肺免受中性粒细胞介导的损伤，从而调节肺损伤的严重程度。

<details open>
<summary>摘要翻译</summary>

> 肺损伤后的早期事件是细胞外基质重塑及临时基质的形成。尽管巨核细胞与血小板在止血过程中发挥重要作用，但其对肺损伤中基质的影响尚未完全明确。通过肺活体显微镜、多光子共聚焦混合成像的三维大范围扫描及无标记定量蛋白质组学技术，本研究发现源自巨核细胞/血小板的基质细胞蛋白血小板反应蛋白-1（thrombospondin-1, TSP1）能保护肺泡免受损伤。巨核细胞/血小板特异性敲除Thbs1基因的条件性敲除小鼠表现出肺泡屏障破坏加剧，并伴有中性粒细胞介导的损伤加重。这些条件性敲除小鼠在损伤后出现显著的细胞外基质重组，基底膜基质蛋白COL6A1减少。此外，条件性敲除小鼠的巨核细胞数量在纤维状胶原沉积区及肺泡渗漏区域增多。我们的研究结果表明，巨核细胞/血小板来源的TSP1通过保护基底膜免受中性粒细胞介导的蛋白水解损伤，调节损伤严重程度及肺泡界面处的巨核细胞数量，是实现基质稳定的关键机制。肺损伤后的早期事件是细胞外基质重塑。本研究揭示巨核细胞/血小板来源的血小板反应蛋白-1（TSP1）能保护肺细胞外基质，特别是基底膜蛋白COL6。缺乏TSP1的小鼠表现出更严重的肺损伤和中性粒细胞活性增强，证明TSP1可减轻损伤程度。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> An early event after lung injury is extracellular matrix (ECM) remodeling and the formation of a provisional matrix. While megakaryocytes and platelets (Mgk/plt) play important roles in hemostasis, their impact on the matrix in lung injury is not fully understood. Using lung intravital microscopy, 3D large area scanning with multiphoton confocal hybrid imaging, and label-free quantitative proteomics, the matricellular protein thrombospondin-1 (TSP1) arising from Mgk/plt protects the lung from alveolar injury. Mgk/plt cell-specific Thbs1 knockout (cKO) mice show increased alveolar barrier disruption with exaggerated neutrophil-mediated injury. The cKO mice exhibit striking extracellular matrix re-organization with reduction in basement membrane matrix protein COL6A1 after injury. Moreover, cKO mice increase Mgk numbers to regions of fibrillar collagen deposition and alveolar leak. Our findings indicate Mgk/plt-derived TSP1 represents a key mechanism of matrix stabilization by protecting the basement membrane from neutrophil-mediated proteolytic damage, regulating injury severity and Mgk numbers at the alveolar interface. An early event after lung injury is extracellular matrix remodelling. Here, the authors show that thrombospondin-1 (TSP1) from megakaryocytes/platelets protects the lung’s extracellular matrix, particularly basement protein COL6. Mice without TSP1 had greater lung damage and neutrophil activity, showing TSP1 reduces injury severity.

</details>
<br>

**关键词**: lung injury, thrombospondin-1, megakaryocytes, platelets, extracellular matrix, basement membrane, COL6A1, neutrophil-mediated injury

---

### 45. ❌ scTWAS: a powerful statistical framework for single-cell transcriptome-wide association studies

**作者**: Zhaotong Lin, Chang Su
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70374-7](https://doi.org/10.1038/s41467-026-70374-7)

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

**评分理由**: 论文标题为'scTWAS: a powerful statistical framework for single-cell transcriptome-wide association studies'，摘要内容完全围绕单细胞转录组学、基因表达预测、基因-性状关联分析等生物信息学和遗传学领域展开。论文使用统计方法（潜在变量模型和矩估计）处理单细胞RNA测序数据，应用于血液和脑组织分析，识别与复杂性状和疾病（如阿尔茨海默病）相关的基因。所有评分关键词均涉及医学影像分析、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像和基础模型医学影像，这些主题在论文标题、摘要和内容中完全没有出现。论文研究的是单细胞转录组学统计方法，而非任何形式的医学影像分析或相关AI应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Leveraging a latent-variable model and moment-based estimation to address the challenges of single-cell data, scTWAS consistently improves the prediction of genetically regulated gene expression across cell types in both blood and brain tissues.

!!! tip deepseek-chat TL;DR

    该论文提出了scTWAS统计框架，用于利用单细胞RNA测序数据进行细胞类型特异性转录组范围关联研究，解决了单细胞数据中的噪声和稀疏性问题，并在血液和脑组织中提高了基因表达预测准确性，识别了更多基因与性状的关联。

<details open>
<summary>摘要翻译</summary>

> 摘要：全转录组关联研究（TWAS）已成功识别出与复杂性状及疾病相关的基因，但多数研究基于混合基因表达数据开展，此类数据整合了异质细胞类型中的信号。如今，群体规模单细胞RNA测序数据的出现使得在细胞类型分辨率下进行TWAS成为可能，但由于单细胞数据存在强噪声、技术变异和高稀疏性等独特挑战，其分析面临困难。本文提出scTWAS——一种利用单细胞数据进行细胞类型特异性TWAS的统计方法。该方法通过潜变量模型和基于矩估计的策略应对单细胞数据的挑战，在血液和脑组织多种细胞类型中持续提升了遗传调控基因表达的预测准确性。与现有方法相比，scTWAS在29种血液性状和三种免疫相关疾病的分析中，于免疫细胞类型内识别出显著更多的基因-性状关联。在阿尔茨海默病的应用案例中，该方法进一步揭示了细胞亚型特异性关联，包括疾病相关小胶质细胞亚型中的MS4A6A基因以及炎症性小胶质细胞亚型中的PPP1R37基因。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Transcriptome-wide association studies (TWAS) have successfully identified genes associated with complex traits and diseases, but most have been performed using bulk gene expression data, which aggregate signals across heterogeneous cell types. Population-scale single-cell RNA sequencing data now make it possible to perform TWAS at the cell-type resolution, but present unique challenges due to strong noises, technical variations, and high sparsity. Here, we propose scTWAS, a statistical method to conduct cell-type-specific TWAS using single-cell data. Leveraging a latent-variable model and moment-based estimation to address the challenges of single-cell data, scTWAS consistently improves the prediction of genetically regulated gene expression across cell types in both blood and brain tissues. Compared to existing methods, scTWAS identifies substantially more gene-trait associations across 29 hematological traits and three immune-related diseases in immune cell types. An application to Alzheimer’s disease also reveals cell-subtype-specific associations, including MS4A6A in the disease-associated microglial subtype and PPP1R37 in the inflammatory microglial subtype.

</details>
<br>

**关键词**: single-cell RNA sequencing, transcriptome-wide association studies, statistical framework, gene expression prediction, cell-type-specific analysis, genetic associations, Alzheimer's disease, hematological traits

---

### 46. ❌ Strategic synthesis of FLPClusters toward catalysis

**作者**: Zhenhao Geng, Ayisha He, Xuexin You, Qingyuan Wu, Jingjuan Wang, Huifang Guo, Simin Li, Zhenlang Xie, Xuekun Gong, Muyi Yang, Dongjie Zuo, Rong Huo, Fengyu Li, Nanfeng Zheng, Hui Shen
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70577-y](https://doi.org/10.1038/s41467-026-70577-y)

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

**评分理由**: 论文研究的是化学催化领域，具体涉及FLPClusters（含受阻路易斯对的金属簇）的合成与催化性能，完全不涉及医学图像分析、人工智能、疾病诊断、手术规划等医疗相关主题。所有评分关键词均与论文内容无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了FLPClusters（含受阻路易斯对的金属簇）的战略合成难题，通过使用DPEphos配体成功合成了三种具有明确、可定制FLP活性位点的FLPClusters，并证明其在有机硅烷水解氧化反应中具有高催化活性，且催化性能与FLP位点数量相关。

<details open>
<summary>摘要翻译</summary>

> FLPClusters是一类结合受阻路易斯酸碱对（Frustrated Lewis Pairs, FLPs）且结构精确的金属团簇，代表了一类前景广阔的FLP催化剂。尽管FLPClusters近期才出现，但其精确且具有策略性的合成方法仍不成熟。本文中，我们报道了一种策略性合成FLPClusters的方法，该团簇具有明确、可定制且易于接近的FLP活性位点。我们的方法采用双(2-(二苯基膦基)苯基)醚（DPEphos）作为刚性表面配体。DPEphos的两个膦末端桥连相邻的金属原子，而其中央的醚氧原子（路易斯碱）在几何上受到约束，从而能够在团簇表面与铜原子（路易斯酸）形成稳定的FLPs。通过调节辅助硫醇盐配体的结构，我们成功合成了三种FLPClusters。这些FLPClusters在有机硅烷水解氧化生成硅醇的反应中表现出高催化活性。理论和实验研究均证实该催化过程由FLP驱动。关键的是，其催化性能与存在的FLP位点数量呈正相关。FLPClusters作为一类结合受阻路易斯酸碱对且结构精确的金属团簇，代表了一类有前景的催化剂，但其易于发生中和的倾向限制了催化效率。本文中，作者报道了合成具有明确、可定制且易于接近的FLP活性位点的FLPClusters的方法。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> FLPClusters, which are structurally precise metal clusters incorporating Frustrated Lewis Pairs (FLPs), represent a promising class of FLP catalysts. Although FLPClusters have emerged only recently, their precise and strategic synthesis remains underdeveloped. Herein, we report the approach for the strategic synthesis of FLPClusters featuring well-defined, tailorable, and accessible FLP active sites. Our approach utilizes bis(2-(diphenylphosphino)phenyl)ether (DPEphos) as a rigid surface ligand. The two phosphine termini of DPEphos bridge adjacent metal atoms, while the central ether oxygen atom (Lewis base) is geometrically constrained, enabling the formation of stable FLPs with copper atoms (Lewis acid) on the cluster surface. By modulating the structure of ancillary thiolate ligands, we successfully synthesized three FLPClusters. These FLPClusters demonstrate high catalytic activity in the hydrolytic oxidation of organosilanes to silanols. Both theoretical and experimental studies confirm that the catalysis is FLP-driven. Crucially, their catalytic performance scales with the number of FLP sites present. FLPClusters, which are structurally precise metal clusters incorporating Frustrated Lewis Pairs (FLPs), represent a promising class of catalysts, but their tendency to undergo neutralization limits catalytic efficiency. Herein, the authors report the synthesis of FLPClusters featuring well-defined, tailorable, and accessible FLP active sites.

</details>
<br>

**关键词**: FLPClusters, Frustrated Lewis Pairs, strategic synthesis, catalysis, organosilanes hydrolysis, metal clusters, DPEphos ligand, copper atoms

---

### 47. ❌ Increased contact transmission of contemporary Human H5N1 compared to Bovine and Mountain Lion H5N1 in a hamster model

**作者**: Reshma Koolaparambil Mukesh, Franziska K. Kaiser, Jonathan E. Schulz, Shane Gallogly, Jessica Prado-Smith, Arthur Wickenhagen, Kathleen Cordova, Brian S. Smith, Chad S. Clancy, Carl Shaia, Greg Saturday, Emmie de Wit, Neeltje van Doremalen, Claude Kwe Yinda, Vincent J. Munster
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-68900-8](https://doi.org/10.1038/s41467-026-68900-8)

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

**评分理由**: 论文研究的是H5N1禽流感病毒在仓鼠模型中的传播性和致病性，属于病毒学、传染病学和动物模型研究领域。所有评分关键词均涉及医学影像分析、人工智能、深度学习、诊断、预后、手术规划等方向，与论文的病毒传播实验研究内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The findings demonstrate that the Syrian hamster model complements existing animal models for influenza A virus research and expands the resources available for investigating the pathogenicity, transmissibility, and efficacy of countermeasures against HPAIV H5N1.

!!! tip deepseek-chat TL;DR

    该研究在仓鼠模型中比较了从牛、山狮和人类分离的当代H5N1禽流感病毒的传播效率，发现人类分离株比动物分离株具有相对更高的接触传播性。

<details open>
<summary>摘要翻译</summary>

> 摘要 当前在美国爆发的高致病性禽流感病毒（HPAIV）H5N1亚型构成了重大的公共卫生威胁。截至目前，美国已确认70例人类感染病例，其中包括两例重症及一例死亡。尽管合适的动物模型对于预测新出现病原体在人类中的潜在大流行风险至关重要，但针对当代HPAIV H5N1传播动态的研究仍然有限。本研究利用叙利亚仓鼠模型，对近期从牛、美洲狮及人类病例中分离的2.3.4.4b分支H5N1病毒的致病性和传播效率进行了评估。经鼻接种后，三种分离株均能在呼吸道有效复制并排出病毒。传播研究表明，所有分离株通过直接接触和空气途径的传播效率均有限。尽管总体传播效率不高，但人类H5N1分离株表现出比牛和美洲狮分离株相对更强的接触传播能力。综上所述，我们的研究结果表明，叙利亚仓鼠模型补充了现有的甲型流感病毒研究动物模型，并拓展了可用于研究HPAIV H5N1的致病性、传播能力及防控措施有效性的资源体系。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract The ongoing outbreak of highly pathogenic avian influenza virus (HPAIV) subtype H5N1 in the U.S. poses a significant public health threat. To date, 70 human cases have been confirmed in the United States, including two severe cases and one fatality. While suitable animal models are crucial for predicting the potential pandemic risk of newly emerging pathogens in humans, studies investigating contemporary HPAIV H5N1 transmission dynamics remain limited. Here, we investigate the pathogenicity and transmission efficiency of recent clade 2.3.4.4b H5N1 viruses isolated from a bovine, mountain lion, and a human case using Syrian hamsters. Intranasal inoculation results in productive virus replication in the respiratory tract and shedding for all three isolates. Transmission studies demonstrate limited efficiency via direct contact and airborne routes for all isolates. Although overall transmission is inefficient, the human H5N1 isolate demonstrates relatively greater contact transmissibility than the bovine and mountain lion isolates. Taken together, our findings demonstrate that the Syrian hamster model complements existing animal models for influenza A virus research and expands the resources available for investigating the pathogenicity, transmissibility, and efficacy of countermeasures against HPAIV H5N1.

</details>
<br>

**关键词**: H5N1 influenza, transmission efficiency, Syrian hamster model, contact transmission, pathogenicity, avian influenza virus, animal model, viral shedding

---

### 48. ❌ NAA40 and NAC cooperate in co-translational histone acetylation in humans

**作者**: Dandan Guan, Timo Denk, Ariel Klavaris, Matthias Thoms, Otto Berninghausen, Birgitta Beatrix, Antonis Kirmizis, Roland Beckmann
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70279-5](https://doi.org/10.1038/s41467-026-70279-5)

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

**评分理由**: 该论文研究的是分子生物学和生物化学领域，具体涉及组蛋白乙酰化、核糖体翻译后修饰、NAA40-NAC复合物等机制，完全不涉及医学影像分析、深度学习、AI诊断、手术规划等医疗AI相关主题。所有关键词均与论文内容无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that the NAA40-NAC interaction is required for efficient ribosome binding and histone acetylation and provided insights on the potential coordination of methionine removal and subsequent NAA40-mediated acetylation by formation of a multienzyme complex on the ribosome involving METAP1.

!!! tip deepseek-chat TL;DR

    该研究揭示了人类组蛋白H2A和H4的N端乙酰化过程中，NAA40酶如何与NAC复合物在核糖体出口协同作用，并通过冷冻电镜阐明了其分子机制。

<details open>
<summary>摘要翻译</summary>

> 摘要 N端乙酰化是真核生物中一种普遍存在且主要共翻译的修饰方式，深刻影响靶蛋白的折叠、区室化保真度与周转。与其他N-乙酰转移酶不同，人源NatD仅由催化亚基NAA40构成，且特异性修饰组蛋白H2A与H4。然而，NAA40共翻译活性的分子机制尚未明晰。本研究通过生物化学与冷冻电镜技术揭示了NAA40活性如何在核糖体肽通道出口处与NAC复合物协同作用。我们证明NAA40与NAC的相互作用是有效结合核糖体及实现组蛋白乙酰化所必需的。此外，本研究通过发现核糖体上METAP1参与形成的多酶复合物，揭示了甲硫氨酸切除与后续NAA40介导的乙酰化过程可能存在协同机制。因此，我们的结果阐明了NAA40介导的N端组蛋白乙酰化作用细节，并凸显了NAC作为新生蛋白修饰通用协调因子的功能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract N-terminal acetylation is an abundant and predominantly co-translational modification in eukaryotes that profoundly affects folding, compartmentalization fidelity and turnover of target proteins. Unlike other N-acetyltransferases, human NatD is composed solely of the catalytic subunit NAA40 and exclusively modifies histone proteins H2A and H4. However, the molecular details of co-translational NAA40 activity have remained elusive. Here, we show biochemically and by cryo-EM how NAA40 activity is coordinated at the ribosomal peptide tunnel exit involving the NAC complex. We demonstrate that the NAA40-NAC interaction is required for efficient ribosome binding and histone acetylation. Furthermore, we provide insights on the potential coordination of methionine removal and subsequent NAA40-mediated acetylation by formation of a multienzyme complex on the ribosome involving METAP1. Therefore, our results illustrate the details of N-terminal histone acetylation by NAA40 and highlight the role of NAC as a general coordinator of nascent protein modification.

</details>
<br>

**关键词**: N-terminal acetylation, histone acetylation, NAA40, NAC complex, ribosomal peptide tunnel, co-translational modification, cryo-EM, METAP1

---

### 49. ❌ Multi-mode piezoelectric radiation-based microantennas and miniaturized wireless sensing unit driven by bulk acoustic waves

**作者**: Xinyu Cai, Rui Wan, Rui Ding, Jianhui Wu, Jie Li, Kaihang Zhang, Jiaqi Lu, Dinku Hazarika, Liangquan Xu, Jiafeng Ni, Weipeng Xuan, Yungui Ma, Hao Jin, Shurong Dong, Jikui Luo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70058-2](https://doi.org/10.1038/s41467-026-70058-2)

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

**评分理由**: 论文研究的是基于体声波驱动的压电微天线和微型无线传感系统，属于微机电系统、无线传感技术领域。论文内容涉及压电材料、体声波谐振器、天线设计、无线传输性能等，主要应用场景包括生物医学、可穿戴设备和航空航天。所有评分关键词均与医学图像分析、深度学习医疗影像、AI诊断、预后预测、手术规划、多模态医学影像、基础模型医疗影像等医学AI领域完全无关，因此所有关键词评分为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文开发了一种基于体声波驱动的压电微天线和微型无线传感系统，实现了温度与应变传感，传输距离达1米，为超紧凑无线传感器和通信节点建立了可扩展平台。

<details open>
<summary>摘要翻译</summary>

> 无线传感系统为下一代智能平台实现了实时、非接触式监测。理想的无线传感系统应具备紧凑、低功耗和长通信距离的特点。本文报道了一种集成声共振驱动压电微天线（PE μ-antenna）的小型化无线传感系统，其有效面积仅为0.0196平方毫米。该压电微天线集成于薄膜体声波谐振器（Film Bulk Acoustic Resonator, FBAR）上，实现了1.85 GHz和3.91 GHz的双频辐射，增益分别为–32.96 dBi和–20.5 dBi。与现有压电发射器相比，该微天线实现了超过四个数量级的辐射效率提升和体积缩减。我们进一步将这种方法扩展到具有高品质因数的高次谐波体声波谐振器（High-Overtone Bulk Acoustic Resonators），用于无线传感。该系统可实现温度和应变传感，传输距离达1米，展现了无线传感系统中先进的小型化与传输性能。这项工作为生物医学、可穿戴及航空航天应用中的超紧凑无线传感器与通信节点建立了一个可扩展的平台。本研究开发了声波驱动的压电微天线。基于该天线的传感器实现了高达1米的无线温度与应变传感，为超紧凑无线传输与传感系统构建了一个可扩展的平台。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Wireless sensing systems enable real-time, non-contact monitoring for next-generation intelligent platforms. Ideal wireless sensing systems feature compact, low power consumption, and long communication range. Here we report a miniaturized wireless sensing system with an integrated acoustic-resonance-driven piezoelectric microantenna (PE μ-antenna) with a 0.0196 mm2 active area. The PE μ-antenna integrated on a film bulk acoustic resonator (FBAR) achieves dual-frequency radiation at 1.85 GHz and 3.91 GHz with gains of –32.96 dBi and –20.5 dBi, respectively. The μ-antennas achieve over four orders of magnitude radiation efficiency enhancement and volume reduction compared with existing piezoelectric transmitters. We further extend this approach to high-overtone bulk acoustic resonators with high quality factors for wireless sensing. The system enables temperature and strain sensing with a transmission range up to 1 m, demonstrating state-of-the-art miniaturization and transmission performance among wireless sensing systems. This work establishes a scalable platform for ultracompact wireless sensors and communication nodes in biomedical, wearable, and aerospace applications. Piezoelectric microantennas driven by acoustic waves were developed. A sensor based on the antenna enables wireless temperature and strain sensing up to 1 m, establishing a scalable platform for ultracompact wireless transmission and sensing systems.

</details>
<br>

**关键词**: piezoelectric microantenna, bulk acoustic waves, wireless sensing system, FBAR, temperature sensing, strain sensing, miniaturized wireless sensor, acoustic-resonance-driven

---

### 50. ❌ DEUP1 functions as a scaffold for basal foot integrity and planar polarity in multiciliated cells

**作者**: Haeryung Lee, Jiyeon Lee, Miram Shin, Ravi Shankar Goutam, Jaebong Kim, Soochul Park
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70661-3](https://doi.org/10.1038/s41467-026-70661-3)

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

**评分理由**: 论文研究的是细胞生物学中DEUP1蛋白在纤毛细胞基底足完整性和平面极性中的作用机制，属于基础细胞生物学研究。所有评分关键词均涉及医学影像分析、人工智能、临床决策支持等应用领域，与论文的分子机制研究完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that DEUP1 plays a critical role in the basal foot-an asymmetric appendage of the basal body required for coordinated ciliary beating and is established as a key structural regulator of BF integrity that is required for the long-term maintenance of coordinated ciliary motility.

!!! tip deepseek-chat TL;DR

    该研究发现DEUP1蛋白作为支架蛋白，对于维持多纤毛细胞中基底足的完整性和平面极性至关重要。

**关键词**: DEUP1, scaffold protein, basal foot, planar polarity, multiciliated cells, ciliary function, cellular organization

---

### 51. ❌ Kilogram-scale one-pot synthesis of multicomponent fullerene composites for efficient inverted perovskite solar cells

**作者**: Enlong Hou, Shuo Cheng, Song Kong, Yujue Qiu, Jingfu Chen, Xingyu CHEN, Shanshan Chen, Yiming Xing, Jinxin Yang, Liqiang Xie, Xinjin Zhao, Tongle Bu, Zhanhua Wei, Chengbo Tian
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70022-0](https://doi.org/10.1038/s41467-026-70022-0)

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

**评分理由**: 该论文研究的是钙钛矿太阳能电池中富勒烯复合材料的合成与应用，属于材料科学和能源技术领域，与医学图像分析、人工智能临床决策支持等医疗领域完全无关。论文内容涉及化学合成、材料表征、器件性能测试等，没有任何医学图像、诊断、预后、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了倒置钙钛矿太阳能电池中单组分富勒烯成本高且易聚集的问题，通过千克级一锅法合成多组分富勒烯复合材料，经热退火交联后显著提高了器件效率（达26.55%）和稳定性。

<details open>
<summary>摘要翻译</summary>

> 传统单组分富勒烯（如C60和PCBM）的高成本及有害的自聚集效应，是倒置结构钙钛矿太阳能电池商业化面临的主要障碍。本研究报道了一种千克级、一锅法合成的多组分富勒烯复合材料，该材料包含C60、双((3-甲基氧杂环丁烷-3-基)甲基)丙二酸-C60单加合物及其双加合物。该富勒烯复合材料的产率达96%，且无需复杂的柱色谱纯化，显著降低了生产成本。经过热退火处理后，其中的单加合物与双加合物发生交联，形成坚固的封装网络，将C60均匀包覆其中，从而提升了薄膜稳定性和电子迁移率。采用交联富勒烯复合材料的倒置钙钛矿太阳能电池实现了26.55%的优异效率，超越了基于PCBM的器件。此外，基于该复合材料的器件在ISOS-L-1和ISOS-D-2标准测试条件下分别运行1000小时后，仍能保持初始效率的96.0%和95.1%。值得注意的是，该复合材料在多种器件构型中均表现出卓越性能，包括宽带隙电池、大面积器件以及小型组件。单组分富勒烯的高成本与聚集问题阻碍了倒置钙钛矿太阳能电池的发展。作者通过高产率合成了一种富勒烯复合材料，该材料在退火过程中发生交联，在提升器件稳定性和效率的同时，保持了在不同器件构型中的性能表现。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The high cost and detrimental self-aggregation of conventional single-component fullerenes such as C60 and PCBM constitute a major obstacle to the commercialization of inverted perovskite solar cells (IPSCs). We report a kilogram-scale, one-pot synthesis of a multi-component fullerene composite (FC), comprising C60, a bis((3-methyloxetan-3-yl)methyl) malonate-C60 mono-adduct (BCM), and its bis-adduct (BCB). FC is obtained in 96% yields without complex column chromatography, significantly reducing production costs. Upon thermal annealing, BCM and BCB undergo cross-linking to form a robust encapsulation network that homogeneously incorporates C60, enhancing film stability and electron mobility. IPSCs incorporating cross-linked fullerene composite (CFC) demonstrate an impressive efficiency of 26.55%, surpassing that of PCBM-based devices (24.82%). Additionally, CFC-based devices maintain 96.0% and 95.1% of their initial efficiency after 1000 hours under ISOS-L-1 and ISOS-D-2 protocols, respectively. Notably, CFC demonstrates excellent performance across a range of device configurations, including wide-bandgap (1.68 eV and 1.77 eV) cells, large-area devices (1 cm2), and mini-modules (14.4 cm2). High cost and aggregation of single-component fullerenes hinder inverted perovskite solar cell development. The authors synthesize a fullerene composite in high yield that cross-links during annealing, improving stability and efficiency while maintaining performance in various device formats.

</details>
<br>

**关键词**: perovskite solar cells, fullerene composite, kilogram-scale synthesis, cross-linking, efficiency, stability, inverted structure, large-area devices

---

### 52. ❌ Brachiopod genome unveils the evolution of BMP signalling in bilaterian body patterning

**作者**: Thomas D. Lewin, Tosuke Sakagami, Keisuke Shimizu, Li-Jung Kao, Yi‐Ling Chiu, Isabel Jiah-Yih Liao, Mu-En Chen, Kanako Hisata, Kazuyoshi Endo, Noriyuki Satoh, Peter W. H. Holland, Yue Him Wong, Yi‐Jyun Luo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70403-5](https://doi.org/10.1038/s41467-026-70403-5)

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

**评分理由**: 该论文研究腕足动物基因组和BMP信号通路在双侧对称动物体轴模式形成中的进化机制，属于进化发育生物学和基因组学领域。论文内容完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或医学影像基础模型等主题。所有关键词与论文研究内容无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is argued that the spiralian ancestor retained the ancestral bilaterian mechanism, although downstream network components have undergone developmental system drift.

!!! tip deepseek-chat TL;DR

    该研究通过构建腕足动物染色体水平基因组并应用功能转录组学，揭示了BMP信号通路在双侧对称动物背腹轴模式形成中的保守机制，表明螺旋动物祖先保留了这一祖先双侧对称动物机制。

<details open>
<summary>摘要翻译</summary>

> 摘要：由于螺旋卵裂动物物种间存在显著多样性，其背腹轴图式形成的分子调控机制与祖先状态尚不明确。本研究通过构建腕足动物海豆芽（Lingula anatina）的染色体级别基因组，并运用功能转录组学方法探究了BMP信号调控下的背腹轴发育模式。我们发现原肠胚背侧存在BMP信号的不对称激活，该过程受腹侧脊索蛋白（chordin）表达与BMP配体“跷跷板”式相互作用的调控。通过小分子药物与重组蛋白实验，我们证实高BMP活性会抑制原肠胚期及幼虫期通常与神经图式形成相关的基因表达，这一现象与后口动物及非螺旋卵裂原口动物相似。研究结果表明该机制在三大两侧对称动物支系中具有深层保守性，腕足动物与非洲爪蟾（Xenopus）在BMP调控基因集上呈现的显著相似性为此提供了佐证。我们认为螺旋卵裂动物的祖先保留了两侧对称动物的原始调控机制，尽管其下游调控网络成分已发生发育系统漂变。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract The molecular control and ancestral state of dorsal–ventral patterning within spiralians remain unclear due to the remarkable diversity across species. Here we present a chromosome-level genome for the brachiopod Lingula anatina and apply functional transcriptomics to study dorsal–ventral patterning under BMP signalling control. We uncover asymmetrical activation of BMP signalling at the dorsal side of the gastrula, governed by ventral chordin expression and a ‘seesaw’ of BMP ligands. Using small-molecule drugs and recombinant proteins, we show that high BMP activity inhibits genes typically associated with neural patterning during gastrula and larval stages, similar to deuterostomes and non-spiralian protostomes. Our findings suggest deep conservation of this mechanism across all three major bilaterian clades, supported by striking similarities in BMP-regulated gene sets between brachiopods and Xenopus . We argue that the spiralian ancestor retained the ancestral bilaterian mechanism, although downstream network components have undergone developmental system drift.

</details>
<br>

**关键词**: brachiopod genome, BMP signalling, dorsal-ventral patterning, bilaterian evolution, developmental system drift, gastrula, chordin, spiralian ancestor

---

### 53. ❌ mist: a hierarchical Bayesian framework for detecting differential DNA methylation dynamics in single-cell data

**作者**: Daoyu Duan, Wenjing Ma, Wen Tang, Hao Wu, Liangliang Zhang, Hao Feng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70523-y](https://doi.org/10.1038/s41467-026-70523-y)

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

**评分理由**: 论文专注于单细胞DNA甲基化数据分析，属于计算生物学和表观遗传学领域，与医学影像分析、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像和基础模型医学影像等关键词完全无关。论文未涉及任何医学影像技术或临床应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work presents a hierarchical Bayesian framework for scDNAm data analysis, named mist (methylation inference for single-cell along trajectory), which models stage-specific biological variations, identifies genomic features with significant methylation changes along pseudotime, and performs Differential Methylation (DM) analysis across phenotypical groups.

!!! tip deepseek-chat TL;DR

    该论文提出了一种名为mist的层次贝叶斯框架，用于分析单细胞DNA甲基化数据，以检测沿伪时间轨迹的差异甲基化动态，并在小鼠胚胎发育和人类大脑发育的多组学数据集中识别了关键的发育调控因子。

<details open>
<summary>摘要翻译</summary>

> 单细胞DNA甲基化（scDNAm）测序技术的最新进展使得我们能够以前所未有的分辨率解析表观遗传景观，从而深入理解细胞异质性、分化与演化过程。轨迹推断技术通过将细胞沿伪时间轴排序，使研究者能够追踪连续细胞状态间的基因组学变化，并识别出呈现差异甲基化的关键位点。然而，目前尚缺乏能够在scDNAm数据中沿伪时间轴建模甲基化动态变化的方法。本文提出一个用于scDNAm数据分析的层次贝叶斯框架。我们的方法命名为mist（沿轨迹的单细胞甲基化推断），它能够建模阶段特异性生物变异，识别沿伪时间轴发生显著甲基化变化的基因组特征，并在表型组间进行差异甲基化（DM）分析。模拟实验表明，在检测沿伪时间的DM基因方面，该方法相较于现有技术具有更高的准确性。将mist应用于小鼠胚胎发育和人类大脑发育的多组学数据集时，该方法成功识别出关键发育调控因子，其甲基化模式与谱系转换过程相吻合。mist已作为R/Bioconductor软件包公开发布。单细胞DNA甲基化可追踪发育过程中的细胞状态转换，但现有方法难以对伪时间轴上的渐进变化进行建模。本文作者引入了一种贝叶斯方法，能够评估阶段特异性变异并发现动态甲基化模式。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Recent advancements in single-cell DNA methylation (scDNAm) sequencing technologies have enabled the profiling of epigenetic landscapes at unprecedented resolution, offering insights into cellular heterogeneity, differentiation and evolution. Trajectory inference, which orders cells along pseudotime, allows researchers to track genomics changes across continuous cell states and identify key loci exhibiting differential methylation. However, no methods currently exist to model methylation changes along pseudotime in scDNAm data. Here, we present a hierarchical Bayesian framework for scDNAm data analysis. Our method, named mist (methylation inference for single-cell along trajectory), models stage-specific biological variations, identifies genomic features with significant methylation changes along pseudotime, and performs Differential Methylation (DM) analysis across phenotypical groups. Simulations demonstrate its superior accuracy in detecting DM genes along pseudotime compared to existing methods. Applied to multi-omics datasets of mouse embryonic development and developing human brain, mist identifies key developmental regulators, whose methylation patterns align with lineage transitions. mist is publicly available as an R/Bioconductor package. Single-cell DNA methylation tracks developmental cell-state transitions, but existing methods struggle to model gradual changes over pseudotime. Here, authors introduce a Bayesian approach that estimates stage-specific variability and finds dynamic methylation.

</details>
<br>

**关键词**: single-cell DNA methylation, hierarchical Bayesian framework, pseudotime trajectory, differential methylation, epigenetic landscapes, developmental regulators, multi-omics data, R/Bioconductor package

---

### 54. ❌ Machine learning–driven design of engineered cilia enables hybrid operations in acoustic microrobots

**作者**: Yun Ling, Yujing Lu, Joseph Rich, Mingyuan Liu, Xianchen Xu, Ty Naquin, Ying Chen, Shanglin Li, Ruoyu Zhong, Kaichun Yang, Shuaiguo Zhao, Qian WU, Ke Jin, Tony Jun Huang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70048-4](https://doi.org/10.1038/s41467-026-70048-4)

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

**评分理由**: 论文研究的是声学微机器人中工程化纤毛的机器学习驱动设计，属于微纳机器人、声学驱动和微流体领域，与医学图像分析、临床决策支持、疾病诊断等医疗AI主题完全无关。论文未涉及任何医学影像数据、医疗应用或临床场景。

</details>
<br>

!!! info Semantic Scholar TL;DR

    E engineered cilia for hybrid operations microrobots are introduced, a class of acoustic microrobots that use geometry-tuned cilia and resonance-induced forces to execute complex motions such as bidirectional bending, controllable rotation, and adaptive morphing, establishing acoustic-driven microrobots as a scalable and efficient platform for intelligent microrobotic actuation in biomedical and microfluidic applications.

!!! tip deepseek-chat TL;DR

    该研究通过机器学习方法设计工程化纤毛，实现了声学微机器人的混合操作模式，包括平移、旋转和螺旋运动。

**关键词**: acoustic microrobots, engineered cilia, machine learning, hybrid operations, microfluidics, acoustic actuation, microswimmers, design optimization

---

### 55. ❌ PTBP1 inhibition reprograms myogenesis to rescue impaired muscle regeneration in mdx mice through correcting E2A splicing

**作者**: Shusheng Fan, Xiaoyun Liu, Qian Pan, Haowei Tong, Qiaoqiao Gui, Guangyao Guo, Huitao Hong, Wanting Hu, Xiaofei Huang, Lei Zhao, Xihua Li, Qinwei Yu, Luyong Zhang, Zhenzhou Jiang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70669-9](https://doi.org/10.1038/s41467-026-70669-9)

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

**评分理由**: 论文研究的是杜氏肌营养不良症（DMD）的分子机制和治疗策略，聚焦于PTBP1蛋白调控E2A选择性剪接对肌肉再生的影响。所有评分关键词均涉及医学影像分析、AI诊断、手术规划等方向，而本文属于分子生物学、遗传学和肌肉疾病治疗领域，未涉及任何医学影像技术、AI模型或影像数据分析内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that dergrasyn, a deubiquitinase inhibitor, induces polypyrimidine tract binding protein 1 degradation, restores myogenic differentiation, restores myogenic differentiation, and ameliorates dystrophic pathology.

!!! tip deepseek-chat TL;DR

    该研究发现抑制PTBP1可纠正E2A剪接失衡，重编程肌肉细胞发育，并在杜氏肌营养不良症小鼠模型中挽救缺陷的肌肉再生。

<details open>
<summary>摘要翻译</summary>

> 杜氏肌营养不良症由编码抗肌萎缩蛋白的DMD基因突变引起，是一种以肌肉再生受损为特征的严重进行性肌肉消耗性疾病。本研究揭示了转录因子E2-α（编码转录因子E12和E47）的选择性剪接在肌源性进程中起关键作用。E47在增殖期的成肌细胞中高表达并促进细胞增殖，而E12在分化阶段上调并驱动肌源性定向分化。机制上，我们发现核剪接因子多嘧啶区结合蛋白1是调控转录因子E2-α互斥选择性剪接的关键调节因子。在正常成肌细胞分化过程中，多嘧啶区结合蛋白1水平下降，促进从E47到E12的转换。然而，在杜氏肌营养不良症患者和mdx小鼠模型中，多嘧啶区结合蛋白1持续异常升高，导致E47/E12比例失调（E47增加、E12减少），从而破坏肌源性分化并损害肌肉再生。治疗方面，敲低多嘧啶区结合蛋白1可恢复成肌细胞分化、增强肌肉修复并改善mdx小鼠的肌肉功能。此外，我们证明去泛素化酶抑制剂德格拉辛可诱导多嘧啶区结合蛋白1降解，恢复肌源性分化并改善肌营养不良病理。我们的研究确认多嘧啶区结合蛋白1是杜氏肌营养不良症的潜在治疗靶点，并强调调控转录因子E2-α剪接是恢复肌肉再生的有效策略。本研究证实，抑制多嘧啶区结合蛋白1可纠正E2A剪接失衡、重编程肌肉细胞发育，并在杜氏肌营养不良症小鼠模型中挽救缺陷的肌肉再生功能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Duchenne muscular dystrophy, caused by mutations in the DMD gene encoding dystrophin, is a severe progressive muscle-wasting disorder characterized by impaired muscle regeneration. We reveal the alternative splicing of transcription factor E2-alpha (encoding transcription factors E12 and E47) plays a pivotal role in myogenic progression. E47 is highly expressed in proliferating myoblasts and promotes proliferation, whereas E12 is upregulated during differentiation and drives myogenic commitment. Mechanistically, we identify the nuclear splicing factor polypyrimidine tract binding protein 1 as a key regulator of transcription factor E2-alpha mutually exclusive alternative splicing. Polypyrimidine tract binding protein 1 levels decline during normal myoblast differentiation, facilitating the switch from E47 to E12. However, in Duchenne muscular dystrophy patients and mdx mice, polypyrimidine tract binding protein 1 remains aberrantly elevated, resulting in dysregulated E47/E12 ratios (increased E47 and decreased E12), which disrupts myogenic differentiation and impairs muscle regeneration. Therapeutically, polypyrimidine tract binding protein 1 knockdown restores myoblast differentiation, enhances muscle repair, and improves muscle function in mdx mice. Furthermore, we demonstrate that dergrasyn, a deubiquitinase inhibitor, induces polypyrimidine tract binding protein 1 degradation, restores myogenic differentiation, and ameliorates dystrophic pathology. Our findings identify polypyrimidine tract binding protein 1 as a potential therapeutic target for Duchenne muscular dystrophy and highlight modulation of transcription factor E2-alpha splicing as a promising strategy to restore muscle regeneration. Here, the authors demonstrate that Inhibiting PTBP1 corrects E2A splicing imbalance, reprograms muscle cell development, and rescues defective muscle regeneration in a Duchenne muscular dystrophy mouse model.

</details>
<br>

**关键词**: Duchenne muscular dystrophy, PTBP1 inhibition, E2A splicing, muscle regeneration, mdx mice, myogenic differentiation, therapeutic target, alternative splicing

---

### 56. ❌ VHL synthetic lethality screens uncover CBF-β as a negative regulator of STING

**作者**: James A. C. Bertlin, Tekle Pauzaite, Qian Liang, Niek Wit, James C. Williamson, Jia Jhing Sia, Nicholas J. Matheson, Brian M. Ortmann, Thomas J. Mitchell, Anneliese O. Speak, Qing Zhang, James A. Nathan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70517-w](https://doi.org/10.1038/s41467-026-70517-w)

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

**评分理由**: 该论文研究的是肾细胞癌的分子机制和基因靶向治疗，通过CRISPR/Cas9筛选发现CBF-β与VHL的合成致死关系，并揭示其对STING通路的调控作用。论文内容完全属于分子生物学、癌症研究和基因功能领域，不涉及任何医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态影像或基础模型等主题。所有关键词均与论文内容无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究发现CBF-β是肾细胞癌中VHL的合成致死靶点，其缺失通过上调I型干扰素信号通路诱导肿瘤细胞死亡。

<details open>
<summary>摘要翻译</summary>

> 摘要：透明细胞肾细胞癌（ccRCC）是最常见的肾癌类型，其典型特征为von Hippel-Lindau（VHL）肿瘤抑制基因的双等位基因失活。本研究通过全基因组CRISPR/Cas9筛选技术，揭示了VHL的合成致死相互作用因子，并发现在VHL缺失的ccRCC细胞系中，核心结合因子β（Core Binding Factor β, CBF-β）的缺失会导致细胞死亡，并在体内损害肿瘤的形成与生长。这种合成致死关系不依赖于VHL缺失细胞中缺氧诱导因子（hypoxia inducible factors, HIFs）活性的升高，而是涉及CBF-β的已知结合伴侣——RUNX转录因子家族。机制研究表明，CBF-β缺失会上调I型干扰素信号通路；我们进一步发现CBF-β在STING基因位点具有直接的抑制作用，从而调控干扰素刺激基因的表达。靶向肾癌中的CBF-β既能选择性诱导肿瘤细胞死亡，又能促进I型干扰素信号通路的激活。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Clear cell renal cell carcinoma (ccRCC) represents the most common form of kidney cancer and is typified by biallelic inactivation of the von Hippel-Lindau ( VHL ) tumour suppressor gene. Here, we undertake genome-wide CRISPR/Cas9 screening to reveal synthetic lethal interactors of VHL , and uncover that loss of Core Binding Factor β (CBF-β) causes cell death in VHL -null ccRCC cell lines and impairs tumour establishment and growth in vivo. This synthetic relationship is independent of the elevated activity of hypoxia inducible factors (HIFs) in VHL -null cells, but does involve the RUNX transcription factors that are known binding partners of CBF-β. Mechanistically, CBF-β loss leads to upregulation of type I interferon signalling, and we uncover a direct inhibitory role for CBF-β at the STING locus controlling Interferon Stimulated Gene expression. Targeting CBF-β in kidney cancer both selectively induces tumour cell lethality and promotes activation of type I interferon signalling.

</details>
<br>

**关键词**: clear cell renal cell carcinoma, VHL, CBF-β, synthetic lethality, CRISPR/Cas9 screening, type I interferon signaling, STING, tumor suppression

---

### 57. ❌ Genetic alternative splicing regulation mapping of cartilage and synovium reveals tissue-specific mechanisms of joint-related traits

**作者**: Wen Tian, Shou-Ye Hu, Shan-Shan Dong, Chen Wang, Junqi Zhang, Feng (Kevin) Jiang, Zhi Yang, Tie-Lin Yang, Yan Guo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70419-x](https://doi.org/10.1038/s41467-026-70419-x)

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

**评分理由**: 论文研究的是遗传学、基因组学和分子生物学领域，具体关注软骨和滑膜组织的选择性剪接调控及其与关节相关疾病（骨关节炎、类风湿关节炎）和性状（身高）的遗传关联。研究内容涉及sQTL分析、GWAS整合、功能变异鉴定和效应基因识别，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态影像或基础模型等关键词。所有关键词与论文主题完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A splicing quantitative trait loci (sQTL) resource for cartilage and synovium is generated and highlights the significant impact of tissue-specific alternative splicing regulation on disease etiology and provides a valuable resource for further mechanistic validation.

!!! tip deepseek-chat TL;DR

    该研究通过构建软骨和滑膜组织的剪接数量性状位点图谱，揭示了组织特异性选择性剪接调控在骨关节炎、类风湿关节炎和身高遗传风险中的作用，并识别了相关的效应基因。

<details open>
<summary>摘要翻译</summary>

> 软骨与滑膜是参与骨关节炎（OA）、类风湿关节炎（RA）及人类身高等关节相关疾病与性状的关键组织。尽管全基因组关联研究（GWAS）已鉴定出大量与这些性状相关的风险位点，但由于缺乏相关组织的剪接遗传学数据，这些关联背后的分子机制——尤其是涉及可变剪接的部分——仍不甚明确。为弥补这一不足，我们构建了软骨与滑膜的剪接数量性状基因座（sQTL）资源。我们在两种组织中鉴定出2,796个独立的顺式sQTL和六个反式s基因，其中包括179个组织特异性顺式sQTL。精细定位分析确定了116个高可信度的功能性剪接变异（sVariants），这些变异预计通过剪接位点的获得或缺失影响剪接过程，其中约半数位于经典剪接位点模体之外。将sQTL数据与GWAS汇总统计结果整合，我们在关节组织中发现了12个骨关节炎、6个类风湿关节炎及183个身高效应基因。值得注意的是，12个骨关节炎效应基因中有七个显示出关节组织特异性的共定位。结合组织特异性s基因在组织相关生物学过程及疾病中起关键作用的发现，我们的研究揭示了组织特异性可变剪接调控对疾病病因学的重要影响，并为后续机制验证提供了宝贵资源。可变剪接可能有助于解释关节疾病的遗传风险。本研究通过构建软骨与滑膜的sQTL图谱，揭示了组织特异性剪接变异，并精确定位了骨关节炎、类风湿关节炎及身高的效应基因。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Cartilage and synovium are essential tissues involved in joint-related diseases and traits, including osteoarthritis (OA), rheumatoid arthritis (RA), and human height. Although genome-wide association studies (GWAS) identify numerous risk loci for these traits, the molecular mechanisms underlying these associations, particularly those involving alternative splicing, remain poorly understood due to the lack of splicing-related genetic data in relevant tissues. To address this limitation, we generate a splicing quantitative trait loci (sQTL) resource for cartilage and synovium. We identify 2,796 independent cis-sQTLs and six trans-sGenes across the two tissues, including 179 tissue-specific cis-sQTLs. Fine-mapping analysis identifies 116 high-confidence functional sVariants predicted to affect splicing through splice site gain or loss, with approximately half located outside canonical splice site motifs. Integration of sQTL data with GWAS summary statistics reveals 12 osteoarthritis, 6 rheumatoid arthritis, and 183 height effector genes in joint tissues. Notably, seven of the 12 osteoarthritis effector genes show joint tissue-specific colocalization. Together with the finding that tissue-specific sGenes play crucial roles in tissue-related biological processes and diseases, our work highlights the significant impact of tissue-specific alternative splicing regulation on disease etiology and provides a valuable resource for further mechanistic validation. Alternative splicing may help explain genetic risk for joint diseases. Here, the authors generate cartilage and synovium sQTL maps, revealing tissue‑specific splicing variants and pinpointing effector genes for osteoarthritis, rheumatoid arthritis, and height

</details>
<br>

**关键词**: alternative splicing, splicing quantitative trait loci (sQTL), cartilage, synovium, osteoarthritis, rheumatoid arthritis, genome-wide association studies (GWAS), effector genes

---

### 58. ❌ Visualising reaction complexes in amine-based unloaded and CO2-loaded carbon capture solutions

**作者**: Harrison Laurent, Daniel Sault, Thomas F. Headen, Terri-Louise Hughes, James E. Wheatley, Christopher M. Rayner, Lorna Dougan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70391-6](https://doi.org/10.1038/s41467-026-70391-6)

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

**评分理由**: 该论文研究的是碳捕获溶剂（氨基乙酸钠/钾溶液）在未负载和CO2负载状态下的分子结构分析，使用中子衍射数据和结构精修方法。论文主题属于物理化学、材料科学和环境工程领域，与医学影像分析、人工智能、临床决策支持、疾病诊断、手术规划等医学领域完全无关。所有评分关键词均针对医学影像和医疗AI应用，因此相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过中子衍射和结构精修方法揭示了两种碳捕获溶剂（氨基乙酸钠和钾溶液）在未负载和CO2负载状态下的分子结构，量化了分子间相互作用的结构、频率和能量稳定性，为碳捕获溶液的大规模建模和理性设计提供了新见解。

<details open>
<summary>摘要翻译</summary>

> 在发电及不可避免产生二氧化碳排放的工业领域，碳捕集、利用与封存是应对气候变化的重要技术手段。许多碳捕集剂采用水性胺类混合溶液，其吸收二氧化碳后可通过热法再生。溶质间的物理相互作用对这些溶液的化学反应性及再生能耗具有关键影响。然而，目前尚未有基于实验获得的原子尺度结构信息报道。本研究通过对氢/氘同位素置换的中子衍射数据进行结构精修，揭示了两种典型碳捕集溶剂——甘氨酸钠水溶液与甘氨酸钾水溶液——在未负载与负载二氧化碳状态下的微观结构。该方法使我们能够定量分析溶液中存在的分子间相互作用的结构特征、出现频率以及基于经验势结构精修（EPSR）推算的配对相互作用能稳定性。此类研究方法可便捷应用于其他碳捕集体系，为深入理解溶液微观机制、推进大规模模拟计算及理性设计提供前所未有的洞察力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> In power generation and industries where CO<sub>2</sub> emissions are unavoidable, carbon capture, utilisation, and storage is an important tool to offset climate change. Many carbon capture agents are blends of aqueous amines, which absorb CO<sub>2</sub> and are then thermally regenerated. The physical interactions between solutes play a crucial role in their reactivity and energy requirements for regeneration. Atomically resolved, experimentally derived information about the structure of these solutions, however, has yet to be reported. In this work, we report the structure of two model carbon capture solvents, aqueous sodium and potassium glycinate, in the unloaded and CO<sub>2</sub>-loaded state by performing structural refinement on H/D isotopically varied neutron diffraction data. This allows us to quantify the structure, frequency, and EPSR-derived pair interaction energetic stability of intermolecular interactions present. Such methodology can be readily applied to other carbon capture solutions, providing unparalleled insight and facilitating their large-scale modelling and rational design.

</details>
<br>

**关键词**: carbon capture, amine solutions, neutron diffraction, molecular structure, CO2-loaded solvents, structural refinement, intermolecular interactions, aqueous glycinate

---

### 59. ❌ Mode hopping via nonlinear magnon-magnon coupling in a synthetic antiferromagnet

**作者**: Mujin You, Moojune Song, Jun Seo, Donghyeon Lee, Seungha Yoon, Daiju Hayashi, Yoichi Shiota, Teruo Ono, Sanghoon kim, Se Kwon Kim, Albert Min Gyu Park, Kab-Jin Kim
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70298-2](https://doi.org/10.1038/s41467-026-70298-2)

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

**评分理由**: 论文研究的是合成反铁磁体中的非线性磁振子动力学，属于凝聚态物理和自旋电子学领域，与医学图像分析、人工智能临床决策支持等医疗AI主题完全无关。所有关键词均涉及医疗影像、疾病诊断、手术规划等医学应用，而本文专注于基础物理现象（非线性磁振子耦合、模式跳跃）和自旋电子器件开发，两者领域完全不同，无任何交叉点。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了合成反铁磁体中非线性磁振子耦合引起的模式跳跃现象，实验观察到了声学与光学磁振子模式之间的GHz级频率跳变和滞后行为，为磁振子信息处理器件开发提供了新平台。

<details open>
<summary>摘要翻译</summary>

> 识别磁振子之间的非线性相互作用对于推动磁振子学领域发展和开发下一代自旋电子器件至关重要。本研究报道了在合成反铁磁体（SAF）中非线性磁振子模式跳变及其滞后行为的实验观测。在强射频激发下，磁振子系统在声学模与光学模之间发生急剧跃迁，并伴随千兆赫兹量级的频率跳变——其幅度比先前报道的基于磁振子的混合系统中观测到的结果高出数个数量级。我们进一步揭示了这种模式跳变具有滞后特性，反映了多稳态非线性动力学，并通过理论分析和微磁模拟验证了这些发现。这些结果确立了非线性磁振子动力学的新范式，超越了以往报道的强耦合效应，凸显了合成反铁磁体作为磁振子频率转换器与信息处理开关平台的潜力。非线性在广泛的长度与能量尺度上催生了极为丰富的物理现象。在此，You及其合作者研究了磁振子系统（特别是合成反铁磁体）的非线性行为，观测到光学支与声学支磁振子之间具有滞后特性的模式跳变。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Identifying nonlinear interactions among magnons is crucial for advancing the field of magnonics and developing next-generation spintronic devices. In this work, we report the experimental observation of nonlinear magnon mode hopping and hysteretic behavior in a synthetic antiferromagnet (SAF). Under strong radio-frequency excitation, the magnon system exhibits abrupt transitions between acoustic and optic modes, accompanied by GHz-scale frequency jumps—orders of magnitude larger than previously reported in magnon-based hybrid systems. We further show that this mode hopping is hysteretic, reflecting multistable nonlinear dynamics, and support these findings through theory and micromagnetic simulations. These results establish a new regime of nonlinear magnon dynamics, going beyond previously reported strong-coupling effects, and highlight the potential of SAFs as platforms for magnon-based frequency converters and switches for information processing. Non-linearity leads to remarkably rich physics across a wide variety of length and energy. Here, You and coauthors study the non-linear behaviour of a magnonic system, specifically a synthetic antiferromagnet, where they observe hysteretic mode hopping between the optical and acoustic magnon branches.

</details>
<br>

**关键词**: nonlinear magnon-magnon coupling, synthetic antiferromagnet, mode hopping, hysteretic behavior, magnon dynamics, spintronic devices, micromagnetic simulations, frequency converters

---

### 60. ❌ Millennial-to-orbital-scale subsurface ocean warming and Polynya formation off Dronning Maud Land during the last glacial

**作者**: Tainã M. L. Pinho, Dirk Nürnberg, A. Nele Meckler, Gesine Mollenhauer, Juliane de Borba Müller, Gerrit Lohmann, Lester Lembke-Jene, Salma Hidayat, Vincent Rigalleau, Frank Lamy, Ralf Tiedemann
**期刊/来源**: nature_communications
**发布日期**: 2026-03-12
**DOI**: [10.1038/s41467-026-70498-w](https://doi.org/10.1038/s41467-026-70498-w)

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

**评分理由**: 论文研究的是古气候学领域，具体是关于南极洲德龙宁毛德地附近冰期海洋温度变化和冰间湖形成的多代理重建，使用沉积物中的浮游有孔虫进行分析。所有评分关键词均属于医学影像分析和人工智能临床决策支持领域，与论文的地质学、古海洋学主题完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过分析沉积物中的浮游有孔虫，重建了南极洲德龙宁毛德地附近冰期上层水柱的热盐结构变化，发现冰期南极冰阶期间海洋次表层变暖可能导致冰间湖形成，从而增加南极水分供应并促进冰盖增厚。

<details open>
<summary>摘要翻译</summary>

> 摘要 我们基于一份跨越75,000至20,000年冰期的独特沉积记录中的浮游有孔虫，提出了对东南极冰架附近上层水体性质变化的千年尺度多指标重建。研究结果表明，南极表层水与温暖深层水之间温盐结构的变化，可能导致上层水体层化增强或促进冰间湖（对流翻转）的形成。在冰期南极亚冰期及低黄赤交角时期，海洋次表层变暖与盐度、营养盐含量增加同时出现，表明层化结构破坏且存在冰间湖。这片形成于毛德皇后地外海的冰期冰间湖，反映了一种混合型海岸-开阔海洋冰间湖模式。我们将该冰期毛德皇后地冰间湖的发展归因于海冰引起的温暖深层水次表层变暖、密度层化减弱以及大气与海洋环流变化的共同作用。冰期亚冰期期间，冰间湖驱动的海洋热量释放可能增加了向南极输送的水汽，从而促进了大陆架边缘前进冰盖的冰积累与增厚。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract We present a millennial-scale multi-proxy reconstruction of changes in properties of the upper water column near the East Antarctic ice shelf based on planktonic foraminifera from a unique sedimentary archive spanning the glacial period from 75,000 to 20,000 years. Our results imply that variations in the thermohaline structure between Antarctic Surface Water and Warm Deep Water (WDW) may have resulted in either strengthening the stratification of the upper water column or promoting polynya formation (convective overturning). Oceanic subsurface warming during glacial Antarctic stadials and periods of low obliquity, combined with increased salinity and nutrient content, suggests the breakdown in stratification and polynya presence. This glacial polynya formed off Dronning Maud Land (DML) reflects a hybrid coastal-open-ocean polynya mode. We attribute the development of the Glacial DML Polynya to sea-ice induced subsurface warming of WDW and a decrease in density stratification in combination with circulation changes in the atmosphere and ocean. The polynya-driven oceanic heat release during the glacial stadials may have increased the moisture supply to Antarctica and thus promoted the accumulation of ice and the thickening of an advancing ice sheet at the continental shelf margin.

</details>
<br>

**关键词**: Antarctic glaciation, polynya formation, subsurface ocean warming, planktonic foraminifera, thermohaline structure, Warm Deep Water, Dronning Maud Land, glacial stadials

---

### 61. ❌ Intrinsic capacity and stroke risk in a multiple cohort study

**作者**: Ying Li, Yi Chen, Yin Chen, YiYang Pan, Yuan Chen, LiJuan Huang, Wei Jiang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70524-x](https://doi.org/10.1038/s41467-026-70524-x)

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

**评分理由**: 论文研究的是内在能力与中风风险的流行病学关联，使用队列研究和Cox回归模型，完全不涉及医学影像分析、深度学习、AI诊断、手术规划或多模态医学影像等主题。所有关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Overall intrinsic capacity and each of its five domains are significantly associated with stroke incidence, with the strongest association observed among adults aged 80 years or older, highlighting intrinsic capacity as a promising, multidimensional target for primary stroke prevention in an aging population.

!!! tip deepseek-chat TL;DR

    这项大规模队列研究探讨了内在能力与中风发病率之间的关联，发现内在能力及其五个领域均与中风风险显著相关，尤其在80岁及以上人群中关联最强。

<details open>
<summary>摘要翻译</summary>

> 内在能力是世界卫生组织确立的概念，旨在综合反映个体生理与心理能力的总和，其测量涵盖认知、心理、感官、活力及运动能力五个被认定为健康老龄化至关重要的维度。该概念的核心目标是将关注点从疾病转向功能，以预测健康、失能与衰弱状态。在此项大规模队列研究中，我们旨在探讨内在能力与卒中发病之间的关联。研究共纳入184,219名年龄在40岁及以上的参与者。内在能力依据世卫组织《老年人整合照护指南》框架，通过五个维度进行评估。我们采用Cox比例风险回归模型检验该关联，并进行分层分析与敏感性分析，以评估各维度的特异性贡献及结果的稳健性。本研究结果显示，整体内在能力及其所有五个维度均与卒中发病率显著相关，其中在80岁及以上人群中观察到的关联最为强烈。这些发现表明，内在能力可作为老龄化人群原发性卒中预防的一个具有前景的多维度干预靶点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Intrinsic capacity is a concept established by the World Health Organization (WHO). The concept aims to represent the total of a person's physical and mental abilities, measured across five domains: cognition, psychological, sensory, vitality, and locomotor that were identified as crucial for healthy aging. The aim being to shift focus from disease to function to predict health, disability, and frailty. In this large-scale cohort study, we aim to investigate the association between intrinsic capacity and incident stroke. The study includes 184,219 participants aged 40 years or older. Intrinsic capacity is assessed across five domains according to the WHO Integrated Care for Older People framework. We use Cox proportional hazards regression models to examine this association and perform stratified and sensitivity analyses to evaluate domain-specific contributions and robustness. Here we show that both overall intrinsic capacity and each of its five domains are significantly associated with stroke incidence, with the strongest association observed among adults aged 80 years or older. These findings highlight intrinsic capacity as a promising, multidimensional target for primary stroke prevention in an aging population.

</details>
<br>

**关键词**: intrinsic capacity, stroke risk, cohort study, aging population, Cox proportional hazards regression, primary stroke prevention, WHO Integrated Care for Older People

---

### 62. ❌ Biological valorization of methane and nitrogen gas-derived ammonia via methanotrophic bacteria for gut-beneficial nutrients

**作者**: Zhan Gao, Yuyu Liu, Shanyao Jiao, Rongzhan Fu, Yunhao Chen, Chenyue Zhang, Xuemei Shen, Guidong Yang, Su Yang, Xiaoyan Wang, Liang Shi, Qiang Fei
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70448-6](https://doi.org/10.1038/s41467-026-70448-6)

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

**评分理由**: 论文研究的是利用甲烷氧化细菌将甲烷和氨转化为功能性饲料添加剂的生物技术，涉及代谢工程、发酵优化、营养分析和动物实验，属于生物工程、微生物学和营养学领域。所有评分关键词均与医学影像分析、人工智能临床决策支持相关，而论文完全不涉及医学影像、深度学习、疾病诊断、手术规划或多模态医学数据，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A rational metabolic engineering strategies and an optimized fed-batch fermentation are developed to enhance ammonia utilization in a methanotrophic bacterium of Methylotuvimicrobium sanxanigenens, which significantly ameliorates colitis symptoms in male mice by attenuating inflammatory progression and restoring the intestinal barrier.

!!! tip deepseek-chat TL;DR

    该研究通过代谢工程和发酵优化改造甲烷氧化细菌，使其高效共利用甲烷和氨生产富含必需氨基酸和多糖的营养蛋白，口服该蛋白能显著改善小鼠结肠炎症状并维持肠道微生态平衡。

<details open>
<summary>摘要翻译</summary>

> 通过甲烷氧化菌对分散式甲烷与氮气（N<sub>2</sub>）来源的氨进行原位升级转化具有显著吸引力。然而，氨氧化过程中产生的有毒中间体会严重抑制细胞生长，从而阻碍高效的生物生产。本研究通过整合转录组分析，开发了合理的代谢工程策略并优化了分批补料发酵工艺，以增强桑氏甲烷微菌（Methylotuvimicrobium sanxanigenens）对氨的利用能力。经过改造、过表达羟胺还原酶的桑氏甲烷微菌能够高效共同化甲烷与氨用于细胞蛋白质合成，其生产效率提升了18倍。所得甲烷氧化菌细胞蛋白（MCP）不仅具备理想的人体必需氨基酸组成，还富含多糖和肽类等生物活性营养物质。口服这种营养型MCP能通过减轻炎症进程、修复肠道屏障，显著缓解雄性小鼠的结肠炎症状。此外，MCP处理可维持肠道微生物群稳态，促进有益代谢产物的分泌，从而保护肠道微环境。因此，本研究为将分散式CH<sub>4</sub>与空气就地生物转化为功能性饲料添加剂提供了一种前景广阔的生物学途径。该技术不仅有助于推动负碳气体价值化路径的发展，还能通过减少抗生素和疫苗的使用，促进畜牧业的绿色转型。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The in-situ upcycling of decentralized methane and nitrogen gas (N<sub>2</sub>)-derived ammonia via methanotrophic bacteria is highly attractive. However, the toxic intermediate generated from ammonia oxidation significantly inhibits cell growth, thereby hindering efficient bioproduction. Herein, by integrating transcriptomic analysis, we develop rational metabolic engineering strategies and an optimized fed-batch fermentation to enhance ammonia utilization in a methanotrophic bacterium of Methylotuvimicrobium sanxanigenens. The modified M. sanxanigenens overexpressing hydroxylamine reductase efficiently co-assimilates methane and ammonia for cell protein synthesis, with an 18-fold increase in productivity. The resulting methanotrophic cell protein (MCP) not only exhibits an ideal essential amino acid profile but also contains bioactive nutrients, including polysaccharides and peptides. Oral administration of this nutritional MCP significantly ameliorates colitis symptoms in male mice by attenuating inflammatory progression and restoring the intestinal barrier. Moreover, MCP treatment maintains gut microbiota homeostasis and promotes the excretion of beneficial metabolites, thereby protecting the intestinal microenvironment. Hence, this study provides a promising biological approach for the local bio-valorization of decentralized CH<sub>4</sub> and air into functional feed additives. This biotechnology not only facilitates advancements in developing carbon-negative gas-to-value pathways but also drives green transformations in animal husbandry by reducing the use of antibiotics and vaccines.

</details>
<br>

**关键词**: methanotrophic bacteria, metabolic engineering, ammonia utilization, cell protein synthesis, colitis amelioration, gut microbiota, functional feed additives, carbon-negative biotechnology

---

### 63. ❌ Optical imaging of the intrinsic adsorption kinetics in single zeolite nanoparticles

**作者**: Xuannuo Yi, Haoran Han, Aosheng Chang, Ziyuan Liu, Qingxue Hui, Chongqin Zhu, Zhaoqiang Zhang, Shasha Liu, Wei Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70625-7](https://doi.org/10.1038/s41467-026-70625-7)

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

**评分理由**: 论文研究的是单纳米颗粒水平的光学成像方法，用于研究分子筛中的吸附动力学，属于化学、材料科学和纳米技术领域。所有评分关键词均与医学影像分析、人工智能临床决策支持相关，而论文完全不涉及医学影像、疾病诊断、手术规划或医疗AI模型，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种单纳米颗粒光学成像方法，揭示了在ZSM-5纳米颗粒上，限制效应（而非相互作用强度）主导了轻质烯烃的吸附动力学逆转现象。

<details open>
<summary>摘要翻译</summary>

> 限域效应日益被认为是影响分子筛中客体-骨架相互作用的关键因素，但其对吸附动力学的影响在很大程度上仍未得到探索。传统对毫克级颗粒集合体的整体测量所获得的表观吸附动力学，将动态分子相互作用与宏观传质过程混为一谈。本文提出一种光学成像方法，通过将样品尺寸减小至单纳米颗粒水平（亚皮克级），定量监测以相互作用为主导的吸附过程。该结果使得确定基本吸附与脱附步骤的本征速率常数和活化能垒成为可能。在同系轻质烯烃于同一ZSM-5纳米颗粒上的吸附中，观察到相对于质子亲和力而言，限域效应诱导了吸附动力学的反转。这一发现表明，在单纳米颗粒水平上，吸附动力学主要由限域效应而非相互作用强度主导，并为探究和理性设计适用于多种应用的分子筛提供了一个通用平台。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The confinement effect is increasingly recognized as a critical factor influencing guest-framework interactions in molecular sieves, yet its impact on adsorption kinetics remains largely unexplored. Conventional ensemble measurements on milligram-scale particle assemblies yield apparent adsorption kinetics that conflate dynamic molecular interactions with macroscopic mass transport. Here, we present an optical imaging approach that quantitatively monitors interaction-dominated adsorption by reducing the sample size to the single-nanoparticle level (sub-picogram scale). The results enable the determination of intrinsic rate constants and activation energy barriers for elementary adsorption and desorption steps. A confinement-induced reversal of adsorption kinetics, relative to proton affinities, is observed among homologous light olefins on the same ZSM-5 nanoparticle. This finding reveals that confinement-rather than interaction strength-primarily governs adsorption kinetics at the single-nanoparticle level and provides a general platform for probing and rationally designing molecular sieves for diverse applications.

</details>
<br>

**关键词**: optical imaging, single-nanoparticle, adsorption kinetics, confinement effect, ZSM-5, intrinsic rate constants, activation energy barriers, molecular sieves

---

### 64. ❌ Auto-crosslinking sporesilk fibers promote endospore and Cry toxin clustering

**作者**: Mike Sleutel, Adrià Sogues, Han Remaut
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70495-z](https://doi.org/10.1038/s41467-026-70495-z)

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

**评分理由**: 论文研究的是苏云金芽孢杆菌的孢子丝纤维结构、自组装机制及其作为毒力因子在生物害虫控制中的作用，属于微生物学、结构生物学和农业生物技术领域。所有评分关键词均涉及医学影像分析、人工智能诊断、手术规划等临床医疗技术，与论文的生物学基础研究内容完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The recombinant production and self-assembly of A-ENA nanofibers are demonstrated, and it is shown that the exogenic addition of A-ENA fibers to B. thuringiensis strains natively lacking sporesilks results in spore-PSB clustering and gain of virulence, enabling the rational, non-GMO functionalization of these biological pest control agents.

!!! tip deepseek-chat TL;DR

    该研究发现苏云金芽孢杆菌的孢子丝纤维通过自交联形成稳定结构，能聚集孢子和毒素颗粒增强杀虫毒性，并实现了该纤维的重组生产和功能化应用。

<details open>
<summary>摘要翻译</summary>

> 苏云金芽孢杆菌以色列亚种通过其芽孢及伴随的含昆虫毒素伴孢晶体侵染并杀死昆虫幼虫。本研究发现，该菌的内生芽孢与伴孢晶体表面覆盖着一层由8纳米宽纤维构成的"孢丝"基质，这些纤维具有双螺旋对称性，由堆叠的α螺旋发夹结构原丝组装而成。这些α型芽孢附属结构（简称"A-ENA"）每个亚基通过多达十个自催化及邻近诱导的分子间异肽键稳定，形成连续共价聚合物，具备卓越的化学与物理稳定性。研究证实A-ENA作为苏云金芽孢杆菌的毒力因子，通过将芽孢与伴孢晶体聚集为感染性团块来增强杀虫活性。此外，我们实现了A-ENA纳米纤维的重组生产与自组装，并证明外源性添加A-ENA纤维至天然缺乏孢丝结构的苏云金芽孢杆菌菌株后，可引发芽孢-伴孢晶体聚集并获得毒力，这为这些生物害虫防治剂的合理化、非转基因功能化改造提供了新途径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Bacillus thuringiesis infects and kills insect larvae via its spores and associated entomotoxin-containing parasporal bodies (PSBs). We show that endospores and PSBs of B. thuringiensis Sv. Israëlensis are covered in a 'sporesilk' matrix that consist of 8 nm wide fibers with a double helical symmetry, formed by protofilaments of stacked alphahelical hairpins. These alpha endospore appendages ('A-ENA') are stabilized by up to ten autocatalytic and proximity-induced intermolecular isopeptide bonds per subunit, forming a continuous covalent polymer with remarkable chemical and physical robustness. We show A-ENA functions as B. thuringiensis virulence factor, increasing insecticidal activity by clustering spores and PSBs into an infectious clumps. Moreover, we demonstrate the recombinant production and self-assembly of A-ENA nanofibers, and show that the exogenic addition of A-ENA fibers to B. thuringiensis strains natively lacking sporesilks results in spore-PSB clustering and gain of virulence, enabling the rational, non-GMO functionalization of these biological pest control agents.

</details>
<br>

**关键词**: Bacillus thuringiensis, sporesilk fibers, endospore appendages, isopeptide bonds, virulence factor, insecticidal activity, recombinant production, biological pest control

---

### 65. ❌ Highly ordered mesoporous TiO2 nanomeshes with tunable pore periodicity via self-limiting modular monolayer assembly of monomicelles

**作者**: Pengfei Zhang, Liangliang Liu, Wanhai Zhou, Shixiang Ding, Zirui Lv, Linlin Duan, Zaiwang Zhao, Yun Tang, Dongliang Chao, Weiwei Li, Dongyuan Zhao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70387-2](https://doi.org/10.1038/s41467-026-70387-2)

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

**评分理由**: 论文研究的是材料科学领域，具体涉及介孔TiO2纳米网的合成、结构控制和在电池中的应用，与医疗影像分析、人工智能临床决策支持等医学领域完全无关。所有关键词均未在标题或摘要中出现，也没有任何相关概念提及。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了二维介孔TiO2纳米网的可控制备难题，通过单分子胶束自限制组装合成了具有可调孔周期性的高度有序纳米网，并证明其作为锡水系电池阳极保护层可延长循环寿命至1400小时以上。

<details open>
<summary>摘要翻译</summary>

> 精确调控单层胶束构筑单元进行二维模块化组装，从而制备具有可调孔道周期性与构型的自支撑高度有序介孔晶体纳米网格，仍是一项重大挑战。本研究通过单胶束的自限制模块化单层组装，成功合成了具有周期性孔阵列的高度均匀自支撑超薄介孔二氧化钛纳米网格。所得的自支撑介孔二氧化钛纳米网格由单层长程有序六方孔阵列贯穿构成，孔道贯通（直径约25纳米），形成了厚度约17纳米、比表面积约97平方米/克的高度周期性二维介观结构。通过改变前驱体与模板剂的比例，孔道周期性能被精确控制在约30至51纳米范围内。作为概念验证，该二氧化钛纳米网格被用作锡水系电池的阳极保护层，在1.0毫安/平方厘米的电流密度下实现了超过1400小时的循环寿命。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Precisely controlling the two-dimensional (2-D) modular assembly of monolayer micelle building blocks into free-standing highly-ordered mesoporous crystalline nanomeshes with adjustable pore periodicity and configuration remains a significant challenge. Here, highly-uniform free-standing ultrathin mesoporous TiO<sub>2</sub> nanomeshes with periodically arranged pore arrays have been synthesized via a self-limiting modular monolayer assembly of monomicelles. The resultant free-standing mesoporous TiO<sub>2</sub> nanomeshes are perforated by monolayer long-range ordered hexagonal pore arrays with through mesopores ( ~25 nm in diameter), forming highly periodic 2-D mesostructures with a thickness of ~17 nm and a specific surface area of ~97 m<sup>2</sup> g<sup>-1</sup>. The pore periodicity can accurately be controlled from ~30 to 51 nm by varying the precursor-to-template ratio. As a proof of concept, the TiO<sub>2</sub> nanomeshes are deployed as anode protectors in Sn aqueous batteries, with a prolonged cycle life of over 1400 h at 1.0 mA cm<sup>-2</sup>.

</details>
<br>

**关键词**: mesoporous TiO2 nanomeshes, self-limiting assembly, monomicelle assembly, pore periodicity control, anode protector, aqueous batteries, cycle life improvement, 2D mesostructures

---

### 66. ❌ Scalable and stretchable 1D multifunctional fibers for multimodal sensing and stimulation

**作者**: Junyi Yin, Jie Zhu, Shaolei Wang, Jiangnan Yuan, Chenyang Li, Samuel Margolis, Hong Bao, Yanan Wang, Wei Zhao, Enbo Zhu, Longlong Mu, Shuai He, Kaidong Wang, Jie Zhao, YongAn Huang, Yunlei Zhou
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70178-9](https://doi.org/10.1038/s41467-026-70178-9)

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

**评分理由**: 论文研究的是可拉伸多功能纤维的制造及其在生物医学传感和刺激中的应用，属于生物电子学和柔性电子学领域。研究背景要求的是医学图像分析、深度学习、AI诊断、手术规划等医学影像相关主题，而该论文完全不涉及医学图像处理、分析或基于图像的临床决策支持。所有关键词均与医学影像相关，因此相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A solution-deposition strategy for the scalable and cost-effective fabrication of stretchable liquid metal fibers integrated with electrochemically stable, tissue-interfacing electrodes, thereby enabling the realization of stretchable multifunctional fibers.

!!! tip deepseek-chat TL;DR

    该研究开发了一种可拉伸的液态金属多功能纤维，用于生理信号传感、神经刺激和无线能量传输，为下一代一维生物电子学提供了平台。

<details open>
<summary>摘要翻译</summary>

> 一维多功能纤维因其几何特性优势而备受关注，这种特性使其能够与柔软生物组织形成共形界面并实现高效电荷传输。本研究开发了一种溶液沉积策略，用于可规模化、低成本制备集成电化学稳定组织界面电极的可拉伸液态金属纤维，从而实现了可拉伸多功能纤维的制造。该纤维将电极与导电通路无缝集成于单一结构中，能够支持多种应用，如电生理信号传感、体内神经刺激和无线能量传输。多功能纤维在应变下表现出显著提升的电学性能，在拉伸和弯曲过程中保持导电性，并展现出更低的阻抗和更高的信号稳定性，尤其在生理监测和电刺激过程中更为突出。该纤维优异的生物相容性和机械顺应性使其非常适用于可穿戴系统和长期生物医学应用，为下一代一维生物电子学提供了稳健的平台。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> One-dimensional (1D) multifunctional fibers have garnered significant attention due to their advantageous geometry properties, which allows conformal interfacing with soft biological tissues and efficient charge transport. Here, we developed a solution-deposition strategy for the scalable and cost-effective fabrication of stretchable liquid metal fibers integrated with electrochemically stable, tissue-interfacing electrodes, thereby enabling the realization of stretchable multifunctional fibers. This fiber seamlessly combines electrodes and conductive pathways into a single structure, enabling versatile applications such as electrophysiological signal sensing, in vivo nerve stimulation, and wireless energy transmission. The multifunctional fiber demonstrates significantly improved electrical performance under strain, maintaining conductivity during stretching and bending, and exhibits lower impedance and higher signal stability, particularly during physiological monitoring and electrical stimulation. The fiber's excellent biocompatibility and mechanical compliance makes it well suited for wearable systems and long-term biomedical applications, offering a robust platform for next generation 1D bioelectronics.

</details>
<br>

**关键词**: stretchable multifunctional fibers, liquid metal fibers, electrophysiological signal sensing, nerve stimulation, wireless energy transmission, biocompatibility, wearable biomedical systems, 1D bioelectronics

---

### 67. ❌ Water-generated dangling linkers in a metal-organic framework

**作者**: Yu Fu, Yifeng Yao, Sébastien Paul, Kenji Mochizuki, Gaël De Paëpe
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70247-z](https://doi.org/10.1038/s41467-026-70247-z)

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

**评分理由**: 论文研究金属有机框架（MOFs）中水分子与材料结构的相互作用机制，属于材料科学、化学和物理化学领域。论文使用固态核磁共振、动态核极化技术和计算模拟方法，研究水分子如何可逆地改变UiO-66 MOF的结构。所有评分关键词均涉及医学影像分析、人工智能医疗应用、疾病诊断预测等医学领域，而本论文完全不涉及任何医学、影像、临床或AI相关内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    本研究揭示了水分子在金属有机框架UiO-66中可逆地导致连接基团脱离形成悬挂基团的分子机制，通过多维固态核磁共振和计算模拟重新定义了水-MOF相互作用的理解。

<details open>
<summary>摘要翻译</summary>

> 金属有机框架（MOFs）因其在水相关领域的应用而受到广泛关注。深入理解水与MOFs之间的分子水平相互作用对于指导分子设计和优化水相关应用至关重要。水既可以作为被动客体，与开放金属位点或极性连接体发生弱相互作用而不改变框架结构；也可以作为反应物种，切断无机簇与有机连接体之间的配位键，导致不可逆降解。在本研究中，我们揭示了水对原型MOF材料UiO-66（一种公认具有高水稳定性的MOF）中金属-连接体键合的重要影响。水分子在UiO-66中的吸附会导致连接体上牢固附着的羧酸基团发生位移，从而将其转化为悬垂羧酸基团。这些悬垂基团通过水分子和μ<sub>3</sub>-OH形成的氢键得以稳定。值得注意的是，这种结构转变在去除水分子的条件下是可逆的。这些发现通过多维固态核磁共振、前沿动态核极化（DNP）技术以及计算模拟相结合的方法得以阐明。我们的研究通过挑战传统认知，提出了一种可逆的分子结构演化模式，重新定义了人们对水-MOF相互作用的理解。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Metal-Organic Frameworks (MOFs) have attracted widespread attention for their applications in water-related contexts. A comprehensive understanding of the molecular-level interactions between water and MOFs is crucial for guiding molecular design and optimizing water-related applications. Water can act as a passive guest, interacting weakly with open metal sites or polar linkers without altering the framework, or as a reactive species that cleaves the dative bonds between inorganic clusters and organic linkers, leading to irreversible degradation. In this work, we uncover a significant impact of water on the metal-linker linkage in UiO-66, a prototype MOFs which is considered highly stable with water. The adsorption of water molecules in UiO-66 results in the displacement of firmly attached carboxylate groups of the linker, thereby transforming them into dangling carboxylate groups. These dangling groups are stabilized by water molecules and μ<sub>3</sub>-OH through hydrogen bonding. Remarkably, this structural transformation is reversible upon water removal. These findings were elucidated through the integration of multidimensional solid-state NMR, cutting-edge dynamic nuclear polarization (DNP) techniques, and computational calculations. By challenging conventional wisdom, our research has introduced a reversible molecular structure evolution scenario, redefining the understanding of water-MOF interactions.

</details>
<br>

**关键词**: Metal-Organic Frameworks, water-MOF interactions, UiO-66, dangling carboxylate groups, solid-state NMR, dynamic nuclear polarization, reversible structural transformation, computational calculations

---

### 68. ❌ Integrated small and long RNA sequencing reveals piRNA mediated transposon repression during human oogenesis

**作者**: Feng Zhang, Hongdao Zhang, Yao Xiao, M Liu, Aimin Ren, Suying Liu, Ligang Wu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-11
**DOI**: [10.1038/s41467-026-70296-4](https://doi.org/10.1038/s41467-026-70296-4)

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

**评分理由**: 该论文研究人类卵子发生过程中piRNA介导的转座子抑制机制，属于生殖生物学和分子遗传学领域。论文内容涉及单细胞RNA测序、piRNA表达动态、转座子调控等，与评审要求的所有医学影像分析、深度学习医学影像、AI诊断、预后预测、手术规划、多模态医学影像、基础模型医学影像等关键词完全无关。论文未涉及任何医学影像技术或临床应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Together, this study provides a valuable single-cell dataset of small and long RNA co-expression landscapes in developing human oocytes and reveals coordinated yet distinct roles of different PIWI/piRNA classes in TE repression during human oogenesis, with short-piRNAs acting as the primary and broad-spectrum suppressors, and long-piRNAs providing coordinated ERV-specific repression.

!!! tip deepseek-chat TL;DR

    本研究通过单细胞小RNA和长RNA测序揭示了人类卵子发生过程中不同PIWI/piRNA类别在转座子抑制中的协调作用，发现短piRNA是主要的广谱抑制因子，而长piRNA提供协调的ERV特异性抑制。

<details open>
<summary>摘要翻译</summary>

> piwi互作RNA（piRNAs）在调控生殖细胞中转座元件（TE）活性中至关重要，然而其在人类卵子发生过程中的表达动态与功能仍不甚明确。本研究同步分析了人类单个卵细胞在四个发育阶段的小RNA与长RNA表达谱。piRNAs，尤其是与PIWIL3蛋白相关的短链piRNAs，是人类卵子发生过程中占主导地位的小非编码RNA。短链piRNA的显著增加与转座元件整体表达下降同步发生，尤以LINE-1和内源性逆转录病毒（ERVs）最为明显。相比之下，与PIWIL1和PIWIL2蛋白相关的长链piRNAs则与特定ERV亚家族的下调相关。基因组分析显示，高产出piRNA簇在进化中形成了针对LINE-1和ERVs的不对称反义插入偏好，从而实现对转座元件家族的特异性调控。本研究共同提供了发育中人类卵细胞小RNA与长RNA共表达图谱的珍贵单细胞数据集，揭示了不同PIWI/piRNA类别在人类卵子发生过程中协同而分工明确的转座元件抑制机制：短链piRNA发挥主要且广谱的抑制作用，而长链piRNA则提供协同的ERV特异性抑制。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The piwi-interacting RNAs (piRNAs) are essential for controlling transposable elements (TEs) activity in germ cells, yet their expression dynamics and functions during human oogenesis remain poorly understood. Here, we simultaneously profile small and long RNAs in individual human oocytes across four developmental stages. piRNAs, especially PIWIL3-associated short piRNAs, are the predominant small non-coding RNAs during human oogenesis. A marked increase in short-piRNAs coincide with a global reduction of TE expression, particularly LINE-1 and endogenous retroviruses (ERVs). In contrast, PIWIL1- and PIWIL2-associated long piRNAs correlate with the downregulation of certain specific ERV subfamilies. Genomic analyses reveal that highly productive piRNA clusters have evolved asymmetric antisense insertion bias toward LINE-1 and ERVs, enabling TE families-specific regulation. Together, our study provides a valuable single-cell dataset of small and long RNA co-expression landscapes in developing human oocytes and reveals coordinated yet distinct roles of different PIWI/piRNA classes in TE repression during human oogenesis, with short-piRNAs acting as the primary and broad-spectrum suppressors, and long-piRNAs providing coordinated ERV-specific repression.

</details>
<br>

**关键词**: piRNA, human oogenesis, transposable elements, single-cell RNA sequencing, PIWI proteins, LINE-1, endogenous retroviruses, germ cells

---

### 69. ❌ Amorphous/crystalline interwoven multipods with high Co/Ni activity for wide-temperature-range sodium-sulfur batteries

**作者**: Tingjiao Xiao, Zhen Fang, Nian Ran, Ronghui Liu, Yuxuan Gao, Jianbo Wu, Jianjun Liu, Hua Wang, Wen-Feng Lin, Wei Zhou
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-69749-7](https://doi.org/10.1038/s41467-026-69749-7)

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

**评分理由**: 该论文研究的是钠硫电池的电化学催化剂材料（Sn掺杂的CoNiS多足结构），属于能源存储材料领域，与医学图像分析、人工智能临床决策支持等医学领域完全无关。论文内容涉及电池性能、催化剂设计、界面工程等，未提及任何医学成像、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了钠硫电池在宽温度范围内因多硫化物转化动力学缓慢导致的性能限制问题，通过设计Sn掺杂的CoNiS多足结构催化剂，优化了Co/Ni活性位点的吸附能，显著提升了电池的循环稳定性和宽温性能。

<details open>
<summary>摘要翻译</summary>

> 由16电子转移导致的缓慢动力学阻碍了宽温域钠硫电池的发展。本文报道了一种具有非晶-晶相交织结构的锡掺杂钴镍硫多足体材料。作为正极催化剂使用时，所得钠硫电池在室温下以3 A g<sup>-1</sup>的电流密度循环1200次后，放电容量仍保持1320.8 mAh g<sup>-1</sup>，并在-20至50°C的宽温度范围内表现出稳定且高容量的电化学性能。研究证实，锡掺杂产生的非晶/晶相界面能够调控钴和镍原子的微电子环境，通过Co-S和Ni-S键优化其对多硫化钠中间产物的吸附能，从而降低多硫化物转化的能垒。这种界面调控有效降低了决速步骤的能垒，促进了宽温度范围内的整体反应动力学。本研究为开发高性能催化剂提供了一种有效的非晶/晶相界面工程策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Sluggish kinetics caused by 16-electron transfer hinders development of wide-temperature-range sodium-sulfur batteries. Here we report Sn-doped CoNiS multipods with an amorphous-crystalline interwoven structure. Employed as a positive electrode catalyst, the resulting sodium-sulfur battery exhibits a discharge capacity of 1320.8 mAh g<sup>-1</sup> at 3 A g<sup>-1</sup> after 1200 cycles at room temperature, together with stable and high-capacity electrochemical performance ranged from -20 to 50 °C. It has been evidenced that the amorphous/crystalline interfaces generated by Sn doping can adjust the microelectronic environment of Co and Ni atoms, optimize their adsorption energy toward sodium polysulfide intermediates through Co-S and Ni-S bonding, and thus decrease the energy barrier of polysulfide conversion. This interfacial regulation efficiently lowers the energy barrier of the rate-determining step and facilitates the overall reaction kinetics over a wide temperature range. This work provides an efficient amorphous/crystalline interface engineering strategy to develop high-performance catalysts.

</details>
<br>

**关键词**: sodium-sulfur batteries, amorphous-crystalline interface, CoNiS catalyst, polysulfide conversion, wide-temperature-range, electrochemical performance, Sn doping, energy barrier

---

## Token 消耗统计

- **总计**: 301,442 tokens（输入 207,844 / 输出 93,598）
