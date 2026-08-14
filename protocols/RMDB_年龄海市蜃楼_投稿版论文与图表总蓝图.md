# RMDB 投稿版总蓝图：从“年龄海市蜃楼”到可靠视网膜血管表型

## A. 稿件定位与写作规则

### A.1 文章类型

这不是一篇以最高 AUROC 为目标的普通眼底预测论文，而是一篇**生物标志物有效性审计 + 可靠表型方法学**论文。

核心临床问题是：

> 对于“cIMT 比同年龄、同性别预期更高”的人，眼底图像中是否存在可靠、可迁移、超越年龄代理的微血管信号？

### A.2 中心命题

> A retinal model can appear highly accurate for cIMT because both the image and cIMT encode chronological age. The unmet problem is to identify vascular aging that is discordant with chronological age.

中文中心句：

> 眼底模型在原始 cIMT 任务中的高性能，可能来自年龄这一共同驱动因素；真正尚未解决的问题，是识别“血管年龄超过实际年龄”的个体。

### A.3 三条不允许模糊的边界

1. 本文不声称已完成独立 cIMT 临床确认性验证。
2. RAV/Fundus-AVSeg 只验证解剖表型迁移，不验证 cIMT 临床效能。
3. mBRSET 只验证机制代理与失败模式，不是 cIMT 外部验证。

### A.4 VOCT 风格借鉴原则

借鉴 `VOCT_1.5_hidden_context_reframed.pdf` 的形式语言，而不是其内容：

- 单一、清晰的隐藏问题贯穿标题、摘要、图 1、结果和讨论；
- Methods 使用编号层级，先定义数据和评价边界，再解释核心模块；
- Results and Discussion 连续推进，每个小节回答一个明确问题；
- 每张图均先给出一个论点，再展示为该论点服务的面板；
- 量化结果与限制在同一段落出现，不把限制推迟到文末；
- 图注独立可读，明确数据来源、单位、样本量、统计检验和不能支持的推断。

## B. 题目、摘要与摘要图

### B.1 推荐题目

**主标题：**

*Beyond the Age Mirage: A Patient-Level Audit of Retinal Microvascular Phenotypes for Age-Discordant Carotid Intima-Media Thickness*

**中文工作标题：**

*超越年龄海市蜃楼：面向年龄不匹配颈动脉内膜中层厚度的患者级视网膜微血管表型审计*

### B.2 Running title

*The age-proxy paradox in retinal cIMT modeling*

### B.3 摘要的五句结构（不在摘要中堆模型名）

1. **背景：** cIMT 与眼底血管特征均强烈受年龄影响，使传统图像到 cIMT 预测难以区分病理信号与年龄代理。
2. **问题：** 临床更重要的是检测相对于年龄/性别预期异常偏高的 cIMT，即 accelerated vascular aging。
3. **方法：** 在 2,603 名患者中，构建年龄/性别条件化 cIMT 偏离目标，并用质量门控的 mass 与 structure 双读出、双眼不一致性和患者级 nested CV 进行审计；随后进行标签盲跨域表型迁移。
4. **发现：** 原始任务中临床年龄/性别基线已表现强，而额外血管特征不能稳定增加区分能力；在年龄条件化目标中，任何剩余信号都较弱且高度依赖测量质量与域重叠。
5. **结论：** 视网膜系统性血管 AI 应先证明超越年龄代理的可靠表型，再主张临床生物标志物价值。

### B.4 Graphical abstract

只用一张横向图，分为三部分：

```text
传统任务              隐藏问题                  RMDB 重新定义任务
眼底 → 高/低 cIMT      年龄同时影响眼底和 cIMT     眼底 → 年龄条件化 cIMT 偏离
高性能可能是年龄代理    “高 cIMT”不等于早发异常      + 质量/双眼/跨域审计
```

左侧和右侧必须用不同的真实受试者眼底图；中心仅画年龄—cIMT—图像的因果示意，不使用卡通血管。

## C. 正文大纲（按 VOCT 的编号和节奏）

## 1. Introduction

### 1.1 The attractive but incomplete promise of retinal vascular AI

从临床可及性开始：眼底摄影可规模化，cIMT 超声难规模化。提出公众和临床真正想要的是识别早期、无症状的血管异常。

### 1.2 The hidden age-proxy problem

直接提出全文冲突：年龄使 cIMT 增厚，也改变眼底外观和血管形态。若原始 cIMT 标签不条件化，模型可能学到年龄而不是异常动脉壁改变。

### 1.3 Why more retinal vascular detail may worsen validity

把血管表型定义为一条测量链，而非一个 feature vector：图像质量、分割概率、视盘定位、左右眼一致性、设备/域偏移都会造成伪信号。说明这也是公共外部数据普遍缺少同步 cIMT 的根本困难。

### 1.4 Study objective and contribution

用一段清楚列出四项贡献：

1. 年龄/性别条件化 cIMT 偏离目标，明确区分 cIMT 水平与异常血管老化；
2. RMDB 双读出：soft mass + structural topology；
3. 双眼一致性、测量不确定性和质量门控；
4. 内部患者级临床审计 + 标签盲外部表型迁移 + 机制代理验证。

最后一句必须声明：本文审计候选生物标志物有效性，而非声称完成临床替代性诊断。

## 2. Methods

### 2.1 Study design, data roles, and locked analysis boundary

先列队列角色表：

- China-Fundus-CIMT train：内部结局开发，2,603 患者/5,206 眼；
- RAV：外部解剖迁移；
- Fundus-AVSeg：外部低重叠域迁移；
- mBRSET：224 px 机制代理；
- FIVES/视盘组件：模块 QC。

单独写清 early clinical baseline 曾访问 test artifact 的事实；锁定双读出开发、模型选择和主要迁移分析不使用 test 调参。

### 2.2 From raw cIMT to age-discordant vascular aging

定义两套任务，且绝不混合报告：

- **Task A - raw cIMT level:** 描述传统、年龄主导的表观高性能；
- **Task B - age-discordant cIMT deviation:** 主要科学任务，基于年龄/性别期望 cIMT 的 residual 或 z-score；
- **Task C - accelerated vascular aging:** 根据预先定义阈值二分类，用于补充的临床可解释性。

明确：Task A 与 Task B 的 AUROC 不可横向比较，也不使用 Task A 的高 AUROC 为 Task B 背书。

### 2.3 Anatomical preprocessing and measurement provenance

描述真实 RGB 预处理、视盘定位、VascX logits、occupancy 概率、文件完整性、有限值和视盘回退。每只眼均保留 provenance 字段：图像 ID、来源域、视盘回退、有效像素、预测置信度。

### 2.4 RMDB dual-readout phenotype

#### 2.4.1 Soft vessel-mass readout

从概率图提取血管总量、动静脉软质量、Zone B 软质量和连续性。强调它表达的是“不确定性下的血管量”，不是硬阈值分割面积。

#### 2.4.2 Structural/topological readout

提取动静脉比、骨架长度、分支/端点密度、交叉、连通性及视盘几何关系。强调它表达的是“结构关系”。

#### 2.4.3 Bilateral phenotype construction

对每个读出保留 bilateral mean、absolute difference 和 within-eye SD。把它们分别解释为 common phenotype、inter-eye discordance 和 repeat-view instability。

### 2.5 Quality-gated and uncertainty-aware patient aggregation

定义每只眼的质量权重：视盘状态、soft support、occupancy/VascX 一致性和图像域可用性。质量门控只能降低可疑观测的影响，不能把低质量图像重新解释为病理。

### 2.6 Internal patient-level evaluation

5-fold outer / 3-fold inner nested CV；所有分割按患者；模型族 E0-E6 与 E7-E11 目标、特征定义和用途单独列出。报告 OOF MAE、R²、AUROC、AUPRC、Brier、calibration 和 paired bootstrap。

### 2.7 Falsification, repeatability, and cross-domain transport

三个预先规定的审计：

1. 标签置换和随机双眼配对负对照；
2. 重复性和 Bland-Altman；
3. RAV/Fundus-AVSeg 的质量、overlap、漂移和域判别；mBRSET 的机制代理分析。

### 2.8 Statistical analysis and interpretation rules

明确只有 paired bootstrap CI 不跨 0 才称“支持增量”；所有 mBRSET 低事件终点标记 exploratory；外部结果不参与调参。

## 3. Results and Discussion

仿照 VOCT，将 Results 与 Discussion 连续组织。每节都先给一个结论句，再给数字和边界。

### 3.1 The apparent signal in raw cIMT is dominated by age

**首句：** 原始 cIMT 风险任务的高区分度并不等价于对年龄异常血管老化的识别。

展示 clinical-only E0 对 raw Task A 的表现，以及 dual-readout E4 没有稳定优于 E0。再切换到 Task B，展示表现显著下降。这是全稿最重要的“证据反转”。

### 3.2 When the target becomes age-discordant cIMT, the residual signal is weak and measurement-sensitive

展示 E7/E8。语气要精确：不是“模型失败”，而是“在剥离年龄后，候选视网膜信号较弱；这正说明常规 raw cIMT benchmark 不能单独证明生物标志物价值”。

### 3.3 RMDB separates biological commonality from measurement discordance

展示真实双眼图像、soft mass、结构读出、左右眼差异、视盘回退和质量权重。说明 RMDB 不把所有不一致都说成病理。

### 3.4 Quality-gated dual readout provides a small but reproducible error improvement, with bounded benefit

报告 E8B 相对 E8A 的 MAE 差异，及 E11 nested fusion 对均值头的 MAE 差异；同时报告 RMSE CI 跨 0，防止过度叙述。强调这是 reliability improvement，不是临床效能突破。

### 3.5 Transportability is a phenotype property, not a post hoc validation label

RAV 的高重叠证明高质量外部域下读出可计算；Fundus-AVSeg 的低 overlap 暴露标注/图像域差异；mBRSET 视盘回退、低分辨率和重复视图证明“迁移”不能只汇报一个总 AUC。

### 3.6 Mechanism-proxy analyses do not support a universal systemic-risk classifier

展示 mBRSET：高血压中 ocular 信息的 Brier 有小改善，但 vascular/full 读出没有稳定增量；无 DR、vascular disease、diabetic foot、AMI 的异质性结果全部说明不可泛化为系统性风险通用分类器。

### 3.7 Implications: the endpoint must be more specific than the model

将全文升华为方法学结论：未来论文应优先报告年龄条件化目标、clinical-only 参照、配对增量、双眼审计、质量门控和跨域特征可用性，而非只报告 raw cIMT AUC。

## 4. Conclusion

三句话：

1. raw cIMT 预测容易被年龄代理夸大；
2. RMDB 提供将血管特征、测量质量和双眼不确定性分离的框架；
3. 独立高分辨率 cIMT 队列仍是临床确认的必要下一步。

## D. 主图重构：每张图只负责一个“认知转折”

### Figure 1. The age mirage: why raw cIMT prediction is not the clinical question

**唯一论点：** 高 cIMT 并不自动等于“异常早发血管老化”。

| 面板 | 内容 | 真实数据要求 |
|---|---|---|
| A | 年龄、原始 cIMT、眼底形态的共同变化示意 | 仅简洁因果图，不用卡通眼底 |
| B | 年龄 vs cIMT 散点；标出年龄条件化 expected curve 和 deviation | China-Fundus-CIMT 真值 |
| C | 两个年龄相近、cIMT 明显不同的真实双眼样例 | 同年龄同性别匹配，匿名、各用不同左右眼 |
| D | 两个 cIMT 都高、但年龄不同的真实样例 | 说明 raw high cIMT 的混淆 |
| E | Task A 与 Task B 的问题定义 | 大字文本，临床语言 |

**视觉：** 黑/深灰为传统任务，深红为风险偏高，湖蓝为年龄条件化新任务。主标题 28-32 pt，面板标题 18-20 pt，灰色说明 13-14 pt。

### Figure 2. The performance reversal after removing the age proxy

**唯一论点：** raw Task A 的表观高性能主要由 clinical age/sex 基线解释；Task B 才是严格检验。

| 面板 | 内容 |
|---|---|
| A | E0 clinical、E1-E6 在 raw Task A 的 grouped point/CI plot |
| B | clinical-only 与 dual-readout 的 paired bootstrap 差异森林图 |
| C | Task A 到 Task B 的性能“落差图”，严禁共享 y 轴造成误导 |
| D | clinical-only、mass、structure、dual 在 Task B 的表现 |
| E | 一句大字结论：“High raw-cIMT discrimination did not establish age-discordant vascular signal.” |

**视觉：** 与 Fig. 1 完全不同。白底、石墨灰柱、橙色强调双读出、紫色强调 age-discordant task。不要用眼底图。

### Figure 3. RMDB turns an image into an auditable patient-level phenotype

**唯一论点：** RMDB 的创新是测量链审计，而不是网络复杂度。

| 面板 | 内容 | 真实数据要求 |
|---|---|---|
| A | 一名患者左右眼的不同原始 RGB | China-Fundus-CIMT 真图，不能复用 Fig. 1 样例 |
| B | 每只眼对应 soft vessel mass、occupancy、VascX A/V overlay | 真预测输出 |
| C | 结构读出：骨架、动静脉、Zone B、视盘关系 | 真输出；失败则标回退 |
| D | bilateral mean / absolute difference / within-eye SD | 用同一真实患者的数值举例 |
| E | quality gate：图像质量、视盘回退、分支不一致进入患者表型 | 真权重或真实 QA 字段 |

**视觉：** 青色只属于 mass；橙色只属于 structure；紫色只属于 uncertainty；灰色只属于 provenance。字体最小不低于 13 pt。

### Figure 4. Reliability is measurable: uncertainty, repeatability, and bounded improvement

**唯一论点：** 当把不确定性作为测量变量处理，收益是小而可审计的，而不是夸大的临床跃迁。

| 面板 | 内容 |
|---|---|
| A | E8A vs E8B MAE paired bootstrap forest plot |
| B | H0 mean vs H2 nested fusion MAE 和 RMSE 双指标对照 |
| C | 25 outer-fold 改善方向条形/蜂群图 |
| D | coverage-risk 曲线 |
| E | repeatability ICC/Bland-Altman 小面板 |
| F | 标签置换、随机双眼配对负对照 |

**视觉：** 深蓝和浅灰为统计底色，绿色只表示“CI 支持的改善”，红色只表示“CI 不支持/失败”。

### Figure 5. Cross-dataset transport reveals where the phenotype survives and where it breaks

**唯一论点：** 外部验证不应只有一个总分数；表型迁移需要报告域重叠与失败位置。

| 面板 | 内容 | 真实数据要求 |
|---|---|---|
| A | RAV 原图、真值 mask、预测 overlay | RAV 真图和标注 |
| B | Fundus-AVSeg 原图、真值、预测 overlay | Fundus-AVSeg 真图和标注；不能复用 RAV 图 |
| C | RAV/Fundus-AVSeg Dice/IoU、disc success、finite rate | 真审计结果 |
| D | phenotype shift / correlation drift / domain discrimination | 已有 transport CSV |
| E | 质量—overlap 权重分布 | 已有 overlap weights |

每个外部面板下放灰色大字：

- RAV: `External anatomy transport`
- Fundus-AVSeg: `Low-overlap transport stress test`
- `Neither panel is external cIMT outcome confirmation`

### Figure 6. Failure cases are data, not exclusions

**唯一论点：** 可靠性框架的临床价值首先是识别“何时不该相信模型”。

四列真实病例，每列都展示 RGB、soft mask、结构 mask、质量字段和患者级处理决定：

1. 视盘定位回退；
2. 低对比度/低 overlap；
3. 双眼显著不一致；
4. 重复视图不稳定或近常数特征。

底部只写两种状态：`retained with down-weighting` / `flagged for sensitivity analysis`，避免把算法标记为临床诊断。

### Figure 7. What the external evidence does - and does not - establish

**唯一论点：** 证据等级必须与结论匹配。

| 层级 | 数据 | 可支持结论 | 不可支持结论 |
|---|---|---|---|
| 1 | China-Fundus-CIMT | 内部患者级方法学关联 | 独立临床确认 |
| 2 | RAV/Fundus-AVSeg | 解剖表型迁移与域偏移审计 | cIMT 临床预测 |
| 3 | mBRSET | 机制代理、低分辨率/质量敏感性 | 通用系统性风险分类 |
| 4 | future independent cIMT cohort | 独立临床确认 | 当前未完成 |

右侧加入 mBRSET 代理终点的森林图；明确显示高血压、无 DR、vascular disease、diabetic foot、AMI 的结果及其探索性标签。

## E. 主表与补充材料重构

### Table 1. Cohort, label, and evidentiary role

将样本数、患者数、眼数、分辨率、标签、是否参与调参、可支持的结论并列。这个表必须放在正文前半部分，避免读者误把所有外部数据当 clinical external validation。

### Table 2. The age-proxy audit

行：clinical-only、legacy、mass、structure、dual、dual without Zone B、dual without uncertainty。

列分为两个 block：

- Raw cIMT task：MAE、R²、AUROC、AUPRC、Brier；
- Age-discordant task：MAE deviation、AUROC、AUPRC、Brier、paired Δ。

### Table 3. Reliability and falsification audit

E8/E11 paired bootstrap、25-fold direction、coverage-risk、repeatability、label permutation、random eye-pairing。

### Table 4. Cross-domain phenotype transport audit

RAV、Fundus-AVSeg、mBRSET：分辨率、患者/图像、视盘成功、finite rate、Dice/IoU（如可用）、drift、质量/overlap 状态、可支持结论。

### Table 5. External mechanism-proxy analyses

mBRSET 各终点的 n、events、M0/M1/M2/M3 AUROC、AUPRC、Brier、paired CI、探索性说明。

### Supplementary figures

- S1: cohort flow and file-completeness audit；
- S2: all phenotype feature distributions and constant-feature audit；
- S3: age and sex balance before/after cIMT-deviation construction；
- S4: all calibration curves / decision curves；
- S5: full paired-bootstrap forests；
- S6: external domain shift and overlap-weight diagnostics；
- S7: additional failure examples；
- S8: implementation/reproducibility flow chart。

## F. 图表制作纪律

1. 所有眼底图均来自项目本地真实数据与真实处理结果；不使用网络图片或生成式眼底替代真实证据。
2. 同一张真实输入图最多在一张主图中出现一次；Fig. 1、Fig. 3、Fig. 5、Fig. 6 的原图样例必须不同。
3. Fig. 1 是临床问题图；Fig. 3 是技术测量链图；两图禁止复用布局、配色、输入样例或标题结构。
4. 正文主图不低于 300 dpi；所有正文字体 13 pt 以上，面板标题 18 pt 以上，图的总标题 28 pt 以上。
5. 灰色文字不是脚注残渣，而是“证据角色标签”；字号至少为主图正文的 80%。
6. 统计图由代码精确生成；真实图像面板采用原始 RGB + 真预测 overlay；概念箭头仅补充关系，不替代数据。
7. 每个图注都写样本量、患者级或眼级单位、数据集角色、统计方法和限制。

## G. 摘要、引言、结果中的高频句式

### 可以使用

- “Raw cIMT discrimination did not establish signal beyond age and sex.”
- “We therefore reframed the task as age-discordant cIMT deviation.”
- “RMDB treats retinal vascular phenotyping as a measurement and transport problem before treating it as a prediction problem.”
- “External anatomical datasets were used label-blind to audit phenotype transport, not to tune the model.”
- “The improvement was small and bounded; paired uncertainty intervals are reported throughout.”

### 禁止使用

- “The model predicts systemic vascular disease from fundus images.”
- “External validation confirmed cIMT prediction.”
- “RMDB outperformed all baselines” （除非所有预注册主要指标和 CI 均支持）。
- “Bilateral asymmetry indicates disease” （只能说是待解释的表型或测量不一致）。

## H. 最终读者体验

读者读完应得到的不是“又一个模型”，而是这个判断：

> 原来我们一直把一个年龄驱动、质量敏感、跨域不稳定的预测问题，当成了已被解决的血管生物标志物问题。RMDB 的贡献，是把这个问题拆开，让真正可验证的部分重新变得可见。

