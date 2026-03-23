# 📊 Nature Communications 研究报告 (2026-03-18)

> 生成时间: 2026-03-18 18:05:33
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

- **总抓取**: 47 篇
- **及格论文**: 1 篇 (2.1%)
- **深度分析**: 1 篇

---

## ⭐ 及格论文详细分析

### 1. FineST: contrastive learning integrates histology and spatial transcriptomics for nuclei-resolved li

**作者**: Lingyu Li, Tianjie Wang, Zhuo Liang, Huajian Yu, Stephanie Ma, Lequan Yu, Yuanhua HUANG
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70528-7](https://doi.org/10.1038/s41467-026-70528-7)

**评分**: 57.0 / 29.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical image segmentation | 1.0 | 8.0/10 | 8.0 |
| deep learning medical imaging | 1.0 | 10.0/10 | 10.0 |
| AI for diagnosis | 1.0 | 6.0/10 | 6.0 |
| prognosis prediction | 1.0 | 5.0/10 | 5.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 10.0/10 | 10.0 |
| foundation models medical imaging | 1.0 | 10.0/10 | 10.0 |

**评分理由**: 论文FineST专注于空间转录组学（ST）与组织学图像的融合分析，属于生物医学图像分析范畴，但并非传统医学影像（如CT/MRI/超声）。其核心是使用深度学习（对比学习）整合多模态数据（ST+组织学图像），并利用基础模型（histology foundation model）。因此，与'deep learning medical imaging'、'multimodal medical imaging'和'foundation models medical imaging'高度相关（10分）。论文涉及细胞核分割，与'medical image segmentation'相关（8分），整体属于'medical image analysis'（8分）。研究应用于癌症分析（如肿瘤-免疫互作），与'AI for diagnosis'有一定关联（6分），与'prognosis prediction'关联较弱（5分）。论文未涉及手术规划，与'surgical planning'完全无关（0分）。

</details>
<br>

!!! info Semantic Scholar TL;DR

    FineST, a deep contrastive learning model that leverages a histology foundation model to fuse ST and histology images, enabling Fine-grained Spatial Transcriptomics analysis, is introduced, highlighting a new paradigm in ST analysis through the integration of readily available histology images.

!!! tip deepseek-chat TL;DR

    该研究提出了FineST模型，通过深度学习融合组织学图像与空间转录组数据，解决了高分辨率RNA表达估算和细胞间通讯模式识别的难题，并在多种癌症数据集中验证了其优越性能。

<details open>
<summary>摘要翻译</summary>

> 空间转录组学（ST）已成为分析从胚胎发育到癌症进展等多种生物过程中细胞间通讯（CCC）的有力工具。然而，其有限的分辨率和较高的数据稀疏性阻碍了对复杂组织内CCC模式的详细表征。本文介绍FineST，一种深度对比学习模型，它利用组织学基础模型融合ST与组织学图像，实现精细空间转录组学分析。该方法有助于实现精确的细胞核分割、高分辨率RNA表达插补以及复杂配体-受体相互作用的识别。通过结直肠癌VisiumHD和乳腺癌Xenium数据集，我们证明FineST在高分辨率RNA插补、细胞类型预测和CCC模式发现方面显著优于现有方法。通过聚焦应用于Visium平台，FineST揭示了跨多种癌症类型的肿瘤-免疫相互作用的新生物学见解，包括乳腺癌的侵袭前沿、鼻咽癌的三级淋巴结构以及肝细胞癌的PD-1治疗耐药屏障。这些发现通过整合易于获取的组织学图像，凸显了ST分析的新范式。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Spatial transcriptomics (ST) has emerged as a powerful tool for analyzing cell-cell communication (CCC) across various biological processes, ranging from embryonic development to cancer progression. However, its limited resolution and high data sparsity hinder the detailed characterization of CCC patterns within complex tissues. Here, we introduce FineST , a deep contrastive learning model that leverages a histology foundation model to fuse ST and histology images, enabling Fine -grained S patial T ranscriptomics analysis. This approach facilitates precise nuclei segmentation, high-resolution RNA expression imputation, and the identification of intricate ligand-receptor interactions. Using both colorectal cancer VisiumHD and breast cancer Xenium datasets, we demonstrate that FineST significantly outperforms existing methods in high-resolution RNA imputation, cell type prediction, and CCC pattern discovery. With focused application to the Visium platform, FineST reveals novel biological insights into tumor-immune interactions across multiple cancer types, including invasive fronts in breast cancer, tertiary lymphoid structures in nasopharyngeal carcinoma, and PD-1 therapy resistance barriers in hepatocellular carcinoma. These findings highlight a new paradigm in ST analysis through the integration of readily available histology images.

</details>
<br>

**关键词**: spatial transcriptomics, histology images, contrastive learning, nuclei segmentation, RNA expression imputation, cell-cell communication, cancer analysis, multimodal fusion

**深度分析**:

#### FineST：基于对比学习整合组织学与空间转录组学实现细胞核分辨率配体-受体分析

**摘要**:

> 本研究针对空间转录组学（ST）在细胞间通讯分析中存在的分辨率有限、数据稀疏性问题，提出了一种名为FineST的深度对比学习模型。该模型通过整合组织学图像与空间转录组数据，利用组织学基础模型实现多模态数据融合，能够进行精细的细胞核分割、高分辨率RNA表达插补以及复杂配体-受体相互作用的识别。研究在结直肠癌VisiumHD和乳腺癌Xenium数据集上验证了FineST在RNA插补、细胞类型预测和细胞通讯模式发现方面的优越性能。特别在Visium平台应用中，该模型揭示了乳腺癌侵袭前沿、鼻咽癌三级淋巴结构、肝癌PD-1治疗耐药屏障等多个癌症类型中肿瘤-免疫相互作用的新生物学见解，为空间转录组分析提供了新的范式。

**创新点**:
- 提出首个基于对比学习的组织学与空间转录组多模态融合框架FineST
- 实现细胞核分辨率的空间转录组分析，突破传统ST技术分辨率限制
- 开发高精度RNA表达插补方法，有效缓解空间转录组数据稀疏性问题
- 建立精细化的配体-受体相互作用识别系统，揭示细胞通讯空间模式
- 构建可扩展的Python软件包，提供完整的分析流程和可视化工具

<details>
<summary>方法</summary>

!!! info

    研究采用深度对比学习技术路线：1）数据预处理阶段对齐组织学图像与空间转录组数据；2）利用预训练的组织学基础模型（如Virchow2）提取图像特征；3）设计双模态对比学习框架，通过最大化组织学特征与对应空间转录组特征的互信息实现特征融合；4）构建编码器-解码器架构进行高分辨率RNA表达预测；5）集成细胞分割算法实现细胞核级别分析；6）基于CellChat等数据库进行配体-受体相互作用推断；7）在多个癌症数据集上进行验证和生物学解释。

</details>
<br>

**关键结果**:
- 在结直肠癌和乳腺癌数据集上，FineST在RNA表达插补精度显著优于现有方法
- 实现细胞类型预测准确率提升，特别是在肿瘤微环境复杂区域
- 成功识别多个癌症类型中新的肿瘤-免疫相互作用空间模式
- 发现乳腺癌侵袭前沿、鼻咽癌三级淋巴结构、肝癌免疫治疗耐药相关的特异性配体-受体对
- 验证了组织学图像作为补充信息源对提升空间转录组分析分辨率的有效性

**技术栈**: 深度学习框架：PyTorch, 对比学习算法：InfoNCE损失函数, 基础模型：Virchow2（病理图像预训练模型）, 细胞分割：Hover-Net改进版本, 空间分析：Scanpy、CellChat, 数学方法：互信息最大化、自编码器、高斯过程回归, 可视化工具：Matplotlib、Plotly

<details>
<summary>优点</summary>

- 创新性地将组织学基础模型与空间转录组分析相结合，充分利用多模态数据互补性
- 方法具有较好的通用性，在Visium、Xenium等多个平台数据上验证有效
- 提供完整的开源软件包和详细文档，便于学术社区使用和复现
- 生物学发现丰富，为多个癌症类型的免疫治疗研究提供新见解
- 技术路线设计合理，对比学习框架能有效学习跨模态特征表示

</details>
<br>

<details>
<summary>局限</summary>

- 方法依赖于高质量的组织学图像与空间转录组数据对齐，对齐误差可能影响结果
- 在极稀疏的空间转录组数据区域，插补结果可能存在不确定性
- 当前主要验证于癌症组织，在其他组织类型（如发育组织）的普适性需进一步验证
- 计算资源需求较高，特别是处理大尺寸全切片图像时
- 配体-受体数据库的完整性可能限制相互作用发现的全面性

</details>
<br>

**与研究方向的相关性**: {'医学图像分割与解剖结构建模': '论文核心涉及组织学图像的细胞核分割和空间结构建模，直接相关', '深度学习医学影像分析': '采用深度对比学习框架处理组织学图像，高度相关', 'AI疾病诊断与预后预测': '通过分析肿瘤微环境细胞通讯模式，为癌症诊断和治疗提供新见解，间接相关', '多模态医学数据融合': '核心创新点在于组织学图像与空间转录组数据的深度融合，高度相关', '鲁棒可泛化医疗AI模型': '在多个癌症数据集和平台验证，体现了一定的泛化能力，相关'}

---

## 📋 所有论文列表

### 1. ✅ FineST: contrastive learning integrates histology and spatial transcriptomics for nuclei-resolved ligand-receptor analysis

**作者**: Lingyu Li, Tianjie Wang, Zhuo Liang, Huajian Yu, Stephanie Ma, Lequan Yu, Yuanhua HUANG
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70528-7](https://doi.org/10.1038/s41467-026-70528-7)

**评分**: 57.0 / 29.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical image segmentation | 1.0 | 8.0/10 | 8.0 |
| deep learning medical imaging | 1.0 | 10.0/10 | 10.0 |
| AI for diagnosis | 1.0 | 6.0/10 | 6.0 |
| prognosis prediction | 1.0 | 5.0/10 | 5.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 10.0/10 | 10.0 |
| foundation models medical imaging | 1.0 | 10.0/10 | 10.0 |

**评分理由**: 论文FineST专注于空间转录组学（ST）与组织学图像的融合分析，属于生物医学图像分析范畴，但并非传统医学影像（如CT/MRI/超声）。其核心是使用深度学习（对比学习）整合多模态数据（ST+组织学图像），并利用基础模型（histology foundation model）。因此，与'deep learning medical imaging'、'multimodal medical imaging'和'foundation models medical imaging'高度相关（10分）。论文涉及细胞核分割，与'medical image segmentation'相关（8分），整体属于'medical image analysis'（8分）。研究应用于癌症分析（如肿瘤-免疫互作），与'AI for diagnosis'有一定关联（6分），与'prognosis prediction'关联较弱（5分）。论文未涉及手术规划，与'surgical planning'完全无关（0分）。

</details>
<br>

!!! info Semantic Scholar TL;DR

    FineST, a deep contrastive learning model that leverages a histology foundation model to fuse ST and histology images, enabling Fine-grained Spatial Transcriptomics analysis, is introduced, highlighting a new paradigm in ST analysis through the integration of readily available histology images.

!!! tip deepseek-chat TL;DR

    该研究提出了FineST模型，通过深度学习融合组织学图像与空间转录组数据，解决了高分辨率RNA表达估算和细胞间通讯模式识别的难题，并在多种癌症数据集中验证了其优越性能。

<details open>
<summary>摘要翻译</summary>

> 空间转录组学（ST）已成为分析从胚胎发育到癌症进展等多种生物过程中细胞间通讯（CCC）的有力工具。然而，其有限的分辨率和较高的数据稀疏性阻碍了对复杂组织内CCC模式的详细表征。本文介绍FineST，一种深度对比学习模型，它利用组织学基础模型融合ST与组织学图像，实现精细空间转录组学分析。该方法有助于实现精确的细胞核分割、高分辨率RNA表达插补以及复杂配体-受体相互作用的识别。通过结直肠癌VisiumHD和乳腺癌Xenium数据集，我们证明FineST在高分辨率RNA插补、细胞类型预测和CCC模式发现方面显著优于现有方法。通过聚焦应用于Visium平台，FineST揭示了跨多种癌症类型的肿瘤-免疫相互作用的新生物学见解，包括乳腺癌的侵袭前沿、鼻咽癌的三级淋巴结构以及肝细胞癌的PD-1治疗耐药屏障。这些发现通过整合易于获取的组织学图像，凸显了ST分析的新范式。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Spatial transcriptomics (ST) has emerged as a powerful tool for analyzing cell-cell communication (CCC) across various biological processes, ranging from embryonic development to cancer progression. However, its limited resolution and high data sparsity hinder the detailed characterization of CCC patterns within complex tissues. Here, we introduce FineST , a deep contrastive learning model that leverages a histology foundation model to fuse ST and histology images, enabling Fine -grained S patial T ranscriptomics analysis. This approach facilitates precise nuclei segmentation, high-resolution RNA expression imputation, and the identification of intricate ligand-receptor interactions. Using both colorectal cancer VisiumHD and breast cancer Xenium datasets, we demonstrate that FineST significantly outperforms existing methods in high-resolution RNA imputation, cell type prediction, and CCC pattern discovery. With focused application to the Visium platform, FineST reveals novel biological insights into tumor-immune interactions across multiple cancer types, including invasive fronts in breast cancer, tertiary lymphoid structures in nasopharyngeal carcinoma, and PD-1 therapy resistance barriers in hepatocellular carcinoma. These findings highlight a new paradigm in ST analysis through the integration of readily available histology images.

</details>
<br>

**关键词**: spatial transcriptomics, histology images, contrastive learning, nuclei segmentation, RNA expression imputation, cell-cell communication, cancer analysis, multimodal fusion

---

### 2. ❌ A selective enrichment and specific probe terminal mediated strategy for highly sensitive detection of microRNAs

**作者**: Zecheng Zhong, Weida Huang, Jinhua Ren, L. Yuan, Qiurong Zhong, Yi Ge, Jin Wang, Jiyu Xiang, Lesi Lin, Yanmei Chen, Jingjing Xu, ZY Zhang, T. Li, Jun Zhang, Jianda Hu, Shuizhen He, Lei Tang, Shengxiang Ge, Ningshao Xia, Ting Yang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70811-7](https://doi.org/10.1038/s41467-026-70811-7)

**评分**: 2.0 / 29.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical image segmentation | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |
| AI for diagnosis | 1.0 | 2.0/10 | 2.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 0.0/10 | 0.0 |
| foundation models medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是基于SE-SPTM-PCR平台的microRNA检测技术，用于液体活检和癌症诊断。这与医学影像分析、分割、深度学习医学影像、手术规划、多模态医学影像、基础模型医学影像等关键词完全无关（0分）。与AI诊断有一定关联（2分），因为论文涉及通过生物标志物检测提高诊断准确性，但未使用AI方法。与预后预测无关（0分），论文未涉及疾病进展预测。

</details>
<br>

!!! info Semantic Scholar TL;DR

    SE-SPTM-PCR is presented, a detection platform integrating selective miRNA enrichment using locked nucleic acid probes with specific probe terminal mediated RT-qPCR that eliminates nonspecific amplification and achieves 100-fold higher sensitivity than conventional stem-loop RT-qPCR.

!!! tip deepseek-chat TL;DR

    该论文开发了一种名为SE-SPTM-PCR的高灵敏度microRNA检测平台，显著提高了结直肠癌、HCMV再激活和鼻咽癌的诊断准确性。

<details open>
<summary>摘要翻译</summary>

> 摘要：微小核糖核酸（miRNA）是极具前景的液体活检生物标志物，但其临床转化受到检测挑战的阻碍，包括丰度低、序列相似性高以及背景干扰。本文提出SE-SPTM-PCR检测平台，该平台整合了使用锁核酸探针的选择性miRNA富集技术与特异性探针末端介导的逆转录定量聚合酶链式反应（RT-qPCR）。研究表明，SE-SPTM-PCR能消除非特异性扩增，并比传统的茎环RT-qPCR灵敏度提高100倍。在临床研究中，针对结直肠癌检测，SE-SPTM-PCR显著提升了hsa-miR-92a-3p的性能：在48例患者与48例对照的对比中，其受试者工作特征曲线下面积（AUC）从0.72提高至0.85。此外，该平台还成功恢复了两种已被弃用生物标志物的应用价值：在32例DNA阳性与32例DNA阴性造血干细胞移植受者的人巨细胞病毒（HCMV）再激活监测中，hcmv-miR-UL22A-5p的AUC达到0.95；针对鼻咽癌检测，在40例患者与40例对照中，ebv-miR-BART3-3p的AUC达到完美的1.0。该平台为基于miRNA的液体活检提供了稳健工具，通过提升诊断准确性，有望支持早期疾病检测与个性化治疗策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract MicroRNAs are promising liquid biopsy biomarkers, but their clinical translation is hindered by detection challenges, including low abundance, high sequence similarity, and background interference. Here we present SE-SPTM-PCR, a detection platform integrating selective miRNA enrichment using locked nucleic acid probes with specific probe terminal mediated RT-qPCR. We show that SE-SPTM-PCR eliminates nonspecific amplification and achieves 100-fold higher sensitivity than conventional stem-loop RT-qPCR. In clinical studies, SE-SPTM-PCR significantly improves hsa-miR-92a-3p performance for colorectal cancer detection, increasing its AUC from 0.72 to 0.85 in 48 patients versus 48 controls. Additionally, SE-SPTM-PCR also restores utility to two abandoned biomarkers: For HCMV reactivation monitoring in 32 DNA positive and 32 DNA negative hematopoietic stem cell transplant recipients, hcmv-miR-UL22A-5p achieves an AUC of 0.95. For nasopharyngeal carcinoma, ebv-miR-BART3-3p reaches a perfect AUC of 1.0 in 40 patients and 40 controls. This platform provides a robust tool for miRNA-based liquid biopsy, offering enhanced diagnostic accuracy to support early disease detection and personalized treatment strategies.

</details>
<br>

**关键词**: microRNA detection, liquid biopsy, SE-SPTM-PCR, diagnostic accuracy, colorectal cancer, HCMV reactivation, nasopharyngeal carcinoma, biomarker

---

### 3. ❌ Sub-5 nm high-entropy nanoalloys beyond the hume-rothery limit

**作者**: Yiqian Du, Xiaodi Zhou, Bangxin Li, Zhizhong Wang, Enyuan Zhou, Yihao Liu, Huibin Zhang, Xuhui Xiong, Jiacheng Cui, Hualiang Lv, Renchao Che
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**DOI**: [10.1038/s41467-026-69681-w](https://doi.org/10.1038/s41467-026-69681-w)

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

**评分理由**: 论文标题和摘要显示该研究聚焦于材料科学领域的高熵纳米合金，涉及亚5纳米尺度、Hume-Rothery极限等材料学概念，与医学图像分析、人工智能临床决策支持等关键词完全无关。所有关键词均未在论文内容中出现或相关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了亚5纳米高熵纳米合金，突破了Hume-Rothery极限，实现了优异的催化性能。

**关键词**: high-entropy nanoalloys, sub-5 nm, Hume-Rothery limit, catalytic performance, nanomaterials, alloy design, advanced materials

---

### 4. ❌ Heat-assisted hot-hole transfer increases the surface-enhanced Raman activity of Au-TiO2 nanoarrays

**作者**: Mengya Zhang, Tongcheng Yu, Hao Liu, Chao Lin, Yaping Yang, Bowen Lv, Qi Zhang, Ming Chen, Tianshuai Wang, weihong Hua, Kai Han
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**DOI**: [10.1038/s41467-026-70822-4](https://doi.org/10.1038/s41467-026-70822-4)

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

**评分理由**: 该论文研究Au-TiO2纳米阵列作为SERS基底在高温下增强拉曼信号的机制，属于材料科学、化学分析和光谱技术领域。论文内容完全不涉及医学图像分析、深度学习、疾病诊断、预后预测、手术规划或多模态医学成像等医疗AI相关主题。所有关键词与论文研究内容无任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了传统表面增强拉曼光谱在高温环境下活性损失的问题，通过合成Au-TiO2纳米阵列并发现热辅助空穴转移机制，实现了在180°C时拉曼信号强度比22°C时增强11.41倍。

<details open>
<summary>摘要翻译</summary>

> 摘要：在光热协同诱导的物理与化学过程中监测分子演化，对于化学、材料及能源研究等领域具有至关重要的意义。表面增强拉曼光谱（Surface-enhanced Raman spectroscopy, SERS）技术因其高灵敏度、实时性与无标记检测的优势，在此方面展现出巨大潜力。然而，传统SERS在高温环境中应用时，常因活性不可避免的丧失与灵敏度下降而面临挑战。本研究合成了Au-TiO₂纳米阵列作为SERS基底，并观察到拉曼信号随温度升高而异常增强的现象：在180°C时信号强度较22°C时提升了11.41倍。这种高温下拉曼活性的增强归因于一种深层机制：热辅助空穴转移，即热量促进了785 nm光子诱导的空穴从Au向TiO₂的转移。本工作拓展了SERS技术在高温化学分析与分子诊断领域的应用前景。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Monitoring the evolution of molecules during photo and thermal synergistically induced physical and chemical processes is of paramount interest in fields including chemical, material, and energy research. Surface-enhanced Raman spectroscopy (SERS) is a highly promising technology in this regard, offering advantages of sensitivity, real-time, and label-free detection. However, the application of conventional SERS in high-temperature environments has faced challenges due to the inevitable loss of activity and decline in sensitivity. Herein, we synthesize Au-TiO 2 nanoarrays as SERS substrates, and an anomalous enhancement of Raman signal with increasing temperature is observed. The signal intensity increases by 11.41 times at 180 °C compared to that at 22 °C. This high-temperature enhancement in Raman activity is attributed to an underlying mechanism: heat-assisted hot-hole transfer, which enables 785 nm photon-induced hot-hole transfer from Au to TiO 2 . Our work expands the application of the SERS technique for high-temperature chemical analysis and molecular diagnostics.

</details>
<br>

**关键词**: surface-enhanced Raman spectroscopy, Au-TiO2 nanoarrays, high-temperature SERS, hot-hole transfer, Raman signal enhancement, molecular diagnostics, thermal-assisted enhancement, nanostructured substrates

---

### 5. ❌ Exploring electron spin dynamics in spin chains using defects as a quantum probe

**作者**: L. Soriano, Avdhesh Kumar, Guillaume Gerbaud, A. Savoyant, Rémy Dassonneville, H. Vezin, Olivier Jeannin, Maylis Orio, Marc Fourmigué, Sylvain Bertaina
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**arXiv链接**: [https://arxiv.org/abs/2512.06722](https://arxiv.org/abs/2512.06722)
**DOI**: [10.1038/s41467-026-70589-8](https://doi.org/10.1038/s41467-026-70589-8)

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

**评分理由**: 论文研究的是量子物理中的电子自旋动力学和缺陷作为量子探针在自旋链中的应用，属于凝聚态物理和量子信息领域。所有评分关键词均涉及医学影像分析、人工智能临床决策支持等医学应用方向，与论文的物理研究内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究利用缺陷作为量子探针探索自旋链中的电子自旋动力学，揭示了自旋链系统的量子行为和缺陷的探测能力。

**关键词**: electron spin dynamics, spin chains, quantum probe, defects, quantum sensing, magnetic resonance, solid-state physics

---

### 6. ❌ Calcium-mediated calreticulin-IRE1α interaction drives dynamic fluctuation of IRE1α activity under chronic endoplasmic reticulum stress

**作者**: Jianwei Cao, Xudong Zhao, Yunxin Xu, Chen Yang, Yazhen Huo, Ting Li, Wenjia Gu, Lei Wang, Youjun Wang, Likun Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**DOI**: [10.1038/s41467-026-70679-7](https://doi.org/10.1038/s41467-026-70679-7)

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

**评分理由**: 论文研究的是细胞生物学中内质网应激的分子机制，具体探讨钙离子介导的calreticulin-IRE1α相互作用如何调节IRE1α活性。研究内容完全属于基础分子生物学领域，涉及蛋白质相互作用、信号通路和细胞应激反应，与医学影像分析、人工智能、临床决策支持等关键词无任何关联。所有关键词均与论文主题无关，因此全部评分为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This study suggests a calcium-mediated, calreticulin-driven IRE1α activity fluctuation, representing an intermediate status that the cell adopts to cope with chronic ER stress that may exist under both pathophysiological and physiological conditions.

!!! tip deepseek-chat TL;DR

    该研究揭示了在慢性内质网应激条件下，钙离子介导的calreticulin-IRE1α相互作用驱动IRE1α活性动态波动的分子机制。

**关键词**: endoplasmic reticulum stress, IRE1α, calreticulin, calcium signaling, protein interaction, molecular mechanism, cellular stress response

---

### 7. ❌ Local lateral connectivity is sufficient for replicating cortex-like topographical organization in deep neural networks

**作者**: Xinyu Qian, Amir Ozhan Dehghani, Asa Farahani, Pouya Bashivan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**DOI**: [10.1038/s41467-026-70065-3](https://doi.org/10.1038/s41467-026-70065-3)

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

**评分理由**: 论文研究的是深度神经网络中局部横向连接如何模拟大脑皮层地形组织，属于计算神经科学和机器学习基础研究，与医学影像分析、临床决策支持、疾病诊断、手术规划等医疗应用领域完全无关。所有关键词均未在标题或摘要中出现，也没有任何医疗影像或临床应用的提及。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过实验证明，在深度神经网络中仅使用局部横向连接就足以复制大脑皮层的地形组织模式，揭示了神经网络结构与生物视觉系统组织之间的相似性。

**关键词**: local lateral connectivity, cortex-like topographical organization, deep neural networks, visual cortex, neural network architecture, computational neuroscience, machine learning

---

### 8. ❌ Oligomerization-competent PIF4 drives thermomorphogenesis through functional redundancy in transactivation and DNA binding

**作者**: Haibo Xiong, Abhishesh Bajracharya, Ranjeeta Odari, Eden E. Bayer, Alyssa Stoner, Anupa Wasti, Jing Xi, Scott R. Baerson, Meng Chen, Yongjian Qiu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**DOI**: [10.1038/s41467-026-70748-x](https://doi.org/10.1038/s41467-026-70748-x)

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

**评分理由**: 论文研究植物生物学中PIF4转录因子在热形态建成中的作用机制，涉及分子生物学、遗传学和植物生理学，与医学影像分析、人工智能临床决策支持、疾病诊断预测、手术规划等医疗领域完全无关。所有关键词均属于医疗AI领域，而论文主题是植物热响应机制，两者无任何交集。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is suggested that PIF4's oligomerization competence contributes significantly to thermomorphogenesis by enabling partner recruitment, allowing DNA-binding and transactivation functions to be supplied in trans.

!!! tip deepseek-chat TL;DR

    该研究揭示了PIF4转录因子通过功能冗余的转录激活和DNA结合能力驱动植物热形态建成的分子机制。

**关键词**: PIF4, thermomorphogenesis, oligomerization, transcription factor, functional redundancy, DNA binding, transactivation, plant biology

---

### 9. ❌ A highly potent nanobody-based bispecific therapeutic provides broad-spectrum protection against ebolavirus

**作者**: Meihua Wang, Xinghai Zhang, Wujian Li, Yanfeng Yao, Entao Li, Baoyue Zhang, Jinge Zhou, Shunli Liu, Yongxiang Gao, Zhongliang Zhu, Lixia Zhu, Mengyao Liu, Jing Hu, Cheng Peng, Fangxu Li, Miaoyu Chen, Hang Liu, Chengbing Yao, Yuhua Shang, Feihu Yan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**DOI**: [10.1038/s41467-026-70464-6](https://doi.org/10.1038/s41467-026-70464-6)

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

**评分理由**: 论文研究的是针对埃博拉病毒的纳米抗体双特异性治疗药物开发，属于病毒学、免疫学和药物研发领域。标题和摘要内容完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或基础模型等关键词。所有关键词与论文主题完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Two camelid-derived nanobodies (1A10 and BA2) are identified that neutralize EBOV, SUDV, and BDBV in vitro and protect female rodents against these pathogens and highlight compact antibodies for next-generation antivirals.

!!! tip deepseek-chat TL;DR

    该研究开发了一种基于纳米抗体的双特异性治疗药物，能够提供针对埃博拉病毒的广谱保护作用。

**关键词**: nanobody, bispecific therapeutic, broad-spectrum protection, ebolavirus, antibody therapy, viral infection, immunotherapy, drug development

---

### 10. ❌ Single-cell spatial map of cis-regulatory elements for disease-related genes in the macaque cortex

**作者**: Juan Meng, Cheng Chen, Zhiyong Zhu, Yongkang Sun, Yiming Huang, Kaijie Hu, Jiqiang Fu, Luyan Wu, Ling Li, Yiqin Bai, Tianyi Fei, Zhen Liu, Chao Li, Zhiming Shen, Ya Liu, Chengyu Li, Tao Song, CiRong Liu, Muming Poo, Shiping Liu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-17
**DOI**: [10.1038/s41467-026-70497-x](https://doi.org/10.1038/s41467-026-70497-x)

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

**评分理由**: 论文研究的是灵长类动物大脑皮层的单细胞空间转录组学，重点在顺式调控元件和疾病相关基因的定位，属于基础神经科学和基因组学领域。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等临床应用方向，与论文的分子生物学和基因组学研究内容完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究构建了猕猴大脑皮层的单细胞空间转录组图谱，定位了疾病相关基因的顺式调控元件，揭示了其在皮层分层和细胞类型特异性中的调控作用。

**关键词**: single-cell spatial transcriptomics, macaque cortex, cis-regulatory elements, disease-related genes, spatial map, gene regulation, brain atlas, neuroscience

---

### 11. ❌ Structured coherent thermal emission from non-Hermitian metasurfaces

**作者**: Kaili Sun, Keren Wang, Wenyu Li, Yangjian Cai, Wei Wang, Y. S. Kivshar, Zhanghua Han
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70823-3](https://doi.org/10.1038/s41467-026-70823-3)

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

**评分理由**: 论文研究非厄米超表面热发射，属于光学、热辐射和纳米光子学领域，与医学图像分析、人工智能临床决策支持完全无关。所有关键词均涉及医学成像、诊断、预后或手术规划，而论文专注于物理和工程领域的热辐射控制，无任何医学应用或内容提及。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究如何利用非厄米超表面将非相干热波动转化为具有高方向性、窄带宽和定制矢量偏振的结构化相干热发射。

<details open>
<summary>摘要翻译</summary>

> 超表面能够通过定制化的方向性、光谱选择性和偏振控制来重塑热辐射，然而具有矢量偏振或结构光特性的相干热辐射仍鲜有实现。本文提出一种非厄米热超表面发射器，在实验中实现了高度定向、无彩虹效应且具有矢量偏振特性的热辐射。通过微扰诱导的布里渊区折叠，我们将高辐射损耗的法布里-珀罗模式与对称性保护的连续域束缚态耦合，并利用异常点附近的非厄米动力学实现色散与损耗的协同调控。这导致辐射品质因子在k空间发生剧烈变化，仅在选定的输出角度灵活触发矢量偏振发射。实验研究在3-5微米大气透明窗口观测到环形窄带热辐射，展现出高光谱纯度、极端方向性和清晰的矢量偏振特性。我们的设计建立了一个强大的非厄米平台，能够将非相干热涨落塑造成特定频率的相干矢量偏振光束，突破了相干性、光谱选择性与偏振控制之间的传统制约关系。该研究报道的非厄米热超表面发射器能够将非相干热涨落转化为具有高方向性、窄带宽和定制化矢量偏振特性的结构化相干热辐射。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Metasurfaces can reshape thermal radiation with tailored directionality, spectral selectivity and polarization control, yet coherent thermal emission exhibiting vectorial polarization or structured light property has been rarely demonstrated. Here, we introduce a non-Hermitian thermal meta-emitter that experimentally generates highly directional, rainbow-free, vectorial-polarized thermal emission. Through perturbation-induced Brillouin-zone folding, we couple high-radiative-loss Fabry–Perót modes to symmetry-protected bound states in the continuum and exploit non-Hermitian dynamics near exceptional points to achieve simultaneous dispersion and loss engineering. This yields a sharp variation of the radiative Q-factor in k-space, flexibly triggering vectorial-polarized emissions only at selected output angles. Experimental studies reveal doughnut-shaped narrowband thermal emission in the 3–5 μm atmospheric transparency window, exhibiting high spectral purity, extreme directionality and distinct vectorial polarizations. Our design establishes a powerful non-Hermitian platform to sculpt incoherent thermal fluctuations into coherent vectorial-polarized beams at a specific frequency, overcoming trade-offs in coherence, spectral selectivity and polarization control. The authors report a non-Hermitian thermal meta-emitter capable of transforming incoherent thermal fluctuations into structured coherent thermal emission with high directionality, narrow bandwidth and tailored vectorial polarizations.

</details>
<br>

**关键词**: non-Hermitian metasurfaces, thermal emission, vectorial polarization, structured light, exceptional points, bound states in the continuum, directional emission, spectral purity

---

### 12. ❌ Learning earthquake ground motions via conditional generative modeling

**作者**: Pu Ren, Rie Nakata, Maxime Lacour, Ilan Naiman, Nori Nakata, Jialin Song, Zhengfa Bi, Osman Asif Malik, Dmitriy Morozov, Omri Azencot, N. Benjamin Erichson, Michael W. Mahoney
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70719-2](https://doi.org/10.1038/s41467-026-70719-2)

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

**评分理由**: 论文研究地震地面运动的生成建模，属于地球物理学和地震学领域，使用AI方法预测地震波谱。所有评分关键词均针对医学影像分析、临床诊断、手术规划等医疗健康应用，而本文完全不涉及任何医学、医疗影像或临床相关内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种条件生成模型CGM-GM，用于预测地震地面运动的高保真频谱，以补充传统物理模拟和经验模型，并在旧金山湾区地震数据上验证了其潜力。

<details open>
<summary>摘要翻译</summary>

> 摘要：预测未来地震的高保真地面运动对于地震危险性评估和基础设施韧性至关重要。传统经验模拟方法受限于稀疏的传感器分布和地理局部化的震源位置，而基于物理的模拟方法则计算成本高昂，且需要精确的地球结构和震源表征。我们提出了一种人工智能（AI）频谱图生成器——地面运动条件生成模型（Conditional Generative Modeling for Ground Motion, CGM-GM）。CGM-GM以地震震级、震源及传感器的地理坐标作为输入，经相位信息后处理后，能够捕捉空间连续的傅里叶振幅谱（FAS）以及P波和S波到时、波形持续时间等特性，而无需显式的物理约束。这一目标通过概率自编码器实现，该编码器提取时频域的潜在分布，并利用变分序列模型处理先验与后验分布。我们在具有高地震风险的旧金山湾区，使用小震级地震记录评估了CGM-GM的性能。结果表明，CGM-GM展现出补充基于物理的模拟与非遍历性经验地面运动模型的潜力，并在地震学及其他领域具有广阔应用前景。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Predicting high-fidelity ground motions for future earthquakes is crucial for seismic hazard assessment and infrastructure resilience. Conventional empirical simulations suffer from sparse sensor distribution and geographically localized earthquake locations, while physics-based methods are computationally intensive and require accurate representations of Earth structures and earthquake sources. We propose an artificial intelligence (AI) spectrogram generator, Conditional Generative Modeling for Ground Motion (CGM-GM). CGM-GM leverages earthquake magnitudes and geographic coordinates of earthquakes and sensors as inputs, when postprocessed with phase information, capturing spatially continuous Fourier amplitude spectra (FAS) as well as properties such as P and S arrivals, and waveform durations, without explicit physics constraints. This is achieved through a probabilistic autoencoder that extracts latent distributions in the time-frequency domain and variational sequential models for prior and posterior distributions. We evaluate the performance of CGM-GM using small-magnitude earthquake records from the San Francisco Bay Area, a region with high seismic risks. Here, we report that CGM-GM demonstrates potential for complementing physics-based simulations and non-ergodic empirical ground motion models, as well as shows promise in seismology and beyond.

</details>
<br>

**关键词**: earthquake ground motion, conditional generative modeling, seismic hazard assessment, Fourier amplitude spectra, probabilistic autoencoder, variational sequential models, non-ergodic empirical models, seismology

---

### 13. ❌ Space and space-time topologies in a type-II hyperbolic lattice

**作者**: Jingming Chen, Zebin Zhu, Minqi Cheng, Linyun Yang, Yuxin Zhong, Zhen Gao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**arXiv链接**: [https://arxiv.org/abs/2601.09140](https://arxiv.org/abs/2601.09140)
**DOI**: [10.1038/s41467-026-70706-7](https://doi.org/10.1038/s41467-026-70706-7)

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

**评分理由**: 论文标题和摘要显示该研究聚焦于物理和材料科学领域，具体研究双曲晶格中的空间和时空拓扑结构，属于凝聚态物理、拓扑光子学或材料物理范畴，与医学图像分析、临床决策支持、医疗AI等医学领域完全无关。所有关键词均涉及医疗应用和技术，因此相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究探讨了II型双曲晶格中空间和时空拓扑结构的理论特性，揭示了其独特的物理行为。

**关键词**: hyperbolic lattice, topology, space-time, type-II, photonic crystals, wave propagation, theoretical physics

---

### 14. ❌ High-accuracy fatigue life prediction and early fracture warning for ferromagnetic metals via spin correlation amplification

**作者**: Benniu Zhang, Liangshuo Zhang, X. Wu, Jigang Yu, Xiaochuan Cao, Haonan Xia, Z. F. Zhang, Xin Li, Fupeng Zhou, Jinglin Pan, Hui Jiang, Gang Zheng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70290-w](https://doi.org/10.1038/s41467-026-70290-w)

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

**评分理由**: 论文研究的是利用量子自旋相关放大效应进行铁磁金属疲劳寿命预测和早期断裂预警，属于材料科学、工程物理和量子传感领域。研究背景要求的是医学图像分析、人工智能临床决策支持等医学领域，论文内容完全不涉及医学图像、CT/MRI/超声、疾病诊断、手术规划或医疗AI模型。所有关键词均与医学相关，而论文是纯工程材料研究，因此所有关键词相关度均为0。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过量子自旋相关放大方法将微观原子变化放大为宏观磁信号，实现了铁磁金属的高精度疲劳寿命预测和早期断裂预警，预测准确度R²>0.9。

<details open>
<summary>摘要翻译</summary>

> 金属结构的突发疲劳失效每年引发数千起安全事故，造成数万人伤亡及近千亿美元经济损失。传统检测技术在捕捉亚纳米级原子位移与金属键局部断裂等早期疲劳损伤特征方面面临挑战。基于铁磁金属疲劳过程中结合力与交换相互作用同步弱化的机制，本研究通过外磁场激发量子自旋关联放大效应，获得了高灵敏度的疲劳观测结果。我们对193个铁磁金属样本进行了累计3700小时的疲劳试验，建立了疲劳引起的磁通量变化与结合力弱化程度之间的映射关系。该工作将宏观疲劳寿命预测与铁磁材料微观结构参数相结合，实现了R2 > 0.9的预测精度，提供了可靠的断裂前预警，有望缓解大型工程结构的疲劳断裂问题并降低相关经济损失。通过采用量子自旋关联放大方法将微观原子变化放大为宏观磁信号，本研究实现了对大型结构的高精度疲劳寿命预测与早期断裂预警。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Sudden fatigue failure of metallic structures triggers thousands of safety accidents annually, causing tens of thousands of casualties and economic losses approaching $100 billion. Traditional detection techniques face challenges in capturing early fatigue damage features like subnanometer atomic displacements and localized metal bond ruptures. Based on the synchronized weakening mechanism between binding forces and exchange interactions during fatigue processes in ferromagnetic metals, this study obtained high-sensitivity fatigue observations by exciting the quantum spin correlation amplification effect via an external magnetic field. We conducted fatigue tests on 193 ferromagnetic metal samples over 3700 cumulative hours, establishing a mapping relationship between fatigue-induced magnetic flux changes and the degree of binding force weakening. This work integrated macroscopic fatigue life prediction with ferromagnetic material microstructural parameters, achieving a prediction accuracy with R2 > 0.9 and providing a reliable prefracture warning, potentially mitigating fatigue fractures in large-scale engineering structures and reducing the associated economic losses. By employing a quantum spin correlation amplification method to magnify microscopic atomic changes into macroscopic magnetic signals, this study enables high-accuracy fatigue life prediction and early fracture warnings for large-scale structures.

</details>
<br>

**关键词**: fatigue life prediction, ferromagnetic metals, quantum spin correlation amplification, early fracture warning, magnetic flux changes, binding force weakening, large-scale engineering structures, fatigue failure

---

### 15. ❌ Toroidicity as a route towards non-volatile quaternary memory in antiferromagnets

**作者**: N. Qureshi, Adheena Painganoor, Mikkel C. Larsen, Mikkel Ravn-Feld, K. Beauvois, José  Alberto Rodríguez-Velamazán, David Vaknin, Paul Steffens, Rasmus Toft-Petersen, Niels Bech Christensen
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70767-8](https://doi.org/10.1038/s41467-026-70767-8)

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

**评分理由**: 论文标题和摘要显示该研究聚焦于反铁磁材料中的环形磁性和四态非易失性存储器，属于凝聚态物理和材料科学领域，与医学图像分析、人工智能临床决策支持等关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了反铁磁材料中环形磁性的物理机制，并探索了其作为实现四态非易失性存储器的潜在途径。

**关键词**: antiferromagnets, toroidicity, non-volatile memory, quaternary memory, magnetic materials, neutron diffraction, magnetic structure

---

### 16. ❌ Author Correction: Central American mountains inhibit eastern North Pacific seasonal tropical cyclone activity

**作者**: Dan Fu, Ping Chang, Christina M. Patricola-DiRosario, R. Saravanan, Xue Liu, Hylke E. Beck
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-68407-2](https://doi.org/10.1038/s41467-026-68407-2)

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

**评分理由**: 论文研究的是中美洲山脉对东太平洋季节性热带气旋活动的影响，属于气候学和气象学领域，与医学图像分析、人工智能临床决策支持等医疗领域完全无关。所有关键词均涉及医疗技术应用，而论文内容是关于地理特征与气候现象的物理关系研究，两者领域完全不同，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究发现中美洲山脉通过改变大气环流模式，抑制了东太平洋季节性热带气旋的活动。

**关键词**: Central American mountains, eastern North Pacific, tropical cyclone activity, seasonal variation, atmospheric circulation, geographic barrier, climate impact, meteorological modeling

---

### 17. ❌ Structural basis of lipid-linked galactan export by the mycobacterial ABC transporter Wzm-Wzt

**作者**: Alisa A. Garaeva, Viktória Fabianová, Karin Savková, Stanislav Huszár, Xiaochao Xue, Todd L. Lowary, Katarı́na Mikus̃ová, Markus A. Seeger
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70429-9](https://doi.org/10.1038/s41467-026-70429-9)

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

**评分理由**: 论文研究的是分枝杆菌细胞壁生物合成中ABC转运蛋白Wzm-Wzt的结构和功能机制，属于结构生物学和微生物学领域。所有评分关键词均涉及医学影像分析、人工智能诊断、手术规划等临床决策支持技术，与论文的结构生物学研究内容完全无关。论文未涉及任何医学影像处理、深度学习、AI诊断或手术相关技术。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Data suggests that the hydrophobic polyprenyl-moiety is translocated first, followed by the galactan-polysaccharide, which requires Wzm-Wzt to open a continuous channel through which the sugar chain is ratcheted at the expense of ATP hydrolysis, providing a rational basis for the development of drugs that inhibit mycobacterial cell wall biosynthesis.

!!! tip deepseek-chat TL;DR

    该研究通过冷冻电镜结构揭示了分枝杆菌ABC转运蛋白Wzm-Wzt转运脂质连接半乳糖的分子机制，为抑制结核分枝杆菌细胞壁生物合成的药物开发提供了结构基础。

<details open>
<summary>摘要翻译</summary>

> 摘要 分枝杆菌（包括结核分枝杆菌）具有独特的细胞包膜，其中含有阿拉伯半乳聚糖——一种对细胞壁完整性至关重要的异质多糖，也是多种结核病药物的作用靶点。阿拉伯半乳聚糖的胞质前体——脂联半乳聚糖（LLG）——由必需的ABC转运蛋白Wzm-Wzt跨质膜转运，其分子机制尚不明确。本研究通过冷冻电镜技术解析了脓肿分枝杆菌Wzm-Wzt在转运周期中不同构象的一系列结构。通过三种正交功能实验对LLG推测转运路径上的保守残基进行研究，发现胞质侧门控螺旋（GH）在多糖转运中起关键作用。我们的数据表明，疏水性的聚戊烯基部分首先被转运，随后半乳聚糖链的转运需要Wzm-Wzt打开一个连续通道，并通过消耗ATP水解使糖链以棘轮机制通过。本研究为开发抑制分枝杆菌细胞壁生物合成的药物提供了理论依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Mycobacteria, including Mycobacterium tuberculosis , possess a unique cell envelope containing arabinogalactan, a heteropolysaccharide critical for cell wall integrity and target of several tuberculosis drugs. The cytosolic precursor of arabinogalactan, lipid-linked galactan (LLG), is translocated across the plasma membrane by the essential ABC transporter Wzm-Wzt through a molecular mechanism that is poorly understood. Here, we present a series of cryo-EM structures of Wzm-Wzt from Mycobacterium abscessus , representing different conformations of the transport cycle. Conserved residues lining the proposed LLG translocation pathway were investigated by three orthologous functional assays, revealing that the cytosolic gate helix (GH) plays a key functional role in polysaccharide transport. Our data suggests that the hydrophobic polyprenyl-moiety is translocated first, followed by the galactan-polysaccharide, which requires Wzm-Wzt to open a continuous channel through which the sugar chain is ratcheted at the expense of ATP hydrolysis. Our results provide a rational basis for the development of drugs that inhibit mycobacterial cell wall biosynthesis.

</details>
<br>

**关键词**: Mycobacterium, ABC transporter, Wzm-Wzt, lipid-linked galactan, cryo-EM structures, cell wall biosynthesis, polysaccharide transport, ATP hydrolysis

---

### 18. ❌ Synchronous activation of striatal cholinergic interneurons induces local serotonin release

**作者**: Lior Matityahu, Zachary Hobel, Noa Berkowitz, Jeffrey M. Malgady, Naomi Gilin, Joshua L. Plotkin, Joshua A. Goldberg
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70359-6](https://doi.org/10.1038/s41467-026-70359-6)

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

**评分理由**: 该论文研究的是神经科学领域，具体关注纹状体胆碱能中间神经元如何通过烟碱型乙酰胆碱受体驱动局部血清素释放的神经机制，并使用Sapap3-/-小鼠模型研究强迫症样行为。论文内容完全属于基础神经生物学研究，涉及电生理、神经递质释放和动物行为模型，与医学影像分析、人工智能、临床决策支持、疾病诊断/预后、手术规划等关键词没有任何关联。所有关键词评分均为0分，因为论文完全不涉及这些主题。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A regionally confined form of acetylcholine-5-HT crosstalk in the striatum is demonstrated and CINs are identified as regulators of 5-HT dynamics in both healthy and pathological states.

!!! tip deepseek-chat TL;DR

    该研究发现纹状体胆碱能中间神经元通过激活血清素能轴突上的烟碱型受体驱动局部血清素释放，这一机制在强迫症样行为小鼠模型中增强，揭示了纹状体中乙酰胆碱-血清素交互的区域特异性调控。

<details open>
<summary>摘要翻译</summary>

> 纹状体胆碱能中间神经元（CINs）可通过多巴胺能轴突上表达的烟碱型乙酰胆碱受体（nAChRs）驱动局部多巴胺释放，但其在调节血清素（5-HT）信号中的作用尚不明确。本研究证明，CINs的同步激活可通过血清素能轴突上表达的nAChRs直接触发背侧纹状体的局部5-HT释放。尽管腹侧纹状体拥有更密集的血清素能神经支配，但此种CIN–5-HT耦合现象在该区域未被检测到。这种依赖nAChR的释放不仅提高了背侧纹状体的5-HT水平，还扩展了血清素能信号的空间作用范围。在Sapap3-/-小鼠（一种强迫症样行为模型）中，由于胆碱能功能亢进状态，该机制被放大，选择性地增强了单胺释放中依赖nAChR的组分。这些发现揭示了纹状体内一种区域局限的乙酰胆碱–5-HT交互作用形式，并确立了CINs在生理和病理状态下作为5-HT动态调节者的角色。局部纹状体血清素释放的神经机制尚未完全阐明。本研究作者发现，纹状体胆碱能中间神经元通过激活背侧（而非腹侧）纹状体中血清素能轴突上的烟碱型受体，驱动局部血清素释放。该机制扩展了血清素释放的空间范围，并在强迫行为小鼠模型中呈现过度增强现象。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Striatal cholinergic interneurons (CINs) can drive local dopamine release via nicotinic acetylcholine receptors (nAChRs) expressed on dopaminergic axons, but their role in modulating serotonin (5-HT) signaling is poorly understood. Here, we show that synchronous activation of CINs directly triggers local 5-HT release in the dorsal striatum via nAChRs expressed on serotonergic axons. This CIN–5-HT coupling is not detectable in the ventral striatum, despite its substantially denser serotonergic innervation. The nAChR-dependent release not only increases 5-HT levels in the dorsal striatum, but also expands the spatial footprint of serotonergic signaling. In Sapap3-/- mice, a model of obsessive-compulsive disorder (OCD)-like behavior, this mechanism is exaggerated due to a hypercholinergic state, selectively amplifying the nAChR-dependent component of monoamine release. These findings demonstrate a regionally confined form of acetylcholine–5-HT crosstalk in the striatum and identify CINs as regulators of 5-HT dynamics in both healthy and pathological states. Neural mechanisms underlying local striatal serotonin release are not fully understood. Here authors show that striatal cholinergic interneurons drive local serotonin release by activating nicotinic receptors on serotonergic axons in the dorsal but not ventral striatum. This mechanism expands the spatial range of serotonin release and is exaggerated in a mouse model of compulsive behavior.

</details>
<br>

**关键词**: striatal cholinergic interneurons, serotonin release, nicotinic acetylcholine receptors, dorsal striatum, Sapap3-/- mice, obsessive-compulsive disorder, monoamine release, neural mechanisms

---

### 19. ❌ Precise Quantum Chemistry calculations with few Slater Determinants

**作者**: Clemens Giuliani, Jannes Nys, Rocco Martinazzo, Giuseppe Carleo, Riccardo Rossi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**arXiv链接**: [https://arxiv.org/abs/2503.14502](https://arxiv.org/abs/2503.14502)
**DOI**: [10.1038/s41467-026-70255-z](https://doi.org/10.1038/s41467-026-70255-z)

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

**评分理由**: 论文标题和摘要显示该研究专注于量子化学计算，特别是使用少量Slater行列式进行精确计算，属于计算化学和量子物理领域。所有评分关键词均涉及医学影像分析、人工智能临床决策支持等医学应用领域，与论文的量子化学主题完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了量子化学中精确计算需要大量Slater行列式的问题，通过开发新方法实现了使用少量Slater行列式进行高精度量子化学计算。

**关键词**: quantum chemistry, Slater determinants, precise calculations, computational methods, electronic structure, wavefunction approximation, many-body systems

---

### 20. ❌ Light-programmable mechanical computing via polyaniline composite film

**作者**: Xiunan Yan, Yixiang Li, Yichen Zhao, Chen Pan, S. Frank Yan, Dong Yang, Gong-Jie Ruan, Hang Zhao, Fanqing Frank Chen, Xing-Jian Yangdong, Peng Wang, Wentao Yu, Yuekun Yang, Cong Wang, Bin Cheng, Shi-Jun Liang, Feng Miao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70425-z](https://doi.org/10.1038/s41467-026-70425-z)

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

**评分理由**: 论文研究的是基于聚苯胺复合薄膜的光可编程机械计算系统，用于可扩展逻辑运算和环境自适应光学伪装，属于材料科学、柔性电子和机械计算领域。所有评分关键词均涉及医学影像分析、AI医疗诊断、手术规划等医疗健康应用，而该论文完全不涉及任何医学、医疗影像或临床相关内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文开发了一种基于聚苯胺复合薄膜的光可编程机械计算系统，实现了可扩展的逻辑运算电路和环境自适应的光学伪装功能。

<details open>
<summary>摘要翻译</summary>

> 摘要：机械计算是一种极具前景的环境自适应信息处理范式。然而，现有实现方案通常受限于有限的架构可扩展性，且其在实际场景中的应用模式仍不够明确。本文开发了一种光可编程机械计算系统，该系统不仅能执行可扩展的逻辑运算，还能实现环境自适应光学伪装。该系统基于聚苯胺复合薄膜（PCF, polyaniline composite film），该薄膜将光响应性伸缩元件与柔性导电层集成在一起。光照射动态调制导电通路，从而产生光控单刀单掷（SPST）和单刀双掷（SPDT）继电器，这些继电器能够重新配置信号传输路径。通过互连这些继电器，可以构建基本逻辑门和2位全加器电路，从而建立了一种可扩展的光可编程机械计算范式。此外，我们实现了一种自适应伪装功能，该功能能够感知环境纹理并生成匹配的光学图案，展示了其作为能够与环境交互的智能蒙皮的潜力。这项工作建立了一个光可编程、通路可重构的机械计算框架，为自主和自适应智能系统拓展了可能性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Mechanical computing represents a highly promising paradigm for environment-adaptive information processing. However, existing implementations are generally constrained by limited architectural scalability, and their modes of application in practical scenarios remain insufficiently defined. Here, we develop a light-programmable mechanical computing system that not only performs scalable logic operations but also enables environment-adaptive optical camouflage. The system is based on a polyaniline composite film (PCF) that integrates light-responsive expansion–contraction elements with a flexible conductive layer. Light illumination dynamically modulates the conductive pathways, giving rise to optically controlled single-pole single-throw (SPST) and single-pole double-throw (SPDT) relays that reconfigure signal transmission routes. Interconnecting these relays enables the construction of basic logic gates and 2-bit full-adder circuits, establishing a scalable paradigm for light-programmable mechanical computation. Moreover, we implement an adaptive camouflage function that senses environmental textures and generates matching optical patterns, demonstrating potential for intelligent skin applications capable of environmental interaction. This work establishes a light-programmable, pathway-reconfigurable mechanical computing framework, expanding possibilities for autonomous and adaptive intelligent systems.

</details>
<br>

**关键词**: light-programmable mechanical computing, polyaniline composite film, optical camouflage, logic gates, adaptive intelligent systems, environment-adaptive, signal transmission reconfiguration, scalable computing paradigm

---

### 21. ❌ Ynimines as versatile precursors to 2-imido- and 2-amido-1,3-dienes for stereodivergent diels–alder reactions

**作者**: Ruijia Wang, Xin-Qi Zhu, Maël Djaïd, Rémi Lavernhe, Wang, Qian, Janice, Jieping Zhu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70363-w](https://doi.org/10.1038/s41467-026-70363-w)

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

**评分理由**: 该论文属于有机化学合成领域，研究ynimines转化为2-imido/amido-1,3-dienes及其在Diels-Alder反应中的应用，与医学影像分析、人工智能、临床决策支持等关键词完全无关。所有关键词均未在标题或摘要中出现，也无任何医学影像、AI或临床相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文开发了一种将ynimines转化为2-imido/amido-1,3-dienes的通用策略，并利用这些中间体实现了立体发散的Diels-Alder反应，高效合成了具有特定立体构型的环己烯衍生物。

<details open>
<summary>摘要翻译</summary>

> 摘要 与化学性质已被广泛探索的炔酰胺相比，炔亚胺尽管具有丰富的官能团，但在有机合成中仍未得到充分利用。本文报道了一种通过炔亚胺与羧酸反应来获取合成上具有挑战性的构建模块——2-亚氨基-1,3-二烯的通用策略。基于该转化，我们开发了炔亚胺、羧酸与缺电子烯烃的三组分反应，能够高效合成1-亚氨基-3,4-反式二取代环己-1-烯。该反应序列经由区域选择性氢酰氧基化与Mumm重排生成2-亚氨基-1,3-二烯，继而发生狄尔斯-阿尔德环加成反应。其分子内变体能构建反式稠合三环结构，类似于反式-Δ⁹-四氢大麻酚。通过化学选择性水解，可将2-亚氨基-1,3-二烯进一步转化为2-酰胺基-1,3-二烯，从而实现手性方酰胺催化的对映选择性狄尔斯-阿尔德反应，以高立体控制度获得1-酰胺基-3,4-顺式二取代环己-1-烯。观察到的立体发散性可通过协同与分步两种不同的环加成路径予以合理解释。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract In contrast to ynamides, whose chemistry has been extensively explored, ynimines remain underutilized in organic synthesis despite their rich functionalities. Here we report a general strategy to access 2-imido-1,3-dienes, synthetically challenging building blocks, through the reaction of ynimines with carboxylic acids. Leveraging this transformation, we develop a three-component reaction of ynimines, carboxylic acids and electron-deficient alkenes that enables the efficient synthesis of 1-imido-3,4- trans -disubstituted cyclohex-1-enes. The sequence proceeds via regioselective hydroacyloxylation and Mumm rearrangement to generate 2-imido-1,3-dienes, which undergo Diels–Alder cycloadditions. An intramolecular variant furnishes trans -fused tricyclic architectures reminiscent of trans -Δ⁹-tetrahydrocannabinol. Chemoselective hydrolysis further converts 2-imido-1,3-dienes into 2-amido-1,3-dienes, enabling chiral squaramide-catalysed enantioselective Diels–Alder reactions to afford 1-amido-3,4- cis -disubstituted cyclohex-1-enes with high stereocontrol. Distinct concerted and stepwise cycloaddition pathways rationalize the observed stereodivergence.

</details>
<br>

**关键词**: ynimines, 2-imido-1,3-dienes, Diels-Alder reactions, stereodivergent synthesis, hydroacyloxylation, Mumm rearrangement, enantioselective catalysis, cyclohex-1-enes

---

### 22. ❌ Illuminating cell states by a comprehensive and interpretable single cell foundation model

**作者**: Jue Wang, Cheng Tan, Zhangyang Gao, Sida Shao, Shiping Liu, Stan. Z. Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70071-5](https://doi.org/10.1038/s41467-026-70071-5)

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

**评分理由**: 论文标题和摘要表明该研究专注于单细胞RNA测序数据分析，开发了一个名为scFoundation的综合性可解释单细胞基础模型，用于细胞状态识别和基因调控网络推断。研究领域属于生物信息学和计算生物学，而非医学影像分析。所有评分关键词均针对医学影像分析、分割、诊断、预后、手术规划等临床决策支持应用，与论文的单细胞转录组学主题完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work introduces CellVQ, a truly applicable and generalizable AI tool for the cell biology community that outperforms strong baselines in all downstream tasks, and also uncovered intriguing biological phenomena with compelling explanations.

!!! tip deepseek-chat TL;DR

    该研究开发了一个名为scFoundation的综合性可解释单细胞基础模型，用于从单细胞RNA测序数据中识别细胞状态并推断基因调控网络，从而揭示细胞异质性和功能。

**关键词**: single cell foundation model, scFoundation, single cell RNA sequencing, cell state identification, gene regulatory network inference, interpretable AI, comprehensive model, transcriptomics

---

### 23. ❌ BMP–Smad1/9 signaling plays a critical role in regulating zebrafish PGC proliferation

**作者**: Tao Zheng, Yaqi Li, Guangyuan Li, Zihang Wei, Jie Li, Zheng Jiang, Roshan Shah, Weiying Zhang, Cencan Xing, Anming Meng, Xiaotong Wu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70624-8](https://doi.org/10.1038/s41467-026-70624-8)

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

**评分理由**: 论文研究的是斑马鱼原始生殖细胞增殖的分子信号通路（BMP–Smad1/9），属于发育生物学和分子遗传学领域，与医学影像分析、人工智能、临床决策支持等关键词完全无关。论文未涉及任何医学影像技术、AI模型、疾病诊断、手术规划或多模态数据融合等内容。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that BMP-Smad1/9 signaling plays a critical role in zebrafish primordial germ cell (PGC) maintenance rather than fate determination, and conserved but functionally distinct roles of BMP signaling in vertebrate PGC development are underscore.

!!! tip deepseek-chat TL;DR

    该研究揭示了BMP–Smad1/9信号通路在调控斑马鱼原始生殖细胞增殖中的关键作用。

**关键词**: BMP signaling, Smad1/9, zebrafish, primordial germ cells, PGC proliferation, developmental biology, molecular pathway

---

### 24. ❌ Bridging the latency gap with a continuous stream evaluation framework in event-driven perception

**作者**: Jie Chu, Runze Zhang, Chu Yang, Zongyou Yu, Zongtao Bu, Haotian Liu, Florian Röhrbein, Alois Knoll, Gang Chen, Chao Jiang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70240-6](https://doi.org/10.1038/s41467-026-70240-6)

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

**评分理由**: 论文研究的是神经形态视觉系统的事件驱动感知评估框架，专注于解决异步事件流处理中的延迟问题，并提出了STARE评估框架和ESOT500数据集。所有评分关键词均涉及医学影像分析、诊断、手术规划等医疗AI应用领域，而该论文的研究领域是计算机视觉中的神经形态视觉和事件相机，与医学影像完全无关。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work introduces the STream-based lAtency-awaRe Evaluation (STARE) framework, and introduces two model enhancement strategies: Asynchronous Tracking, a fast-slow architecture that boosts model throughput, and Context-Aware Sampling, which dynamically adapts input to handle low event density cases.

!!! tip deepseek-chat TL;DR

    该论文针对神经形态视觉系统中事件驱动感知的评估存在延迟差距问题，提出了STARE延迟感知评估框架和ESOT500数据集，实验表明延迟会使在线准确率降低50%以上，并通过异步跟踪和上下文感知采样策略提升了模型性能。

<details open>
<summary>摘要翻译</summary>

> 神经形态视觉系统处理连续事件流，并为实时应用提供变革性潜力。然而，其评估方法仍受限于传统RGB成像的评估范式。现有方法将异步事件流转换为同步帧并忽略感知延迟，导致基准测试与实际性能之间存在关键差距。为解决这一问题，我们提出了基于流处理的延迟感知评估（STARE）框架。STARE整合了两个核心组件：连续采样（Continuous Sampling），通过最大化模型吞吐量以减少延迟影响；以及延迟感知评估（Latency-Aware Evaluation），量化延迟导致的在线精度损失。为严格验证STARE，我们构建了ESOT500数据集，这是一个包含500赫兹标注的高动态目标跟踪数据集。实验表明，延迟会使在线精度严重下降超过50%。我们进一步提出了两种模型增强策略：异步跟踪（Asynchronous Tracking），一种通过快慢架构提升模型吞吐量的方法；以及上下文感知采样（Context-Aware Sampling），可动态调整输入以应对事件密度较低的情况。总体而言，我们的工作弥合了模型理论潜力与实际部署之间的延迟鸿沟。在神经形态视觉领域，基于帧的基准测试会显著高估系统性能。本文提出的延迟感知评估框架，有效缩小了仿真与真实场景间的差距。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Neuromorphic vision systems process continuous event streams and offer transformative potential for real-time applications. However, their evaluation remains tethered to methodologies from RGB imaging. These approaches convert asynchronous event streams into synchronized frames and ignore perception latency, creating a critical gap between benchmarks and real-world performance. To address this, we introduce the STream-based lAtency-awaRe Evaluation (STARE) framework. STARE integrates two core components: Continuous Sampling, maximizing model throughput to reduce the impact of latency, and Latency-Aware Evaluation, quantifying latency-induced online accuracy. To rigorously validate STARE, we developed ESOT500, a high-dynamic object tracking dataset with 500 Hz annotations. Experiments reveal that latency severely degrades online accuracy by over 50%. We further introduce two model enhancement strategies: Asynchronous Tracking, a fast-slow architecture that boosts model throughput, and Context-Aware Sampling, which dynamically adapts input to handle low event density cases. Overall, our work bridges the latency gap between models’ theoretical potential and real-world deployment. In neuromorphic vision, frame-based benchmarks substantially overestimate performance. Here, the authors introduce latency-aware evaluation framework, bridging the sim-to-real gap.

</details>
<br>

**关键词**: neuromorphic vision, event-driven perception, latency-aware evaluation, STARE framework, ESOT500 dataset, asynchronous tracking, continuous event streams, online accuracy

---

### 25. ❌ Semantic similarity across languages reflects neurocognitive dimensions shaped by climate

**作者**: Ze Fu, Yuxi Chu, Tangxiaoxue Zhang, Yong Li, Xiaosha Wang, Yan Bi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70608-8](https://doi.org/10.1038/s41467-026-70608-8)

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

**评分理由**: 论文研究语言语义与气候环境的关系，使用词嵌入和行为评级分析跨语言语义维度，完全不涉及医学影像分析、深度学习医疗影像、AI诊断、预后预测、手术规划、多模态医疗影像或医疗影像基础模型等主题。所有关键词与论文内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究探讨了跨语言语义相似性如何反映受气候环境塑造的神经认知维度，发现气候变量能解释语义变异，且右前颞叶活动模式与气候相关。

<details open>
<summary>摘要翻译</summary>

> 摘要：人类语言千差万别，但在其表达的基本语义表征层面却存在系统性的规律。这种共性与差异如何形成尚不明确，部分原因在于语义理论往往缺乏与神经认知约束之间的原理性关联。基于神经认知理论——该理论认为语义知识植根于生物显著性信息维度——我们探究了环境因素如何塑造语言中的概念表征。本文研究表明，不同语言中的词汇意义沿着共享的神经认知维度组织，而沿这些维度的系统性变异与气候因素相关。通过分析53种语言的词嵌入模型以及8种语言使用者的行为评分数据，我们发现一致证据表明：气候变量能够解释超越常见社会文化因素的语义变异。补充性的探索性脑数据进一步提示，右前颞叶的活动模式受到气候相关的调节。这些发现共同表明，语言中的语义表征反映了以生物基础为依托的维度，这些维度在长期环境条件的影响下被灵活塑造。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Human languages differ widely, yet they share systematic regularities in the underlying semantic representations being expressed. How such similarities and differences arise remains unclear, in part because semantic theories often lack a principled link to neurocognitive constraints. Drawing on neurocognitive accounts in which semantic knowledge is grounded in biologically salient information dimensions, we examine how environmental factors shape conceptual representations in language. Here we show that word meanings across languages are organized along shared neurocognitive dimensions, while systematic variation along these dimensions is associated with climate. Using word embeddings from 53 languages and behavioral ratings from speakers of 8 languages, we find converging evidence that climatic variables explain semantic variation beyond commonly considered sociocultural factors. Complementary exploratory brain data further suggest climate-related modulation of activity patterns in the right anterior temporal lobe. Together, these findings indicate that semantic representations in language reflect biologically grounded dimensions that are flexibly shaped by long-term environmental conditions.

</details>
<br>

**关键词**: semantic similarity, cross-linguistic analysis, neurocognitive dimensions, climate effects, word embeddings, anterior temporal lobe, conceptual representations

---

### 26. ❌ Identification of cis-regulatory elements provides insights into tissue-specific gene regulation in the sheep genome

**作者**: Shangqian Xie, Kimberly M Davenport, Mazdak Salavati, Alex Caulton, Emily L. Clark, Alan Archibald, Shannon Clarke, Rüdiger Bräuning, Alisha T. Massa, Michelle R. Mousel, Stephen N. White, Kim Worley, Gordon K. Murdoch, Gabrielle M. Becker, Morgan R. Stegmiller, Sarem F. Khilji, Katie A Shira, Temitayo Olagunju, Tracy Hadfield, Stephanie McKay
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70382-7](https://doi.org/10.1038/s41467-026-70382-7)

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

**评分理由**: 论文研究的是绵羊基因组中顺式调控元件的注释和功能分析，使用多组学数据（ChIP-seq、ATAC-seq、CAGE-seq、RRBS、WGBS、RNA-seq）来识别增强子和启动子，并分析组织特异性基因调控机制。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划等临床决策支持领域，而该论文属于基因组学、生物信息学和动物遗传学研究范畴，与医学影像或临床AI应用完全无关。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Comparative analysis of enhancer-promoter combinations in human, mouse, pig, cattle, and sheep reveals ruminant-specific pathways, including pentose catabolism and long-chain fatty acid import regulation.

!!! tip deepseek-chat TL;DR

    该研究通过多组学方法系统注释了绵羊基因组中的顺式调控元件，揭示了组织特异性基因调控机制，并发现了与乳脂产量和出生体重相关的调控位点。

<details open>
<summary>摘要翻译</summary>

> 调控元件的注释对于理解基因调控机制至关重要，尤其是在人类和动物组织特异性调控方面。本研究利用ChIP-seq、ATAC-seq、CAGE-seq、RRBS、WGBS和RNA-seq技术，对一只成年母羊的24种组织进行了分析，共鉴定了274,682个增强子和25,975个启动子。我们在脑组织中发现了七个拥有超过10个增强子的神经发育相关基因，凸显了组织特异性调控的作用。顺式调控增强子-启动子组合的分析揭示了组织特异性增强子，例如小脑特异性增强子（chr15: 57390520-57390685）调控着在小脑和大脑皮层均有表达的BDNF基因。通过对人、小鼠、猪、牛和羊的增强子-启动子组合进行比较分析，我们发现了反刍动物特有的调控通路，包括戊糖分解代谢和长链脂肪酸输入调控。在一个增强子内鉴定出的一个乳脂产量数量性状位点（QTL）与脂肪代谢相关基因COMMD1存在相互作用，而在一个小脑特异性增强子内检测到的与出生体重相关的QTL则调控着XKR4基因。本研究为探索顺式调控机制和组织特异性调控提供了坚实的框架，推进了绵羊参考基因组的功能注释。对家畜基因组中调控元件进行注释对于理解基因调控机制具有重要意义。本研究利用绵羊的多组学数据，绘制了绵羊基因组中的调控元件图谱。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Annotation of regulatory elements is essential for understanding mechanisms underlying gene regulation, particularly tissue-specific regulation in human and animals. Here, we characterize 274,682 enhancers and 25,975 promoters across 24 tissues from an adult female sheep using ChIP-seq, ATAC-seq, CAGE-seq, RRBS, WGBS, and RNA-seq. We identify seven neural development-related genes with over 10 enhancers in brain tissues, highlighting the role of tissue-specific regulation. Cis-regulatory enhancer-promoter combinations provide insights into tissue-specific enhancers, such as the cerebellum-specific enhancer (chr15: 57390520-57390685) regulating BDNF, which is expressed in both the cerebellum and cerebral cortex. Comparative analysis of enhancer-promoter combinations in human, mouse, pig, cattle, and sheep reveals ruminant-specific pathways, including pentose catabolism and long-chain fatty acid import regulation. A milk fat yield quantitative trait locus (QTL) identified within an enhancer interacts with the fat metabolism-related gene COMMD1, and a birth weight-associated QTL detected within a cerebellum-specific enhancer regulates XKR4. This study provides a robust framework for exploring cis-regulatory mechanisms and tissue-specific regulation, advancing the functional annotation of the sheep reference genome. Annotating regulatory elements in domestic animal genomes is important to understand the mechanisms underlying gene regulation. Here, the authors use multi-omics data from sheep to map regulatory elements in the sheep genome.

</details>
<br>

**关键词**: cis-regulatory elements, tissue-specific gene regulation, sheep genome, enhancer-promoter combinations, multi-omics data, quantitative trait locus, functional annotation

---

### 27. ❌ Implantable soft bladder-machine interface for neurogenic bladder dysfunction

**作者**: Hanfei Li, Shuai Wang, Qianhengyuan Yu, Hang Zhao, Zhuochao Tang, LinChen Lv, Fei Han, Ruofan Yang, Yang Zhao, Zhuojia Fu, Benkang Shi, Guanglin Li, Changxian Wang, George Zhang, Kaikai Song, Yan Li, Zhiyuan Liu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70680-0](https://doi.org/10.1038/s41467-026-70680-0)

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

**评分理由**: 论文研究的是用于神经源性膀胱功能障碍的植入式软膀胱-机器接口（BdMI），属于生物电子学、柔性电子和神经调控领域。论文核心是开发一种可拉伸的导电薄膜设备，用于膀胱压力检测、肌电监测和电刺激治疗。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态成像和基础模型，这些主题在论文中完全没有涉及。论文未使用任何医学影像技术或AI模型进行分析、诊断或预测，也未涉及手术规划或多模态数据融合。因此，所有关键词的相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An implantable soft bladder-machine interface (BdMI) that integrates seamlessly with the bladder, providing monitoring and electrical stimulation, and validate the potential of BdMI in offering real-time, physiological feedback and electrical stimulation-based regulation for neurogenic bladder pathologies, marking a significant advancement in the field.

!!! tip deepseek-chat TL;DR

    该论文针对神经源性膀胱功能障碍，开发了一种可植入的软膀胱-机器接口，实现了膀胱压力检测、肌电监测和电刺激治疗，并在大鼠模型中验证了其有效性和稳定性。

<details open>
<summary>摘要翻译</summary>

> 神经源性膀胱功能障碍会损害膀胱感觉与收缩功能，并引发严重肾脏并发症。膀胱的大幅度各向同性扩张特性阻碍了用于监测与电刺激的可植入式生物电子器件的开发。针对这一问题，本研究报道了一种可与膀胱无缝集成的可植入软质膀胱-机器接口（BdMI），该接口具备监测与电刺激双重功能。该BdMI采用一种导电薄膜，能在无需对其弹性基底进行复杂预拉伸的情况下，承受高达800%的各向同性拉伸并保持功能稳定。我们阐明了其拉伸机制，并在大鼠模型中验证了BdMI可实现膀胱内压同步检测、逼尿肌肌电监测及电刺激治疗。植入7天后，BdMI仍能高效工作，并在电刺激后显著降低非自主膀胱收缩频率。这些发现证实了BdMI在神经源性膀胱病理治疗中提供实时生理反馈及基于电刺激调控的潜力，标志着该领域的重要进展。神经源性膀胱功能障碍损害膀胱感觉与收缩功能。本研究报道了一种可与膀胱集成的可植入软质膀胱-机器接口，该接口具备监测与电刺激功能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Neurogenic bladder dysfunction impairs bladder sensation and contraction, causing severe renal complications. The bladder’s large isotropic expansion hinders the development of implantable bioelectronic devices for monitoring and electrical stimulation. Addressing this, we report an implantable soft bladder-machine interface (BdMI) that integrates seamlessly with the bladder, providing monitoring and electrical stimulation. This BdMI features a conductive thin film capable of keeping functions under isotropic stretch up to 800%, created without the complex pre-stretching of its elastic substrate. We elucidate its stretchability mechanism and validate the BdMI in rat models, which enables simultaneous intravesical pressure detection, detrusor electromyographic monitoring, and electrical stimulation therapy. Implanted for 7 days, the BdMI operates efficiently and markedly reduces involuntary bladder contraction frequency post-stimulation. These findings validate the potential of BdMI in offering real-time, physiological feedback and electrical stimulation-based regulation for neurogenic bladder pathologies, marking a significant advancement in the field. Neurogenic bladder dysfunction impairs bladder sensation and contraction. Here, the authors report an implantable soft bladder-machine interface that integrates with the bladder providing monitoring and electrical stimulation.

</details>
<br>

**关键词**: implantable bladder-machine interface, neurogenic bladder dysfunction, conductive thin film, isotropic stretch, intravesical pressure detection, detrusor electromyographic monitoring, electrical stimulation therapy, soft bioelectronic device

---

### 28. ❌ Condensin accelerates long-range intra-chromosomal interactions

**作者**: Fan Zou, Yi Li, Timothy Földes, Henrik Dahl Pinholt, C. Smith, Leonid Mirny, Lu Bai
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70538-5](https://doi.org/10.1038/s41467-026-70538-5)

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

**评分理由**: 论文研究染色体3D组织、染色质动力学和凝聚素介导的环挤压，属于分子生物学和基因组学领域，与医学影像分析、人工智能临床决策支持等关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A novel role for condensin is uncovered in shaping the interphase genome organization and new insights into chromosomal search dynamics in vivo are provided.

!!! tip deepseek-chat TL;DR

    该研究揭示了凝聚素通过环挤压机制加速染色体长程相互作用，从而塑造间期基因组组织。

<details open>
<summary>摘要翻译</summary>

> 三维基因组结构在调控染色体位点间相互作用中起着关键作用。尽管基于染色体构象捕获（3C）的技术已提供染色质结构的静态快照，但活细胞中染色体接触的动力学特征仍不清楚。本研究采用化学诱导染色体相互作用（CICI）技术，测量了G1期停滞芽殖酵母中多个位点对的接触时间。结果表明，染色体运动高度符合Rouse聚合物模型，所有测试位点均表现出相似的扩散参数。出乎意料的是，在相似三维距离下，染色体内长程接触的发生速度显著快于染色体间接触。通过靶向耗竭实验，我们发现凝聚素（而非黏连蛋白）是介导这些快速染色体内相互作用的主要复合物。Hi-C分析进一步支持这一结论，显示凝聚素在G1期酵母中促进长距离染色体内相互作用。通过聚合物模拟，我们估算凝聚素以约2 kb/s的速度挤压染色质，其作用密度为每1-2 Mb一个复合物，持续合成能力为120-220 kb。这些发现揭示了凝聚素在塑造间期基因组结构中的新功能，并为体内染色体搜索动力学提供了新见解。细胞中长程染色体接触难以量化。本研究通过在酵母中诱导人工接触，证明在G1期酵母中凝聚素介导的环挤压驱动染色体内相互作用比染色体间相互作用形成更快。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The 3D genome organization plays a key role in regulating interactions among chromosomal loci. While Chromosome Conformation Capture (3C)-based methods have provided static snapshots of chromatin architecture, the kinetics of chromosomal encounters in live cells remain poorly characterized. In this study, we employ Chemically Induced Chromosomal Interaction (CICI) to measure encounter times between multiple loci pairs in G1-arrested budding yeast. Our results show that chromosome motion closely follows the Rouse polymer model, with similar diffusion parameters at all tested loci. Surprisingly, we find that long-range intra-chromosomal encounters occur significantly faster than inter-chromosomal encounters at similar 3D distances. Using targeted depletion experiments, we identify condensin, but not cohesin, as the complex mostly responsible for these rapid intra-chromosomal interactions. This is further supported by Hi-C analysis, which reveals that condensin promotes long-distance intra-chromosomal interactions in G1 yeast. Through polymer simulations, we estimate that condensin extrudes chromatin at ~2 kb/s with a density of one complex per 1-2 Mb and a processivity of 120-220 kb. These findings uncover a novel role for condensin in shaping the interphase genome organization and provide new insights into chromosomal search dynamics in vivo. Long‑range chromosome encounters in cells are hard to quantify. Here, the authors induce artificial contacts in yeast and show that intra‑chromosomal interactions form faster than inter‑chromosomal ones in G1 yeast, driven by condensin‑mediated loop extrusion.

</details>
<br>

**关键词**: 3D genome organization, chromosome conformation, condensin, loop extrusion, intra-chromosomal interactions, polymer model, yeast, Hi-C analysis

---

### 29. ❌ DRP1 induces neuroinflammation via transcriptional regulation of NF-ĸB.

**作者**: Yanhao Lai, Rebecca Z. Fan, Harry Brown, Said S. Salehe, Ethan Kim Tieu, Kim Tieu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70780-x](https://doi.org/10.1038/s41467-026-70780-x)

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

**评分理由**: 论文研究DRP1蛋白通过NF-κB通路调控神经炎症的分子机制，属于基础医学/神经科学领域，完全不涉及医学影像分析、深度学习、AI诊断、手术规划或任何医学影像相关技术。所有评分关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This study identifies a previously unrecognized function of DRP1 in mediating neuroinflammation via the NF-κB-lipocalin-2 axis and highlights DRP1-mediated pathways as potential therapeutic targets for neurodegenerative and other inflammation-related diseases.

!!! tip deepseek-chat TL;DR

    该研究发现线粒体分裂蛋白DRP1可作为转录因子激活NF-κB通路促进神经炎症，揭示了DRP1在神经退行性疾病中的新功能。

<details open>
<summary>摘要翻译</summary>

> 摘要：神经炎症是神经退行性疾病的主要致病机制。理解神经炎症的调控方式对于治疗开发至关重要。本文报道，动力相关蛋白1（dynamin-related protein 1, DRP1）——一个因其在线粒体分裂中的作用而广为人知的蛋白——同时也发挥着转录因子的功能，调控神经炎症。通过使用多种炎症模型，我们证明，在促炎性脂多糖（lipopolysaccharides, LPS）的刺激下，DRP1从细胞质转位至细胞核，并在核内结合Rela基因（编码NF-κB p65）的启动子区域，从而激活其基因产物及其他下游炎症细胞因子。我们的数据进一步揭示了促炎性脂质运载蛋白-2（lipocalin-2）在大脑中的重要作用。综上所述，本研究发现了DRP1通过NF-κB–lipocalin-2轴介导神经炎症的一个先前未被认识的功能，并强调了DRP1介导的通路可作为神经退行性疾病及其他炎症相关疾病的潜在治疗靶点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Neuroinflammation is a major pathogenic mechanism underlying neurodegenerative diseases. Understanding how neuroinflammation is regulated is critical to therapeutic development. Here, we report that dynaminrelated protein 1 (DRP1), well-recognized for its role in mitochondrial fission, also functions as a transcription factor that regulates neuroinflammation. Using multiple inflammatory models, we demonstrate that upon stimulation with pro-inflammatory lipopolysaccharides (LPS), DRP1 translocates from the cytosol to the nucleus, where it binds to the promoter region of Rela (encoding NF-κB p65) to activate its gene products and other downstream inflammatory cytokines. Our data further reveal a significant role of the proinflammatory lipocalin-2 in the brain. In combination, this study identifies a previously unrecognized function of DRP1 in mediating neuroinflammation via the NF-κB-lipocalin-2 axis and highlights DRP1-mediated pathways as potential therapeutic targets for neurodegenerative and other inflammation-related diseases.

</details>
<br>

**关键词**: DRP1, neuroinflammation, NF-κB, transcriptional regulation, neurodegenerative diseases, lipocalin-2, mitochondrial fission, inflammatory cytokines

---

### 30. ❌ Author Correction: Organocatalytic enantioselective [2π + 2σ] cycloaddition reactions of bicyclo[1.1.0]butanes with α,β-unsaturated aldehydes

**作者**: Yi-Xiang Geng, Tengfei Xiao, Dong Xie, Ming-Ming Li, Panpan Zhou, Guo-Qiang Xu, Ping Xu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-69148-y](https://doi.org/10.1038/s41467-026-69148-y)

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

**评分理由**: 论文标题和摘要显示该研究是关于有机催化不对称[2π+2σ]环加成反应的化学研究，涉及双环[1.1.0]丁烷与α,β-不饱和醛的反应。所有评分关键词均属于医学影像分析和人工智能临床决策支持领域，而该论文属于有机化学合成领域，两者在研究对象、方法、应用上完全不同，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了有机催化下双环[1.1.0]丁烷与α,β-不饱和醛的不对称[2π+2σ]环加成反应，实现了高对映选择性的环丁烷衍生物合成。

**关键词**: organocatalysis, enantioselective, [2π+2σ] cycloaddition, bicyclo[1.1.0]butanes, α,β-unsaturated aldehydes, cyclobutane derivatives, asymmetric synthesis

---

### 31. ❌ Single-cell multi-omic analysis of mitochondrial mutational mosaicism and dynamics

**作者**: Yu-Hsin Hsieh, Pauline Kautz, Lena Nitsch, Ambre Giguelay, Janet Liebold, Veronika Dimitrova, Stephania Contreras Castillo, Freya Jungen, Gábor Zsurka, Genevieve Trombly, Markus Schuelke, Wolfram S. Kunz, Caleb A. Lareau, Leif S. Ludwig
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70399-y](https://doi.org/10.1038/s41467-026-70399-y)

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

**评分理由**: 论文研究的是线粒体DNA突变在单细胞水平上的分析，使用单细胞测序技术（如ATAC-seq）和细胞系模型，开发了scmtMPM和scwMSS两个指标来量化突变负荷和异质性。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等方向，而本文完全不涉及任何医学影像处理、图像分割、深度学习模型或临床决策支持系统。论文属于单细胞基因组学、线粒体遗传学和分子生物学领域，与医学影像分析无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that individual POLGD274A cells exhibit complex mutational landscapes, with pathogenic mutations and truncating variants only present at subthreshold levels, indicative of their negative selection.

!!! tip deepseek-chat TL;DR

    该研究开发了单细胞线粒体DNA突变分析指标（scmtMPM和scwMSS），揭示了健康人和线粒体病患者在单细胞水平上线粒体DNA突变景观的异质性和约束模式。

<details open>
<summary>摘要翻译</summary>

> 线粒体DNA（mtDNA）突变的发生频率高于核基因突变，并与多种疾病相关。尽管单细胞测序技术能够分析mtDNA变异异质性，但对单个细胞内mtDNA突变全景的整体认识仍存在局限。本研究利用线粒体单细胞ATAC-seq技术和mtDNA高突变的POLG D274A敲入HEK293细胞系，引入两项指标——单细胞每百万碱基mtDNA突变数（scmtMPM）与异质性加权线粒体局部约束评分（scwMSS），以量化细胞突变负荷与体细胞嵌合现象。我们证明单个POLG D274A细胞呈现复杂的突变图谱，其中致病性突变与截短变异仅存在于亚阈值水平，暗示其受到负向选择。在人类健康供体与线粒体病患者中，我们识别出复合物I中的约束性突变，揭示了单细胞水平上先前未被认识的mtDNA突变景观异质性。总体而言，scmtMPM与scwMSS为探究线粒体遗传学、疾病机制及体细胞嵌合现象的基本特性提供了研究框架。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Mitochondrial DNA (mtDNA) mutations occur more frequently than nuclear mutations and are associated with various diseases. While single-cell sequencing enables mtDNA variant heteroplasmy analysis, a holistic view of mtDNA mutational landscapes in individual cells has remained limited. Here, we leverage mitochondrial single-cell ATAC-seq and mtDNA-hypermutated POLG D274A knock-in HEK293 cell lines to introduce two metrics—single-cell mtDNA mutations per million base pairs (scmtMPM) and heteroplasmy-weighted mitochondrial local constraint scores (scwMSS)—to capture cellular mutational loads and somatic mosaicism. We demonstrate that individual POLG D274A cells exhibit complex mutational landscapes, with pathogenic mutations and truncating variants only present at subthreshold levels, indicative of their negative selection. In human healthy donors and mitochondriopathy patients, we identify constrained mutations in complex I, highlighting previously unrecognized mtDNA mutational landscape heterogeneity present on the single-cell level. Overall, scmtMPM and scwMSS provide a framework to investigate fundamental properties of mitochondrial genetics, disease, and somatic mosaicism.

</details>
<br>

**关键词**: mitochondrial DNA mutations, single-cell sequencing, heteroplasmy, somatic mosaicism, POLG D274A, scmtMPM, scwMSS, mitochondriopathy

---

### 32. ❌ Climate response to Nature Future scenarios in a regional Earth System Model

**作者**: Petra Sieber, Dirk Nikolaus Karger, Nikki Zimmerman, Sara Si-Moussi, Wilfried Thuiller, Gabriele Midolo, Milan Chytrý, Irena Axmanová, Jonas Schwaab, Édouard L. Davin, Matthieu Leclair, Stephan Kambach, Helge Bruelheide, Thomas Hickler, Zvjezdana Stančić, Idoia Biurrun, Behlul Guler, Jürgen Dengler, Jan Divíšek, Peter H. Verburg
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70284-8](https://doi.org/10.1038/s41467-026-70284-8)

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

**评分理由**: 论文研究的是欧洲土地利用管理对区域气候的影响，使用地球系统模型和土地利用/栖息地/物种预测，属于气候科学、生态学和环境政策领域。所有评分关键词都涉及医学影像分析、人工智能医疗应用、疾病诊断/预后、手术规划等医学领域，与论文内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过地球系统模型评估欧洲基于自然保护政策的土地利用管理对区域气候的影响，发现基于文化关系价值观（Nature as Culture）的政策可能导致额外变暖和干旱，而基于内在价值观（Nature for Nature）或生态系统服务（Nature for Society）的政策则不会对气候适应和减缓构成重大挑战。

<details open>
<summary>摘要翻译</summary>

> 摘要：土地利用管理有助于应对人为引发的气候与生物多样性危机。然而，为实现自然保护、生态修复、可持续农业及森林覆盖等国际共识目标，土地系统需要进行实质性转型。此类转型会影响能量、水分和碳在陆地与大气间的交换，并可能通过改变地表反照率和蒸散作用，对局地至区域气候产生显著影响。本文探讨了在欧洲实施符合《昆明-蒙特利尔全球生物多样性框架》、自然未来框架及可持续低碳排放情景的土地利用管理，将如何影响本世纪中叶的欧洲气候。通过地球系统模型与详细的土地利用、栖息地及物种预测，我们发现：以关系价值（即“自然即文化”）为指导的政策实施可能导致额外的增温与干旱，进一步威胁生物多样性和人类福祉。相反，倡导内在价值（即“自然为本”）或生态系统服务价值（即“自然为社会”）则不会对气候适应与减缓构成重大挑战。这些差异结果凸显了构建综合性土地利用情景的必要性——此类情景应能协同提升生物多样性、稳定气候，并充分考虑陆地至大气的反馈机制，从而有助于权衡利弊并为欧洲政策实施提供科学依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Land use management can help address the human-induced climate and biodiversity crises. However, substantial transformations in land systems are needed to meet internationally agreed targets concerning nature conservation, restoration, sustainable agriculture, and tree cover. Such transformations influence land-atmosphere exchanges of energy, water, and carbon, and could have particularly strong effects on local to regional climate through changes in albedo and evapotranspiration. Here, we explore how land use management in Europe, consistent with the Kunming-Montreal Global Biodiversity Framework, the Nature Futures Framework, and a sustainable low-emissions scenario, would affect the European climate mid-century. Using Earth System Modelling and detailed land use, habitat, and species projections, we show that policy implementation guided by relational values (Nature as Culture) could lead to additional warming and drying further threatening biodiversity and human well-being. Conversely, promoting intrinsic values (Nature for Nature) or ecosystem services (Nature for Society) would not add major challenges for climate adaptation and mitigation. These different outcomes highlight the need to develop integrative land use scenarios that enhance biodiversity and stabilise the climate, while considering feedbacks from land to the atmosphere. Such scenarios could help navigate trade-offs and inform policy implementation in Europe.

</details>
<br>

**关键词**: land use management, climate change, Earth System Modelling, biodiversity, Nature Futures Framework, regional climate, land-atmosphere interactions, policy implementation

---

### 33. ❌ Coupled polarization dynamics and charge tunneling enable reconfigurable heterojunctions

**作者**: Ce Li, Tianze Yu, Zirui Zhang, Qingsong Deng, Fei Hui, Zhongrui Wang, Mario Lanza, Linfeng Sun
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70803-7](https://doi.org/10.1038/s41467-026-70803-7)

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

**评分理由**: 论文研究的是电子器件物理领域，具体涉及极化动力学、电荷隧穿和可重构异质结，与医学图像分析、人工智能临床决策支持等医疗领域完全无关。所有关键词均未在标题或摘要中出现，也没有任何间接关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了耦合极化动力学和电荷隧穿如何实现可重构异质结，并展示了其在电子器件中的应用潜力。

**关键词**: polarization dynamics, charge tunneling, reconfigurable heterojunctions, electronic devices, memristors, ferroelectric materials, tunneling junctions, device reconfiguration

---

### 34. ❌ Author Correction: Generalizable and scalable protein stability prediction with rewired protein generative models

**作者**: Ziang Li, Yunan Luo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70929-8](https://doi.org/10.1038/s41467-026-70929-8)

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

**评分理由**: 论文标题和摘要明确表明研究主题是蛋白质稳定性预测和蛋白质生成模型，属于计算生物学和蛋白质工程领域，与医学影像分析、临床决策支持、疾病诊断、手术规划等医疗AI主题完全无关。所有关键词均未在论文内容中涉及，因此相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种基于重连蛋白质生成模型的通用可扩展蛋白质稳定性预测方法，提高了预测性能。

**关键词**: protein stability prediction, generative models, rewired models, generalizable, scalable, protein engineering, computational biology

---

### 35. ❌ Observation of resonance of kagome flat band doublet

**作者**: Renjie Zhang, Bei Jiang, Xiangqi Liu, Heidi Tan, Xuefeng Zhang, Mojun Pan, Quanxin Hu, Yiwei Cheng, Chengnuo Meng, Yudong Hu, Yufan Zhao, R.Z. Wang, Dupeng Zhang, Junqin Li, Zhengtai Liu, Mao Ye, Ziqiang Wang, Yaobo Huang, G. Li, Y. F. Guo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70779-4](https://doi.org/10.1038/s41467-026-70779-4)

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

**评分理由**: 该论文研究的是凝聚态物理中的kagome晶格材料CsCr₆Sb₆，通过角分辨光电子能谱、输运测量和理论计算，观测到了平带共振现象及其与磁性的关联。所有评分关键词均属于医学影像分析和人工智能临床决策支持领域，而论文内容完全聚焦于量子材料的基础物理研究，两者之间没有任何交叉或关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究在kagome双层材料CsCr₆Sb₆中首次观测到了平带共振现象，并发现其与短程反铁磁关联的非常规耦合关系。

<details open>
<summary>摘要翻译</summary>

> 局域电子与巡游电子的相互作用是许多关联与拓扑量子态的基础。Kagome晶格因其同时具备平带（局域态）和色散带（巡游态）而提供了一个理想的研究平台，然而关于二者动力学耦合的直接谱学证据一直难以获得。本文报道了在准二维kagome双层材料CsCr₆Sb₆中观测到长期追寻的平带共振现象。通过角分辨光电子能谱、输运测量，以及结合密度泛函理论与动力学平均场理论的计算，我们确定了费米能附近共存的平带双重态和色散带。随着温度降低，平带与色散带均表现出显著的谱权重增强和杂化现象，直接证实了平带共振的存在。关键在于，这一现象的出现与短程反铁磁关联的起始同时发生，这与传统的近藤晶格行为形成鲜明对比。我们的发现不仅证实了kagome材料中长期探寻的平带共振，也揭示了其与磁性的非常规关联。平带共振是量子材料中平带态与色散带态相互作用的一个标志性特征。本文中，作者在kagome双层材料CsCr6Sb6中观测到了源于双层单元kagome带双重态的平带共振。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The interplay between local and itinerant electrons underpins many correlated and topological quantum states. Kagome lattices provide an ideal platform by hosting both flat (localized states) and dispersive bands (itinerant states), yet direct spectroscopic evidence of their dynamical coupling has remained elusive. Here we report the long-sought flat band resonance in the quasi-two-dimensional kagome bilayer material CsCr₆Sb₆. Using angle-resolved photoemission spectroscopy, transport measurements, and combined density functional theory and dynamical mean-field theory, we identify coexisting flat band doublets and dispersive bands near the Fermi energy. Upon cooling, the flat and dispersive bands exhibit a pronounced enhancement of spectral weight and hybridization, directly evidencing flat band resonance. Crucially, this emergence coincides with the onset of short-range antiferromagnetic correlations, contrasting sharply with conventional Kondo lattice behavior. Our findings demonstrate not only the long-sought flat band resonance in kagome materials, but also its unconventional correlation with magnetism. A hallmark of the interaction between flat band and dispersive band states in quantum materials is the flat band resonance. Here, the authors report the observation of a flat band resonance in the kagome bilayer material CsCr6Sb6 originating from the doublet kagome bands of the bilayer unit.

</details>
<br>

**关键词**: kagome lattice, flat band resonance, CsCr6Sb6, angle-resolved photoemission spectroscopy, antiferromagnetic correlations, quantum materials, bilayer material, spectral weight enhancement

---

### 36. ❌ Magnaporthe oryzae MoPh1 perceives ER stress and promotes adaptive responses via a plasma membrane-to-vacuole pathway

**作者**: Ziyi Yin, Jian Xu, Shijie Ma, Jiazong Liu, Tianfeng Zhao, Yan Li, Yi Wang, Chunyan Liu, Ziming Wang, Yanke Jiang, Haimiao Zhang, Chongchong Lu, Yingying Qin, Ziying Kong, Shi‐En Lu, Congming Lu, Yan Li, Xinhua Ding
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70610-0](https://doi.org/10.1038/s41467-026-70610-0)

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

**评分理由**: 论文研究的是真菌（Magnaporthe oryzae）中内质网应激感知和细胞适应性反应的分子机制，具体涉及质膜蛋白MoPh1通过ER-PM接触位点感知应激并激活自噬途径。所有评分关键词均围绕医学影像分析、人工智能辅助临床决策等医疗技术领域，而该论文属于基础分子生物学和细胞生物学研究，与医学影像、AI诊断、手术规划等临床应用完全无关。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A PM sensor, MoPh1, was observed to perceive stress through ER-PM contact sites and target the autophagosome and vacuole, consequently stimulating the autophagy process and supporting stress relief and might be highly important in both fungi and plants.

!!! tip deepseek-chat TL;DR

    该研究发现真菌中的质膜蛋白MoPh1通过内质网-质膜接触位点感知内质网应激，并激活一条独立的质膜-液泡途径来刺激自噬，从而帮助细胞缓解应激并促进适应性生存。

<details open>
<summary>摘要翻译</summary>

> 在生长与发育过程中，细胞会经历内外源胁迫，若应对不当可能产生有害影响。内质网（ER）胁迫是一种内源性胁迫，当蛋白质错误折叠或扰动速率过高时被诱发，此时从内质网到细胞核的常规响应通路会被激活以应对胁迫。然而，质膜（PM）系统参与响应此类内源胁迫的机制尚未得到充分研究。本研究发现，质膜传感器蛋白MoPh1可通过内质网-质膜接触位点感知胁迫，并靶向自噬体与液泡，从而激活自噬过程并协助缓解胁迫。由MoPh1介导的质膜-液泡通路独立于经典的内质网-细胞核通路，且可能在真菌与植物中均具有重要作用，因为它对减轻内质网胁迫、促进细胞适应性以维持生存至关重要。蛋白质错误折叠会激活内质网中的未折叠蛋白响应。本研究表明，在稻瘟病菌中，定位于质膜的MoPh1蛋白通过内质网-质膜接触位点感知胁迫，并刺激自噬以协助缓解胁迫。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> During growth and development, cells experience both internal and external stresses, which can exert harmful impacts if they are poorly managed. Endoplasmic reticulum (ER) stress is an internal stress that is induced when protein misfolding or perturbations occur at excess rates, and the conventional response pathways from the ER to the nucleus are activated to address the stress. However, the involvement of the plasma membrane (PM) system in response to this internal stress has been insufficiently investigated. Here, a PM sensor, MoPh1, was observed to perceive stress through ER-PM contact sites and target the autophagosome and vacuole, consequently stimulating the autophagy process and supporting stress relief. The PM-to-vacuole pathway mediated by MoPh1 is independent of the classical ER-to-nucleus pathway and might be highly important in both fungi and plants, as it plays a crucial role in alleviating ER stress and promoting cellular adaptation for cell survival. The unfolded protein response is activated at the ER due to protein misfolding. Here the authors show that in Magnaporthe oryzae, the plasma membrane localized MoPh1 protein perceives stress through ER-PM contact sites and stimulates autophagy to support stress relief.

</details>
<br>

**关键词**: Magnaporthe oryzae, ER stress, plasma membrane sensor, autophagy, ER-PM contact sites, cellular adaptation, MoPh1 protein, vacuole targeting

---

### 37. ❌ Dynamics of phage-host interactions in Bacteroides fragilis resolved by single-cell transcriptomics

**作者**: Anika Gupta, Norma M. Morella, Dmitry Sutormin, Naisi Li, Karl D. Gaisser, Alexander Robertson, Yaroslav Ispolatov, Georg Seelig, Neelendu Dey, A. S. Kuchina
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70381-8](https://doi.org/10.1038/s41467-026-70381-8)

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

**评分理由**: 论文标题和摘要表明该研究聚焦于细菌学（Bacteroides fragilis）的噬菌体-宿主相互作用，使用单细胞转录组学技术，属于微生物学/分子生物学领域。所有评分关键词均涉及医学影像分析、人工智能在医疗影像中的应用、疾病诊断/预后、手术规划等临床决策支持技术，与论文的生物学研究内容完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Bacterial single-cell RNA sequencing is established as a powerful platform for investigating the dynamics of host-phage interactions and revealing the roles of phase variation and stochasticity in bacterial defenses.

!!! tip deepseek-chat TL;DR

    该研究利用单细胞转录组学解析了脆弱拟杆菌中噬菌体与宿主相互作用的动态过程，揭示了感染期间基因表达的异质性变化。

**关键词**: phage-host interactions, Bacteroides fragilis, single-cell transcriptomics, gene expression dynamics, microbial infection, transcriptional heterogeneity, bacteriophage

---

### 38. ❌ Prediction of thermally driven quasi-1D superionic states in carbon hydride under giant planetary conditions

**作者**: Cong Liu, R. E. Cohen, Jian Sun
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70603-z](https://doi.org/10.1038/s41467-026-70603-z)

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

**评分理由**: 论文研究的是碳氢化合物在巨行星条件下的热驱动准一维超离子态预测，属于凝聚态物理、行星科学和材料科学领域，与医学图像分析、人工智能临床决策支持、深度学习医学成像、疾病诊断、预后预测、手术规划、多模态医学成像或医学成像基础模型完全无关。所有关键词均得0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了碳氢化合物在巨行星极端条件下的热驱动准一维超离子态预测问题，发现并预测了这些状态的存在及其特性。

**关键词**: carbon hydride, thermally driven, quasi-1D superionic states, giant planetary conditions, prediction, high-pressure physics, material properties, computational modeling

---

### 39. ❌ A model for drug transport across two membranes of Gram-negative bacteria by an MFS tripartite assembly

**作者**: Zhaojun Zhong, Tuerxunjiang Maimaiti, Matthew O. Jackson, Rui Dong, Xueyan Gao, Qing Ouyang, Wenqian Wang, Jinliang Guo, Shangrong Li, Wenyu Shang, Huajun Liu, Hongnian Jiang, Shuo Zhang, Ulrich Zachariae, Ben F. Luisi, Yanjie Chao, Dijun Du
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70500-5](https://doi.org/10.1038/s41467-026-70500-5)

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

**评分理由**: 论文研究的是革兰氏阴性细菌中MFS型三联外排泵（EmrAB-TolC）的结构与药物转运机制，属于结构生物学和微生物学领域，与医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像及基础模型等关键词完全无关。论文未涉及任何医学影像处理或临床决策支持相关内容。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The structural and functional data support a model for one-step drug transport by the MFS pump across the entire envelope of Gram-negative bacteria.

!!! tip deepseek-chat TL;DR

    该研究解析了革兰氏阴性细菌中MFS型三联外排泵EmrAB-TolC的高分辨率结构，揭示了其不对称组装机制和关键药物转运残基，提出了该泵一步跨膜转运药物的模型。

<details open>
<summary>摘要翻译</summary>

> 摘要：蛋白质与小分子跨细胞膜的转运对于细菌与环境相互作用及抵抗抗生素生存至关重要。在拥有双层膜的革阴性细菌中，底物跨越细胞被膜的转运通常需要通过间接的逐步过程，并由专门的大分子机器执行。主要易化子超家族（MFS）型三联外排泵利用质子电化学梯度在多种细菌中排出药物，但其组装结构与作用机制仍不明确。作为典型的MFS型三联外排泵，EmrAB-TolC通过质子耦合的EmrB（DHA2转运蛋白家族成员）介导对多种抗菌药物的耐药性。本研究报道了EmrAB-TolC泵的高分辨率（3.13 Å）结构，揭示了由TolC:EmrA:EmrB以3:6:1比例组装形成的独特不对称架构，以及对该泵组装至关重要的相互作用界面。通过突变实验和抗生素敏感性测定，我们鉴定并验证了参与药物转运的关键残基。这些结构与功能数据支持了MFS泵一步式跨越革阴性细菌完整被膜进行药物转运的作用模型。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Transport of proteins and small molecules across cellular membrane is crucial for bacterial interaction with the environment and survival against antibiotics. In Gram-negative bacteria that possess two layers of membranes, specialized macromolecular machines are required to transport substrates across the cell envelope, often via an indirect stepwise process. The major facilitator superfamily (MFS)-type tripartite efflux pumps use proton electrochemical gradient to extrude drugs in diverse bacterial species, but the architecture of the assembly and structural mechanisms remain elusive. A representative MFS-type tripartite efflux pump, EmrAB-TolC, mediates resistance to multiple antimicrobial drugs through proton-coupled EmrB, a member of the DHA2 transporter family. Here, we report the high-resolution (3.13 Å) structure of the EmrAB-TolC pump, revealing a distinct, asymmetric architecture emerging from the assembly of TolC:EmrA:EmrB with a ratio of 3:6:1 and contacts that are essential for the pump assembly. Key residues involved in drug transport are identified and corroborated by mutagenesis and antibiotic sensitivity assays. The structural and functional data support a model for one-step drug transport by the MFS pump across the entire envelope of Gram-negative bacteria.

</details>
<br>

**关键词**: Gram-negative bacteria, MFS tripartite efflux pump, EmrAB-TolC, drug transport, antibiotic resistance, structural biology, membrane protein, antimicrobial drugs

---

### 40. ❌ Publisher Correction: Dynamic realization of emergent high-dimensional optical vortices

**作者**: Dongha Kim, Geonhyeong Park, Yun-Seok Choi, Arthur Baucour, Jisung Hwang, Jaeyu Kim, Sanghyeok Park, Hyungdon Yun, Jonghwa Shin, Haiwen Wang, Shengli Fan, Dong Ki Yoon, Min-Kyo Seo
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-69478-x](https://doi.org/10.1038/s41467-026-69478-x)

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

**评分理由**: 论文标题和摘要（尽管摘要内容缺失）表明该研究聚焦于光学物理领域，具体涉及高维光学涡旋的动态实现。这与医学图像分析、人工智能临床决策支持等关键词完全无关，因为研究内容属于基础光学物理而非医疗应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究探索了高维光学涡旋的动态实现方法，属于光学物理领域，与医学图像分析无关。

**关键词**: optical vortices, dynamic realization, high-dimensional optics, publisher correction, optical physics

---

### 41. ❌ Bidirectional catalysts with dual-atom dynamic d-band centre modulation and support self-reconstruction for de/hydrogenation in MgH2/Mg

**作者**: Jinlong JIN, Jiyue Zhang, Jingjing Zhang, X. J. Chen, Heyi Qian, Bohua Jia, Jianxing Liu, Baoxin Han, W. Wang, Xiaojun Yan, Yigang Yan, Jianglan Shui, Jianmei Huang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70604-y](https://doi.org/10.1038/s41467-026-70604-y)

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

**评分理由**: 论文研究的是固态氢存储材料MgH2/Mg的催化改性，属于材料科学、化学工程和能源存储领域，与医学图像分析、人工智能临床决策支持等医学领域完全无关。论文内容涉及双原子催化剂设计、d带中心调控、金属-载体相互作用等材料化学概念，没有任何医学图像、诊断、手术规划或医疗AI相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了MgH2/Mg固态氢存储系统脱/加氢反应温度高、动力学缓慢的问题，通过设计Ni1Co1@TiO2双原子催化剂，实现了d带中心的双向调控和载体自重构，显著提高了反应动力学和循环稳定性。

<details open>
<summary>摘要翻译</summary>

> 采用MgH2的高容量固态储氢技术需要较高的脱/加氢温度且动力学性能迟缓。尽管MgH2的催化改性已被广泛研究，但现有催化剂主要侧重于单向优化，未能同时高效地优化MgH2/Mg体系的可逆储氢性能。本研究通过理性设计与构建异核双原子催化剂Ni1Co1@TiO2，在该体系中镍与钴双向调控d带中心，实现协同互补催化。具体而言，在脱氢过程中，镍作为Mg–H键断裂的主要活性位点，其活性通过钴诱导的d带中心下移得以增强；而在加氢过程中，钴则通过镍触发的d带中心上移成为H2解离的主要活性位点。同时，钛物种与氧空位的自重构效应，结合强金属-载体相互作用（Ni/Co–TiO2），加速了界面电子转移并抑制金属原子迁移。这种协同作用显著提升了反应动力学与循环稳定性，为大规模储氢应用展示了广阔前景。氢化镁虽储存丰富氢能，但其释氢与吸氢过程缓慢且需高温条件。负载于氧化钛上的镍-钴双原子催化剂通过调控电子结构，有效加速储氢动力学并提升循环稳定性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> High-capacity solid-state hydrogen storage using MgH2 requires high de/hydrogenation temperatures and exhibits sluggish kinetics. Although catalytic modification of MgH2 has been extensively studied, existing catalysts largely focus on unidirectional optimisation, failing to simultaneously and efficiently optimise the reversible hydrogen-storage properties of the MgH2/Mg system. Herein, we rationally design and construct a heteronuclear dual-atom catalyst, Ni1Co1@TiO2. In this system, Ni and Co bidirectionally modulate the d-band centres, enabling synergistic and complementary catalysis. Specifically, Ni serves as the primary active site for Mg–H bond cleavage during dehydrogenation, facilitated by Co-induced d-band centre downshift. Conversely, Co acts as the primary active site for H2 dissociation during hydrogenation via Ni-triggered d-band centre upshift. Simultaneously, self-reconstruction of titanium species and oxygen vacancies, coupled with strong metal-support interactions (Ni/Co–TiO2), accelerate interfacial electron transfer and inhibit metal atom migration. This synergy significantly enhances both reaction kinetics and cycling stability, showing great promise for large-scale hydrogen-storage applications. Magnesium hydride stores abundant hydrogen but releases and absorbs it too slowly and at high temperatures. A dual-atom Ni–Co catalyst on titanium oxide tunes its electronic structure, speeding hydrogen storage kinetics and improving cycling stability.

</details>
<br>

**关键词**: solid-state hydrogen storage, MgH2/Mg, dual-atom catalyst, d-band centre modulation, dehydrogenation/hydrogenation, reaction kinetics, cycling stability, metal-support interaction

---

### 42. ❌ Impact of NPAS2 on mPFC dopamine synthesis and nap behavior

**作者**: Lianxia Guo, Haobin Cen, Yuwei Huang, Zanjin Li, Kengran Zeng, Zicong Wu, Jiaxian Weng, Xiaocao Guo, Di He, Xinyu Liu, Zhehan Yang, Hui Xu, Tingying Hao, Binbin Wei, Xingxing Diao, Baojian Wu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70424-0](https://doi.org/10.1038/s41467-026-70424-0)

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

**评分理由**: 论文研究的是小鼠午睡行为的神经分子机制，聚焦于NPAS2基因通过POU2F2-TH通路调控mPFC多巴胺合成的昼夜节律机制。所有评分关键词均涉及医学影像分析、AI诊断、手术规划等临床决策支持技术，而该论文属于基础神经生物学研究，未涉及任何医学影像、AI模型或临床应用，因此所有关键词相关度均为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An endogenous circadian mechanism where mPFC NPAS2 periodically inhibits wake-promoting dopaminergic activity to drive nap behavior is established, providing fundamental insights into the neural and molecular regulation of nap biology.

!!! tip deepseek-chat TL;DR

    该研究揭示了小鼠午睡行为的神经机制，发现mPFC中NPAS2基因通过激活POU2F2抑制TH表达和多巴胺合成，从而周期性降低促觉醒神经活动以驱动午睡行为。

<details open>
<summary>摘要翻译</summary>

> 午间小睡作为一种普遍存在却未被充分理解的现象，其生物学基础一直不甚明确。本研究在核心生物钟调节因子中鉴定出NPAS2是小鼠午睡行为的性别非依赖性决定因子。具体而言，内侧前额叶皮层（medial prefrontal cortex, mPFC）表达的NPAS2通过对局部多巴胺能活性的昼夜节律性调控来协调午睡调节。我们证明mPFC中的酪氨酸羟化酶阳性（TH+）神经元具有随时间变化的促觉醒活性，并在午睡时段表现出最低程度的兴奋性。从机制上讲，NPAS2通过POU2F2-TH调控通路实现这种昼夜节律性抑制：1）转录激活转录抑制因子POU2F2；2）进而下调mPFC TH+神经元中TH（多巴胺合成的限速酶）的表达及多巴胺的产生。这些发现确立了一种内源性昼夜节律机制，即mPFC中的NPAS2周期性抑制促觉醒的多巴胺能活性以驱动午睡行为，为理解午睡生物学的神经与分子调控提供了基础性见解。午间小睡的生物学基础尚不清楚。本文作者发现，mPFC TH阳性神经元中的NPAS2通过激活POU2F2来抑制TH水平及多巴胺合成，从而降低促觉醒的神经活性并驱动午睡行为。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The biological basis of the afternoon nap, a widespread yet poorly understood phenomenon, has remained elusive. Here we identify NPAS2, among core circadian regulators, as a sex-independent determinant of the nap behavior in mice. Specifically, medial prefrontal cortex (mPFC)-expressed NPAS2 orchestrates nap regulation through circadian modulation of local dopaminergic activity. We demonstrate that tyrosine hydroxylase-positive (TH+) neurons in mPFC exhibit time-of-day dependent wake-promoting activity, showing minimal excitation precisely during nap hours. Mechanistically, NPAS2 achieves this circadian suppression through a POU2F2-TH regulatory pathway: 1) transcriptional activation of the transcription repressor POU2F2, and 2) consequent downregulation of TH expression (a rate-limiting enzyme for dopamine synthesis) and dopamine production in mPFC TH+ neurons. These findings establish an endogenous circadian mechanism where mPFC NPAS2 periodically inhibits wake-promoting dopaminergic activity to drive nap behavior, providing fundamental insights into the neural and molecular regulation of nap biology. The biological basis of afternoon nap remains unclear. Here, authors show that NPAS2 in mPFC TH-positive neurons activates POU2F2 to suppress TH level and dopamine production, thereby reducing wake-promoting neural activity and driving nap behavior.

</details>
<br>

**关键词**: NPAS2, nap behavior, mPFC, dopamine synthesis, circadian regulation, TH-positive neurons, POU2F2, wake-promoting activity

---

### 43. ❌ A dual-cathode zinc-ethylene glycol/air battery for concurrent electricity generation and plastic waste upcycling

**作者**: Nan Li, Mingzi Sun, Qilin Pan, ruxia zhang, Hang Lou, Wanbo Zhu, Chao Xie, Yi Yang, Bolong Huang, Weilu Zhang, Hao Jiang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70736-1](https://doi.org/10.1038/s41467-026-70736-1)

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

**评分理由**: 论文研究的是锌-乙二醇/空气双阴极电池技术，专注于电化学、能源存储和塑料废物升级回收，与医学图像分析、人工智能临床决策支持等医疗领域完全无关。所有关键词均涉及医疗影像和AI医疗应用，而论文内容属于能源/材料/环境工程领域，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了传统锌空气电池反应动力学慢和热力学不兼容的问题，通过开发双阴极锌-乙二醇/空气电池和PdCuCo三金属烯双功能催化剂，实现了高效发电（91.7%能量转换效率）与塑料废物电化学重整为高价值C2化学品的同步进行。

<details open>
<summary>摘要翻译</summary>

> 传统可充电锌空气电池面临两大关键挑战：(1) 氧还原反应与析氧反应动力学缓慢；(2) 单一空气阴极上ORR与OER反应的热力学不兼容性。为解决这些局限，本研究提出了一种双阴极锌-乙二醇/空气电池，其通过空间分离的设计将ORR与乙二醇氧化反应分别置于不同阴极，实现了同步发电与聚对苯二甲酸乙二醇酯塑料废料电重整转化为高价值C2化学品。此外，我们开发了一种由富含缺陷的亚纳米厚度PdCuCo三金属烯组成的双功能催化剂，以同时增强EGOR和ORR动力学。得益于解耦的阴极构型与双功能PdCuCo催化剂，该D-ZEAB表现出91.7%的能量转换效率、1696小时的长循环寿命以及>93%的乙醇酸法拉第效率。这项工作不仅为推进锌空气电池技术提供了有前景的策略，也为同步实现能量存储与塑料废料升级回收提供了一条可持续路径。传统可充电锌空气电池面临动力学缓慢和热力学不兼容的问题。本文作者提出了一种双阴极锌-乙二醇/空气电池，能够同时实现高效发电并将塑料废料电重整转化为高价值C2化学品。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Conventional rechargeable zinc-air batteries (ZABs) face two critical challenges: (1) slow kinetics of the oxygen reduction (ORR) and oxygen evolution (OER) reactions; and (2) the thermodynamic incompatibility of OER and ORR occurring concurrently on a single air cathode. To address these limitations, we propose in this study a dual-cathode zinc-ethylene glycol/air battery (D-ZEAB) that spatially decouples ORR and the ethylene glycol oxidation reaction (EGOR) onto separate cathodes, enabling concurrent electricity generation and electroreforming of polyethylene terephthalate (PET) plastic waste into high-value C2 chemicals. Furthermore, we develop a bifunctional catalyst composed of defect-rich subnanometer-thick PdCuCo trimetallenes to enhance both EGOR and ORR kinetics. Benefiting from the decoupled cathode configuration and the bifunctional PdCuCo catalyst, the D-ZEAB demonstrates an energy conversion efficiency of 91.7%, a long cycle life of 1696 h, and a Faradaic efficiency of >93% for GA production. This work not only presents a promising strategy for advancing the zinc-air battery technology but also offers a sustainable route for simultaneous energy storage and plastic waste upcycling. Conventional rechargeable zinc-air batteries face slow kinetics and thermodynamic incompatibility. Here, the authors propose a dual-cathode zinc-ethylene glycol/air battery, enabling concurrent efficient electricity generation and electro-reforming of plastic wastes into high-value C2 chemicals.

</details>
<br>

**关键词**: zinc-air battery, dual-cathode battery, plastic waste upcycling, ethylene glycol oxidation, PdCuCo trimetallenes, electroreforming, energy conversion efficiency, C2 chemicals

---

### 44. ❌ The impact of minimum energy performance standards on the commercial real estate market

**作者**: Piet Eichholtz, Nils Kok, Xudong Sun
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70684-w](https://doi.org/10.1038/s41467-026-70684-w)

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

**评分理由**: 论文研究商业房地产市场中的最低能源性能标准影响，属于房地产经济学和政策分析领域，与医疗图像分析、人工智能临床决策支持等医学研究主题完全无关。所有关键词均未在标题或摘要中提及，也无任何关联内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究分析了最低能源性能标准对商业房地产市场的影响，发现这些标准提高了能源效率认证建筑的价值和租金溢价。

**关键词**: minimum energy performance standards, commercial real estate, energy efficiency, building certification, rental premiums, property values, sustainability policy

---

### 45. ❌ Durvalumab and cediranib with and without olaparib in recurrent ovarian cancer: a phase II proof-of-concept study

**作者**: Junya Tabata, Tzu‐Ting Huang, Elena Giudice, Kristen R. Ibanez, Jayakumar R. Nair, A. Warner, B. Brooke Solarz, Valentina Bolanos, Bernadette Redd, Nahoko Sato, Shraddha Rastogi, Sunmin Lee, Roshan L. Shrestha, Alexander Y. Mitrophanov, S. Lipkowitz, K. C. Conlon, Chien Chu Huang, J. Jack Lee
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70785-6](https://doi.org/10.1038/s41467-026-70785-6)

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

**评分理由**: 该论文是一项关于复发性卵巢癌的II期概念验证临床试验，研究药物组合（durvalumab、olaparib、cediranib）的疗效和安全性。论文内容完全集中在临床试验设计、患者反应率、生存期、毒性管理和分子生物标志物分析上，没有涉及任何医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态成像或基础模型等主题。所有关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Findings support the proof-of-concept clinical activity of D’ + O’+ C and D’ + C and identify molecular signatures with potential predictive value in subsets of recurrent ovarian cancer and identify molecular signatures with potential predictive value in subsets of recurrent ovarian cancer.

!!! tip deepseek-chat TL;DR

    这项II期临床试验评估了durvalumab联合cediranib加或不加olaparib在复发性卵巢癌中的疗效，结果显示D+C方案达到了主要终点（ORR 29.6%），而D+O+C方案未达到（ORR 19.4%），两组的无进展生存期均为4.5个月，并发现了与临床获益相关的分子特征。

<details open>
<summary>摘要翻译</summary>

> 本研究报道了在一项单中心、多臂、非随机、多队列I/II期试验（NCT02484404）的复发性卵巢癌队列中，度伐利尤单抗（durvalumab）、奥拉帕利（olaparib）和西地尼布（cediranib）（D + O + C）联合方案，以及度伐利尤单抗联合西地尼布（D + C）方案的疗效与转化研究发现。共入组68例患者（D + O + C组39例，D + C组29例）。主要终点为客观缓解率（ORR）；次要终点包括无进展生存期（PFS）和安全性。D + O + C组的ORR为19.4%（95% CI，9.5-43.5），D + C组为29.6%（95% CI，13.8-46.9）；D + C组达到了主要终点，而D + O + C组未达到。两组中位PFS均为4.5个月，每组各有4例卓越应答者（PFS ≥ 12个月）。毒性可控。研究收集了治疗前和治疗中的活检组织与血液样本，用于预设的转录组学和免疫表型分析；特征分析和临床前研究为事后开展且具有探索性。来自卓越应答者和具有临床获益（部分缓解或疾病稳定且PFS ≥ 4个月）患者的基线肿瘤显示出免疫激活和代谢通路的富集，而无临床获益（NCB；疾病进展或疾病稳定但PFS < 4个月）的肿瘤则表现出血管适应和细胞骨架重塑通路的上调。这些发现支持了D + O + C和D + C方案的概念验证性临床活性，并识别出在复发性卵巢癌亚群中具有潜在预测价值的分子特征。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Here we report the efficacy and translational findings of durvalumab, olaparib, and cediranib (D + O + C) and of durvalumab plus cediranib (D + C) from the recurrent ovarian cancer cohort within a single-center, multi-arm, non-randomized, multi-cohort phase I/II trial (NCT02484404). Sixty-eight patients were enrolled (39 in D + O + C, 29 in D + C). The primary endpoint was objective response rate (ORR); secondary endpoints included progression-free survival (PFS) and safety. ORR was 19.4% (95% CI, 9.5-43.5) for D + O + C and 29.6% (95% CI, 13.8-46.9) for D + C; D + C met the primary endpoint while D + O + C did not. Median PFS was 4.5 months in both arms, with four exceptional responders (PFS ≥ 12 months) per arm. Toxicity was manageable. Pre- and on-treatment biopsies and blood samples were collected for prespecified transcriptomic and immunophenotypic profiling; signature analyses and preclinical studies were conducted post hoc and were exploratory. Baseline tumors from exceptional responders and patients with clinical benefit (partial response or stable disease with PFS ≥ 4 months) demonstrated enrichment of immune activation and metabolic pathways, whereas tumors with no clinical benefit (NCB; progressive disease or stable disease with PFS &lt; 4 months) exhibited upregulation of vascular adaptation and cytoskeletal remodeling pathways. These findings support the proof-of-concept clinical activity of D + O + C and D + C and identify molecular signatures with potential predictive value in subsets of recurrent ovarian cancer.

</details>
<br>

**关键词**: recurrent ovarian cancer, phase II trial, durvalumab, cediranib, olaparib, objective response rate, progression-free survival, molecular signatures

---

### 46. ❌ Resonant and non-resonant driving of linearly-polarized excitons in Cd3P2 magic-size clusters

**作者**: Yuan Liu, Yuxuan Li, Yupeng Yang, Jingyi Zhu, Kaifeng Wu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70674-y](https://doi.org/10.1038/s41467-026-70674-y)

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

**评分理由**: 论文研究Cd3P2魔法尺寸团簇中线性极化激子的共振和非共振驱动，属于凝聚态物理、纳米材料和光学领域，与医学影像分析、人工智能临床决策支持、疾病诊断、手术规划等医疗应用完全无关。所有关键词均未在标题或摘要中出现，也无任何间接关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究探讨了Cd3P2魔法尺寸团簇中线性极化激子在共振和非共振光驱动下的行为，揭示了其光学性质和量子限制效应。

**关键词**: Cd3P2, magic-size clusters, linearly-polarized excitons, resonant driving, non-resonant driving, optical properties, quantum confinement

---

### 47. ❌ Large megathrust earthquakes in cold mantle wedge corners under lawsonite blueschist facies

**作者**: Hao Zhang, Sylvain Barbot, zekang Yang, Mingqi Liu, L. X. Zhang, John Paul Platt
**期刊/来源**: nature_communications
**发布日期**: 2026-03-16
**DOI**: [10.1038/s41467-026-70315-4](https://doi.org/10.1038/s41467-026-70315-4)

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

**评分理由**: 论文研究的是地球科学领域的地震机制，特别是俯冲带中大型逆冲地震的发生条件，涉及岩石力学、变质岩相学和地震学。所有评分关键词均属于医学影像分析和人工智能在医疗决策支持中的应用领域，与论文的地球物理研究内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究探讨了在冷俯冲带中，大型逆冲地震如何在蓝片岩相变质沉积物通道中发生，并通过实验发现稳定矿物在低温条件下使上地幔发生大地震成为可能。

<details open>
<summary>摘要翻译</summary>

> 巨型逆冲地震通常发生在暖俯冲带的上覆板块莫霍面或350°C等温线以上。然而，在冷俯冲带（如克马德克、日本海沟和智利边缘）的35-55公里深度处，地幔楔角内也会发生大型地震。本文研究了可能在冷俯冲通道中出现的硬柱石蓝片岩相变杂砂岩的摩擦行为，以更好地理解变质程度对发震深度这种一级变化的控制作用。我们在室温至500°C、有效正应力50 MPa至320 MPa条件下对变杂砂岩断层泥进行了速度阶跃实验，捕捉了不稳定摩擦状态及脆性-流动转变过程。变杂砂岩的本构行为表明其在莫霍面以下的高温条件下可能具有发震潜力。地幔楔角中的大型逆冲地震可能发育于冷俯冲板块的硬柱石蓝片岩相变沉积物通道中。本研究发现，冷俯冲带的稳定矿物使得地球土地幔中发生大型地震成为可能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Giant megathrust earthquakes typically occur above the upper-plate Moho or the 350°C isotherm in warm subduction zones. However, large earthquakes also occur within the mantle wedge corner at 35-55 km depth at cold subduction zones, such as the Kermadec, Japan Trench, and Chilean margins. Here we investigate the frictional behavior of lawsonite blueschist metagreywacke, potentially found in cold subduction channels, to better understand the control of metamorphic grade on such first-order variations in seismogenic depth. We perform velocity-step experiments on metagreywacke gouge from room temperature to 500°C and effective normal stresses from 50 MPa to 320 MPa, capturing the unstable friction regime and the brittle-to-flow transition. The constitutive behavior of metagreywacke indicates a potential seismogenic behavior at high temperatures below the Moho. Large megathrust earthquakes in the mantle wedge corner may develop in the lawsonite blueschist metasediment channel of cold subduction slabs. This study finds that stable minerals at cold subduction zones enable large earthquakes in Earth’s upper mantle.

</details>
<br>

**关键词**: megathrust earthquakes, cold subduction zones, mantle wedge corner, lawsonite blueschist, metagreywacke, seismogenic depth, frictional behavior, brittle-to-flow transition

---

## Token 消耗统计

- **总计**: 652,823 tokens（输入 452,888 / 输出 199,935）
