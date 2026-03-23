# 📊 Nature Communications 研究报告 (2026-03-10)

> 生成时间: 2026-03-10 16:32:05
> 数据源: Nature Communications

> ⚠️ **注意**: 该数据源不支持PDF下载，仅提供评分和摘要翻译，无深度分析

## 📌 配置信息

### 关键词列表（共 3 个，总权重 3.0）

| 关键词 | 权重 | 类型 |
|--------|------|------|
| medical image analysis | 1.0 | 主要 |
| medical imaging | 1.0 | 主要 |
| deep learning medical imaging | 1.0 | 主要 |

### 评分设置

- **每个关键词最大分**: 10
- **及格分公式**: 5.0 + 3.0 × 总权重
- **当前及格分**: 14.0

## 📈 论文统计

- **总抓取**: 96 篇
- **及格论文**: 3 篇 (3.1%)
- **深度分析**: 3 篇

---

## ⭐ 及格论文详细分析

### 1. Contrast-free identification of glioma blood-brain barrier status via generative diffusion AI and no

**作者**: Kaiyi Zheng, Yiwen Zhang, Hai Shu, Ruhui Xiao, Chuan Peng, Jianhua Ma, Qianjin Feng, Yuankui Wu, Wei Yang, Liming Zhong
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69578-8](https://doi.org/10.1038/s41467-026-69578-8)

**评分**: 30.0 / 14.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 10.0/10 | 10.0 |
| medical imaging | 1.0 | 10.0/10 | 10.0 |
| deep learning medical imaging | 1.0 | 10.0/10 | 10.0 |

**评分理由**: 论文标题和摘要明确聚焦于医学影像分析（medical image analysis），具体研究非对比MRI图像处理，属于医学影像（medical imaging）领域；方法核心是生成扩散AI模型，属于深度学习在医学影像（deep learning medical imaging）的应用，因此所有关键词均高度相关，评分为10分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A contrast-free BBB status identification model (CBSI) is introduced that can identify BBB status with high accuracy using non-contrast MR images and generative diffusion AI networks and generalizability analysis indicates that CBSI can facilitate BBB status identification using synthetic T1Gd findings, avoiding GBCA adverse effects and streamlining clinical workflows.

!!! tip deepseek-chat TL;DR

    该研究提出了一种基于生成扩散AI和非对比MRI的对比剂无创血脑屏障状态识别模型（CBSI），在多个数据集上验证了其高准确性和泛化能力，并显著提升了胶质瘤分割和分级性能。

<details open>
<summary>摘要翻译</summary>

> 常规用于胶质瘤术前诊断及制定治疗策略的非增强磁共振成像，具备在不使用可能引发不良反应的钆基对比剂的前提下评估血脑屏障状态的潜力。此外，生成式人工智能模型能够从非增强图像合成对比增强图像。尽管存在这种潜力，肿瘤区域中钆基对比剂诱导特征的异质性以及合成不准确导致的误差累积，在很大程度上限制了传统生成模型的有效性。为解决这些局限性，我们提出了一种无对比剂的血脑屏障状态识别模型，该模型能够利用非增强磁共振图像和生成式扩散人工智能网络，高精度地识别血脑屏障状态。基于包含1,535名患者的多中心数据集进行训练和验证，该模型在外部测试集中取得了81.31%的曲线下面积，其性能超越了仅使用非增强磁共振的模型（曲线下面积 = 72.76%），并与T1Gd磁共振模型（曲线下面积 = 88.68%）的表现相当。此外，在两个公共数据集（BraTS-Africa和BraTS-GLI）上的验证支持了该模型在血脑屏障状态识别方面的泛化能力。值得注意的是，凭借合成T1Gd图像所提供的准确血脑屏障状态信息，胶质瘤分割与分级的性能相较于现有方法得到了显著提升。泛化性分析表明，该模型能够利用合成的T1Gd结果促进血脑屏障状态识别，从而避免钆基对比剂的不良反应并优化临床工作流程。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Non-contrast MRI, routinely used for the preoperative diagnosis of glioma tumors and establishing treatment strategies, provides the potential for assessing blood-brain barrier (BBB) status without using gadolinium-based contrast agents (GBCA) which could cause adverse events. Additionally, generative artificial intelligence (AI) models enable the synthesis of contrast-enhanced images from non-contrast images. Despite this potential, the heterogeneity of GBCA-induced features in tumor areas and error accumulation from inaccurate synthesis largely limit the efficacy of conventional generative models. To address these limitations, we introduce a contrast-free BBB status identification model (CBSI) that can identify BBB status with high accuracy using non-contrast MR images and generative diffusion AI networks. Trained and validated on a multi-center dataset of 1,535 patients, CBSI achieves an area under the curve (AUC) of 81.31%, surpassing the performance of the model using only non-contrast MR (AUC = 72.76%) and demonstrating comparable performance to the T1Gd MR model (AUC = 88.68%) in an external test set. Furthermore, validation on two public datasets (BraTS-Africa and BraTS-GLI) supports the generalizability of CBSI in BBB status identification. Notably, with accurate BBB status of synthetic T1Gd, the performance of glioma segmentation and grading is improved significantly compared to existing methods. Generalizability analysis indicates that CBSI can facilitate BBB status identification using synthetic T1Gd findings, avoiding GBCA adverse effects and streamlining clinical workflows.

</details>
<br>

**关键词**: glioma, blood-brain barrier, non-contrast MRI, generative diffusion AI, contrast-free identification, medical image analysis, deep learning, synthetic T1Gd

**深度分析**:

#### 基于生成扩散人工智能与非对比磁共振成像的无对比剂胶质瘤血脑屏障状态识别

**摘要**:

> 本研究针对胶质瘤诊断中依赖钆基对比剂（GBCA）评估血脑屏障（BBB）状态可能引发不良反应的问题，提出了一种无对比剂的BBB状态识别方法。研究背景在于非对比MRI常规用于胶质瘤术前诊断，但缺乏BBB状态信息；生成式AI虽能合成对比增强图像，但传统方法受肿瘤区域异质性和合成误差限制。为此，作者开发了CBSI模型，结合生成扩散AI网络与非对比MR图像，通过ET引导的生成模块合成具有准确BBB状态的T1Gd图像，并利用对比最大学习识别网络减少误差累积。在1535例患者的多中心数据集上验证，CBSI的AUC达81.31%，优于仅使用非对比MRI的模型（72.76%），并与真实T1Gd模型性能接近（88.68%）。外部测试显示模型具有良好的泛化能力，且合成T1Gd能显著提升胶质瘤分割和分级性能。结论表明，该方法可避免GBCA不良反应，优化临床工作流程。

**创新点**:
- 提出ET引导的生成扩散AI模型，通过增强类型标签合成具有特定BBB状态的T1Gd图像，以处理肿瘤区域的异质性增强特征
- 开发对比最大学习识别网络，利用合成T1Gd图像与非对比MRI区分伪阳性和阴性BBB状态，减少合成误差累积
- 在扩散模型中整合辅助肿瘤分割任务，增强语义感知能力，提升合成图像质量
- 实现无对比剂的BBB状态识别，避免钆基对比剂的潜在风险，如肾源性系统性纤维化和脑内钆沉积
- 通过多中心和大规模公共数据集验证，证明模型在胶质瘤分割和分级任务中的泛化性能提升

<details>
<summary>方法</summary>

!!! info

    研究采用合成-识别两阶段框架：首先，使用ET引导的生成扩散AI模型，以T1和T2-FLAIR非对比MRI为输入，合成带有BBB状态伪标签（完整或破坏）的T1Gd图像；该模型结合增强类型标签和肿瘤分割任务，学习异质性增强特征。其次，通过对比最大学习识别网络，基于合成T1Gd和非对比MRI确定真实BBB状态；该模块通过对比学习区分不同BBB状态，减少合成误差影响。技术路线包括数据预处理、模型训练（使用多中心数据集）、内部验证与外部测试（涉及独立数据集和公共挑战数据），并评估合成图像质量及下游任务性能。

</details>
<br>

**关键结果**:
- CBSI在BBB状态识别中AUC达81.31%，较仅使用非对比MRI的模型（AUC=72.76%）提升14.82%，接近真实T1Gd模型（AUC=88.68%）
- 在外部测试集（MR-2、BraTS-Africa、BraTS-GLI）上验证，模型表现出良好泛化能力，支持无对比剂BBB状态识别的临床应用
- 合成T1Gd图像质量优：全脑区域MAE为13.78±2.60，PSNR为26.51±2.30，SSIM为0.79±0.04；肿瘤区域MAE为22.38±10.87，SSIM为0.72±0.10
- 与SOTA合成方法（如Pix2pix、CycleGAN、DDPM）相比，CBSI在定量指标（如LPIPS、FID）和视觉细节上表现更佳
- 使用合成T1Gd后，胶质瘤分割和分级性能显著提升，优于现有方法

**技术栈**: 生成扩散AI网络（基于扩散模型）, ET引导模块（用于增强类型条件合成）, 对比最大学习识别网络（基于对比学习）, 3D ResNet18（用于分类任务）, 辅助肿瘤分割网络（整合于扩散模型中）, 评估指标：AUC、ACC、SEN、SPE、MAE、PSNR、SSIM、LPIPS、FID, 数据处理工具：多中心MRI数据集（包括T1、T2-FLAIR、T1Gd序列）, 优化方法：联合学习、误差减少策略

<details>
<summary>优点</summary>

- 创新性地结合生成扩散AI与对比学习，解决非对比MRI中BBB状态识别难题，避免对比剂使用风险
- 模型设计兼顾合成与识别，通过ET引导和分割任务提升合成准确性，减少误差传播
- 大规模多中心验证（1535例患者）和外部测试，结果稳健，泛化能力强
- 下游任务（如胶质瘤分割和分级）性能显著改善，体现临床实用价值
- 方法流程清晰，技术路线完整，从数据预处理到模型评估均有详细阐述

</details>
<br>

<details>
<summary>局限</summary>

- 模型性能虽接近真实T1Gd模型，但仍存在差距（AUC相差约7%），可能影响高精度临床决策
- 合成图像在肿瘤区域的细节还原仍有改进空间，如MAE在肿瘤区域较高（22.38±10.87）
- 研究依赖大规模标注数据，在数据稀缺场景中应用可能受限
- 未充分讨论模型在不同MRI设备或采集参数下的鲁棒性
- 计算复杂度较高，生成扩散模型训练和推理可能需较多资源，影响实时应用

</details>
<br>

**与研究方向的相关性**:

> 论文与'医学图像分析'高度相关：聚焦于胶质瘤的MRI图像处理，核心目标是通过AI技术从非对比MRI中识别BBB状态，涉及图像合成、分类和分割等典型医学图像分析任务。方法上整合生成式AI（扩散模型）和深度学习（对比学习、ResNet），直接应用于临床诊断场景，提升图像信息的利用效率，减少对对比剂的依赖，体现了医学图像分析在精准医疗中的前沿应用。

---

### 2. Bayesian machine learning enables discovery of risk factors for hepatosplenic multimorbidity related

**作者**: Yin-Cong Zhi, Victor Anguajibi, John Bosco Oryema, Betty Nabatte, Christopher K. Opio, Narcis B. Kabatereine, Goylette F. Chami
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69528-4](https://doi.org/10.1038/s41467-026-69528-4)

**评分**: 23.0 / 14.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical imaging | 1.0 | 9.0/10 | 9.0 |
| deep learning medical imaging | 1.0 | 6.0/10 | 6.0 |

**评分理由**: 论文使用B-mode超声（一种医学影像技术）评估肝脾疾病，属于医学影像分析范畴，因此与'medical image analysis'（8分）和'medical imaging'（9分）高度相关。虽然论文采用贝叶斯多任务学习框架（一种机器学习方法），但未明确使用深度学习技术，因此与'deep learning medical imaging'（6分）关联度中等。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种贝叶斯多任务学习框架，利用B超影像识别乌干达农村地区血吸虫病患者肝脾多病共存的危险因素，并发现了年龄、血红蛋白浓度和血吸虫性门静脉周围纤维化等关键风险因素。

<details open>
<summary>摘要翻译</summary>

> 全球每25例死亡中就有1例与肝脏疾病相关，且常伴有多种肝脾共病。然而，人们对肝脾共病的风险因素知之甚少，尤其是在慢性感染背景下。我们提出了一种新颖的贝叶斯多任务学习框架，对乌干达乡村地区血吸虫病流行队列（SchistoTrack）中3155名5-91岁个体通过床旁B型超声评估的45种肝脾疾病进行联合建模。我们识别了单一疾病及肝脾共病独特或共通的生物医学、社会经济和空间风险因素，并引入了量化疾病间依赖关系作为风险因素的测量方法。值得注意的是，对于胃食管静脉曲张，我们发现高龄、较低血红蛋白浓度和血吸虫性门脉周围纤维化是关键风险因素。我们的研究结果提供了风险因素汇编，可为疾病监测、分诊和随访提供依据，同时该模型能提升肝脾共病的预测能力，若在其他解剖系统验证，或可推广至普遍性共病预测。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> One in 25 deaths worldwide is related to liver disease, and often with multiple hepatosplenic conditions. Yet, little is understood of the risk factors for hepatosplenic multimorbidity, especially in the context of chronic infections. We present a novel Bayesian multitask learning framework to jointly model 45 hepatosplenic conditions assessed using point-of-care B-mode ultrasound for 3155 individuals aged 5-91 years within the SchistoTrack cohort across rural Uganda, where chronic intestinal schistosomiasis is endemic. We identify distinct and shared biomedical, socioeconomic, and spatial risk factors for individual conditions and hepatosplenic multimorbidity, and introduce methods for measuring condition dependencies as risk factors. Notably, for gastro-oesophageal varices, we discover key risk factors of older age, lower haemoglobin concentration, and schistosomal periportal fibrosis. Our findings provide a compendium of risk factors to inform surveillance, triage, and follow-up, while our model enables improved prediction of hepatosplenic multimorbidity, and if validated on other anatomical systems, general multimorbidity.

</details>
<br>

**关键词**: hepatosplenic multimorbidity, schistosomiasis, Bayesian multitask learning, B-mode ultrasound, risk factors, medical imaging, liver disease, point-of-care ultrasound

**深度分析**:

#### 贝叶斯机器学习助力发现血吸虫病相关肝脾多病共患风险因素

**摘要**:

> 本研究针对血吸虫病流行地区肝脾多病共患风险因素认知不足的问题，开发了一种新颖的贝叶斯多任务学习框架。研究背景是全球肝病相关死亡比例高，尤其在慢性感染背景下，肝脾多病共患的风险因素尚不明确。方法上，研究团队利用贝叶斯多任务学习架构，结合图网络编码疾病间的相互依赖关系，对乌干达农村地区SchistoTrack队列中3155名5-91岁个体的45种肝脾疾病状态（通过床旁B型超声评估）进行联合建模。研究整合了生物医学、社会经济和空间等多维度风险因素。结论显示，研究成功识别了各疾病特有及共享的风险因素，并量化了疾病间依赖关系作为风险因素的影响。特别针对指示门脉高压的胃食管静脉曲张，发现了年龄增长、血红蛋白浓度降低和血吸虫性门脉周围纤维化是关键风险因素。该模型不仅提供了风险因素汇编以指导监测、分诊和随访，还提升了肝脾多病共患的预测能力，并有望推广至其他解剖系统的多病共患研究。

**创新点**:
- 开发了新颖的贝叶斯多任务学习框架，用于联合建模多种肝脾疾病，克服了传统单一疾病研究的局限性。
- 引入图网络来编码和量化不同肝脾疾病状态之间的相互依赖关系，并将其参数化为风险因素。
- 首次在社区层面大规模应用床旁超声评估45种肝脾疾病，并结合广泛的生物医学、社会经济和空间变量进行风险因素探索。
- 针对血吸虫病流行区，系统研究了包括胃食管静脉曲张在内的危及生命的严重肝脾疾病的风险因素，填补了知识空白。
- 提出了通过组合似然比来分析肝纤维化模式（Niamey协议）与风险因素关联的新方法。

<details>
<summary>方法</summary>

!!! info

    研究采用贝叶斯多任务学习架构。技术路线包括：1) 数据收集：基于SchistoTrack社区队列，对3155名参与者进行床旁B型超声检查，依据WHO Niamey协议评估45种肝脾疾病状态，并收集广泛的协变量（临床、社会人口学和空间变量）。2) 模型构建：构建一个联合预测所有45种疾病的多任务学习模型。利用图（网络）来编码疾病间的依赖关系，模型参数根据节点连接性进行同质化，使得每种疾病可以从其他疾病的风险因素中学习。3) 统计分析：采用贝叶斯推断方法，计算后验优势比(OR)和95%可信区间(CI)来评估风险因素的显著性。进行了敏感性分析以检验先验选择的稳健性。4) 结果分析：识别个体疾病及多病共患的显著风险因素，特别关注胃食管静脉曲张等严重疾病，并分析疾病间依赖性的影响。

</details>
<br>

**关键结果**:
- 研究人群中有54%的个体患有两种或以上肝脾疾病，多病共患现象普遍。
- 血红蛋白浓度是信息量最大的测量指标，与11种（24.44%）疾病呈负相关，其中包括多种严重疾病。
- 年龄与29种（64.44%）疾病相关，且大多数呈正相关。
- 性别（女性）和职业（渔民）分别与6种疾病相关，女性多为保护因素，渔民多为风险因素。
- 针对胃食管静脉曲张，发现年龄每增加一岁，患病几率增加4%；对数转换的血红蛋白浓度每增加10%，患病几率降低22%。血吸虫性门脉周围纤维化是其关键风险因素。
- HIV、HBV共感染、性别和职业等因素对胃食管静脉曲张的影响显示出非零效应趋势，但未达到统计显著性。
- 空间因素（如居住地区）与多种疾病状态相关。
- 模型能够识别疾病间共享和特有的风险因素，并量化疾病依赖性作为风险因素的作用。

**技术栈**: 算法/模型：贝叶斯多任务学习框架，图网络模型, 统计/数学方法：贝叶斯推断，优势比(OR)分析，可信区间(CI)计算，似然比, 数据评估协议：WHO Niamey Protocol（用于肝纤维化模式分类）, 评估工具：点状护理B型超声, 软件/库：未在提供文本中明确提及，但通常涉及贝叶斯建模工具（如Stan, PyMC3）和机器学习库

<details>
<summary>优点</summary>

- 方法学创新性强：将贝叶斯机器学习与多任务学习、图网络结合，为多病共患研究提供了强大的分析框架。
- 研究设计全面：基于大规模社区队列，整合多模态数据（超声影像、临床、社会、空间），分析维度丰富。
- 临床意义重大：聚焦于资源有限地区被忽视的热带病及其严重并发症，研究成果可直接用于指导公共卫生实践，如风险分层和患者管理。
- 模型解释性好：贝叶斯方法提供了参数的不确定性度量（可信区间），结果更具说服力。
- 泛化潜力：作者指出该模型框架经过验证后可推广至其他解剖系统或更普遍的多病共患研究。

</details>
<br>

<details>
<summary>局限</summary>

- 数据局限性：研究基于乌干达特定地区的单一队列，结果的外推性（到其他血吸虫病流行区或非流行区）需要进一步验证。
- 横断面设计：主要揭示了关联关系，难以确定风险因素与疾病之间的因果关系。
- 未明确说明的细节：论文未详细描述图网络的具体构建方式、先验分布的具体选择以及模型比较和验证的细节（如与基准模型的对比）。
- 潜在未测量混杂因素：尽管考虑了众多变量，但仍可能存在未知或未测量的混杂因素影响结果。
- 计算复杂性：贝叶斯多任务学习模型可能计算成本较高，限制了在更大数据集或实时应用中的可扩展性。

</details>
<br>

**与研究方向的相关性**:

> 论文内容与研究关键词'Medical image analysis'高度相关，具体体现在：1) **核心数据来源**：研究依赖于对3155名个体进行的床旁B型超声检查，这是医学影像分析的直接应用。超声影像用于评估45种肝脾形态学条件，是风险因素发现的基石。2) **分析目标**：虽然最终输出是风险因素模型，但模型的输入特征严重依赖于对超声影像的定量和定性分析（如肝纤维化模式分类、器官测量等）。3) **方法交叉**：研究采用的贝叶斯机器学习框架是处理高维、复杂医学影像数据衍生特征的先进分析方法。因此，医学影像分析不仅是数据获取手段，也是驱动整个研究发现的关键技术环节。

---

### 3. Dual deconvolution in multiphoton structured illumination microscopy for deep-tissue super-resolutio

**作者**: Sumin Lim, Youngho Jin, Jin Hee Hong, Young-Ho Jin, Kalpak Gupta, Moonseok Kim, Suhyun Kim, Sumin Lim, S Yoon
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-69798-y](https://doi.org/10.1038/s41467-026-69798-y)

**评分**: 19.0 / 14.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical imaging | 1.0 | 9.0/10 | 9.0 |
| deep learning medical imaging | 1.0 | 2.0/10 | 2.0 |

**评分理由**: 论文专注于医学成像技术，特别是多光子结构照明显微镜在深层组织超分辨率成像中的应用，与'medical image analysis'和'medical imaging'高度相关。然而，论文主要采用计算自适应光学和双反卷积算法，未涉及深度学习技术，因此与'deep learning medical imaging'相关性较低。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A cost-effective and accessible alternative to hardware-based AO for multiphoton structured illumination microscopy, enabling deep-tissue super-resolution imaging with minimal hardware modifications and expanding the potential for high-resolution deep-tissue imaging in biological research.

!!! tip deepseek-chat TL;DR

    该研究解决了厚生物组织中样本诱导像差导致成像分辨率下降的问题，通过计算自适应光学框架和双反卷积算法，在180微米深的小鼠脑组织中实现了130纳米的横向超分辨率成像。

<details open>
<summary>摘要翻译</summary>

> 厚生物组织成像常因样本诱导的像差而质量下降，这些像差会降低分辨率与对比度，在超分辨率技术中尤为明显。虽然基于硬件的自适应光学（AO）技术可通过波前整形校正此类像差，但其系统复杂性与高昂成本阻碍了广泛应用。本文提出一种用于多光子结构光照明显微镜的计算自适应光学框架，仅需最小限度的硬件改造即可实现深层组织超分辨率成像。通过将传统激光扫描多光子显微镜的光电探测器替换为相机，我们捕获了一系列扫描图像。利用虚拟结构光照，我们开发了一种双重解卷积算法，可独立校正激发与发射像差，从而恢复具有扩展空间频率带宽的无像差物体频谱。我们通过双光子超分辨率成像实验验证了该框架，在厚小鼠脑组织180微米深度处实现了130纳米的横向分辨率——相当于发射波长的四分之一，而传统解卷积方法在此条件下无法保持超分辨率能力。该方法为基于硬件的自适应光学提供了一种经济高效且易于实施的替代方案，拓展了生物学研究中高分辨率深层组织成像的应用潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Imaging in thick biological tissues is often degraded by sample-induced aberrations, which reduce resolution and contrast, particularly in super-resolution techniques. While hardware-based adaptive optics (AO) using wavefront shaping can correct these aberrations, their complexity and cost hinder widespread adoption. Here, we present a computational AO framework for multiphoton structured illumination microscopy, enabling deep-tissue super-resolution imaging with minimal hardware modifications. By replacing the photodetector with a camera from the conventional laser-scanning multiphoton microscope, we capture a sequence of scanned images. Using virtual structured illumination, we develop a dual deconvolution algorithm that independently corrects excitation and emission aberrations, recovering an aberration-free object spectrum with an extended spatial frequency bandwidth. We experimentally validate this framework through two-photon super-resolution imaging, achieving a lateral resolution of 130 nm-one-fourth of the emission wavelength-at a depth of 180 μm in thick mouse brain tissue, where conventional deconvolution fails to maintain super-resolution capability. This approach provides a cost-effective and accessible alternative to hardware-based AO, expanding the potential for high-resolution deep-tissue imaging in biological research.

</details>
<br>

**关键词**: multiphoton structured illumination microscopy, deep-tissue super-resolution imaging, computational adaptive optics, dual deconvolution algorithm, aberration correction, biological tissue imaging, two-photon super-resolution

**深度分析**:

#### 多光子结构光照明显微镜中的双重反卷积用于深层组织超分辨率成像

**摘要**:

> 本研究针对厚生物组织中样本诱导像差导致超分辨率成像质量下降的问题，提出了一种计算自适应光学框架。该方法基于多光子虚拟结构照明，通过将传统激光扫描多光子显微镜的探测器替换为相机，捕获扫描图像序列。研究开发了双重反卷积算法，能够独立校正激发和发射路径的像差，恢复无像差的物体频谱并扩展空间频率带宽。实验验证表明，在180微米深的小鼠脑组织中实现了130纳米的横向分辨率（发射波长的四分之一），而传统反卷积方法在此条件下无法保持超分辨率能力。该框架为硬件自适应光学提供了成本效益高且易于实现的替代方案。

**创新点**:
- 提出计算自适应光学框架，无需复杂硬件修改即可校正深层组织像差
- 开发双重反卷积算法，独立处理激发和发射路径的像差
- 实现多光子虚拟结构照明，线性化像差校正问题
- 在180微米深度达到130纳米分辨率，超越传统方法极限
- 提供硬件自适应光学的低成本替代方案

<details>
<summary>方法</summary>

!!! info

    研究采用图像扫描显微镜配置，将积分探测器替换为相机。通过点扫描获取荧光强度图f(rd,ri)，利用虚拟结构照明Iill(ri)=e^{iki·ri}生成宽场荧光图像。在空间频率域中，通过频谱合成扩展带宽。核心创新是双重反卷积算法，通过矩阵分解独立校正激发PSF(hex)和发射PSF(hem)，而非使用单一有效PSF。算法在傅里叶域中处理，通过独立补偿两个PSF的像差来恢复物体频谱。

</details>
<br>

**关键结果**:
- 在180微米深的小鼠脑组织中实现130纳米横向分辨率
- 分辨率达到发射波长的四分之一，突破衍射极限
- 双重反卷积在强像差条件下优于传统反卷积方法
- 成功可视化小鼠脑组织中的树突棘结构
- 验证了计算自适应光学在深层组织成像中的可行性

**技术栈**: 双重反卷积算法, 多光子虚拟结构照明, 傅里叶变换与频谱合成, 矩阵分解方法, 图像扫描显微镜技术, 两光子荧光显微镜

<details>
<summary>优点</summary>

- 无需昂贵硬件修改，成本效益高
- 独立校正激发和发射像差，提高校正精度
- 在深层组织中实现超分辨率成像
- 算法鲁棒性强，适用于强像差条件
- 与现有显微镜系统兼容性好

</details>
<br>

<details>
<summary>局限</summary>

- 主要验证于两光子成像，其他多光子模式需进一步验证
- 计算复杂度较高，可能影响实时成像
- 实验验证组织类型相对有限
- 与硬件自适应光学相比，校正能力可能有理论极限
- 需要准确的PSF模型假设

</details>
<br>

**与研究方向的相关性**:

> 本研究与医学图像分析高度相关：1）针对生物医学成像中的关键挑战——深层组织成像，提供解决方案；2）开发的超分辨率成像技术可直接应用于病理组织分析和细胞结构研究；3）计算成像方法为医学图像处理提供了新思路；4）在神经科学（小鼠脑组织成像）中有直接应用价值；5）算法框架可扩展至其他医学成像模态。

---

## 📋 所有论文列表

### 1. ✅ Contrast-free identification of glioma blood-brain barrier status via generative diffusion AI and non-contrast MRI

**作者**: Kaiyi Zheng, Yiwen Zhang, Hai Shu, Ruhui Xiao, Chuan Peng, Jianhua Ma, Qianjin Feng, Yuankui Wu, Wei Yang, Liming Zhong
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69578-8](https://doi.org/10.1038/s41467-026-69578-8)

**评分**: 30.0 / 14.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 10.0/10 | 10.0 |
| medical imaging | 1.0 | 10.0/10 | 10.0 |
| deep learning medical imaging | 1.0 | 10.0/10 | 10.0 |

**评分理由**: 论文标题和摘要明确聚焦于医学影像分析（medical image analysis），具体研究非对比MRI图像处理，属于医学影像（medical imaging）领域；方法核心是生成扩散AI模型，属于深度学习在医学影像（deep learning medical imaging）的应用，因此所有关键词均高度相关，评分为10分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A contrast-free BBB status identification model (CBSI) is introduced that can identify BBB status with high accuracy using non-contrast MR images and generative diffusion AI networks and generalizability analysis indicates that CBSI can facilitate BBB status identification using synthetic T1Gd findings, avoiding GBCA adverse effects and streamlining clinical workflows.

!!! tip deepseek-chat TL;DR

    该研究提出了一种基于生成扩散AI和非对比MRI的对比剂无创血脑屏障状态识别模型（CBSI），在多个数据集上验证了其高准确性和泛化能力，并显著提升了胶质瘤分割和分级性能。

<details open>
<summary>摘要翻译</summary>

> 常规用于胶质瘤术前诊断及制定治疗策略的非增强磁共振成像，具备在不使用可能引发不良反应的钆基对比剂的前提下评估血脑屏障状态的潜力。此外，生成式人工智能模型能够从非增强图像合成对比增强图像。尽管存在这种潜力，肿瘤区域中钆基对比剂诱导特征的异质性以及合成不准确导致的误差累积，在很大程度上限制了传统生成模型的有效性。为解决这些局限性，我们提出了一种无对比剂的血脑屏障状态识别模型，该模型能够利用非增强磁共振图像和生成式扩散人工智能网络，高精度地识别血脑屏障状态。基于包含1,535名患者的多中心数据集进行训练和验证，该模型在外部测试集中取得了81.31%的曲线下面积，其性能超越了仅使用非增强磁共振的模型（曲线下面积 = 72.76%），并与T1Gd磁共振模型（曲线下面积 = 88.68%）的表现相当。此外，在两个公共数据集（BraTS-Africa和BraTS-GLI）上的验证支持了该模型在血脑屏障状态识别方面的泛化能力。值得注意的是，凭借合成T1Gd图像所提供的准确血脑屏障状态信息，胶质瘤分割与分级的性能相较于现有方法得到了显著提升。泛化性分析表明，该模型能够利用合成的T1Gd结果促进血脑屏障状态识别，从而避免钆基对比剂的不良反应并优化临床工作流程。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Non-contrast MRI, routinely used for the preoperative diagnosis of glioma tumors and establishing treatment strategies, provides the potential for assessing blood-brain barrier (BBB) status without using gadolinium-based contrast agents (GBCA) which could cause adverse events. Additionally, generative artificial intelligence (AI) models enable the synthesis of contrast-enhanced images from non-contrast images. Despite this potential, the heterogeneity of GBCA-induced features in tumor areas and error accumulation from inaccurate synthesis largely limit the efficacy of conventional generative models. To address these limitations, we introduce a contrast-free BBB status identification model (CBSI) that can identify BBB status with high accuracy using non-contrast MR images and generative diffusion AI networks. Trained and validated on a multi-center dataset of 1,535 patients, CBSI achieves an area under the curve (AUC) of 81.31%, surpassing the performance of the model using only non-contrast MR (AUC = 72.76%) and demonstrating comparable performance to the T1Gd MR model (AUC = 88.68%) in an external test set. Furthermore, validation on two public datasets (BraTS-Africa and BraTS-GLI) supports the generalizability of CBSI in BBB status identification. Notably, with accurate BBB status of synthetic T1Gd, the performance of glioma segmentation and grading is improved significantly compared to existing methods. Generalizability analysis indicates that CBSI can facilitate BBB status identification using synthetic T1Gd findings, avoiding GBCA adverse effects and streamlining clinical workflows.

</details>
<br>

**关键词**: glioma, blood-brain barrier, non-contrast MRI, generative diffusion AI, contrast-free identification, medical image analysis, deep learning, synthetic T1Gd

---

### 2. ✅ Bayesian machine learning enables discovery of risk factors for hepatosplenic multimorbidity related to schistosomiasis

**作者**: Yin-Cong Zhi, Victor Anguajibi, John Bosco Oryema, Betty Nabatte, Christopher K. Opio, Narcis B. Kabatereine, Goylette F. Chami
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69528-4](https://doi.org/10.1038/s41467-026-69528-4)

**评分**: 23.0 / 14.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical imaging | 1.0 | 9.0/10 | 9.0 |
| deep learning medical imaging | 1.0 | 6.0/10 | 6.0 |

**评分理由**: 论文使用B-mode超声（一种医学影像技术）评估肝脾疾病，属于医学影像分析范畴，因此与'medical image analysis'（8分）和'medical imaging'（9分）高度相关。虽然论文采用贝叶斯多任务学习框架（一种机器学习方法），但未明确使用深度学习技术，因此与'deep learning medical imaging'（6分）关联度中等。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种贝叶斯多任务学习框架，利用B超影像识别乌干达农村地区血吸虫病患者肝脾多病共存的危险因素，并发现了年龄、血红蛋白浓度和血吸虫性门静脉周围纤维化等关键风险因素。

<details open>
<summary>摘要翻译</summary>

> 全球每25例死亡中就有1例与肝脏疾病相关，且常伴有多种肝脾共病。然而，人们对肝脾共病的风险因素知之甚少，尤其是在慢性感染背景下。我们提出了一种新颖的贝叶斯多任务学习框架，对乌干达乡村地区血吸虫病流行队列（SchistoTrack）中3155名5-91岁个体通过床旁B型超声评估的45种肝脾疾病进行联合建模。我们识别了单一疾病及肝脾共病独特或共通的生物医学、社会经济和空间风险因素，并引入了量化疾病间依赖关系作为风险因素的测量方法。值得注意的是，对于胃食管静脉曲张，我们发现高龄、较低血红蛋白浓度和血吸虫性门脉周围纤维化是关键风险因素。我们的研究结果提供了风险因素汇编，可为疾病监测、分诊和随访提供依据，同时该模型能提升肝脾共病的预测能力，若在其他解剖系统验证，或可推广至普遍性共病预测。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> One in 25 deaths worldwide is related to liver disease, and often with multiple hepatosplenic conditions. Yet, little is understood of the risk factors for hepatosplenic multimorbidity, especially in the context of chronic infections. We present a novel Bayesian multitask learning framework to jointly model 45 hepatosplenic conditions assessed using point-of-care B-mode ultrasound for 3155 individuals aged 5-91 years within the SchistoTrack cohort across rural Uganda, where chronic intestinal schistosomiasis is endemic. We identify distinct and shared biomedical, socioeconomic, and spatial risk factors for individual conditions and hepatosplenic multimorbidity, and introduce methods for measuring condition dependencies as risk factors. Notably, for gastro-oesophageal varices, we discover key risk factors of older age, lower haemoglobin concentration, and schistosomal periportal fibrosis. Our findings provide a compendium of risk factors to inform surveillance, triage, and follow-up, while our model enables improved prediction of hepatosplenic multimorbidity, and if validated on other anatomical systems, general multimorbidity.

</details>
<br>

**关键词**: hepatosplenic multimorbidity, schistosomiasis, Bayesian multitask learning, B-mode ultrasound, risk factors, medical imaging, liver disease, point-of-care ultrasound

---

### 3. ✅ Dual deconvolution in multiphoton structured illumination microscopy for deep-tissue super-resolution imaging

**作者**: Sumin Lim, Youngho Jin, Jin Hee Hong, Young-Ho Jin, Kalpak Gupta, Moonseok Kim, Suhyun Kim, Sumin Lim, S Yoon
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-69798-y](https://doi.org/10.1038/s41467-026-69798-y)

**评分**: 19.0 / 14.0 ✅

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 8.0/10 | 8.0 |
| medical imaging | 1.0 | 9.0/10 | 9.0 |
| deep learning medical imaging | 1.0 | 2.0/10 | 2.0 |

**评分理由**: 论文专注于医学成像技术，特别是多光子结构照明显微镜在深层组织超分辨率成像中的应用，与'medical image analysis'和'medical imaging'高度相关。然而，论文主要采用计算自适应光学和双反卷积算法，未涉及深度学习技术，因此与'deep learning medical imaging'相关性较低。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A cost-effective and accessible alternative to hardware-based AO for multiphoton structured illumination microscopy, enabling deep-tissue super-resolution imaging with minimal hardware modifications and expanding the potential for high-resolution deep-tissue imaging in biological research.

!!! tip deepseek-chat TL;DR

    该研究解决了厚生物组织中样本诱导像差导致成像分辨率下降的问题，通过计算自适应光学框架和双反卷积算法，在180微米深的小鼠脑组织中实现了130纳米的横向超分辨率成像。

<details open>
<summary>摘要翻译</summary>

> 厚生物组织成像常因样本诱导的像差而质量下降，这些像差会降低分辨率与对比度，在超分辨率技术中尤为明显。虽然基于硬件的自适应光学（AO）技术可通过波前整形校正此类像差，但其系统复杂性与高昂成本阻碍了广泛应用。本文提出一种用于多光子结构光照明显微镜的计算自适应光学框架，仅需最小限度的硬件改造即可实现深层组织超分辨率成像。通过将传统激光扫描多光子显微镜的光电探测器替换为相机，我们捕获了一系列扫描图像。利用虚拟结构光照，我们开发了一种双重解卷积算法，可独立校正激发与发射像差，从而恢复具有扩展空间频率带宽的无像差物体频谱。我们通过双光子超分辨率成像实验验证了该框架，在厚小鼠脑组织180微米深度处实现了130纳米的横向分辨率——相当于发射波长的四分之一，而传统解卷积方法在此条件下无法保持超分辨率能力。该方法为基于硬件的自适应光学提供了一种经济高效且易于实施的替代方案，拓展了生物学研究中高分辨率深层组织成像的应用潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Imaging in thick biological tissues is often degraded by sample-induced aberrations, which reduce resolution and contrast, particularly in super-resolution techniques. While hardware-based adaptive optics (AO) using wavefront shaping can correct these aberrations, their complexity and cost hinder widespread adoption. Here, we present a computational AO framework for multiphoton structured illumination microscopy, enabling deep-tissue super-resolution imaging with minimal hardware modifications. By replacing the photodetector with a camera from the conventional laser-scanning multiphoton microscope, we capture a sequence of scanned images. Using virtual structured illumination, we develop a dual deconvolution algorithm that independently corrects excitation and emission aberrations, recovering an aberration-free object spectrum with an extended spatial frequency bandwidth. We experimentally validate this framework through two-photon super-resolution imaging, achieving a lateral resolution of 130 nm-one-fourth of the emission wavelength-at a depth of 180 μm in thick mouse brain tissue, where conventional deconvolution fails to maintain super-resolution capability. This approach provides a cost-effective and accessible alternative to hardware-based AO, expanding the potential for high-resolution deep-tissue imaging in biological research.

</details>
<br>

**关键词**: multiphoton structured illumination microscopy, deep-tissue super-resolution imaging, computational adaptive optics, dual deconvolution algorithm, aberration correction, biological tissue imaging, two-photon super-resolution

---

### 4. ❌ Atomic imaging for hydrogen and boron aggregates in boron-doped diamond by spectro-photoelectron holography

**作者**: Hiroto Tomita, Wataru Hosoda, Takumi Taniguchi, Hirokazu Fujiwara, Noriyuki Kataoka, Taisuke Kageura, Yoshihiko Takano, Hiroshi Kawarada, Koji Tsuda, T. Yokoya, T. Matsushita
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70231-7](https://doi.org/10.1038/s41467-026-70231-7)

**评分**: 4.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 2.0/10 | 2.0 |
| medical imaging | 1.0 | 2.0/10 | 2.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是利用光谱光电子全息技术对硼掺杂金刚石薄膜中的硼和氢原子聚集进行原子级成像，属于材料科学和凝聚态物理领域。虽然涉及成像技术，但这是原子尺度的物理成像，而非医学图像分析。关键词'medical image analysis'和'medical imaging'与论文内容仅有微弱关联（因为都涉及成像技术），但论文完全不涉及医学应用或生物组织成像。关键词'deep learning medical imaging'则完全无关，因为论文未使用深度学习或任何机器学习方法。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究利用光谱光电子全息技术首次在原子尺度上成像并识别了硼掺杂金刚石中导致电学性能下降的硼二聚体和硼-氢复合物结构，揭示了氢在生长过程中钝化硼受主的具体机制。

<details open>
<summary>摘要翻译</summary>

> 金刚石的电学特性可通过杂质掺杂进行调控。孤立的替位硼原子会引入空穴；然而，在较高掺杂浓度下，电学非活性硼原子的比例会增加。这一现象通常归因于硼的聚集和氢钝化，尽管基于原子排列的结构识别尚未得到实验验证。本文通过利用光谱光电子全息技术分析硼的原子环境，揭示了同质外延生长硼掺杂金刚石薄膜中多种化学态的起源。我们的分析识别出硼二聚体及硼-氢复合物，其中氢占据不同的原子位点并产生不同的化学位移。这些结果表明，生长过程中的氢掺入导致了硼受主的钝化。我们证明，光电子全息技术是一种可用于氢成像以及确定掺杂剂原子位点的有前景的工具。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The electrical properties of diamond are modulated by impurity doping. Isolated substitutional boron atoms introduce holes; however, the fraction of electrically inactive boron atoms increases at higher doping concentrations. This has been attributed to boron aggregation and hydrogen passivation, although their structural identification based on atomic arrangement has yet to be experimentally verified. Here we show the origin of multiple chemical states in homoepitaxially grown boron-doped diamond thin films by analyzing the atomic environment of boron using spectro-photoelectron holography. Our analysis identifies boron dimers and boron-hydrogen complexes, with hydrogen occupying different atomic sites that give rise to distinct chemical shifts. These results suggest that hydrogen incorporation during growth leads to passivation of boron acceptors. We demonstrate that photoelectron holography serves as a promising tool for imaging hydrogen as well as determining the atomic sites of dopants.

</details>
<br>

**关键词**: boron-doped diamond, spectro-photoelectron holography, atomic imaging, hydrogen passivation, boron aggregation, dopant atomic sites, chemical states, homoepitaxial thin films

---

### 5. ❌ Genetic variations interact with polybrominated diphenyl ether exposure to alter lipid homeostasis

**作者**: Naifan Hu, Bin Li, Yifu Lu, Qi Jiang, Ying Zhu, Zheng Li, Yingli Qu, Tian Qiu, Donghui Zhang, Zhuo Wang, Yunfei Ma, Huibin Jin, Peijie Sun, Haocan Song, Yunhao Zhao, Yifan Zhao (659636), MING SEN ZHANG, Feng Zhao, Saisai Ji, Bifeng Yuan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70222-8](https://doi.org/10.1038/s41467-026-70222-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是环境污染物PBDEs与遗传变异相互作用对脂质代谢的影响，涉及暴露组学、基因组学、代谢组学分析，以及CRISPR/Cas9功能验证。全文未涉及医学影像分析、医学成像或深度学习在医学影像中的应用，与所有评分关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A gene-environment interaction mechanism through which genetic variants modulate lipid metabolism in response to PBDE exposure is elucidated, which significantly enhances dyslipidemia prediction in highly exposed individuals.

!!! tip deepseek-chat TL;DR

    该研究揭示了遗传变异如何与多溴联苯醚暴露相互作用，通过影响SLC6A20表达和甘氨酸转运来调节脂质代谢，从而增加血脂异常风险。

<details open>
<summary>摘要翻译</summary>

> 多溴联苯醚（PBDEs）与血脂异常相关，但个体易感性的分子基础尚不明确。本研究基于中国国家人体生物监测队列，通过整合暴露组、基因组和代谢组数据，识别出3,571个与PBDE暴露相互作用并影响血脂异常风险的遗传变异。代谢组分析提示甘氨酸和甘油磷酸是关键介导因子。基于这些PBDE交互变异构建的多基因风险评分显著提升了高暴露个体中血脂异常的预测效能。其中，rs9869609被确定为候选因果变异，其与高胆固醇血症风险关联最强（β = 1.18，错误发现率FDR = 0.0078）。通过单碱基CRISPR/Cas9编辑进行的功能验证进一步揭示，rs9869609-G等位基因通过增强BHLHE40结合而下调SLC6A20表达，进而损害甘氨酸转运并促进胆固醇积累，这一效应在2,2',4,4'-四溴联苯醚暴露环境下尤为显著。综上，本研究阐明了一种基因-环境交互作用机制，即遗传变异通过该机制调控脂质代谢以响应PBDE暴露。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Polybrominated diphenyl ethers (PBDEs) are implicated in dyslipidemia, but the molecular basis of individual susceptibility remains elusive. Here we report an analysis based on the China National Human Biomonitoring cohort, where we integrate exposome, genomic, and metabolomic data to identify 3,571 genetic variants that interact with PBDE exposure to influence dyslipidemia risk. Metabolomic analysis highlights glycine and glycerophosphate as key mediators. A polygenic risk score derived from these PBDE-interactive variants significantly enhances dyslipidemia prediction in highly exposed individuals. Among these, rs9869609 emerges as a candidate causal variant, showing the strongest association with hypercholesterolemia risk (β = 1.18, FDR = 0.0078). Further functional validation using single-base CRISPR/Cas9 editing reveals that the rs9869609-G allele downregulates SLC6A20 expression by strengthening BHLHE40 binding, which further impairs glycine transport and promotes cholesterol accumulation, particularly under 2,2',4,4'-Tetrabromodiphenyl ether exposure. Collectively, our study elucidates a gene-environment interaction mechanism through which genetic variants modulate lipid metabolism in response to PBDE exposure.

</details>
<br>

**关键词**: polybrominated diphenyl ethers, genetic variants, dyslipidemia, gene-environment interaction, lipid metabolism, CRISPR/Cas9, SLC6A20, glycine transport

---

### 6. ❌ Altering the carbohydrate-binding specificity of the legume lectin FRIL through structure-guided engineering

**作者**: Yo-Min Liu, Hong Thuy Vy Nguyen, Xiaorui Chen, Md. Shahed-Al-Mahmud, Ting-Hua Chen, Kuo-Shiang Liao, Jennifer M. Lo, Tzu-Chun Kan, Chien-Tai Ren, Che Ma
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70188-7](https://doi.org/10.1038/s41467-026-70188-7)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是豆科植物凝集素FRIL的碳水化合物结合特异性，通过结构引导工程改变其识别复杂N-聚糖的能力。研究涉及蛋白质工程、结构生物学（cryo-EM）、糖生物学和病毒学，但完全不涉及医学图像分析、医学成像或深度学习医学成像。论文内容与评分关键词的领域（医学图像处理）无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown legume lectin carbohydrate recognition domain (CRD) loop B is the main determinant of complex versus high-mannose N-glycan specificity in FRIL and Concanavalin A (ConA), respectively and the crucial role that loop B residues play in establishing oligosaccharide specificity is demonstrated.

!!! tip deepseek-chat TL;DR

    该研究通过结构引导工程揭示了豆科植物凝集素FRIL中loop B残基在决定复杂N-聚糖特异性中的关键作用，并成功构建了只识别高甘露糖N-聚糖的FRIL突变体。

<details open>
<summary>摘要翻译</summary>

> FRIL是一种来自扁豆的豆科植物凝集素，具有广谱抗病毒活性。在与甘露糖/葡萄糖特异性豆科凝集素的同类蛋白中，FRIL的显著特征在于其对复杂型N-聚糖的特异性识别。我们推测FRIL上延伸的结合位点促成了这种配体选择性。本文研究表明，豆科植物凝集素的碳水化合物识别结构域（CRD）B环分别是决定FRIL与伴刀豆球蛋白A（ConA）对复杂型或高甘露糖型N-聚糖选择性的关键因素。首先，我们发现重组FRIL（rFRIL）与前体proConA（rproConA）的非活性形式可通过去糖基化被激活。其次，我们解析了非活性apo rFRIL、活性FRIL与Galβ1,4-(Fucα1,3-)GlcNAcβ1,2-Man四糖复合物，以及活性rFRIL与甘露糖九聚体GlcNAc二聚体（Man9）N-聚糖复合物的冷冻电镜结构，并确定B环上的H102和Y101残基是识别复杂聚糖的关键位点。最后，我们将FRIL的B环101-102位点及C环145位点替换为ConA中的对应残基，获得了仅特异性结合高甘露糖型N-聚糖的FRIL突变体。综上所述，我们建立了通过去糖基化激活重组FRIL及相关凝集素的方法，并证实了B环残基在确立寡糖特异性中的决定性作用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> FRIL is a legume lectin from the hyacinth bean that has broad-spectrum antiviral activity. A distinctive trait of FRIL among similar mannose/glucose-specific legume lectins is that FRIL shows specificity for complex type N-glycans. We postulate that an extended binding site on FRIL facilitates this ligand selectivity. Here, we show legume lectin carbohydrate recognition domain (CRD) loop B is the main determinant of complex versus high-mannose N-glycan specificity in FRIL and Concanavalin A (ConA), respectively. First, we find that the inactive precursors of recombinant FRIL (rFRIL) and proConA (rproConA) can be activated via deglycosylation. Secondly, the cryo-EM structures of inactive apo rFRIL, active FRIL in complex with Galβ1,4-(Fucα1,3-)GlcNAcβ1,2-Man tetrasaccharide, and active rFRIL in complex with Mannose<sub>9</sub>GlcNAc<sub>2</sub> (Man9) N-glycan are determined, and residues H102 and Y101 on loop B are identified as crucial for complex glycan recognition. Finally, we swapped loop B residues 101 and 102 alongside loop C residue 145 on FRIL to their structural equivalent on ConA, resulting in a FRIL mutant that binds exclusively to high mannose N-glycans. Taken together, we have established a process of activating recombinant FRIL and related lectins through deglycosylation, and demonstrated the crucial role that loop B residues play in establishing oligosaccharide specificity.

</details>
<br>

**关键词**: FRIL, legume lectin, carbohydrate-binding specificity, N-glycans, cryo-EM structure, loop B, protein engineering, Concanavalin A

---

### 7. ❌ FeCu dual-single-atom catalyst promotes gradient H2O2 activation for enhanced methane oxidation to methanol

**作者**: Haonan Zhang, Shuai Wang, Yang Li, Hongjie Qin, Mingwang Wang, Qinghai Chen, Boshi Zheng, Shuxu Zhu, Pengye Zhang, Chaoqun Gu, Yunyun Li, Qi Hua, Mingbo Wu, Wenting Wu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70179-8](https://doi.org/10.1038/s41467-026-70179-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是化学催化领域，具体涉及双单原子催化剂（FeCu/ZSM-CI）用于甲烷选择性氧化制甲醇，通过空间构型调控H2O2活化梯度。全文内容围绕催化剂设计、反应机理、选择性氧化等化学工程主题，未涉及任何医学图像分析、医学成像或深度学习在医学成像中的应用。因此，所有关键词与论文内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了通过空间分离的Fe-Cu双单原子催化剂调控H2O2活化梯度，实现了甲烷高选择性氧化制甲醇，获得了20.2 mmol gcat-1 h-1的甲醇产率和90.1%的选择性。

<details open>
<summary>摘要翻译</summary>

> 过氧化氢是一种极具吸引力且可持续的氧化剂，但其在惰性烷烃氧化中的有效应用受到限制，原因在于难以精确匹配所生成氧物种的分布、浓度及反应活性与底物活化需求。本文报道了一种双单原子催化剂FeCu/ZSM-CI，其中原子级分散的Fe和Cu在ZSM-5的微孔骨架内空间分离：Fe位于孔道内部，而Cu位于外表面，从而实现了对H<sub>2</sub>O<sub>2</sub>活化梯度的调控。这种空间构型诱导了差异化活性氧物种的演化：内部生成的高价Fe=O和•OOH物种将甲烷活化为CH<sub>3</sub>OOH，而表面的Cu位点则选择性将CH<sub>3</sub>OOH转化为甲醇，从而抑制了过度氧化路径。优化后的FeCu/ZSM-CI催化剂实现了20.2 mmol g<sub>cat</sub><sup>-1</sup> h<sup>-1</sup>的甲醇产率，选择性达90.1%，且H<sub>2</sub>O<sub>2</sub>利用效率高达74.6%。结合动力学同位素效应、捕获剂实验、原位电子顺磁共振（EPR）/漫反射傅里叶变换红外光谱（DRIFTS）及密度泛函理论（DFT）计算的机理研究表明，Fe-Cu协同作用将决速步从H<sub>2</sub>O<sub>2</sub>活化转移至C-H键活化。这些发现确立了一种通过空间构型驱动协同效应来调控活性氧物种空间分布的普适性策略及可迁移的设计原则，为设计在温和条件下实现选择性碳氢化合物氧化的先进催化剂提供了新见解。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Hydrogen peroxide is an attractive and sustainable oxidant, yet its effective application in inert alkane oxidation is limited by the inability to precisely match the distribution, concentration, and reactivity of generated oxygen species with substrate activation requirements. Herein, a dual single-atom catalyst, FeCu/ZSM-CI, in which atomically dispersed Fe and Cu are spatially separated within the microporous framework of ZSM-5, with Fe located in the inner channels and Cu on the external surface, thereby enabling a controlled H<sub>2</sub>O<sub>2</sub> activation gradient. This spatial configuration induces differentiated reactive oxygen species evolution: high-valent Fe=O and •OOH species form in the interior to activate methane into CH<sub>3</sub>OOH, while surface Cu sites selectively convert CH<sub>3</sub>OOH into methanol, mitigating overoxidation pathways. The optimized FeCu/ZSM-CI catalyst achieves a methanol yield of 20.2 mmol g<sub>cat</sub><sup>-1</sup> h<sup>-1</sup> with 90.1% selectivity and a remarkable H<sub>2</sub>O<sub>2</sub> utilization efficiency of 74.6%. Mechanistic studies combining kinetic isotope effects, scavenger assays, in-situ EPR/DRIFTS, and DFT calculations reveal that Fe-Cu synergy shifts the rate-determining step from H<sub>2</sub>O<sub>2</sub> activation to C-H bond activation. These findings establish a generalizable strategy for manipulating ROS spatial distribution via spatial-configuration-driven synergy and a transferable design principle, offering new insights for designing advanced catalysts for selective hydrocarbon oxidation under ambient conditions.

</details>
<br>

**关键词**: dual single-atom catalyst, methane oxidation, methanol production, H2O2 activation, selective oxidation, Fe-Cu synergy, spatial configuration, reactive oxygen species

---

### 8. ❌ Lossy phononic metamaterials for valley nonreciprocity

**作者**: Shunda Yin, Qiuyan Zhou, YuXiang Xi, Weiyin Deng, Wenxing Chen, Jiuyang Lu, Manzhu Ke, Zhengyou Liu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70037-7](https://doi.org/10.1038/s41467-026-70037-7)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是声子超材料中的非厄米物理和谷非互易性，属于凝聚态物理和声学超材料领域。论文内容涉及声子超材料、谷物理、非厄米物理、非互易传输等概念，与医学图像分析、医学成像、深度学习医学成像等关键词完全无关。论文未提及任何医学图像、医学诊断、医学影像技术或深度学习在医学中的应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了声子超材料中通过耦合损耗操控谷自由度的非厄米物理机制，理论结合实验展示了谷非互易性导致的单向传输、谷依赖皮肤效应和异常波束路由三种现象。

<details open>
<summary>摘要翻译</summary>

> 非厄米物理——以复能带谱为特征——在凝聚态体系和超材料中建立了新的研究范式。结合非互易性，非厄米增益可被任意注入系统以调控其谷动力学，由此产生诸如用于声学激射的放大拓扑回音壁模式等现象。本文揭示了耦合损耗同样可用于调控声子超材料中的谷自由度。我们通过理论与实验展示了由谷非互易性引发的三种显著效应：包括可作为谷滤波器的谷体态单向输运、不同谷的体态局域于相反边界的谷依赖趋肤效应，以及具有边界依赖寿命并导致异常波束路由的谷投影边缘态。基于本文所展示的对损耗的简易调控，我们的研究揭示了非厄米物理与谷物理之间的相互作用，为基于谷的器件应用提供了新路径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Non-Hermitian physics - characterized by complex band spectra - established a new paradigm in condensed matter systems and metamaterials. Combined to nonreciprocity, non-Hermitian gain can be arbitrarily injected in a system to manipulate its valley dynamics, leading to phenomena such as the amplified topological whispering gallery modes for acoustic lasing. Here, we reveal that the coupling loss can also be used to manipulate valley degrees of freedom in a phononic metamaterial. We theoretically and experimentally show three distinct effects induced by valley nonreciprocity, including unidirectional transport of valley bulk states that functions as a valley filter, valley-dependent skin effects, where bulk states from different valleys localize at opposite boundaries, and valley-projected edge states with boundary-dependent lifetimes that leads to an anomalous beam routing. Owing to the simple control over losses demonstrated here, our findings shed light on the interplay between non-Hermitian and valley physics, providing a route to applications of valley-based devices.

</details>
<br>

**关键词**: phononic metamaterials, valley nonreciprocity, non-Hermitian physics, unidirectional transport, valley-dependent skin effects, anomalous beam routing, loss manipulation, valley filter

---

### 9. ❌ Tough hydrogels enabled by transient entanglements

**作者**: Zhaoyang Yuan, Zhenxing Cao, Hao Wang, Haitao Wu, J. S. Zheng, Rongchun Zhang, Jinrong Wu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70194-9](https://doi.org/10.1038/s41467-026-70194-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是水凝胶材料的力学性能改进，通过瞬态缠结策略解决强度与韧性之间的权衡问题，属于材料科学和化学工程领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，标题、摘要和作者信息中均未提及任何医学图像相关概念。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了单共价网络水凝胶中强度与韧性难以兼得的长期挑战，通过引入可滑动的瞬态缠结结构，实现了高断裂应变、高强度和高疲劳阈值的优异力学性能。

<details open>
<summary>摘要翻译</summary>

> 在单一共价网络水凝胶中同时实现高韧性与高强度，始终是一项长期存在的挑战。本文报道了一种简单而有效的策略，通过构建具有丰富悬垂链的聚丙烯酰胺（PAAm）网络来化解这一强度-韧性矛盾，这些悬垂链可形成瞬态缠结。与永久性捕获的缠结不同，这些瞬态缠结在负载作用下能够滑移并完全解缠结，从而在宽应变范围内实现高效的能量耗散和应力重新分布。此外，与其他结构相比，该网络展现出优异的均质性，能有效缓解应力集中。因此，我们制备的单一共价网络水凝胶表现出良好的力学性能，包括5071%的断裂应变、1.06 MPa的断裂强度、1968 J·m⁻²的疲劳阈值以及约60,000 J·m⁻²的断裂能。此外，这些水凝胶还具有低摩擦和高耐磨的特性。这种简单而稳健的设计范式，无需借助多网络结构的复杂性，便有效克服了长期存在的强度-韧性权衡问题，为下一代水凝胶在生物医学、可穿戴电子设备及其他严苛环境中的应用开辟了新途径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Achieving high toughness and strength simultaneously in single-covalent-network hydrogels remains a longstanding challenge. Herein, we report a simple yet effective strategy to resolve this strength-toughness conflict by constructing polyacrylamide (PAAm) networks with abundant dangling chains that form transient entanglements. Unlike permanently trapped entanglements, these transient entanglements can slip and fully disentangle upon loading, enabling highly efficient energy dissipation and stress redistribution over a broad range of strains. Besides, these networks exhibit superior homogeneity compared to other structures, effectively mitigating stress concentration. As a result, our single-covalent-network hydrogels exhibit good mechanical properties, including a fracture strain of 5071%, a fracture strength of 1.06 MPa, a fatigue threshold of 1968 J·m⁻², and a fracture energy of approximately 60,000 J·m⁻². Moreover, these hydrogels feature low friction and high wear-resistance. Such a simple yet robust design paradigm effectively overcomes the longstanding strength-toughness trade-off without the complexity of multi-network architectures, opening avenues for next-generation hydrogels in biomedicine, wearable electronics, and other demanding environments.

</details>
<br>

**关键词**: hydrogels, transient entanglements, mechanical properties, strength-toughness trade-off, polyacrylamide networks, energy dissipation, wear-resistance, biomedical applications

---

### 10. ❌ TCL1A mediates DNA methylation defects in recurrent hydatidiform mole with NLRP7 pathogenic variants

**作者**: Zheng Gao, Li Zhang, Lei Li, Ting Hu, Xukun Lu, Yu Wu, Dandan Qin, Jinze Li, Chen Gu, Jin Li, Chengpeng Xu, Dan Zhou, Fan Zhou, Yanling Bai, Xiangjin Kang, Jianqiao Liu, Dong Deng, Lei Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-69744-y](https://doi.org/10.1038/s41467-026-69744-y)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是复发性葡萄胎的分子机制，具体探讨NLRP7基因变异如何通过TCL1A影响DNA甲基化缺陷。全文聚焦于分子生物学、遗传学和表观遗传学机制，使用的方法包括结构生物学（cryo-EM）、生化分析和计算预测。论文完全没有涉及医学图像分析、医学成像或深度学习在医学成像中的应用，这些关键词与论文内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A cytoplasmic regulatory mechanism governing nuclear DNA methylation is proposed, explaining the hypomethylation pathogenesis in NLRP7 variant-associated recurrent hydatidiform mole.

!!! tip deepseek-chat TL;DR

    该研究发现TCL1A是NLRP7的内源性相互作用伙伴，NLRP7通过将TCL1A隔离在细胞质中来保护卵母细胞甲基组，解释了NLRP7变异相关复发性葡萄胎中低甲基化的发病机制。

<details open>
<summary>摘要翻译</summary>

> NLRP7基因的致病性变异与55%的复发性葡萄胎病例相关，其特征是母源甲基化印记区域低甲基化。这些变异被认为会破坏人类卵母细胞中的从头DNA甲基化过程，但其精确机制尚不明确。本研究鉴定出DNMT3A抑制剂TCL1A是NLRP7的内源性相互作用蛋白。通过冷冻电镜解析的NLRP7-TCL1A复合物结构揭示了其基本架构。综合分析表明，大多数导致复发性葡萄胎的NLRP7变异会损害其与TCL1A的相互作用。机制上，NLRP7可能通过将TCL1A隔离在细胞质中，阻止其进入细胞核，从而避免其对DNMT3A介导的从头甲基化的抑制，以此保护卵母细胞甲基化组的稳定性。结合计算机预测与相互作用分析，我们鉴定出L766R为一个致病性变异。这些发现提出了一种调控核内DNA甲基化的细胞质机制，从而解释了NLRP7变异相关复发性葡萄胎中低甲基化的发病机理。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Pathogenic variants in NLRP7, implicated in 55% of recurrent hydatidiform mole characterized by hypomethylation at maternally methylated imprinted regions, are proposed to disrupt de novo DNA methylation in human oocytes. However, the precise mechanism remains unclear. Here, we identify TCL1A, a DNMT3A inhibitor, as an endogenous NLRP7-interacting partner. The cryo-EM structure of the NLRP7-TCL1A complex reveals its fundamental architecture. Comprehensive analysis demonstrates that the majority of recurrent hydatidiform mole-causing NLRP7 variants impair its interaction with TCL1A. Mechanistically, NLRP7 potentially safeguards oocyte methylome by sequestering TCL1A in the cytoplasm, thereby preventing its nuclear entry and subsequent suppression of DNMT3A-mediated de novo methylation. Combining in silico predictions and interaction analysis, we identify L766R as a pathogenic variant. These findings propose a cytoplasmic regulatory mechanism governing nuclear DNA methylation, explaining the hypomethylation pathogenesis in NLRP7 variant-associated recurrent hydatidiform mole.

</details>
<br>

**关键词**: NLRP7, TCL1A, DNA methylation, recurrent hydatidiform mole, oocyte methylome, DNMT3A, cytoplasmic regulatory mechanism, pathogenic variants

---

### 11. ❌ Quantifying the trade-off between spring phenology and lethal frost risk: a meta-analysis

**作者**: Zhengjie Yan, Cheng Chen, Yue Liu (292931), Yujiang Li, Huiying Liu, Hao Wang, Tao Yan, Xin Jing, Shuai Ren, Hongbiao Zi, Yan Shi, Tao Wang (12008), Jin He
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70187-8](https://doi.org/10.1038/s41467-026-70187-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是植物物候学（spring phenology）与霜冻风险（frost risk）之间的权衡关系，通过全球荟萃分析评估气候变化下的植物适应性。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均涉及医学影像分析领域，而论文内容完全不涉及医学、影像或深度学习技术，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A global meta-analysis encompassing 193 plant species across 126 study sites finds consistently high freezing resistance with remarkably low lethal frost risk during spring emergence, and highlights the necessity of incorporating biotic factors and biotic processes into next-generation phenological models to enhance prediction accuracy under climate change.

!!! tip deepseek-chat TL;DR

    该论文通过全球荟萃分析发现，春季物候提前与致命霜冻风险之间存在权衡关系，在轻度至中度气候变暖情景下物候提前不会增加霜冻风险，而在高度变暖情景下霜冻安全边际反而会扩大。

<details open>
<summary>摘要翻译</summary>

> 春季物候的时机体现了生长季延长与霜冻风险规避之间的关键权衡，其平衡关系决定了植物的适应度并塑造了植物物种的分布格局。然而，目前鲜有定量评估研究，表明这一权衡机制在很大程度上尚未得到实证检验。本文通过一项涵盖126个研究站点、193种植物的全球荟萃分析发现，在春季萌发期间，植物普遍表现出较高的抗冻性（可耐受-12°C低温），且致死性霜冻风险极低（安全边际达17°C）。在预测的气候变暖情景下，轻度至中度变暖不会因春季物候提前而影响致死性霜冻风险，这很可能源于温度敏感性的降低，符合权衡机制的预测。与之相反，在高度变暖情景下，预计冻结安全边际将扩大（约1.7°C），导致致死性霜冻风险降低。这种扩大可能补偿极端变暖下预期的抗冻性减弱。我们的研究结果挑战了传统观点——即简单环境因子主导春季物候调控，并强调必须将生物因子（如抗冻性freezing resistance）和生物过程（如早期生长与霜冻风险的权衡）纳入新一代物候模型，以提升气候变化下的预测准确性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The timing of spring phenology represents a critical trade-off between growing season extension and frost risk avoidance, the balance of which governs plant fitness and shapes plant species' distributions. However, few quantitative assessments exist, indicating that this trade-off is largely untested empirically. Here, we present a global meta-analysis encompassing 193 plant species across 126 study sites, finding consistently high freezing resistance (to -12 °C) with remarkably low lethal frost risk (safety margin of 17 °C) during spring emergence. Under projected climate warming scenarios, predictions indicate that advances in spring phenology do not affect the lethal frost risk under light and moderate warming scenarios. This is likely due to the reduced temperature sensitivity, consistent with trade-off predictions. By contrast, in the high-warming scenario, the freezing safety margin is predicted to expand (by ~1.7 °C), resulting in a lower lethal frost risk. This expansion may compensate for the diminished freezing resistance predicted under extreme warming. Our findings challenge the conventional view that simple environmental factors moderate spring phenology, and highlight the necessity of incorporating biotic factors (e.g., freezing resistance) and biotic processes (e.g., early growth versus frost risk trade-offs) into next-generation phenological models to enhance prediction accuracy under climate change.

</details>
<br>

**关键词**: spring phenology, frost risk, meta-analysis, climate warming, freezing resistance, plant species, trade-off, safety margin

---

### 12. ❌ Re-entrant unconventional superconductivity induced by rare-earth substitution in Nd1-xEuxNiO2 thin films

**作者**: Dung Vu, Hangoo Lee, Daniele Nicoletti, Wenzheng Wei, Zheting Jin, Dmitry V. Chichinadze, M. Buzzi, W. Li, Xinhao Yang, Rongting Wu, Christopher A. Mizzi, Tiema Qian, B. Maiorov, Alexey Suslov, Yu He, Cyprian Lewandowski, Sohrab Ismail‐Beigi, F. J. Walker, Andrea Cavalleri, Charles H. Ahn
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**arXiv链接**: [https://arxiv.org/abs/2508.15968](https://arxiv.org/abs/2508.15968)
**DOI**: [10.1038/s41467-026-70254-0](https://doi.org/10.1038/s41467-026-70254-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是镍酸盐薄膜中的高温超导现象，具体探讨了铕（Eu）替代对Nd1-xEuxNiO2薄膜超导性能的影响，包括超导能隙增强、强耦合机制和磁场增强超导性。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均与医学图像分析相关，而论文内容完全属于凝聚态物理和材料科学领域，涉及超导材料、薄膜制备、磁阻测量和红外光谱分析，与医学图像没有任何关联。因此，所有关键词的相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了在Nd1-xEuxNiO2薄膜中通过稀土铕替代增强超导能隙并诱导强耦合机制，实验表明铕替代导致磁场增强的超导性和违反弱耦合泡利极限的上临界磁场，为无限层镍酸盐的高温超导工程提供了新途径。

<details open>
<summary>摘要翻译</summary>

> 高温超导通常与强耦合和大超导能隙相关联，然而这些特性在镍酸盐体系中尚未得到证实。本文通过实验证明，在Nd<sub>1-x</sub>Eu<sub>x</sub>NiO<sub>2</sub>（NENO）薄膜的间隔层中掺入Eu能够增强超导能隙，驱动体系进入强耦合区域。这一过程伴随着磁交换驱动的磁场增强超导现象。我们研究了x = 0.2至0.35的NENO超导薄膜的上临界磁场（H<sub>c2</sub>）和超导能隙。磁阻测量揭示了NENO薄膜中磁场增强的超导性。我们将此现象解释为磁性Eu离子与Ni的d<sub>x2-y2</sub>轨道中超导态之间相互作用的结果。其上临界磁场严重违反了弱耦合的泡利极限。红外光谱证实了较大的能隙-转变温度比值（2Δ/k<sub>B</sub>T<sub>c</sub> ≃ 5-6），表明NENO相对于掺Sr的NdNiO<sub>2</sub>具有更强的耦合配对机制。稀土层中Eu的取代显著改变了钕基镍酸盐的超导能隙和磁相互作用，为无限层镍酸盐中设计高转变温度（高T<sub>c</sub>）超导性开辟了新途径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> High temperature superconductivity is typically associated with strong coupling and a large superconducting gap, yet these characteristics have not been demonstrated in the nickelates. Here, we provide experimental evidence that Eu substitution in the spacer layer of Nd<sub>1-x</sub>Eu<sub>x</sub>NiO<sub>2</sub> (NENO) thin films enhances the superconducting gap, driving the system toward a strong-coupling regime. This is accompanied by a magnetic-exchange-driven magnetic-field-enhanced superconductivity. We investigate the upper critical magnetic field, H<sub>c2</sub>, and the superconducting gap of superconducting NENO thin films with x = 0.2 to 0.35. Magnetoresistance measurements reveal magnetic-field-enhanced superconductivity in NENO films. We interpret this phenomenon as a result of an interaction between magnetic Eu ions and superconducting states in the Ni d<sub>x2-y2</sub> orbital. The upper critical magnetic field strongly violates the weak-coupling Pauli limit. Infrared spectroscopy confirms a large gap-to-T<sub>c</sub> ratio <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mn>2</mml:mn><mml:mi>Δ</mml:mi><mml:mo>/</mml:mo><mml:msub><mml:mrow><mml:mi>k</mml:mi></mml:mrow><mml:mrow><mml:mi>B</mml:mi></mml:mrow></mml:msub><mml:msub><mml:mrow><mml:mi>T</mml:mi></mml:mrow><mml:mrow><mml:mi>c</mml:mi></mml:mrow></mml:msub><mml:mo>≃</mml:mo><mml:mn>5</mml:mn><mml:mo>-</mml:mo><mml:mn>6</mml:mn></mml:math>, indicating a stronger coupling pairing mechanism in NENO relative to the Sr-doped NdNiO<sub>2</sub>. The substitution of Eu in the rare-earth layer causes pronounced modifications of the superconducting gap and magnetic interactions in Nd-based nickelates, opening new pathways to engineer high-T<sub>c</sub> superconductivity in infinite-layer nickelates.

</details>
<br>

**关键词**: nickelates, superconductivity, thin films, rare-earth substitution, superconducting gap, magnetic-field-enhanced superconductivity, upper critical magnetic field, strong-coupling regime

---

### 13. ❌ The eco-evolutionary assembly of complex communities with multiple interaction types

**作者**: Gui Araujo, Miguel Lurgi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70117-8](https://doi.org/10.1038/s41467-026-70117-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确表明这是一篇关于生态学中复杂群落组装的论文，研究生态相互作用（如竞争、互利共生）如何通过生态和进化过程塑造生物多样性网络。全文未提及任何医学图像分析、医学成像或深度学习在医学成像中的应用。论文的核心是生态模型、物种相互作用和群落组装，与医学图像领域完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过一个结合种群动态和进化过程（如物种形成和相互作用遗传）的生态进化模型，揭示了复杂物种相互作用网络中生物多样性的产生和维持机制，发现相互作用的成本效益平衡将群落分为稀疏的竞争主导网络和高度互利的连接社区两种类型。

<details open>
<summary>摘要翻译</summary>

> 揭示复杂生态群落结构形成的机制是理解其群落构建的基础。然而，关于生态与进化过程如何共同塑造这些模式的完整图景仍不清晰。我们采用一个结合了相互作用驱动的种群动态以及进化过程（包括物种形成和相互作用的遗传）的群落构建生态进化模型，以阐明在复杂物种相互作用网络中产生和维持生物多样性的机制。重要的是，我们的模型通过比较在不同相互作用类型组合下，基于进化的构建与基于入侵的构建过程，区分了相互作用类型的选择效应与遗传效应。研究发现，相互作用积累的成本-收益平衡将群落划分为两种截然不同的类型。弱有益性相互作用产生稀疏的、竞争主导的网络，而强有益性相互作用则催生出高度互惠、连接更紧密的群落。由选择和遗传共同驱动的互惠作用，促进了规模更大、复杂性更高的群落的出现。通过将模型结果与微生物群落的经验模式进行比较，我们识别了生态系统构建的潜在驱动因素及其特征性的相互作用结构。我们的研究结果基于生态相互作用的组成，提出了一套复杂生态系统的分类体系，从而为不同群落类型（互惠型 vs. 竞争型）在何种条件下可能出现，提供了可检验的假说。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Identifying the mechanisms that generate structure in complex ecological communities is fundamental for understanding their assembly. Yet a comprehensive picture of how ecology and evolution combine to generate these patterns remains limited. We use an eco-evolutionary model of community assembly that incorporates interaction-driven population dynamics and evolutionary processes, including speciation and inheritance of interactions, to unveil the mechanisms generating and maintaining biodiversity in complex species interaction networks. Importantly, our model unpicks the effects of selection of interaction types from those of inheritance by comparing evolutionary assembly with invasion-based assembly under different combinations of interaction types. We find that a cost-benefit balance in accumulating interactions separates communities into two distinct types. Weakly beneficial interactions produce sparse, competition-dominated networks, whereas strongly beneficial interactions generate highly mutualistic, more connected communities. Mutualism, driven by both selection and inheritance, facilitates the emergence of large communities with increased complexity. Comparing model results with empirical patterns from microbial communities, we identify potential drivers of ecosystem assembly and characteristic interaction structures. Our results provide a classification system of complex ecosystems based on their composition of ecological interactions, thus generating testable hypotheses on the conditions under which different community types (mutualistic vs. competitive) might emerge.

</details>
<br>

**关键词**: eco-evolutionary model, community assembly, species interaction networks, biodiversity, mutualism, competition, ecological interactions, microbial communities

---

### 14. ❌ Oceanic upper crustal accretion by melt sill and lava flow interaction at Axial volcano

**作者**: Han Wu, Wenxin Xie, Satish C. Singh, Hélène Carton, Graham M. Kent, Adrien F. Arnulf, Alistair J. Harding
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70033-x](https://doi.org/10.1038/s41467-026-70033-x)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是海洋地质学中火山地壳形成过程，使用三维地震反射数据成像分析Axial火山的熔岩流层结构。所有评分关键词均涉及医学图像分析领域（医学影像、深度学习医学影像），而论文内容属于地球物理学和海洋地质学，两者领域完全不同，无任何相关性。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究使用三维地震反射成像揭示了Axial火山的上地壳是通过熔岩流层与熔体岩床的复杂相互作用形成的，而非传统的席状岩墙模式。

<details open>
<summary>摘要翻译</summary>

> 传统观点认为，沿大洋中脊岩浆增生形成的上地壳由熔岩流覆盖于席状岩墙杂岩之上。然而，在受热点影响的洋脊段，上地壳如何形成仍属未知。本研究利用三维地震反射数据，对胡安·德富卡海脊轴向火山下方的熔岩流层理进行了成像。这些熔岩流层向火山口和裂谷带内侧倾斜，其成因是火山峰下方岩浆抽离及裂谷带伸展引发的沉降作用。此外，我们的图像显示该区域不存在经典的、横向连续的席状岩墙杂岩。相反，熔岩流层发生旋转并直接与岩浆域接触，导致这些单元发生部分同化作用。三维图像还显示熔体沿熔岩流层向外贯入，这表明轴向火山上地壳的形成源于贯入熔岩席与熔岩流层之间复杂的相互作用。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Magmatically-accreted upper crust along mid-ocean ridges is traditionally considered to consist of lava flows overlying a sheeted-dyke complex. However, how the upper crust is formed at hotspot-influenced ridge segments remains unknown. Using three-dimensional seismic reflection data, here we report images of lava flow layering beneath Axial volcano on the Juan de Fuca Ridge. These lava flow layers dip inward towards the caldera and rift zones, resulting from subsidence caused by magma withdrawal beneath the summit and rift zone extension. Furthermore, our images reveal that the classic, laterally continuous sheeted-dyke complex is absent. Instead, lava flow layers are rotated and brought into direct contact with the magma domain, leading to partial assimilation of these units. Three-dimensional images also show that melt is injected outward along lava flow layers, suggesting that the upper crust at Axial volcano is formed by complex interactions between injected melt sills and lava flow layers.

</details>
<br>

**关键词**: oceanic crust, lava flow layers, melt sills, seismic reflection, Axial volcano, mid-ocean ridge, magma assimilation, three-dimensional imaging

---

### 15. ❌ A bionic robotic trunk with tensegrity-enabled elephant-comparable stiffness variability for assisted daily living

**作者**: Jie Zhang (64655), Chaozhong Yang, Hao Yang, Pengfei Ma, Chenyu He, Teng Zhang, Xiaofeng Wang, Ke Liu, Xiu Jia, Yun Wen
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70380-9](https://doi.org/10.1038/s41467-026-70380-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是仿生机器人躯干（bionic robotic trunk）的设计与应用，具体涉及电缆驱动的张拉整体结构、刚度调节机制及其在辅助日常生活中的应用。全文未提及医学图像分析、医学成像或深度学习医学成像相关内容。论文属于机器人学、生物启发工程和辅助技术领域，与医学图像处理完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work presents a bionic robotic trunk with a cable-driven tensegrity skeleton, leveraging synergistic and antagonistic muscle-mimicking mechanisms to achieve dynamic stiffness regulation and highlights the potential of stiffness-tunable robotic trunks in assistive applications.

!!! tip deepseek-chat TL;DR

    该研究开发了一种具有大象可比刚度可变性的仿生机器人躯干，通过电缆驱动张拉整体结构实现快速大范围刚度调节，并集成到电动轮椅上辅助中风患者完成日常任务。

<details open>
<summary>摘要翻译</summary>

> 象鼻能够在宽泛范围内快速调节其刚度，在灵巧操作所需的柔软状态与负重任务所需的刚性状态间无缝切换。尽管已有大量研究尝试通过阻塞结构、相变材料等多种方法模拟这种刚度可变性，但现有仿生机器人仍受限于狭窄的刚度调节范围和/或较低的切换频率。本研究提出了一种采用缆绳驱动张拉整体骨架的仿生机器人象鼻，通过协同与拮抗的仿肌肉机制实现动态刚度调控。借助电机驱动缆绳的协调收缩（即拮抗作用），该机器人象鼻实现了23.94至542.47 N/m的刚度调节范围及1.06 Hz的切换频率，达到了与象鼻相仿的适应能力。这种快速、大幅的刚度变化使其能够在非结构化环境中灵巧穿行，并有力操控重物。该机器人象鼻集成于配备人机交互界面的电动轮椅中，成功协助一位中风后患者完成日常活动，如打开柜门、从冰箱取牛奶及浇花。本工作推进了仿生机器人学的发展，并彰显了刚度可调机器人象鼻在辅助应用领域的潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Elephant trunks can rapidly vary their stiffness over a broad range, seamlessly switching between soft states for dexterous operation and rigid states for load-bearing tasks. Despite extensive efforts to mimic this stiffness variability using various approaches, such as jamming structures and phase-change materials, existing bionic robots are limited to narrow tunable stiffness ranges and/or slow switching frequencies. In this work, we present a bionic robotic trunk with a cable-driven tensegrity skeleton, leveraging synergistic and antagonistic muscle-mimicking mechanisms to achieve dynamic stiffness regulation. Through coordinated contraction of motor-actuated cables (i.e., antagonistic action), the robotic trunk achieves a stiffness range of 23.94 to 542.47 N/m and a switching frequency of 1.06 Hz, matching the adaptability of elephant trunks. This rapid and large-scale stiffness variation enables dexterous navigation in unstructured environments and powerful manipulation of heavy objects. Incorporated into an electric wheelchair with the human-machine interface, the robotic trunk assists a post-stroke individual with daily activities, such as opening cabinet doors, retrieving milk from refrigerators, and watering flowers. This work advances bio-inspired robotics and highlights the potential of stiffness-tunable robotic trunks in assistive applications.

</details>
<br>

**关键词**: bionic robotic trunk, tensegrity skeleton, stiffness variability, cable-driven mechanism, assistive robotics, elephant trunk inspiration, dynamic stiffness regulation, human-machine interface

---

### 16. ❌ Swapped and non-swapped TRAAK states co-exist in membranes at a ratio influenced by temperature

**作者**: Yue Ma, Katrin Ackermann, Qaiser Waheed, Vincent L. G. Postis, Terry K. Smith, Bela E. Bode, Christos Pliotas
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70027-9](https://doi.org/10.1038/s41467-026-70027-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究TRAAK离子通道在膜中的构象状态和脂质环境，属于结构生物学和生物物理学领域，完全不涉及医学图像分析、医学成像或深度学习医学成像。论文使用EPR光谱等技术，而非任何医学图像技术。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This work demonstrates the coexistence of the swapped and non-swapped states, quantifies their populations within the TRAAK ensemble, and shows that the swapped conformation dominates, with the ratio being influenced by temperature.

!!! tip deepseek-chat TL;DR

    该研究揭示了TRAAK离子通道的帽结构域在膜中同时存在交换和非交换构象，量化了它们的比例并发现温度影响该比例，同时发现TRAAK选择性地与信号脂质结合形成微域。

<details open>
<summary>摘要翻译</summary>

> 双孔域钾离子通道（K2P）TRAAK在神经系统中表达，并调控膜上的快速动作电位。与所有K2P通道类似，TRAAK具有独特的细胞外帽结构域，该结构域存在交换构象与非交换构象<sup>1,2</sup>。然而，这两种构象在天然膜中的比例分布，以及引发此构象转换的触发因素或刺激信号，目前尚不明确。本研究采用脉冲偶极电子顺磁共振波谱技术，结合异源单亚基自旋标记方法，监测了TRAAK帽结构域在膜环境中的完整构象集合。我们证实了交换态与非交换态共存，量化了它们在TRAAK集合中的分布比例，并发现交换构象占主导地位，且该比例受温度影响。天然脂质分析表明，TRAAK选择性结合信号脂质并被其激活，同时从其周围排除膜中占主导地位的磷脂酰胆碱脂质，从而形成独特的微结构域。我们的方法能够识别通道的直接脂质环境，检测并量化同源/异源K2P通道中帽结构状态的比例分布，并将结构域交换与特定触发因素联系起来。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The potassium two-pore domain (K2P) ion channel TRAAK is expressed in the nervous system and regulates the fast action potential in membranes. Like all K2P channels, TRAAK possesses a distinct extracellular cap, which adopts a swapped and a non-swapped conformation<sup>1,2</sup>. However, the proportional representation of these two species within native membranes - and the trigger or stimulus associated with this conformational transition - are unknown. Here, we utilise Pulse Dipolar EPR Spectroscopy combined with heterologous single-subunit spin-labelling and monitor the complete conformational ensemble of TRAAK's cap domain in membranes. We demonstrate the coexistence of the swapped and non-swapped states, quantify their populations within the TRAAK ensemble, and show that the swapped conformation dominates, with the ratio being influenced by temperature. Native lipid analysis shows that TRAAK selectively associates with and is activated by signalling lipids to the exclusion of membrane-dominant phosphatidylcholine lipids from its vicinity, forming a distinct microdomain. Our approach can identify the immediate lipid environment, detect and quantify cap state populations in homo-/hetero-K2P channels and link domain swapping to specific triggers.

</details>
<br>

**关键词**: TRAAK, K2P ion channel, conformational states, membrane, EPR spectroscopy, lipid microdomain, temperature, cap domain

---

### 17. ❌ Long-range spatial extension of exciton states in van der Waals heterostructure

**作者**: Zhiwen Zhou, E. A. Szwed, W. J. Brunner, H. Henstridge, L. H. Fowler-Gerace, L. V. Butov
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**arXiv链接**: [https://arxiv.org/abs/2508.20306](https://arxiv.org/abs/2508.20306)
**DOI**: [10.1038/s41467-026-70218-4](https://doi.org/10.1038/s41467-026-70218-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是二维材料范德华异质结中激子的空间扩展特性，属于凝聚态物理和材料科学领域，与医学图像分析、医学成像或深度学习医学成像完全无关。论文内容涉及光致发光光谱、激子态、空间间接激子、莫尔势等物理概念，没有任何医学或临床相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过分析MoSe2/WSe2范德华异质结中空间间接激子的光致发光窄线，发现这些激子态的空间扩展可达微米量级，表明激子被限制在弱无序的莫尔势中，而非随机势能景观。

<details open>
<summary>摘要翻译</summary>

> 激子光致发光（PL）光谱中的窄线是低维半导体的特征。这些谱线对应于异质结构中局域激子环境涨落所形成的势能景观局域极小值中激子态的发射。此类激子态的空间延伸范围在纳米尺度。本工作中，我们研究了MoSe<sub>2</sub>/WSe<sub>2</sub>范德瓦尔斯（van der Waals）异质结构中空间间接激子（IXs）PL光谱的窄线特征。窄线随IX密度增加而消失。窄线的消失与IX输运的开始相关联，表明窄线对应于局域化的激子态。这些窄线在空间上可延伸数微米，覆盖范围可达样品面积的约百分之十。与窄线对应的激子态所具有的这种宏观空间延伸，表明激子能量景观偏离随机势，并证明激子被限制在具有弱无序性的莫尔（moiré）势中。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Narrow lines in photoluminescence (PL) spectra of excitons are characteristic of low-dimensional semiconductors. These lines correspond to the emission of exciton states in local minima of a potential energy landscape formed by fluctuations of the local exciton environment in the heterostructure. The spatial extension of such states was in the nanometer range. In this work, we present studies of narrow lines in PL spectra of spatially indirect excitons (IXs) in a MoSe<sub>2</sub>/WSe<sub>2</sub> van der Waals heterostructure. The narrow lines vanish with increasing IX density. The disappearance of narrow lines correlates with the onset of IX transport, indicating that the narrow lines correspond to localized exciton states. The narrow lines extend over distances reaching several micrometers and over areas reaching ca. ten percent of the sample area. This macroscopic spatial extension of the exciton states, corresponding to the narrow lines, indicates a deviation of the exciton energy landscape from random potential and shows that the excitons are confined in moiré potential with a weak disorder.

</details>
<br>

**关键词**: van der Waals heterostructure, exciton states, photoluminescence spectra, spatial extension, moiré potential, localized excitons, MoSe2/WSe2

---

### 18. ❌ Site-specific profiling of structure and function of Igµ B cell receptor glycans

**作者**: M. D. Holborough-Kerkvliet, L. Hafkenscheid, S. Kroos, R. Biersteker, R. van de Wetering, O. Singh, E. Fadda, R. T. N. Tjokrodirijo, P. A. van Veelen, M. Wuhrer, D. Falck, R. E. M. Toes
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70121-y](https://doi.org/10.1038/s41467-026-70121-y)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是B细胞受体（BCR）糖基化的分子生物学和免疫学特征，具体分析Igμ BCR糖基化位点、结构与功能，属于免疫学、糖生物学和分子生物学领域。论文完全不涉及医学图像分析、医学成像或深度学习医学成像技术，这些关键词与论文内容无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    High conservation of Igµ BCR glycosylation across B cell subsets and limited contribution to BCR expression and function are shown, suggesting BCR glycans may have evolved to support IgM antibody functions.

!!! tip deepseek-chat TL;DR

    该研究分析了人类Igμ B细胞受体（BCR）四个N-连接糖基化位点的特异性糖基化特征，发现BCR糖基化在B细胞亚型间高度保守，对BCR表达和功能影响有限，可能主要支持IgM抗体功能。

<details open>
<summary>摘要翻译</summary>

> 尽管N-连接聚糖在调节抗体效应功能中起着关键作用，但人们对于附着在人B细胞受体（BCR）上的聚糖组成及其功能影响知之甚少。本文中，我们描述了来自初始B细胞和记忆B细胞的人Igµ BCR所有4个N-连接糖基化位点的特异性糖基化谱。数据显示，Igµ BCR聚糖在从初始B细胞向记忆细胞转变过程中未发生结构改变，因为来自健康供体的两种B细胞亚型的BCR均携带相似的聚糖。相反，血清IgM抗体表现出与Igµ BCR不同的糖基化特征，这部分归因于Igµ BCR与IgM抗体分子形式的差异。此外，通过使用表达特定BCR的B细胞系，我们发现尽管缺失Igµ BCR N209位点聚糖会降低抗原结合能力，但单个糖基化位点对于细胞表面表达及BCR触发后的内化过程并非必需。总体而言，我们的研究表明Igµ BCR糖基化在不同B细胞亚群间高度保守，且对BCR表达和功能的贡献有限，这提示BCR聚糖的进化可能主要在于支持IgM抗体的功能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Although N-linked glycans play pivotal roles in the regulation of antibody effector functions, little is known about the composition and functional impact of glycans attached to human B cell receptors (BCR). Here, we describe the site-specific glycosylation profiles of all 4 N-linked glycosylation sites of human Igµ BCRs from primary naive and memory B cells. Our data indicate that the Igµ BCR glycans do not undergo structural changes during transition from naive to memory cells, as healthy donor-derived BCRs from both B cell subtypes carry similar glycans. Conversely, serum IgM antibodies display distinct glycosylation features to Igµ BCRs, which are in part explained by the different molecular form of Igµ BCRs and IgM antibodies. Moreover, using B cell lines expressing defined BCRs, we show that, although the absence of the Igµ BCR N209 glycans reduces antigen binding, the individual glycosylation sites are nonessential for cell surface expression and BCR internalization following BCR triggering. Collectively, we show high conservation of Igµ BCR glycosylation across B cell subsets and limited contribution to BCR expression and function, suggesting BCR glycans may have evolved to support IgM antibody functions.

</details>
<br>

**关键词**: B cell receptor, glycosylation, Igμ, N-linked glycans, naive B cells, memory B cells, antigen binding, BCR internalization

---

### 19. ❌ Vibronically assisted sub-cycle charge transfer at a non-fullerene acceptor heterojunction

**作者**: Pratyush Ghosh, Jeroen Royakkers, Giacomo Londi, Samuele Giannini, Rakesh Arul, Alexander J. Gillett, Scott T. Keene, Szymon J. Zelewski, David Beljonne, Hugo Bronstein, Akshay Rao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70292-8](https://doi.org/10.1038/s41467-026-70292-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是有机光伏材料中的超快电荷转移机制，涉及光物理、光化学和材料科学领域。标题和摘要中完全没有提及医学图像分析、医学成像或深度学习医学成像相关内容。论文的核心是光激发下的电荷转移动力学、振动辅助过程和有机异质结特性，与医学图像领域完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了在能量偏移极小且耦合弱的聚合物-非富勒烯受体异质结中，通过高频振动模式辅助实现超快电荷转移的机制，发现电荷转移时间可达约18飞秒。

<details open>
<summary>摘要翻译</summary>

> 激发态电荷转移是有机光伏、光催化和光电探测的基础，但传统观点认为该过程需要较大的能量偏移和强给体-受体耦合，这可能限制器件性能。本文研究了基于空间聚合物-非富勒烯受体的模型异质结体系，其中苝二酰亚胺受体通过共价键连接于低带隙聚合物给体。这些体系的前线轨道间能量偏移极小（< 100 meV），且在弗兰克-康登区域内给体-受体耦合较弱。然而，我们仍实现了约18 fs的电荷转移时间尺度。这种超快电荷转移伴随着沿非富勒烯受体势能面上高频振动坐标（周期26 fs）的相干波包运动。通过分析光激发后弗兰克尔激子态与电荷转移态的混合，我们发现了特定的聚合物中心驱动振动模式，正是这些模式实现了如此快速的电荷转移速率。我们的研究结果表明：即使在没有大能量偏移或强基态耦合的情况下，仍可实现超快电荷转移——其最终极限取决于高频振动周期。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Excited-state charge transfer underpins organic photovoltaics, photocatalysis and photodetection, but is traditionally thought to require large energy offsets and strong donor-acceptor coupling that can limit device performance. Here, we investigate through-space polymer non-fullerene-acceptor based model heterojunctions in which a perylene diimide acceptor is covalently tethered to a low-bandgap polymer donor. These systems feature an exceptionally small energy offset (< 100 meV) between frontier orbitals, with weak donor-acceptor coupling in the Franck-Condon region. We nevertheless achieve a charge-transfer timescale of ~18 fs. This ultrafast charge-transfer is accompanied via the launch of coherent wavepackets along a high-frequency vibrational coordinate (26 fs period) on the non-fullerene acceptor's potential energy surface. We uncover specific polymer-centered driving vibrational modes that enable such rapid charge-transfer rates, by mixing Frenkel exciton and charge-transfer states following photoexcitation. Our results demonstrate that ultrafast charge-transfer can be achieved-ultimately limited by high-frequency vibrational periods-even in the absence of large energy offsets or strong ground-state coupling.

</details>
<br>

**关键词**: charge transfer, non-fullerene acceptor, heterojunction, vibrational modes, ultrafast dynamics, organic photovoltaics, energy offset, coherent wavepackets

---

### 20. ❌ Design-driven optimization of low-cost reagent formulations for reproducible and high-yielding cell-free gene expression

**作者**: Mari Olsen, Caroline E. Copeland, Chad Sundberg, Rochelle Aw, Zachary M. Shaver, G. P. Rao, James R. Swartz, Ashty S. Karim, Michael C. Jewett
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-69605-8](https://doi.org/10.1038/s41467-026-69605-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确聚焦于细胞游离基因表达系统的试剂配方优化，用于蛋白质生产，属于合成生物学和生物技术领域。全文未提及医学图像分析、医学成像或深度学习医学成像相关内容，与所有评分关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过多维筛选设计优化了细胞游离基因表达系统的试剂配方，显著降低了成本并提高了蛋白质产率，实现了多种治疗相关蛋白质的高效生产。

<details open>
<summary>摘要翻译</summary>

> 获取重组蛋白质是基础科学与生物技术研究的关键。无细胞基因表达系统为满足这一需求提供了一种途径，但其广泛应用仍受限于现有平台的成本、复杂性和不稳定性。为突破这些限制，我们采用多维确定性筛选设计，以减少试剂组分数量并去除昂贵的次级能量底物。通过对1,231种不同试剂配方的筛选，我们开发出一种基于12种组分的简易且可重复的系统。优化后的试剂配方在15微升规模下可产出2.4 ± 0.3 g/L的蛋白质产物（成本约$60/克<sub>蛋白质</sub>），在4毫升规模并补充氧气的条件下可产出3.7 ± 0.2 g/L（成本约$39/克<sub>蛋白质</sub>），较以往无细胞试剂配方的平均成本降低95%。我们进一步证明，该优化配方能够从含氮碱基和核糖合成核苷三磷酸，并且在多批次细胞裂解液、不同操作者/实验场所的差异条件下均保持稳定，成功合成了超过20种不同蛋白质。例如，我们展示了包括全长非糖基化单克隆抗体在内的15种治疗相关产物的生产。我们预期该优化试剂配方将推动无细胞系统在蛋白质制造和合成生物学应用中的普及化。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Access to recombinant proteins is vital in basic science and biotechnology research. Cell-free gene expression systems provide one approach to address this need, but widespread utilization remains limited by the cost, complexity, and inconsistency of current platforms. To address these limitations, we carry out a multi-dimensional definitive screening design to reduce the number of reagent components and remove costly secondary energy substrates. From 1,231 different reagent formulations, we discover a simple and reproducible system based on 12 components. The optimized reagent formulation can produce 2.4 ± 0.3 g/L of protein product at the 15-µL scale (~$60/g<sub>protein</sub>) and 3.7 ± 0.2 g/L (~$39/g<sub>protein</sub>) at the 4-mL scale with oxygen supplementation. This provides an average 95% reduction in cost over previous cell-free reagent formulations. We further show that the optimized reagent formulation can produce nucleoside triphosphates from nitrogenous bases and ribose and that it is robust to failure across batches of cell lysates, users/locations, and in the synthesis of more than 20 different proteins. For example, we demonstrate the production of fifteen therapeutically relevant products, including full-length aglycosylated monoclonal antibodies. We anticipate that our optimized reagent formulation will democratize the use of cell-free systems for protein manufacturing and synthetic biology applications.

</details>
<br>

**关键词**: cell-free gene expression, reagent formulation optimization, protein production, cost reduction, synthetic biology, recombinant proteins, definitive screening design, therapeutic proteins

---

### 21. ❌ Sub-micron-resolution temperature mapping of Zn negative electrode for flow batteries

**作者**: Shengnan Wang, Yao Gao, Shixun Wang, Mingzhong AI, Yihui Guo, Xingjun Liu, Yiqiao Wang, Zhiquan Wei, Jiaxiong Zhu, Qingshun Nian, Cuili Zhang, Lang Wang, Shengbo Lu, Tracy Chenmin Liu, Quan Li, Chunyi Zhi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70318-1](https://doi.org/10.1038/s41467-026-70318-1)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究锌基液流电池负极的亚微米级温度分布与枝晶生长的关系，采用光学检测磁共振和纳米金刚石量子传感器进行温度监测，属于能源存储和电化学领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，这些关键词与论文主题无任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了锌基液流电池负极在沉积过程中局部温度分布与枝晶生长的关系，通过开发亚微米分辨率温度映射技术并引入液态金属电极，成功抑制了热点驱动的枝晶生长，显著提升了电池在高荷电状态下的循环稳定性。

<details open>
<summary>摘要翻译</summary>

> 在全球能源转型挑战的背景下，锌基液流电池因其安全、经济且可持续的储能特性而备受关注。然而，锌负极较差的电化学可逆性与枝晶生长问题，尤其是在高荷电状态条件下，阻碍了其实际应用。尽管针对锌负极已有广泛研究，但局部温度分布与枝晶形成之间的关联仍未得到充分探索，这主要受限于微观观测技术的不足。本研究采用基于纳米金刚石量子传感器的非侵入式光学探测磁共振技术，监测锌沉积过程中的温度变化，实现了亚微米级空间分辨率（约300纳米）和约2 K/Hz<sup>0.5</sup>的温度灵敏度。研究结果表明，空间温度不均匀性可能在加速枝晶生长并引发更严重短路方面起到关键作用。模拟分析显示，提高基底热导率可改善锌沉积的均匀性。基于此，我们引入了一种可流动的镓-铟液态金属电极，该电极能有效分散局部热量并降低界面温度梯度，从而抑制热点驱动的枝晶生长，并实现液态锌合金的原位形成。采用该液态金属电极的锌-溴液流电池在90%高荷电状态下循环稳定性显著提升，稳定运行超过2400小时，在40 mA cm<sup>-2</sup>电流密度下累计放电容量达到46.2 Ah cm<sup>-2</sup>。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Zinc-based flow batteries are gaining attention as safe, cost-effective, and sustainable energy storage solutions amid global energy transition challenges. However, their practical application is hindered by poor reversibility and dendrite formation of Zn negative electrode, particularly under high state-of-charge conditions. Despite extensive research on Zn side, the relationship between localized temperature distribution and dendrites remains underexplored, primarily due to limited microscopic observation techniques. Here, we present a non-invasive optically detected magnetic resonance with nanodiamond quantum sensors to monitor temperature variations during Zn deposition, achieving a sub-micron spatial resolution ( ~ 300 nm) and a temperature sensitivity of ~2 K/Hz<sup>0.5</sup>. Our findings suggest that spatial temperature non-uniformity may play a critical role in accelerating dendrite growth and potentially leading to more severe short circuits. Simulations revealed that higher substrate thermal conductivity improves Zn deposition uniformity. Herein, we introduced a flowable gallium-indium liquid metal electrode, which disperses localized heat and lowers interfacial temperature gradients, thereby suppressing hotspot-driven dendrite growth and enabling in situ formation of a liquid Zn alloy. The zinc-bromine flow battery with the liquid metal electrode demonstrated enhanced cycling stability over 2400 hours at a high state-of-charge of 90%, achieving a cumulative discharge capacity of 46.2 Ah cm<sup>-2</sup> at 40 mA cm<sup>-2</sup>.

</details>
<br>

**关键词**: zinc-based flow batteries, temperature mapping, dendrite growth, sub-micron resolution, liquid metal electrode, cycling stability, Zn deposition, thermal conductivity

---

### 22. ❌ Linker histones consolidate heterogenous nucleosome fiber contacts by linking together multiple nucleosomes

**作者**: Zenita Adhireksan, Deepti Sharma, Qiuye Bao, Phoi Leng Lee, Sivaraman Padavattan, Gabriela E. Davey, Jeffrey C. Hansen, Curtis A. Davey
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-69842-x](https://doi.org/10.1038/s41467-026-69842-x)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是染色质结构和组蛋白H1的分子生物学机制，具体涉及核小体组装、结晶学分析和染色质调控。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均与医学影像分析相关，而论文内容完全属于结构生物学和分子遗传学领域，两者之间没有任何关联。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The activity of the somatic H1 variants is investigated by conducting crystallographic analysis of nucleosomal assemblies and characterization of nucleosome array condensates, which recapitulate long-range nucleosome fiber interactions in chromatin.

!!! tip deepseek-chat TL;DR

    该研究通过结晶学分析和核小体阵列表征，揭示了连接组蛋白H1通过多种DNA结合模式（包括连接多个核小体/纤维）来支持染色质调控的结构和功能复杂性。

<details open>
<summary>摘要翻译</summary>

> 连接组蛋白（H1）的共识结合模式表现为与单个核小体的“dyad上”结合，这使得在高度异质的结构支架背景下，理解H1在染色质动态变化和压缩活动中的作用变得困难。本研究通过对核小体组装体进行晶体学分析，以及对重现染色质中长程核小体纤维相互作用的核小体阵列凝聚体进行表征，探究了体细胞H1变体的活性。研究发现，H1以多种结合模式依赖变体类型与核小体结合，其中包括将多个核小体/纤维连接在一起。这种结合多样性得益于H1球状结构域倾向于识别DNA结构基序的能力，这些基序在单个核小体与核小体簇内的特定微环境之间具有相似性。我们提出，连接组蛋白通过采取多种依赖于情境和变体的DNA结合模式，支持了染色质调控在结构和功能上的复杂调控机制。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The consensus mode for linker histone (H1) association coincides with 'on-dyad' binding to an individual nucleosome, making it challenging to rationalize the chromatin dynamics and compacting activities of H1 in the context of a highly heterogeneous structural scaffold. Here, we investigate the activity of the somatic H1 variants by conducting crystallographic analysis of nucleosomal assemblies and characterization of nucleosome array condensates, which recapitulate long-range nucleosome fiber interactions in chromatin. H1 is observed to associate variant-dependently with nucleosomes through a diversity of binding modes that include linking multiple nucleosomes/fibers together. Binding versatility is facilitated by the proclivity of the H1 globular domain to recognize DNA structural motifs, which are similar between an individual nucleosome and specific niches within clusters of nucleosomes. We propose that linker histones support a structurally and functionally complex repertoire for chromatin regulation by assuming a variety of context-and variant-dependent DNA binding modes.

</details>
<br>

**关键词**: linker histone H1, nucleosome, chromatin structure, crystallographic analysis, DNA binding modes, nucleosome array, chromatin regulation, heterogeneous binding

---

### 23. ❌ Graphene quantum dot membranes with tailorable pores for efficient gas separation

**作者**: Xinjing Zhang, Qiuxia Feng, Liang Zhang, Zhongwei Cao, Hongbo Li, Xuefeng Zhu, WS Yang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-69938-4](https://doi.org/10.1038/s41467-026-69938-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是石墨烯量子点膜材料用于气体分离（如CO2/N2、CO2/CH4、C3H6/C3H8），涉及膜材料制备、孔结构调控和气体分离性能，与医学图像分析、医学成像或深度学习医学成像完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种通过热处理和原位交联调控石墨烯量子点膜孔结构的后调控策略，实现了可定制的CO2/N2、CO2/CH4等气体高效分离性能，并超越了工业CO2捕获目标。

<details open>
<summary>摘要翻译</summary>

> 膜材料与制备方法通常需要协同开发以满足不同气体分离应用对渗透通量与选择性的特定要求，这限制了膜技术的适应性。本文提出一种后调控策略——通过调节标准“原始”膜的孔结构来满足多样化的分离需求——该策略极大简化了膜制备过程并加速了技术发展。我们引入石墨烯量子点（Graphene Quantum Dots, GQDs）作为创新构筑单元：通过紧密堆叠GQDs构建了连续的GQD膜，随后通过热处理以及与小型胺分子的原位交联对其孔结构进行调控。结合可调节的埃尺度孔隙与对CO<sub>2</sub>的优先吸附特性，所得GQD膜展现出广泛可调的CO<sub>2</sub>/N<sub>2</sub>和CO<sub>2</sub>/CH<sub>4</sub>分离性能。其CO<sub>2</sub>渗透通量与分离因子均超越多数已报道的膜材料，并可调控至超过工业CO<sub>2</sub>捕集目标。通过改变热处理温度，该膜的分离范围进一步拓展至C<sub>3</sub>H<sub>6</sub>/C<sub>3</sub>H<sub>8</sub>等具有挑战性的气体组对，证明了这种可定制的后调控孔结构策略的巨大潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Membrane materials and fabrication methods often need to be co-developed to meet the specific permeance and selectivity requirements of different gas separation application, which limits the adaptability of membrane technology. Here we propose a post-regulation strategy-adjusting the pore structures of a standard "primitive" membrane to meet various separation needs-that greatly simplifies membrane preparation and accelerates technological advancement. Graphene quantum dots (GQDs) are introduced as innovative building blocks: a continuous GQD membrane is constructed by tightly stacking GQDs, and then its pore structure is tuned via heat treatment and in-situ cross-linking with small amine molecules. Combining adjustable angstrom-scale pores with preferential CO<sub>2</sub> adsorption, the resulting GQD membranes exhibit widely tunable CO<sub>2</sub>/N<sub>2</sub> and CO<sub>2</sub>/CH<sub>4</sub> separation performances. The CO<sub>2</sub> permeance and separation factors surpass most reported membranes and can be tuned to exceed industrial targets for CO<sub>2</sub> capture. By varying the heat treatment temperature, the separation scope of the membrane is further extended to challenging gas pairs such as C<sub>3</sub>H<sub>6</sub>/C<sub>3</sub>H<sub>8</sub>, demonstrating the high potential of this customizable post-regulation pore structure strategy.

</details>
<br>

**关键词**: graphene quantum dots, membrane materials, gas separation, pore structure, CO2 capture, post-regulation strategy, tunable separation performance

---

### 24. ❌ Segmented filamentous bacteria are worldwide human gut commensals

**作者**: Shashi Kiran, Ana Rita Cruz, Alice Daniau, Bing Ma, Martial Marbouty, Juliana Pipoli da Fonseca, Agnès Legrand, Lyam Baudry, Caroline Proux, Matthieu Bensussan, Maryse Moya-Nilges, Julian R. Garneau, Marc Monot, John B. Ochieng, Martin Antonio, Boubou Tamboura, Willem M. de Vos, Anne Salonen, Jahangir Hossain, Richard Omore
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70010-4](https://doi.org/10.1038/s41467-026-70010-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是人类肠道共生菌Segmented filamentous bacteria (SFB)的全球分布、分类和定植动态，属于微生物学、肠道菌群和免疫学领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像技术。所有关键词与论文主题无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This study establishes the presence of multiple SFB species in the human population and SFB as a minor but wide-spread group of commensals in humans.

!!! tip deepseek-chat TL;DR

    该研究首次在人类中鉴定并命名了一种名为Anisomitus miae的SFB物种，并基于16S rRNA基因序列在全球44个国家发现了多个SFB谱系，揭示了SFB作为广泛分布的人类肠道共生菌的定植动态和年龄相关性。

<details open>
<summary>摘要翻译</summary>

> 分段丝状细菌（SFB）指在哺乳动物、鱼类和鸟类中发现的一类形态相似的肠道共生菌。在小鼠中，SFB于断奶期紧密定植于回肠上皮，引发强烈的多效性免疫激活，这种作用既能增强定植抗性，又在多种疾病模型中加剧疾病严重程度。因此，SFB在健康与疾病中均具有关键作用，但关于人类SFB的信息仍十分有限。本研究首先鉴定并表征了一种人类SFB物种，其具有SFB典型的形态特征（包括介导附着的钩状尖端结构）和独特的基因组特征（包含淀粉与糖原降解模块）。我们将该物种命名为Anisomitus miae，并将其确立为SFB属的命名模式种，该物种在非洲地区普遍存在。随后，我们基于16S rRNA基因V3-V4可变区序列，通过生物信息学分析，在遍布六大洲的44个国家中识别出四个主要和两个次要的人类SFB谱系。我们提供了关于SFB谱系共定植潜力及其定植动态的证据，包括其在1至5岁儿童中存在一个强烈但短暂的定植高峰。本研究证实了人类群体中存在多种SFB物种，并表明SFB是人类中一类数量较少但分布广泛的共生菌群。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Segmented filamentous bacteria (SFB) describe morphologically similar gut commensals found in mammals, fish and birds. In mice, SFB intimately colonizes the ileal epithelium at the time of weaning and elicits a strong pleiotropic immune activation that fosters colonization resistance while augmenting disease severity in various disease models. SFB is therefore critical in both health and disease but information regarding SFB in humans remains limited. Here, we first identify and characterize a human SFB species with SFB-specific morphology, including the hook-like tip structure that mediates attachment, and unique genome features, including a starch and glycogen degradation module. This species, which we name Anisomitus miae and establish as the nomenclature type for the SFB genus, is common across Africa. We then bioinformatically identify, based on the 16S rRNA gene V3-V4 variable region sequence, four major, and two minor, human SFB lineages in forty-four countries distributed across all six inhabited continents. We provide evidence towards the co-colonization potential of the SFB lineages and their colonization dynamics, including a potent but short-lived colonization peak in children between one to five years of age. This study establishes the presence of multiple SFB species in the human population and SFB as a minor but wide-spread group of commensals in humans.

</details>
<br>

**关键词**: Segmented filamentous bacteria, human gut commensals, Anisomitus miae, 16S rRNA gene, global distribution, colonization dynamics, immune activation, microbiome

---

### 25. ❌ Going wild in banana breeding enables Fusarium-resistant hybrids with improved fruit quality

**作者**: Xin Liu, Ning Fu, Jia Li, Tian‐Wen Xiao, Shaohua Zeng, Rong Jiang, Xin-Feng Wang, Hui-Ye Zhang, Lei Wei, Lu-Yun Lu, Zheng-Feng Wang, Hai-Fei Yan, Linfeng Li, Mathieu Rouard, Xue-Jun Ge, Wei-Ming Li, H. Huang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70186-9](https://doi.org/10.1038/s41467-026-70186-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究香蕉育种、抗病性、基因组组装和杂交改良，主题是植物遗传学和农业科学，与医学影像分析、医学成像、深度学习医学成像等关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过鉴定野生香蕉Musa cheesmanii对镰刀菌的高抗性，将其与栽培品种杂交，培育出抗病性强、产量高、品质优的香蕉杂交种，并组装了其完整基因组以解析抗病机制。

<details open>
<summary>摘要翻译</summary>

> 香蕉（Musa spp.）对粮食安全至关重要，但现代栽培品种源自少数野生种并通过无性繁殖，遗传多样性低且抗病性弱。因此，鉴定新的亲本系对香蕉育种至关重要。本文研究表明，Musa cheesmanii 对尖孢镰刀菌古巴专化型热带4号生理小种（Fusarium oxysporum f. sp. cubense tropical race 4）表现出高抗性。我们将其与中国广泛种植的两个ABB型栽培品种‘玉林蕉’和‘金玉蕉’进行杂交。所得杂交种表现出增强的抗病性、高产、果肉口感优良以及货架期延长等特点，凸显了该野生种的育种价值。此外，本研究组装了M. cheesmanii 的端粒到端粒无间隙基因组，并通过多组学分析揭示了其物种分化、假茎黑色着色及抗病性的机制。总体而言，M. cheesmanii 是增加遗传多样性、改良香蕉品种的一个极具潜力的父本资源。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Bananas (Musa spp.) are crucial for food security, but modern cultivars derived from few wild species and propagated vegetatively possess low genetic diversity, and weak disease resistance. Identifying new parental lines is therefore essential for banana breeding. Here we show that Musa cheesmanii exhibits high resistance to Fusarium oxysporum f. sp. cubense tropical race 4. We cross it with two Musa ABB cultivars popular in China, 'Yulin' and 'Jinyu'. The resulting hybrids exhibit enhanced disease resistance, high yield, desirable pulp taste, and extended shelf-life, underscoring the breeding value of this wild species. Additionally, a telomere-to-telomere, gap-free genome of M. cheesmanii is assembled, with multi-omics analyses offering insights into its diversification, black pseudo-stem coloration, and disease resistance. Overall, M. cheesmanii is a promising male parent for enhancing genetic diversity and improving banana cultivars.

</details>
<br>

**关键词**: banana breeding, Fusarium resistance, Musa cheesmanii, genome assembly, hybrid cultivars, disease resistance, genetic diversity, multi-omics analysis

---

### 26. ❌ Root wounds facilitate the uptake of microplastics in crop plants

**作者**: Jingjing Yin, Xiaozun Li, Feng Cui, Yang Yu, Baoshan Xing, Fang Wang, Guoxin Xu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70273-x](https://doi.org/10.1038/s41467-026-70273-x)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究植物根系伤口如何促进微塑料在农作物中的吸收和转运，属于环境科学、植物生理学和农业科学领域。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均涉及医学影像分析，与论文内容完全无关。论文未涉及任何医学影像、图像分析或深度学习在医学影像中的应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that both shallowly wounded roots and unwounded roots exhibit effective resistance to the penetration of microplastics, providing substantial evidence that root wounds facilitate the uptake, translocation, and accumulation of microplastics in crops.

!!! tip deepseek-chat TL;DR

    该研究发现根系深部伤口为微塑料进入农作物（如芋头和玉米）提供了快速通道，导致微塑料在作物组织中积累，强调了防止根系损伤对食品安全的重要性。

<details open>
<summary>摘要翻译</summary>

> 微塑料可被植物根系吸收并进入食物链。在植物生命周期中，根系常遭遇各类物理损伤。然而，这些普遍存在的损伤是否构成微塑料进入植物的关键途径尚不明确。本研究证明，浅层根系损伤（仅限于皮层受损）与未受损根系均能有效抵抗微塑料渗透；相比之下，深层根系损伤（延伸至中柱的损伤）为微塑料进入芋头（Colocasia esculenta）和玉米（Zea mays）等作物提供了快速通道。在蛭石和土壤培养条件下，微塑料均可通过伤口暴露的木质部导管快速向上运输。当20%的根系遭受深层损伤并暴露于含50 mg kg⁻¹聚苯乙烯微塑料的蛭石中时，芋头球茎中的微塑料积累量达到161.1 ± 26.4（1 μm）和135.6 ± 24.9（5 μm）个/g，而玉米茎中积累量达503.4 ± 147.4（1 μm）和222.3 ± 63.8（5 μm）个/g。我们的研究为根系损伤促进微塑料在作物中的吸收、转运和积累提供了实质性证据，强调亟需通过规范农业操作来预防根系损伤以提升食品安全。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Microplastics can be absorbed by plant roots and enter the food chain. Throughout the plant life cycle, roots frequently encounter various physical injuries. However, whether these prevalent injuries serve as critical pathways for microplastics entry into plants remains unknown. Here, we demonstrate that both shallowly wounded roots (injuries limited to the cortex) and unwounded roots exhibit effective resistance to the penetration of microplastics. In contrast, deep wounds (injuries extending to the stele) in roots provide a rapid pathway for microplastics to enter crops such as taro (Colocasia esculenta) and maize (Zea mays). Microplastics are rapidly transported upward via wound-exposed xylem vessels in both vermiculite and soil culture conditions. When 20% of the roots were subjected to deep wounds and exposed to vermiculite containing 50 mg kg<sup>-1</sup> of polystyrene microplastics, the accumulation levels in taro corms reached 161.1 ± 26.4 (1 μm) and 135.6 ± 24.9 (5 μm) items g<sup>-1</sup>, while in maize stems reached 503.4 ± 147.4 (1 μm) and 222.3 ± 63.8 (5 μm) items g<sup>-1</sup>. Our findings provide substantial evidence that root wounds facilitate the uptake, translocation, and accumulation of microplastics in crops, underscoring the urgent need for proper farming practices to prevent root injuries and enhance food safety.

</details>
<br>

**关键词**: microplastics, root wounds, crop plants, uptake, translocation, food safety, polystyrene, xylem vessels

---

### 27. ❌ An H3K14ub-H3K9me3 feedback circuit governs heterochromatin spreading and inheritance in fission yeast

**作者**: Takenori Toda, Junyao Zang, Hongyun Qi, Yimeng Fang, Peng Jiang, Chun-Min Shan, Jiemin Wong, Songtao Jia
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70276-8](https://doi.org/10.1038/s41467-026-70276-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是裂殖酵母中异染色质传播和遗传的表观遗传调控机制，具体涉及H3K14ub-H3K9me3反馈回路、组蛋白修饰和染色质稳定性。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均与医学影像分析相关，而论文内容完全属于基础分子生物学和表观遗传学领域，未涉及任何医学影像、图像分析或深度学习在医学影像中的应用，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that H3K14ub and H3K9me3 form a feedback loop: H3K14ub strongly stimulates Clr4 activity on nucleosomes, while both H3K14ub and H3K9me3 stabilize CLRC binding to chromatin.

!!! tip deepseek-chat TL;DR

    该研究发现裂殖酵母中H3K14ub和H3K9me3形成一个反馈回路，通过整合泛素化、去乙酰化和甲基化调控异染色质的传播和遗传，而非仅依赖传统的H3K9me3'读写'循环。

<details open>
<summary>摘要翻译</summary>

> 异染色质是一种对基因组稳定性和基因调控至关重要的双稳态染色质状态。其扩散与遗传长期以来通过“读写”循环模型解释，即组蛋白甲基转移酶结合预先存在的组蛋白H3第9位赖氨酸三甲基化（H3K9me3）标记，并将此标记传播至相邻核小体。然而，仅靠H3K9me3所提供的弱亲和力与有限的催化刺激作用对这一模型提出了挑战。裂殖酵母的H3K9甲基转移酶Clr4在CLRC复合体内发挥作用，该复合体同时催化组蛋白H3第14位赖氨酸泛素化（H3K14ub）。本研究表明，H3K14ub与H3K9me3形成了一个反馈环路：H3K14ub强烈刺激Clr4对核小体的活性，而H3K14ub和H3K9me3共同稳定CLRC与染色质的结合。即使是破坏此反馈环路的细微扰动——例如突变三个H3基因之一以阻止泛素化或甲基化，或损害Clr3介导的H3K14去乙酰化——也会损害异染色质的扩散与遗传。相反，拮抗性活动，如Mst2催化的H3K14乙酰化和Epe1催化的H3K9去甲基化，则协同限制异染色质的扩张。因此，异染色质的维持并非仅仅依赖微弱的H3K9me3“读写”循环，而是通过一个整合了泛素化、去乙酰化和甲基化的调控电路来实现，该电路共同主导了其扩散与遗传过程。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Heterochromatin is a bistable chromatin state essential for genome stability and gene regulation. Its spreading and inheritance have long been explained by a "read-write" cycle in which histone methyltransferases bind pre-existing tri-methylation of histone H3 lysine 9 (H3K9me3) and propagate this mark to neighboring nucleosomes. However, the weak affinity and limited catalytic stimulation provided by H3K9me3 alone challenge this model. The fission yeast H3K9 methyltransferase Clr4 functions within the CLRC complex, which also catalyzes histone H3 lysine 14 ubiquitination (H3K14ub). Here we show that H3K14ub and H3K9me3 form a feedback loop: H3K14ub strongly stimulates Clr4 activity on nucleosomes, while both H3K14ub and H3K9me3 stabilize CLRC binding to chromatin. Even subtle perturbations that disrupt this feedback, such as mutating one of the three H3 genes to prevent ubiquitination or methylation, or impairing Clr3-mediated H3K14 deacetylation, compromises heterochromatin spreading and inheritance. Conversely, counteracting activities, such as H3K14 acetylation by Mst2 and H3K9 demethylation by Epe1, synergistically constrains heterochromatin expansion. Thus, rather than relying solely on the weak H3K9me3 "read-write" cycle, heterochromatin is maintained through an integrated circuit of ubiquitination, deacetylation, and methylation, which governs spreading and inheritance.

</details>
<br>

**关键词**: heterochromatin, H3K14ub, H3K9me3, feedback loop, Clr4, chromatin inheritance, histone modification, fission yeast

---

### 28. ❌ Multicomponent solid-solution alloy negative electrode for Li-metal batteries

**作者**: Jinxi Wang, Jiawen Zhu, Yichao Cai, Huimin Zhang, Xinpeng Li, Zongzi Jin, Zhuoying Zhu, Deguang Liu, Zhen Zhang, Peichen Zhong, Yuansen Xie, Wenhui Zhu, Guolei Cai, Huanyu Xie, Rong Huang, Yuhao Lu, Shuhong Jiao, Song Jin, Hengxing Ji
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70301-w](https://doi.org/10.1038/s41467-026-70301-w)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是锂金属电池的负极材料（多组分固溶体合金），属于电化学储能领域，与医学图像分析、医学成像或深度学习医学成像完全无关。论文内容涉及电池材料、电化学性能、循环寿命等，未提及任何医学图像相关技术或应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究锂金属电池负极材料，通过开发一种多组分固溶体合金负极，实现了无枝晶生长和高可逆比容量（3100 mAh g⁻¹），使1安时软包电池在600次循环后仍保持82%的容量。

<details open>
<summary>摘要翻译</summary>

> 锂金属电池因锂金属的高理论比容量而具备高理论比能量。然而，实际应用需要降低负极中的锂质量分数和锂利用率，以提升循环寿命并抑制枝晶生长，这导致其实际可逆容量仅为理论值的30%至50%。本文提出了一种基于锂金属的多组分固溶体合金，其锂含量约为90 wt.%，其余10 wt.%由原子比例相等的镉、银、镁和铝构成。增加的混合熵使锂原子具有高扩散性，促使锂向金属箔内部传输，而非传统锂金属负极中常见的表面沉积，同时促进了热力学稳定的（110）晶面的形成。这些因素共同作用，产生了一种无枝晶的负极，其可逆比容量达到3100 mAh g<sup>-1</sup>。采用该负极与LiNi<sub>0.8</sub>Co<sub>0.1</sub>Mn<sub>0.1</sub>O<sub>2</sub>正极所制备的一安时软包电池，其比能量达到385 Wh kg<sup>-1</sup>（基于软包电池总质量），且在600次循环后容量保持率为82%。这一成果凸显了该合金负极在实现安全、耐用且高能量密度锂金属电池实际应用方面的潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Lithium metal batteries possess the high theoretical specific energy owing to the high theoretical specific capacity of lithium metal. However, practical implementations necessitate a reduction in both lithium mass fraction and lithium utilization within the negative electrode to enhance cycling life and suppress dendrite formation, resulting in a practical reversible capacity of only 30 - 50% of the theoretical value. Herein, we present a lithium metal-based multicomponent solid-solution alloy comprising approximately 90 wt.% lithium, with equal atomic ratios of cadmium, silver, magnesium, and aluminium constituting the remaining 10 wt.%. The increased mixing entropy enables high lithium-atom diffusivity, facilitating inward lithium transport into the metal foil rather than the surface deposition typically observed in conventional lithium metal negative electrodes, while simultaneously promoting a thermodynamically stable (110) crystal facet. These factors collectively yield a dendrite-free negative electrode with a reversible specific capacity of 3100 mAh g<sup>-1</sup>. One-ampere-hour pouch cells employing this negative electrode and a LiNi<sub>0.8</sub>Co<sub>0.1</sub>Mn<sub>0.1</sub>O<sub>2</sub> positive electrode achieve an specific energies of 385 Wh kg<sup>-1</sup> (based on the total mass of the pouch cell) with 82% capacity retention over 600 cycles. This achievement highlights the potential of this alloy negative electrode to enable safe and durable high-energy-density lithium metal batteries for practical applications.

</details>
<br>

**关键词**: lithium metal batteries, multicomponent solid-solution alloy, dendrite-free negative electrode, reversible specific capacity, high-energy-density, cycling stability, LiNi0.8Co0.1Mn0.1O2

---

### 29. ❌ TCF21 promotes epithelial-to-mesenchymal transition and cytoskeleton reorganization in uterine development and endometriosis

**作者**: Jingwen Zhu, Peili Wu, Yilei Ma, Zijun Peng, Hangwei Fa, Qin Liu, Mengyang Geng, Ruihui Lu, Cheng Zeng, Wu Ning, Deyu Zhang, Xin Gen Lei, Chao Peng, Yingfang Zhou, Yongfeng Shang, Jing Liang, Qing Xue
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-69551-5](https://doi.org/10.1038/s41467-026-69551-5)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究子宫内膜异位症的分子机制，聚焦于TCF21转录因子通过促进上皮-间质转化和细胞骨架重组调控子宫发育和疾病进程。全文涉及基因表达、信号通路、动物模型和临床样本分析，未提及任何医学影像技术、图像分析或深度学习在医学影像中的应用。因此，所有关键词均与论文内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Observations uncover the importance of the TCF21-LIMK2-cofilin axis in uterine development and endometriosis, supporting the pursuit of TCF21-LIMK2-cofilin targeting in the diagnosis and therapeutics of endometriosis.

!!! tip deepseek-chat TL;DR

    该研究发现转录因子TCF21通过激活LIMK2-cofilin信号轴促进上皮-间质转化和细胞骨架重组，从而调控子宫发育和子宫内膜异位症的发病机制。

<details open>
<summary>摘要翻译</summary>

> 子宫内膜异位症是一种常见的妇科疾病，与盆腔疼痛和不孕相关。尽管存在多种理论，其病因学与分子机制仍有待阐明。本文报道转录因子21（TCF21）通过促进上皮-间质转化（EMT）与细胞骨架重组，调控子宫发育及子宫内膜异位症的发病机制。小鼠子宫特异性敲除Tcf21可促进子宫内膜EMT及子宫发育异常。相应地，子宫内膜异位症患者在位与异位内膜中均呈现TCF21高表达及间质细胞群扩增。对患者来源异位间质细胞的整合表观基因组与转录组分析显示，TCF21转录激活了一系列基因，其中包括关键参与细胞骨架组织的LIMK2。事实上，TCF21在间质细胞中激活的LIMK2-cofilin信号通路与肌动蛋白细胞骨架重组、细胞侵袭及黏附能力增强相关。在外科手术构建的小鼠模型中，在位内膜间质细胞中敲低Tcf21可减轻异位病灶；而使用AAV-Pgr-Tcf21处理小鼠则会增加子宫内膜异位症发生率，该效应可通过给予LIM激酶抑制剂LIMKi 3得以缓解。这些发现揭示了TCF21-LIMK2-cofilin轴在子宫发育及子宫内膜异位症中的重要作用，为靶向该通路进行子宫内膜异位症的诊断与治疗提供了依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Endometriosis is a common gynecological disease associated with pelvic pain and infertility. Despite several existing theories, the etiology and molecular mechanisms of endometriosis remain to be investigated. Here we report that transcription factor 21 (TCF21) regulates uterine development and endometriosis pathogenesis by promoting epithelial-to-mesenchymal transition (EMT) and cytoskeleton reorganization. Uterine-specific knockout of Tcf21 in mice promotes EMT of the endometrium and dysplasia of the uterus. Accordingly, patients with endometriosis exhibit high TCF21 expression and an expanded population of stromal cells in both eutopic and ectopic endometria. Integrative epigenomic and transcriptomic analyses in patient-derived ectopic stromal cells reveal that TCF21 transcriptionally activated a cohort of genes, including LIMK2, which is critically involved in cytoskeleton organization. Indeed, TCF21-activated LIMK2-cofilin signaling in stromal cells is associated with actin-cytoskeleton reorganization and increased cell invasion and adhesion. In a surgically constructed mouse model, depletion of Tcf21 in eutopic stromal cells alleviates endometriotic lesions, whereas treatment of mice with AAV-Pgr-Tcf21 leads to increased endometriosis incidence, which could be mitigated by administering the LIM kinase inhibitor LIMKi 3. These observations uncover the importance of the TCF21-LIMK2-cofilin axis in uterine development and endometriosis, supporting the pursuit of TCF21-LIMK2-cofilin targeting in the diagnosis and therapeutics of endometriosis.

</details>
<br>

**关键词**: TCF21, endometriosis, epithelial-to-mesenchymal transition, cytoskeleton reorganization, LIMK2-cofilin axis, uterine development, stromal cells, transcriptional regulation

---

### 30. ❌ Pathways to global hydrogen production within planetary boundaries

**作者**: Michaël Lejeune, Sami Kara, Cécile Guignard, Sareh Shahrabifarahani, Rahman Daiyan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70168-x](https://doi.org/10.1038/s41467-026-70168-x)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是全球清洁氢生产的行星边界影响，属于能源与环境科学领域，完全不涉及医学图像分析、医学成像或深度学习医学成像等医疗技术主题。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究量化了全球清洁氢生产的行星足迹，发现即使最有利情景下氢生产仍可能不可持续，且地球系统相互作用会放大其影响，与当前对'绿氢'的关注形成对比。

<details open>
<summary>摘要翻译</summary>

> 氢是实现难以电气化领域脱碳的关键杠杆。减排情景预测氢在使人类活动回归气候变化行星边界方面将发挥关键作用。然而，其行星足迹仍不明确，特别是在考虑地球系统相互作用时。本文通过结合自下而上的系统模型与地球系统相互作用模型，量化了全球清洁氢生产的行星足迹。从2025年至2050年，即使在最有利的情景下，全球氢生产也很可能不可持续，这证实了先前的研究发现。我们进一步表明，地球系统相互作用会放大氢的行星足迹。尽管电解制氢与化石燃料减排制氢具有互补性，但生物质制氢的不可持续性要高出一个数量级，这与当前趋势相反。我们的研究结果与当前聚焦于“绿氢”的潮流形成对比，后者并未揭示其可持续性。实现可持续的氢生产需要重新审视可行的生产路径，首先应从现有产能的脱碳开始。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Hydrogen is a key lever for decarbonising hard-to-electrify sectors. Mitigation scenarios project an essential role for hydrogen in returning within the climate change planetary boundary. Yet, its planetary footprint remains unclear, particularly when Earth system interactions are considered. Here, we quantify the planetary footprint of global clean hydrogen production using a bottom-up system model coupled with an Earth system interaction model. From 2025 to 2050, even under the most favourable scenarios, global hydrogen production is likely unsustainable, confirming previous findings. We further show that Earth system interactions amplify hydrogen's planetary footprint. While electrolytic and abated fossil production are complementary, bio-based production is an order of magnitude more unsustainable, as opposed to current trends. Our results contrast with the current focus on "green hydrogen" which does not inform on its sustainability. Achieving sustainable hydrogen production will require the reconsideration of viable production pathways, starting with the decarbonisation of existing production capacity.

</details>
<br>

**关键词**: hydrogen production, planetary boundaries, sustainability, Earth system interactions, clean hydrogen, decarbonisation, global footprint

---

### 31. ❌ Post-catalysis structures of mitochondrial complex I with ubiquinol-10 bound in the active site

**作者**: Injae Chung, Caroline S. Pereira, J. J. Wright, Guilherme M. Arantes, J. P. P. Hirst
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70030-0](https://doi.org/10.1038/s41467-026-70030-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是线粒体复合物I的催化后结构，使用电子冷冻显微镜技术解析蛋白质结构，属于结构生物学和生物化学领域。论文完全不涉及医学图像分析、医学成像或深度学习医学成像，这些关键词与论文内容无任何关联。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Highly hydrated structures exhibit near-continuous proton-transfer connections along the length of the membrane domain, enabling comparisons between them to assist in identifying the proton-transfer control points that are essential to catalysis.

!!! tip deepseek-chat TL;DR

    该研究使用电子冷冻显微镜解析了哺乳动物线粒体复合物I与还原型泛醌-10结合的催化后结构，揭示了泛醌还原过程中的底物结合构象和质子转移通道。

<details open>
<summary>摘要翻译</summary>

> 呼吸复合体I是一种多亚基能量转导膜酶，对线粒体及细胞能量代谢至关重要。它将NADH氧化与泛醌-10（Q<sub>10</sub>）还原偶联，同时泵出四个质子以形成驱动氧化磷酸化的质子动力势。尽管近期在复合体I结构研究方面取得进展，其诸多机制细节仍不明确，包括Q<sub>10</sub>的反应性结合构象、Q<sub>10</sub>还原如何启动质子传递级联反应，以及质子如何穿越膜结构域。本研究采用冷冻电镜技术解析了哺乳动物复合体I的结构样本——该样本重构于含有外源性Q<sub>10</sub>的磷脂纳米盘并经NADH还原，整体分辨率达2.0至2.6 Å。我们观测到还原型Q<sub>10</sub>H<sub>2</sub>分子的两种构象，在催化相关的闭合状态下完全嵌入Q结合通道。通过比较氧化态与还原态复合体I结构中结合的醌类物质，并结合分子动力学模拟研究关键周围残基的电荷状态，我们提出了Q<sub>10</sub>在还原过程中经历的一系列底物结合构象。这些高度水合化的结构显示出沿膜结构域纵向近乎连续的质子传递通道，通过结构对比有助于识别对催化至关重要的质子传递控制位点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Respiratory complex I is a multi-subunit energy-transducing membrane enzyme essential for mitochondrial and cellular energy metabolism. It couples NADH oxidation and ubiquinone-10 (Q<sub>10</sub>) reduction to the concomitant pumping of four protons to generate the proton-motive force that powers oxidative phosphorylation. Despite recent advances in structural knowledge of complex I, many mechanistic aspects including the reactive binding poses of Q<sub>10</sub>, how Q<sub>10</sub> reduction initiates the proton transfer cascade, and how protons move through the membrane domain, remain unclear. Here, we use electron cryomicroscopy to determine structures of mammalian complex I, reconstituted into phospholipid nanodiscs containing exogenous Q<sub>10</sub> and reduced by NADH, to global resolutions of 2.0 to 2.6 Å. Two conformations of a reduced Q<sub>10</sub>H<sub>2</sub> molecule are observed, fully inserted into the Q-binding channel in the turnover-relevant closed state. By comparing the quinone species bound in oxidised and reduced complex I structures, paired with molecular dynamics simulations to investigate the charge states of key surrounding residues, we propose a series of substrate binding poses that Q<sub>10</sub> transits through for reduction. Our highly hydrated structures exhibit near-continuous proton-transfer connections along the length of the membrane domain, enabling comparisons between them to assist in identifying the proton-transfer control points that are essential to catalysis.

</details>
<br>

**关键词**: mitochondrial complex I, ubiquinol-10, electron cryomicroscopy, proton transfer, quinone reduction, membrane enzyme, structural biology, NADH oxidation

---

### 32. ❌ DiNovo enables high-coverage and high-confidence de novo peptide sequencing via mirror proteases and deep learning

**作者**: Zixuan Cao, Xiu Peng, Di Zhang, Piyu Zhou, Kang Li, Hao Chi, Ruitao Wu, Zhiyuan Cheng, Yao Zhang, Jiaxing Dai, Yong Li, Lijin Yao, Xiaoyao Li, Y. He, Jinghan Yang, Haipeng Wang, Ping Xu, Yan Fu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-70224-6](https://doi.org/10.1038/s41467-026-70224-6)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文《DiNovo enables high-coverage and high-confidence de novo peptide sequencing via mirror proteases and deep learning》的研究领域是蛋白质组学（proteomics）和肽段测序（peptide sequencing），具体涉及使用镜像蛋白酶和深度学习算法进行从头肽段测序。虽然论文使用了深度学习技术，但其应用对象是质谱数据（mass spectrometry data）和肽段序列，而非医学图像（如X光、CT、MRI等）。评分关键词“medical image analysis”、“medical imaging”和“deep learning medical imaging”均明确指向医学图像处理领域，与论文的蛋白质组学主题完全无关。因此，所有关键词的相关度评分均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Compared with the trypsin protease used alone, DiNovo using two pairs of mirror proteases leads to two to three times high-confidence amino acids sequenced and shows great potential as a practical and powerful alternative to database search for peptide identification with quality control.

!!! tip deepseek-chat TL;DR

    该论文解决了单蛋白酶蛋白质组学实验中肽段测序覆盖率低和置信度不足的问题，通过开发DiNovo软件系统，利用镜像蛋白酶互补性和深度学习算法，实现了更高覆盖率和置信度的从头肽段测序。

<details open>
<summary>摘要翻译</summary>

> 尽管深度学习近期取得了进展，但基于单一蛋白酶的蛋白质组学实验中，不完全的肽段碎裂和不足的蛋白质酶切仍然制约着从头肽段测序的发展。本文提出一款名为DiNovo的软件系统，通过利用镜像蛋白酶的互补性，实现高覆盖度、高可信度的从头肽段测序。DiNovo由多项创新算法驱动，包括不依赖于预测序的镜像谱图识别算法、分别基于深度学习和图论的两种测序算法，以及无需先验肽段鉴定的测序结果评估方法——靶向-诱饵映射。与单独使用胰蛋白酶相比，采用两对镜像蛋白酶的DiNovo可测序的高可信度氨基酸数量增加两到三倍。与以往的单蛋白酶从头测序算法相比，DiNovo实现了显著更高的序列覆盖度。该软件还展现出作为具备质量控制的数据搜索方法的一种实用且强大的替代方案，在肽段鉴定方面具有巨大潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Despite the recent advancements driven by deep learning, de novo peptide sequencing is still constrained by incomplete peptide fragmentation and insufficient protein digestion in current single protease-based proteomic experiments. Here, we present a software system, named DiNovo, for high-coverage and high-confidence de novo peptide sequencing by leveraging the complementarity of mirror proteases. DiNovo is empowered by several innovative algorithms, including a mirror-spectra recognition algorithm independent of pre-sequencing, two sequencing algorithms based on deep learning and graph theory, respectively, and target-decoy mapping, a method for sequencing result evaluation free of prior peptide identification. Compared with the trypsin protease used alone, DiNovo using two pairs of mirror proteases leads to two to three times high-confidence amino acids sequenced. Compared with previous single-protease de novo sequencing algorithms, DiNovo achieves much higher sequence coverage. DiNovo also shows great potential as a practical and powerful alternative to database search for peptide identification with quality control.

</details>
<br>

**关键词**: de novo peptide sequencing, mirror proteases, deep learning, proteomics, mass spectrometry, sequence coverage, peptide identification, DiNovo

---

### 33. ❌ Martian ionospheric response during the may 2024 solar superstorm

**作者**: Jacob Parrott, Beatriz Sánchez-Cano, H. Svedhem, Olivier Witasse, Dikshita Meggi, Colin Wilson, Alejandro Cardesín-Moinelo, Ingo C.F. Müller-Wodarg
**期刊/来源**: nature_communications
**发布日期**: 2026-03-05
**DOI**: [10.1038/s41467-026-69468-z](https://doi.org/10.1038/s41467-026-69468-z)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要均未提及医学图像分析相关内容。论文研究火星电离层对2024年5月太阳超级风暴的响应，属于行星科学和空间物理学领域，与医学图像分析、医学成像、深度学习医学成像等关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了2024年5月太阳超级风暴期间火星电离层的响应，发现风暴导致电离层电子密度显著增加并改变了其垂直结构。

**关键词**: Martian ionosphere, solar superstorm, May 2024, ionospheric response, electron density, vertical structure, space weather

---

### 34. ❌ Convergent evolutionary shifts in AGT targeting between mitochondria and peroxisomes across mammal transitions to herbivory

**作者**: Chen Huang, Bingjun Wang, Jun Yu, Stephen J. Rossiter, Huabin Zhao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-70246-0](https://doi.org/10.1038/s41467-026-70246-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是哺乳动物食草性进化过程中AGT酶（丙氨酸:乙醛酸氨基转移酶）的亚细胞定位机制，涉及比较基因组学、功能实验和转录组分析，属于进化生物学和分子生物学领域。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均与医学影像分析相关，而论文完全不涉及任何医学影像、图像处理或深度学习在医学影像中的应用，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A central role of AGT peroxisomal targeting efficiency, driven by the PTS1 motif, plays a crucial role in adapting to plant-based diets, and increased targeting efficiency has evolved convergently via the interplay of transcriptional regulation and targeting signals.

!!! tip deepseek-chat TL;DR

    本研究揭示了在哺乳动物向食草性进化过程中，AGT酶通过PTS1基序的过氧化物酶体靶向效率提升以及转录调控的协同作用，实现了向植物性饮食适应的趋同进化机制。

<details open>
<summary>摘要翻译</summary>

> 在哺乳动物多样化进程中，植食性多次独立演化，对这一全球分布类群的成功起到关键作用。植食动物面临的核心代谢挑战是乙醛酸的解毒过程。丙氨酸：乙醛酸氨基转移酶（AGT）能将乙醛酸转化为甘氨酸，从而阻止有害草酸钙晶体的形成。AGT分别通过线粒体靶向序列（MTS）和过氧化物酶体靶向信号（PTS1）定位于线粒体与过氧化物酶体。尽管多数研究集中于MTS，但仅MTS的变异无法完全解释AGT的定位模式。为评估PTS1基序的相对重要性，我们结合比较序列分析与功能实验进行研究。我们发现多个植食性谱系经历了独立突变，导致MTS区域被破坏或截短，而PTS1基序始终保持功能。免疫荧光实验显示，植食动物中AGT的过氧化物酶体定位效率更高，即使MTS完整时，PTS1也常能覆盖线粒体靶向信号。此外，转录组分析表明若干植食谱系优先使用下游转录起始位点，产生缺乏MTS的AGT亚型。综上，我们的研究揭示了AGT过氧化物酶体靶向在植食性演化中的核心作用，并阐明了通过转录调控与靶向信号的相互作用，如何趋同演化出更高的靶向效率。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Herbivory has evolved multiple times during mammalian diversification, playing a key role in the success of this globally distributed clade. A central metabolic challenge for herbivores is the detoxification of glyoxylate. The enzyme alanine:glyoxylate aminotransferase (AGT) converts glyoxylate to glycine, preventing the formation of harmful calcium oxalate crystals. AGT localizes to mitochondria and peroxisomes based on the mitochondrial targeting sequence (MTS) and the peroxisomal targeting signal (PTS1), respectively. While most studies focused on MTS, MTS variation alone does not fully explain AGT localization patterns. To assess the relative importance of the PTS1 motif, we combined comparative sequence analyses with functional assays. We find that multiple herbivorous lineages underwent independent mutations resulting in disrupted or truncated MTS regions, whereas the PTS1 motif remains functional. Immunofluorescence assays revealed more efficient peroxisomal localization of AGT in herbivores, with PTS1 often overriding mitochondrial signals even when the MTS is intact. Additionally, transcriptomic analyses show that several herbivorous lineages preferentially use downstream transcriptional start sites, producing AGT isoforms lacking the MTS. Together, our findings reveal a central role of AGT peroxisomal targeting in evolution of plant-based diets, and demonstrate how increased targeting efficiency has evolved convergently via the interplay of transcriptional regulation and targeting signals.

</details>
<br>

**关键词**: AGT, peroxisomal targeting, herbivory evolution, convergent evolution, mitochondrial targeting sequence, PTS1 motif, transcriptional regulation, mammalian adaptation

---

### 35. ❌ Inverse-designed nanophotonic neural network accelerators for ultra-compact optical computing

**作者**: Joel Sved, Shijie Song, Liwei Li, George Li, Debin Meng, Xiaoke Yi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**arXiv链接**: [https://arxiv.org/abs/2506.06150](https://arxiv.org/abs/2506.06150)
**DOI**: [10.1038/s41467-026-68648-1](https://doi.org/10.1038/s41467-026-68648-1)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确聚焦于光学计算和神经网络加速器的逆向设计，涉及纳米光子学、光学神经网络和计算硬件。所有关键词均与医学图像分析相关，但论文内容完全不涉及医学、医疗、图像分析或任何医疗应用领域。论文讨论的是通用光学计算加速器，而非特定医学应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过逆向设计方法开发了超紧凑的纳米光子神经网络加速器，用于高效的光学计算。

**关键词**: inverse-designed, nanophotonic, neural network accelerators, ultra-compact, optical computing, neural networks, photonic devices

---

### 36. ❌ Dolutegravir restores gut microbiota in late-stage HIV-1 unlike darunavir: an open-label, randomized clinical trial

**作者**: Francesc Català‐Moll, Carlos Blázquez-Bondia, Judit Farré-Badia, Francesc Torres, Christian Manzardo, Eva Bonfill, Adrià Curran, P. Domingo, D Podzamczer, Lluís Force, Choy Man, Mariona Parera, María Casadellà, José M. Miró, Marc Noguera-Julian, Roger Paredes, ADVANZ-4 MISTRAL investigators, Alessandra Borgognone, Nel Marín, Oriol Careta
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-69846-7](https://doi.org/10.1038/s41467-026-69846-7)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是HIV-1治疗药物（Dolutegravir vs Darunavir）对肠道菌群的影响，属于传染病学、微生物学和临床药理学领域。论文标题、摘要和内容均未涉及医学影像分析、医学成像或深度学习医学成像技术，与所有评分关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Dolutegravir-based therapy restores the gut microbiota more effectively than darunavir/ritonavir in patients who present late with HIV, and that recovery is linked to improved immune reconstitution.

!!! tip deepseek-chat TL;DR

    这项开放标签随机临床试验比较了Dolutegravir和Darunavir对晚期HIV-1患者肠道菌群的影响，发现Dolutegravir能恢复肠道菌群而Darunavir不能。

**关键词**: Dolutegravir, Darunavir, HIV-1, gut microbiota, randomized clinical trial, late-stage HIV, ADVANZ-4 MISTRAL, antiretroviral therapy

---

### 37. ❌ Minimal N-hydroxyphthalimide-urethane bonds enable superior thermomechanical stability for covalent adaptable networks

**作者**: Yuhan Yin, Shijia Yang, Yong Zhou, ZhuSheng Yang, Zhi Qiao, Fu-Lin Gao, Pan Ma, Qian-Nan Bi, Shuaiyuan Wang, Leiyu Chen, Wangmao Tian, Wenxing Liu, Jian Xu, Ning Zhao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-70151-6](https://doi.org/10.1038/s41467-026-70151-6)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是高分子材料科学领域，具体涉及共价适应性网络（CANs）的热机械稳定性改进，通过动态N-羟基邻苯二甲酰亚胺-氨基甲酸酯键（NUBs）实现。论文内容完全围绕材料化学、聚合物网络设计和动态共价键展开，与医学图像分析、医学成像或深度学习医学成像没有任何关联。所有关键词均得0分，因为论文主题与这些医学图像领域完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文通过开发一种“高活性低含量”策略，利用动态N-羟基邻苯二甲酰亚胺-氨基甲酸酯键，使共价适应性网络在保持优异可再加工性的同时，实现了卓越的热机械稳定性和机械性能，克服了传统性能权衡问题。

<details open>
<summary>摘要翻译</summary>

> 相较于传统热固性材料，由动态共价键（DCBs）赋予的共价自适应网络（CANs）虽具备可再加工性，却往往以牺牲机械性能和热机械稳定性为代价。本文提出一种“高活性、低含量”策略，通过动态N-羟基邻苯二甲酰亚胺-氨基甲酸酯键（NUBs）使CANs实现优异的热机械稳定性。在二甲基亚砜中，N-羟基邻苯二甲酰亚胺与异氰酸酯之间的无催化剂加成反应在室温下2小时内即可达到接近定量的转化率，而所形成的键在120°C下解离率甚至可达约28%。这种兼具高解离度和快速结合动力学的双重高活性，使得在保持CANs动态特性的同时，有效降低其内部动态共价键含量成为可能。我们仅引入5 mol%的动态单元，成功构建了聚(N-羟基邻苯二甲酰亚胺-氨基甲酸酯)（PNU）网络。这种“高活性、低含量”的设计赋予PNU材料优异的机械性能、卓越的裂纹容忍度以及高温下显著的结构稳定性。此外，即使在动态共价键参与度极低的情况下，PNU仍表现出良好的可再加工性，并在中性水环境中具备温和的降解能力。本研究提出了一种极具说服力的策略，使CANs能够在保持机械强度和热机械稳定性的同时实现优异的可再加工性——从而突破了这些性能之间传统的权衡关系。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Compared to classic thermosets, the reprocessability of covalent adaptable networks (CANs) endowed by dynamic covalent bonds (DCBs) often comes at the expense of mechanical performance and thermomechanical stability. Herein, we report a "High Activity & Low Content" strategy for CANs to achieve superior thermomechanical stability, which is enabled by dynamic N-hydroxyphthalimide-urethane bonds (NUBs). The catalyst-free addition reaction between N-hydroxyphthalimides and isocyanates proceeds to a near-quantitative conversion within 2 h at room temperature in dimethyl sulfoxide, while the formed bonds dissociate even up to ~ 28% at 120 °C. The dual high activity, characterized by a high degree of dissociation and fast association kinetics, allows for an effective reduction in DCB content within CANs while preserving their dynamic characteristics. We incorporate only 5 mol% of dynamic units to develop poly(N-hydroxyphthalimide-urethanes) (PNU) networks. The "High Activity & Low Content" design endows PNUs with superior mechanical properties, exceptional crack tolerance, and remarkable mechanical stability at high temperatures. Furthermore, even with minimal DCB participation, the PNUs exhibit excellent reprocessability and mild degradability in neutral aqueous conditions. This study proposes a compelling strategy that enables CANs to achieve excellent reprocessability while retaining their mechanical strength and thermomechanical robustness-overcoming the traditional trade-off between these properties.

</details>
<br>

**关键词**: covalent adaptable networks, dynamic covalent bonds, N-hydroxyphthalimide-urethane bonds, thermomechanical stability, reprocessability, mechanical properties, poly(N-hydroxyphthalimide-urethanes), High Activity & Low Content strategy

---

### 38. ❌ Stretch-induced reversible self-growth of high aspect ratio microstructures scribed by femtosecond laser

**作者**: Yan Zhang, Nian Zhang, Dong Wu, Zehang Cui, Hong Liu, T. Wang, Rui Xu, Kejia Lu, Zhaoxin Lao, Sizhu Wu, Jiawen Li, Liu Wang, Ying Li, Li Zhang, Jiaru Chu, Yanlei Hu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-70098-8](https://doi.org/10.1038/s41467-026-70098-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是利用飞秒激光切割和拉伸弹性膜制造可调谐微结构的方法（SIPS），应用于微纳制造、自适应表面工程、盲文训练和信息加密等领域。全文未涉及医学图像分析、医学成像或深度学习医学成像的任何内容，与所有评分关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种基于拉伸诱导聚合物自生长（SIPS）和飞秒激光切割的方法，用于在弹性膜上可逆地制造高纵横比微结构，并展示了其在信息加密和触觉感知等领域的应用潜力。

<details open>
<summary>摘要翻译</summary>

> 受自然界复杂表面图案的启发，聚合物自生长概念近年来被应用于构建合成结构。然而，现有技术——无论是基于化学反应还是物理传质驱动——均无法实现快速可逆的调控，且通常只能制备低深宽比的结构。本文提出了一种通用的拉伸诱导聚合物自生长方法，可在多种预拉伸弹性膜上可逆地构建结构，包括硅胶、聚氨酯、聚二甲基硅氧烷、介电弹性体及水凝胶。通过飞秒激光切割，可便捷地制备具有不同截面形状的高深宽比直线与弯曲微柱。当释放并重新拉伸基底膜时，可实现生长结构的灵活调控，使表面在结构化与平坦状态之间实现快速可逆转变。实验与模拟结果证实，微柱高度由拉伸比和激光刻蚀深度共同决定。高深宽比特性增强了触觉感知能力，并可通过定向弯曲实现信息编码。这些功能在盲文训练和信息加密/解密的原理性应用中得到了验证。本研究所提出的SIPS方法，结合了飞秒激光切割与弹性膜拉伸技术，为制备可调谐功能微结构提供了一种高效途径，在微纳制造与自适应表面工程领域具有广阔的应用前景。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Inspired by the intricate surface patterns in nature, the concept of polymer self-growth has recently been applied to construct synthetic structures. However, existing techniques, whether driven by chemical reactions or physical mass transport, fail to offer rapid and reversible tuning, and typically can only produce structures with low aspect ratios. Here, we present a generalized stretch-induced polymer self-growth (SIPS) method for reversibly constructing structures on a wide range of pre-stretched elastic membranes, including silicone, PU, PDMS, dielectric elastomer (VHB), and hydrogel. High aspect ratio (~1.4, much larger than the previously reported value ~ 0.25) straight and bent micropillars with different cross-sections are facilely fabricated by femtosecond laser cutting. By releasing and subsequent re-stretching the membrane, tuning of the grown structures is readily achievable, enabling a rapid (~ 30 s) and reversible transition between structured and flat surface. Experimental and simulation results confirm that the micropillar height is governed by the stretch ratio and laser scribing depth. The high aspect ratio enhances tactile perception and allows directional bending for encoding information. These capabilities are demonstrated through proof-of-concept applications in Braille training and information encryption/decryption. The presented SIPS method that combines femtosecond laser cutting and the stretching of elastic membranes, offers an efficient approach for fabricating tunable functional microstructures with great potential in the fields of micro/nanofabrication and adaptive surface engineering.

</details>
<br>

**关键词**: stretch-induced polymer self-growth, femtosecond laser cutting, high aspect ratio microstructures, reversible tuning, elastic membranes, information encryption, tactile perception, adaptive surface engineering

---

### 39. ❌ Inhibiting Mrt4-rRNA interaction with fumaramidmycin-based derivatives as an antifungal strategy

**作者**: Hongxuan Cao, Jie Tu, Jana Shen, Bingzhang Chen, Zeyue Huang, Yingjie Wang, Jing Shen, Xiuqi Hu, Jialin Bo, Li Rao, Zheng Liu, Nokwanda P. Makunga, Muhammad Salman Hameed, Chen Su, Jian Wan, Wenqiang Chang, Chunquan Sheng, Yanliang REN
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-70226-4](https://doi.org/10.1038/s41467-026-70226-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是抗真菌药物开发，通过化学方法抑制Mrt4-rRNA相互作用来破坏真菌核糖体组装，涉及药物筛选、化学遗传学分析和动物模型验证。全文未提及医学图像分析、医学成像或深度学习医学成像相关内容，与这些关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The development of cis-fumaramidmycin-derived analogs inhibiting the interactions of ribosome assembly factor Mrt4 with rRNA to combat fungal infections provides a potential and much needed therapeutic strategy to address the rapidly rising burden of drug-resistant fungal infections.

!!! tip deepseek-chat TL;DR

    该研究开发了基于顺式富马酰胺霉素衍生物的抗真菌策略，通过选择性抑制CaMrt4-rRNA相互作用破坏真菌核糖体组装，有效对抗包括耳念珠菌在内的耐药真菌感染。

<details open>
<summary>摘要翻译</summary>

> 当前抗真菌药物耐药性的上升及现有治疗手段的局限性，凸显了对创新抗真菌策略的迫切需求。本文报道了通过抑制核糖体组装因子Mrt4与rRNA相互作用来对抗真菌感染的顺式富马酰胺霉素衍生物类似物的开发。通过抗真菌活性筛选，我们鉴定出先导化合物20，其对多种耐药真菌（包括 notorious super-fungus Candida auris）均表现出强效抑制活性。结合活性与非活性导向的蛋白质谱分析（AIBPP）、化学遗传谱分析以及荧光偏振实验的综合研究表明，化合物20的抗真菌活性主要源于其能选择性抑制关键的CaMrt4-rRNA相互作用，其机制是通过共价结合CaMrt4上的C96和C189位点，而对HuMrt4-rRNA相互作用无影响，从而破坏真菌核糖体组装。化合物20在Galleria mellonella幼虫模型和小鼠念珠菌感染模型中均展现出良好的治疗效果，验证了该抗真菌策略的有效性。综上所述，我们的研究为应对日益严峻的耐药真菌感染负担提供了一种潜在且亟需的治疗策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The rise of drug resistance and limitations of current antifungal treatments highlight the urgent need for innovative antifungal strategies. Here we present the development of cis-fumaramidmycin-derived analogs inhibiting the interactions of ribosome assembly factor Mrt4 with rRNA to combat fungal infections. Through antifungal screening, we identified a promising lead 20 with strong efficacy against various drug-resistant fungi, including notorious super-fungus Candida auris. A comprehensive approach combining active-and-inactive-based protein profiling (AIBPP), chemical-genetic profiling, and fluorescence polarization revealed that the antifungal activity of 20 is primarily due to selectively inhibiting essential CaMrt4-rRNA interaction by conjointly covalent engaging C96&C189 on CaMrt4 but inactive for HuMrt4-rRNA interaction, thereby disrupting fungal ribosomal assembly. Therapeutic efficacy of 20 in both Galleria mellonella larvae and murine candidiasis models validate this antifungal strategy. Collectively, our studies provide a potential and much needed therapeutic strategy to address the rapidly rising burden of drug-resistant fungal infections.

</details>
<br>

**关键词**: antifungal strategy, Mrt4-rRNA interaction, drug-resistant fungi, Candida auris, ribosomal assembly, chemical-genetic profiling, animal models

---

### 40. ❌ Stereodivergent synthesis of chiral amines bearing vicinal stereocenters via hydroamination of trisubstituted alkenes

**作者**: Haohao Bai, Yanyu Chen, Xiuping Wang, Tao Jiang, Lintao Zeng, Lanlan Zhang, Chao Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-70294-6](https://doi.org/10.1038/s41467-026-70294-6)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确表明这是一篇有机化学领域的论文，研究镍催化烯烃的不对称氢胺化反应，用于合成具有相邻手性中心的胺类化合物。全文未提及任何医学图像分析、医学成像或深度学习医学成像相关内容，与所有评分关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了手性胺类化合物立体发散性合成的长期挑战，通过镍催化非环三取代烯烃的不对称氢胺化反应，实现了具有β,γ-立体中心的手性胺的高效、可预测立体选择性合成。

<details open>
<summary>摘要翻译</summary>

> 含有邻位立体中心的手性脂肪胺是药物及生物活性分子中普遍存在的结构基元，然而高效且立体发散性地合成此类结构仍是长期存在的挑战。本文报道了一种镍催化的无环三取代烯烃对映选择性氢胺化反应，为构建含有β,γ-立体中心的手性胺提供了一个统一的立体发散性合成平台。该反应具有广泛的底物适用性，可兼容多种胺亲电试剂和三取代烯烃（包括衍生自复杂生物活性分子的烯烃），并表现出优异的区域选择性、非对映选择性和对映选择性。通过调控烯烃几何构型与手性双咪唑啉配体（chiral biimidazoline ligand）的构型，能够以可预测的方式获得全部四种立体异构体。该反应条件温和，耐受多种官能团，可实现后期官能化，证明了其在构建密集功能化三维胺类骨架方面的实用性。本工作为不对称合成提供了有价值的平台，在药物发现与分子设计领域具有巨大潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Chiral aliphatic amines bearing vicinal stereocenters are prevalent motifs in pharmaceuticals and bioactive molecules, yet efficient and stereodivergent access to these structures remains a longstanding challenge. Herein, we report a nickel-catalyzed enantioselective hydroamination of acyclic trisubstituted alkenes that provides a unified platform for the stereodivergent construction of chiral amines bearing β,γ-stereocenters. The reaction exhibits broad substrate scope, accommodating diverse amine electrophiles and tri-substituted alkenes, including those derived from complex bioactive molecules, with high levels of regio-, diastereo-, and enantioselectivity. By modulating the alkene geometry and the configuration of a chiral biimidazoline ligand, all four stereoisomers can be accessed in a predictable manner. The protocol proceeds under mild conditions, tolerates various functional groups, and enables late-stage derivatization, demonstrating its utility for constructing densely functionalized, three-dimensional amine scaffolds. This work provides a valuable platform for asymmetric synthesis and holds strong potential for drug discovery and molecular design.

</details>
<br>

**关键词**: chiral amines, hydroamination, trisubstituted alkenes, nickel catalysis, stereodivergent synthesis, enantioselective, drug discovery, asymmetric synthesis

---

### 41. ❌ Maintenance breeding and breeding for yield potential both contribute to genetic improvement in wheat yield

**作者**: José F. Andrade, Jianguo Man, Juan Pablo Monzón, Juan I. Rattalino Edreira, Shen Yuan, Romulo P. Lollato, Abelardo J. de la Vega, Clara Llorens, Amanda de Oliveira Silva, Shaobing Peng, Kenneth G. Cassman, Patricio Grassini
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-69936-6](https://doi.org/10.1038/s41467-026-69936-6)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确表明这是一篇关于小麦遗传育种和产量提升的农业科学研究论文，与医学图像分析、医学成像或深度学习医学成像完全无关。论文讨论的是小麦育种策略、遗传改良、产量潜力等农业主题，没有任何医学或图像分析相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究评估了维持育种和产量潜力育种两种策略对小麦产量遗传改良的贡献，发现两者都显著提高了小麦产量，但产量潜力育种对长期遗传增益的贡献更大。

**关键词**: wheat breeding, genetic improvement, yield potential, maintenance breeding, crop yield, genetic gain, agricultural research

---

### 42. ❌ Metamaterials and Fluid Flows

**作者**: Francesco Avallone, Federico Bosia, Yi Chen, Giada Colombo, Richard V. Craster, Jacopo Maria De Ponti, Nicolò Fabbiane, Michael R. Haberman, Mahmoud I. Hussein, Wontae Hwang, Umberto Iemma, Abigail T. Juhl, Muamer Kadic, Marios Kotsonis, Guodong Fang, Olivier Marquet, Fabien Mery, Theodoros Michelis, Mostafa Nouh, Daniele Ragni
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**arXiv链接**: [https://arxiv.org/abs/2509.05371](https://arxiv.org/abs/2509.05371)
**DOI**: [10.1038/s41467-026-70163-2](https://doi.org/10.1038/s41467-026-70163-2)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题为'Metamaterials and Fluid Flows'，摘要全面讨论流体-结构相互作用、超材料在流动控制、声学响应和能量收集等领域的应用。虽然提到'biomedical devices'作为新兴技术之一，但全文未涉及医学图像分析、医学成像或深度学习医学成像的具体内容、方法或应用。论文核心是流体力学、超材料和结构动力学的交叉研究，与医学图像处理领域无直接关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    This review paper explores how metamaterials can be engineered to control fluid-structure interactions for applications in flow control, noise mitigation, and energy harvesting, surveying contemporary frameworks and future directions in this interdisciplinary field.

<details open>
<summary>摘要翻译</summary>

> 理解并控制流体流动与固体材料及结构之间的动态相互作用——这一领域被称为流固耦合——不仅是航空航天与船舶工程等传统学科的核心，也对能量收集、软体机器人和生物医学设备等新兴技术至关重要。近年来，超材料（metamaterials）的出现为重新思考和设计流固耦合提供了令人振奋的机遇。通过设计界面流体流动的材料内部结构，这一理念为精确有效地操控耦合的流体、声学和弹性动力学响应开辟了新视野。本综述聚焦于这一具有广泛技术意义但相对未被深入探索的交叉学科主题。诸多重要的潜在应用，如运输系统的燃料消耗、可再生能源提取效率、噪声抑制以及结构疲劳的耐受性，都依赖于对流动、声学和振动机制之间相互作用的控制。例如，涵盖层流、转捩流、湍流和非定常分离流等多种流态的流动控制，就深受流固耦合的影响。本综述梳理并讨论了描述流体与弹性固体间相互作用的概念框架，重点关注当代及新兴理念。本文分为三个主要部分：流固与流体-声子相互作用、流动及声学与超材料的相互作用，以及对流固耦合具有潜在影响的奇异超材料概念。最后，本文对这一快速扩展的研究领域当前面临的挑战和未来发展方向进行了展望。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Understanding and controlling the dynamic interactions between fluid flows and solid materials and structures-a field known as fluid-structure interaction-is central not only to established disciplines such as aerospace and naval engineering, but also to emerging technologies such as energy harvesting, soft robotics, and biomedical devices. In recent years, the advent of metamaterials has provided exciting opportunities to rethink and redesign fluid-structure interactions. The idea of engineering the internal structure of materials that interface with fluid flows opens a new horizon for the precise and effective manipulation and control of coupled fluidic, acoustic, and elastodynamic responses. This review focuses on this relatively unexplored interdisciplinary theme with broad technological significance. Salient potential applications, such as fuel consumption in transport systems, efficiency of renewable energy extraction, noise mitigation, and resilience against structural fatigue, depend on controlling interactions among flow, acoustic, and vibration mechanisms. Flow control, for example, which spans a wealth of regimes such as laminar, transitional, turbulent, and unsteady separated flows, is strongly influenced by fluid-structure interaction. This review surveys and discusses conceptual frameworks that describe the interplay between fluids and elastic solids, with a focus on contemporary and emerging concepts. The paper is organised into three main sections: flow-structure and fluid-phonon interactions, flow and acoustic interactions with metamaterials, and exotic metamaterial concepts with potential impact on fluid-structure interaction. It concludes with perspectives on current challenges and future directions in this rapidly expanding area of research.

</details>
<br>

**关键词**: metamaterials, fluid-structure interaction, flow control, acoustic response, energy harvesting, fluid flows, elastodynamic responses, interdisciplinary research

---

### 43. ❌ Additive manufacturing of cellulose-based photopolymerizable resin with high strength and shape-memory

**作者**: Xin Zhao, Jian Li, Su Xiao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-70253-1](https://doi.org/10.1038/s41467-026-70253-1)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是基于纤维素的增材制造光聚合树脂材料，专注于材料科学、制造技术和机械性能，与医学图像分析、医学成像或深度学习医学成像完全无关。论文摘要和标题中未提及任何医学图像相关概念。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文开发了一种基于纤维素的增材制造光聚合树脂材料，解决了现有材料稳定性差、形状恢复有限和机械性能不足的问题，实现了优异的刚度-变形协同效应和时空形状记忆能力。

<details open>
<summary>摘要翻译</summary>

> 作为核心先进制造技术之一，增材制造在航空航天、生物医学及工业部件制造领域具有极高的应用价值。然而，当前增材制造材料（如石油基树脂）面临稳定性差、形状恢复能力有限及力学性能不足等局限，制约了可持续制造的发展。受植物细胞壁应力耗散机制的启发，我们开发了一种纤维素基光聚合树脂，该材料具备优异的刚度-可变形协同效应及时空形状记忆能力。这些结构融合了卓越的机械强度与变形后的快速恢复性能。该增材制造纤维素基光聚合树脂材料展现出协同的刚度-可变形特性，其压缩强度达115.42 MPa，刚度达1404.16 MPa。这些特性为专用国防部件、能量吸收系统及时空记忆材料奠定了基础。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> As one of the core advanced manufacturing technologies, additive manufacturing is of high application value in the aerospace, biomedical, and industrial component manufacturing fields. Nevertheless, current additive manufacturing materials (e.g., petroleum-based resins) face limitations such as poor stability, limited shape recovery, and insufficient mechanical properties, which restrict sustainable manufacturing progress. Inspired by the stress-dissipation mechanism in plant cell walls, we develop a cellulose-based photopolymerizable resin that delivers exceptional stiffness-deformability synergy and spatiotemporally shape memory capability. These structures integrate excellent mechanical strength and rapid recovery performance after deformation. The additive manufacturing cellulose-based photopolymerizable resin material exhibits a synergistic stiffness-deformability profile, achieving a compressive strength of 115.42 MPa and stiffness of 1404.16 MPa. These characteristics lay the foundation for specialized defense components, energy absorption systems, and spatiotemporal memory materials.

</details>
<br>

**关键词**: additive manufacturing, cellulose-based photopolymerizable resin, mechanical strength, shape-memory, stiffness-deformability synergy, compressive strength, advanced manufacturing, sustainable materials

---

### 44. ❌ A hormetic transcriptional program coregulates invasion, proliferation and dormancy to define metastatic potential

**作者**: Raúl Jiménez-Castaño, Nitin Narwade, Moreno‐Bueno Gema, Berta López Sánchez-Laorden, Joan Galcerán, Khalil Kass Youssef, M. Angela Nieto
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-70242-4](https://doi.org/10.1038/s41467-026-70242-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是乳腺癌转移的分子机制，聚焦于转录因子Prrx1如何调控侵袭、增殖和休眠程序，从而决定转移潜能。研究使用了多组学分析（空间转录组学、单细胞基因表达、染色质图谱）和临床队列数据，但完全不涉及医学影像分析、医学成像或深度学习医学成像技术。论文内容属于癌症生物学和分子肿瘤学领域，与给定的医学影像关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that cells exit the primary tumor with pre-set metastatic potential, indicating that metastatic competence emerges from the integration of Prrx1 co-regulated molecular programs, explaining why some invasive cells enter dormancy while others resume growth.

!!! tip deepseek-chat TL;DR

    该研究发现转录因子Prrx1通过非线性的剂量效应共同调控侵袭、增殖和休眠程序，从而决定了乳腺癌细胞的转移潜能，并解释了为何一些侵袭细胞进入休眠而另一些恢复生长。

<details open>
<summary>摘要翻译</summary>

> 转移仍是癌症死亡的主要原因，但决定转移能力及其获得时间的因素尚不明确。通过人类乳腺癌队列研究和临床前模型的多组学分析，本研究揭示细胞离开原发肿瘤时已具备预设的转移潜能。整合空间转录组学与单细胞基因表达及染色质图谱分析，我们鉴定出转录因子Prrx1作为扩散的主调控因子：除了已知的侵袭功能外，它通过作用于细胞周期蛋白和细胞周期抑制剂（Ccnd1/2、Cdkn2a/b/c）抑制增殖，并激活休眠程序（Gas6、Mme、Ogn）。中等水平的Prrx1表达可优化侵袭与增殖/休眠之间的平衡，在Prrx1表达与转移负荷之间形成毒物兴奋效应（非线性）关系。联合侵袭与增殖特征谱能显著分层乳腺癌预后，凸显了这种表型相互作用的临床相关性。这些发现表明，转移能力源于Prrx1协同调控的分子程序的整合，这解释了为何某些侵袭细胞进入休眠状态，而其他细胞则恢复生长。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Metastasis remains the leading cause of cancer mortality, yet the factors that determine metastatic competence and the timing of its acquisition are not well understood. Using human breast cancer cohorts and multi-omics in preclinical models, here we show that cells exit the primary tumor with pre-set metastatic potential. Integrating spatial transcriptomics with single-cell gene expression and chromatin profiles, we identify the transcription factor Prrx1 as a master regulator of dissemination: beyond its known role in invasion, it represses proliferation by acting on cyclins and cell-cycle inhibitors (Ccnd1/2, Cdkn2a/b/c) and activates a dormancy program (Gas6, Mme, Ogn). Intermediate Prrx1 levels optimize the trade-off between invasion and proliferation/dormancy, producing a hormetic (nonlinear) relationship between Prrx1 expression and metastatic burden. Combined invasion and proliferation signatures strongly stratify breast cancer prognosis, underscoring the clinical relevance of this phenotypic interplay. These findings indicate that metastatic competence emerges from the integration of Prrx1 co-regulated molecular programs, explaining why some invasive cells enter dormancy while others resume growth.

</details>
<br>

**关键词**: metastasis, breast cancer, Prrx1, invasion, proliferation, dormancy, hormetic relationship, spatial transcriptomics

---

### 45. ❌ Clonal evolutionary analysis reveals patterns of malignant transformation of Intraductal Papillary Mucinous Neoplasms of the pancreas

**作者**: Antonio Pea, Xiaotong He, Rosie Upstill-Goddard, Claudio Luchini, Leonor Patricia Schubert Santana, Lea Abdulkhalek, Fraser Duthie, Nigel B. Jamieson, Colin J. McKay, Euan J. Dickson, Alessandra Pulvirenti, Selma Rebus, Paola Piccoli, Nicola Sperandio, Rita T. Lawlor, Michele Milella, Fieke E. M. Froeling, Roberto Salvia, Aldo Scarpa, Andrew V. Biankin
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-69762-w](https://doi.org/10.1038/s41467-026-69762-w)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究胰腺导管内乳头状黏液性肿瘤（IPMN）的克隆进化、基因组和转录组分析，使用全基因组测序、转录组测序和系统发育树构建方法，属于癌症基因组学和分子病理学领域。论文未涉及医学图像分析、医学成像或深度学习医学成像的任何内容，标题、摘要和方法中均未提及图像数据、成像技术或深度学习模型。因此，所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Transcriptomic analysis reveals unique gene expression profiles and variations in the immune landscape that correlate with different progression stages of IPMN, revealing the complex molecular dynamics of IPMN heterogeneity and progression, highlighting the need to refine early detection and treatment strategies.

!!! tip deepseek-chat TL;DR

    该研究通过多区域全基因组和转录组测序分析胰腺导管内乳头状黏液性肿瘤的克隆进化，揭示了两种不同的进化轨迹以及突变特征、结构变异和免疫景观在肿瘤进展中的作用。

<details open>
<summary>摘要翻译</summary>

> 导管内乳头状黏液性肿瘤（IPMN）是胰腺导管腺癌的关键前驱病变，后者是一种以晚期检出和快速进展为特征的高致死性癌症。本研究整合多区域全基因组与转录组测序数据，追溯IPMN的演化过程，构建了详细的系统发育树以揭示其亚克隆结构与进展路径。分析识别出两种不同的演化轨迹：一种由单一祖细胞克隆驱动，另一种则涉及多个独立的祖细胞克隆。我们进一步探讨了突变特征与结构变异在促进克隆演化及新亚克隆出现中的作用。作为基因组发现的补充，转录组分析揭示了与IPMN不同进展阶段相关的独特基因表达谱及免疫微环境变化。这些发现揭示了IPMN异质性与进展的复杂分子动态，强调了优化早期检测与治疗策略的必要性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Intraductal papillary mucinous neoplasms (IPMNs) are critical precursors to pancreatic ductal adenocarcinoma, a highly lethal cancer characterized by late detection and rapid progression. Here we integrate multi-region whole-genome and transcriptome sequencing to trace the evolution of IPMN, constructing detailed phylogenetic trees to provide insights into subclonal architectures and progression pathways. Our analysis identifies two distinct evolutionary trajectories: one driven by a single ancestral clone, and another involving multiple independent ancestral clones. We further explore the roles of mutational signatures and structural variants in promoting clonal evolution and the emergence of new subclones. Complementing these genomic findings, our transcriptomic analysis reveals unique gene expression profiles and variations in the immune landscape that correlate with different progression stages of IPMN. These insights reveal the complex molecular dynamics of IPMN heterogeneity and progression, highlighting the need to refine early detection and treatment strategies.

</details>
<br>

**关键词**: Intraductal papillary mucinous neoplasms, pancreatic ductal adenocarcinoma, clonal evolution, whole-genome sequencing, transcriptome sequencing, phylogenetic trees, mutational signatures, immune landscape

---

### 46. ❌ Retraction Note: Multifunctional nanoagents for ultrasensitive imaging and photoactive killing of Gram-negative and Gram-positive bacteria

**作者**: Jiali Tang, Binbin Chu, Jinhua Wang, Bin Song, Yuanyuan Su, Houyu Wang, Yao He
**期刊/来源**: nature_communications
**发布日期**: 2026-03-04
**DOI**: [10.1038/s41467-026-68401-8](https://doi.org/10.1038/s41467-026-68401-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究是关于多功能纳米试剂用于细菌成像和光活性杀伤的，属于纳米材料、生物医学工程和细菌治疗领域。虽然涉及成像（imaging），但这是指纳米材料在生物体内的荧光或光学成像，用于追踪纳米颗粒分布，而非医学影像分析（如CT、MRI、X光等图像的计算机分析）。论文未涉及医学图像处理、分析算法或深度学习在医学影像中的应用，与所有评分关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文因数据问题（图像重叠）被撤稿，原研究旨在开发多功能纳米试剂用于革兰氏阴性和阳性细菌的超灵敏成像和光活性杀伤。

<details open>
<summary>摘要翻译</summary>

> 编辑已撤回本文。文章发表后，图7中呈现的数据受到质疑，具体包括：图7b HeLa细胞中，Ce6组3与SiNPs组3的图像似乎重叠；图7b HeLa细胞中，GP-Ce6-SiNPs对照组、组1与组2的图像似乎重叠；图7c中，心脏组织GP-Ce6-SiNPs (-)与PBS (-)的图像似乎重叠；图7c中，肺组织PBS (-)、PBS (+)与GP-Ce6-SiNPs (+)的图像似乎重叠。作者已发布更正声明1以回应部分质疑。然而，出版方进一步核查后发现其他问题：图7b ARPE细胞中，Ce6组2与组5的图像似乎重叠；图7c中，肾脏组织PBS (+)与GP-Ce6-SiNPs (+)的图像似乎重叠。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The Editors have retracted this article.After publication, concerns were raised regarding the data presented in Fig. 7, specifically: In Fig. 7b HeLa, Ce6 group 3 and SiNPs group 3 images appear to overlap; In Fig. 7b HeLa, GP-Ce6-SiNPs control, group 1 and group 2 images appear to overlap; In Fig. 7c, Heart GP-Ce6-SiNPs (-) and PBS (-) images apear to overlap; In Fig. 7c, Lung PBS -, PBS + and GP-Ce6-SiNPs + images appear to overlap.The authors have issued a Correction 1 to address some of these concerns.However, further checks by the Publisher identified additional concerns: In Fig. 7b ARPE, Ce6 group 2 and 5 images appear to overlap; In Fig. 7c, Kidney PBS + and GP-Ce6-SiNPs + images appear to overlap.

</details>
<br>

**关键词**: retraction, nanoagents, ultrasensitive imaging, photoactive killing, Gram-negative bacteria, Gram-positive bacteria, data overlap concerns, correction

---

### 47. ❌ Machine learning discovers numerous new computational principles supporting elementary motion detection

**作者**: Alon Poleg-Polsky
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70288-4](https://doi.org/10.1038/s41467-026-70288-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是视觉运动方向检测的神经计算原理，使用机器学习方法分析视网膜和皮层回路，属于计算神经科学和生物信息学领域。虽然涉及机器学习，但研究对象是生物神经回路而非医学影像，与医学图像分析、医学成像或深度学习医学成像完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Biological inspired machine learning applied to retinal and cortical circuits is used to uncover receptive field architectures capable of direction selectivity, offering fresh insights into motion processing and illustrating how machine learning can uncover general principles of neural computation.

!!! tip deepseek-chat TL;DR

    该研究使用机器学习方法分析视网膜和皮层回路，发现了八种支持运动方向检测的计算原理，其中四种是新的，这些机制在鲁棒性和精度上优于经典模型。

<details open>
<summary>摘要翻译</summary>

> 运动方向检测是一种基础的视觉计算，它将空间亮度模式转化为方向调谐的输出。经典的方向选择性模型依赖于时间不对称性，即通过延迟兴奋或抑制来实现运动检测。本文采用受生物学启发的机器学习方法，应用于视网膜和皮层回路，以揭示能够实现方向选择性的感受野结构。这些机制包括基于不对称突触特性、空间感受野变化、突触前与突触后抑制的新作用，以及先前未被认识的动力学实现方式。从概念上讲，这些回路结构可归纳为八种构成运动检测基础的计算基元，其中四种是此前未被描述的。许多解决方案在鲁棒性和精确度上可与经典模型媲美或更优，并且其中几种表现出更强的噪声容忍度。所有机制都具有生物学合理性，并与已知的生理学和解剖学模式相对应，从而为运动处理提供了新的见解，并展示了机器学习如何能够揭示神经计算的普遍原理。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Motion direction detection is a fundamental visual computation that transforms spatial luminance patterns into directionally tuned outputs. Classical models of direction selectivity rely on temporal asymmetry, where motion detection arises through either delayed excitation or inhibition. Here, I used biologically inspired machine learning applied to retinal and cortical circuits to uncover receptive field architectures capable of direction selectivity. These include mechanisms based on asymmetric synaptic properties, spatial receptive field variations, new roles for pre- and postsynaptic inhibition, and previously unrecognized kinetic implementations. Conceptually, these circuit architectures cluster into eight computational primitives underlying motion detection, four of which are previously undescribed. Many of the solutions rival or outperform classical models in both robustness and precision, and several exhibit enhanced noise tolerance. All mechanisms are biologically plausible and correspond to known physiological and anatomical motifs, offering fresh insights into motion processing and illustrating how machine learning can uncover general principles of neural computation.

</details>
<br>

**关键词**: motion direction detection, machine learning, retinal circuits, cortical circuits, direction selectivity, computational primitives, neural computation, biologically plausible mechanisms

---

### 48. ❌ Mitotic microhomology-mediated break-induced replication promotes chromoanasynthesis

**作者**: Greg H. P. Ngo, Kez Cleal, Sara Seifan, Vanda Miklós, Szymon A. Barwacz, Brian L. Ruis, Siamak A. Kamranvar, Julia W. Grimstead, Ying Liu, Eric A. Hendrickson, Duncan M. Baird
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70086-y](https://doi.org/10.1038/s41467-026-70086-y)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是染色体异常（chromoanasynthesis）的分子机制，涉及DNA修复、有丝分裂和癌症遗传学，属于分子生物学和遗传学领域。标题、摘要和内容均未提及医学影像分析、医学成像或深度学习医学成像。论文使用单分子长读DNA测序技术，而非医学影像技术。因此，所有关键词与论文主题完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A single-molecule long-read DNA sequencing approach is developed to characterise ultra-complex mutational events, consistent with chromoanasynthesis, occurring at shortened telomeres and sub-telomeric DNA double-strand breaks in human cells, and establishes mitotic MM-BIR as a key driver of CCRs.

!!! tip deepseek-chat TL;DR

    该研究揭示了染色体异常（chromoanasynthesis）是由有丝分裂中的微同源介导的断裂诱导复制（MM-BIR）机制驱动的，这一发现解释了癌症和先天性疾病中复杂染色体重排的起源。

<details open>
<summary>摘要翻译</summary>

> 染色体合成是一种常见于癌症和先天性疾病的复杂染色体重排形式，但其产生机制尚不明确。本研究开发了一种单分子长读长DNA测序方法，用于表征人类细胞中端粒缩短和亚端粒DNA双链断裂处发生的、与染色体合成相符的超复杂突变事件。我们的数据显示，染色体合成是由微同源介导的断裂诱导复制机制在细胞有丝分裂期特异性触发生成的。出乎意料的是，这一有丝分裂途径涉及微同源末端连接与断裂诱导复制的协同作用：微同源末端连接蛋白启动了一个依赖于Polδ的断裂诱导复制通路，该通路受PIF1、POLD3和PCNA蛋白调控。该通路极易发生模板转换，能在单次事件中引发基因组位点的剧烈扩增。这些发现有助于解释染色体合成的高度诱变特性，并确立了有丝分裂微同源介导的断裂诱导复制作为复杂染色体重排的关键驱动机制，对癌症和先天性疾病的起源研究具有重要意义。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Chromoanasynthesis is a form of complex chromosomal rearrangement (CCR) commonly detected in cancers and congenital disorders, but the mechanism underlying its generation remain elusive. Here we develop a single-molecule long-read DNA sequencing approach to characterise ultra-complex mutational events, consistent with chromoanasynthesis, occurring at shortened telomeres and sub-telomeric DNA double-strand breaks in human cells. Our data reveal that chromoanasynthesis is generated by microhomology-mediated break-induced replication (MM-BIR), occurring specifically in mitosis. Surprisingly, this mitotic pathway involves a collaboration between microhomology-mediated end-joining (MMEJ) and BIR, where MMEJ proteins initiate a Polδ-dependent BIR pathway that is regulated by PIF1, POLD3 and PCNA. This pathway is highly prone to template switching and can generate dramatic amplification of genomic loci in a single event. Our findings help explain the extreme mutagenic nature of chromoanasynthesis and establish mitotic MM-BIR as a key driver of CCRs, with important implications for the origin of cancers and congenital disorders.

</details>
<br>

**关键词**: chromoanasynthesis, complex chromosomal rearrangement, mitotic MM-BIR, microhomology-mediated break-induced replication, DNA double-strand breaks, cancer, congenital disorders, single-molecule sequencing

---

### 49. ❌ Alpha frequency shapes perceptual sensitivity by modulating optimal phase likelihood

**作者**: Vincenzo Romei, Luca Tarasi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70124-9](https://doi.org/10.1038/s41467-026-70124-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是脑电图（EEG）中alpha频率振荡与感知敏感性的关系，属于认知神经科学领域。虽然涉及神经信号分析，但完全不涉及医学影像分析（medical image analysis）、医学成像（medical imaging）或深度学习医学成像（deep learning medical imaging）。论文未使用任何医学影像数据或技术，也未提及深度学习在医学影像中的应用。因此，所有关键词的相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Insight is provided into the neural candidate mechanisms through which alpha frequency relates to perceptual decisions, which may provide more opportunities for the stimulus to coincide with optimal phases for perception, thereby increasing the likelihood of accurate sensory processing.

!!! tip deepseek-chat TL;DR

    该研究通过EEG实验发现，刺激前的瞬时alpha频率是感知决策敏感性和准确性的预测因子，更高的alpha频率通过增加刺激与感知最优相位重合的机会来提高感觉处理精度。

<details open>
<summary>摘要翻译</summary>

> α频段振荡是否主导感觉采样的节律，是目前存在争议的议题。本研究利用脑电图技术，通过考察刺激前瞬时α频率是否影响知觉敏感性来检验这一假说。我们的结果支持α频率在塑造感觉获取准确性中的作用。试次间自发α频率的波动显现为知觉决策敏感性与准确性的预测指标——更快的节律对应更高的感觉精度，这一观察结果得到了包括贝叶斯统计与计算建模在内的多种互补分析方法的支持。本文进一步揭示了α频率与知觉决策相关联的潜在神经机制。具体而言，α频率可能决定刺激时间窗口内所覆盖的相位角度范围。因此，更高的α频率可能为刺激与知觉最优相位相吻合提供更多机会，从而增加感觉信息被准确处理的可能性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Whether alpha frequency oscillations orchestrate the pace of sensory sampling is current matter of debate. Using EEG, we test this hypothesis by investigating whether pre-stimulus instantaneous alpha frequency accounts for perceptual sensitivity. Our results support the role of alpha frequency in shaping the accuracy of sensory acquisition. Spontaneous alpha frequency inter-trial fluctuations emerged as a predictor of perceptual decision-making sensitivity and accuracy, with higher pace accounting for higher sensory precision - an observation supported across complementary analytical approaches, including Bayesian statistics and computational modelling. Here, we provide insights into the neural candidate mechanisms through which alpha frequency relates to perceptual decisions. Specifically, alpha frequency would determine the extent of phase angles covered within the stimulus timeframe. As a result, higher alpha frequencies may provide more opportunities for the stimulus to coincide with optimal phases for perception, thereby increasing the likelihood of accurate sensory processing.

</details>
<br>

**关键词**: alpha frequency, perceptual sensitivity, EEG, sensory sampling, phase likelihood, computational modelling, Bayesian statistics

---

### 50. ❌ Engineering molecular rotor-stator ligand architectures on copper nanoclusters for efficient photothermal conversion

**作者**: Yanru Yin, D. Sulalith N. D. Samarasinghe, Jing Sun, Hongwen Deng, Lei Li, Ming‐Qiang Qi, Fangming Zhao, Qinghua Xu, Huifang Guo, Xueli Sun, Xuekun Gong, Rong Huo, Mengsi Zhu, Qingyuan Wu, zhenlang Xie, Chengrui Xin, Yaqi Wang, Xiaotong Jiang, Simin Li, Fengyu Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70141-8](https://doi.org/10.1038/s41467-026-70141-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是铜纳米团簇的光热转换性能优化，通过分子转子-定子配体结构设计提高光热转换效率至75%。全文聚焦于材料科学、纳米技术、光热转换机制，未涉及医学图像分析、医学成像或深度学习在医学成像中的应用。论文内容与所有评分关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过设计铜纳米团簇表面的分子转子-定子配体结构，将光热转换效率提升至75%，实现了在激光照射下快速升温至200°C。

<details open>
<summary>摘要翻译</summary>

> 铜纳米团簇是材料科学中一个前景广阔但尚未充分开发的领域。本文提出了一种通用且高效的策略，通过在铜纳米团簇表面引入转子-定子配体结构来提升光热转换效率。作为一个代表性示例，我们设计了金刚烷功能化的羧酸配体，用于稳定一个[Cu<sub>36</sub>(4-F-PhS)<sub>24</sub>(AdmCOO)<sub>6</sub>(PPh<sub>3</sub>)<sub>4</sub>H<sub>8</sub>]<sup>2-</sup>纳米团簇。在该结构中，金刚烷单元充当分子转子，而羧酸根基团则作为分子定子。所设计的纳米团簇实现了75%的光热转换效率。金刚烷转子在团簇框架内表现出降低的旋转能垒，能够实现稳定且快速的分子旋转，从而有效促进非辐射跃迁。这一机制优化了光能到热能的转换，使得该纳米团簇在功率密度为1.0 W cm<sup>-2</sup>的445 nm激光照射下能迅速升温至200 °C。所提出的策略可适用于其他转子类型，从而构建出一个具有增强光热转换能力及多功能潜力的、广泛的铜纳米团簇家族。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Copper nanoclusters represent a promising yet underdeveloped frontier in materials science. Here, we propose a general and efficient strategy for enhancing photothermal conversion efficiency through the incorporation of rotor-stator ligand architectures onto copper nanocluster surfaces. As a representative example, we design carboxylate ligands functionalized with adamantane groups to stabilize a [Cu<sub>36</sub>(4-F-PhS)<sub>24</sub>(AdmCOO)<sub>6</sub>(PPh<sub>3</sub>)<sub>4</sub>H<sub>8</sub>]<sup>2-</sup> nanocluster. In this architecture, the adamantane unit functions as a molecular rotor, while the carboxylate group serves as a molecular stator. The engineered nanocluster achieves a photothermal conversion efficiency of 75%. The adamantane rotors exhibit a lowered rotational energy barrier within the cluster framework, enabling stable and rapid molecular rotation that effectively promotes non-radiative transitions. This mechanism optimizes the conversion of light into thermal energy, enabling the nanocluster to rapidly heat up to 200 °C under 445 nm laser irradiation at a power density of 1.0 W cm<sup>-2</sup>. The proposed strategy could be applicable to other rotor types, yielding a broad family of copper nanoclusters with enhanced photothermal conversion capabilities and multifunctional potential.

</details>
<br>

**关键词**: copper nanoclusters, photothermal conversion, rotor-stator ligand, molecular rotor, adamantane, non-radiative transitions, light-to-heat conversion, nanomaterial engineering

---

### 51. ❌ sRNA centered signaling activates nitrate respiration and enhances Cronobacter sakazakii virulence in host environments

**作者**: Xiaoya Li, Hao Sun, Xinyuan Yang, Liying Feng, Yuanyuan Niu, Binbin Xiang, Jingliang Qin, Yì Wáng, LI Zhen-gang, Lu Wang, Feng Lu, Lei Wang, Bin Liu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70257-x](https://doi.org/10.1038/s41467-026-70257-x)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是细菌病原体Cronobacter sakazakii的致病机制，具体涉及sRNA信号通路、硝酸盐呼吸和毒力增强，属于微生物学、分子生物学和感染性疾病领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像技术，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A signal transduction pathway centered on a novel sRNA, CsrN, is revealed, which facilitates C. sakazakii in utilizing nitrate respiration in response to oxygen-limited environments within the host, thereby enhancing its virulence in vivo.

!!! tip deepseek-chat TL;DR

    该研究发现Cronobacter sakazakii通过sRNA CsrN信号通路激活硝酸盐呼吸，增强其在宿主缺氧环境中的生存和毒力，并证明硝酸盐呼吸可作为潜在治疗靶点。

<details open>
<summary>摘要翻译</summary>

> 阪崎克罗诺杆菌是一种重要的新生儿致病菌，常与婴幼儿配方奶粉相关联。然而，该细菌如何适应宿主环境并实现系统性播散的机制尚不明确。本研究揭示了一条以新型小RNA（CsrN）为核心的信号转导通路，该通路使阪崎克罗诺杆菌能够在宿主内部缺氧环境下利用硝酸盐呼吸，从而增强其在体内的致病力。阪崎克罗诺杆菌感染会引发炎症反应，导致宿主源性硝酸盐（一种关键的替代电子受体）积累。CsrN的表达在厌氧条件下通过ArcAB双组分调控系统被诱导。随后，CsrN可增强编码硝酸盐还原酶复合物的narGHJI操纵子的表达。这一机制促进了阪崎克罗诺杆菌在胃肠道中的定植，并有利于其在巨噬细胞内的存活，最终导致细菌在宿主体内的系统性播散能力和毒力增强。动物实验表明，施用硝酸盐呼吸的特异性抑制剂钨酸盐能显著减弱阪崎克罗诺杆菌的毒力。本研究为理解阪崎克罗诺杆菌在宿主环境中的生存和致病机制提供了新见解，并提示硝酸盐呼吸可作为对抗阪崎克罗诺杆菌感染的潜在治疗靶点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Cronobacter sakazakii is an important neonatal pathogen frequently associated with powdered infant formula. However, the mechanisms by which C. sakazakii adapts to the host environment and establishes systemic dissemination remain poorly understood. Here, we reveal a signal transduction pathway centered on a novel sRNA, CsrN, which facilitates C. sakazakii in utilizing nitrate respiration in response to oxygen-limited environments within the host, thereby enhancing its virulence in vivo. C. sakazakii infection triggers an inflammatory response, leading to the accumulation of host-derived nitrate, a key alternative electron acceptor. The expression of CsrN is induced under anaerobic conditions via the ArcAB two-component regulation system. CsrN subsequently enhances the expression of the narGHJI operon, which encodes a nitrate reductase complex. This promotes the colonization of C. sakazakii in the gastrointestinal tract and benefits its survival within macrophages, ultimately leading to increased systemic bacterial dissemination and virulence in the host. We show that administration of tungstate, a specific inhibitor of nitrate respiration, significantly attenuates C. sakazakii virulence in animal experiments. This work provides novel insights into the survival and pathogenicity mechanisms employed by C. sakazakii in host environments and suggests nitrate respiration as a potential therapeutic target for combating C. sakazakii infections.

</details>
<br>

**关键词**: Cronobacter sakazakii, sRNA CsrN, nitrate respiration, virulence, ArcAB two-component system, narGHJI operon, tungstate inhibitor, host adaptation

---

### 52. ❌ Pharmacological stabilization of hypoxia-inducible factor 1-α dampens the interferon response and promotes glycolysis in Aicardi-Goutières syndrome

**作者**: Maxime Batignes, Marine Luka, Surabhi Jagtap, Camille de Cevins, Ivan Nemazanyy, Jacqueline Leib, Tinhinane Fali, Alexandre Pierga, M Zarhrate, Víctor Paredes, F. Carbone, Brieuc P. Pérot, B. Neven, Brigitte Bader-Meunier, Pierre Marie Quartier, Aline Cano, Alexandre Belot, Alice Lepelley, Marie-Louise Frémond, Alain Fischer
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69979-9](https://doi.org/10.1038/s41467-026-69979-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究Aicardi-Goutières综合征（AGS）的分子机制和潜在治疗方法，使用单细胞转录组学、靶向代谢组学、机器学习方法和体外细胞模型，核心内容涉及基因突变、干扰素反应、代谢转换（糖酵解与氧化磷酸化）、HIF-1α稳定化治疗等。所有评分关键词均与医学影像分析相关，但论文未涉及任何医学影像数据、技术或应用，因此完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is proposed that an energy metabolic switch contributes to chronic inflammation in AGS and that targeting this pathway might represent a potential therapeutic approach.

!!! tip deepseek-chat TL;DR

    该研究发现Aicardi-Goutières综合征中HIF-1α表达缺失导致代谢转换偏向氧化磷酸化，而化学稳定HIF-1α可逆转代谢转换、减轻线粒体应激并显著降低干扰素反应，提示靶向该通路可能成为潜在治疗方法。

<details open>
<summary>摘要翻译</summary>

> Aicardi-Goutières综合征（AGS）是一种由I型干扰素（IFN）介导的遗传性疾病，其特征为神经系统受累，发病于子宫内或儿童期。本研究利用单细胞转录组学和靶向代谢组学技术，分析了携带ADAR1、RNASEH2B或SAMHD1基因致病突变的AGS患者外周血样本。通过机器学习方法和差异基因表达分析，我们发现单核细胞和树突状细胞中转录因子缺氧诱导因子1α（HIF-1α）的表达和活性丧失，并伴随代谢特征转向：倾向于氧化磷酸化和谷胱甘肽代谢，而非糖酵解。同时，研究还观察到线粒体应激以及胞质内双链DNA和RNA的积累。在AGS患者原代外周血单个核细胞的代谢水平上，这一能量代谢转换得到了证实。在AGS体外细胞模型中，使用合成药物化学稳定HIF-1α，可将能量代谢逆转回糖酵解方向，减轻线粒体应激，并显著降低干扰素反应及IP-10的产生。因此，我们认为能量代谢转换是AGS慢性炎症的驱动因素之一，靶向该通路可能成为一种潜在的治疗策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Aicardi-Goutières syndrome (AGS) is a genetic type I interferon (IFN)-mediated disease characterized by neurological involvement with onset in utero or in childhood. Here, we analyze peripheral blood samples from patients bearing AGS-causing mutations in ADAR1, RNASEH2B or SAMHD1 using single-cell transcriptomics and targeted metabolomics. Using machine-learning approaches and differential gene expression analysis, we identified a loss of transcription factor hypoxia induced factor 1 α (HIF-1α) expression and activity associated with features of a metabolic switch favoring oxidative phosphorylation and glutathione metabolism over glycolysis in monocytes and dendritic cells. Evidences of mitochondrial stress and accumulation of cytosolic double-stranded DNA and RNA were also found. The energy metabolic switch was confirmed at the metabolic level in primary peripheral blood mononuclear cells of AGS patients. Chemical stabilization of HIF-1α using a synthetic drug in in vitro cellular models of AGS, reversed the energy metabolic switch towards glycolysis, attenuated mitochondrial stress, and markedly reduced the IFN response and IP-10 production. We therefore propose that an energy metabolic switch contributes to chronic inflammation in AGS and that targeting this pathway might represent a potential therapeutic approach.

</details>
<br>

**关键词**: Aicardi-Goutières syndrome, HIF-1α, metabolic switch, interferon response, glycolysis, oxidative phosphorylation, single-cell transcriptomics, therapeutic approach

---

### 53. ❌ Intrinsic gradient oxygen-driven second-order memristors for continual reinforcement learning

**作者**: Jianyu Ming, Ruiheng Wang, Jingwei Fu, Jing Liu, Siqi Wu, Shanshuo Liu, He Shao, Yanfei Li, Yì Wáng, Yue Wang, Xi Zhang, Linghai Xie, Haifeng Ling, Wei Huang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70014-0](https://doi.org/10.1038/s41467-026-70014-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是基于氧梯度驱动的二阶忆阻器在持续强化学习中的应用，属于神经形态计算和硬件实现领域。虽然论文提到了"learning"和"algorithm"，但这是针对强化学习算法在硬件上的实现，与医学图像分析、医学成像或深度学习医学成像完全无关。论文内容聚焦于忆阻器器件物理特性、氧离子迁移、强化学习算法硬件映射等，没有任何涉及医学图像或医学领域的内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了现有忆阻器缺乏内在梯度导致状态突变的问题，通过设计具有稳定氧梯度的二阶忆阻器，实现了与强化学习算法学习率协同演化的时间自适应电导状态，将训练迭代次数在静态和动态环境中分别减少了68.75%和35.65%。

<details open>
<summary>摘要翻译</summary>

> 生物体内的内在梯度调控着动态环境中的长期信息处理与持续学习能力。强化学习旨在模拟这种时序调控机制以提升学习效率与适应性。然而，现有忆阻器件缺乏内在梯度的构建，导致状态变化呈现随机性与突变性，破坏了持续强化学习所依赖的时序关联内部状态的生成。本研究通过分子配位层设计了一种具有稳定内在氧梯度的二阶忆阻器，实现了长达10<sup>2</sup>秒量级的动态势垒演化。这种缓慢的动态响应促进了单极脉冲刺激下氧离子的平衡迁移与扩散，从而实现了显著的电导调制（ΔG = -98.1%）。这些时序自适应电导态被定量映射至强化学习算法中的学习率，使学习任务的时间尺度与器件动力学协同演化。与传统策略相比，内在梯度驱动的调制在静态与动态环境中分别将训练迭代次数降低了68.75%与35.65%。这些发现揭示了慢动态二阶忆阻器作为物理基础的时间自适应单元的潜力，能够在神经形态系统中实现器件动力学与算法学习的有效衔接。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The intrinsic gradient in organisms governs long-term information processing and continual learning in dynamic environments. Reinforcement learning (RL) aims to emulate such temporal regulation to enhance learning efficiency and adaptability. However, the absence of intrinsic gradient construction in existing memristive devices leads to stochastic and abrupt state changes, disrupting the generation of temporally correlated internal states critical for continual RL. In this work, a second-order memristor incorporating a stable intrinsic oxygen gradient was designed via a molecular-coordinated layer, which enables a prolonged dynamic barrier evolution (>10<sup>2 </sup>s). This slow dynamic response facilitates balanced oxygen ion migration and diffusion under unipolar spike stimulation, resulting in a significant conductance modulation (ΔG = -98.1%). These temporally adaptive conductance states were quantitatively mapped to learning rates in the RL algorithm, allowing the learning task timescale to co-evolve with device dynamics. Compared with conventional strategies, intrinsic-gradient-driven modulation reduced training iterations by 68.75% and 35.65% in static and dynamic environments, respectively. These findings underscore the potential of slow-dynamic second-order memristors as physically grounded time-adaptive units bridging device dynamics and algorithmic learning in neuromorphic systems.

</details>
<br>

**关键词**: second-order memristor, intrinsic oxygen gradient, reinforcement learning, neuromorphic systems, conductance modulation, continual learning, device dynamics, temporal adaptation

---

### 54. ❌ Clay-organic matter interactions drive microbial necromass preservation in soils

**作者**: Xu Wang, Cynthia M. Kallenbach, Maya Almaraz, Katerina Georgiou, Lifei Sun, Changpeng Sang, Ping Jiang, Yue Liu, Edith Bai, Chao Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70156-1](https://doi.org/10.1038/s41467-026-70156-1)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究土壤有机质中微生物残体的矿质保护机制，属于土壤科学、环境科学和微生物生态学领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，没有使用任何医学图像数据、方法或应用场景。所有关键词与论文主题完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过同位素标记实验探究了粘土含量如何通过增强矿物保护、抑制微生物活性和减少淋失来促进微生物残体在土壤中的持久性，并发现残体来源对保留影响不大，而有机-有机界面是重要的稳定途径。

<details open>
<summary>摘要翻译</summary>

> 微生物残体日益被认为是稳定土壤有机质（SOM）的主要来源，其持久性常归因于与黏粒级矿物的相互作用。然而，这种矿物介导的稳定化机制仍不甚明晰。本研究沿黏粒含量梯度进行了一项原位双标记（<sup>13</sup>C和<sup>15</sup>N）微生物残体实验，以量化黏粒含量及残体来源（细菌与真菌）如何调控残体的存留。我们发现，较高的黏粒含量通过增强矿物保护、抑制微生物活性和多样性、并限制淋溶损失，显著提高了残体的存留。纳米二次离子质谱（NanoSIMS）成像显示，新形成的残体优先与粗糙矿物表面的有机质涂层结合，凸显了有机质-有机质界面作为重要稳定途径的作用。尽管碳氮比（C:N）和整体化学组成存在显著差异，但残体来源对其存留影响甚微，这表明土壤中残体的稳定化过程主要受更精细尺度的分子特征调控，而非宽泛的组成差异。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Microbial necromass is increasingly recognized as a major source of stable soil organic matter (SOM), and its persistence is often attributed to interactions with clay-sized minerals. However, the mechanisms underlying this mineral-mediated stabilization remain poorly understood. Here, we conducted an in situ dual-labeled (<sup>13</sup>C and <sup>15</sup>N) microbial necromass experiment across a clay gradient to quantify how clay content and necromass origin (bacterial vs. fungal) regulate necromass persistence. We find that higher clay content markedly enhances necromass retention by strengthening mineral protection, suppressing microbial activity and diversity, and limiting leaching losses. NanoSIMS imaging shows that new necromass preferentially associates with organic matter coatings on the rough mineral surfaces, highlighting organo-organic interfaces as important stabilization pathways. Necromass origin exerts little effect on retention despite marked differences in C:N ratios and bulk chemical composition, indicating that finer-scale molecular features, rather than broad compositional differences, govern necromass stabilization in soils.

</details>
<br>

**关键词**: microbial necromass, soil organic matter, clay minerals, mineral protection, NanoSIMS imaging, organo-organic interfaces, necromass persistence, soil stabilization

---

### 55. ❌ VISTA drives pancreatic tumor progression through modulation of the tumor-associated macrophage polarity

**作者**: SK Shin, Gwanghun Kim, Su Min Park, Eun-Bi Seo, Sang-Kyu Ye, Gyeong Hoon Kang, Keehoon Jung, Hyun Mu Shin, H T. Kim, Dong Sup Lee
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70215-7](https://doi.org/10.1038/s41467-026-70215-7)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究胰腺导管腺癌（PDAC）中VISTA蛋白如何调控肿瘤相关巨噬细胞极化和CD8⁺ T细胞反应，属于肿瘤免疫学和分子生物学领域。全文未涉及医学图像分析、医学成像或深度学习医学成像的任何内容，没有使用图像数据、成像技术或相关分析方法，因此所有关键词相关度均为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that V-domain immunoglobulin suppressor of T cell activation (VISTA) plays a crucial role in orchestrating macrophage polarity within the PDAC TME, and positions VISTA inhibition as a promising strategy to reshape the TME and potentiate anti-tumor immunity in PDAC.

!!! tip deepseek-chat TL;DR

    该研究发现VISTA蛋白通过调控肿瘤相关巨噬细胞的极化状态和CXCL9:SPP1比例来抑制抗肿瘤免疫，抑制VISTA可重塑肿瘤微环境并增强CD8⁺ T细胞反应，为胰腺癌治疗提供了新策略。

<details open>
<summary>摘要翻译</summary>

> 胰腺导管腺癌（PDAC）因其高度免疫抑制性的肿瘤微环境（Tumor Microenvironment, TME）而仍是最致命的恶性肿瘤之一，这限制了有效的治疗干预。本研究证明，T细胞激活的V域免疫球蛋白抑制因子（VISTA）在调控PDAC肿瘤微环境中的巨噬细胞极化方面起着关键作用。利用小鼠PDAC模型，我们发现VISTA缺失显著抑制肿瘤生长，并延长生存期。在功能上，VISTA缺失与肿瘤相关巨噬细胞（Tumor-Associated Macrophages, TAMs）的表型转变相关：从以分泌磷蛋白1（SPP1）为标志的免疫抑制表型，转变为富含C-X-C基序趋化因子配体9（CXCL9）的表型，这指示了促炎状态。这一转变伴随着具有持续细胞毒潜能的CXCR3⁺ CD8⁺ T细胞的募集增强，其中终末耗竭样CD8<sup>+</sup> T细胞状态较少出现。此外，VISTA缺失的TAMs表现出增强的抗原交叉呈递能力，进一步放大了CD8<sup>+</sup> T细胞的抗肿瘤反应。这些发现在人类PDAC数据中得到证实，反映了类似的免疫重编程趋势。通过阐明VISTA在控制Cxcl9:Spp1比例和调节CD8⁺ T细胞动态中的作用，本研究将VISTA抑制定位为一种有前景的策略，可用于重塑PDAC的肿瘤微环境并增强抗肿瘤免疫。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Pancreatic ductal adenocarcinoma (PDAC) remains one of the deadliest malignancies due to its highly immunosuppressive tumor microenvironment (TME), which limits effective therapeutic interventions. Here, we demonstrate that V-domain immunoglobulin suppressor of T cell activation (VISTA) plays a crucial role in orchestrating macrophage polarity within the PDAC TME. Using murine PDAC models, we show that VISTA deficiency markedly impairs tumor growth, leading to prolonged survival. Functionally, VISTA deficiency is linked to a shift in tumor-associated macrophages (TAMs) from an immunosuppressive phenotype marked by secreted phosphoprotein 1 (SPP1), to one enriched for C-X-C motif chemokine ligand 9 (CXCL9), indicative of a pro-inflammatory state. This shift is accompanied by enhanced recruitment of CXCR3⁺ CD8⁺ T cells with sustained cytotoxic potential, among which terminal exhaustion-like CD8<sup>+</sup> T cell states are less prevalent. Additionally, VISTA-deficient TAMs exhibit increased antigen cross-presentation, further amplifying CD8<sup>+</sup> T cell response against tumors. These findings are corroborated by human PDAC data, which reflect similar immune reprogramming trends. By defining the role of VISTA in controlling Cxcl9:Spp1 ratio and modulating CD8⁺ T cell dynamics, this study positions VISTA inhibition as a promising strategy to reshape the TME and potentiate anti-tumor immunity in PDAC.

</details>
<br>

**关键词**: VISTA, pancreatic ductal adenocarcinoma, tumor-associated macrophages, CXCL9, SPP1, CD8⁺ T cells, tumor microenvironment, immunotherapy

---

### 56. ❌ Velocity sensitivity of mechanotransduction in the afferent terminal underlies vibration detection in the Pacinian corpuscle

**作者**: A Chikamoto, Melissa Meng, Elena O. Gracheva, Sviatoslav N. Bagriantsev
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69251-0](https://doi.org/10.1038/s41467-026-69251-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是帕西尼小体的机械感受机制和振动检测的神经生物学基础，属于神经科学、生理学和生物物理学领域，完全不涉及医学图像分析、医学成像或深度学习医学成像。论文内容聚焦于感觉神经末梢的机械转导、离子通道（如Piezo2）和振动检测机制，与医学图像处理技术无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that the detection of high-frequency vibration results from the afferent terminal’s sensitivity to stimulus velocity rather than to stimulus cycle rate, which is generally independent of the corpuscular environment.

!!! tip deepseek-chat TL;DR

    该研究揭示了帕西尼小体检测高频振动的机制源于传入末梢对刺激速度的敏感性，而非传统模型中的外层核心过滤作用，并提出了基于末梢机械转导速度敏感性的修订模型。

<details open>
<summary>摘要翻译</summary>

> 帕西尼小体（Pacinian corpuscles）是羊膜动物高频振动的主要探测器，使其能够在探索和觅食过程中感知环境、识别细微纹理以及操控工具和物体。小体由包裹感觉内芯的多层外芯构成，内芯包含层状施万细胞（lamellar Schwann cells），这些细胞围绕位于中心的传入神经末梢。在传统模型中，外芯充当机械滤波器，仅允许高频振动传递至传入末梢。本文研究表明，频率滤波与感觉功能均由传入末梢而非外芯执行。我们证实，高频振动的检测源于传入末梢对刺激速度的敏感性，而非对刺激周期率的响应。此外，这些特性总体上独立于小体环境，而是反映了末梢中机械门控离子通道（如Piezo2）的生物物理特性。我们提出了一个修正模型，其中帕西尼小体的高频调谐功能由传入末梢机械转导的速度敏感性实现。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Pacinian corpuscles are the principal detectors of high-frequency vibrations in amniotes, enabling environmental awareness, the detection of fine textures, and the manipulation of tools and objects during exploration and foraging. Corpuscles consist of a multilayered outer core enclosing a sensory inner core, which contains lamellar Schwann cells enveloping the afferent terminal at its center. In the traditional model, the outer core acts as a mechanical filter, enabling only high-frequency vibrations to reach the afferent terminal. Here, we show that the afferent terminal, not the outer core, carries out both the frequency filtering and sensory functions. We demonstrate that the detection of high-frequency vibration results from the afferent terminal's sensitivity to stimulus velocity rather than to stimulus cycle rate. Furthermore, these properties are generally independent of the corpuscular environment and instead reflect the biophysical characteristics of the mechanically gated ion channels in the terminal, such as Piezo2. We present a revised model wherein the high-frequency tuning of Pacinian corpuscles is enabled by the velocity sensitivity of mechanotransduction in the afferent terminal.

</details>
<br>

**关键词**: Pacinian corpuscle, vibration detection, afferent terminal, mechanotransduction, velocity sensitivity, Piezo2, high-frequency tuning, mechanical filter

---

### 57. ❌ Canonical BAF chromatin remodeling complex specifies stem cell fate via cell-type-specific co-factor recruitment

**作者**: Mingyi Zhang, Jifan Feng, Tingwei Guo, Yu Fu, Fei Pei, Lu Gao, Zhiyuan Hu, Thach‐Vu Ho, Yang Chai
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70038-6](https://doi.org/10.1038/s41467-026-70038-6)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是染色质重塑复合体cBAF在成体干细胞命运决定和微环境维持中的分子机制，属于干细胞生物学和表观遗传学领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，没有使用任何医学图像数据、成像技术或图像分析方法。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    Using the adult mouse incisor, cBAF is established as a central regulator of adult stem cell niches and lineage commitment, and cofactor-dependent mechanisms that may have broader implications for tissue regeneration and BAF-associated disorders are highlighted.

!!! tip deepseek-chat TL;DR

    该研究揭示了染色质重塑复合体cBAF通过招募不同的转录共因子来调控成体间充质干细胞的命运决定和微环境维持的分子机制。

<details open>
<summary>摘要翻译</summary>

> 经典BAF（cBAF）染色质重塑复合体中的单个亚基已知可调控干细胞行为，且亚基间存在一定的功能冗余。然而，cBAF复合体如何指导成体干细胞命运特化并维持干细胞微环境仍不明确。本研究以成年小鼠门齿为模型，发现cBAF通过募集不同的转录共因子来塑造细胞类型特异性的染色质调控，从而决定间充质干细胞（MSC）的命运。通过单细胞多组学与体内功能分析，我们鉴定出含ARID1的cBAF复合体是维持MSC自我更新与分化间动态平衡的关键守门员。具体而言，cBAF-DLX2相互作用通过重塑微环境特征标记物Runx2的内含子染色质可及性来维持微环境特性；而cBAF-FOXO1则直接调控谱系相关转录因子（包括STAT3和TRP53等）的启动子可及性，以平衡祖细胞增殖与分化。对RUNX2和TRP53的功能扰动证实了它们在cBAF下游对微环境维持和命运特化的调控作用。我们的研究确立了cBAF作为成体干细胞微环境与谱系定向的核心调控因子，并揭示了共因子依赖的调控机制，这些发现可能对组织再生及BAF相关疾病具有更广泛的启示意义。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Individual subunits within the canonical BAF (cBAF) chromatin remodeling complex are known to regulate stem cell behavior, with some functional redundancy across subunits. Yet, how the cBAF complex directs adult stem cell fate specification and maintains stem cell niches remains unclear. Using the adult mouse incisor, we show that cBAF specifies mesenchymal stem cell (MSC) fate by recruiting distinct transcriptional co-factors to shape cell-type-specific chromatin regulation. Through single-cell multi-omics and in vivo functional analyses, we identify ARID1-containing cBAF as an essential gatekeeper that maintains the dynamic balance between MSC self-renewal and differentiation. Specifically, cBAF-DLX2 interactions preserve niche identity by remodeling intronic chromatin accessibility of niche-defining marker Runx2, while cBAF-FOXO1 directly modulates promoter accessibility of lineage-regulating transcription factors, including STAT3 and TRP53, among others, to balance progenitor proliferation and differentiation. Functional perturbation of RUNX2 and TRP53 confirms their roles downstream of cBAF in niche maintenance and fate specification. Our findings establish cBAF as a central regulator of adult stem cell niches and lineage commitment, and highlight cofactor-dependent mechanisms that may have broader implications for tissue regeneration and BAF-associated disorders.

</details>
<br>

**关键词**: cBAF chromatin remodeling complex, adult stem cell fate specification, mesenchymal stem cell, chromatin accessibility, transcriptional co-factors, stem cell niche, single-cell multi-omics, lineage commitment

---

### 58. ❌ Chip scale coil stabilized Brillouin laser driving a room temperature trapped ion qubit

**作者**: Nitesh Chauhan, Christopher Caron, Andrei Isichenko, Meiting Song, Zhenyu Wei, Nishat Helaly, K. Liu, Jiawei Wang, Robert Niffenegger, Daniel J. Blumenthal
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69948-2](https://doi.org/10.1038/s41467-026-69948-2)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是量子计算和光学时钟领域的芯片级布里渊激光器，用于驱动室温下捕获的锶离子量子比特，涉及光子集成、激光稳定、量子信息处理等技术。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均与医学图像分析相关，而论文内容完全不涉及医学图像、医学成像或深度学习在医学成像中的应用，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了量子系统中传统激光器体积大、功耗高的问题，通过开发芯片级线圈稳定的布里渊激光器，成功驱动了室温捕获离子量子比特，实现了高稳定性的光学时钟过渡和量子比特操作。

<details open>
<summary>摘要翻译</summary>

> 光子集成稳定超低噪声激光器对于可扩展、便携的量子信息系统至关重要。囚禁离子是量子计算与光学原子钟的主要实现方式之一，其室温操作特性为便携化应用提供了可能。当前系统依赖于自由空间激光器、稳频腔、频率转换及低温基础设施，限制了系统的尺寸、重量与功耗。本研究展示了一种芯片级线圈稳频的674纳米布里渊激光器，该激光器在无体光学参考腔的条件下，驱动了室温表面电极囚禁的<sup>88</sup>Sr<sup>+</sup>离子中的量子比特态制备与测量以及光学钟跃迁。采用CMOS兼容氮化硅集成的3米线圈与布里渊激光器实现了8.8×10<sup>-13</sup>（20毫秒）的稳定度，足以探测0.4赫兹的四极光学钟跃迁。该离子驯服激光器实现了5.3×10<sup>-13</sup>/√τ的稳定度、1.5千赫兹线宽的谱线测量，以及99.6%的量子比特态制备与测量保真度。这些成果为将稳频激光器与囚禁离子芯片集成，以实现便携且鲁棒的量子技术指明了方向。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Photonic integrated stable, ultra-low-noise lasers are essential for scalable and portable quantum information systems. Trapped ions are a leading modality for quantum computing and optical clocks, with room-temperature operation enabling portable applications. Current systems rely on free-space lasers and stabilization cavities, frequency conversion, and cryogenic infrastructure, limiting size, weight, and power. We demonstrate a chip-scale coil-stabilized 674 nm Brillouin laser driving qubit state preparation and measurement and the optical clock transition in a room-temperature surface electrode trapped <sup>88</sup>Sr<sup>+</sup> ion without a bulk-optic reference cavity. The CMOS compatible silicon nitride integrated 3-meter coil and Brillouin laser achieve 8.8×10<sup>-13</sup> stability at 20 ms, sufficient to interrogate the 0.4 Hz quadrupole optical clock transition. The ion-disciplined laser achieves 5.3 <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:mo>×</mml:mo><mml:msup><mml:mrow><mml:mn>10</mml:mn></mml:mrow><mml:mrow><mml:mo>-</mml:mo><mml:mn>13</mml:mn></mml:mrow></mml:msup><mml:mo>/</mml:mo><mml:msqrt><mml:mrow><mml:mi>τ</mml:mi></mml:mrow></mml:msqrt></mml:math> stability, spectroscopy with 1.5 kHz linewidths, and 99.6% qubit state preparation and measurement fidelity. These results light the way towards integration of stabilized lasers with trapped-ion chips for portable and robust quantum technologies.

</details>
<br>

**关键词**: chip-scale Brillouin laser, trapped ion qubit, room-temperature operation, optical clock transition, quantum information systems, CMOS compatible silicon nitride, laser stabilization, portable quantum technologies

---

### 59. ❌ A hotspot phosphorylation site on SHP2 drives oncoprotein activation and drug resistance

**作者**: Prashath Karunaraj, Remkes Scheele, Malcolm L. Wells, Ruchita Rathod, Ipek Simay Gokulu, Sophia Abrahamson, Lila Taylor, Lamia Chowdhury, Abiha Kazmi, Weixiao Song, Peter Hornbeck, Jing Li, Anum Glasgow, Neil Vasan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70060-8](https://doi.org/10.1038/s41467-026-70060-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究SHP2磷酸化在癌症信号通路中的作用和耐药机制，属于分子生物学、癌症生物学和药物发现领域。全文未涉及医学图像分析、医学成像或深度学习医学成像的任何内容，因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is established that SHP2 pY62 is a phosphorylation hotspot phenocopying mutational activation, a mechanism of primary resistance to SHP2 inhibitors, and a cancer drug target distinct from wildtype SHP2.

!!! tip deepseek-chat TL;DR

    该研究发现SHP2在酪氨酸62位点的磷酸化是一个热点修饰位点，能导致SHP2组成性激活、驱动MAPK信号通路，并赋予SHP2抑制剂原发性耐药，为癌症治疗提供了新靶点。

<details open>
<summary>摘要翻译</summary>

> SHP2是一种磷酸酶，也是受体酪氨酸激酶（RTK）驱动的RAS/丝裂原活化蛋白激酶（MAPK）信号通路的关键介质。尽管临床前数据表现出良好前景，但SHP2抑制剂在临床上疗效甚微，且其原发性耐药的确切临床机制尚未明确。本研究揭示，SHP2第62位酪氨酸磷酸化（pY62）是患者蛋白质组及RTK驱动型肿瘤中的磷酸化热点位点。我们证明，SRC家族激酶能够直接磷酸化SHP2的Y62位点，该过程位于RTK下游，但并非由RTK直接磷酸化。通过生物化学与生物物理学分析，我们发现SHP2<sup>Y62D</sup>突变会强制蛋白维持开放、活跃的构象，导致组成型磷酸酶激活，足以驱动MAPK信号通路，并对变构SHP2抑制剂产生耐药性。这些研究结果证实，SHP2 pY62是一个模拟突变激活的磷酸化热点，是SHP2抑制剂原发性耐药的一种机制，并成为一个不同于野生型SHP2的癌症药物靶点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> SHP2 is a phosphatase and a critical mediator of receptor tyrosine kinase (RTK)-driven RAS/mitogen-activated protein kinase (MAPK) signaling. Despite promising preclinical data, SHP2 inhibitors have shown minimal clinical efficacy, with no defined clinical mechanisms of primary resistance. Here, we elucidate phosphorylation of SHP2 at tyrosine 62 (pY62) as a hotspot phosphorylation site in the proteome and RTK-driven tumor types in patients. We demonstrate that SRC family kinases directly phosphorylate SHP2 at Y62, downstream of but not directly phosphorylated by RTKs. Using biochemical and biophysical analyses, we show that SHP2<sup>Y62D</sup> enforces an open, active conformation, resulting in constitutive phosphatase activation that is sufficient to activate MAPK signaling and confer resistance to allosteric SHP2 inhibitors. These findings establish that SHP2 pY62 is a phosphorylation hotspot phenocopying mutational activation, a mechanism of primary resistance to SHP2 inhibitors, and a cancer drug target distinct from wildtype SHP2.

</details>
<br>

**关键词**: SHP2, phosphorylation, tyrosine 62, MAPK signaling, drug resistance, SHP2 inhibitors, cancer, SRC family kinases

---

### 60. ❌ Universal work extraction in quantum thermodynamics

**作者**: Kaito Watanabe, Ryuji Takagi
**期刊/来源**: nature_communications
**发布日期**: 2025-04-16
**arXiv链接**: [https://arxiv.org/abs/2504.12373](https://arxiv.org/abs/2504.12373)
**DOI**: [10.1038/s41467-026-69143-3](https://doi.org/10.1038/s41467-026-69143-3)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题为'Universal work extraction in quantum thermodynamics'，摘要内容完全围绕量子热力学中的功提取问题展开，涉及量子系统、自由能、状态感知与状态不可知等概念。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均属于医学图像分析领域，与论文的量子热力学主题无任何关联。论文未提及医学图像、医学成像技术或深度学习在医学成像中的应用，因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了量子热力学中未知量子状态下的最大功提取问题，并提出了一种不依赖输入状态描述的通用功提取协议，实现了与自由能相等的最优功提取。

<details open>
<summary>摘要翻译</summary>

> 评估纳米尺度量子系统中可提取的最大功是量子热力学的核心问题之一。先前研究在关键假设下将输入态的自由能确定为可提取功的最优速率：实验者已知给定量子态的完整描述，这将其适用性限制在极为有限的情境中。本文证明，即使完全未知输入态，仍可实现这一最优可提取功，从而消除了前述基本操作限制。我们通过提出一种普适的功提取协议达成此目标——该协议的描述不依赖于输入态，却能提取出与未知输入态自由能等量的功。值得注意的是，我们的结果部分涵盖了无限维系统的情况，而即使在传统的态已知设定下，此类系统的最优可提取功也尚未明确。研究结果表明：尽管在完成信息论任务时，态已知与态未知情境存在本质差异，但关于给定态的信息是否已知并不影响渐近功提取的最优性能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Evaluating the maximum amount of work extractable from a nanoscale quantum system is one of the central problems in quantum thermodynamics. Previous works identified the free energy of the input state as the optimal rate of extractable work under the crucial assumption: experimenters know the description of the given quantum state, which restricts the applicability to significantly limited settings. Here, we show that this optimal extractable work can be achieved without knowing the input states at all, removing the aforementioned fundamental operational restrictions. We achieve this by presenting a universal work extraction protocol, whose description does not depend on input states but nevertheless extracts work quantified by the free energy of the unknown input state. Remarkably, our result partially encompasses the case of infinite-dimensional systems, for which optimal extractable work has not been known even for the standard state-aware setting. Our results clarify that, in spite of the crucial difference between the state-aware and state-agnostic scenarios in accomplishing information-theoretic tasks, whether we are in possession of information on the given state does not influence the optimal performance of the asymptotic work extraction.

</details>
<br>

**关键词**: quantum thermodynamics, work extraction, free energy, quantum system, state-agnostic, universal protocol, asymptotic work extraction

---

### 61. ❌ In-cell bypass diodes for high-efficiency and shading-tolerant back contact silicon photovoltaic modules

**作者**: Hanbo Tang, Yunpeng Li, Hao Lin, Chaowei Xue, Genshun Wang, Yongyuan Xu, Feng Ye, Liang Fang, Xixiang Xu, Pingqi Gao
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70005-1](https://doi.org/10.1038/s41467-026-70005-1)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究光伏太阳能电池模块的阴影耐受性问题，提出了一种集成反向导电性的电池架构，与医学图像分析、医学成像或深度学习医学成像完全无关。论文内容属于光伏技术、太阳能电池和可再生能源领域，未涉及任何医学或医疗相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种具有集成反向导电通道的太阳能电池架构，以解决光伏模块在部分阴影条件下的功率损失和热损伤问题，实验证明该设计能显著改善热管理和功率输出稳定性。

<details open>
<summary>摘要翻译</summary>

> 局部遮光是光伏组件户外部署中的常见现象，可能导致显著的功率损失与严重的热损伤。现有解决方案在效果与成本间难以兼顾，亟需一种从太阳能电池层面进行根本性重构的彻底解决方案。本文提出一种具备集成反向导电特性的电池结构以应对这一挑战。我们从旁路二极管中汲取灵感，推导出设计原则，成功在电池内部引入了空间均匀分布的反向导通通道。这些经工程设计的胞内通道表现出偏压依赖的开关特性，使电池在保持功率转换效率的同时实现反向导电。本文阐明了该电池的内在工作机制与调控策略。采用所设计电池制备的光伏组件在局部遮光条件下展现出显著的热管理与功率输出稳定性优势。本研究中的设计原则与导通通道策略也为其他钝化接触太阳能电池提供了参考。这种胞内设计方法在可靠性、成本与集成度方面具有优势，有望应用于下一代光伏技术。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Partial shading is a common condition in the outdoor deployment of photovoltaic modules, potentially causing significant power loss and severe thermal damage. Limitations of existing solutions in balancing effect and cost necessitate a thorough solution, which involves a fundamental redesign at the solar cell level. Here we propose a cell architecture featuring integrated reverse conductivity to address this challenge. We derive the design principles by drawing inspiration from bypass diodes, and manage to introduce spatially uniform reverse conduction channels to the cell. These engineered in-cell channels exhibit bias-dependent switching behavior that enables reverse conductivity of the cell without compromising power conversion efficiency. The underlying mechanisms and modulation strategies of the cell are elucidated. Prepared photovoltaic modules composed of the proposed cells demonstrate clear advantages in thermal management and power output stability under partial shading conditions. The design principles and conduction channel strategies in this work also provide insight for other passivating-contact solar cells. The in-cell design approach offers merits in reliability, cost, and integration, and holds promise for next-generation photovoltaic technologies.

</details>
<br>

**关键词**: photovoltaic modules, partial shading, bypass diodes, reverse conductivity, solar cell architecture, thermal management, power conversion efficiency, back contact silicon

---

### 62. ❌ GPR146 in adipose tissue drives adipose-liver crosstalk and promotes hepatic steatosis in mice

**作者**: Yu Shi, Kai Yan Cheng, Thi Tun Thi, Yifan Wang, Yang Yang, Xiaoyun Cao, Vanna Chhay, Yujia Shen, Yuchen He, Chen Zhang, Yan Ting Lim, Amy Deik, Courtney Dennis, Kerry Pierce, Jason Roy, Martin Wabitsch, Clary B. Clish, Alexander S. Banks, Radoslaw M. Sobota, Chad A. Cowan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70136-5](https://doi.org/10.1038/s41467-026-70136-5)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究GPR146受体在脂肪组织中的作用及其通过脂肪-肝脏串扰促进肝脏脂肪变性的机制，属于代谢疾病、分子生物学和肝脏病理学领域。全文未涉及医学图像分析、医学成像或深度学习医学成像的任何内容，没有使用图像数据、成像技术或图像分析方法。因此所有关键词相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The orphan G protein-coupled receptor GPR146 is identified as a regulator of hepatic steatosis through adipose-liver crosstalk and a potential therapeutic target for MASLD.

!!! tip deepseek-chat TL;DR

    该研究发现孤儿G蛋白偶联受体GPR146通过调节脂肪组织生物学（促进脂肪生成和增强脂肪分解）增加游离脂肪酸向肝脏的输送，从而驱动肝脏脂肪变性，为代谢功能障碍相关脂肪性肝病（MASLD）提供了新的治疗靶点。

<details open>
<summary>摘要翻译</summary>

> 代谢功能障碍相关脂肪性肝病（MASLD）的有限治疗选择凸显了深入理解其机制和开发新治疗策略的迫切性。本研究通过脂肪-肝脏互作，发现孤儿G蛋白偶联受体GPR146是肝脏脂肪变性的调控因子。人类遗传学分析将GPR146基因座与循环中的肝损伤和炎症标志物相关联。在小鼠中，无论是组成性还是急性敲除GPR146，均能预防饮食诱导的肥胖和肝脏脂肪变性。值得注意的是，脂肪组织特异性（而非肝脏特异性）敲除GPR146可通过限制游离脂肪酸（FFA）的流入，减少肝脏脂质堆积。机制上，GPR146通过Gαq-PKC-AKT信号通路促进前脂肪细胞的脂肪生成，增加脂质储存能力；同时通过激活ERK增强成熟脂肪细胞的脂解作用，从而升高循环FFA水平。这些协同作用共同增加了FFA向肝脏的输送，促进了甘油三酯的积累。我们的研究确立了GPR146是脂肪组织生物学的多效性调控因子，并可能成为MASLD的潜在治疗靶点。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The limited therapeutic options for metabolic dysfunction-associated steatotic liver disease (MASLD) underscore the need for deeper mechanistic insight and new treatment strategies. Here, we identify the orphan G protein-coupled receptor GPR146 as a regulator of hepatic steatosis through adipose-liver crosstalk. Human genetic analyses link the GPR146 locus to circulating markers of liver injury and inflammation. In mice, both constitutive and acute GPR146 depletion protect against diet-induced obesity and hepatic steatosis. Notably, adipose-specific, but not liver-specific, GPR146 deletion reduces hepatic lipid accumulation by limiting free fatty acid (FFA) influx. Mechanistically, GPR146 promotes adipogenesis in preadipocytes via Gαq-PKC-AKT signaling, increasing lipid storage capacity, and enhances lipolysis in mature adipocytes through ERK activation, elevating circulating FFA. Together, these coordinated actions increase FFA delivery to the liver, promoting triglyceride accumulation. Our findings establish GPR146 as a pleiotropic regulator of adipose tissue biology and a potential therapeutic target for MASLD.

</details>
<br>

**关键词**: GPR146, adipose-liver crosstalk, hepatic steatosis, MASLD, free fatty acid, adipogenesis, lipolysis, therapeutic target

---

### 63. ❌ Generative modeling enables molecular structure retrieval from Coulomb explosion imaging

**作者**: Xiang (Lorraine) Li, T. Jahnke, Ritika Dagar, Jiaqi Han, Minkai Xu, Michael Meyer, Markus Ilchen, Daniel Rolles, Artem Rudenko, Florian Trinter, Thomas J A Wolf, Jana Thayer, James Cryan, Stefano Ermon, Phay J. Ho
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70160-5](https://doi.org/10.1038/s41467-026-70160-5)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是分子结构重建问题，使用Coulomb爆炸成像技术和基于扩散的Transformer神经网络来重建分子几何结构。虽然涉及成像和深度学习技术，但研究对象是分子化学结构而非医学图像，应用领域是化学/物理而非医学。所有关键词均与医学图像分析相关，而本文完全不涉及医学领域，因此相关度为0。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文解决了从Coulomb爆炸成像的离子动量分布中重建分子几何结构这一非线性逆问题，通过基于扩散的Transformer神经网络实现了低于一个玻尔半径的平均绝对误差重建精度。

<details open>
<summary>摘要翻译</summary>

> 在真实空间与时间中捕捉化学反应过程中分子结构的变化，是一个长期以来的梦想，也是理解和最终控制飞秒化学的重要前提。应对这一挑战性任务的关键方法是库仑爆炸成像技术，该技术近期得益于高重复频率X射线自由电子激光光源的出现而取得了决定性进展。该技术通过分子快速库仑爆炸产生的离子动量分布来推断分子结构信息。从这些分布中反演分子结构是一个高度非线性的逆问题，对于超过几个原子组成的分子，该问题至今尚未得到解决。在此，我们利用基于扩散模型的Transformer神经网络应对这一挑战。研究表明，该网络能够从离子动量分布中重建未知分子几何构型，其平均绝对误差低于一个玻尔半径（约为典型化学键长度的一半）。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Capturing the structural changes that molecules undergo during chemical reactions in real space and time is a long-standing dream and an essential prerequisite for understanding and ultimately controlling femtochemistry. A key approach to tackle this challenging task is Coulomb explosion imaging, which has benefited decisively from recently emerging high-repetition-rate X-ray free-electron laser sources. With this technique, information on the molecular structure is inferred from the momentum distributions of the ions produced by the rapid Coulomb explosion of molecules. Retrieving molecular structures from these distributions poses a highly nonlinear inverse problem that remains unsolved for molecules consisting of more than a few atoms. Here, we address this challenge using a diffusion-based Transformer neural network. We show that the network reconstructs unknown molecular geometries from ion-momentum distributions with a mean absolute error below one Bohr radius, which is half the length of a typical chemical bond.

</details>
<br>

**关键词**: Coulomb explosion imaging, molecular structure retrieval, diffusion-based Transformer, ion-momentum distributions, nonlinear inverse problem, molecular geometries, neural network, femtochemistry

---

### 64. ❌ TIGAR regulates intestinal mucus barrier integrity by inhibiting lactylation of G6PD/6PGD in ulcerative colitis

**作者**: Dan Wu, Sen Su, Panyang Zhang, Xule Zha, Yan Wei, Ting Zhang (102583), Xiaoyan Liu, Qian Hong Chen, Chunyan Li, Qianying Huang, Zhihao Zhou, Yan Yang, Lin Xia, Fan Shijun, Xi Peng
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70263-z](https://doi.org/10.1038/s41467-026-70263-z)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是溃疡性结肠炎（UC）的分子机制，聚焦于TIGAR蛋白如何通过抑制G6PD/6PGD的乳酰化来调节NADPH合成、氧化应激和肠道黏液屏障完整性。全文涉及细胞生物学、分子机制和动物模型实验，未提及任何医学影像分析、医学成像或深度学习在医学影像中的应用。因此，所有关键词与论文内容完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is demonstrated that TIGAR inhibits lactylation of the key NADPH-synthesizing enzymes G6PD and 6PGD, thereby preserving their enzymatic activities by promoting G6PD homodimer formation and 6PGD binding to NADP+.

!!! tip deepseek-chat TL;DR

    该研究揭示了在溃疡性结肠炎中，TIGAR通过抑制G6PD和6PGD的乳酰化来维持NADPH合成和氧化还原稳态，从而保护肠道黏液屏障完整性，并提出了TIGAR作为潜在治疗靶点。

<details open>
<summary>摘要翻译</summary>

> 杯状细胞中的氧化应激与代谢失调是溃疡性结肠炎（UC）发病机制的关键环节。TIGAR能促进NADPH合成并有助于缓解氧化应激，但其如何调控NADPH生成并影响UC尚不明确。本研究揭示，TIGAR通过抑制关键NADPH合成酶G6PD（位点K432）和6PGD（位点K38）的乳酸化修饰，从而维持其酶活性——具体机制为促进G6PD同源二聚体形成以及增强6PGD与NADP⁺的结合。在雄性UC小鼠模型中，持续低表达的TIGAR会提升乳酸水平，促使G6PD和6PGD发生乳酸化并损害其功能。这一过程抑制了NADPH合成，加剧了杯状细胞的氧化应激。随之导致的Trx1还原酶活性下降，会诱导黏蛋白加工酶AGR2发生S-亚硝基化，从而抑制成熟MUC2的产生并破坏肠道黏液屏障。我们的研究阐明了TIGAR维持细胞氧化还原稳态的分子通路，为其作为UC潜在治疗靶点提供了理论依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Oxidative stress and metabolic dysregulation in goblet cells are pivotal in ulcerative colitis (UC) pathogenesis. TIGAR promotes the synthesis of NADPH and contributes to mitigate oxidative stress, but how it regulates NADPH production and affects UC remains unclear. Here we demonstrate that TIGAR inhibits lactylation of the key NADPH-synthesizing enzymes G6PD (at K432) and 6PGD (at K38), thereby preserving their enzymatic activities by promoting G6PD homodimer formation and 6PGD binding to NADP<sup>+</sup>. In male UC mice, persistently low TIGAR expression elevates lactate levels, promoting the lactylation of G6PD and 6PGD and impairing their function. This process suppresses NADPH synthesis, exacerbating goblet cell oxidative stress. The resulting decline in Trx1 reductase activity induces S-nitrosylation of the mucin-processing enzyme AGR2, thereby inhibiting mature MUC2 production and compromising the intestinal mucus barrier. Our findings elucidate a mechanistic pathway through which TIGAR maintains cellular redox homeostasis, presenting it as a potential therapeutic target for UC.

</details>
<br>

**关键词**: TIGAR, ulcerative colitis, lactylation, G6PD, 6PGD, NADPH, oxidative stress, mucus barrier

---

### 65. ❌ Pressure dependence of surface tension of polymer melts under high vacuum

**作者**: Thanmayee Shastry, A.P. Ashika, Aum Sagar Panda, Kai Jiang, Rong‐Ming Ho
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70208-6](https://doi.org/10.1038/s41467-026-70208-6)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究聚合物熔体在高真空下的表面张力与气压关系，属于高分子物理/材料科学领域，完全不涉及医学图像分析、医学成像或深度学习医学成像。论文内容聚焦于聚合物表面性质、气压效应和实验测量，与医学图像处理无任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了聚合物熔体在高真空条件下的表面张力随气压变化的异常行为，发现表面张力随温度降低而随气压增加，并用Hill方程描述了测量结果。

<details open>
<summary>摘要翻译</summary>

> 聚合物在常压或高压条件下的表面张力已被广泛研究，但在高真空环境下的相关研究较少。本文利用自主搭建的装置，研究了空气压力对聚合物熔体表面张力的影响。以往研究表明，大多数聚合物的表面张力随温度或压力的升高呈线性下降，而我们的工作揭示了聚合物表面张力的一种反常行为：表面张力虽仍随温度升高而降低，却随空气压力增大而增加。在10⁻⁴至10⁵ N/m²的压力范围内，多个聚合物样品的实测表面张力均能通过希尔方程（Hill equation）良好描述。结合空气吸附（air adsorption）的背景，本文进一步讨论了该行为对空气-聚合物相互作用的启示。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The surface tension of polymers under ambient or high-pressure conditions has been extensively studied but is less explored under high vacuum. Here, the effect of air pressure on the surface tension of polymer melts is studied by using a home-built apparatus. While previous studies showed that the surface tension of most polymers decreases linearly when the temperature or pressure is increased, we show that the surface tension of polymer exhibits an anomalous behavior: The surface tension remains a decreasing function of the temperature, but increases with increasing air pressure. The measured surface tension of several polymer samples is well described by the Hill equation in the pressure range of <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:msup><mml:mrow><mml:mn>10</mml:mn></mml:mrow><mml:mrow><mml:mo>-</mml:mo><mml:mn>4</mml:mn></mml:mrow></mml:msup></mml:math> to <mml:math xmlns:mml="http://www.w3.org/1998/Math/MathML"><mml:msup><mml:mrow><mml:mn>10</mml:mn></mml:mrow><mml:mrow><mml:mn>5</mml:mn></mml:mrow></mml:msup><mml:mspace></mml:mspace><mml:mi>N</mml:mi><mml:mo>/</mml:mo><mml:msup><mml:mrow><mml:mi>m</mml:mi></mml:mrow><mml:mrow><mml:mn>2</mml:mn></mml:mrow></mml:msup></mml:math>. The implication of this behavior on the air-polymer interaction is discussed within the context of air adsorption.

</details>
<br>

**关键词**: polymer melts, surface tension, high vacuum, air pressure, Hill equation, air adsorption, anomalous behavior, pressure dependence

---

### 66. ❌ Optimizing cross-domain transfer for universal machine learning interatomic potentials

**作者**: Jaesun Kim, Jinmu You, Yutack Park, Yunsung Lim, Yujin Kang, Jisu Kim, Hyejin Jeon, Suyeon Ju, Deokgi Hong, Seung Yul Lee, Saerom Choi, Yongdeok Kim, Jae Seung Lee, Seungwu Han
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**arXiv链接**: [https://arxiv.org/abs/2510.11241](https://arxiv.org/abs/2510.11241)
**DOI**: [10.1038/s41467-026-70195-8](https://doi.org/10.1038/s41467-026-70195-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确表明该研究专注于机器学习的原子间势能（interatomic potentials）在材料科学和化学领域的应用，包括分子、晶体、表面和催化吸附能等。全文未提及任何医学图像分析、医学成像或相关概念。研究背景为材料科学和计算化学，与医学图像分析领域完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A transferable multi-domain training strategy that jointly optimizes parameters through selective regularization, coupled with a domain-bridging set that aligns potential-energy surfaces across datasets that achieves state-of-the-art accuracy in cross-domain benchmarks.

!!! tip deepseek-chat TL;DR

    该论文提出了一种可转移的多领域训练策略，用于优化机器学习原子间势能的跨领域泛化能力，并在包含分子、晶体和表面的15个开放数据集上训练的SevenNet-Omni模型在跨领域基准测试中达到了最先进的精度。

<details open>
<summary>摘要翻译</summary>

> 兼具精确性与可迁移性的机器学习原子间势函数对于加速材料与化学发现至关重要。然而，许多现有的通用模型过度拟合于狭窄的化学空间或计算协议，限制了其在多样化化学与功能领域的可靠性。本文提出一种可迁移的多领域训练策略，该策略通过选择性正则化联合优化参数，并结合一个领域桥接集来对齐不同数据集间的势能面。系统性消融实验表明，所提出的策略能协同增强分布外泛化能力，同时保持领域内保真度。基于此观察，我们在涵盖分子、晶体与表面的15个公开数据集上训练了SevenNet-Omni模型。该模型在跨领域基准测试中达到了最先进的精度，在包括催化表面吸附能和金属-有机框架在内的多种场景中实现了化学精度。SevenNet-Omni还能通过有效迁移从更大规模、较低精度数据库中学到的知识，精确复现高保真性质。这一框架为构建连接量子力学保真度与化学领域的通用可迁移模型提供了一条可扩展的路径。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Accurate yet transferable machine-learning interatomic potentials are essential for accelerating materials and chemical discovery. However, many existing universal models are overfitted to narrow chemical spaces or computational protocols, limiting their reliability across diverse chemical and functional domains. Here, we introduce a transferable multi-domain training strategy that jointly optimizes parameters through selective regularization, coupled with a domain-bridging set that aligns potential-energy surfaces across datasets. Systematic ablation experiments show that suggested strategies synergistically enhance out-of-distribution generalization while preserving in-domain fidelity. Based on our observation, we train SevenNet-Omni on 15 open datasets spanning molecules, crystals, and surfaces. Our model achieves state-of-the-art accuracy in cross-domain benchmarks, reaching chemical accuracy in various scenarios including adsorption-energy in catalytic surfaces and metal-organic frameworks. SevenNet-Omni also accurately reproduces high-fidelity properties by effectively transferring knowledge learned from larger, lower-accuracy databases. This framework offers a scalable route toward universal, transferable models that bridge quantum-mechanical fidelities and chemical domains.

</details>
<br>

**关键词**: machine-learning interatomic potentials, cross-domain transfer, multi-domain training, out-of-distribution generalization, materials discovery, chemical accuracy, universal models, potential-energy surfaces

---

### 67. ❌ Climate’s influence on topography encoded in stream network topology and geometry

**作者**: Minhui Li, Hansjörg Seybold, Fu X, Baosheng Wu, Peter A. Raymond, James W. Kirchner
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70200-0](https://doi.org/10.1038/s41467-026-70200-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是地球科学和水文学领域，分析河流网络拓扑结构和几何形态如何受气候和地形演化影响，与医学图像分析、医学成像、深度学习医学成像等关键词完全无关。论文内容涉及地理学、水文学、气候学，没有任何医学或医疗相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究分析了美国16,322个河流网络的拓扑和几何特征，发现气候通过影响河流网络的几何和地形属性（如交汇角度和河道坡度比）来调节网络拓扑结构，揭示了河流网络几何、地形和拓扑在气候驱动下的协同演化关系。

<details open>
<summary>摘要翻译</summary>

> 河流网络展现了地球水文循环如何嵌入其三维地形之中。从自上而下的视角看，河流网络的形态通常通过其拓扑连通性与分支几何结构来描述。尽管这两大特征天然关联，但以往研究大多将其独立分析，导致对其协同演化机制理解不足。本文分析了美国本土16,322个五级真实河流网络的拓扑结构与几何形态，揭示了它们如何受气候及地形演化过程的塑造。研究发现约73%的网络在其分支模式中表现出拓扑自相似性，且小型支流以系统性更大的角度汇入主流。分析进一步表明，其他研究中观测到的气候与网络拓扑之间的相关性，主要通过网络几何与地形属性（如汇流角度及合并支流的河道坡度比）的气候依赖性所介导。这些发现论证了在气候驱动下的景观演化过程中，网络几何、地形与拓扑结构的协同演化关系。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Stream networks express how Earth's hydrologic cycle is embedded within its three-dimensional topography. In a top-down view, a stream network's morphology is often described by its topological connectivity and branching geometry. Although these two characteristics are naturally connected, they have mostly been studied independently, leaving their co-evolution poorly understood. Here, we analyze the topology and geometry of 16,322 5<sup>th</sup>-order real-world stream networks across the contiguous United States, showing how they are shaped by climate and the evolution of Earth's topography. We find that ~73% of these networks show topological self-similarity in their branching patterns and that small tributaries join larger streams at systematically wider angles. Our analysis further reveals that correlations between climate and network topology observed in other studies are mainly mediated through the climate-dependence of networks' geometric and topographic properties, such as their junction angles and channel slope ratios of merging tributaries. These findings demonstrate the co-evolution of network geometry, topography, and topology under the influence of landscape evolution driven by climatic forcing.

</details>
<br>

**关键词**: stream networks, topology, geometry, climate, topography, branching patterns, junction angles, channel slope ratios

---

### 68. ❌ Declining grassland canopy height in China under asymmetric biomass allocation

**作者**: Huaqiang Li, Xinmiao Hu, Fei Li, Yingjun Zhang, Kejian Lin, Jianjun Wang, Jianjun Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70275-9](https://doi.org/10.1038/s41467-026-70275-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是中国草原冠层高度变化及其与生物量分配、气候因素和放牧的关系，使用机器学习算法融合气候因子、卫星数据和地面调查数据来估计地上生物量。研究领域属于生态学、遥感技术和环境科学，完全不涉及医学图像分析、医学成像或深度学习在医学成像中的应用。所有关键词与论文内容完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过机器学习融合多源数据，发现2001-2022年中国草原地上生物量增加主要由水平生物量分配驱动，导致草原冠层高度显著下降，这种下降与辐射减少、气候变暖、放牧及植物多样性变化有关。

<details open>
<summary>摘要翻译</summary>

> 草地冠层高度是决定植物多样性与群落结构的关键性状之一，直接影响草地生态系统中牲畜的资源利用效率。然而，由于物种聚集对种间和种内结构的复杂影响，大尺度草地冠层高度的变化鲜有报道。本研究将草地地上生物量解耦为垂直与水平分配，从而提供了一条反映草地冠层高度变化的途径。通过融合气候因子、卫星驱动指标及8年连续地面实测数据，采用机器学习算法估算草地地上生物量；草地地上生物量的水平分配则通过优化的线性光谱混合分析获得。研究发现，2001年至2022年间中国草地地上生物量的增加主要源于水平生物量分配的变化，这导致草地冠层高度显著下降。草地冠层高度的降低由辐射减少所驱动，更重要的是由气候变暖与放牧的共同作用所塑造，同时也与植物多样性的变化相关。冠层高度下降导致的草地群落矮化可能加剧牲畜干扰的影响，从而削弱草地生态系统对气候波动的抵抗力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Grassland canopy height is one of the most important traits for determining plant diversity and community structure, directly affecting the resource use efficiency of livestock in grassland ecosystems. However, broad-scale changes in grassland canopy height are seldom reported due to the complex effects of species aggregation on both interspecific and intraspecific structures. Here, we decouple grassland aboveground biomass into vertical and horizontal allocations, thereby offering a pathway to mirror changes in grassland canopy height. Grassland aboveground biomass is estimated using a machine learning algorithm by fusing climatic factors, satellite-driving metrics, and 8-year consecutive ground-truth surveys; the horizontal allocation of grassland aboveground biomass is derived from optimized linear spectral mixture analysis. We find that changes in horizontal biomass allocation primarily accounted for increases in Chinese grassland aboveground biomass from 2001 to 2022, resulting in a significant decline in grassland canopy height. The decline in grassland canopy height is shaped by reduced radiation and, more importantly, by the combined effects of warming and grazing, while also being related to variations in plant diversity. The dwarfing grassland community with declining canopy height may increase the impact of livestock disturbances, thus diminishing the resistance of grassland ecosystems to climate fluctuations.

</details>
<br>

**关键词**: grassland canopy height, aboveground biomass, machine learning, satellite data, climate factors, grazing, plant diversity, China grassland

---

### 69. ❌ Dual slab stagnation depths controlled by grain-size-induced sporadic low-viscosity zones at around 1000 km depth

**作者**: Jie Li, Keqing Li, Jie Li, Hongzhan Fei, Jiashun Hu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69987-9](https://doi.org/10.1038/s41467-026-69987-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究地球物理领域的地幔板块停滞机制，使用数值模型分析板块在660公里和1000公里深度的停滞现象，与医学图像分析、医学成像、深度学习医学成像等关键词完全无关。论文内容涉及地震层析成像、地幔对流、板块俯冲等地球科学主题，未涉及任何医学或图像分析技术。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过数值模型揭示了地幔中化石板块引起的颗粒尺寸变化如何产生局部低黏度区，从而控制板块在约660公里和1000公里深度的停滞机制。

<details open>
<summary>摘要翻译</summary>

> 地震层析成像揭示了广泛存在的停滞板块，主要分布于约660公里和约1000公里深度，然而对于这两个深度的成因仍缺乏统一解释。本研究采用自洽追踪粒度演化的数值模型，探讨控制板块停滞深度的因素。模型显示，古板块可诱发地幔下沉流穿越660公里不连续面，在此处相变诱发的粒度减小在660至1000公里深度之间形成了局部化的低黏度带。在俯冲带缓慢后退且存在低黏度带的条件下，板块可穿透660公里不连续面并停滞于约1000公里深度附近；反之，在俯冲带快速后退或缺乏低黏度带时，板块则停滞于约660公里深度附近或直接进入深部地幔。这些结果揭示了间歇性低黏度带可作为解释两种停滞深度的机制，并暗示中地幔黏度结构存在横向不均匀性，其成因可追溯至历史俯冲过程中下沉的古板块。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Seismic tomography reveals widespread stagnant slabs, mainly at depths of ~ 660 and ~ 1000 km, yet a unified explanation for both depths remains lacking. Here we use numerical models that self-consistently track grain-size evolution to investigate controls on slab stagnation depth. Our models show that fossil slabs can induce mantle downwelling that crosses the 660-km discontinuity, where phase-transition-induced grain-size reduction generates a localized low-viscosity zone (LVZ) between 660 and 1000 km depths. Under slow trench retreat and in the presence of an LVZ, slabs penetrate the 660 km discontinuity and stagnate near ~ 1000 km depth. Conversely, under fast trench retreat or without an LVZ, slabs stagnate near ~ 660 km depth or penetrate into the deep mantle. These results highlight sporadic LVZs as a mechanism for the two stagnation depths and imply laterally inhomogeneous mid-mantle viscosity structure driven by sinking fossil slabs from past subduction.

</details>
<br>

**关键词**: slab stagnation, mantle viscosity, grain-size evolution, 660-km discontinuity, low-viscosity zone, seismic tomography, numerical modeling, subduction

---

### 70. ❌ Topological Magneto-optical Kerr Effect without Spin-orbit Coupling in Spin-compensated Antiferromagnet

**作者**: Camron Farhang, Weihang Lu, Kai Du, Yunpeng Gao, Junjie Yang, Sang-Wook Cheong, Jing Xia
**期刊/来源**: nature_communications
**发布日期**: 2025-07-13
**arXiv链接**: [https://arxiv.org/abs/2507.09493](https://arxiv.org/abs/2507.09493)
**DOI**: [10.1038/s41467-026-70238-0](https://doi.org/10.1038/s41467-026-70238-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是凝聚态物理和磁光学领域，具体涉及磁光克尔效应（MOKE）、反铁磁体、自旋手性等物理机制，完全不涉及医学图像分析、医学成像或深度学习医学成像。论文内容属于基础物理研究，与医学应用无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文在非共面反铁磁体Co1/3TaS2中首次实验验证了无需自旋轨道耦合和净磁化的磁光克尔效应，并实现了标量自旋手性畴的成像和反转。

<details open>
<summary>摘要翻译</summary>

> 磁光克尔效应（Magneto-optical Kerr effect, MOKE）作为相反圆偏振光之间的差分反射现象，传统上被认为与相对论性自旋-轨道耦合（spin-orbit coupling, SOC）相关，后者将粒子的自旋与其轨道运动联系起来。在铁磁体中，磁化与自旋-轨道耦合的共同作用会产生显著的磁光克尔效应信号；而在某些共面反铁磁体中，尽管净磁化强度为零，但由自旋-轨道耦合诱导的贝里曲率仍可实现磁光克尔效应。理论上，在更广泛的自旋补偿磁性材料中，即使不依赖自旋-轨道耦合，也可能产生显著的磁光克尔效应——例如，在具有实空间标量自旋手性的体系中。然而其实验验证一直难以实现。本文中，我们在非共面反铁磁体Co1/3TaS2中展示了这种无需自旋-轨道耦合与净磁化的磁光克尔效应。利用萨格纳克干涉显微镜，我们实现了对标量自旋手性畴及其翻转的成像。我们的发现通过实验确立了一种产生强磁光克尔信号的新机制，并将补偿磁体中的手性自旋织构定位为超快、抗杂散光电子自旋应用的有力平台。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The magneto-optical Kerr effect (MOKE), the differential reflection of oppositely circularly polarized light, has traditionally been associated with relativistic spin-orbit coupling (SOC), which links a particle's spin with its orbital motion. In ferromagnets, large MOKE signals arise from the combination of magnetization and SOC, while in certain coplanar antiferromagnets, SOC-induced Berry curvature enables MOKE despite zero net magnetization. Theoretically, large MOKE can also arise in a broader class of magnetic materials with compensated spins, without relying on SOC - for example, in systems exhibiting real-space scalar spin chirality. The experimental verification has remained elusive. Here, we demonstrate such a SOC- and magnetization-free MOKE in the noncoplanar antiferromagnet Co1/3TaS2. Using a Sagnac interferometer microscope, we image domains of scalar spin chirality and their reversal. Our findings establish experimentally a new mechanism for generating large MOKE signals and position chiral spin textures in compensated magnets as a compelling platform for ultrafast, stray-field-immune opto-spintronic applications.

</details>
<br>

**关键词**: magneto-optical Kerr effect, antiferromagnet, spin chirality, Co1/3TaS2, Sagnac interferometer, opto-spintronics, compensated magnets

---

### 71. ❌ Topological magneto-optical Kerr effect without spin-orbit coupling in spin-compensated antiferromagnet

**作者**: Camron Farhang, Weihang Lu, Kai Du, Yunpeng Gao, Jie Yang, Sang-Wook Cheong, Jing Xia
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**arXiv链接**: [https://arxiv.org/abs/2507.09493](https://arxiv.org/abs/2507.09493)
**DOI**: [10.1038/s41467-026-70238-0](https://doi.org/10.1038/s41467-026-70238-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 该论文研究的是凝聚态物理和磁光学领域，具体探讨非共面反铁磁体中的拓扑磁光克尔效应，完全不涉及医学图像分析、医学成像或深度学习医学成像。论文内容聚焦于磁性材料的光学特性、自旋结构和实验验证，与医学图像处理没有任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文在非共面反铁磁体Co1/3TaS2中实验验证了无需自旋轨道耦合和净磁化的拓扑磁光克尔效应，并实现了标量自旋手性畴的成像和反转。

<details open>
<summary>摘要翻译</summary>

> 磁光克尔效应（Magneto-optical Kerr effect, MOKE）作为相反圆偏振光之间的差分反射现象，传统上被认为与相对论性自旋-轨道耦合（spin-orbit coupling, SOC）相关，后者将粒子的自旋与其轨道运动联系起来。在铁磁体中，磁化与自旋-轨道耦合的共同作用会产生显著的磁光克尔效应信号；而在某些共面反铁磁体中，尽管净磁化强度为零，但由自旋-轨道耦合诱导的贝里曲率仍可实现磁光克尔效应。理论上，在不依赖自旋-轨道耦合的情况下，一大类具有补偿自旋的磁性材料（例如展现实空间标量自旋手性的体系）也可能产生显著的磁光克尔效应，但其实验验证一直难以实现。本文中，我们在非共面反铁磁体Co<sub>1/3</sub>TaS<sub>2</sub>中展示了这种无需自旋-轨道耦合与净磁化的磁光克尔效应。利用萨格纳克干涉显微镜，我们实现了对标量自旋手性畴及其翻转的成像。我们的发现通过实验确立了一种产生强磁光克尔信号的新机制，并将补偿磁体中的手性自旋织构定位为超快、抗杂散光电子自旋应用的一个极具潜力的平台。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The magneto-optical Kerr effect (MOKE), the differential reflection of oppositely circularly polarized light, has traditionally been associated with relativistic spin-orbit coupling (SOC), which links a particle's spin with its orbital motion. In ferromagnets, large MOKE signals arise from the combination of magnetization and SOC, while in certain coplanar antiferromagnets, SOC-induced Berry curvature enables MOKE despite zero net magnetization. Theoretically, large MOKE can also arise in a broader class of magnetic materials with compensated spins, without relying on SOC - for example, in systems exhibiting real-space scalar spin chirality. The experimental verification has remained elusive. Here, we demonstrate such a SOC- and magnetization-free MOKE in the noncoplanar antiferromagnet Co<sub>1/3</sub>TaS<sub>2</sub>. Using a Sagnac interferometer microscope, we image domains of scalar spin chirality and their reversal. Our findings establish experimentally a new mechanism for generating large MOKE signals and position chiral spin textures in compensated magnets as a compelling platform for ultrafast, stray-field-immune opto-spintronic applications.

</details>
<br>

**关键词**: magneto-optical Kerr effect, antiferromagnet, spin chirality, Sagnac interferometer, Co1/3TaS2, opto-spintronics, compensated magnets

---

### 72. ❌ Chemodivergent Coupling of 1,3-Enynes with Anilines to Access Dihydropyrrole Skeleton under Palladium Catalysis

**作者**: Shuai Xu, Xueting Li, Zhi-Hui Wang, Ding‐Wei Ji, Qingyan Chen
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70201-z](https://doi.org/10.1038/s41467-026-70201-z)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确表明这是一篇有机化学领域的论文，研究钯催化下1,3-烯炔与苯胺的化学发散性偶联反应，用于构建二氢吡咯骨架。全文内容涉及催化反应、合成方法、机理研究，与医学图像分析、医学成像、深度学习医学成像等关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文开发了一种钯催化的化学发散性方法，通过调控反应条件，可以选择性地从1,3-烯炔和苯胺合成两种不同类型的官能化2,5-二氢吡咯骨架，产率高且选择性好。

<details open>
<summary>摘要翻译</summary>

> 2,5-二氢吡咯是多种天然产物和生物活性分子中普遍存在的结构单元。构建这类杂环的传统方法通常依赖于繁琐的多步流程或复杂的起始原料。本文报道了一种钯催化的化学发散性策略，利用易于获取的1,3-烯炔和苯胺衍生物合成功能化的2,5-二氢吡咯骨架。通过调控决定选择性的关键步骤的相对速率，可选择性实现双组分环化反应或三组分调聚反应，从而以优异收率和高选择性获得两种不同类型的功能化2,5-二氢吡咯。机理研究表明，该反应首先通过1,3-烯炔的1,4-氢胺化反应生成氨基甲基丙二烯中间体，随后发生分子内环化得到2-取代的2,5-二氢吡咯。该过程在Pd(II)催化剂存在下显著加速。然而，使用Pd(0)前体、强酸和过量配体可有效减缓该路径，将反应选择性导向与第二当量1,3-烯炔反应，从而生成调聚产物。本研究不仅为构建2,5-二氢吡咯核心结构提供了一种原子经济性方法，也为发展调聚化学提供了有价值的策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> 2,5-Dihydropyrroles are prevalent structural motifs in various natural products and biologically active molecules. Conventional methods for constructing these heterocycles often rely on elaborate multi-step procedures or complex starting materials. Herein, we describe a palladium-catalyzed chemodivergent protocol for synthesizing functionalized 2,5-dihydropyrrole scaffolds from readily accessible 1,3-enynes and anilines. By modulating the relative rates of the selectivity-determining steps, either two-component annulation or three-component telomerization can be selectively achieved, affording two distinct types of functionalized 2,5-dihydropyrroles in excellent yields and with high selectivities. Mechanistic studies reveal that the reaction initially proceeds through 1,4-hydroamination of 1,3-enynes to generate an aminomethyl allene intermediate, followed by an intramolecular annulation affording 2-substituted 2,5-dihydropyrroles. This process is significantly accelerated in the presence of Pd(II) catalysts. However, employing Pd(0) precursors, strong acids, and excess ligand effectively decelerates this pathway, diverting the selectivity towards reaction with a second equivalent of 1,3-enyne to yield the telomeric products. This study not only provides an atom-economical method for constructing the 2,5-dihydropyrrole core but also offers a valuable strategy for the development of telomerization chemistry.

</details>
<br>

**关键词**: palladium catalysis, chemodivergent coupling, 1,3-enynes, anilines, 2,5-dihydropyrrole, annulation, telomerization, mechanistic study

---

### 73. ❌ Universal work extraction in quantum thermodynamics

**作者**: Kaito Watanabe, Ryuji Takagi
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**arXiv链接**: [https://arxiv.org/abs/2504.12373](https://arxiv.org/abs/2504.12373)
**DOI**: [10.1038/s41467-026-69143-3](https://doi.org/10.1038/s41467-026-69143-3)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题为'Universal work extraction in quantum thermodynamics'，摘要讨论量子热力学中的功提取问题，涉及量子系统、自由能、量子通道等概念。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均与医学图像分析相关，而论文内容完全属于量子热力学领域，两者之间没有任何关联。因此所有关键词相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了量子热力学中未知输入态下的最优功提取问题，证明了无需知道量子态描述即可实现以自由能量化的最优功提取，并部分适用于无限维系统。

<details open>
<summary>摘要翻译</summary>

> 评估纳米尺度量子系统中可提取的最大功是量子热力学的核心问题之一。先前研究在关键假设下将输入态的自由能确定为可提取功的最优速率：实验者已知给定量子态的描述，这将其适用性限制在极为有限的情境中。本文证明，这一最优可提取功可在完全未知输入态的情况下实现，从而消除了前述基本操作限制。我们通过构建一个量子信道来实现这一目标，该信道的描述不依赖于输入态，却能提取以未知输入态自由能量化的功。值得注意的是，我们的结果部分涵盖了无限维系统的情况——即使在已知量子态描述的标准情境下，此类系统的最优可提取功也尚未明确。研究结果表明：尽管在协议开始时是否提供量子态描述通常会使信息任务完成的操作情境产生本质差异，但对输入态的无知并不影响渐近功提取的最优性能。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Evaluating the maximum amount of work extractable from a nanoscale quantum system is one of the central problems in quantum thermodynamics. Previous works identified the free energy of the input state as the optimal rate of extractable work under the crucial assumption: experimenters know the description of the given quantum state, which restricts the applicability to significantly limited settings. Here, we show that this optimal extractable work can be achieved without knowing the input states at all, removing the aforementioned fundamental operational restrictions. We achieve this by presenting the construction of a quantum channel whose description does not depend on input states but nevertheless extracts work quantified by the free energy of the unknown input state. Remarkably, our result partially encompasses the case of infinite-dimensional systems, for which optimal extractable work has not been known even for the standard state-aware setting. Our results clarify that, even though whether the description of the given state is provided at the beginning of the protocol generally makes the operational setting fundamentally different in accomplishing information-theoretic tasks, not knowing the input state does not influence the optimal performance of the asymptotic work extraction.

</details>
<br>

**关键词**: quantum thermodynamics, work extraction, free energy, quantum channel, unknown input state, asymptotic work extraction, quantum system

---

### 74. ❌ Proteomics-based machine learning model for predicting secondary infection in HBV-related liver failure

**作者**: Feixiang Xiong, Jianming Zheng, Jianzhong Chen, Linhuan Wu, Yuyong Jiang, Lu Ls, Tong Zhou, Yang Zhou, Tong Wu, Yamin Sun, Ronghua Jin, Yixin Hou
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69075-y](https://doi.org/10.1038/s41467-026-69075-y)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是基于血浆蛋白质组学预测乙型肝炎病毒相关肝衰竭患者继发感染风险的机器学习模型，研究内容涉及蛋白质组学、生物标志物发现、逻辑回归建模和临床验证。论文完全没有涉及医学图像分析或医学成像技术，也没有使用深度学习进行医学图像处理。所有关键词与论文主题完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A proteomics-derived model reliably identifies patients at high SI risk and supports early clinical intervention and predicts 28-day mortality better than Chronic Liver Failure-Consortium Acute-on-Chronic Liver Failure score (CLIF-C ACLF) and Model for End-Stage Liver Disease (MELD).

!!! tip deepseek-chat TL;DR

    该研究开发并验证了一个基于血浆蛋白质组学的机器学习模型，用于早期预测乙型肝炎病毒相关肝衰竭患者的继发感染风险，该模型在发现和验证队列中均表现出优异的区分能力。

<details open>
<summary>摘要翻译</summary>

> 乙型肝炎病毒相关肝衰竭患者继发感染风险极高，但早期预测工具仍显不足。本研究旨在开发并验证一种基于血浆蛋白质组学的早期继发感染风险评估模型。在一项前瞻性多中心研究中，114名患者纳入发现队列，两个验证队列各纳入60名患者。研究采用非靶向蛋白质组学技术识别继发感染相关蛋白，随后基于最小冗余最大相关特征选择法进行变量筛选，并建立逻辑回归模型。通过靶向蛋白质组学和酶联免疫吸附测定进行外部验证。研究发现炎症与凝血通路失调与继发感染密切相关。最终构建的模型包含溶菌酶（LYZ）、钙调蛋白1（CALM1）、丝氨酸蛋白酶抑制剂D家族成员1（SERPIND1）、皮肤桥蛋白（DPT）、总胆红素和谷草转氨酶，展现出优异的区分能力（发现队列受试者工作特征曲线下面积（AUROC）为0.980；验证队列为0.873），其性能优于C反应蛋白（CRP）、白细胞计数（WBC）和中性粒细胞百分比（NE%）。该模型对28天死亡率的预测能力也优于慢性肝衰竭联盟-慢加急性肝衰竭评分（CLIF-C ACLF）和终末期肝病模型（MELD）。在验证队列2中，酶联免疫吸附测定结果呈现一致趋势，基于此建立的模型AUROC达到0.883。该蛋白质组学模型能可靠识别继发感染高危患者，为早期临床干预提供支持。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Patients with Hepatitis B Virus-related liver failure are highly vulnerable to secondary infections (SI), yet early predictive tools remain limited. In this work, we aim to develop and validate a plasma proteomics-based model for early SI risk assessment. In a prospective multicenter study, 114 patients are enrolled in the discovery cohort, 60 each in two validation cohorts. Untargeted proteomics is used to identify SI-related proteins, followed by Minimum Redundancy Maximum Relevance based feature selection and logistic regression modeling. Targeted proteomics and ELISA are applied for external validation. Inflammatory and coagulation pathway dysregulation is strongly associated with SI. A final model including Lysozyme (LYZ), Calmodulin 1 (CALM1), Serpin Family D Member 1 (SERPIND1), Dermatopontin (DPT), total bilirubin, and AST show excellent discrimination (area under the receiver operating characteristic curve (AUROC) 0.980 in discovery; 0.873 in validation), outperforming C-reactive protein (CRP), white blood cell (WBC), and Neutrophil percentage (NE%). It also predicts 28-day mortality better than Chronic Liver Failure-Consortium Acute-on-Chronic Liver Failure score (CLIF-C ACLF) and Model for End-Stage Liver Disease (MELD). ELISA measurements in validation cohort 2 yield consistent trends, and an ELISA-based model achieve an AUROC of 0.883. This proteomics-derived model reliably identifies patients at high SI risk and supports early clinical intervention.

</details>
<br>

**关键词**: proteomics, machine learning, secondary infection, HBV-related liver failure, risk prediction, biomarkers, logistic regression, clinical validation

---

### 75. ❌ Nucleotide-resolution mapping of regulatory elements via allelic readout of tiled base editing

**作者**: Basheer Becerra, Sandra Wittibschlager, Zain M. Patel, Ana P. Kutschat, Justin Delano, Eric Che, Anzhelika Tauber, Ting Wu, M M Starrs, Christina S. Horstmann, Sophie Müller, Madelynn N. Whittaker, Elise Sylvander, Manfred Lehner, Michael I. Love, Benjamin P. Kleinstiver, Martin Jankowiak, Daniel E. Bauer, Davide Seruggia, Luca Pinello
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69918-8](https://doi.org/10.1038/s41467-026-69918-8)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是CRISPR碱基编辑技术在基因调控元件鉴定中的应用，具体针对CD19增强子与CAR-T细胞治疗的关系。全文未涉及医学影像分析、医学成像或深度学习医学成像的任何内容，研究领域属于基因组学、基因编辑和癌症免疫治疗，与给定的医学影像关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An end-to-end experimental assay and computational pipeline is introduced, which leverages targeted sequencing of CRISPR-introduced alleles at the endogenous target locus following dense base-editing mutagenesis following dense base-editing mutagenesis to achieve nucleotide-resolution genotype-phenotype mapping at regulatory elements beyond conventional gRNA-based screens.

!!! tip deepseek-chat TL;DR

    该研究开发了一种基于CRISPR碱基编辑的高分辨率方法，用于鉴定调控CD19表达的核苷酸位点，并发现MYB和PAX5结合位点的突变会导致CD19 CAR-T细胞治疗耐药。

<details open>
<summary>摘要翻译</summary>

> CRISPR平铺筛选技术虽能表征调控序列，但其分辨率受限于通过向导RNA测序和富集分析间接读取编辑信号的固有缺陷。本研究开发了一种端到端的实验检测方法与计算流程，其核心在于对密集碱基编辑诱变后内源靶位点的CRISPR引入等位基因进行靶向测序。作为概念验证，我们以白血病免疫治疗靶点CD19的假定增强子为研究对象，鉴定了对CD19调控至关重要的等位基因及单核苷酸位点。我们的可视化工具揭示了与最高评分核苷酸相对应的转录因子结合基序。验证实验证实，MYB、PAX5和EBF1结合位点的突变会降低CD19表达。关键的是，编辑MYB与PAX5基序可赋予细胞对CD19 CAR-T细胞疗法的抵抗能力，这揭示了非编码区变异如何驱动免疫治疗逃逸。综上所述，该方法在调控元件上实现了超越传统基于gRNA筛选的核苷酸分辨率基因型-表型映射。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> CRISPR tiling screens have enabled the characterization of regulatory sequences but are limited by low resolution arising from the indirect readout of editing via guide RNA sequencing and enrichment analysis. This study introduces an end-to-end experimental assay and computational pipeline, which leverages targeted sequencing of CRISPR-introduced alleles at the endogenous target locus following dense base-editing mutagenesis. As a proof of concept, we studied a putative CD19 enhancer, an immunotherapy target in leukemia, and identified alleles and single nucleotides crucial for CD19 regulation. Our visualization tools revealed transcription factor motifs corresponding to the top-ranked nucleotides. Validation experiments confirmed that mutations in MYB, PAX5, and EBF1 binding sites reduce CD19 expression. Critically, editing MYB and PAX5 motifs conferred resistance to CD19 CAR-T cell therapy, revealing how non-coding variants can drive immunotherapy escape. Taken together, this approach achieves nucleotide-resolution genotype-phenotype mapping at regulatory elements beyond conventional gRNA-based screens.

</details>
<br>

**关键词**: CRISPR base editing, regulatory elements, nucleotide-resolution mapping, CD19 enhancer, CAR-T cell therapy, immunotherapy escape, genotype-phenotype mapping, allelic readout

---

### 76. ❌ Global economic exposure to climate change amplified by spatially compounding climate extremes

**作者**: Bianca Biess, Lukas Gudmundsson, Sonia I. Seneviratne
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70127-6](https://doi.org/10.1038/s41467-026-70127-6)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是气候变化极端事件对全球经济暴露度的影响，使用地球系统模型和耦合模型比对项目数据进行分析。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，这些关键词与论文主题无任何关联。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究分析了空间复合气候极端事件如何通过跨区域依赖性放大全球经济暴露度，发现经济较不发达地区更可能同时面临极端事件，从而加剧其经济稳定性威胁。

<details open>
<summary>摘要翻译</summary>

> 尽管越来越多的证据表明，气候极端事件能显著影响地方经济，但极端气候事件跨区域及全球尺度依赖性的影响仍未得到充分理解。我们揭示了空间复合型高温、湿润及干旱极端事件的预计增长与全球经济暴露度放大之间的关键联系。基于第六次耦合模式比较计划中的地球系统模式预测，我们分析了全球尺度及跨区域依赖性如何加剧经济暴露度的区域差异。研究结果表明，当前经济财富水平较低的地区更可能与其他区域同时面临极端事件，从而放大其经济稳定性面临的潜在威胁。本研究强调，有必要超越局部尺度来审视气候极端事件的经济暴露度，并着重指出需要评估跨区域暴露风险，理解局部暴露与全球经济动态之间的关联。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Despite growing evidence that climate extreme events can significantly affect local economies, the implications of cross-regional and planetary-scale dependencies in climate extremes remain inadequately understood. We demonstrate a crucial link between the projected increase in spatially compounding hot, wet, and dry extremes and the amplification of global economic exposure. Based on Earth System Model projections from the 6th phase of the Coupled Model Intercomparison Project, we analyze how planetary-scale and cross-regional dependencies can exacerbate regional disparities in economic exposure. Our findings reveal that regions with lower present-day economic wealth are more likely to face extreme events simultaneously with other areas, amplifying the potential threats to their economic stability. This study highlights the necessity of considering economic exposure to climate extremes beyond local scales, emphasizing the need for assessing cross-regional exposures and understanding the connections between localized exposures and global economic dynamics.

</details>
<br>

**关键词**: climate extremes, economic exposure, spatially compounding, global economy, regional disparities, Earth System Model, CMIP6, cross-regional dependencies

---

### 77. ❌ In-situ formatting benzisoxazole-linked covalent organic framework for enhanced photocatalytic hydrogen peroxide generation

**作者**: Pu Zhang, Haihua Zeng, Qiang Zhang, Peifang Wang, Huinan Che, Chunmei Tang, Jianzhi Xu, Jinlin Long, Bin Liu, YANHUI AO
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70161-4](https://doi.org/10.1038/s41467-026-70161-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是共价有机框架材料在光催化过氧化氢合成中的应用，属于材料化学和光催化领域。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均涉及医学影像分析，与论文的研究主题完全无关。论文中未提及任何医学影像、图像分析或深度学习在医学影像中的应用内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文提出了一种光诱导结构转化策略，用于构建苯并异恶唑连接的共价有机框架，实现了在纯水中1986.9 μmol·g⁻¹·h⁻¹的高过氧化氢产率。

<details open>
<summary>摘要翻译</summary>

> 唑基连接的共价有机框架在过氧化氢的光催化合成领域备受关注，但其合成路线复杂且成本高昂的问题仍待解决。本文提出一种光诱导结构转化策略，用于简便构建唑基连接的共价有机框架。我们发现亚胺键在光照射下可原位形成苯并异噁唑键。正如预期，演化生成的部分苯并异噁唑连接的共价有机框架在纯水中实现了1986.9 μmol·g<sup>-1</sup>·h<sup>-1</sup>的高过氧化氢产率。理论计算与光谱表征表明，由于给体-受体结构的形成，载流子分离与传输效率得到显著提升。此外，原位生成的苯并异噁唑单元同时作为电子受体和催化中心，促进了双氧还原为超氧自由基，进而转化为过氧化氢，最终提高了产率。本研究展示了一种开创性的策略，用于构建在过氧化氢光合成方面具有高性能的苯并异噁唑连接共价有机框架。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Azole-linked covalent organic frameworks have drawn a lot of attention in photocatalytic synthesis of hydrogen peroxide, yet remain challenged by complex and costly synthetic routes. Here, we present a light-induced structural transformation strategy to facilely construct azole-linked covalent organic frameworks. We find that benzisoxazole linkages can be in-situ formed from imine linkages under light irradiation. As expected, the evolved partially benzisoxazole-linked covalent organic framework achieves a high hydrogen peroxide yield rate of 1986.9 μmol·g<sup>-1</sup>·h<sup>-1</sup> in pure water. Theoretical calculations and spectral characterizations reveal significantly enhanced charge carrier separation and transfer efficiency, due to the formation of donor-acceptor structure. Furthermore, the in-situ formed benzisoxazole unit acts as both electron acceptor and catalytic center, promoting the reduction of dioxygen to superoxide radical, which is then converted into hydrogen peroxide, ultimately enhancing the yield. This work demonstrates a pioneering strategy for constructing benzisoxazole-linked covalent organic frameworks with high performance on hydrogen peroxide photo-synthesis.

</details>
<br>

**关键词**: covalent organic framework, photocatalytic hydrogen peroxide generation, benzisoxazole linkage, light-induced structural transformation, donor-acceptor structure, charge carrier separation, in-situ formation, photocatalysis

---

### 78. ❌ Machine learning helps to strongly reduce future warming uncertainty

**作者**: Chang Li, Jingchun Wu, Zheng Wang, Francis W. Zwiers, Xuebin Zhang, Xi Chen
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70205-9](https://doi.org/10.1038/s41467-026-70205-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是气候变化预测，使用机器学习分析历史温度数据来约束未来全球变暖的不确定性，完全不涉及医学图像分析、医学成像或深度学习在医学成像中的应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This study uses machine learning to uncover spatially resolved emergent constraint relationships between 1971-2020 warming trends at individual grid cells and future global mean warming in a large collection of climate model simulations, which identifies key tropical and polar regions where historical warming most effectively constrains future outcomes.

!!! tip deepseek-chat TL;DR

    该研究使用机器学习从历史温度的空间模式中提取物理可解释的涌现约束关系，显著降低了未来全球变暖预测的不确定性，提高了巴黎协定阈值被提前突破的可能性。

<details open>
<summary>摘要翻译</summary>

> 观测到的全球平均地表温度升温现象已被用于降低未来气候变化及其影响预估的不确定性，但升温空间格局中所蕴含的信息在很大程度上尚未得到有效利用。本研究采用机器学习方法，在大量气候模式模拟数据中，揭示了1971-2020年间各网格单元升温趋势与未来全球平均升温之间的空间解析型涌现约束关系。该方法识别出具有明确物理解释的关键热带和极地区域，这些区域的历史升温趋势能最有效地约束未来气候结果。纳入观测到的空间格局信息后，未来全球变暖预估的误差方差降低了约70%，而仅基于全球平均趋势的常用约束方法仅能降低约48%的不确定性。这些精细化预估意味着《巴黎协定》温控阈值被提前突破的可能性更高。例如，在SSP3-7.0情景下，到本世纪中叶升温超过2°C的可能性约为80%，而仅使用观测的全球平均趋势进行约束时该概率约为70%。我们的研究凸显了机器学习在发掘具有物理解释性的涌现约束关系方面的潜力，这些约束关系能够显著改进未来气候预估。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The observed warming of global mean surface temperature has been used to reduce uncertainty in future climate change and impact projections, but the information embedded in the spatial pattern of warming remains largely untapped. Here, we use machine learning to uncover spatially resolved emergent constraint relationships between 1971-2020 warming trends at individual grid cells and future global mean warming in a large collection of climate model simulations. This approach identifies key tropical and polar regions, with clear physical interpretations, where historical warming most effectively constrains future outcomes. Including the observed pattern information reduces the error variance in future global warming projections by about 70%, while commonly used constraints based solely on the global mean trend reduce that uncertainty by about 48%. These refined projections imply a higher likelihood of early exceedance of Paris Agreement thresholds. For example, the likelihood of exceeding 2 °C by mid-century under the SSP3-7.0 scenario is approximately 80%, compared to 70% when constrained by observed global mean trend alone. Our study highlights the potential of machine learning to uncover physically interpretable emergent constraints that improve future climate projections.

</details>
<br>

**关键词**: machine learning, climate change, global warming, emergent constraints, future projections, Paris Agreement, uncertainty reduction, spatial pattern

---

### 79. ❌ Tubulin transforms Tau and α-synuclein condensates from pathological to physiological

**作者**: Lathan Lucas, Phoebe S. Tsoi, My Diem Quan, Kyoung-Jae Choi, Josephine C. Ferreon, Allan Chris M. Ferreon
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69618-3](https://doi.org/10.1038/s41467-026-69618-3)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究Tau和α-synuclein蛋白质相分离、微管蛋白调控以及神经退行性疾病机制，属于分子生物学和神经科学领域。全文未涉及医学影像分析、医学成像或深度学习医学成像技术，与所有评分关键词完全无关。

</details>
<br>

!!! info Semantic Scholar TL;DR

    It is shown that Tubulin modulates Tau:αSyn condensates by promoting microtubule interactions and inhibiting homotypic and heterotypic pathological oligomers, and in the absence of Tubulin, Tau-driven condensation accelerates formation of pathogenic Tau:αSyn heterodimers and amyloid fibrils.

!!! tip deepseek-chat TL;DR

    该研究发现微管蛋白通过调节Tau和α-synuclein的相分离过程，抑制病理性寡聚体形成并促进微管稳定，揭示了神经退行性疾病中蛋白质聚集的调控机制。

<details open>
<summary>摘要翻译</summary>

> 蛋白质通过相分离形成无膜凝聚体，从而在空间上调控生物分子相互作用。这些凝聚体既可支持细胞生理功能，也可能引发病理性蛋白质聚集。Tau蛋白与α-突触核蛋白（αSyn）是两种神经元蛋白，它们可形成异型Tau:αSyn凝聚体，该过程与生理及病理进程相关。Tau与αSyn既能调控微管功能，也会错误折叠并共同沉积于神经退行性疾病相关的聚集体中，这凸显了Tau:αSyn凝聚现象在健康与疾病中的双重作用。本研究表明，微管蛋白（Tubulin）通过促进微管相互作用并抑制同型及异型病理性寡聚体的形成，从而调控Tau:αSyn凝聚体。在缺乏微管蛋白的情况下，Tau驱动的相分离会加速致病性Tau:αSyn异源二聚体及淀粉样纤维的形成。微管蛋白进入凝聚体后可促进微管聚合，并阻止Tau与αSyn的寡聚化。我们进一步揭示了在缺乏微管蛋白的病理性凝聚体与富含微管蛋白的生理性凝聚体中，Tau和αSyn分别处于不同的结构状态。在神经元模型中，微管缺失会驱动病理性寡聚体形成及神经突损毁，而可诱导的Tau凝聚则能稳定微管结构。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Proteins undergo phase separation to form membraneless condensates that spatially organize biomolecular interactions. These condensates can support cellular physiology or instigate pathological protein aggregation. Tau and α-synuclein (αSyn) are neuronal proteins that form heterotypic Tau:αSyn condensates associated with physiological and pathological processes. Tau and αSyn regulate microtubules, but also misfold and co-deposit in aggregates linked to neurodegenerative disease, highlighting the ambivalent impact of Tau:αSyn condensation in health and disease. Here, we show that Tubulin modulates Tau:αSyn condensates by promoting microtubule interactions and inhibiting homotypic and heterotypic pathological oligomers. In the absence of Tubulin, Tau-driven condensation accelerates formation of pathogenic Tau:αSyn heterodimers and amyloid fibrils. Tubulin partitioning into condensates promotes microtubule polymerization and prevents Tau and αSyn oligomerization. We identify distinct Tau and αSyn structural states in pathological Tubulin-absent versus physiological Tubulin-rich condensates. In neuronal models, microtubule loss drives pathological oligomer formation and neurite loss, whereas inducible Tau condensation stabilizes microtubules.

</details>
<br>

**关键词**: Tau, α-synuclein, phase separation, microtubules, neurodegenerative disease, protein aggregation, condensates, oligomerization

---

### 80. ❌ Lasing-like dynamics with virtual gain driven by complex-frequency excitations

**作者**: Boyi Xue, Ruixiang Zhang, Yicheng Zhu, Ruixin Ma, Xi Chen, Andrea Alù, Wenjie Wan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70123-w](https://doi.org/10.1038/s41467-026-70123-w)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是光学微腔中的非厄米光-物质相互作用，使用复频率激发实现虚拟增益和激光样动力学，属于光学物理和光子学领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，没有医学图像数据、医学成像技术或深度学习在医学中的应用。所有关键词与论文主题完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了在被动光学微腔中使用复频率激发实现虚拟增益，从而产生激光样动力学和完美吸收共存的现象，无需主动介质或粒子数反转。

<details open>
<summary>摘要翻译</summary>

> 复频激发通过时域信号整形规避了材料固有增益或损耗的限制，从而实现对非厄米光-物质相互作用的调控。尽管虚拟损耗已实现了相干完美吸收，但其时间反演对应物——虚拟增益——在光学系统中仍较少被探索。本文通过理论与实验，利用复频激发在无源回音壁模式微腔中展示了类激光动力学行为。虚拟增益抵消了本征的材料损耗与辐射损耗，产生了超过单位值的瞬时透射率，并最终饱和于一个准稳态值。超越一个类似临界阈值的拐点后，系统进入响应发散、指数增长的区间，模拟了真实激光器的瞬态建立过程，而无需粒子数反转或主动增益介质。这一线性效应使得类激光行为与完美吸收能够稳定共存，且二者之间的转换可通过虚拟增益的调谐进行控制。这些研究成果为在无源平台上操控非厄米相互作用建立了一个通用框架，为传感、光通信及能量存储等应用领域提供了显著潜力。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Complex-frequency excitation controls non-Hermitian light-matter interactions by temporally shaping signals to bypass inherent material gain or loss constraints. While virtual loss has enabled coherent perfect absorption, its time-reversed counterpart: virtual gain, remains less explored in optical systems. Here, we theoretically and experimentally demonstrate lasing-like dynamics in a passive whispering-gallery-mode microcavity using complex-frequency excitations. Virtual gain counteracts intrinsic material and radiation losses, producing an instantaneous transmittance that exceeds unity and saturates at a quasi-steady value. Beyond a critical threshold-like point, the system enters a regime of divergent, exponentially growing response, mimicking the transient buildup of a real laser without requiring population inversion or active media. This linear effect allows for the robust coexistence of lasing-like behavior and perfect absorption, with transitions controlled by virtual gain tuning. These results establish a versatile framework for manipulating non-Hermitian interactions in passive platforms, offering remarkable potential for applications in sensing, optical communications, and energy storage.

</details>
<br>

**关键词**: complex-frequency excitations, virtual gain, non-Hermitian light-matter interactions, whispering-gallery-mode microcavity, lasing-like dynamics, perfect absorption, passive optical systems, optical communications

---

### 81. ❌ Non-chelation control in allylations of α-oxy ketones using group-14 allylatranes

**作者**: Yuya Tsutsui, Kokoro Shiga, Akihito Konishi, Makoto Yasuda
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69732-2](https://doi.org/10.1038/s41467-026-69732-2)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要明确表明这是一篇有机化学领域的研究论文，专注于α-氧代酮的非螯合控制烯丙基化反应，涉及立体选择性、烯丙基三烷、有机合成方法学等。全文未提及任何医学图像分析、医学成像或深度学习医学成像相关内容，与给定的三个关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了α-氧代酮通过非螯合途径进行反式选择性烯丙基化的难题，利用具有高配位第14族元素中心的烯丙基三烷实现了高产率和高非对映选择性的反式选择性烯丙基化反应。

<details open>
<summary>摘要翻译</summary>

> 对α-取代羰基化合物的立体选择性亲核加成是有机化学当代研究的关键领域。在羰基化合物加成反应的π-面选择性研究中，（极性）Felkin-Anh模型和螯合模型已被广泛认可为能够准确解释烯丙基产物选择性的理论框架。对于α-氧代羰基类化合物——这类在天然产物合成中应用广泛且作为有机合成中高效构建模块的底物——其立体选择性反应通常遵循螯合模型，倾向于发生顺式选择性加成。与已充分建立的α-氧代羰基化合物顺式选择性加成相比，通过非螯合途径实现的反式选择性加成仍鲜有探索。本研究报道了利用具有高配位第14族元素中心的烯丙基杂环三醇（allylatranes）实现α-氧代酮的反式选择性烯丙基化反应。这些杂环三醇因其跨环相互作用和刚性骨架，表现出高亲核性和低螯合能力，从而促进了反式选择性烯丙基化的进行。我们采用实验与理论相结合的方法，揭示了这类杂环三醇独特的电子性质。该方法适用于多种底物，与传统方法相比，能以高产率和优异的非对映选择性合成带有高烯丙基结构单元的反式-1,2-二醇。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Stereoselective nucleophilic additions to α-substituted carbonyl compounds are a crucial area of contemporary research in organic chemistry. Of the various advancements in π-facial selectivity in addition reactions of carbonyl compounds, the (polar) Felkin-Anh model and the chelation model are well recognized for accurately explaining the selectivity of the allylic products. For reactions that involve α-oxy carbonyl groups - known for their broad applications in natural-product synthesis and as effective building blocks in organic synthesis - the stereoselective reaction typically follows the chelation model, favoring syn-selective addition. In contrast to the well-established syn-selective additions of α-oxy carbonyls, anti-selective additions through a non-chelation pathway remain largely unexplored. In this study, we present the anti-selective allylation of α-oxy ketones using allylatranes that feature a highly coordinated group-14-element center. These atranes demonstrate high nucleophilicity and low chelating ability due to their transannular interactions and rigid framework, facilitating anti-selective allylations. A combined experimental and theoretical approach has been used to highlight the unique electronic properties of these atranes. This method is applicable to a wide variety of substrates, producing anti-1,2-diols with a homoallylic moiety in high yield and excellent diastereoselectivity compared to traditional methods.

</details>
<br>

**关键词**: stereoselective allylation, α-oxy ketones, non-chelation pathway, anti-selective addition, allylatranes, group-14 elements, diastereoselectivity, organic synthesis

---

### 82. ❌ An interfacial-intramolecular electron highway for accelerated electrocatalytic CO2 reduction by an O2-tolerant formate dehydrogenase

**作者**: Weisong Liu, Peng Zhang, Xiufeng Wang, Kuncheng Zhang, Wenhua Yang, Huijuan Cui, Jianxing Liu, Junsong Sun, Chun You, Haiyang Cui, Zhiguang Zhu, Lingling Zhang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69827-w](https://doi.org/10.1038/s41467-026-69827-w)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是生物电催化CO2还原，涉及酶工程、电化学和结构生物学（Cryo-EM分析），与医学图像分析、医学成像或深度学习医学成像完全无关。所有关键词得分为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The merits of oxygen tolerance and efficient (electro)catalytic property endow SoFdhAB a robust enzyme adopted in potential application scenarios, and the inherent DET capability may inspire the interfacial engineering of other oxidoreductases.

!!! tip deepseek-chat TL;DR

    该研究解决了生物电催化CO2还原中电子转移效率低和氧敏感性的问题，通过挖掘一种耐氧的甲酸脱氢酶并解析其结构机制，构建了高效的直接生物电催化CO2还原系统。

<details open>
<summary>摘要翻译</summary>

> 生物电催化CO<sub>2</sub>还原为CO<sub>2</sub>生物转化提供了一条可持续路径，但其发展仍受限于界面-分子内电子转移及氧敏感性。本研究从希瓦氏菌Shewanella oneidensis MR-1中挖掘出一种甲酸脱氢酶（SoFdhAB），该酶具备完全耐氧特性及直接电子转移（Direct-Electron-Transfer, DET）电催化性能。冷冻电镜（Cryo-EM）分析揭示其分子内存在一条由五个[4Fe-4S]簇构成的电子高速通道、一个促进界面电子转移的区域性面对面接触结构，以及一种区别于“失活-再激活”模式的独特耐氧机制。通过获得有益突变体SoFdhAB-Y94S，构建了直接生物电催化CO<sub>2</sub>还原系统，在64小时内累积生成2.88 ± 0.03 mmol甲酸盐，稳态速率为45.3 ± 0.5 μmol h<sup>-1</sup> cm<sup>-2</sup>，法拉第效率达93.1 ± 5.2%。其耐氧特性与高效（电）催化性能使SoFdhAB成为一种可应用于潜在场景的稳健酶，而其固有的直接电子转移能力可为其他氧化还原酶的界面工程设计提供启示。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Bioelectrocatalytic CO<sub>2</sub> reduction offers a sustainable route for CO<sub>2</sub> bioconversion, yet remains limited by interfacial-intramolecular electron transfer and oxygen sensitivity. Here, we mine a formate dehydrogenase from Shewanella oneidensis MR-1 (SoFdhAB) featuring completely oxygen tolerant and direct-electron-transfer (DET) electrocatalytic performances. Cryo-electron microscopy (Cryo-EM) analysis reveals an intramolecular electron highway comprising five [4Fe-4S] clusters, a regional face-face contact facilitating interfacial ET, and a unique oxygen resistance mechanism different from inactivation-activation. By acquiring a beneficial variant SoFdhAB-Y94S, a direct bioelectrocatalytic CO<sub>2</sub> reduction system is constructed, accumulating 2.88 ± 0.03 mmol formate in 64 hours with a steady rate of 45.3 ± 0.5 μmol h<sup>-1</sup> cm<sup>-2</sup> and a Faradaic efficiency of 93.1 ± 5.2%. The merits of oxygen tolerance and efficient (electro)catalytic property endow SoFdhAB a robust enzyme adopted in potential application scenarios, and the inherent DET capability may inspire the interfacial engineering of other oxidoreductases.

</details>
<br>

**关键词**: CO2 reduction, formate dehydrogenase, oxygen tolerance, direct electron transfer, Cryo-EM analysis, bioelectrocatalysis, electron highway, Faradaic efficiency

---

### 83. ❌ Subcellular proteomics reveals a blueprint for endosymbiont integration in trypanosomatid Angomonas deanei

**作者**: Michael Hammond, Ľubomíra Chmelová, Natascha A. van Geelen-Kuenzel, Anay K. Maurya, Éden Ramalho de Araujo [UNIFESP] Ferreira, Vanesa Puente, Lawrence Rudy Cadena, Kristína Záhonová, Adam Dowle, Jeremy C. Mottram, Eva C M Nowack, Julius Lukeš, Vyacheslav Yurchenko
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70084-0](https://doi.org/10.1038/s41467-026-70084-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题为《Subcellular proteomics reveals a blueprint for endosymbiont integration in trypanosomatid Angomonas deanei》，摘要描述了通过亚细胞蛋白质组学分析研究锥虫Angomonas deanei与其内共生细菌的整合机制，包括蛋白质定位、代谢相互作用等。研究内容属于分子生物学、细胞生物学和共生进化领域，涉及蛋白质组学、显微镜验证和遗传操作，但未涉及医学图像分析、医学成像或深度学习医学成像。这些关键词与医学诊断、临床影像或相关AI应用无关，因此所有关键词的相关度均为0。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An in-depth subcellular proteomic analysis was performed to determine the compartmental localisation of both host and endosymbiont proteins, and confirmed an energetic basis for the previously observed association between the host's glycosomes and its endosymbiont and the host's acidocalcisomes.

!!! tip deepseek-chat TL;DR

    该研究通过亚细胞蛋白质组学分析揭示了锥虫Angomonas deanei与其内共生细菌的整合机制，包括发现新的宿主靶向蛋白和代谢相互作用。

<details open>
<summary>摘要翻译</summary>

> 内共生体的获取是驱动真核生物进化的基本过程。生命之树中充满了原核生物被内化并与宿主整合的案例，这些关系通常形成互利共生。锥虫类Angomonas deanei便是其中一例，其体内含有单个β-变形菌门内共生体。这种共生关系高度进化，其证据包括已鉴定出由宿主编码、可靶向细菌并控制其分裂的蛋白质。为深入理解这种整合机制，我们进行了深入的亚细胞蛋白质组学分析，以确定宿主与内共生体蛋白质的区室定位。我们的分析解析了超过5,000种宿主蛋白质和400多种内共生体蛋白质。利用这一丰富数据集，我们鉴定出数种新型的宿主编码、可靶向细菌的蛋白质，并通过遗传操作和显微技术验证了预测结果。通过定位酶系统的空间分布，我们得以阐明两种生物之间的代谢互作。我们证实了先前观察到的宿主糖酵解体（glycosomes）与其内共生体之间存在能量基础的关联，并发现了内共生体与宿主酸钙体（acidocalcisomes）之间的相互作用。这一亚细胞蛋白质组学数据集为未来研究细菌整合这一非凡过程提供了全面的基础。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The acquisition of endosymbionts is a fundamental process that has driven the evolution of eukaryotes. The tree of life is filled with cases of internalised prokaryotes that have become integrated into their hosts, often forming mutually beneficial relationships. The trypanosomatid Angomonas deanei is one such case, harbouring a single β-proteobacterial endosymbiont. This symbiotic relationship is highly advanced, as evidenced by the identification of host-encoded proteins that are targeted to the bacterium and control its division. To deeper understand this integration, we performed an in-depth subcellular proteomic analysis to determine the compartmental localisation of both host and endosymbiont proteins. Our analysis resolved over 5,000 host proteins and over 400 endosymbiont proteins. We used this rich dataset to identify several novel host-encoded proteins targeted to the bacterium, and validated our predictions using genetic manipulations and microscopy. By mapping the localised enzymatic repertoire, we were able to shed light on metabolic interplay between the two organisms. We confirmed an energetic basis for the previously observed association between the host's glycosomes and its endosymbiont, and discovered an interaction between the endosymbiont and the host's acidocalcisomes. This subcellular proteomic dataset provides a comprehensive foundation for future research into the remarkable process of bacterial integration.

</details>
<br>

**关键词**: subcellular proteomics, endosymbiont integration, trypanosomatid Angomonas deanei, host-encoded proteins, metabolic interplay, protein localization, symbiotic relationship, bacterial integration

---

### 84. ❌ Cross-species gene redesign leveraging ortholog information and generative modeling

**作者**: Manato Akiyama, Motohiko Tashiro, Ying Huang, Mika Uehara, Taiki Kanzaki, Mitsuhiro Itaya, Masakazu Kataoka, K. Miyamoto, Yasubumi Sakakibara
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69966-0](https://doi.org/10.1038/s41467-026-69966-0)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究专注于基因工程和计算生物学领域，具体涉及跨物种基因重新设计、直系同源信息和生成模型的应用。论文内容完全不涉及医学图像分析、医学成像或深度学习在医学成像中的应用，因此所有关键词的相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    OrthologTransformer is presented, a Transformer-based deep learning model that converts orthologous genes between species by learning from large-scale orthologous gene datasets and recapitulates evolutionary differences to predict coding sequences optimized for target species while preserving protein function.

!!! tip deepseek-chat TL;DR

    该研究利用直系同源信息和生成模型开发了一种跨物种基因重新设计的方法，成功实现了基因功能的优化和跨物种适应性。

**关键词**: cross-species gene redesign, ortholog information, generative modeling, gene engineering, computational biology, functional optimization, species adaptation

---

### 85. ❌ Femtosecond laser synthesis of multiscale high-entropy alloys/graphene composites for high-performance Joule heating

**作者**: Lingxiao Wang, Kai Yin, Jianqiang Xiao, Xinghao Song, Jiaqing Pei, Jun He, Ji-an Duan
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70162-3](https://doi.org/10.1038/s41467-026-70162-3)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是飞秒激光合成高熵合金/石墨烯复合材料用于高性能焦耳加热应用，属于材料科学、纳米技术和能源领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，没有提到任何医学图像、诊断、成像技术或相关应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究通过飞秒激光合成高熵合金纳米颗粒/激光诱导石墨烯复合材料，实现了高性能焦耳加热应用，其电热转换效率高达~285.4°C cm² W⁻¹，红外发射率~0.98，比传统电加热器节能约49.1%。

<details open>
<summary>摘要翻译</summary>

> 高熵合金纳米颗粒（HEA-NPs）在多个领域引起了广泛关注。然而，迄今为止，其应用研究主要集中于电催化领域。将HEA-NPs的应用拓展至当前领域之外既及时又必要，但仍面临挑战。本文展示了在激光诱导石墨烯（LIG）上成功飞秒激光合成HEA-NPs，以实现高性能焦耳加热应用。所制备的复合材料（HEAs/LIG）表现出卓越的电热转换能力，效率高达约285.4 °C cm<sup>2</sup> W<sup>-1</sup>。此外，HEAs/LIG在2.5至20 μm波长范围内还展现出约0.98的高宽带红外发射率。最后，我们展示了HEAs/LIG作为高效焦耳加热器的应用，其在冬季比传统电加热器节能约49.1%。这项工作将HEA-NPs的应用拓展至焦耳加热领域，并强调了进一步发展高效能源利用技术的重要性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> High-entropy alloy nanoparticles (HEA-NPs) have garnered significant interest across diverse fields. However, thus far, research on their applications has predominantly focused on electrocatalysis. Expanding the applications of HEA-NPs beyond current fields is timely and desirable but remains a challenge. Here, we demonstrate the successful femtosecond laser synthesis of HEA-NPs on the laser-induced graphene (LIG) for realizing high-performance Joule heating applications. This prepared composites (HEAs/LIG) exhibits exceptional electrothermal conversion ability with efficiency up to ~285.4 °C cm<sup>2</sup> W<sup>-1</sup>. Furthermore, the HEAs/LIG also shows high broadband infrared emissivity of ~0.98 across the wavelength range from 2.5 to 20 μm. Finally, we present the applications of HEAs/LIG as an efficient Joule heater, which consumes ~49.1% less energy compared to conventional electrical heaters in winter. This work expands the application of HEA-NPs into the Joule heating field, and underlining the importance of further development in efficient energy utilization technology.

</details>
<br>

**关键词**: femtosecond laser synthesis, high-entropy alloy nanoparticles, laser-induced graphene, Joule heating, electrothermal conversion, infrared emissivity, energy efficiency, composite materials

---

### 86. ❌ Discovery of the most compact 3+1-type quadruple star system TIC 120362137

**作者**: Tamás Borkovits, Saul Rappaport, Hai-Liang Chen, Guillermo Torres, Tibor Mitnyan, Veselin B. Kostov, Brian P. Powell, Theo Pribulla, P. Zasche, I Bíró, István Csányi, Donát R. Czavalinga, Z. Dencs, Z. Garai, J. Kolář, P. Cagaš, Zbyněk Henzl, Tom G. Kaye, Hana Kučáková, Martin Mašek
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69223-4](https://doi.org/10.1038/s41467-026-69223-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题和摘要显示该研究是关于天文学领域，具体是发现一个紧凑的四重星系统TIC 120362137，涉及恒星系统、轨道周期、天体物理观测等内容。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均属于医学影像分析领域，与论文的天文学主题完全无关，因此相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究发现了迄今为止最紧凑的3+1型四重星系统TIC 120362137，并分析了其轨道结构和动力学特性。

**关键词**: quadruple star system, TIC 120362137, compact stellar system, orbital dynamics, astrophysical discovery, stellar evolution, multiple star systems, astronomical observations

---

### 87. ❌ Single-cell thiol profiling enabled by live-cell labeling reveals metabolic heterogeneity in ferroptosis

**作者**: Daiyu Miao, Q. Y. Li, Yi Zhang, Shaojie Qin, Ying Wang, Xiaoyun Liu, Yu Bai
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70336-z](https://doi.org/10.1038/s41467-026-70336-z)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是单细胞水平的硫醇代谢分析技术及其在铁死亡研究中的应用，属于细胞生物学、代谢组学和化学分析领域。论文内容完全不涉及医学影像分析（medical image analysis）、医学成像（medical imaging）或深度学习医学成像（deep learning medical imaging）。论文使用的方法是活细胞标记和有机质谱流式细胞术，而非任何医学影像技术。因此所有关键词的相关度均为0分。

</details>
<br>

!!! info Semantic Scholar TL;DR

    An integrated strategy for thiol profiling at the single-cell level which combines live-cell labeling with organic mass cytometry is reported which is capable of pathway activity monitoring, metabolic network mapping and untargeted metabolome profiling.

!!! tip deepseek-chat TL;DR

    该论文开发了一种结合活细胞标记和有机质谱流式细胞术的单细胞硫醇分析方法，并应用该方法揭示了RSL3诱导的铁死亡中谷胱甘肽代谢的异质性。

<details open>
<summary>摘要翻译</summary>

> 硫醇在催化、氧化还原稳态和能量代谢中发挥着不可或缺的生化功能。然而，由于硫醇含量极低且易被氧化，在单细胞水平上对多种硫醇进行分析仍具挑战性。本文报道了一种在单细胞水平进行硫醇分析的综合策略，该策略将活细胞标记技术与有机质谱流式技术相结合。活细胞标记策略有助于对固有硫醇进行全面测量，扩大了检测范围并提高了灵敏度，而有机质谱流式技术则能够同时定量单个细胞中的27种标记硫醇及355种其他代谢物。通过对刺激下代谢波动的评估，证明了该集成方法的实用性与准确性，该方法能够用于通路活性监测、代谢网络图谱绘制以及非靶向代谢组分析。进一步应用此方法研究RSL3诱导的铁死亡发现，RSL3通过核因子E2相关因子2-谷胱甘肽轴抑制谷胱甘肽合成，并导致不同细胞亚型间异质性的谷胱甘肽代谢。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Thiols serve indispensable biochemical functions across catalysis, redox homeostasis and energy metabolism. However, profiling multiple thiols at the single-cell level remains challenging due to their trace amount and susceptibility to oxidation. Herein, we report an integrated strategy for thiol profiling at the single-cell level which combines live-cell labeling with organic mass cytometry. The live-cell labeling strategy facilitates the comprehensive measurement of intrinsic thiols with expanded coverage and improved sensitivity, while organic mass cytometry enables simultaneous quantification of 27 labeled thiols and 355 other metabolites from single cells. Assessment of metabolic fluctuation upon stimulation demonstrates practicability and accuracy of this integrated methodology which is capable of pathway activity monitoring, metabolic network mapping and untargeted metabolome profiling. Further application of this method in investigating RSL3-triggered ferroptosis reveals that RSL3 inhibits glutathione synthesis via nuclear factor E2-related factor 2- glutathione axis and results in heterogenous glutathione metabolism between subtypes.

</details>
<br>

**关键词**: single-cell thiol profiling, live-cell labeling, organic mass cytometry, metabolic heterogeneity, ferroptosis, glutathione metabolism, RSL3, metabolome profiling

---

### 88. ❌ UV-activated assisted electrochemical process for mine water deep mineralization and resource recovery

**作者**: Xiaohu Liu, Youzheng Chai, Yuwei Gu, Yongqi Li, Xiao Wang, Qiancheng Wang, Gong Zhang, Huijuan Liu, Jiuhui Qu
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70043-9](https://doi.org/10.1038/s41467-026-70043-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是高盐度矿井水的处理技术，通过紫外线激活辅助电化学过程实现有机物的矿化和资源回收。论文内容完全围绕水处理、电化学、紫外线激活、资源回收等环境工程领域，与医学图像分析、医学成像、深度学习医学成像等医学影像领域没有任何关联。所有关键词的相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究开发了一种紫外线激活辅助电化学工艺，有效去除矿井水中的稳定有机物（总有机碳去除率约89.9%），并通过集成双极膜电渗析实现了酸、高纯度碱和可回用水的资源回收。

<details open>
<summary>摘要翻译</summary>

> 在矿井水膜浓缩过程中产生的高盐度矿井水含有结构稳定的复杂有机物，这些物质难以通过常规高级氧化工艺去除和矿化，最终产生低价值的副产盐，阻碍了资源化利用路径。本研究利用其固有发色团和共轭结构对紫外光的敏感性，开发了一种紫外活化辅助电化学工艺。该方法通过紫外/氧化剂协同作用，实现了约89.9%的总有机碳去除率，且在1000小时内性能衰减极微。结合紫外-可见光谱、荧光激发-发射矩阵光谱、傅里叶变换离子回旋共振质谱以及模型污染物实验，本研究阐明了驱动有机物矿化的紫外活化与自由基攻击协同机制。将净化后的浓盐水直接与双极膜电渗析集成，成功生产出酸、高纯度碱（>99%）和可回用水，从而实现了杂质去除与资源回收的闭环。该集成系统为高价值资源回收和可持续矿井水管理提供了有力的策略。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> High-salinity mine water generated during membrane concentration of mine water contains structurally stable complex organic matter that resists removal and mineralization by conventional advanced oxidation processes, ultimately producing low-value by-product salts that hinder the resource utilization pathway. Leveraging the ultraviolet sensitivity of inherent chromophore groups and conjugated structures, this study developed an ultraviolet-activated assisted electrochemical process. By harnessing ultraviolet/oxidant synergies, this approach achieves ~89.9% total organic carbon removal, with minimal performance decay over 1000 hours. Combined with ultraviolet-visible spectroscopy, fluorescence excitation-emission-matrix spectroscopy, fourier transform ion cyclotron resonance mass spectrometer, and model contaminant experiments, this study elucidates an ultraviolet activation and radical attack synergistic mechanism driving organic mineralization. The direct integration of purified brine with bipolar membrane electrodialysis successfully produces acid, high-purity alkali (>99%), and reusable water, thereby closing the loop of impurities removal and resource recovery. This integrated system offers a strong strategy for high-value resource recovery and sustainable mine water management.

</details>
<br>

**关键词**: mine water treatment, ultraviolet-activated electrochemical process, organic mineralization, resource recovery, bipolar membrane electrodialysis, total organic carbon removal, high-salinity water, sustainable water management

---

### 89. ❌ Integrated computational and experimental immunoengineering of adeno-associated virus capsid T cell epitopes in mice

**作者**: Sojin Bing, Arya Eskandarian, Sean Smith, Abdul Mohin Sajib, Stephanee Warrington, Sima Saleh, Susana S. Najera, Rebecca J. D’Esposito, Luis V. Santana‐Quintero, Ronit Mazor
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69917-9](https://doi.org/10.1038/s41467-026-69917-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是基因治疗中腺相关病毒（AAV）载体的免疫原性工程，通过计算预测和实验验证来改造AAV9衣壳以减少T细胞表位。研究内容完全属于免疫工程、基因治疗和计算生物学领域，与医学图像分析、医学成像或深度学习医学成像没有任何直接或间接关联。论文中未提及任何图像数据、成像技术或图像分析方法。

</details>
<br>

!!! info Semantic Scholar TL;DR

    This study combines computational prediction with experimental validation to engineer AAV9 capsids with reduced immunogenicity, using the Epitope Modification and MHC Prediction pipeline, which systematically automates the evaluation of amino acid substitutions for their predicted effects on major histocompatibility complex (MHC) presentability.

!!! tip deepseek-chat TL;DR

    该研究通过计算和实验方法改造AAV9衣壳的T细胞表位，成功降低了免疫原性，为优化基因治疗载体设计提供了新策略。

<details open>
<summary>摘要翻译</summary>

> 腺相关病毒（AAV）载体在基因治疗中被广泛应用，但其免疫原性仍是一个重大挑战，限制了长期疗效和重复给药的可行性。本研究结合计算预测与实验验证，对AAV9衣壳进行工程化改造以降低其免疫原性。为此，我们开发了“表位修饰与主要组织相容性复合体（MHC）预测”（EMMP）流程，该流程能系统化、自动化地评估氨基酸替换对MHC递呈性（presentability）的预测影响。利用此流程，我们以概念验证的方式，对一个已鉴定并表征的AAV9衣壳中的CD4⁺ T细胞表位进行了修饰。研究筛选出两种突变变体R312H和R312Q，并在体外评估其转导效率，在体内评估其免疫反应调节能力。值得注意的是，R312Q变体显示出T细胞活化和抗AAV9抗体产生的显著降低，尽管在低感染复数（MOI）下其转导效率略有下降。这些结果展示了一种优化AAV载体设计的理性方法，在提升基因治疗安全性和有效性方面具有潜在应用价值。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Adeno-associated virus (AAV) vectors are widely used in gene therapy, but their immunogenicity remains a significant challenge, limiting long-term efficacy and the feasibility of repeated administration. In this study, we combine computational prediction with experimental validation to engineer AAV9 capsids with reduced immunogenicity. To facilitate this, we developed the Epitope Modification and MHC Prediction (EMMP) pipeline, which systematically automates the evaluation of amino acid substitutions for their predicted effects on major histocompatibility complex (MHC) presentability. Using this pipeline, we modify a CD4⁺ T-cell epitope in the AAV9 capsid that is identified and characterized as a proof-of-concept. Two mutant variants, R312H and R312Q, are selected and evaluated for transduction efficiency in vitro and immune response modulation in vivo. Notably, R312Q shows a significant reduction in T-cell activation and anti-AAV9 antibody production, albeit with a slight reduction in transduction at low multiplicities of infection (MOI). These results demonstrate a rational approach for optimizing AAV vector design, with potential applications for improving the safety and efficacy of gene therapy.

</details>
<br>

**关键词**: adeno-associated virus, gene therapy, immunogenicity, T-cell epitope, capsid engineering, computational prediction, AAV9, MHC presentability

---

### 90. ❌ HIV-seq reveals gene expression differences between HIV-transcribing cells from viremic and suppressed people with HIV

**作者**: J. Frouard, Sushama Telwatte, Xiaoyu Luo, Natalie Gill, Reuben Thomas, Douglas Arneson, Pavitra Roychoudhury, Atul J. Butte, Joseph K. Wong, Hoh Rebecca, Steven G. Deeks, Sulggi A. Lee, Eva Tolosa, A Steven
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-68797-3](https://doi.org/10.1038/s41467-026-68797-3)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文标题为'HIV-seq reveals gene expression differences between HIV-transcribing cells from viremic and suppressed people with HIV'，摘要描述了一种名为'HIV-seq'的新方法，用于通过单细胞RNA测序（scRNA-seq）检测HIV转录细胞，并分析其在病毒血症和ART抑制期间的基因表达差异。论文的核心内容是HIV研究、单细胞测序技术和基因表达分析，与'medical image analysis'、'medical imaging'和'deep learning medical imaging'这三个关键词完全无关，因为这些关键词涉及医学影像分析和深度学习在医学影像中的应用，而论文未涉及任何影像数据、图像处理或深度学习在影像中的应用。

</details>
<br>

!!! info Semantic Scholar TL;DR

    A technique to increase detection of HIV RNA during scRNA-seq is developed and the transcriptomes of HIV RNA+ blood cells obtained pre- and post-antiretroviral therapy are compared to provide insights into the persistence of the HIV RNA+ reservoir.

!!! tip deepseek-chat TL;DR

    该研究开发了一种名为'HIV-seq'的新方法，通过改进单细胞RNA测序来检测HIV转录细胞，发现这些细胞在病毒血症期间表现出细胞毒性特征，而在ART抑制期间则表现出抗炎特征。

<details open>
<summary>摘要翻译</summary>

> 在抗逆转录病毒治疗（ART）抑制的艾滋病病毒感染者（PWH）中，能够转录HIV的细胞可能维持慢性炎症状态，并可能在ART中断后促进病毒反弹。然而，由于这些细胞频率低且HIV转录本水平通常较低（且多为非多聚腺苷酸化），使用单细胞RNA测序（scRNA-seq）进行研究存在困难。通过在scRNA-seq过程中加入靶向HIV保守区域的捕获序列（我们称之为“HIV-seq”的新方法），我们从PWH样本中检测到的单细胞平均HIV读数增加了一倍。无论在病毒血症期还是ART抑制期，HIV RNA阳性细胞均在效应记忆T细胞中富集，但仅在病毒血症期表现出细胞毒性特征。相比之下，来自ART抑制时间点的HIV转录细胞则表现出独特的抗炎特征，包括TGF-β信号升高和IFN信号减弱。这些发现表明，HIV-seq是一种有效的工具，有助于更好地理解HIV转录细胞在ART期间持续存在的机制。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> HIV-transcribing cells can perpetuate chronic inflammation in ART-suppressed people with HIV (PWH) and likely contribute to viral rebound after ART interruption. However, these cells are difficult to study using single-cell RNA-seq (scRNA-seq) due to their low frequency and low levels of HIV transcripts, which are usually not polyadenylated. By spiking in capture sequences targeting conserved regions of HIV during scRNA-seq - a new method we call "HIV-seq" - we detect double the mean number of HIV reads per cell from PWH. HIV RNA+ cells are enriched among T effector memory cells during both viremia and ART suppression but exhibit a cytotoxic signature during viremia only. In contrast, HIV-transcribing cells from ART-suppressed timepoints exhibit a distinct anti-inflammatory signature involving elevated TGF-β and diminished IFN signaling. These findings demonstrate that HIV-seq is a useful tool to better understand the mechanisms by which HIV-transcribing cells can persist during ART.

</details>
<br>

**关键词**: HIV-seq, single-cell RNA-seq, HIV-transcribing cells, gene expression, ART suppression, viremia, T effector memory cells, anti-inflammatory signature

---

### 91. ❌ Integrative epigenomic landscape of Alzheimer’s Disease brains reveals oligodendrocyte molecular perturbations associated with tau

**作者**: Stephanie R. Oatman, J. Reddy, Amin Atashgaran, X. Wang, Yuhao Min, Zachary Quicksall, Floor Vanelderen, Minerva M. Carrasquillo, Chia‐Chen Liu, Yu Yamazaki, T. Nguyen, Michael Heckman, Na Zhao, Michael DeTure, Melissa E. Murray, GuoJun Bu, Takahisa Kanekiyo, Dennis W. Dickson, M. Allen, Nilüfer Ertekin-Taner
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-68864-9](https://doi.org/10.1038/s41467-026-68864-9)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究阿尔茨海默病（AD）的整合表观基因组学，通过DNA甲基化分析、转录组-甲基组整合等方法，揭示与tau病理相关的少突胶质细胞基因扰动。研究内容属于神经科学、表观遗传学和生物信息学领域，完全不涉及医学图像分析、医学成像或深度学习医学成像。论文未使用任何医学图像数据或图像分析方法，而是基于分子生物学和基因组学数据。

</details>
<br>

!!! info Semantic Scholar TL;DR

    The integrative epigenomic landscape of AD is uncovered, tau-related oligodendrocyte gene perturbations as a common potential pathomechanism across tauopathies are demonstrated and findings are shared via the Multiomic Atlas.

!!! tip deepseek-chat TL;DR

    本研究通过整合表观基因组分析揭示了阿尔茨海默病大脑中与tau病理相关的少突胶质细胞基因扰动，为tau蛋白病的共同病理机制提供了新见解。

<details open>
<summary>摘要翻译</summary>

> 阿尔茨海默病（AD）大脑存在异质性的神经病理学与生物化学改变。捕捉与此异质性相关的表观遗传因素，可为AD病理生理机制提供新的生物学见解。本研究对472例AD大脑进行了全表观基因组关联分析，检测了与AD发病机制核心相关的神经病理学及脑内蛋白质水平的DNA甲基化状态。通过采用新型区域甲基化（rCpGm）分析方法，我们识别出5478个显著关联，其中99.7%与tau蛋白生化指标相关，并在外部数据集中验证了93个一致性关联。转录组-甲基组整合分析显示，少突胶质细胞相关基因存在显著富集，包括已知的AD风险基因BIN1、既往研究提示与AD相关的髓鞘形成基因MYRF、MBP和MAG，以及LDB3等新型基因。在独立的AD及原发性tau蛋白病数据集中对这些扰动进行进一步表征，均凸显出与tau蛋白相关的一致性关联。综上所述，本研究揭示了AD的整合表观基因组图谱，证实了tau相关的少突胶质细胞基因扰动是跨tau蛋白病的共同潜在病理机制，并通过我们的多组学图谱共享了相关发现。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Alzheimer's disease (AD) brains have variable neuropathologic and biochemical changes. Capturing epigenetic factors associated with this variability can reveal novel biological insights into AD pathophysiology. Here, we conduct an epigenome-wide association study of DNA methylation in 472 AD brains with neuropathologic and biochemical brain protein levels core to AD pathogenesis. Using a novel regional methylation (rCpGm) approach, we identify 5478 significant associations, 99.7% of which associate with tau biochemical measures, and 93 concordant associations in external datasets. Transcriptome-methylome integration reveals enrichment in oligodendrocyte genes, including known AD risk gene BIN1, myelination genes MYRF, MBP and MAG previously implicated in AD, and novel genes like LDB3. Further characterization of these perturbations in independent AD and primary tauopathy datasets highlights consistent tau-related associations. In summary, we uncover the integrative epigenomic landscape of AD, demonstrate tau-related oligodendrocyte gene perturbations as a common potential pathomechanism across tauopathies and share findings via our Multiomic Atlas.

</details>
<br>

**关键词**: Alzheimer's disease, epigenomics, DNA methylation, tau pathology, oligodendrocyte, BIN1, multiomic atlas, tauopathies

---

### 92. ❌ Pt size-dependent reverse oxygen spillover on Sn-doped Pt/TiO2 for CO oxidation

**作者**: Shangchao Xiong, Zhengjun Gong, H. Y. Wang, Jianqiang Shi, Hailong Liu, Xiaoping Chen, Jinxing Mi, Jianjun Chen, Jin Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69327-x](https://doi.org/10.1038/s41467-026-69327-x)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是Pt/TiO2催化剂中Pt颗粒尺寸对反向氧溢流效应的影响及其在CO氧化反应中的应用，属于材料科学、催化化学和计算化学领域。论文内容完全不涉及医学图像分析、医学成像或深度学习医学成像，没有使用医学图像数据、医学成像技术或深度学习在医学图像中的应用。因此所有关键词的相关度均为0分。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究揭示了Pt颗粒尺寸对Sn掺杂Pt/TiO2催化剂中反向氧溢流效应的影响，发现纳米团簇Pt具有最显著的反向氧溢流效应，从而在CO氧化反应中表现出最高的周转频率。

<details open>
<summary>摘要翻译</summary>

> 载体向贵金属活性位点的界面氧迁移，即反向氧溢流，是影响Pt/TiO<sub>2</sub>催化剂性能的关键金属-载体相互作用。本研究通过原位表征与从头算分子动力学模拟相结合，揭示了Pt/Sn<sub>0.2</sub>Ti<sub>0.8</sub>O<sub>2</sub>催化剂中Pt颗粒尺寸对反向氧溢流的影响效应。在单原子Pt、纳米团簇Pt和纳米晶Pt中，纳米团簇Pt表现出最显著的反向氧溢流现象，从而在一氧化碳氧化反应中实现了最高的转换频率。这种最显著的反向氧溢流主要归因于CO吸附（具有适中的吸附能）引发的、向界面晶格氧的最强电子转移。相比之下，CO在单原子Pt上的吸附过强，难以启动反向氧溢流；而在纳米晶Pt上，CO吸附会导致Pt位点与载体间的相互作用减弱，从而阻碍反向氧溢流。本研究阐明了Pt颗粒尺寸与反向氧溢流效应之间的关系，为设计具有优异活性的贵金属催化剂提供了理论基础。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Interfacial oxygen migration from support to noble metal active sites, termed reverse oxygen spillover, represents a critical metal-support interaction influencing the performance of Pt/TiO<sub>2</sub> catalysts. In this study, we uncover a size effect of Pt particles on reverse oxygen spillover in Pt/Sn<sub>0.2</sub>Ti<sub>0.8</sub>O<sub>2</sub> catalysts via a combination of in situ characterizations with ab initio molecular dynamics simulations. Among single-atom Pt, nanocluster Pt, and nanocrystal Pt, nanocluster Pt exhibits the most pronounced reverse oxygen spillover and thus achieves the highest turnover frequency in CO oxidation. The most pronounced reverse oxygen spillover is mainly due to the strongest electron transfer to the interfacial lattice oxygen triggered by CO adsorption with moderate adsorption energy. In contrast, CO adsorption on single-atom Pt is too strong to initiate reverse oxygen spillover, while on nanocrystal Pt, it leads to a weakening of the interaction between Pt sites and the support, thus hinders the reverse oxygen spillover. This study clarifies the relationship between Pt particle size and reverse oxygen spillover effects, furnishing a theoretical basis for designing noble metal catalysts with excellent activity.

</details>
<br>

**关键词**: reverse oxygen spillover, Pt particle size, CO oxidation, Pt/TiO2 catalyst, Sn-doped, nanocluster Pt, metal-support interaction, ab initio molecular dynamics

---

### 93. ❌ Moisture-responsive crystallization strategy for efficient CsPbI3 solar cells fabricated under high-humidity conditions

**作者**: Weideren Dai, Jie Li, Yanzhuo Gou, Jiaqi Zhang, Zexun Pan, Xianglong Li, Haojun Hu, S. Q. Wang, Tao Mei, Xianbao Wang, Chao Chen, Qidong Tai, Jingbi You
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-69687-4](https://doi.org/10.1038/s41467-026-69687-4)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是钙钛矿太阳能电池（CsPbI3 PSCs）的制造工艺，具体涉及在高温条件下通过湿度响应结晶策略提高器件效率。论文内容完全围绕材料科学、化学工程和光伏技术，与医学图像分析、医学成像或深度学习医学成像没有任何关联。所有关键词均得0分，因为论文主题与这些医学领域关键词完全无关。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究解决了CsPbI3钙钛矿太阳能电池在高温条件下制造时相不稳定的问题，通过引入丙基三乙氧基硅烷（PTES）的湿度响应结晶策略，使器件在55%相对湿度下实现了21.00%的功率转换效率，并表现出良好的操作稳定性。

<details open>
<summary>摘要翻译</summary>

> CsPbI<sub>3</sub>钙钛矿固有的相不稳定性要求苛刻的制备条件，严重阻碍了其实际应用。在二甲胺（DMA）介导的CsPbI<sub>3</sub>成核体系中，Cs<sup>+</sup>/DMA<sup>+</sup>离子交换过程对最终薄膜质量起着关键调控作用。本研究采用一种湿度响应结晶策略，利用丙基三乙氧基硅烷（PTES）在高湿度（55%）环境空气中沉积CsPbI<sub>3</sub>薄膜。研究表明，硅氧烷基团能够捕获中间相DMAPbI<sub>3</sub>中的DMA<sup>+</sup>，促进DMA<sup>+</sup>的提取与Cs<sup>+</sup>的掺入，从而加速结晶动力学。该方法使CsPbI<sub>3</sub>钙钛矿太阳能电池（PSCs）在55%相对湿度（RH）条件下制备时，获得了21.00%的功率转换效率（PCE）和高达86.1%的填充因子（FF）。在25%较低湿度下制备的器件，以及在氮气（N<sub>2</sub>）氛围中旋涂薄膜后于环境空气中退火的器件，分别实现了21.85%和22.60%（认证效率22.02%）的更高效率。此外，经PTES处理的器件在环境条件下展现出优异的工作稳定性。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> The intrinsic phase instability of CsPbI<sub>3</sub> perovskites necessitates stringent fabrication conditions, significantly hindering the practical deployment. In the DMA-mediated CsPbI<sub>3</sub> nucleation system, the Cs<sup>+</sup>/DMA<sup>+</sup> ion exchange critically governs the resulting film quality. Here, we employ a moisture-responsive crystallization strategy utilizing propyltriethoxysilane (PTES) to deposite CsPbI<sub>3</sub> under ambient air with high humidity (55%). We demonstrate that the siloxane groups can capture DMA<sup>+</sup> in the intermediate DMAPbI<sub>3</sub>, facilitating DMA<sup>+</sup> extraction and Cs<sup>+</sup> incorporation, thereby accelerating crystallization kinetics. This approach enables CsPbI<sub>3</sub> PSCs to achieve a power conversion efficiency (PCE) of 21.00% with an impressive fill factor (FF) of 86.1% while processing perovskite under relative humidity (RH) of 55%. Higher PCEs of 21.85% and 22.60% (certified 22.02%) were achieved for devices fabricated at a lower RH of 25% and for films spin-coated under an N<sub>2</sub> atmosphere followed by annealing in ambient air, respectively. Furthermore, PTES-treated devices exhibit excellent operational stability under ambient conditions.

</details>
<br>

**关键词**: CsPbI3 perovskite, solar cells, moisture-responsive crystallization, high-humidity fabrication, power conversion efficiency, operational stability, propyltriethoxysilane, phase instability

---

### 94. ❌ Stereoselective depolymerization of chiral polyesters

**作者**: Rulin Yang, Guangqiang Xu, Xia Guo, Wei Wu, Yanju Jia, Zhiheng Wang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70164-1](https://doi.org/10.1038/s41467-026-70164-1)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是高分子化学领域的手性聚酯立体选择性解聚，涉及合成催化剂、手性识别和聚合物转化，与医学图像分析、医学成像或深度学习医学成像完全无关。论文内容属于化学催化和高分子材料领域，没有涉及任何医学图像或成像技术。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该论文研究了使用合成催化剂BisSalen-Al实现手性聚合物聚乳酸（PLA）的立体选择性解聚为手性丙交酯单体，揭示了催化剂手性空腔与聚合物立体化学的匹配机制，将不对称催化拓展到了大分子体系。

<details open>
<summary>摘要翻译</summary>

> 酶通过其精确构筑的手性活性口袋，能够实现对大小分子的高选择性手性识别，从而驱动不对称转化。受酶催化启发，合成催化剂的设计已实现多种小分子的不对称反应。然而，由合成催化剂催化的高分子立体选择性转化仍未被探索。本工作通过展示利用合成催化剂实现聚合物的手性识别与转化，在该领域取得了重要进展。以代表性手性聚合物聚乳酸（PLA）为模型底物，一种特殊设计的具有受限手性空腔的催化剂BisSalen-Al，能够促进PLA立体选择性解聚为手性丙交酯（LA）单体。通过对催化剂结构与立体选择性之间关系的深入探究，揭示了聚合物立体化学与催化剂手性空腔匹配的手性识别机制。本工作为手性聚合物的立体选择性转化提供了一种策略，并显著推动了不对称催化向高分子体系的拓展。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Enzymes precisely structured chiral active pockets can achieve highly selective recognition of chirality in small molecules as well as macromolecule, enabling asymmetric transformation. Inspired by enzymic catalysis, the design of synthetic catalysts has enabled diverse asymmetric reactions of small molecules. However, stereoselective transformations of macromolecules catalyzed by synthetic catalysts remain unexplored. This work establishes a significant advancement in the field by demonstrating chiral recognition and conversion of polymers using synthetic catalysts. Employing the representative chiral polymer polylactic acid (PLA) as a model substrate, a specially designed catalyst BisSalen-Al with confined chiral cavity facilitated the stereoselective depolymerization of PLA into chiral lactide (LA) monomers. In depth exploration of the relationship between catalyst structure and stereoselectivity revealed the chiral recognition mechanism of polymer stereochemistry and catalyst chiral cavity matching. This work provides a strategy for the stereoselective conversion of chiral polymers and significantly advances the expansion of asymmetric catalysis into macromolecular systems.

</details>
<br>

**关键词**: stereoselective depolymerization, chiral polyesters, synthetic catalysts, polylactic acid (PLA), chiral recognition, asymmetric catalysis, macromolecular systems, BisSalen-Al catalyst

---

### 95. ❌ Cost-effective strategies can reduce water and energy requirements in China’s wastewater treatment by 2035

**作者**: Siqi Han, Edward R. Jones, Tuo Yin, Weijie Chen, Yanhong Wu, En Xie, Lei Li, Yang Xiao, Jiading Zhang, Peng Zhu, Xiaokaitijiang Kasmu, Qiang Zheng, Bo Zhou, Yunkai Li
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70159-y](https://doi.org/10.1038/s41467-026-70159-y)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究的是中国污水处理的水和能源足迹评估及成本效益优化策略，属于环境工程和可持续发展领域。所有评分关键词（medical image analysis, medical imaging, deep learning medical imaging）均涉及医学影像分析，与论文主题完全无关。论文未提及任何医学影像、医学图像分析或深度学习在医学影像中的应用。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究评估了中国污水处理的水和能源足迹，并提出通过多目标权衡选择处理工艺，到2035年可将水足迹减少16.1%、能源足迹减少25.6%，投资低于总处理成本的8%。

<details open>
<summary>摘要翻译</summary>

> 污水处理是保障未来水资源安全的关键环节。然而，该过程本身在水耗与能耗方面面临重大挑战。在不影响污水处理效果的前提下，以低成本减少这些投入对于可持续发展至关重要。本文基于中国10,124座城镇污水处理厂的估算数据及90个案例，评估了污水处理的水足迹与能源足迹。研究表明，2009年至2022年间，中国污水处理的水足迹与能源足迹已增长近三倍。通过多目标权衡优化处理工艺选择，可有效实现减排。到2035年，中国污水处理的水足迹与能源足迹可分别降低16.1%和25.6%，所需投资低于处理总成本的8%，且污染物去除效果保持稳定。我们的研究为引导可持续污水管理、支持实现可持续发展目标（Sustainable Development Goals, SDGs）提供了一个具有广泛适用性的框架。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Wastewater treatment is a key component in ensuring future water resource security. However, this process itself faces major challenges in water and energy consumption. Reducing these inputs at low cost without compromising wastewater treatment effectiveness is crucial for sustainable development. Here, we assess the water and energy footprint of wastewater treatment in China, using estimated data from 10,124 urban wastewater treatment plants and 90 cases. We show that the water and energy footprints of wastewater treatment in China have nearly tripled from 2009 to 2022. By aligning treatment process selection through multi-objective trade-offs, reductions can be effectively achieved. By 2035, China's wastewater treatment water footprint and energy footprint could be reduced by 16.1% and 25.6%, respectively, with investments below 8% of total treatment costs, while the removal remains stable. Our findings offer a broadly applicable framework to guide sustainable wastewater management and support progress toward the Sustainable Development Goals.

</details>
<br>

**关键词**: wastewater treatment, water footprint, energy footprint, China, cost-effective strategies, sustainable development, multi-objective trade-offs, 2035

---

### 96. ❌ Contrary effects of soil moisture-atmosphere feedback on dry and humid heatwaves

**作者**: Sisi Chen, Peng Ji, Shanshui Yuan, Qibo Xu, Yu Ye, Jianyun Zhang
**期刊/来源**: nature_communications
**发布日期**: 2026-03-03
**DOI**: [10.1038/s41467-026-70210-y](https://doi.org/10.1038/s41467-026-70210-y)

**评分**: 0.0 / 14.0 ❌

<details>
<summary>评分详情</summary>

| 关键词 | 权重 | 相关度 | 得分 |
|------|------|------|------|
| medical image analysis | 1.0 | 0.0/10 | 0.0 |
| medical imaging | 1.0 | 0.0/10 | 0.0 |
| deep learning medical imaging | 1.0 | 0.0/10 | 0.0 |

**评分理由**: 论文研究土壤湿度-大气反馈（SAF）对干热浪和湿热浪的不同影响，属于气候科学和地球科学领域，与医学图像分析、医学成像、深度学习医学成像等关键词完全无关。论文内容涉及CMIP6实验、部分微分分析、全球地图绘制、温度-湿度耦合机制等，没有任何医学或图像分析相关内容。

</details>
<br>

!!! tip deepseek-chat TL;DR

    该研究揭示了土壤湿度-大气反馈（SAF）通过温度-湿度耦合对干热浪和湿热浪产生相反影响的全球空间分异机制，发现SAF在中低纬度减少湿热浪持续时间和强度20-40%，而在高纬度增加≥50%。

<details open>
<summary>摘要翻译</summary>

> 尽管土壤湿度-大气反馈（SAF）已被广泛认为是极端温度事件的关键驱动因子，但其对干热浪和湿热浪的差异化影响仍未得到充分理解，这主要源于以往研究多集中于干热浪。本研究结合CMIP6的SAF扰动实验与偏微分分析，构建了1985-2014年间SAF对全球湿热浪与干热浪影响的空间分布图，并阐明了其内在机制。与SAF对干热浪普遍存在的均匀增强效应不同，在土壤湿度-大气耦合强烈的中低纬度地区，SAF通过减少大气湿度使湿热浪的持续时间和强度降低20-40%；而在高纬度地区，SAF则使其持续时间和强度增加≥50%。这种空间分异响应主要归因于SAF引发的热力增温与湿度耗竭之间的竞争，二者分别提升或降低湿球温度。我们的研究揭示了SAF通过温度-湿度耦合影响极端高温的双重调节机制，为针对干热浪与湿热浪的区域差异化适应策略提供了科学依据。

</details>
<br>

<details>
<summary>摘要 (Abstract)</summary>

> Although soil moisture-atmosphere feedback (SAF) has been widely recognized as a key driver of temperature extremes, its distinct impacts on dry and humid heatwaves remain insufficiently understood, largely due to previous studies focusing predominantly on dry heatwaves alone. In this study, we combine SAF perturbation experiments from CMIP6 with partial differential analysis to construct a global map of SAF's influence on both humid and dry heatwaves during 1985-2014 and to elucidate the underlying mechanisms. Unlike the homogeneously amplifying effect of SAF on dry heatwaves, SAF reduces the duration and severity of humid heatwaves by 20-40% in low-to-mid latitude regions with strong soil moisture-atmosphere coupling. In contrast, it increases their duration and severity by ≥50% in high latitude regions. These spatially divergent responses are primarily attributed to the competition between SAF-induced thermal warming and moisture depletion, which respectively raise or lower wet-bulb temperatures. Our findings reveal a dual regulatory mechanism by which SAF influences heat extremes through temperature-humidity coupling, providing scientific insights for region-specific adaptation strategies to both dry and humid heatwaves.

</details>
<br>

**关键词**: soil moisture-atmosphere feedback, dry heatwaves, humid heatwaves, temperature-humidity coupling, wet-bulb temperature, CMIP6 experiments, global spatial patterns, climate adaptation strategies

---
