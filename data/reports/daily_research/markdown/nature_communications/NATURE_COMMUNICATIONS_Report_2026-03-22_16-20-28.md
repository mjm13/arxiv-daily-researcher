# 📊 Nature Communications 研究报告 (2026-03-22)

> 生成时间: 2026-03-22 16:20:28
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

- **总抓取**: 34 篇
- **及格论文**: 1 篇 (2.9%)
- **深度分析**: 1 篇

---

## ⭐ 及格论文详细分析

### 1. Network model for alignment, stitching and slice-to-volume 3D reconstruction of large-scale spatiall

**作者**: Yu Wang, Zaiyi Liu, Xiaoke Ma
**期刊/来源**: nature_communications
**发布日期**: 2026-03-20
**DOI**: [10.1038/s41467-026-71042-6](https://doi.org/10.1038/s41467-026-71042-6)

**评分**: 35.0 / 29.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical image segmentation | 1.0 | 6.0/10 | 6.0 |
| deep learning medical imaging | 1.0 | 7.0/10 | 7.0 |
| AI for diagnosis | 1.0 | 4.0/10 | 4.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 5.0/10 | 5.0 |
| multimodal medical imaging | 1.0 | 3.0/10 | 3.0 |
| foundation models medical imaging | 1.0 | 2.0/10 | 2.0 |

**评分理由**: 论文标题和摘要显示该研究专注于医学图像处理中的3D重建技术，特别是大尺度空间分辨切片的对齐、拼接和切片到体积重建。这与医学图像分析高度相关（8分），涉及图像分割的某些方面（6分），并可能使用深度学习技术（7分）。然而，论文未明确涉及疾病诊断（4分）、预后预测（0分）或手术规划（5分，仅间接相关）。多模态医学成像（3分）和基础模型（2分）的相关性较低，因为论文未强调这些方面。

</details>
<br>

!!! info Semantic Scholar TL;DR

    GEASO (Graph-based Elastic Alignment for Spatial-Omics data), a network-based algorithm for slice alignment, stitching and slice-to-volume 3D reconstruction, providing a versatile tool for analyzing spatial-omics data.

!!! tip deepseek-chat TL;DR

    该论文提出了一种网络模型，用于大尺度空间分辨切片的对齐、拼接和切片到体积3D重建，解决了医学图像处理中重建精度和效率的问题。

**关键词**: 3D reconstruction, medical image processing, slice alignment, image stitching, large-scale slices, spatially resolved slices, network model

**深度分析**:

#### 面向大规模空间分辨切片对齐、拼接及切片到体积三维重建的网络模型

**摘要**:

> 随着空间组学技术的发展，如何在保留空间信息的同时整合不同平台和模态的数据成为挑战。现有工具难以处理部分重叠、局部非刚性形变和大规模数据。本文提出GEASO（基于图的空间组学数据弹性对齐算法），一种基于网络的算法，用于切片对齐、拼接及切片到体积三维重建。GEASO利用图神经网络学习一致的斑点特征，并通过利用斑点连通性图的拓扑结构进行弹性配准，以解决切片的刚性变换和局部形变。同时，GEASO采用加速策略以适应大规模数据集。实验结果表明，GEASO在多种平台、模态和组织的切片对齐、拼接和三维重建方面优于现有基线方法，为空间组学数据分析提供了一个通用工具。

**创新点**:
- 提出GEASO算法，首次将图神经网络与弹性配准结合，用于空间组学数据的对齐、拼接和三维重建
- 利用斑点连通性图的拓扑结构处理局部非刚性形变，提高了对齐精度
- 设计了加速策略，使算法能够处理大规模空间组学数据集
- 提供了一个统一的框架，可跨多种平台和模态处理异质切片数据

<details>
<summary>方法</summary>

!!! info

    GEASO采用基于图神经网络的特征学习模块提取一致的斑点特征，构建斑点连通性图以捕获空间拓扑结构。通过弹性配准算法处理刚性变换和局部形变，利用图结构信息优化配准过程。采用加速策略（如降采样和高斯过程回归）提高计算效率，实现大规模数据处理。最终通过切片对齐和拼接完成三维重建。

</details>
<br>

**关键结果**:
- GEASO在多种空间组学数据集（包括人脑、小鼠脑、乳腺癌等）上实现了优于现有方法的对齐和拼接精度
- 算法能够有效处理局部非刚性形变和部分重叠的切片
- 加速策略使GEASO能够处理大规模数据集，展示了良好的可扩展性
- 在三维重建任务中，GEASO生成了更准确和连贯的体积模型

**技术栈**: 图神经网络（GNN）, 弹性配准算法, 斑点连通性图, 高斯过程回归, 降采样技术, Python编程语言, Scikit-learn库

<details>
<summary>优点</summary>

- 创新性地结合图神经网络和弹性配准，有效处理空间组学数据的复杂形变
- 算法设计兼顾精度和效率，通过加速策略适应大规模数据
- 在多种组织和模态上验证了算法的通用性和鲁棒性
- 提供了完整的开源代码和教程，便于学术和临床应用

</details>
<br>

<details>
<summary>局限</summary>

- 算法性能可能依赖于斑点特征的提取质量，对低质量数据敏感
- 尽管有加速策略，处理极大规模数据时计算成本仍可能较高
- 方法主要针对空间组学数据，在其他医学影像模态上的适用性未充分验证
- 对于高度异质或噪声严重的切片，对齐效果可能下降

</details>
<br>

**与研究方向的相关性**: ["与'医学图像分割和建模'相关：通过三维重建实现组织结构的体积建模", "与'深度学习'相关：核心采用图神经网络进行特征学习和对齐", "与'多模态医学数据融合'相关：处理不同平台和模态的空间组学数据整合", "与'鲁棒和可泛化的AI模型'相关：在多种数据集上验证了算法的通用性", "与'图像引导手术规划'间接相关：三维重建结果可为手术提供空间参考"]

---

## 📋 所有论文列表

### 1. ✅ Network model for alignment, stitching and slice-to-volume 3D reconstruction of large-scale spatially resolved slices

**作者**: Yu Wang, Zaiyi Liu, Xiaoke Ma
**期刊/来源**: nature_communications
**发布日期**: 2026-03-20
**DOI**: [10.1038/s41467-026-71042-6](https://doi.org/10.1038/s41467-026-71042-6)

**评分**: 35.0 / 29.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical image segmentation | 1.0 | 6.0/10 | 6.0 |
| deep learning medical imaging | 1.0 | 7.0/10 | 7.0 |
| AI for diagnosis | 1.0 | 4.0/10 | 4.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 5.0/10 | 5.0 |
| multimodal medical imaging | 1.0 | 3.0/10 | 3.0 |
| foundation models medical imaging | 1.0 | 2.0/10 | 2.0 |

**评分理由**: 论文标题和摘要显示该研究专注于医学图像处理中的3D重建技术，特别是大尺度空间分辨切片的对齐、拼接和切片到体积重建。这与医学图像分析高度相关（8分），涉及图像分割的某些方面（6分），并可能使用深度学习技术（7分）。然而，论文未明确涉及疾病诊断（4分）、预后预测（0分）或手术规划（5分，仅间接相关）。多模态医学成像（3分）和基础模型（2分）的相关性较低，因为论文未强调这些方面。

</details>
<br>

!!! info Semantic Scholar TL;DR

    GEASO (Graph-based Elastic Alignment for Spatial-Omics data), a network-based algorithm for slice alignment, stitching and slice-to-volume 3D reconstruction, providing a versatile tool for analyzing spatial-omics data.

!!! tip deepseek-chat TL;DR

    该论文提出了一种网络模型，用于大尺度空间分辨切片的对齐、拼接和切片到体积3D重建，解决了医学图像处理中重建精度和效率的问题。

**关键词**: 3D reconstruction, medical image processing, slice alignment, image stitching, large-scale slices, spatially resolved slices, network model

---

### 2. ❌ An ultrafast plenoptic-camera system for high-resolution 3D particle tracking in unsegmented scintillators

**作者**: Till Dieminger, Saúl Alonso-Monsalve, Christoph Alt, Claudio Bruschini, Noemi Bührer, Edoardo Charbon, Kodai Kaneyasu, Tim Weber, Matthew Franks, Davide Sgalaberna
**期刊/来源**: nature_communications
**发布日期**: 2026-03-21
**arXiv链接**: [https://arxiv.org/abs/2511.09442](https://arxiv.org/abs/2511.09442)
**DOI**: [10.1038/s41467-026-70918-x](https://doi.org/10.1038/s41467-026-70918-x)

**评分**: 2.0 / 29.0 ❌

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
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文主要研究用于粒子物理探测（如中微子、暗物质探测）的3D粒子追踪系统，核心是plenoptic相机系统和单光子雪崩二极管阵列传感器技术。虽然摘要末尾提到该技术未来可能扩展到医学成像领域，但论文当前内容完全专注于粒子探测器，与医学图像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学成像或医学基础模型等关键词无直接关联。因此，除'medical image analysis'因未来应用潜力得2分外，其余关键词均得0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种基于plenoptic相机和单光子雪崩二极管阵列的快速3D粒子追踪系统，用于未分割闪烁体中的高分辨率粒子探测，并在中微子探测案例中实现了200微米空间分辨率的事件重建。

<details open>
<summary>摘要翻译</summary>

> 摘要：中微子探测器、粒子量能器及部分暗物质探测器需要高密度、大体积的活性介质材料。为实现精确的三维粒子径迹重建，通常需对探测器进行极精细的模块化分割。然而，此类系统在建造上面临巨大挑战，且需要大量读出电子学通道，导致成本极为高昂。本文提出一种全新的基本粒子探测方案，可在非分割的大体积闪烁体中实现超快三维高分辨率成像。其关键技术为光场成像系统与时间分辨单光子雪崩二极管阵列图像传感器。通过结合光场相机与上述技术，我们实现了对闪烁体内单光子发射源点的三维重建。以中微子探测为案例的研究表明，该方案可实现完整事例重建，空间分辨率达200微米。此项工作为一类新型粒子探测器的发展开辟了道路，其性能有望通过未来技术迭代持续提升，并可扩展至切伦科夫光探测、医学成像及中子探测等领域。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Neutrino detectors, particle calorimeters and some dark matter detectors require dense and massive active materials. An extremely fine segmentation is desirable to achieve precise three-dimensional particle tracking. However, such systems introduce significant challenges in construction and demand a large number of readout electronics channels, leading to extremely high costs. In this article, we propose an alternative approach to elementary particle detection that enables ultrafast three-dimensional high-resolution imaging in large volumes of unsegmented scintillator. Enabling technologies are plenoptic systems and time-resolving single-photon avalanche diode array imaging sensors. Together, they enabled us, using a plenoptic camera, to reconstruct the origin of single photons in the scintillator. A case study focused on neutrino detection demonstrates full event reconstruction with a spatial resolution of two hundred micrometres. This work paves the way for a class of particle detectors whose capabilities should be further enhanced through future developments and expanded to Cherenkov light detection, medical imaging and neutron detection.

</details>
<br>

**关键词**: plenoptic camera, 3D particle tracking, unsegmented scintillator, single-photon avalanche diode array, neutrino detection, spatial resolution, event reconstruction, particle detectors

---

### 3. ❌ An epithelial morphogenetic program for maximal urine concentration

**作者**: Jane N. Warshaw, Sunhee Oh, Christopher Chaney, Bryanna L. Felan, Jonathan Pham, Chitkale Hiremath, Kenya Geshow, Hao Liu, Alejandra M. Rivera, Rain Wong, Song Zhang, Kevin M. Dean, Reto P. Fiolka, Michael T. Dellinger, Jonathan M. Whittamore, Thomas J. Carroll, Denise K. Marciano
**期刊/来源**: nature_communications
**发布日期**: 2026-03-21
**DOI**: [10.1038/s41467-026-70938-7](https://doi.org/10.1038/s41467-026-70938-7)

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

**评分理由**: 论文研究的是肾脏上皮形态发生与尿液浓缩的分子机制，使用小鼠模型、组织学、成像和基因表达分析，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划或多模态医学影像等主题。所有关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Findings offer definitive evidence that the inner medulla and aTL are essential for maximal urinary concentration, while revealing a non-canonical, morphogenetic role for claudin-10b.

!!! tip deepseek-chat TL;DR

    该研究揭示了肾脏集合管上皮通过形态发生程序（包括细胞重排和顶端收缩）实现尿液最大浓缩的机制，并确定了调控该过程的转录因子Hnf1b。

**关键词**: kidney, urine concentration, epithelial morphogenesis, collecting duct, Hnf1b, cell rearrangement, apical constriction, mouse model

---

### 4. ❌ Multi-omic identification of key transcriptional regulatory programs during endurance exercise training in rats

**作者**: Gregory R. Smith, Bingqing Zhao, Malene E. Lindholm, Archana Natarajan Raja, Mark Viggars, Hanna Pincas, Nicole R. Gay, Yifei Sun, Sindhu Vangeti, Yue Ge, Venugopalan D. Nair, James A. Sanford, Mary Anne S. Amper, Mital Vasoya, Kevin Smith, Irene Ramos, Stephen B. Montgomery, Elena Zaslavsky, Sue C. Bodine, Karyn A. Esser
**期刊/来源**: nature_communications
**发布日期**: 2026-03-21
**DOI**: [10.1038/s41467-026-70397-0](https://doi.org/10.1038/s41467-026-70397-0)

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

**评分理由**: 论文标题和摘要显示该研究是关于大鼠耐力运动训练中的多组学转录调控程序识别，属于运动生理学、分子生物学和基因组学领域。研究使用RNA测序、ATAC测序等组学技术分析基因表达和染色质可及性，与医学影像分析、深度学习、AI诊断、手术规划等关键词完全无关。所有关键词均未在论文内容中涉及。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An integrated analysis of chromatin accessibility, DNA methylation, mRNA expression, protein abundance and phosphorylation across eight tissues in fifty rats following endurance exercise training is conducted to identify coordinated epigenomic and transcriptional changes and determine key transcription factors involved.

!!! tip deepseek-chat TL;DR

    该研究通过多组学分析识别了大鼠耐力运动训练期间骨骼肌和心脏中的关键转录调控程序，发现组织特异性反应并确定了与运动适应相关的核心转录因子。

**关键词**: endurance exercise training, multi-omic analysis, transcriptional regulation, skeletal muscle, cardiac muscle, RNA sequencing, ATAC sequencing, transcription factors

---

### 5. ❌ Active learning in latent spaces enables rapid inverse design of ferroelectric ceramics for energy storage

**作者**: Zhaochen Xi, Zhentao Wang, Changqing Guo, Ke Xu, Weichen Zhao, Zhengqiao Li, Jian Bao, Haowei Zhou, Cong Zou, Houbing Huang, Di Zhou
**期刊/来源**: nature_communications
**发布日期**: 2026-03-20
**DOI**: [10.1038/s41467-026-70792-7](https://doi.org/10.1038/s41467-026-70792-7)

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

**评分理由**: 论文标题和摘要显示该研究聚焦于铁电陶瓷材料的逆向设计，用于能量存储应用，涉及活性学习、潜在空间建模和材料科学，与医学图像分析、临床决策支持、疾病诊断、手术规划等医疗领域完全无关。所有关键词均与论文内容无任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过活性学习和潜在空间建模，实现了铁电陶瓷材料的快速逆向设计，以优化其能量存储性能。

**关键词**: active learning, latent spaces, inverse design, ferroelectric ceramics, energy storage, materials science, machine learning

---

### 6. ❌ Modified letrozole vs GnRH antagonist protocols in ovarian aging women for IVF: an open-label, multicenter, randomized controlled trial

**作者**: Yang Zhao, Shuyun Zhao, Jiawen Xu, Jingbo Chen, Yun Lin, Yuhong Peng, Xuemei Li, Ping Pan, Jing Shu, Xiaojia Li, Jie Wang, Chu Chu, Rui Hu, Yiqi Yu, Yunting Zhang, Saif ur Rehman, Guanghui Dong, Dongzi Yang, Ricardo Azziz, Ben W. Mol
**期刊/来源**: nature_communications
**发布日期**: 2026-03-20
**DOI**: [10.1038/s41467-026-70964-5](https://doi.org/10.1038/s41467-026-70964-5)

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

**评分理由**: 论文标题和摘要显示这是一项关于体外受精（IVF）的临床随机对照试验，研究卵巢衰老女性中改良来曲唑方案与GnRH拮抗剂方案的比较。研究内容完全属于生殖医学、妇产科和临床试验领域，涉及药物方案、妊娠率、活产率等临床指标。所有评分关键词均属于医学影像分析、人工智能和计算机辅助诊断领域，与论文的临床生殖医学主题无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Although primary outcomes were similar between protocols, the mLP improved clinical pregnancy rates in fresh embryo transfers for women with diminished ovarian reserve, suggesting its potential to enhance in vitro fertilization efficacy in this population.

!!! tip deepseek-chat TL;DR

    这项多中心随机对照试验比较了改良来曲唑方案与GnRH拮抗剂方案在卵巢衰老女性IVF治疗中的效果，结果显示两种方案在持续妊娠率和活产率方面无显著差异，但改良来曲唑方案降低了促性腺激素使用剂量和OHSS风险。

**关键词**: IVF, ovarian aging, letrozole, GnRH antagonist, randomized controlled trial, live birth rate, ovarian hyperstimulation syndrome, clinical outcomes

---

### 7. ❌ When bubbles bounce or stick

**作者**: Xiangyu Zhang, Zhenbo Xu, Steven Wang, Kim Meow Liew
**期刊/来源**: nature_communications
**发布日期**: 2026-03-20
**DOI**: [10.1038/s41467-026-70921-2](https://doi.org/10.1038/s41467-026-70921-2)

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

**评分理由**: 论文标题和摘要（尽管摘要内容未提供）表明研究主题是气泡动力学（气泡弹跳或粘附），这属于流体力学或物理化学领域，与医学影像分析、人工智能、临床决策支持等医疗AI主题完全无关。所有关键词均未在论文内容中体现，因此相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究气泡在界面上的动力学行为（弹跳或粘附），并分析了相关物理机制和影响因素。

**关键词**: bubble dynamics, bubble bouncing, bubble sticking, interface behavior, fluid mechanics, physical mechanisms

---

### 8. ❌ Cooperativity in E. coli aspartate transcarbamoylase is tuned by allosteric breathing

**作者**: Robert C. Miller, Michael G. Patterson, Neti Bhatt, Xiaokun Pei, Nozomi Ando
**期刊/来源**: nature_communications
**发布日期**: 2026-03-20
**DOI**: [10.1038/s41467-026-70909-y](https://doi.org/10.1038/s41467-026-70909-y)

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

**评分理由**: 论文研究的是大肠杆菌天冬氨酸转氨甲酰酶（ATCase）的变构调节机制，属于结构生物学和生物化学领域，与医学影像分析、人工智能、临床决策支持等关键词完全无关。论文内容涉及酶动力学、变构效应、X射线晶体学等，没有任何医学影像、深度学习、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work shows that ATCase behaves like a flexible balloon whose global "breathing" motions directly regulate activity: compression enforces high cooperativity, inhibiting the enzyme, whereas expansion relieves this cooperativity and activates the enzyme.

!!! tip deepseek-chat TL;DR

    该研究通过结构生物学方法揭示了E. coli天冬氨酸转氨甲酰酶如何通过变构呼吸机制调节其协同性，发现酶活性位点和变构位点之间的动态耦合是实现变构调节的关键。

**关键词**: aspartate transcarbamoylase, allosteric regulation, cooperativity, enzyme kinetics, X-ray crystallography, E. coli, structural biology, protein dynamics

---

### 9. ❌ Functional and structural basis of a negative allostery within GABAB hetero-tetramers

**作者**: Cangsong Shen, Hongyang Ding, Shenlan Zhang, Chanjuan Xu, Binqian Zou, Suyu Ji, Yi-Ru Liu, YiZhong Li, Rui Zhou, Jiayin Liang, Dan-Dan Shen, Yuxuan Liu, Xuan Chen, Philippe Rondard, Jun He, Yan Zhang, Jean-Philippe Pin, Jianfeng Liu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-20
**DOI**: [10.1038/s41467-026-70640-8](https://doi.org/10.1038/s41467-026-70640-8)

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

**评分理由**: 论文研究GABAB受体的负变构调节机制，属于分子神经生物学和结构生物学领域，与医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态影像、基础模型等关键词完全无关。论文使用结构生物学方法（如冷冻电镜）研究蛋白质结构，不涉及任何医学影像技术或AI医疗应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that GABAB oligomers exist in neurons, and their function can be specifically affected by human disease-associated mutations, demonstrating their essential role for normal brain function.

!!! tip deepseek-chat TL;DR

    该研究揭示了GABAB受体异源四聚体中存在的负变构调节机制，通过结构生物学方法阐明了其功能和结构基础。

**关键词**: GABAB receptor, negative allostery, hetero-tetramer, structural basis, functional basis, cryo-EM, molecular mechanism, neurotransmitter receptor

---

### 10. ❌ Molecular mechanism of menthol-induced TRPV5 channel inhibition

**作者**: Angélica Méndez-Reséndiz, José J. De Jesús-Pérez, Gisela E. Rangel-Yescas, Tamara Rosenbaum, Vera Moiseenkova-Bell, León D. Islas
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70759-8](https://doi.org/10.1038/s41467-026-70759-8)

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

**评分理由**: 论文研究的是TRPV5离子通道的分子机制和薄荷醇的抑制作用，属于分子生物学、结构生物学和药理学领域。所有评分关键词均涉及医学影像分析、人工智能、深度学习、诊断、预后、手术规划等，与论文内容完全无关。论文使用电生理学和冷冻电镜技术，不涉及任何医学影像分析或AI方法。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that the monoterpene menthol, commonly used for pain and inflammation management, is an inhibitor of TRPV5, and it is suggested that menthol could serve as a scaffold for developing channel-targeting modulators.

!!! tip deepseek-chat TL;DR

    该研究发现薄荷醇通过阻断离子传导抑制TRPV5通道，并通过冷冻电镜揭示了其与关键残基W583相互作用的分子结构，为开发通道靶向调节剂提供了基础。

<details open>
<summary>摘要翻译</summary>

> TRPV5通道在钙稳态调节中起关键作用，并与多种病理生理状态相关。本研究发现，常用于疼痛与炎症管理的单萜类化合物薄荷醇是TRPV5的抑制剂。电生理实验表明，薄荷醇通过缓慢阻断机制抑制离子传导。利用单颗粒冷冻电镜技术，我们解析了薄荷醇结合状态下的TRPV5结构，显示薄荷醇与W583残基相互作用——该残基此前已被证实参与通道渗透、门控调控及内源性调节因子的结合。这些发现拓展了TRPV5调节剂的种类，并提示薄荷醇可作为开发通道靶向调节剂的分子骨架。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> TRPV5 channels play a critical role in calcium homeostasis and are implicated in various pathophysiological conditions. Here, we demonstrate that the monoterpene menthol, commonly used for pain and inflammation management, is an inhibitor of TRPV5. Electrophysiology experiments reveal that menthol blocks ion conduction through a slow blocker mechanism. Using single-particle cryo-EM, we determine the structure of menthol-bound TRPV5, which shows menthol interacting with W583, a residue previously implicated in channel permeation, gating and binding of endogenous modulators. These findings expand the repertoire of TRPV5 modulators and suggest that menthol could serve as a scaffold for developing channel-targeting modulators.

</details>
<br>

**关键词**: TRPV5 channel, menthol inhibition, ion conduction block, cryo-EM structure, W583 residue, calcium homeostasis, channel modulator, molecular mechanism

---

### 11. ❌ FGFR signaling establishes spatial gradients of secretory cell identities along the airway proximal-distal axis

**作者**: Alexandros Sountoulidis, Jonas Theelke, Andreas Liontos, Alexandra B. Firsova, Orane Eliot, Janine Koepke, Pamela Millar-Büchner, Louise Mannerås-Holm, Åsa K. Björklund, Athanasios Fysikopoulos, Antonia Kelm, Eleni Bouloukou, Konstantin Gaengel, Fredrik Bäckhed, Christer Betsholtz, Werner Seeger, S Bellusci, Christos Samakovlis
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70842-0](https://doi.org/10.1038/s41467-026-70842-0)

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

**评分理由**: 该论文研究的是肺气道分泌细胞的异质性、空间组织和分化机制，使用单细胞分辨率分析、基因表达梯度、谱系追踪和Fgfr2b信号通路研究。所有评分关键词都涉及医学影像分析、人工智能、深度学习、诊断、预后、手术规划或多模态成像，而该论文完全不涉及这些技术或应用领域。论文属于基础细胞生物学和发育生物学研究，而非医学影像或人工智能领域。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that Fgfr2b regulates the airway patterning by inducing and maintaining high levels of lipid biosynthesis and vesicle trafficking in distal airways and down-regulating innate-immunity genes in vivo and in airway organoids.

!!! tip deepseek-chat TL;DR

    该论文研究了肺气道分泌细胞沿近端-远端轴的空间异质性分化机制，发现Fgfr2b信号通路通过调节脂质代谢和先天免疫基因表达梯度来建立和维持气道模式。

<details open>
<summary>摘要翻译</summary>

> 分泌细胞是肺气道的主要结构和功能组成部分。其异质性、空间组织模式和特化机制尚未被完全阐明。本研究通过单细胞分辨率对肺分泌细胞类型进行分析。在气道上皮中，我们发现了沿近端-远端气道轴存在两组对立且部分重叠的基因表达梯度，它们叠加在一个编码解毒功能的通用基因程序之上。其中一个梯度程序在近端气道表达升高，涉及先天免疫功能；而另一个梯度程序在远端气道富集，编码脂质代谢和抗原呈递功能。位于中间位置的细胞则同时表达中等水平的两种梯度程序，形成了一个向两端分化的连续谱系。发育过程中的谱系追踪分析揭示，这些梯度是在出生后由共同的上皮祖细胞中依次建立的。我们证明，Fgfr2b通过诱导并维持远端气道高水平的脂质生物合成与囊泡运输，同时在体内和气道类器官模型中下调先天免疫相关基因，从而调控气道模式的形成。本分析为研究上皮及肺组织组织结构提供了一个框架，有助于更好地理解细胞在组织水平病理学中的作用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Secretory cells are major structural and functional constituents of the lung airways. Their heterogeneity, spatial organization and specification mechanisms are partially understood. Here, we analyze secretory lung cell-types at single-cell resolution. In the airway epithelium, we find opposing, partially overlapping gene-expression gradients along the proximal-distal airway axis superimposed on a general gene program encoding detoxification. One graded program is elevated proximally and relates to innate immunity, whereas the other is enriched distally, encoding lipid metabolism and antigen presentation. Intermediately positioned cells express moderate levels of both graded programs creating a differentiation continuum towards each end. Lineage tracing analysis during development reveals the sequential establishment of the gradients in common epithelial progenitors postnatally. We show that Fgfr2b regulates the airway patterning by inducing and maintaining high levels of lipid biosynthesis and vesicle trafficking in distal airways and down-regulating innate-immunity genes in vivo and in airway organoids. Our analysis offers a framework for studying epithelial and lung tissue organization to better understand cellular roles in tissue-level pathology.

</details>
<br>

**关键词**: airway epithelium, secretory cells, spatial gradients, Fgfr2b signaling, single-cell analysis, lipid metabolism, innate immunity, lung development

---

### 12. ❌ Prasugrel inhibits TLR7-driven autoimmunity in systemic lupus erythematosus by acetylating cGAS

**作者**: Zeng-Lin Guo, Li-Ming Sun, Shu Jiang, Ming Zhao, Yuhui Li, Jinjing Qian, Yakai Fu, Chao Wu, Ying Yuan, Wen Xue, Shao-Zhen Jiang, Sen-Chao Yuan, Xucheng Lv, Xingxing Yang, Lehua Yin, Peng-Peng Zhu, Yu Yu, Xin Xu, Kai Wang, Qiuying Han
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70794-5](https://doi.org/10.1038/s41467-026-70794-5)

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

**评分理由**: 论文研究的是系统性红斑狼疮（SLE）的分子机制和药物治疗，聚焦于cGAS酶在SLE发病中的作用以及抗血小板药物普拉格雷通过乙酰化cGAS抑制其活性的治疗机制。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等医学影像和人工智能技术领域，而本论文完全属于分子生物学、免疫学和药物发现领域，未涉及任何医学影像数据、图像分析技术或AI模型。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work elucidates the essential role of cGAS in SLE pathogenesis and presents prasugrel as a promising therapeutic option with immediate translational potential.

!!! tip deepseek-chat TL;DR

    该研究发现cGAS在系统性红斑狼疮（SLE）中被显著激活，并通过筛选FDA批准药物鉴定出抗血小板药物普拉格雷能通过乙酰化cGAS抑制其活性，在动物模型和患者细胞中显示出治疗SLE的显著疗效，同时发现血浆cGAMP可作为预测普拉格雷反应的潜在生物标志物。

<details open>
<summary>摘要翻译</summary>

> 系统性红斑狼疮（SLE）具有复杂、多因素的病因学，这导致其缺乏根治方法且治疗效果有限。本文报道，在SLE患者中环状GMP-AMP合成酶（cGAS）被显著激活。我们进一步证明，cGAS基因缺失能保护小鼠免受TLR7激动剂咪喹莫特（IMQ）诱导的狼疮样症状。在对3,159种FDA批准药物的筛选中，我们鉴定出抗血小板药物普拉格雷是一种有效的cGAS抑制剂。机制研究表明，普拉格雷通过直接乙酰化作用，破坏了DNA触发的cGAS液相凝聚与活化。引人注目的是，我们发现普拉格雷在小鼠模型和患者细胞中均展现出治疗SLE的显著疗效。重要的是，我们报告了SLE患者血浆中环状GMP-AMP（cGAMP）水平升高，并确定其可作为预测普拉格雷治疗反应的潜在生物标志物。因此，我们的工作阐明了cGAS在SLE发病机制中的关键作用，并提出普拉格雷作为一种具有即时转化潜力的前景治疗选择。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Systemic lupus erythematosus (SLE) has a complex, multifactorial etiology, which contributes to a lack of definitive cure and limited treatment efficacy. Here, we report that cyclic GMP-AMP synthase (cGAS) is significantly activated in SLE patients. We further demonstrate that cGAS deletion protects mice from lupus-like symptoms induced by the TLR7 agonist imiquimod (IMQ). In a screen of 3,159 FDA-approved drugs, we identify the antiplatelet agent prasugrel as a potent cGAS inhibitor. Mechanistically, prasugrel disrupts the DNA-triggered liquid phase condensation and activation of cGAS via direct acetylation. Strikingly, we find that prasugrel exhibits remarkable efficacy in treating SLE in both mouse models and patient cells. Importantly, we report elevated plasma cyclic GMP-AMP (cGAMP) in SLE patients and identify it as a potential biomarker for predicting prasugrel response. Thus, our work elucidates the essential role of cGAS in SLE pathogenesis and presents prasugrel as a promising therapeutic option with immediate translational potential.

</details>
<br>

**关键词**: systemic lupus erythematosus, cGAS, prasugrel, acetylation, TLR7, cGAMP biomarker, drug repurposing, autoimmunity

---

### 13. ❌ Significant stability enhancement in photocatalytic CO2 reduction via flow-driven strategies

**作者**: Hyunju Jung, Hyo Sang Jeon, Min Gyu Kim, Aqil Jamal, Issam Gereige, Chansol Kim, Ha‐Kyun Jung
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70542-9](https://doi.org/10.1038/s41467-026-70542-9)

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

**评分理由**: 论文研究的是光催化CO2还原的稳定性问题，属于化学工程、材料科学和能源领域，与医学图像分析、人工智能临床决策支持等医学领域完全无关。论文内容涉及催化剂、流动控制、X射线吸收光谱等，未提及任何医学成像、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了光催化CO2还原中稳定性不足的问题，通过优化CO2和H2O流动条件，使TiO2等光催化剂在15天内保持80%初始活性，稳定性提升达50倍。

<details open>
<summary>摘要翻译</summary>

> 实现长期稳定性仍是光催化二氧化碳（CO<sub>2</sub>）还原领域面临的主要挑战。与自然光合作用不同，由于催化剂失活和表面降解，大多数人工系统在数小时内便表现出严重的活性下降。本研究探讨了在光催化过程中持续通入CO<sub>2</sub>和H<sub>2</sub>O气流的影响。在优化的气流条件下，广泛使用的光催化剂如二氧化钛（TiO<sub>2</sub>）、氧化锌（ZnO）、硫化镉（CdS）和氮化碳（C<sub>3</sub>N<sub>4</sub>）的运行稳定性提升了高达50倍，其中TiO<sub>2</sub>在15天内保持了其初始活性的80%。CO<sub>2</sub>气流比H<sub>2</sub>O气流起着更为主导的作用，它能减轻产物积累并防止催化剂失活。表面和结构分析表明，无气流系统存在产物和中间体积累问题，而气流辅助系统则能保持洁净的催化表面。X射线吸收光谱证实了气流条件下结构降解受到抑制。本研究确立了气流控制作为实现持久性光催化CO<sub>2</sub>还原的一项设计原则，为可规模化的太阳能至化学能转化提供了可行路径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Achieving long-term stability remains a major challenge in photocatalytic CO<sub>2</sub> reduction. Unlike natural photosynthesis, most artificial systems exhibit severe activity losses within hours due to catalyst deactivation and surface degradation. This study investigates the effect of continuous CO<sub>2</sub> and H<sub>2</sub>O flow during the photocatalytic process. Under optimized flow conditions, widely used photocatalysts such as TiO<sub>2</sub>, ZnO, CdS, and C<sub>3</sub>N<sub>4</sub> show up to 50-fold improvement in operational stability, with TiO<sub>2</sub> retaining 80% of its initial activity over 15 days. CO<sub>2</sub> flow plays a more dominant role than H<sub>2</sub>O flow, mitigating product accumulation and preventing catalyst deactivation. Surface and structural analyses reveal that systems without flows suffer from product and intermediate accumulation, while flow-enabled systems maintain clean catalytic surfaces. X-ray absorption spectroscopy confirms the suppression of structural degradation under flow. Here, we establish flow control as a design principle for durable photocatalytic CO<sub>2</sub> reduction, providing a pathway for scalable solar-to-chemical energy conversion.

</details>
<br>

**关键词**: photocatalytic CO2 reduction, stability enhancement, flow-driven strategies, catalyst deactivation, TiO2, X-ray absorption spectroscopy, solar-to-chemical energy conversion

---

### 14. ❌ Behavioral shifts mask the success of legislation and outreach for endangered species recovery

**作者**: Victoria J. Bakker, Daniel F. Doak, Alacia Welch, L. Joseph Burnett, María C. Porras Peña, Joseph Brandt, Sharon A. Poessel, Steve Kirkland, Rachel Wolstenholme, Daniel Ryan, Mike M. Stake, Arianna Punzalan, Nacho Vilchis, Melissa A. Braham, Myra E. Finkelstein
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-69617-4](https://doi.org/10.1038/s41467-026-69617-4)

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

**评分理由**: 论文研究的是濒危物种（加州秃鹫）保护措施的有效性评估，属于生态学和保护生物学领域，与医学影像分析、人工智能、临床决策支持等医疗技术主题完全无关。论文内容涉及野生动物行为变化、铅中毒、立法效果评估等生态保护问题，没有任何医学影像、深度学习、疾病诊断或手术规划相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究评估了加州秃鹫保护措施（铅弹药禁令和公众宣传）的有效性，发现秃鹫和人类的行为变化掩盖了这些措施在降低血铅水平和死亡率方面的实际成效。

<details open>
<summary>摘要翻译</summary>

> 保护生物学中的一个根本性挑战在于评估恢复行动的有效性，以优化濒危物种的管理策略。近年来，全球范围内因中毒事件导致数量锐减的食腐鸟类受到广泛关注，如何采取有效措施应对其濒危状况成为焦点。一个标志性案例是极度濒危的加州神鹫（Gymnogyps californianus）的恢复工作，其死亡的主要原因是摄食动物尸体中含铅弹药导致的中毒。尽管在美国加利福尼亚州投入了大量资源，包括开展公众宣传运动以及实施两项针对含铅弹药的立法禁令，神鹫的铅相关死亡率却有所上升。本文揭示，两类行为转变可以解释观测到的神鹫铅暴露增加现象：神鹫更趋向于野外觅食与扩大活动范围，以及人类对野猪（Sus scrofa）捕猎活动的增加。在排除这些趋势的影响后，我们发现含铅弹药禁令和公众宣传行动均显著降低了加州神鹫的血铅水平，从而减少了死亡率。我们的分析揭示了一种动态机制：不断变化的生态条件掩盖了立法与宣传工作的真实成效。鉴于全球变化的快速性，此类动态机制可能广泛存在于多种情境中，这凸显了对恢复行动进行全面评估的重要性——因为行为模式与威胁因素的演变可能模糊评估结果。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> A fundamental challenge in conservation is assessing the efficacy of recovery actions to optimize endangered species management. Considerable recent attention has focused on effective measures to counter the endangerment of avian scavengers, which have declined worldwide, primarily due to poisoning. One iconic example is efforts to recover the critically endangered California condor (Gymnogyps californianus), whose leading cause of death is poisoning from ingesting lead-based ammunition in carcasses. Despite enormous resources expended in California, USA, including implementation of public outreach campaigns and two legislative bans on lead ammunition, lead-related mortality of condors has increased. Here we show that two types of behavioral shifts explain the observed increases in condor lead exposure: wilder foraging and ranging by condors and increased shooting of wild pigs (Sus scrofa) by humans. After accounting for these trends, we show that both lead ammunition bans and public outreach efforts have significantly reduced condor blood lead levels in California, lowering mortality. Our analyses uncover a dynamic in which changing ecological conditions mask the true efficacy of legislation and outreach. Given rapid global change, such dynamics are likely operating in many settings, underscoring the importance of comprehensive evaluations of recovery actions, which can be obscured by shifting behaviors and threats.

</details>
<br>

**关键词**: endangered species recovery, California condor, lead poisoning, behavioral shifts, legislation effectiveness, conservation management, wildlife conservation, population recovery

---

### 15. ❌ Efficient control of enterochromaffin versus islet differentiation from human pluripotent stem cell-derived pancreatic progenitors

**作者**: Paraish S. Misra, Emily C. McGaugh, Haiyang Huang, Alex Cho, Justin Lin, Farida Sarangi, Amanda Oakie, Rangarajan Sambathkumar, Youngmin Song, Valeria Fabriciova, Romana Bohuslavová, Gabriela Pavlínková, M. Cristina Nostro
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70666-y](https://doi.org/10.1038/s41467-026-70666-y)

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

**评分理由**: 论文研究的是人类多能干细胞向胰腺内分泌细胞分化的分子机制和优化方法，属于干细胞生物学和糖尿病治疗领域，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或基础模型等关键词。所有关键词与论文内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Different methods of pancreatic endocrine differentiation from human pluripotent stem cells (hPSCs) are compared and sequences of patterning that can selectively increase the frequencies of islet-like or off-target enterochromaffin (EC)-like cells are established, thereby significantly increasing islet-like cellular yield and glucose-stimulated insulin secretion.

!!! tip deepseek-chat TL;DR

    该研究通过比较不同分化方法，揭示了人类多能干细胞向胰岛样细胞与肠嗜铬样细胞分化的分子机制，并建立了选择性提高胰岛样细胞产量的分化框架，为糖尿病细胞治疗提供了新策略。

<details open>
<summary>摘要翻译</summary>

> 解析指导胰腺发育的分子信号对于开发治疗糖尿病的β细胞替代疗法至关重要。本研究比较了从人多能干细胞（hPSCs）向胰腺内分泌细胞分化的不同方法，建立了可选择性提高胰岛样细胞或脱靶肠嗜铬（EC）样细胞出现频率的模式化序列，从而显著提升胰岛样细胞产量及葡萄糖刺激的胰岛素分泌水平。通过利用一种产生胰腺EC样细胞的发育异常小鼠胰岛模型，我们发现持续表达的神经元素3（NGN3）是人类与小鼠胰腺EC样细胞分化过程中共有的保守特征。最后，通过比较不同模式化策略获得的细胞表型，我们观察到内分泌亚型在经典谱系标志物表达上存在显著差异。这些发现不仅拓展了我们对胰腺内分泌谱系定向与细胞特性的理解，更为指导构建用于研究和治疗应用的定制化hPSC胰岛建立了逻辑分化的理论框架。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Knowledge of the molecular cues guiding pancreatic development is critical to developing beta cell replacement therapies for the treatment of diabetes. We compare different methods of pancreatic endocrine differentiation from human pluripotent stem cells (hPSCs) and establish sequences of patterning that can selectively increase the frequencies of islet-like or off-target enterochromaffin (EC)-like cells, thereby significantly increasing islet-like cellular yield and glucose-stimulated insulin secretion. Using a model of disrupted murine islet development that gives rise to pancreatic EC-like cells, we identify persistent Neurogenin 3 (NGN3) expression as a conserved feature associated with human and murine pancreatic EC-like cell differentiation. Finally, by comparing the phenotypes obtained through different patterning strategies, we observe that endocrine subtypes can vary significantly in their expression of canonical lineage markers. In addition to expanding our understanding of pancreatic endocrine lineage allocation and identity, these findings establish a logical differentiation framework to guide the generation of designer hPSC-islets for research and therapeutic applications.

</details>
<br>

**关键词**: human pluripotent stem cells, pancreatic differentiation, islet-like cells, enterochromaffin cells, Neurogenin 3, beta cell replacement therapy, diabetes, lineage specification

---

### 16. ❌ Helicity-selective and spectrally tunable chiral thermal emissions

**作者**: Kaili Sun, Haoye Qin, Mengqi Liu, Feng Chen, Yangjian Cai, Pinghui Wu, Cheng-Wei Qiu, Zhifen Han
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70825-1](https://doi.org/10.1038/s41467-026-70825-1)

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

**评分理由**: 该论文研究的是热光子学中的手性热发射调控，属于光学、纳米光子学和热物理领域，与医学图像分析、人工智能临床决策支持等医学领域完全无关。论文内容涉及非局域超表面、手性热发射、圆偏振调控、中红外光谱等物理概念，没有任何医学图像、疾病诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种各向异性热超表面，通过温度调控实现了中红外波段手性可切换和波长可调的圆偏振相干热发射，为对映体识别等应用提供了紧凑平台。

<details open>
<summary>摘要翻译</summary>

> 将非局域超表面与热光子学相结合，已赋予热辐射以时空相干性和手性特征。然而，当前热发射器的静态响应限制了其更广泛的应用，特别是在高精度传感领域。本文提出了一种各向异性热超表面，其专门利用热光子学固有的高温特性，在中红外波段实现螺旋性可切换且波长可调的圆偏振相干热辐射。通过精心的设计，我们实现了一对具有相反手性和显著发射圆二色性的高Q值准导模共振，并在实验中演示了通过250 K的温度变化，可在约100纳米波长范围内实现螺旋性可切换的圆偏振热辐射，同时具备高时间相干性（Q > 150）和强发射圆二色性（>0.8）。我们进一步揭示，简单的几何设计即可实现完整的偏振调控。该平台为片上应用提供了一条紧凑且可扩展的路径，包括用于对映体识别的圆二色光谱学。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Integrating nonlocal metasurfaces with thermal photonics has endowed thermal emissions with temporal and spatial coherence, as well as chirality. However, the static response of current thermal emitters hinders their broader applications, especially in high-precision sensing. Here, we present an anisotropic thermal metasurface that harnesses exclusively elevated temperatures inherent in thermal photonics to achieve helicity-switchable and wavelength-tunable circularly polarized coherent thermal emissions in the mid-infrared. Through a meticulous design to achieve a pair of high-Q quasi-guided mode resonances with opposite chirality and significant emission circular dichroism, we experimentally demonstrate helicity-switchable circularly polarized thermal emissions with high temporal coherence (Q > 150) and strong emission circular dichroism (>0.8) over a ~ 100 nm wavelength range through a temperature change of 250 K. We further reveal that simple geometric design enables full polarization tailoring. Our platform offers a compact and scalable pathway toward on-chip applications including circular dichroism spectroscopy for enantiomer identification.

</details>
<br>

**关键词**: thermal metasurface, chiral thermal emissions, circularly polarized emissions, mid-infrared, helicity-switchable, wavelength-tunable, circular dichroism, enantiomer identification

---

### 17. ❌ Maternal obesity disrupts epigenetic reprogramming via peroxisomal-dependent phospholipid-methyl uncoupling during zygotic genome activation

**作者**: Xiao-Guohui Zhang, Linli Yang, Xu Feng, Yu-Wei Zhang, Lei Guo, Sicong Huang, Tie‐Gang Meng, Peiying Li, Lei-Ning Chen, Ruibao Su, Jun-Yu Ma, Xiao-Yan Fan, Jiali Su, Yue-Fan Wang, Lan-Fang Luo, Qing-Yuan Sun, Ng-Shyh Chang, S -M Luo, Xiang-Hong Ou
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70492-2](https://doi.org/10.1038/s41467-026-70492-2)

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

**评分理由**: 论文研究母体肥胖如何通过过氧化物酶体依赖的磷脂-甲基解偶联破坏表观遗传重编程，影响合子基因组激活和胚胎发育。这是一项基础生物学研究，涉及脂质代谢、表观遗传学和发育生物学。所有评分关键词均与医学影像分析、人工智能、深度学习、诊断、预后、手术规划、多模态成像或基础模型相关，而论文完全不涉及这些领域。论文没有使用任何医学影像技术，没有应用人工智能或机器学习方法，没有进行疾病诊断或预后预测，也没有涉及手术规划。因此，所有关键词的相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that obesity disrupts very-long-chain fatty acids storage in oocytes and downregulates PEX13, impairing peroxisomal protein import in 2-cell embryos and revealing a phospholipid-methyl coupling mechanism underlying obesity-associated embry development, offering novel therapeutic entry points to improve fertility in metabolic disorders.

!!! tip deepseek-chat TL;DR

    该研究发现母体肥胖通过破坏过氧化物酶体β-氧化，导致极长链脂肪酸代谢异常和磷脂-甲基循环解偶联，从而抑制组蛋白H3K4me3擦除和合子基因组激活，最终损害胚胎发育；补充长链脂肪酸或过表达PEMT可恢复这一过程。

<details open>
<summary>摘要翻译</summary>

> 母体肥胖已知会引起全身性脂质代谢紊乱，但其对母源-合子转换（MZT）期间脂质重编程的影响尚不清楚。本研究揭示，肥胖会破坏卵母细胞中极长链脂肪酸（VLCFAs）的储存，并下调PEX13，从而损害2-细胞胚胎中过氧化物酶体蛋白的输入。正常情况下，过氧化物酶体β-氧化将卵母细胞储存的VLCFAs转化为中链和长链脂肪酸，这些脂肪酸驱动甘油三酯合成，并促进磷脂酰乙醇胺（PE）甲基化为磷脂酰胆碱（PC）。这一代谢通量消耗甲基供体，从而促进H3K4me3的擦除和合子基因组激活（ZGA）。在肥胖小鼠中，VLCFAs缺乏和PEX13功能障碍导致代谢-表观遗传解偶联，耗竭脂滴并维持H3K4me3水平，从而抑制ZGA和囊胚发育。重要的是，补充长链脂肪酸或过表达PEMT可恢复磷脂-甲基循环，挽救表观遗传重编程和胚胎发育。我们的研究确立了过氧化物酶体β-氧化作为MZT所必需的代谢-表观遗传枢纽，并揭示了肥胖相关胚胎发育缺陷背后的磷脂-甲基偶联机制，为改善代谢紊乱患者的生育能力提供了新的治疗切入点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Maternal obesity is known to cause systemic lipid dysregulation, yet its effect on lipid reprogramming during the maternal-to-zygotic transition (MZT) remains unknown. Here we show that obesity disrupts very-long-chain fatty acids (VLCFAs) storage in oocytes and downregulates PEX13, impairing peroxisomal protein import in 2-cell embryos. Normally, peroxisomal β-oxidation converts oocyte-stored VLCFAs into medium- and long-chain fatty acids, which fuel triglyceride synthesis and drive phosphatidylethanolamine (PE) methylation to phosphatidylcholine (PC). This metabolic flux consumes methyl donors to facilitate H3K4me3 erasure and zygotic genome activation (ZGA). In obese mice, VLCFAs deficiency and PEX13 dysfunction lead to metabolic-epigenetic uncoupling, depleting lipid droplets and sustaining H3K4me3, thereby suppressing ZGA and blastocyst development. Importantly, supplying long-chain fatty acids or overexpressing PEMT restore the phospholipid-methyl cycle, rescuing epigenetic reprogramming and embryonic development. Our findings establish peroxisomal β-oxidation as a metabolic-epigenetic nexus essential for MZT and reveal a phospholipid-methyl coupling mechanism underlying obesity-associated embry development, offering novel therapeutic entry points to improve fertility in metabolic disorders.

</details>
<br>

**关键词**: maternal obesity, peroxisomal β-oxidation, epigenetic reprogramming, zygotic genome activation, phospholipid-methyl cycle, embryonic development, metabolic-epigenetic coupling, PEX13

---

### 18. ❌ Olfactory cleft biopsy analysis of Alzheimer’s disease pathobiology across disease stages

**作者**: Vincent M. D’Anniballe, Sarah Kim, John B. Finlay, Michael Wang, Tiffany Ko, Sheng Luo, Heather E. Whitson, Kim G. Johnson, Bradley J. Goldstein
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70099-7](https://doi.org/10.1038/s41467-026-70099-7)

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

**评分理由**: 论文研究阿尔茨海默病的早期病理生物学，通过嗅觉刷活检和单细胞RNA测序分析神经组织，属于神经科学和分子生物学领域。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等，而论文完全不涉及医学影像技术、图像处理或AI模型开发，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    These findings establish a platform permitting analysis of neural tissue in AD at its earliest stages, and corroborate heightened CD8 T-cell activation by flow cytometry.

!!! tip deepseek-chat TL;DR

    该研究通过嗅觉刷活检和单细胞RNA测序分析阿尔茨海默病早期阶段的神经组织，发现即使在临床前阶段也能检测到神经炎症T细胞、髓样细胞和嗅觉神经元的变化，为分析疾病最早阶段的神经组织提供了平台。

<details open>
<summary>摘要翻译</summary>

> 阿尔茨海默病（Alzheimer's Disease, AD）是一种影响全球数百万人的神经退行性疾病。界定其早期病理生物学事件仍具挑战性，部分原因在于神经组织的难以获取性。由于嗅觉神经元易于采集，且嗅觉丧失在AD中普遍存在，本研究对对照组个体、脑脊液（cerebrospinal fluid, CSF）生物标志物确认的AD患者，以及认知正常但CSF生物标志物阳性（提示处于临床前AD阶段）的个体进行了嗅觉刷活检评估。通过单细胞RNA测序（涉及22名受试者），我们发现在临床前AD受试者中即可检测到保守的神经炎症性T细胞、髓系细胞和嗅觉神经元的变化，并通过流式细胞术证实了CD8 T细胞活化增强。嗅觉上皮中活化的记忆T细胞状态是临床前AD的一个标志，这与晚期疾病中观察到的CSF T细胞表型相似，同时伴随小胶质细胞样炎症程序以及嗅觉神经元炎症性损伤的证据。综上，我们的研究建立了一个可在AD最早阶段分析神经组织的平台。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Alzheimer's Disease (AD) is a neurodegenerative condition affecting millions worldwide. Defining early pathobiological events remains challenging, in part due to inaccessibility of neural tissue. Because olfactory neurons are accessible, and olfactory loss is prevalent in AD, we evaluated olfactory brush biopsies from controls, individuals with cerebrospinal fluid (CSF) biomarker-confirmed AD, and cognitively typical individuals whose positive CSF biomarkers signal a pre-clinical AD stage. Here we show via single cell RNA-sequencing (n = 22 subjects) conserved neuroinflammatory T cell, myeloid cell, and olfactory neuron changes detectable even in pre-clinical AD subjects, and corroborate heightened CD8 T-cell activation by flow cytometry. Activated memory T cell states in the olfactory epithelium were a hallmark of pre-clinical AD, paralleling CSF T cell phenotypes seen in advanced disease, accompanied by both microglia-like inflammatory programs and evidence of olfactory neuron inflammatory injury. Together, our findings establish a platform permitting analysis of neural tissue in AD at its earliest stages.

</details>
<br>

**关键词**: Alzheimer's disease, olfactory biopsy, single-cell RNA sequencing, neuroinflammation, T cells, pre-clinical stage, neural tissue analysis, CSF biomarkers

---

### 19. ❌ Biomimetic hairy affective-touch sensory AI interface

**作者**: Jianlong Hong, Yan Xiao, Yuqi Chen, Shengshun Duan, Shengxin Xiang, Xiao Wei, Heng Zhang, Li Liu, Jun Xia, Wei Lei, Qiongfeng Shi, Caroline Lee, Jun Wu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70334-1](https://doi.org/10.1038/s41467-026-70334-1)

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

**评分理由**: 论文研究的是仿生毛发触觉传感接口用于情感识别，属于触觉传感、人机交互和情感计算领域。所有评分关键词均针对医学影像分析（CT/MRI/超声图像处理、疾病诊断、手术规划等），而本文完全不涉及医学影像数据、医学诊断或临床决策支持。论文虽然使用了卷积神经网络和大型语言模型，但应用于触觉信号的情感识别，而非医学影像分析。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A biomimetic hairy sensing interface is developed to capture affective touch's spatiotemporal characteristics and intrinsic features, allowing for accurate emotion recognition, and enables real-time emotion recognition with 82.37% accuracy across individualized touch patterns.

!!! tip deepseek-chat TL;DR

    该研究开发了一种仿生毛发触觉传感接口，通过混合神经网络实现了对个性化触摸模式的情感识别，准确率达82.37%，推动了人机情感交互的发展。

<details open>
<summary>摘要翻译</summary>

> 触觉情感感知能力的缺失限制了人工智能解码人类肢体接触中编码的社会行为。本研究开发了一种仿生毛发传感界面，用于捕捉情感性触觉的时空特征与内在属性，从而实现精准的情绪识别。该毛发界面在外部刺激下无需尖峰编码电路即可直接产生类神经电脉冲信号。通过双级毛发结构、均质纳米网制造工艺及等值线理论，该界面实现了高力检测灵敏度（0.67 N<sup>-1</sup>）与空间精度（在100 cm<sup>2</sup>范围内达到1.61 mm定位准确度）。该界面复现了生物C-LTMRs（C类低阈值机械感受器）的行为特征，首次建立了情感触觉转导的生物电子模拟系统。结合混合神经网络架构（卷积神经网络与情境化大语言模型），该系统能对个性化触摸模式实现实时情绪识别，准确率达82.37%。这种神经形态触觉框架促进了人机情感交互的闭环实现，推动着具备自然情感交流能力的人形机器人向前发展。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The absence of tactile emotion perception limits artificial intelligence (AI) in decoding social behaviors encoded in human physical contact. Here, a biomimetic hairy sensing interface is developed to capture affective touch's spatiotemporal characteristics and intrinsic features, allowing for accurate emotion recognition. The hairy interface directly induces neuromimetic electric pulse signals under external stimuli without the need for a spike coding circuit. Through a bistage hairy structure, homogeneous nanomesh manufacturing process and isoline theory, it achieves high force detection sensitivity (0.67 N<sup>-1</sup>) and spatial precision (1.61 mm localization accuracy across 100 cm<sup>2</sup>). The interface replicates biological C-LTMRs' behavior, establishing the first bioelectronic analog of affective touch transduction. Integration with hybrid neural network setting (convolutional neural network and contextual large language model) enables real-time emotion recognition with 82.37% accuracy across individualized touch patterns. This neuromorphic tactile framework facilitates the closed-loop human-AI emotional interaction, advancing toward humanoid robots capable of natural affective communication.

</details>
<br>

**关键词**: biomimetic hairy interface, affective touch sensing, emotion recognition, neuromorphic tactile framework, hybrid neural network, human-AI emotional interaction, tactile emotion perception

---

### 20. ❌ Bst2-targeted senotherapy restores visual function by eliminating senescent retinal cells

**作者**: Jun Yong Oh, Jae-Byoung Chae, Hyo Kyung Lee, Chul-Woo Park, Minseo Bae, Gyuri Kim, Yujeong Oh, Gyeongseok Yang, Sangpil Kim, Hae Won Ok, Dohyun Kim, Chaekyu Kim, S. W. Ricky Lee, Jiwon Jang, Hyewon Chung, Jeha Ryu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70797-2](https://doi.org/10.1038/s41467-026-70797-2)

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

**评分理由**: 论文研究的是视网膜衰老细胞的靶向清除疗法，涉及细胞衰老标记物发现、纳米药物递送平台开发和动物模型验证。所有评分关键词均聚焦于医学影像分析、AI诊断、手术规划等方向，而本文完全不涉及医学影像处理、深度学习模型、AI诊断系统、手术规划或多模态影像融合。论文属于分子生物学、纳米医学和眼科治疗领域，与给定的医学影像AI关键词无直接关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    In vivo administration of ABT-263-loaded B-Z-PON in aged and senescence-induced retinal degeneration models resulted in the selective ablation of senescent cells, restoration of RPE function, and improved visual outcomes, establishing a versatile platform for targeted senotherapy.

!!! tip deepseek-chat TL;DR

    该研究发现Bst2是衰老视网膜色素上皮细胞的膜标记物，并开发了靶向Bst2的纳米药物递送平台，在动物模型中成功清除衰老细胞并恢复视觉功能。

<details open>
<summary>摘要翻译</summary>

> 衰老细胞在包括视网膜在内的多种组织中参与退行性过程。在视网膜色素上皮（RPE）中，衰老细胞的积累与视网膜老化及疾病进展密切相关。清除衰老的RPE细胞已显示出治疗潜力，但传统的衰老细胞清除药物通常缺乏特异性，难以避免损伤非衰老细胞，从而引发安全性担忧。为克服这一局限，我们对自然衰老和化学诱导衰老条件下的雄性小鼠来源RPE细胞进行了整合转录组分析。这些分析发现Bst2作为一种膜定位标记物，在衰老RPE细胞中选择性上调表达，而在年轻对照组中表达极低。基于这一发现，我们开发了一种模块化、抗体可插拔的药物递送平台——B-Z-PON。该平台由介孔二氧化硅纳米颗粒构成，其表面功能化修饰了重组Fc结合结构域，并与抗Bst2抗体偶联。这种纳米载体能选择性聚集于表达Bst2的衰老RPE细胞，实现靶向药物递送并保护健康视网膜细胞。在衰老及衰老诱导的视网膜变性模型中，负载ABT-263的B-Z-PON进行体内给药后，可选择性清除衰老细胞、恢复RPE功能并改善视觉功能。本研究将衰老特异性标记物的发现与精准纳米医学相结合，构建了一个用于靶向衰老治疗的多功能平台。这些发现为年龄相关性黄斑变性等视网膜老化疾病提供了具有前景的治疗策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Senescent cells contribute to degenerative processes in multiple tissues, including the retina. In the retinal pigment epithelium (RPE), their accumulation is closely associated with retinal aging and disease progression. Eliminating senescent RPE cells has shown therapeutic potential, but conventional senolytics often lack the specificity required to spare non-senescent cells, raising safety concerns. To overcome this, we performed integrated transcriptomic analyses of male mouse-derived RPE cells under natural aging and chemically induced senescence conditions. These analyses identified Bst2 as a membrane-localized marker selectively upregulated in senescent RPE cells, with minimal expression in young controls. Based on this discovery, we developed a modular, antibody-pluggable drug delivery platform-B-Z-PON-comprising mesoporous silica nanoparticles functionalized with a recombinant Fc-binding domain and conjugated with anti-Bst2 antibodies. This nanocarrier selectively accumulates in Bst2-expressing senescent RPE cells, enabling targeted drug delivery and sparing healthy retinal cells. In vivo administration of ABT-263-loaded B-Z-PON in aged and senescence-induced retinal degeneration models resulted in the selective ablation of senescent cells, restoration of RPE function, and improved visual outcomes. Together, our study integrates senescence-specific marker discovery with precision nanomedicine, establishing a versatile platform for targeted senotherapy. These findings offer a promising therapeutic approach for retinal aging disorders, such as age-related macular degeneration.

</details>
<br>

**关键词**: senescent cells, retinal pigment epithelium, Bst2 marker, nanomedicine, targeted drug delivery, age-related macular degeneration, visual function restoration

---

### 21. ❌ Publisher Correction: Targeting of NAT10 enhances healthspan in a mouse model of human accelerated aging syndrome

**作者**: Gabriel Balmus, Delphine Larrieu, Ana C. Barros, Casey Collins, Monica Abrudan, Mukerrem Demir, Nicola J. Geisler, Christopher J. Lelliott, Jacqueline K. White, Natasha A. Karp, James B. Atkinson, Andrea Kirton, Matt Jacobsen, Dean Clift, Raphael Rodriguez, Sanger Mouse Genetics Project, Carl Shannon, Mark Sanderson, Amy Gates, Joshua Dench
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-69133-5](https://doi.org/10.1038/s41467-026-69133-5)

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

**评分理由**: 论文研究的是衰老生物学和基因靶向治疗，涉及NAT10酶抑制、小鼠模型、健康寿命延长等，完全不涉及医学影像分析、深度学习、AI诊断、手术规划、多模态影像或基础模型等关键词。所有关键词与论文内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过靶向抑制NAT10酶，在人类加速衰老综合征小鼠模型中成功延长了健康寿命。

**关键词**: NAT10, healthspan, mouse model, human accelerated aging syndrome, targeting, aging, gene therapy, premature aging

---

### 22. ❌ The hidden role of rhizospheric viruses in promoting nitrogen fixation in soils

**作者**: Dan Zhu, Wen Zhang, José Luís Balcázar, D. F. Wang, Mingming Sun, Feng Hu, J. J. Peñuelas, Yan Zhu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70744-1](https://doi.org/10.1038/s41467-026-70744-1)

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

**评分理由**: 论文研究的是土壤微生物学领域，具体探讨根际病毒在促进细菌固氮中的作用，涉及基因检测、稳定同位素示踪和病毒移植实验。所有评分关键词均属于医学影像分析和人工智能临床决策支持领域，与论文的土壤微生物、氮循环、病毒基因转移等主题完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The global distribution of nitrogen-fixing genes is revealed, with widespread detection of nifA, nifL, nifU, and nifH in both bacteria and viruses, and nifU as a viral auxiliary metabolic gene (AMG) is identified.

!!! tip deepseek-chat TL;DR

    该研究发现根际病毒通过携带固氮基因（如nifU）并水平转移给细菌，显著增强了土壤中的固氮酶活性，揭示了病毒在促进土壤氮循环中的先前未知作用。

<details open>
<summary>摘要翻译</summary>

> 生物固氮是陆地氮循环的基石，传统上归因于细菌固氮酶的活性。然而，根际病毒在其中的潜在贡献在很大程度上仍未得到探索。本文揭示了固氮基因的全球分布，在细菌和病毒中均广泛检测到nifA、nifL、nifU和nifH基因，并鉴定出nifU为一种病毒辅助代谢基因。对种植豇豆的根际土壤和本体土壤中病毒群落的分析表明，病毒nifU在根际土壤中的表达显著上调。通过<sup>15</sup>N₂稳定同位素示踪和病毒移植实验，我们证明病毒编码的固氮辅助代谢基因（水平转移自嗜热固氮螺菌等细菌，同源性达70-99%）将固氮酶活性从1.79提升至3.14 nmol C<sub>2</sub>H<sub>4</sub> g<sup>-1</sup>干土 h<sup>-1</sup>。这种增强伴随着细菌群落组成的变化，固氮属固氮菌的相对丰度达到90.8%。这些结果揭示了根际病毒在促进细菌固氮方面一个先前隐藏的作用，表明病毒介导的基因转移或可用于增强土壤氮循环，并为可持续土壤管理策略提供参考。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Biological nitrogen fixation is a cornerstone of terrestrial nitrogen cycling, traditionally attributed to bacterial nitrogenase activity. However, the potential contribution of rhizospheric viruses remains largely unexplored. Here, we reveal the global distribution of nitrogen-fixing genes, with widespread detection of nifA, nifL, nifU, and nifH in both bacteria and viruses, and identify nifU as a viral auxiliary metabolic gene (AMG). Analysis of viral communities in rhizosphere and bulk soils cultivated with cowpea showed that viral nifU expression was significantly upregulated in rhizosphere soils. Using <sup>15</sup>N₂ stable-isotope tracing and virus transplantation experiments, we demonstrate that virus-encoded nitrogen-fixing AMGs, horizontally transferred from bacteria such as Azospirillum thermophilum (70-99% homology), increased nitrogenase activity from 1.79 to 3.14 nmol C<sub>2</sub>H<sub>4</sub> g<sup>-1</sup> dry soil h<sup>-1</sup>. This enhancement was accompanied by shifts in bacterial community composition, with the relative abundance of the nitrogen-fixing genus Azotobacter reaching 90.8%. These results uncover a previously hidden role of rhizospheric viruses in promoting bacterial nitrogen fixation, suggesting that viral-mediated gene transfer could be leveraged to enhance nitrogen cycling in soils and inform sustainable soil management strategies.

</details>
<br>

**关键词**: rhizospheric viruses, nitrogen fixation, viral auxiliary metabolic genes, nifU, stable-isotope tracing, virus transplantation, Azotobacter, soil nitrogen cycling

---

### 23. ❌ Fast-swimming biohybrid OstraBot with self-trained high-strength muscles

**作者**: Pengyu Chen, Xuchen Wang, Jinrun Zhou, Yu Jun Tan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70259-9](https://doi.org/10.1038/s41467-026-70259-9)

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

**评分理由**: 论文研究的是生物混合机器人（biohybrid robot）领域，具体涉及骨骼肌组织工程、肌肉驱动器开发、机器人设计和游泳性能优化。所有评分关键词均属于医学影像分析和人工智能临床决策支持领域，而论文完全不涉及医学影像、疾病诊断、预后预测、手术规划或多模态医学数据。论文使用生理学模型指导机器人设计，但这不是医学影像或临床AI应用。因此，所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A fully autonomous self-training platform that strengthens skeletal muscle tissues by harnessing their robust spontaneous contractions and quantitatively guiding the robotic design for high-performance biohybrid robots is presented.

!!! tip deepseek-chat TL;DR

    该论文解决了生物混合机器人中肌肉力生成不足的问题，通过自主训练平台开发出高强度的骨骼肌驱动器，并基于生理学模型优化设计，实现了高性能的肌肉驱动游泳机器人OstraBot。

<details open>
<summary>摘要翻译</summary>

> 肌肉力量生成受限仍是开发更强、更快、更高效生物混合机器人的主要瓶颈。本文提出了一种完全自主的自训练平台，通过利用骨骼肌组织强大的自发收缩来强化其功能。该方法制备的肌肉驱动器最大力量达到7.05 mN，应力达8.51 mN/mm<sup>2</sup>，这是目前报道的C2C12来源肌肉驱动器的最高性能。为展示其能力，我们开发了一款双尾肌肉驱动鲀形游泳机器人OstraBot，并采用基于生理学的肌肉收缩模型指导其设计。通过模型分析确定了能最大化肌肉能量输出的刚度-频率组合，使机器人最高游速达到467毫米/分钟（15.6倍体长/分钟），显著优于既往报道的骨骼肌驱动生物混合机器人。该机器人通过声触发拍击控制展现出强大的推力生成能力和精确的启停可控性。本研究建立了一个多功能平台，可用于生产高强度骨骼肌驱动器，并为高性能生物混合机器人的设计提供定量化指导。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Limited muscle force generation remains a major bottleneck in developing stronger, faster, and more efficient biohybrid robots. We present a fully autonomous self-training platform that strengthens skeletal muscle tissues by harnessing their robust spontaneous contractions. This approach produced muscle actuators with a maximum force of 7.05 mN and a stress of 8.51 mN/mm<sup>2</sup>, the highest reported for C2C12-derived muscle actuators. To demonstrate their capabilities, we developed a twin-tail muscle-powered ostraciiform swimming robot, OstraBot, and guided its design using a physiology-based muscle contraction model. Model-informed analysis identified stiffness-frequency combinations that maximized muscle energy output, enabling a top speed of 467 mm/min (15.6 body lengths/min), significantly outperforming previously reported skeletal muscle-powered biohybrid robots. The robot demonstrated strong thrust generation and precise on-off controllability through sound-triggered clapping control. This work establishes a versatile platform for producing high-strength skeletal muscle actuators and quantitatively guiding the robotic design for high-performance biohybrid robots.

</details>
<br>

**关键词**: biohybrid robot, skeletal muscle actuators, self-training platform, muscle contraction model, ostraciiform swimming, high-strength muscles, robotic design optimization

---

### 24. ❌ Decomposition of cross-country socioeconomic inequality in mortality by 288 causes of death and 84 risk factors from 1990 to 2021

**作者**: Dong Peng, Rongbin Xu, Simon Hales, Lidia Morawska, Gongbo Chen, Zhengyu Yang, Yiwen Zhang, Michael J. Abramson, Shanshan Li, Yu Guo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70877-3](https://doi.org/10.1038/s41467-026-70877-3)

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

**评分理由**: 论文研究全球跨国家社会经济不平等对死亡率的影响，分析288种死因和84种风险因素的贡献，使用全球疾病负担研究数据。研究内容属于流行病学、公共卫生和全球健康领域，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或基础模型等主题。所有关键词与论文内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究量化了1990年至2021年间288种死因和84种风险因素对全球跨国家社会经济不平等导致的死亡率差异的贡献，发现传染性疾病贡献下降而非传染性疾病贡献上升，为政策制定者提供了促进全球健康公平的数据。

<details open>
<summary>摘要翻译</summary>

> 全球范围内全因年龄标准化死亡率（SIAM）的社会经济不平等现象已持续数十年，但其主要成因和风险因素尚不明确。本研究利用《2021年全球疾病负担研究》（GBD 2021）数据，量化评估了288种死因和84种风险因素对SIAM的贡献。1990年至2021年间，传染性、孕产、新生儿及营养性疾病对SIAM的贡献率从81.2%下降至56.6%，而非传染性疾病的贡献率从13.2%上升至27.8%。2021年导致SIAM的前五位死因分别为：新冠肺炎（COVID-19）（17.9%）、卒中（9.4%）、结核病（7.3%）、下呼吸道感染（7.0%）和腹泻性疾病（5.5%）。2021年影响SIAM的前五位风险因素为：固体燃料造成的室内空气污染（17.2%）、收缩压升高（9.9%）、不安全性行为（4.6%）、高空腹血糖（4.4%）和不安全饮用水源（4.2%）。总体而言，本研究通过揭示导致跨国死亡率差异的关键死因和风险因素，为政策制定者推动全球健康公平提供了数据依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Global cross-country socioeconomic inequalities in all-cause age-standardized mortality (SIAM) have persisted over decades, but major contributing causes and risk factors remain unclear. Here, we quantified contributions of 288 causes and 84 risk factors to SIAM using the Global Burden of Disease Study 2021 (GBD 2021). From 1990 to 2021, communicable, maternal, neonatal, and nutritional diseases' contribution fell from 81.2% to 56.6%, while non-communicable diseases' contribution from 13.2% to 27.8%. The top five causes of death contributing to SIAM in 2021 were COVID-19 (17.9%), stroke (9.4%), tuberculosis (7.3%), lower respiratory infections (7.0%), and diarrheal diseases (5.5%). The top five risk factors contributing to SIAM in 2021 were household air pollution from solid fuels (17.2%), high systolic blood pressure (9.9%), unsafe sex (4.6%), high fasting plasma glucose (4.4%), and unsafe water sources (4.2%). Overall, this study provides policymakers with data to promote global health equity by targeting key causes and risk factors contributing to cross-country mortality inequality.

</details>
<br>

**关键词**: socioeconomic inequality, mortality, causes of death, risk factors, Global Burden of Disease, health equity, cross-country analysis, public health

---

### 25. ❌ Decoupling electronic and geometric effects in Pd catalysts via thermal surface reconstruction for selective hydrogenation

**作者**: Minghang Li, Zhuowei Fu, Qian Luo, Bin Lü, Liwei Zhang, Shipan Liang, Ting Liu, Yong Wang, Shanjun Mao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70568-z](https://doi.org/10.1038/s41467-026-70568-z)

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

**评分理由**: 论文研究的是异相催化中钯催化剂的表面重构对选择性加氢的影响，属于材料科学和化学工程领域。所有评分关键词均涉及医学影像分析、人工智能医疗应用等医学领域，与论文的化学催化研究内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过热诱导表面重构策略解耦钯催化剂的电子和几何效应，揭示了在炔烃半加氢反应中几何结构决定反应速率，而选择性调控则分为电子效应主导和几何效应主导两个不同区域。

<details open>
<summary>摘要翻译</summary>

> 在多相催化中，电子效应与几何效应的长期纠缠使其各自作用的精确归因难以明晰。通过采用热诱导表面重构策略逐步增强金属-载体相互作用，我们实现了对钯（Pd）电子结构和几何结构的连续调控。以炔烃半加氢这一典型结构敏感探针反应为例，我们发现：尽管在Pd重构过程中电子结构与几何结构呈线性耦合，但转化频率仅与几何描述符W（量化Pd颗粒扁平化程度）呈标度关系；而选择性调控则分化为两种截然不同的机制：在临界W值以下，缺电子Pd位点抵消了几何约束，形成对结构不敏感的选择性平台；超过该阈值后，富电子表面则建立起明确的几何控制主导机制。此外，表面重构显著压缩了Pd位点发生过度加氢副反应的电子-几何空间。这些发现为氢化反应中金属催化剂的调控提供了设计蓝图，并为量化其他结构敏感反应中的电子-几何相互作用开辟了新路径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The entangled electronic and geometric effects in heterogeneous catalysis have long obscured precise attribution of their individual roles. By employing a thermal-induced surface reconstruction strategy to progressively enhance metal-support interactions, we achieve continuous tuning of Pd's electronic and geometric structures. Using alkyne semi-hydrogenation as a prototypical structure-sensitive probe reaction, we demonstrate that despite the linear coupling of electronic and geometric structures during Pd reconstruction, the turnover frequency scales solely with the geometric descriptor W (quantifying Pd particle flattening), while selectivity regulation bifurcates into two distinct regimes: Below a critical W, electron-deficient Pd sites offset geometric constraints, yielding a non-structure-sensitive selectivity plateau; whereas above this threshold, electron-rich surfaces establish unequivocal geometric control. Moreover, surface reconstruction drastically shrinks the electronic-geometric space of Pd sites for over-hydrogenation side reaction. These insights provide a blueprint for metal catalysts regulation in hydrogenation and may open avenues for quantifying electronic-geometric interplay in other structure-sensitive reactions.

</details>
<br>

**关键词**: heterogeneous catalysis, surface reconstruction, Pd catalysts, selective hydrogenation, electronic-geometric effects, alkyne semi-hydrogenation, metal-support interactions, structure-sensitive reactions

---

### 26. ❌ Predator-mediated local convergence fosters global microbial community divergence

**作者**: Rasit Asiloglu, Hayato Kuno, Mayu Fujino, Seda Özer Bodur, Murat Aycan, Hideo Ishizuka, Shiori Kazama, Shinya Iwasaki, Jun Murase, Naoki Harada, Miwa Arai, Kenta Ikazaki
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70605-x](https://doi.org/10.1038/s41467-026-70605-x)

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

**评分理由**: 论文研究微生物群落组装机制，聚焦于捕食性原生生物对细菌群落的影响，属于微生物生态学、土壤生物学和生物地理学领域。所有评分关键词均涉及医学影像分析、人工智能诊断、手术规划等临床医学技术，与论文的微生物生态研究主题完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is found that predator identity and prey susceptibility jointly determine convergence outcomes, establishing bacterivorous protists as key, context-dependent agents of biogeography and suggesting new opportunities for microbiome engineering, where targeted use of protists may steer microbial communities toward functional configurations that enhance soil health and ecosystem resilience.

!!! tip deepseek-chat TL;DR

    该研究揭示了捕食性原生生物通过抑制优势细菌类群促进局部微生物群落趋同，同时通过物种特异性捕食效应导致全球尺度上的群落分化，为微生物组工程提供了新思路。

<details open>
<summary>摘要翻译</summary>

> 理解微生物群落如何组装是预测生态系统功能的核心。尽管捕食者通过捕食强烈影响细菌群落，但微生物捕食者在调节全球微生物趋异与趋同模式中的作用在很大程度上仍被忽视。本研究整合了全球尺度的扩增子测序数据、受控野外实验以及自然与合成群落的重建，以探究捕食者介导的群落组装机制。我们发现，食细菌原生生物对微生物群落产生双重且尺度依赖的效应：通过抑制优势细菌类群促进局部趋同，同时通过物种特异性捕食效应引发全球尺度趋异。研究表明，捕食者身份与猎物易感性共同决定趋同结果。由捕食抗性类群主导的群落在捕食压力下表现出较低的趋同性，揭示了一种可预测的基于性状的过滤机制。这项工作确立了食细菌原生生物作为关键且情境依赖的生物地理驱动因子，并为微生物组工程提供了新思路——定向利用原生生物可能引导微生物群落形成增强土壤健康与生态系统恢复力的功能构型。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Understanding how microbial communities assemble is central to predicting ecosystem function. Although predators strongly influence bacterial communities through predation, the role of microbial predators in modulating global microbial divergence and convergence patterns remains largely neglected. Here, we integrated global-scale amplicon sequencing data, controlled field experiments, and reconstructions of natural and synthetic communities to examine predator-mediated community assembly mechanisms. We show that bacterivorous protists exert dual, scale-dependent effects on microbial communities: promoting local convergence by suppressing dominant bacterial taxa, while generating global divergence through species-specific predation effects. We find that predator identity and prey susceptibility jointly determine convergence outcomes. Communities dominated by predator-resistant taxa exhibit reduced convergence under predation pressure, revealing a predictable trait-based filtering mechanism. This work establishes bacterivorous protists as key, context-dependent agents of biogeography and suggests new opportunities for microbiome engineering, where targeted use of protists may steer microbial communities toward functional configurations that enhance soil health and ecosystem resilience.

</details>
<br>

**关键词**: microbial community assembly, bacterivorous protists, predator-mediated convergence, global microbial divergence, trait-based filtering, microbiome engineering, soil health, ecosystem resilience

---

### 27. ❌ Rapid dynamics of dorsal raphe serotonin neurons regulate the strength of visual attention

**作者**: Jonas Lehnert, Kuwook Cha, Julia Forestell, Kerry Yang, Xinyue Ma, Sinan Shariff, Jonathan P. Britt, Anmar Khadra, Erik P. Cook, Arjun Krishnaswamy
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70658-y](https://doi.org/10.1038/s41467-026-70658-y)

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

**评分理由**: 论文研究的是神经科学领域，具体关注小鼠视觉注意力调节的神经机制，涉及中缝背核（DR）血清素神经元快速动力学、光遗传学操作和计算建模。所有评分关键词均属于医学影像分析和人工智能临床决策支持领域，而该论文完全不涉及医学影像、图像处理、深度学习、疾病诊断、预后预测、手术规划或多模态医学数据。论文内容与评分关键词的研究领域完全不同，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is reported that rapid dynamics in both dorsal raphe (DR) activity and cortical serotonin (5HT) release selectively regulate attentional strength and defines rapid DR-5HT neuromodulation as a new regulator of attentional strength.

!!! tip deepseek-chat TL;DR

    该研究发现中缝背核血清素神经元的快速动力学通过控制皮层抑制和除法归一化来独立调节视觉注意力的强度，而不影响注意力的焦点。

<details open>
<summary>摘要翻译</summary>

> 每时每刻，一束注意的“聚光灯”都在我们的视野中游走，以增强对显著刺激的检测。尽管近期研究揭示了大脑如何选择显著相关刺激（注意焦点），但大脑是否具备机制来调节注意力以适应不断变化的目标显著性或内部需求（注意强度），目前尚不清楚。本研究通过在小鼠执行线索检测任务时进行光学记录与扰动，发现中缝背核（DR）活动与皮层血清素（5HT）释放的快速动态变化，能够选择性地调控注意强度。与这些快速的DR-5HT动态变化相反，我们发现先前报道的与奖赏相关的、较慢的动态变化均与注意力无关。短暂的光遗传学DR-5HT抑制提高了注意强度与任务表现，而光遗传学兴奋则降低了注意强度与表现。一个计算模型表明，DR-5HT对注意力的反向效应源于其对皮层抑制和除法归一化的控制。总之，我们的研究结果表明，大脑能够独立控制注意强度与注意焦点，并将快速的DR-5HT神经调制定义为注意强度的一种新型调节器。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Every moment, a spotlight of attention roams our visual field to enhance detection of salient stimuli. While recent work suggests how the brain selects salient relevant stimuli (attentional focus), it is unknown if there are mechanisms that modulate attention to suit fluctuating target salience or internal needs (attentional strength). Here, using optical recordings and perturbations in mice performing a cued detection task, we report that rapid dynamics in both dorsal raphe (DR) activity and cortical serotonin (5HT) release selectively regulate attentional strength. In contrast to these rapid DR-5HT dynamics, we found previously reported reward-associated and slower dynamics were both unrelated to attention. Brief optogenetic DR-5HT suppression increased attentional strength and performance, whereas optogenetic excitation reduced attentional strength and performance. A computational model suggests DR-5HT's inverse effects on attention arise from control of cortical suppression and divisive normalization. Collectively, our results demonstrate that the brain independently controls attentional strength and focus and defines rapid DR-5HT neuromodulation as a new regulator of attentional strength.

</details>
<br>

**关键词**: dorsal raphe, serotonin, visual attention, attentional strength, optogenetic, cortical suppression, computational model, neuromodulation

---

### 28. ❌ Large-scale multi-omics profiling reveals environmental and evolutionary drivers of fungal phylogeographic and metabolic diversity

**作者**: Huali Xie, Jie Hu, Xinyu Zhao, Jianwei Chen, Xiaofeng Yue, Changhao Zhou, Jorge C. Navarro-Muñoz, Jing Jiang, Xiaoqian Tang, Fang Zhao, E. Anne Hatmaker, Antonis Rokas, Amelia E. Barber, Milton T. Drott, Nancy P. Keller, Qi Zhang, Justin J. J. van der Hooft, Marnix H. Medema, P. Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70721-8](https://doi.org/10.1038/s41467-026-70721-8)

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

**评分理由**: 论文研究真菌（Aspergillus flavus）的群体遗传学、代谢组学和基因组学，探讨环境与进化如何驱动真菌代谢多样性和地理分布。所有评分关键词均涉及医学影像分析、AI辅助诊断、手术规划等临床决策支持技术，而论文完全不涉及医学影像、深度学习、AI诊断、手术或任何医学影像模态。论文属于微生物学、进化生物学和代谢组学领域，与医学影像AI无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The results reveal how environmental shifts drive the fungal metabolic evolution, and provide insights for predicting the risk of harmful fungal outbreaks and for biogeographically-informed, precise control measures.

!!! tip deepseek-chat TL;DR

    该研究通过多组学分析揭示了环境变化如何驱动真菌（黄曲霉）的代谢进化和地理分布模式，为预测有害真菌爆发风险提供了见解。

<details open>
<summary>摘要翻译</summary>

> 化学创新是真菌适应不断变化的生态环境的关键。然而，真菌代谢分化的环境与进化驱动因素仍不明确。本研究通过系统发育和生物地理学分析，展示了来自四大洲的1052株黄曲霉（Aspergillus flavus）菌株的系统地理多样性，其中包括544株来自中国的新测序菌株。通过群体代谢组学分析，这些菌株表现出不同程度的群体特异性真菌毒素生产能力。我们通过比较群体基因组学分析，鉴定出一个来自中国的产毒亚群。泛代谢组分析揭示了与特定生态位密切相关的强烈系统地理代谢模式。低产毒素分支拥有独特的未表征生物合成基因簇，并转而产生不同的特化代谢产物。这种差异仅能部分由生物合成途径基因的变异解释，而调控和初级代谢的变化似乎是驱动不同真菌群体间特化代谢谱分化的主要因素，这得到了泛基因组分析、代谢物-全基因组关联研究、基因型-环境关联研究、泛转录组分析和基因敲除实验的证实。总之，我们的结果揭示了环境变化如何驱动真菌代谢进化，并为预测有害真菌爆发的风险以及实施基于生物地理信息的精准防控措施提供了见解。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Chemical innovation is essential for fungi to adapt to ever-changing ecological environments. However, the environmental and evolutionary drivers of fungal metabolic differentiation remain ambiguous. Here, we show the phylogeographic diversity of 1052 Aspergillus flavus strains across four continents, as conducted through phylogenetic and biogeographical analysis, including 544 newly sequenced strains from China. These strains exhibit varying levels of population-specific mycotoxin production, as determined by population metabolomics analysis. We report a toxigenic subpopulation from China, identified through comparative population genomics analysis. Pan-metabolome analysis reveals strong phylogeographic metabolic patterns associated with specific ecological niches. Low-mycotoxin production clades harbor distinct uncharacterized biosynthetic gene clusters and produce different specialized metabolites instead. This discrepancy is only partially explained by variation in biosynthetic pathway genes, and changes in regulation and primary metabolism appear to mainly drive differentiation of specialized metabolite profiles across fungal populations, as indicated by pangenome profiling, metabolites-genome-wide association study, genotype-environment association study, pan-transcriptome analysis, and gene knockout experiments. Altogether, our results reveal how environmental shifts drive the fungal metabolic evolution, and provide insights for predicting the risk of harmful fungal outbreaks and for biogeographically-informed, precise control measures.

</details>
<br>

**关键词**: fungal phylogeography, metabolic diversity, multi-omics profiling, Aspergillus flavus, mycotoxin production, population genomics, environmental drivers, evolutionary drivers

---

### 29. ❌ Celcomen: spatial causal disentanglement for single-cell and tissue perturbation modeling

**作者**: Stathis Megas, Daniel Chen, Krzysztof Polański, Hesam Asadollahzadeh, Moshe Eliasof, Carola-Bibiane Schönlieb, S. Teichmann
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-69856-5](https://doi.org/10.1038/s41467-026-69856-5)

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

**评分理由**: 论文研究的是空间转录组学数据的因果解缠和扰动建模，使用生成图神经网络分析单细胞和组织的基因调控程序。所有评分关键词均聚焦于医学影像分析（CT、MRI、超声等）、基于影像的疾病诊断、预后预测、手术规划等临床决策支持领域。论文内容涉及生物信息学、计算生物学和单细胞组学，与医学影像分析无直接关联，因此所有关键词相关度均为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Celcomen leverages a mathematical causality framework to disentangle intra- and inter-cellular gene regulation programs in spatial transcriptomics data through a generative graph neural network and provides the means to model disease- and therapy-induced changes allowing for new insights into single-cell spatially resolved tissue responses.

!!! tip deepseek-chat TL;DR

    该论文提出了Celcomen方法，利用因果框架和图神经网络解缠空间转录组学数据中的基因调控程序，以生成扰动后的反事实空间转录组数据，并在人类胶质母细胞瘤等样本中验证了其预测能力。

<details open>
<summary>摘要翻译</summary>

> Celcomen利用数学因果框架，通过生成式图神经网络解析空间转录组数据中的细胞内与细胞间基因调控程序。这是构建虚拟组织扰动模型的第一步，能够生成扰动后的反事实空间转录组数据，从而为研究者提供实验难以获取的样本。我们通过模拟数据及在临床相关的人类胶质母细胞瘤、人类胎儿脾脏和小鼠肺癌样本中，验证了其调控程序的解耦能力、因果结构的可识别性以及反事实预测性能。Celcomen为模拟疾病与治疗诱导的组织变化提供了方法，为单细胞空间分辨率下的组织反应研究开辟了新视角。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Celcomen leverages a mathematical causality framework to disentangle intra- and inter-cellular gene regulation programs in spatial transcriptomics data through a generative graph neural network. It is a first step towards perturbation models of Virtual Tissues and can generate post-perturbation counterfactual spatial transcriptomics, thereby offering access to experimentally inaccessible samples. We validated its disentanglement, identifiability of causal structure, and counterfactual prediction capabilities through simulations and in clinically relevant human glioblastoma, human fetal spleen, and mouse lung cancer samples. Celcomen provides the means to model disease- and therapy-induced changes allowing for new insights into single-cell spatially resolved tissue responses.

</details>
<br>

**关键词**: spatial transcriptomics, causal disentanglement, generative graph neural network, perturbation modeling, counterfactual prediction, single-cell analysis, tissue response modeling, gene regulation

---

### 30. ❌ Intellectual disability-causing mutations in KIF11 impair microtubule dynamics and dendritic arborization

**作者**: Jenna L. Wingfield, Lukas Niese, Yosef Avchalumov, X. Liu, Rahul Grover, Yoshihisa Nakahata, Bindu Raveendra, Adrián González-Santiago, Jackson P. Carter, Ryohei Yasuda, Jason X-J Yuan, Stefan Diez, Sathyanarayanan V. Puthanveettil
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70522-z](https://doi.org/10.1038/s41467-026-70522-z)

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

**评分理由**: 论文研究KIF11基因突变对神经元微管动力学和树突分支的影响，属于分子神经生物学和细胞生物学领域。所有评分关键词均涉及医学影像分析、人工智能诊断、手术规划等临床决策支持技术，与论文的细胞机制研究完全无关。论文使用活细胞成像、生化分析等实验方法，未涉及任何医学影像处理、深度学习或AI模型。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is found that KIF11 depletion in postmitotic neurons increases minus-end-out MT dynamics in both axons and dendrites, providing essential insights into the molecular mechanisms driving MCLID.

!!! tip deepseek-chat TL;DR

    该研究揭示了KIF11基因突变通过破坏微管动力学和交叉连接，导致树突分支减少和突触功能受损，阐明了智力障碍疾病MCLID的分子机制。

<details open>
<summary>摘要翻译</summary>

> 伴有或不伴有脉络膜视网膜病变、淋巴水肿或智力障碍的小头畸形（MCLID）是一种由有丝分裂驱动蛋白KIF11突变引起的罕见疾病。然而，KIF11的具体神经元功能、其调控微管（MT）的机制以及MCLID突变对KIF11功能的影响仍未得到充分研究。本研究通过活细胞成像发现，在有丝分裂后神经元中敲低KIF11会增加轴突和树突中负极朝外微管的动态性。引入与MCLID相关的KIF11突变体KIF11<sup>Y82F</sup>和KIF11<sup>ΔCterm</sup>，会显著降低微管动态性、损害树突分支化并减少微型兴奋性突触后电流（mEPSC）频率。生化分析表明，KIF11<sup>ΔCterm</sup>突变体破坏了四聚体形成和微管交联能力，而KIF11<sup>Y82F</sup>突变体则降低了微管滑动速度和ATP亲和力。利用光控KIF11进行时间特异性抑制，可增加微管动态性和树突生长。综上所述，这些数据揭示KIF11是成熟神经元中微管动态性的调控器和树突分支化的调节因子，为理解驱动MCLID的分子机制提供了重要见解。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Microcephaly with or without chorioretinopathy, lymphedema, or intellectual disabilities (MCLID) is a rare disease caused by mutations in the mitotic motor KIF11. However, the specific neuronal functions of KIF11, its mechanisms of microtubule (MT) regulation, and the impact of MCLID mutations on KIF11 function remain underexplored. Here, using live-imaging, we find that KIF11 depletion in postmitotic neurons increases minus-end-out MT dynamics in both axons and dendrites. Introducing MCLID-associated KIF11 mutations, KIF11<sup>Y82F</sup> and KIF11<sup>ΔCterm</sup>, significantly reduces MT dynamics, impairs dendritic arborization, and decreases mEPSC frequency. Biochemical analyses reveal that the KIF11<sup>ΔCterm</sup> mutant disrupts tetramer formation and MT crosslinking, while the KIF11<sup>Y82F</sup> mutant reduces MT sliding velocity and ATP affinity. Temporal inhibition of KIF11 using a photo-controllable KIF11 increases MT dynamics and dendritic growth. Together, these data reveal that KIF11 is a MT dynamics rheostat and regulator of dendritic arborization in mature neurons, providing essential insights into the molecular mechanisms driving MCLID.

</details>
<br>

**关键词**: KIF11, microtubule dynamics, dendritic arborization, intellectual disability, MCLID, neuronal function, live-imaging, mutations

---

### 31. ❌ Enhancing the performance of Magnets photosensors

**作者**: Armin Baumschlager, Yanik Weber, David Cánovas, Sara Dionisi, Mustafa Khammash
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70695-7](https://doi.org/10.1038/s41467-026-70695-7)

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

**评分理由**: 论文研究的是光遗传学中的光敏蛋白工程（Magnets photosensors），通过随机诱变和高通量筛选优化光敏系统的光敏感性和激活特性，应用于细菌中的光遗传调控。所有评分关键词均涉及医学影像分析、AI诊断、手术规划等临床医疗领域，而该论文属于基础生物工程和蛋白质工程领域，两者研究领域完全不同，没有任何相关性。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work presents a simple, yet powerful strategy based on random mutagenesis coupled to high-throughput screening that allowed altering the most fundamental properties of the widely used nMag/pMag photodimerization system: its light sensitivity and activation.

!!! tip deepseek-chat TL;DR

    该论文通过随机诱变和高通量筛选优化了Magnets光敏系统的光敏感性和激活特性，拓宽了其在光遗传调控策略中的应用范围。

<details open>
<summary>摘要翻译</summary>

> 源自天然的光敏蛋白结构域是光遗传学蛋白质工程的基础。通过定制其特性，可在基础研究和应用生物工程中充分发挥其光遗传调控潜力。本文提出一种基于随机诱变与高通量筛选相结合的简洁而高效的策略，成功改变了广泛使用的nMag/pMag光二聚化系统的核心特性：光敏感性与激活特性。我们通过流式细胞术在细菌体内对变异体进行表征，并利用荧光光谱法在整个生长曲线中监测其表现。研究发现，在亚饱和光强条件下，某些突变既能增强也能降低系统光敏感性，同时改善了光激活性能及暗/明态变化倍数。值得注意的是，光敏感性与激活水平可实现独立调控。此外，研究证明剂量响应曲线的形态可被精确调控，这显著拓展了Magnets光感受器在光遗传调控策略中的适用性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Photosensory protein domains, derived from nature, are foundational for optogenetic protein engineering. Tailoring their properties enables their full exploitation for optogenetic regulation in basic research and applied bioengineering applications. Here, we present a simple, yet powerful strategy based on random mutagenesis coupled to high-throughput screening that allowed altering the most fundamental properties of the widely used nMag/pMag photodimerization system: its light sensitivity and activation. Variants were characterized in vivo in bacteria by flow cytometry and during the entire growth curve by spectrofluorometry. We identify mutations that either increase or decrease the light sensitivity at sub-saturating light intensities, while also improving the light activation and dark-to-light fold change. Notably, light sensitivity and activation levels could be changed independently. In addition, we demonstrated that the shapes of the dose-response curves can be finely tuned. This broadens the applicability of the Magnets photosensors for optogenetic regulation strategies.

</details>
<br>

**关键词**: optogenetic protein engineering, photosensory protein domains, Magnets photosensors, random mutagenesis, high-throughput screening, light sensitivity, photodimerization system, optogenetic regulation

---

### 32. ❌ Tough asymmetric thermochromic ionogels via dynamic in situ phase separation for dual-modal smart optical switching

**作者**: Guoli Du, Jianing Li, Changxing Wang, Jianing Li, Yayun Ning, Yifan Yue, Yuechi Xie, Sen Yang, Xuegang Lu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70830-4](https://doi.org/10.1038/s41467-026-70830-4)

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

**评分理由**: 论文研究的是通过动态原位相分离制备坚韧不对称热致变色离子凝胶，用于智能光学开关（如智能冷却窗和动态投影显示）。其核心内容涉及材料科学、化学工程和光学工程，包括热致变色材料、离子凝胶、相分离、机械性能、光学性能等。所有给定的评分关键词均属于医学影像分析和人工智能在临床决策支持领域的范畴，而该论文完全不涉及医学影像、疾病诊断、手术规划或任何医疗应用，因此所有关键词的相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了热致变色材料在实现光学开关、机械鲁棒性和环境耐受性同时优化方面的挑战，通过动态原位相分离制备了坚韧不对称热致变色离子凝胶，实现了高透明度、超低温耐受性、优异韧性、可逆光学开关和自主粘附，并应用于智能冷却窗和动态投影显示。

<details open>
<summary>摘要翻译</summary>

> 尽管热致变色材料在智能光开关领域取得了显著进展，但如何同时实现光学切换性能、机械强度和环境耐受性的优化，仍是其实际应用面临的关键挑战。本文通过动态原位相分离技术制备了坚韧的非对称热致变色离子凝胶。该材料通过顺序自由基聚合法，将热响应光散射层（低临界溶解温度：28 °C 至 41 °C）与机械增强支撑层集成于一体。所得材料展现出高透明度（20 °C 时 >85%）、优异的低温耐受性（-70 °C 甚至 -196 °C 下保持透明）以及卓越的韧性（拉伸强度 >5 MPa，韧性 >17 MJ m<sup>-3</sup>）。得益于以疏水性离子液体作为溶剂，ATIs 无需封装即可实现可逆的光学切换（40 °C 时透光率 <10%），并具备自主粘附能力（在玻璃上的剥离强度 >400 N m<sup>-1</sup>）。应用于智能冷却窗户时，ATIs 可减少 56.8% 的太阳辐射，同时支持美学定制。结合间接/直接焦耳加热技术，ATIs 能够实现主动光学切换乃至动态投影显示，为全天候自适应光学系统提供了一个可扩展的平台。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Despite significant advances in thermochromic materials (TCMs) for smart optical switching, achieving simultaneous optimization of optical switching, mechanical robustness, and environmental tolerance remains a critical challenge for their real-world implementation. Herein, we present tough asymmetric thermochromic ionogels (ATIs) fabricated via dynamic in situ phase separation. The ATIs integrate a thermoresponsive light-scattering layer (LCST: 28 °C to 41 °C) and a mechanically reinforced supporting layer through sequential free-radical polymerization. The resulting material exhibits high transparency (>85% at 20 °C), ultralow-temperature resistance (transparent at -70 °C, even at -196 °C), and exceptional toughness (tensile strength >5 MPa, toughness >17 MJ m<sup>-3</sup>). Leveraging hydrophobic ionic liquid as solvent, the ATIs achieve reversible optical switching (transmittance <10% at 40 °C) without encapsulation, with autonomous adhesion (>400 N m<sup>-1</sup> peel strength on glass). Applied to smart cooling windows, ATIs reduce solar radiation by 56.8% while enabling aesthetic customization. Combined with indirect/direct Joule heating technology, ATIs enable active optical switching and even dynamic projection display, offering a scalable platform for all-weather adaptive optical systems.

</details>
<br>

**关键词**: thermochromic ionogels, dynamic in situ phase separation, smart optical switching, mechanical robustness, low-temperature resistance, reversible optical switching, smart cooling windows, dynamic projection display

---

### 33. ❌ NANP targeting radiosensitizes glioblastoma through TNFR1 sialylation-driven mesenchymal shift

**作者**: Yingwen Ding, Ze-Yan Zhang, Ravesanker Ezhilarasan, Aram S. Modrek, Melanie Graciani, Jerome Karp, Graysen McManus, Ananya Jambhale, Erik P. Sulman
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70853-x](https://doi.org/10.1038/s41467-026-70853-x)

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

**评分理由**: 论文研究的是胶质母细胞瘤（GBM）的放射治疗增敏机制，通过CRISPR筛选发现NANP酶通过调节TNFR1的唾液酸化影响NF-κB信号通路和间充质状态，从而影响放射敏感性。研究内容完全属于分子生物学、肿瘤学和放射治疗领域，使用的方法包括基因组学、细胞实验和动物模型。论文未涉及任何医学影像分析、深度学习、AI诊断、预后预测、手术规划或多模态影像等内容，与所有评分关键词均无关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    NANP is identified as a radiosensitizing target dependent on TNFR1 sialylation and mesenchymal shift, providing a basis for developing RT sensitizers for GBM.

!!! tip deepseek-chat TL;DR

    该研究通过CRISPR筛选发现NANP酶通过调节TNFR1唾液酸化影响胶质母细胞瘤的间充质状态和NF-κB信号通路，从而增强放射治疗敏感性，为开发GBM放射增敏剂提供了新靶点。

<details open>
<summary>摘要翻译</summary>

> 胶质母细胞瘤（GBM）患者因对初始电离放射治疗（RT）产生抵抗而导致生存率极低。克隆演化分析显示不存在主导性的RT抵抗克隆，这促使我们通过全基因组CRISPR筛选来识别放射增敏靶点。筛选结果凸显了DNA损伤反应基因的重要性，验证了我们方法的有效性。N-酰基神经氨酸-9-磷酸酶（NANP）作为唾液酸合成途径中的关键酶，在筛选中排名前列，且与患者预后相关。辐照后，NANP缺陷细胞表现出更严重的DNA损伤、G2/M期阻滞和细胞凋亡，并通过倾向于非同源末端连接而非同源重组的方式削弱了DNA修复能力。机制上，NANP通过调节肿瘤坏死因子受体1（TNFR1）的唾液酸化和内化，影响NF-κB信号传导和间充质状态，从而改变RT敏感性。颅内原位异种移植实验验证了NANP在体内的功能。本研究确认NANP是一个依赖于TNFR1唾液酸化及间充质转变的放射增敏靶点，为开发针对GBM的RT增敏剂提供了依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Glioblastoma (GBM) patients have dismal survival due to resistance to initial ionizing radiation therapy (RT). Clonal evolution analysis reveals no dominant RT-resistant clones, prompting a genome-wide CRISPR screen to identify radiosensitizing targets. The screening highlights DNA damage response genes, validating the effectiveness of our approach. N-acylneuraminate-9-phosphatase (NANP), a critical enzyme in the sialic acid synthetic pathway, is top-ranked in the screening and associated with patient outcomes. After radiation, NANP-deficient cells exhibit more DNA damage, G2/M arrest and apoptosis, and impaired DNA repair by favoring non-homologous end-joining over homologous recombination. Mechanistically, NANP influences NF-κB signaling and the mesenchymal state by modulating sialylation and internalization of tumor necrosis factor receptor 1 (TNFR1), thereby affecting RT sensitivity. Intracranial orthotopic xenograft experiments validate the function of NANP in vivo. Here, we identify NANP as a radiosensitizing target dependent on TNFR1 sialylation and mesenchymal shift, providing a basis for developing RT sensitizers for GBM.

</details>
<br>

**关键词**: glioblastoma, radiosensitization, NANP, TNFR1 sialylation, mesenchymal shift, CRISPR screen, DNA damage response, NF-κB signaling

---

### 34. ❌ Unlocking the reducing power of metal nitrides by mechanochemical hydrodefluorination of fluorinated compounds

**作者**: Jun-Shen Chen, Lifeng Guo, Haiyan Pan, Guan‐Wu Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-18
**DOI**: [10.1038/s41467-026-70813-5](https://doi.org/10.1038/s41467-026-70813-5)

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

**评分理由**: 论文研究的是化学领域的机械化学氢化脱氟反应，使用金属氮化物（特别是氮化镁）作为还原剂降解氟化化合物，包括聚四氟乙烯（特氟龙）。所有评分关键词均涉及医学影像分析、人工智能、疾病诊断、手术规划等医疗AI领域，与论文的化学合成和材料降解研究完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了碳-氟键活化难题，通过开发机械化学氢化脱氟策略，利用金属氮化物作为还原剂，成功从氟化化合物中回收有价值的碳氢化合物，并实现了持久性聚四氟乙烯（特氟龙）的降解。

<details open>
<summary>摘要翻译</summary>

> 碳-氟（C-F）键存在于芳香族C(sp<sup>2</sup>)-F与脂肪族C(sp<sup>3</sup>)-F结构中，具有极高的键能。这种固有的稳定性使得C-F键活化极具挑战性。本研究通过开发一种机械化学氢化脱氟策略，应对这一挑战，并从氟代化合物（包括芳基氟化物、烷基氟化物及全氟烷基物质）中回收有价值的碳氢化合物。该方法利用金属氮化物（特别是氮化镁）作为还原剂，这与以往将金属氮化物仅视为有机反应中氨替代物的认知形成鲜明对比。值得注意的是，该机械化学方案甚至能实现持久性聚四氟乙烯（特氟龙®）——一种典型的“永久化学品”——的降解。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The carbon-fluorine (C-F) bond, present in both aromatic C(sp<sup>2</sup>)-F and aliphatic C(sp<sup>3</sup>)-F moieties, possesses an exceptionally high bond energy. This inherent stability renders C-F bond activation highly challenging. In this work, we address this challenge and reclaim valuable hydrocarbons from fluorinated compounds, including aryl fluorides, alkyl fluorides, and perfluoroalkyl substances, by developing a mechanochemical hydrodefluorination strategy. This approach exploits metal nitrides, particularly magnesium nitride, as reductants, contrasting with previous perception of metal nitrides as merely ammonia surrogates in organic reactions. Remarkably, this mechanochemical protocol achieves the degradation of even persistent polytetrafluoroethylene (Teflon®), a prototypical "forever chemical".

</details>
<br>

**关键词**: mechanochemical hydrodefluorination, metal nitrides, carbon-fluorine bond activation, fluorinated compounds, polytetrafluoroethylene degradation, magnesium nitride, hydrocarbon recovery, reducing power

---

## Token 消耗统计

- **总计**: 118,268 tokens（输入 82,160 / 输出 36,108）
