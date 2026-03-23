# 📊 Nature Communications 研究报告 (2026-03-12)

> 生成时间: 2026-03-12 18:03:55
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

- **总抓取**: 16 篇
- **及格论文**: 1 篇 (6.2%)
- **深度分析**: 1 篇

---

## ⭐ 及格论文详细分析

### 1. A foundation model for multi-task cross-distribution restoration of fluorescence microscopy images

**作者**: Qiqi Lu, Xiuli Liu, Qianjin Feng, Shaoqun Zeng, Shenghua Cheng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70307-4](https://doi.org/10.1038/s41467-026-70307-4)

**评分**: 41.0 / 29.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical image segmentation | 1.0 | 5.0/10 | 5.0 |
| deep learning medical imaging | 1.0 | 8.0/10 | 8.0 |
| AI for diagnosis | 1.0 | 5.0/10 | 5.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 5.0/10 | 5.0 |
| foundation models medical imaging | 1.0 | 10.0/10 | 10.0 |

**评分理由**: 论文专注于荧光显微镜图像的多任务跨分布恢复基础模型，属于医学图像分析范畴，使用深度学习技术，因此与'medical image analysis'和'deep learning medical imaging'高度相关（8分）。'foundation models medical imaging'是核心内容，得10分。'medical image segmentation'和'AI for diagnosis'有一定关联，因为图像恢复可能辅助分割和诊断，但非直接研究，得5分。'multimodal medical imaging'得5分，因涉及跨分布处理，但未明确多模态融合。'prognosis prediction'和'surgical planning'完全无关，得0分。加权总分计算为：8*1 + 5*1 + 8*1 + 5*1 + 0*1 + 0*1 + 5*1 + 10*1 = 41.0，高于及格分29.0。作者列表中未指定专家。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Fluorescence microscopy image restoration in a unified model that leverages textual prior information to adapt to specific tasks and data distributions is presented and the performance of existing cell/organelle segmentation models can be enhanced using the high-quality images restored by FluoResFM.

!!! tip deepseek-chat TL;DR

    该论文提出了一种用于荧光显微镜图像多任务跨分布恢复的基础模型，解决了图像质量退化问题，并展示了其在多种恢复任务中的有效性。

**关键词**: foundation model, fluorescence microscopy, image restoration, multi-task learning, cross-distribution, deep learning, medical imaging

**深度分析**:

#### 用于荧光显微镜图像多任务跨分布修复的基础模型

**摘要**:

> 本研究针对荧光显微镜图像修复领域现有模型任务单一、数据分布受限导致泛化能力不足的问题，提出了FluoResFM基础模型。该模型通过整合文本先验信息，能够适应多种修复任务（如图像去噪、去卷积、超分辨率）和不同数据分布。研究在包含20多种生物结构的数据集上进行训练，结果表明FluoResFM在跨数据集和跨成像条件下表现出优异的修复性能和泛化能力。仅需单个样本微调即可达到传统模型数百样本训练的效果，并能扩展到3D图像修复等新任务。此外，经FluoResFM修复的高质量图像还能提升现有细胞/细胞器分割模型的性能。

**创新点**:
- 提出首个面向荧光显微镜图像多任务跨分布修复的统一基础模型
- 引入文本先验信息实现任务和分布的自适应，提升模型泛化能力
- 实现少样本（单样本）微调即可达到传统模型大量数据训练的效果
- 模型可灵活扩展到3D修复、表面投影等新任务
- 修复后的图像能直接提升下游分割模型的性能

<details>
<summary>方法</summary>

!!! info

    研究采用基于Transformer的架构，整合文本编码器和图像编码器，利用BiomedCLIP预训练的文本-图像表示。通过多任务学习框架，在包含图像去噪、去卷积、超分辨率三个任务的数据集上进行预训练，数据集涵盖20多种生物结构和多样成像条件。采用文本提示引导的图像修复策略，使模型能根据文本描述适应特定任务和数据分布。训练后通过少量样本微调实现对新任务和分布的快速适应。

</details>
<br>

**关键结果**:
- 在多个基准测试中，FluoResFM在图像修复质量上优于现有任务特定模型
- 在跨生物结构和成像条件的数据集上表现出优异的泛化性能
- 仅需单个样本微调，在未见数据上的表现即可媲美传统模型数百样本训练结果
- 成功扩展到3D图像修复、表面投影、各向同性重建等新任务
- 使用FluoResFM修复的图像显著提升了Cellpose等分割模型的性能

**技术栈**: Transformer架构, BiomedCLIP预训练模型（文本和图像编码器）, 多任务学习框架, 文本提示引导的图像修复技术, 扩散模型相关技术, Python、PyTorch深度学习框架, Napari图像查看器插件, 结构相似性指数（SSIM）等图像质量评估指标

<details>
<summary>优点</summary>

- 首次实现荧光显微镜图像修复的多任务统一建模，突破传统任务特定模型的局限
- 强大的跨分布泛化能力，适应不同生物结构和成像条件
- 高效的少样本适应机制，大幅降低新任务的数据需求
- 良好的可扩展性，能轻松适应新修复任务
- 开源代码和预训练模型促进社区使用和后续研究
- 实际应用价值高，能直接提升下游分析任务的性能

</details>
<br>

<details>
<summary>局限</summary>

- 模型性能可能受文本提示质量的影响
- 在极端成像条件或罕见生物结构上的表现仍需验证
- 计算资源需求较大，可能限制在资源有限环境下的应用
- 主要针对荧光显微镜图像，对其他显微成像模式的适用性未充分验证
- 实时处理性能未详细评估，可能不适用于需要实时反馈的应用场景

</details>
<br>

**与研究方向的相关性**: {'医学图像分割与解剖结构建模': '论文虽聚焦图像修复，但修复后的图像直接提升了细胞/细胞器分割模型的性能，与分割任务高度相关', '医学影像深度学习': '完全符合，研究基于深度学习开发基础模型，应用于CT、MRI、超声之外的荧光显微镜影像', 'AI疾病诊断与预后预测': '间接相关，高质量的图像修复是准确诊断的基础，但论文未直接涉及疾病诊断', '图像引导手术规划与导航': '相关性较弱，主要针对显微镜图像而非手术影像', '多模态医学数据融合': '部分相关，模型整合了文本和图像模态，但未涉及临床多模态数据', '医疗健康稳健可泛化AI模型': '高度相关，论文核心贡献正是开发具有强泛化能力的基础模型，能适应多种任务和分布'}

---

## 📋 所有论文列表

### 1. ✅ A foundation model for multi-task cross-distribution restoration of fluorescence microscopy images

**作者**: Qiqi Lu, Xiuli Liu, Qianjin Feng, Shaoqun Zeng, Shenghua Cheng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70307-4](https://doi.org/10.1038/s41467-026-70307-4)

**评分**: 41.0 / 29.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical image segmentation | 1.0 | 5.0/10 | 5.0 |
| deep learning medical imaging | 1.0 | 8.0/10 | 8.0 |
| AI for diagnosis | 1.0 | 5.0/10 | 5.0 |
| prognosis prediction | 1.0 | 0.0/10 | 0.0 |
| surgical planning | 1.0 | 0.0/10 | 0.0 |
| multimodal medical imaging | 1.0 | 5.0/10 | 5.0 |
| foundation models medical imaging | 1.0 | 10.0/10 | 10.0 |

**评分理由**: 论文专注于荧光显微镜图像的多任务跨分布恢复基础模型，属于医学图像分析范畴，使用深度学习技术，因此与'medical image analysis'和'deep learning medical imaging'高度相关（8分）。'foundation models medical imaging'是核心内容，得10分。'medical image segmentation'和'AI for diagnosis'有一定关联，因为图像恢复可能辅助分割和诊断，但非直接研究，得5分。'multimodal medical imaging'得5分，因涉及跨分布处理，但未明确多模态融合。'prognosis prediction'和'surgical planning'完全无关，得0分。加权总分计算为：8*1 + 5*1 + 8*1 + 5*1 + 0*1 + 0*1 + 5*1 + 10*1 = 41.0，高于及格分29.0。作者列表中未指定专家。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Fluorescence microscopy image restoration in a unified model that leverages textual prior information to adapt to specific tasks and data distributions is presented and the performance of existing cell/organelle segmentation models can be enhanced using the high-quality images restored by FluoResFM.

!!! tip deepseek-chat TL;DR

    该论文提出了一种用于荧光显微镜图像多任务跨分布恢复的基础模型，解决了图像质量退化问题，并展示了其在多种恢复任务中的有效性。

**关键词**: foundation model, fluorescence microscopy, image restoration, multi-task learning, cross-distribution, deep learning, medical imaging

---

### 2. ❌ Elucidating the rate-limiting step of CO2 electroreduction on metal phthalocyanines

**作者**: Zhuanghe Ren, Kaige Shi, Zhen Meng, Thomas Egan, Talat S. Rahman, Xiaofeng Feng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70445-9](https://doi.org/10.1038/s41467-026-70445-9)

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

**评分理由**: 论文研究电化学CO2还原反应（CO2RR）在金属酞菁催化剂上的机理，属于电化学、催化化学领域。所有评分关键词均涉及医学影像分析、人工智能医疗应用，与论文内容完全无关。论文未涉及任何医学影像、深度学习、疾病诊断、手术规划或多模态医疗数据相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究揭示了金属酞菁催化剂上电化学CO2还原反应的限速步骤，发现钴酞菁的分散状态决定了是质子化还是CO2吸附成为限速步骤，并阐明了电解质阴离子的作用机制。

<details open>
<summary>摘要翻译</summary>

> 固定化分子催化剂，特别是金属酞菁化合物，因其明确的活性位点和良好的性能，在电化学二氧化碳还原反应（CO<sub>2</sub>RR）中受到广泛关注。然而，其反应机理，尤其是速率决定步骤，仍存在争议。本研究通过电化学分析和动力学同位素效应测量，以金（Au）为参照，确定了固定化金属酞菁上CO<sub>2</sub>RR还原为CO的速率决定步骤。值得注意的是，钴酞菁（CoPc）表现出分散度依赖的动力学：在碳纳米管负载的分子分散CoPc（CoPc/CNTs）上，吸附态*CO<sub>2</sub>的质子化是速率决定步骤；而在聚集态CoPc上，由于钴活性位点界面电场减弱，CO<sub>2</sub>的吸附成为速率决定步骤。这一机理差异进一步阐明了电解质阴离子的作用：HCO<sub>3</sub><sup>-</sup>在Au上主要作为旁观者，而在CoPc/CNTs上，它通过在速率决定的质子化步骤中充当质子供体，促进了CO<sub>2</sub>RR。这些发现为理解金属酞菁上的CO<sub>2</sub>RR反应机理提供了新见解，并为分子电催化剂的理性设计提供了指导。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Immobilized molecular catalysts, especially metal phthalocyanines, have garnered substantial interest for the electrochemical CO<sub>2</sub> reduction reaction (CO<sub>2</sub>RR) due to their well-defined active sites and promising performance. Yet, the reaction mechanism, particularly the rate-limiting step, remains debated. Here, using electrochemical analysis and kinetic isotope effect measurements, we identify the rate-limiting step of CO<sub>2</sub>RR to CO on immobilized metal phthalocyanines, with Au as a reference. Notably, cobalt phthalocyanine (CoPc) exhibits dispersion-dependent kinetics: protonation of adsorbed *CO<sub>2</sub> is rate-limiting on molecularly dispersed CoPc supported on carbon nanotubes (CoPc/CNTs), whereas CO<sub>2</sub> adsorption becomes rate-limiting on aggregated CoPc due to a weakened interfacial electric field at the Co active sites. This mechanistic distinction further elucidates the role of electrolyte anions: HCO<sub>3</sub><sup>-</sup>, largely a spectator on Au, promotes CO<sub>2</sub>RR on CoPc/CNTs by serving as a proton donor in the rate-limiting protonation step. These findings provide mechanistic insights into CO<sub>2</sub>RR on metal phthalocyanines and guide the rational design of molecular electrocatalysts.

</details>
<br>

**关键词**: CO2 electroreduction, metal phthalocyanines, rate-limiting step, cobalt phthalocyanine, kinetic isotope effect, electrochemical analysis, molecular catalysts, electrocatalysts

---

### 3. ❌ Extracellular vesicle engineering using a small scaffold protein

**作者**: Wenjing Yan, Shizhi Wang, Haibin Hao, Hong Lin, Chen Wang, Shuqian Xie, Xing Zhang, Yiran Lu, Xin Ding, Xue Chen, Haohan Liu, Guiyuan Zhang, Dong Wei, ChangYan Ma, Cheng Tang, Xiuting Li, Bingjia Yu, Jing Hu, Zhongze Gu, Evan Y. Yu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70451-x](https://doi.org/10.1038/s41467-026-70451-x)

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

**评分理由**: 论文研究的是细胞外囊泡（EVs）的工程化，通过鉴定和优化支架蛋白ENPP1/EN144来增强EVs的药物递送能力，并应用于炎症性疾病（如脓毒症、骨关节炎）的治疗。所有评分关键词均涉及医学影像分析、AI诊断、手术规划等方向，而本文属于生物医学工程、药物递送和炎症治疗领域，两者在研究对象、方法、应用上均无直接关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work establishes EN144 as a minimal, high-performance scaffold for EV engineering and demonstrates its broad therapeutic potential for inflammatory diseases.

!!! tip deepseek-chat TL;DR

    该研究解决了细胞外囊泡工程中支架蛋白选择有限的问题，通过鉴定ENPP1并开发其截短变体EN144作为高效支架，成功构建了能抑制IL-6信号、减轻炎症的工程化囊泡，并在小鼠模型中验证了对脓毒症和骨关节炎的治疗效果。

<details open>
<summary>摘要翻译</summary>

> 摘要 细胞外囊泡因其良好的生物相容性与低免疫原性，成为极具前景的药物递送载体。通过对膜结合型EV分选支架蛋白进行基因工程改造，可在囊泡表面装配靶向元件并在腔内富集治疗性载荷，从而增强EV的功能。然而，目前结构简单、序列较短的支架蛋白选择有限。本研究通过基于质谱的蛋白质组学分析，鉴定出ENPP1作为一种优异的支架蛋白。进一步研究表明，其144个氨基酸的截短变体EN144能高效装载多种治疗性载荷，且性能优于传统支架。通过将EN144与IL-6诱骗受体gp130融合，我们构建出工程化诱骗EV，可有效抑制炎症性IL-6反式信号传导。在小鼠模型中，这些EV能减轻炎症反应、提高脓毒症存活率；当靶向软骨组织时，还能缓解骨关节炎的组织损伤。本研究确立了EN144作为一种精简高效的新型EV工程支架，并展示了其在炎症性疾病治疗中的广阔应用前景。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Extracellular vesicles (EVs) are promising drug-delivery vehicles owing to their biocompatibility and low immunogenicity. Genetic engineering of a membrane-bound EV-sorting scaffold protein empowers EVs by installing targeting moieties on the surface and enriching therapeutic cargo in the lumen. However, the choice of scaffold proteins with simple structures and short sequences is limited. Here, we conduct mass spectrometry-based proteomic studies and identify ENPP1 as a superior scaffold protein. Furthermore, we show that a truncated 144-amino acid variant, EN144, efficiently loads diverse therapeutic cargoes and outperforms conventional scaffolds. By fusing EN144 to the IL-6 decoy receptor gp130, we create engineered decoy EVs that potently inhibit inflammatory IL-6 trans-signaling. In mouse models, these EVs reduce inflammation, improve survival in sepsis, and, when targeted to cartilage, alleviate tissue damage in osteoarthritis. Our work establishes EN144 as a minimal, high-performance scaffold for EV engineering and demonstrates its broad therapeutic potential for inflammatory diseases.

</details>
<br>

**关键词**: extracellular vesicles, scaffold protein, ENPP1, drug delivery, inflammatory diseases, IL-6 signaling, sepsis, osteoarthritis

---

### 4. ❌ Spatial cartography of human thymus enables the geopositioning of lineage transcription factors in rare mimetic thymic epithelial cells

**作者**: Uma S. Kamaraj, Ying Chen, Junjie Lei, Pradeep Gautam, Pongsatorn Horcharoensuk, Czaryna K. M. Clemente, Katja G. Weinacht, Nicholas R. J. Gascoigne, Jinmiao Chen, C. Chen, Qingfeng Chen, Qi-Jing Li, Lai Guan Ng, Yuin-Han Loh
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-68596-w](https://doi.org/10.1038/s41467-026-68596-w)

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

**评分理由**: 论文研究人类胸腺的空间转录组图谱和罕见模拟胸腺上皮细胞中谱系转录因子的定位，属于免疫学和发育生物学领域，使用单细胞RNA测序、空间转录组学、免疫荧光和流式细胞术等分子生物学技术，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划或多模态医学影像等主题。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A high-resolution spatial atlas of the human fetal and pediatric thymi is established to uncover distinct architectural features and TFs regulating these rare cell types, and serves as a resource for further studies.

!!! tip deepseek-chat TL;DR

    该研究通过空间转录组学绘制了人类胸腺图谱，定位了罕见模拟胸腺上皮细胞中的谱系转录因子，揭示了胸腺微环境的细胞组成和空间组织。

**关键词**: human thymus, spatial cartography, thymic epithelial cells, lineage transcription factors, spatial transcriptomics, single-cell RNA sequencing, immune system development, tissue microenvironment

---

### 5. ❌ Meta-analyses on charitable giving clarify evidence for empathic and effective altruism

**作者**: Matthew J. Hornsey, Jessica L. Spence, Cassandra M. Chapman
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70230-8](https://doi.org/10.1038/s41467-026-70230-8)

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

**评分理由**: 论文标题和摘要显示该研究是关于慈善捐赠的元分析，探讨共情利他主义和有效利他主义的证据，属于心理学、行为科学和社会科学领域。所有评分关键词均涉及医学影像分析、人工智能医疗应用、手术规划等医学技术主题，与论文内容完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文通过元分析研究了慈善捐赠行为，澄清了共情利他主义和有效利他主义的证据基础。

**关键词**: charitable giving, meta-analysis, empathic altruism, effective altruism, altruism, donation behavior, psychological research

---

### 6. ❌ Polyphenol mediated zinc-oxygen synergistic hydrogel remodels senescent microenvironment for periodontal tissue regeneration

**作者**: Chengxinyue Ye, Jin Liu, Jinhui Ran, Shoushan Hu, Lei Yang, Jialiang Zhao, Xinyi Fang, Z J Zhang, Xin Xiong, Xueman Zhou, Yating Yi, Xiaolong Zeng, Xulei Lu, Jun Wang, Chaoming Xie
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70176-x](https://doi.org/10.1038/s41467-026-70176-x)

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

**评分理由**: 论文研究的是用于牙周组织再生的水凝胶材料，通过多酚介导的锌-氧协同作用来改善衰老微环境。研究内容属于生物材料、组织工程和牙周病治疗领域，完全不涉及医学影像分析、深度学习、AI诊断、预后预测、手术规划、多模态医学影像或基础模型等关键词。所有关键词与论文主题无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This polyphenol-mediated synergistic strategy offers a pathway to rejuvenate the senescent periodontal microenvironment, thereby overcoming tissue regeneration barriers and offering a translatable pathway for treating periodontitis and other aging-associated inflammatory diseases.

!!! tip deepseek-chat TL;DR

    该研究开发了一种多酚介导的锌-氧协同水凝胶，通过改善缺氧、氧化应激和微生物失衡来重塑衰老的牙周微环境，从而促进牙周组织再生并治疗牙周炎。

<details open>
<summary>摘要翻译</summary>

> 驻留于炎症、菌群失调及低氧微环境中的衰老间充质干细胞是牙周再生的障碍。本文提出一种氢化咖啡酸介导的丝素蛋白水凝胶体系，其整合了锰/氢化咖啡酸修饰的过氧化钙与氢化咖啡酸修饰的沸石咪唑酯骨架-8材料，以重塑该微环境。该策略赋予水凝胶在牙周袋内增强的粘附性与适应性。锰-氢化咖啡酸复合物通过催化作用降低氧化应激并改善缺氧状态；同时，锌离子与氢化咖啡酸协同恢复微生物平衡并减轻炎症。这种多功能水凝胶通过调控微生物稳态、促进再生性免疫表型，精准靶向衰老的牙周生态位。此外，它直接缓解干细胞端粒缩短、DNA损伤及氧化应激，从而恢复细胞功能。通过特异性干预缺氧与锌缺乏，这种多酚介导的协同策略为衰老牙周微环境的重塑提供了新途径，有望突破组织再生屏障，为治疗牙周炎及其他衰老相关炎症性疾病提供可转化的解决方案。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Senescent mesenchymal stem cells residing in an inflammatory, dysbiotic, and hypoxic microenvironment pose a barrier to periodontal regeneration. Here we introduce a hydrocaffeic acid (HCA)-mediated silk fibroin hydrogel incorporating Mn/HCA-modified calcium peroxide (Mn-hCaO₂) and HCA-modified zeolitic imidazolate framework-8 (hZIF8) to rejuvenate this environment. The strategy imbues the hydrogel with enhanced adhesion and adaptability in periodontal pockets. The Mn-HCA complex acts catalytically to reduce oxidative stress and correct hypoxia. Simultaneously, Zn²⁺ and HCA restore microbial balance and mitigate inflammation. This multifunctional hydrogel targets the senescent periodontal niche by normalizing microbiota homeostasis and promoting a regenerative immune profile. Concurrently, it directly alleviates telomere shortening, DNA damage and oxidative stress in stem cells, thereby rejuvenating cellular function. By specifically addressing hypoxia and zinc deficiency, this polyphenol-mediated synergistic strategy offers a pathway to rejuvenate the senescent periodontal microenvironment, thereby overcoming tissue regeneration barriers and offering a translatable pathway for treating periodontitis and other aging-associated inflammatory diseases.

</details>
<br>

**关键词**: hydrogel, periodontal regeneration, senescent microenvironment, polyphenol, zinc-oxygen synergy, periodontitis, tissue engineering, oxidative stress

---

### 7. ❌ CF2H: a cell-free two-hybrid platform for rapid protein binder screening

**作者**: Julien Capin, Pauline Mayonove, Angelique DeVisch, A. Becher, Giang Ngo, Alexis Courbet, Robert J. Ragotte, Martin Cohen Gonsaud, Julien Espeut, Jerome Bonnet
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-69741-1](https://doi.org/10.1038/s41467-026-69741-1)

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

**评分理由**: 论文标题和摘要显示该研究专注于蛋白质相互作用筛选的生物技术平台开发（CF2H: cell-free two-hybrid platform），涉及蛋白质工程、合成生物学和生物分子检测，与医学影像分析、深度学习医疗影像、疾病诊断/预后、手术规划、多模态影像或医疗基础模型等关键词无任何直接关联。所有关键词均评0分，因为论文内容完全属于分子生物学和生物技术领域，而非医疗影像或临床决策支持AI。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种名为CF2H的无细胞双杂交平台，用于快速筛选蛋白质结合剂，实现了高通量、无细胞的蛋白质相互作用检测。

**关键词**: cell-free two-hybrid, protein binder screening, protein-protein interactions, high-throughput screening, synthetic biology, biomolecular detection, CF2H platform

---

### 8. ❌ Magnetic-driven multifunctional optoelectronic catheter for in vivo chemical mapping and precisely guided-tumor therapy

**作者**: Fuqian Chen, Xiaxu Liu, Yuanxi Zhang, Ying Zheng, Junjie Yang, Tong Wu, Ke Zhao, Weiyuan Chen, Yuanyuan Li, Xia Gong, Hui Wang, Shuo Wu, Xi Xie, Lelun Jiang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70529-6](https://doi.org/10.1038/s41467-026-70529-6)

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

**评分理由**: 论文描述了一种磁驱动的多功能光电导管，用于体内化学映射和精确引导的肿瘤治疗。该研究侧重于导管设备开发、化学传感和光热治疗，不涉及医学图像分析、分割、深度学习、AI诊断、预后预测、手术规划、多模态成像或基础模型。所有关键词均与论文内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A 2.5 mm magnetic-driven multifunctional optoelectronic catheter fabricated via 3D multi-axis printing for in situ tumor mapping and therapy that achieves accurate navigation, multiparametric sensing, and targeted contrast agent delivery in complex anatomy.

!!! tip deepseek-chat TL;DR

    该研究开发了一种磁驱动的多功能光电导管，用于体内化学映射和精确引导的肿瘤治疗，实现了实时化学传感和光热治疗。

**关键词**: optoelectronic catheter, in vivo chemical mapping, tumor therapy, magnetic-driven, photothermal therapy, chemical sensing, real-time monitoring, precise guidance

---

### 9. ❌ Optical control of the cardiac rhythm with photoswitchable NaV1.5 channel blockers

**作者**: Shiqi Liu, Weiqiang Guan, Zhangqiang Li, Wei Wang, Huifang Song, Jia’ao Li, Junjie Hou, Huan Wang, JingWei Xiong, Min Yang, Nieng Yan, Xin Tian, Houhua Li, Zhuo Huang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70305-6](https://doi.org/10.1038/s41467-026-70305-6)

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

**评分理由**: 论文研究的是使用光控钠通道阻断剂（photoswitchable NaV1.5 channel blockers）调控心脏节律，属于分子生物学、心脏电生理学和光遗传学领域，与医学影像分析、深度学习、AI诊断、手术规划等关键词完全无关。论文未涉及任何医学影像处理、AI模型开发或临床决策支持技术。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work establishes azo-Q2a as a robust photoswitchable inhibitor for NaV1.5 and provides a structural blueprint for the rational design of next-generation optopharmacological antiarrhythmic agents.

!!! tip deepseek-chat TL;DR

    该研究开发了一种光控钠通道阻断剂，通过光照可逆地调控心脏钠通道活性，从而精确控制心脏节律，为心律失常治疗提供了新工具。

**关键词**: cardiac rhythm, photoswitchable, NaV1.5 channel, channel blockers, optical control, arrhythmia, heart, ion channels

---

### 10. ❌ Probing boron vacancy defects in hBN via single spin relaxometry

**作者**: Alex L. Melendez, Ruotian Gong, Guanghui He, Yan Wang, Yueh-Chun Wu, Thomas Poirier, Steven Randolph, Sujoy Ghosh, Liangbo Liang, Stephen Jesse, An-Ping Li, Joshua T. Damron, Benjamin J. Lawrie, James H. Edgar, Ivan V. Vlassiouk, Chong Zu, Huan Zhao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**arXiv链接**: [https://arxiv.org/abs/2504.09432](https://arxiv.org/abs/2504.09432)
**DOI**: [10.1038/s41467-026-70545-6](https://doi.org/10.1038/s41467-026-70545-6)

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

**评分理由**: 论文研究的是量子传感和材料科学领域，具体涉及利用金刚石中的氮空位中心探测六方氮化硼中的硼空位缺陷，用于纳米尺度自旋缺陷表征。所有评分关键词均与医学影像分析、临床决策支持、疾病诊断/预后、手术规划等医学应用相关，而该论文完全不涉及这些医学领域，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文开发了一种利用金刚石氮空位中心通过自旋弛豫时间变化间接探测六方氮化硼中硼空位缺陷的方法，实现了纳米尺度自旋缺陷的无光学检测和定量映射。

<details open>
<summary>摘要翻译</summary>

> 摘要：固体中的自旋缺陷因其较长的相干时间和光学可寻址性，为量子传感与量子存储提供了极具前景的平台。本研究将金刚石中的单个氮空位（NV）中心与扫描探针显微镜技术相结合，实现了纳米尺度下基于自旋的量子传感器的探测、读出与空间成像。以六方氮化硼中的硼空位（$${{{{\rm{V}}}}}_{{{{\rm{B}}}}}^{-}$$）中心——一种新兴的二维自旋体系——为模型，我们通过监测邻近NV中心自旋弛豫时间（T1）的变化，间接探测了其电子自旋共振，从而无需对$${{{{\rm{V}}}}}_{{{{\rm{B}}}}}^{-}$$进行光学激发或荧光探测。NV中心与$${{{{\rm{V}}}}}_{{{{\rm{B}}}}}^{-}$$系综之间的交叉弛豫显著降低了NV的T1值，这使得我们能够对超出光学衍射极限的缺陷密度进行定量纳米尺度成像，并清晰分辨了同位素富集的h-10B-15N中的超精细分裂。我们的方法展示了三维与二维材料中自旋传感器之间的相互作用，确立了NV中心作为一种通用探针，可用于表征其他方法难以探测的自旋缺陷。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Spin defects in solids offer promising platforms for quantum sensing and memory due to their long coherence times and optical addressability. Here, we integrate a single nitrogen-vacancy (NV) center in diamond with scanning probe microscopy to detect, read out, and spatially map spin-based quantum sensors at the nanoscale. Using the boron vacancy ( $${{{{\rm{V}}}}}_{{{{\rm{B}}}}}^{-}$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:msubsup> <mml:mrow> <mml:mi>V</mml:mi> </mml:mrow> <mml:mrow> <mml:mi>B</mml:mi> </mml:mrow> <mml:mrow> <mml:mo>−</mml:mo> </mml:mrow> </mml:msubsup> </mml:math> ) center in hexagonal boron nitride—an emerging two-dimensional spin system—as a model, we detect its electron spin resonance indirectly via changes in the spin relaxation time ( T 1 ) of a nearby NV center, eliminating the need for optical excitation or fluorescence detection of the $${{{{\rm{V}}}}}_{{{{\rm{B}}}}}^{-}$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:msubsup> <mml:mrow> <mml:mi>V</mml:mi> </mml:mrow> <mml:mrow> <mml:mi>B</mml:mi> </mml:mrow> <mml:mrow> <mml:mo>−</mml:mo> </mml:mrow> </mml:msubsup> </mml:math> . Cross-relaxation between NV and $${{{{\rm{V}}}}}_{{{{\rm{B}}}}}^{-}$$ <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"> <mml:msubsup> <mml:mrow> <mml:mi>V</mml:mi> </mml:mrow> <mml:mrow> <mml:mi>B</mml:mi> </mml:mrow> <mml:mrow> <mml:mo>−</mml:mo> </mml:mrow> </mml:msubsup> </mml:math> ensembles significantly reduces NV T 1 , enabling quantitative nanoscale mapping of defect densities beyond the optical diffraction limit and clear resolution of hyperfine splitting in isotopically enriched h 10 B 15 N. Our method demonstrates interactions between spin sensors in 3D and 2D materials, establishing NV centers as versatile probes for characterizing otherwise inaccessible spin defects.

</details>
<br>

**关键词**: nitrogen-vacancy center, boron vacancy defect, hexagonal boron nitride, spin relaxometry, quantum sensing, nanoscale mapping, cross-relaxation, spin defects

---

### 11. ❌ Wafer-scale manufacturing of ultra-broadband, high-power erbium-doped integrated lasers

**作者**: Xinru Ji, Xuan Yang, Yang Liu, Zheru Qiu, Grigory Lihachev, Simone Bianconi, Jiale Sun, Andrey Voloshin, Taegon Kim, Joseph C. Olson, Tobias J. Kippenberg
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-69787-1](https://doi.org/10.1038/s41467-026-69787-1)

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

**评分理由**: 论文研究的是集成光子学中的掺铒硅氮化物可调谐激光器的晶圆级制造技术，属于光子学、半导体制造和激光器领域。所有评分关键词均涉及医学影像分析、人工智能诊断、手术规划等医疗AI应用，与论文的光子学制造主题完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了掺铒硅氮化物集成激光器难以大规模制造的问题，通过采用200纳米厚波导设计降低了离子注入能量要求，首次实现了完全晶圆级、与代工厂兼容的可调谐激光器制造，并获得了宽调谐范围、高输出功率和低线宽等优异性能。

<details open>
<summary>摘要翻译</summary>

> 摘要：铒（Er）因其长激发态寿命、低噪声与非线性特性以及温度稳定性，成为放大器与激光器中极具吸引力的增益介质。近期发展的超低损耗Si₃N₄光子集成电路与铒离子注入技术相结合，已实现了高性能片上铒激光器，但其制造可扩展性受限于在紧密限域的700纳米厚度波导所需的高达2 MeV的注入能量。本研究通过采用200纳米厚度波导，首次展示了完全晶圆级、与代工工艺兼容的掺铒Si₃N₄可调谐激光器。该设计将注入能量降低至500 keV以下，从而能够使用300毫米工业级注入设备。低限域设计同时提升了激光器性能与输出功率。我们实现了覆盖C波段与L波段的91纳米调谐范围、47.6毫瓦光纤耦合输出功率以及78.5赫兹的本征线宽。器件可在高达125°C的温度下工作，并在6小时内表现出低于15兆赫的频率漂移，这为集成光子学提供了可扩展的高性能掺铒激光器解决方案。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Abstract Erbium (Er) is an attractive gain medium for amplifiers and lasers due to its long excited-state lifetime, low noise and nonlinearity, and temperature stability. Recently developed ultra-low-loss Si 3 N 4 photonic integrated circuits combined with Er ion implantation have enabled high-performance on-chip Er lasers, but manufacturing scalability has been limited by the high 2 MeV implantation required for tightly confined 700-nm-thick waveguides. Here we demonstrate the first fully wafer-scale, foundry-compatible Er-doped Si 3 N 4 tunable lasers by using 200-nm-thick waveguides, reducing implantation energy to below 500 keV and enabling usage of 300-mm industrial implanters. The low-confinement design also improves laser performance and output power. We achieve 91 nm tuning across the C- and L-bands, 47.6 mW fiber-coupled output power, and a 78.5 Hz intrinsic linewidth. Devices operate up to 125 ∘ C and show less than 15 MHz drift over 6 hours, enabling scalable high-performance Er-doped lasers for integrated photonics.

</details>
<br>

**关键词**: erbium-doped lasers, silicon nitride photonics, wafer-scale manufacturing, tunable lasers, integrated photonics, low-confinement waveguides, ion implantation, high-power lasers

---

### 12. ❌ Protection of telomeres 1b safeguards the Arabidopsis genome by regulating ROS homeostasis

**作者**: Jihee Min, Claudia Castillo-González, Borja Barbero Barcenilla, In-Cheol Yeo, Xiaoyuan Xie, Sreyashree Bose, Fausto Andres Ortiz-Morea, Di Liu, Eli Canal, David E. Curtis, Monisha Yerram, Joonyoung Shin, Pavel Ulianich, Chinmay Phadke, Ping He, Andrzej Wierzbicki, Junjie Zhang, Eugene V. Shakirov, Thomas Juenger, Dorothy E. Shippen
**期刊/来源**: nature_communications
**发布日期**: 2026-03-10
**DOI**: [10.1038/s41467-026-70441-z](https://doi.org/10.1038/s41467-026-70441-z)

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

**评分理由**: 论文标题和摘要显示该研究是关于植物生物学（拟南芥）中端粒保护蛋白POT1b在基因组稳定性和ROS稳态调节中的作用，属于分子生物学和植物遗传学领域。所有评分关键词均涉及医学影像分析、人工智能临床决策支持等医疗技术应用，与论文的植物分子生物学研究内容完全无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that AtPOT1b modulates reactive oxygen species (ROS) homeostasis and genome stability in Arabidopsis thaliana mutants, supporting a conserved role for POT1 in modulating ROS homeostasis and genome stability, distinct from canonical telomeric functions.

!!! tip deepseek-chat TL;DR

    该研究揭示了拟南芥端粒保护蛋白POT1b通过调节活性氧（ROS）稳态来维持基因组稳定性的分子机制。

**关键词**: Arabidopsis, POT1b, telomere protection, genome stability, ROS homeostasis, reactive oxygen species, DNA damage, molecular mechanism

---

### 13. ❌ Gene expression dynamics of human and mouse craniofacial development at the single-cell level

**作者**: Nagham Khouri-Farah, Alexandra Manchel, Emma Wentworth Winchester, Brian M. Schilder, Kelsey Robinson, Sarah W. Curtis, Nathan Skene, Elizabeth J. Leslie-Clarkson, Justin Cotney
**期刊/来源**: nature_communications
**发布日期**: 2026-03-09
**DOI**: [10.1038/s41467-026-70232-6](https://doi.org/10.1038/s41467-026-70232-6)

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

**评分理由**: 论文研究的是人类和小鼠颅面发育的单细胞基因表达动态，使用单核RNA测序和空间转录组学技术，属于发育生物学和基因组学领域。所有评分关键词均涉及医学影像分析、深度学习、AI诊断、手术规划等临床决策支持技术，与论文的分子生物学研究方法完全无关。论文未涉及任何医学影像数据、图像处理、AI模型或临床决策支持系统。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This resource identifies multiple subtypes of mesenchyme, epithelium, and cranial neural crest, among other functionally distinct cell types in human craniofacial development spanning 4 to 8 post-conception weeks, revealing functional conservation of most cell types and identification of anatomically distinct cell subtypes.

!!! tip deepseek-chat TL;DR

    该研究通过单核RNA测序揭示了人类颅面发育4-8周的细胞类型动态，并与小鼠数据比较发现了功能保守性和与颅面裂风险相关的基因网络。

<details open>
<summary>摘要翻译</summary>

> 颅面发育是一个涉及多种短暂细胞类型特化的复杂过程。然而，我们对于人类颅面发育过程中这些过程及现存细胞类型的理解仍然有限。我们通过对受孕后4至8周的人类颅面发育样本进行单核RNA测序，填补了这一知识空白。该资源识别了间充质、上皮、颅神经嵴等多种功能各异的细胞类型及其亚型。通过与对应发育阶段小鼠的单核基因表达及空间转录组数据进行广泛比较，揭示了大多数细胞类型的功能保守性，并识别出解剖学上独特的细胞亚型。我们发现特定细胞亚型对正常面部形态具有不同贡献，并确定了口面裂的常见风险因素。此外，我们识别出特定的外胚层和上皮亚型，其基因表达网络受口面裂患者罕见的蛋白质编码区新生变异影响最为显著。综上，我们的数据为在细胞水平理解人类颅面发育提供了广泛的资源。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Craniofacial development is a complex process that involves the specification of diverse and transient cell types. However, our understanding of these processes and the cell-types present during human craniofacial developmental remains limited. We address this gap in knowledge through single-nucleus RNA sequencing of human craniofacial development spanning 4 to 8 post-conception weeks. This resource identifies multiple subtypes of mesenchyme, epithelium, and cranial neural crest, among other functionally distinct cell types. Extensive comparisons to single-nucleus gene expression and spatial transcriptomics of comparable mouse developmental stages reveal functional conservation of most cell types and identification of anatomically distinct cell subtypes. We find distinct contributions of cellular subtypes to normal facial morphology and common risk factors for orofacial clefts. Additionally, we find specific ectodermal and epithelial subtypes whose gene expression networks are most significantly affected by rare de novo protein-altering variants from orofacial cleft patients. Together our data provide an extensive resource for understanding human craniofacial development at the cellular level.

</details>
<br>

**关键词**: craniofacial development, single-nucleus RNA sequencing, human development, mouse development, cell types, orofacial clefts, spatial transcriptomics, gene expression networks

---

### 14. ❌ Superior resilience to poisoning and amenability to unlearning in quantum machine learning

**作者**: Yu-Qin Chen, Shi-Xin Zhang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-09
**arXiv链接**: [https://arxiv.org/abs/2508.02422](https://arxiv.org/abs/2508.02422)
**DOI**: [10.1038/s41467-026-70420-4](https://doi.org/10.1038/s41467-026-70420-4)

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

**评分理由**: 论文研究量子机器学习（QML）与经典机器学习在数据污染和遗忘学习方面的对比，核心是量子神经网络的理论特性（如对噪声的韧性、相变行为、高效遗忘能力），完全不涉及医学影像分析、疾病诊断、手术规划等医疗应用领域。所有评分关键词均与医学影像或临床决策支持相关，而论文内容纯粹是量子计算与机器学习的基础理论研究，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is established that quantum machine learning possesses the dual advantage of intrinsic resilience and efficient adaptability, providing a promising paradigm for the trustworthy and reliable artificial intelligence of the future.

!!! tip deepseek-chat TL;DR

    该论文通过对比经典与量子神经网络，发现量子模型对数据污染具有更强的韧性（表现为类似相变的临界行为），并提出了量子机器遗忘框架，证明量子模型能更高效地遗忘错误数据影响，从而为可信赖AI提供了新范式。

<details open>
<summary>摘要翻译</summary>

> 人工智能的可靠性取决于其训练数据的完整性，而这一基础常因噪声与损坏而受到破坏。本文通过对经典与量子神经网络在经典及量子数据上的比较研究，揭示了二者对数据损坏响应的根本差异。我们发现，经典模型表现出脆弱的记忆化倾向，导致泛化能力失效。相比之下，量子模型展现出卓越的韧性，其响应随噪声增加呈现类似相变的特征，揭示了一个临界点，超过该点后模型性能发生质变。我们进一步引入了量子机器遗忘（quantum machine unlearning）框架，即高效迫使训练模型遗忘不良影响的过程。研究表明，经典模型对错误数据形成僵化、顽固的记忆，而量子模型则显著更易于通过近似遗忘方法实现高效遗忘。我们的研究结果证实，量子机器学习兼具内在韧性与高效适应性的双重优势，为构建可信赖的未来人工智能提供了前景广阔的范式。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The reliability of artificial intelligence hinges on the integrity of its training data, a foundation often compromised by noise and corruption. Here, through a comparative study of classical and quantum neural networks on both classical and quantum data, we reveal a fundamental difference in their response to data corruption. We find that classical models exhibit brittle memorization, leading to a failure in generalization. In contrast, quantum models demonstrate superior resilience, underscored by a phase transition-like response to increasing noise, revealing a critical point beyond which the model's performance changes qualitatively. We further introduce a framework of quantum machine unlearning, the process of efficiently forcing a trained model to forget bad influences. We show that classical models form rigid, stubborn memories of erroneous data, while the quantum model is significantly more amenable to efficient forgetting with approximate unlearning methods. Our findings establish that quantum machine learning possesses the dual advantage of intrinsic resilience and efficient adaptability, providing a promising paradigm for the trustworthy and reliable artificial intelligence of the future.

</details>
<br>

**关键词**: quantum machine learning, quantum neural networks, data corruption resilience, machine unlearning, phase transition, trustworthy AI, classical vs quantum models

---

### 15. ❌ Multi-modal dissection of cell-type specific TDP-43 pathology in the motor cortex

**作者**: Wolfgang Ruf, Julia K. Kühlwein, Laura Meier, Sarah J. Brockmann, Jaehyun LeeBae, Ghazaleh Sadri-Vakili, Deniz Yilmazer-Hanke, Susanne Petri, Dietmar Rudolf Thal, Veselin Grozdanov, Karin M. Danzer
**期刊/来源**: nature_communications
**发布日期**: 2026-03-09
**DOI**: [10.1038/s41467-026-69944-6](https://doi.org/10.1038/s41467-026-69944-6)

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

**评分理由**: 论文研究的是ALS/ALS-FTD中TDP-43病理的细胞类型特异性机制，使用流式细胞术、单核多组学测序和空间转录组学等分子生物学技术，完全不涉及医学影像分析、深度学习、AI诊断、手术规划或医学影像模态融合。所有关键词均与论文内容无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that mainly excitatory cortical neurons are affected by TDP-43 pathology and define the cell types that are affected the most: intratelencephalic L2-L3-LINC00507-FREM3, L3-L5-RORB-LNX2, L3-L5-RORB-ADGRL4 & L6-THEMIS-LINC00343 neurons and extratelencephalic L5

!!! tip deepseek-chat TL;DR

    该研究通过多模态方法鉴定了ALS/ALS-FTD运动皮层中受TDP-43病理影响的主要神经元细胞类型，并发现转录异常具有细胞类型特异性。

<details open>
<summary>摘要翻译</summary>

> 细胞质TDP-43病理是ALS/ALS-FTD（肌萎缩侧索硬化/肌萎缩侧索硬化-额颞叶痴呆）的病理标志，也是跨越不同基因型、表型和中枢神经系统区域的共同疾病事件。为理解这一过程并寻找治疗靶点，我们需要明确哪些细胞类型受累，以及哪些细胞类型特异性效应使其特别脆弱。我们结合流式细胞术核分选与测序、单核多组学ATAC-seq和RNA-seq以及空间转录组学技术，对死后ALS/ALS-FTD运动皮层（30例ALS、20例ALS-FTD及32例对照样本）中受累神经元的转录细胞类型进行了鉴定。本研究显示，TDP-43病理主要影响兴奋性皮层神经元，并确定了受累最严重的细胞类型：端脑内神经元L2-L3-LINC00507-FREM3、L3-L5-RORB-LNX2、L3-L5-RORB-ADGRL4和L6-THEMIS-LINC00343，以及端脑外神经元L5-FEZF2-NTNG1。TDP-43病理引起的转录异常（如隐蔽外显子插入）具有细胞类型特异性，并在每种细胞类型中影响不同的基因集合，这凸显了以细胞类型特异性方式应对TDP-43病理的必要性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Cytoplasmic TDP-43 pathology is a pathological sign of ALS/ALS-FTD and a converging disease event across different genotypes, phenotypes and CNS areas. To understand this process and target it therapeutically, we need to define which cell types are affected and which cell-type specific effects make them particularly vulnerable. We coupled flow-cytometry nuclear sorting and sequencing with single-nucleus multi-omic ATAC-seq and RNA-seq and spatial transcriptomics to define the transcriptional cell type of affected neurons in the post-mortem ALS/ALS-FTD motor cortex (30 ALS, 20 ALS-FTD & 32 control samples). Here, we show that mainly excitatory cortical neurons are affected by TDP-43 pathology and define the cell types that are affected the most: intratelencephalic L2-L3-LINC00507-FREM3, L3-L5-RORB-LNX2, L3-L5-RORB-ADGRL4 & L6-THEMIS-LINC00343 neurons and extratelencephalic L5-FEZF2-NTNG1 neurons. Transcriptional aberrations by TDP-43 pathology, like cryptic exon inclusion, are cell-type specific and affect distinct gene sets in each cell type, highlighting the need to address TDP-43 pathology in a cell-type specific manner.

</details>
<br>

**关键词**: TDP-43 pathology, ALS/ALS-FTD, motor cortex, cell-type specific, single-nucleus multi-omics, spatial transcriptomics, excitatory neurons, cryptic exon inclusion

---

### 16. ❌ Long-read sequencing of families reveals increased germline and postzygotic mutation rates in repetitive DNA

**作者**: Michelle D. Noyes, Yang Sui, Youngjun Kwon, Nidhi Koundinya, Isaac Wong, Katherine M. Munson, Kendra Hoekzema, Jennifer Kordosky, Gage H. Garcia, Jordan Knuth, Anthony Lewis, Evan E. Eichler
**期刊/来源**: nature_communications
**发布日期**: 2026-03-09
**DOI**: [10.1038/s41467-026-70342-1](https://doi.org/10.1038/s41467-026-70342-1)

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

**评分理由**: 论文研究的是利用长读长测序技术分析自闭症家庭中的生殖系和合子后突变率，特别是重复DNA区域的突变特征。研究内容完全属于基因组学、遗传学和生物信息学领域，涉及测序技术、突变分析、DNA修复机制等。所有评分关键词均与医学影像分析、深度学习、AI诊断、手术规划等医学影像AI领域无关，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that enrichment in repeats occurs predominantly postzygotically, likely resulting from faulty DNA repair and interlocus gene conversion, where segmental duplication mutability is dependent on length and percent identity.

!!! tip deepseek-chat TL;DR

    本研究利用长读长测序技术分析自闭症家庭的突变率，发现重复DNA区域的生殖系和合子后突变率显著增加，且合子后突变主要富集于重复区域，可能与DNA修复错误和基因座间转换有关。

<details open>
<summary>摘要翻译</summary>

> 长读长测序技术提升了在复杂重复区域中发现变异、判定亲本来源以及区分生殖系与合子后突变的灵敏度。本研究应用Illumina、牛津纳米孔技术与PacBio测序平台，对来自42个自闭症谱系家庭的73名儿童（共157个个体）进行新生突变的发现与验证。我们检测了2.77 Gbp的人类基因组区域，平均每次遗传传递产生95个新生突变（87.5个单核苷酸替换，7.8个插入缺失），先证者与其未患病同胞之间的突变率或突变谱无显著差异。长读长测序使新生突变发现率提高20-40%，并将归类为早期胚胎起源的突变数量增加一倍。生殖系突变率为每代每碱基对1.30×10<sup>-8</sup>次替换；合子后突变率为0.23×10<sup>-8</sup>。这些突变率在重复DNA区域显著升高，其中片段重复的突变倾向取决于其长度与序列一致性百分比。本研究进一步表明，重复区域的突变富集主要发生在合子后阶段，可能源于DNA修复缺陷及基因座间转换机制异常。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Long-read sequencing improves sensitivity to discover variation in complex repetitive regions, assign parent-of-origin, and distinguish germline from postzygotic mutations. We applied Illumina, Oxford Nanopore Technologies, and PacBio sequencing to discover and validate de novo mutations in 73 children from 42 autism families (157 individuals). We assay 2.77 Gbp of the human genome, yielding on average 95 de novo mutations per transmission (87.5 single-nucleotide substitutions, 7.8 indels), with no significant difference in mutation rate or profile between probands and their unaffected siblings. Long reads increase de novo mutation discovery by 20-40% and double the mutations classified as early embryonic. The germline mutation rate is 1.30×10<sup>-8</sup> substitutions/base pair/generation; the postzygotic rate is 0.23×10<sup>-8</sup>. These rates are significantly increased in repetitive DNA, where segmental duplication mutability is dependent on length and percent identity. Here, we show that enrichment in repeats occurs predominantly postzygotically, likely resulting from faulty DNA repair and interlocus gene conversion.

</details>
<br>

**关键词**: long-read sequencing, de novo mutations, autism families, germline mutation rate, postzygotic mutation rate, repetitive DNA, segmental duplication, DNA repair

---

## Token 消耗统计

- **总计**: 253,068 tokens（输入 174,432 / 输出 78,636）
