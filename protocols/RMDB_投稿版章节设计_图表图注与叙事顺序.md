# RMDB 投稿版章节设计、图表图注与叙事顺序

## 论文的唯一主问题

**眼底 AI 对原始 cIMT 的高性能，究竟是在发现动脉壁异常，还是在重现年龄这一共同驱动因素？**

这不是一篇“模型能否预测 cIMT”的文章，而是一篇“何时可以把眼底血管特征称为系统性血管生物标志物”的文章。

## 读者的认知路线

```text
临床愿望：用低成本眼底看见早期全身血管异常
          ↓
隐藏冲突：年龄同时塑造眼底与 cIMT
          ↓
证据反转：原始高性能不证明超越年龄的生物标志物信号
          ↓
方法回应：RMDB 把图像变成带有质量、双眼和不确定性的表型
          ↓
严格审计：残余目标、负对照、重复性、跨域迁移
          ↓
边界结论：候选表型可靠性得到审计；独立 cIMT 临床确认仍待完成
```

## 标题与摘要

### Title

*Beyond the Age Mirage: A Patient-Level Audit of Retinal Microvascular Phenotypes for Age-Discordant Carotid Intima-Media Thickness*

### Abstract

采用 Background - Objective - Methods - Results - Interpretation 五段式、总长 250-300 词。前两句不提模型名称，先提出年龄代理问题；结果第一句先报告 clinical-only 基线在 raw cIMT 任务中的强表现，随后才报告年龄条件化任务和 RMDB 的小而有界收益。最后一句必须含有“not independent clinical confirmation”。

## 1. Introduction

### 1.1 The clinical opportunity

cIMT 可反映亚临床动脉壁改变，但超声难在眼科筛查或低资源场景中规模化获得。眼底摄影提供无创、可重复的微血管窗口。

### 1.2 The age mirage

年龄会影响 cIMT 和眼底血管外观。若将原始高/低 cIMT 直接作为标签，模型很容易将年龄代理误报为血管病理信号。这里必须把“高 cIMT”与“相对年龄异常偏高 cIMT”区分开。

### 1.3 The measurement-chain gap

血管表型不是直接存在于一张图中的事实，而是由图像质量、软分割、动静脉结构、视盘定位、双眼聚合和域偏移共同决定的测量结果。

### 1.4 Objective and contributions

用一段并列写出四点：年龄条件化 cIMT 偏离目标；mass/structure 双读出；双眼与不确定性门控；内部患者级审计加标签盲外部表型迁移。

## 2. Methods

### 2.1 Study design, cohorts, and evidence roles

表 1 在这里首次出现。必须用“internal outcome development”“external anatomy transport”“mechanism proxy”三个标签区分 China-Fundus-CIMT、RAV/Fundus-AVSeg 与 mBRSET。

### 2.2 Endpoint construction: raw cIMT versus age-discordant cIMT

定义 Task A（raw cIMT level）、Task B（age/sex-conditioned cIMT deviation）和 Task C（accelerated vascular aging 辅助二分类）。要求所有图表都注明当前属于哪个任务；不同任务的 AUC 不能并排后暗示可比。

### 2.3 Image preprocessing and phenotype provenance

说明 RGB 预处理、视盘定位、VascX logits、occupancy、文件完整性与 189 例 mBRSET 视盘回退记录。

### 2.4 RMDB dual-readout representation

#### 2.4.1 Soft mass readout

软血管质量、动静脉软质量、Zone B 质量、support 和概率不确定性。

#### 2.4.2 Structural readout

硬/结构化血管分数、骨架长度、分支、端点、连通性、动静脉比和视盘几何。

#### 2.4.3 Bilateral phenotype and quality gating

bilateral mean、absolute difference、within-eye SD、disc status、quality weights；任何回退只可降权或进入敏感性分析，不能自动解释为病理。

### 2.5 Internal evaluation and falsification

患者级 nested CV；OOF 指标；paired bootstrap；标签置换；随机双眼配对；重复性；校准和 decision curve。

### 2.6 Label-blind external phenotype transport

RAV/Fundus-AVSeg 用于 anatomy transport，mBRSET 用于 mechanism proxy。说明所有外部分析均不用于 RMDB 调参。

## 3. Results and Discussion

采用 VOCT 风格：每个小节以一个结论句开头，紧随数值、图表和解释边界，不把“讨论”全部堆到文章末尾。

### 3.1 Raw cIMT discrimination does not establish signal beyond age

图 1 和图 2。先让读者看到年龄代理问题，再展示 E0 clinical 与 E1-E6。这里需要明确：raw endpoint 的表现不等于识别 accelerated vascular aging。

### 3.2 Age-discordant cIMT leaves a weak but testable residual signal

图 2D 与表 2 的 Task B block。E7/E8 的结果必须如实写为弱信号；这是方法学发现而不是掩盖失败。

### 3.3 RMDB makes phenotype reliability observable

图 3。通过真实左右眼、soft mass、结构读出和质量权重说明“测量可靠性”如何进入患者级特征。

### 3.4 Uncertainty-aware aggregation yields bounded reliability gains

图 4。报告 E8/E11、paired bootstrap、coverage-risk、重复性和负对照。优势只写 CI 支持的指标。

### 3.5 Cross-domain transport identifies both portability and failure

图 5 与图 6。RAV 支持高重叠 anatomy transport；Fundus-AVSeg 用作低重叠压力测试；真实失败案例证明 RMDB 何时不应该被信任。

### 3.6 Mechanism proxies do not justify a universal systemic-risk claim

图 7 和表 5。mBRSET 结果按照高血压、无 DR、vascular disease、diabetic foot 和 AMI 的异质性逐项报告；所有低事件终点明确探索性。

## 4. Conclusion

结论只保留三层：原始 cIMT 基准可能被年龄代理夸大；RMDB 提供可审计的可靠表型框架；独立高分辨率 cIMT 队列是临床确认的下一步。

## 主图与图注

### Figure 1 | The age-proxy paradox in retinal cIMT modeling

**图的论点：** 原始 high/low cIMT 任务无法区分年龄相关信息与异常血管老化。

**面板：** A 传统任务；B 内部队列年龄-cIMT 散点；C 近同龄同性别的真实眼底输入和年龄条件化 cIMT 差异。

**图注：** 使用 `figures/rmdb_age_mirage/Figure1_caption.md` 中的已锁定版本。

### Figure 2 | Performance reversal after conditioning cIMT on age and sex

**图的论点：** 移除年龄代理后，模型必须在严格得多的目标上重新被评价。

**面板：** A raw Task A 的 E0-E6；B E0 与 E4 paired delta forest；C Task A → Task B 性能落差；D Task B 中 mass、structure、dual 的比较；E 大字结论。

**图注：** 使用 `figures/rmdb_age_mirage/Figure2_caption.md` 中的已锁定版本。

### Figure 3 | RMDB converts real bilateral retinal images into an auditable phenotype

**图的论点：** 创新不在网络花哨，而在把质量、结构、双眼差异和不确定性一起保留。

**面板：** A 不同患者的真实左右眼 RGB；B soft mass 与 occupancy；C A/V 和结构拓扑；D bilateral mean/difference/within-eye SD；E quality gate 到患者级 phenotype。

**图注：** 使用 `figures/rmdb_age_mirage/Figure3_caption.md` 中的已锁定版本。

### Figure 4 | Reliability is measurable, and its gains are bounded

**图的论点：** 不确定性建模带来的是小而透明的可靠性收益，而不是被夸大的临床突破。

**面板：** A E8A vs E8B；B H0 vs H2 的 MAE/RMSE；C 跨 25 outer folds 的方向；D coverage-risk；E 重复性；F 负对照。

**Caption draft：** *Figure 4 | Reliability is measurable, and its gains are bounded. a, Paired bootstrap comparison of raw-mass and double-orthogonal representations. b, Mean-head and nested-fusion estimates are compared for MAE and RMSE. c, Fold-level direction of change across repeated outer folds. d, Selective prediction curves describe error at prespecified coverage levels. e, Repeatability is assessed using repeat images and Bland-Altman analysis. f, Label permutation and random eye-pairing provide falsification controls. Effects are described as improvements only where the paired 95% confidence interval excludes zero.*

### Figure 5 | Cross-dataset transport is a phenotype audit, not external cIMT validation

**图的论点：** 外部图像先回答表型是否可迁移，而不是假装已证明临床效能。

**面板：** A RAV 真实 RGB/真值/预测；B Fundus-AVSeg 真实 RGB/真值/预测；C Dice/IoU/disc success；D phenotype drift；E overlap weights。

**Caption draft：** *Figure 5 | Cross-dataset transport audits phenotype availability and failure modes. a,b, Real RAV and Fundus-AVSeg images with reference annotations and RMDB-derived overlays. c, Anatomical overlap, disc-detection success, and finite-output rates. d, Phenotype shift and correlation drift across domains. e, Quality-overlap weighting used for transport diagnostics. RAV and Fundus-AVSeg are external anatomical datasets; neither contains cIMT outcome confirmation and neither was used for model tuning.*

### Figure 6 | Failure cases are data, not exclusions

**图的论点：** 临床可信度首先来自知道模型何时不可信。

**面板：** 视盘回退、低 overlap、双眼差异、重复视图不稳定/近常数特征；每列为真实输入 + 真处理输出 + 门控决策。

**Caption draft：** *Figure 6 | Failure cases are data, not exclusions. Four representative conditions are shown: optic-disc fallback, low-overlap vascular appearance, inter-eye discordance, and repeat-view instability or near-constant features. For each condition, the original image, derived readouts, quality metadata, and patient-level handling decision are displayed. Flags indicate down-weighting or sensitivity-analysis status, not disease diagnosis.*

### Figure 7 | Evidence hierarchy and mechanism-proxy analyses

**图的论点：** 数据源能支持什么，就只说什么。

**面板：** A 证据层级；B mBRSET 高血压和无 DR；C 低事件探索性终点；D concluding evidence boundary。

**Caption draft：** *Figure 7 | Evidence hierarchy and mechanism-proxy analyses. a, The study separates internal cIMT outcome development, external anatomical transport, and mBRSET mechanism-proxy analyses. b, Patient-level mBRSET results for systemic hypertension and the no-diabetic-retinopathy subgroup. c, Exploratory analyses for vascular disease, diabetic foot, and acute myocardial infarction, with event counts shown. d, The evidence supports phenotype audit and bounded mechanism-proxy inference; independent high-resolution cIMT confirmation remains outstanding.*

## 主表与图著

### Table 1 | Cohort, label, and evidentiary role

列：cohort、patients、eyes/images、resolution、label、analysis role、used for tuning?、supported inference、not supported inference。

### Table 2 | The age-proxy audit of internal cIMT modeling

列块 1：raw Task A；列块 2：Task B age-discordant deviation；只在同一任务内比较模型。

### Table 3 | Reliability, uncertainty, and falsification analyses

E8/E11 paired CI、coverage、repeatability、permutation、random-eye pairing。

### Table 4 | External phenotype transport audit

RAV/Fundus-AVSeg/mBRSET 的样本、分辨率、disc success、finite output、overlap/shift、可支持/不可支持结论。

### Table 5 | mBRSET mechanism-proxy analyses

各终点 n、events、M0/M1/M2/M3 的 AUROC/AUPRC/Brier、paired 95% CI、exploratory note。

## 统一视觉系统

| 语义 | 颜色 | 仅用于 |
|---|---|---|
| 传统 raw task / age context | navy and slate | Fig. 1-2 对照框架 |
| age-concordant / retained quality | teal | 正常预期、可保留观测 |
| age-discordant / contrast | warm red | 年龄异常偏高、对比对象，不等于诊断 |
| structure readout | orange | 动静脉/拓扑特征 |
| uncertainty / quality gating | purple | 降权、回退、风险提示 |
| evidence boundary | gray | 数据角色和不可支持结论 |

所有主图：白色背景、Arial/Helvetica 类字体、标题至少 28 pt、面板标题至少 18 pt、说明文字至少 13 pt、无交叉箭头、无重叠模块、无网络下载图片、无 AI 生成眼底图。
