# RMDB：面向颈动脉内膜中层厚度偏离的双读出视网膜微血管表型与跨域迁移

## 1. 论文定位

### 推荐题目

**中文：** 面向颈动脉内膜中层厚度偏离建模的双读出视网膜微血管表型：患者级不确定性建模与跨数据集迁移评估

**英文：** *A Dual-Readout Retinal Microvascular Phenotype for Carotid Intima–Media Thickness Deviation: Patient-Level Uncertainty Modeling and Cross-Dataset Transport Evaluation*

### 文章类型

这篇文章定位为“方法学 + 外部表型迁移 + 机制代理验证”，而不是独立临床确认性研究。核心贡献是提出一个可解释、可审计的视网膜微血管双读出，并证明其在不同成像域、不同分辨率和不同标注条件下的可迁移性。

### 主张边界

本文可以声称：

1. 在 China-Fundus-CIMT 内部队列中，双读出表型能够对年龄/性别校正后的 cIMT 偏离进行患者级建模。
2. 软血管质量读出和结构/拓扑读出是互补的，质量重叠与不确定性门控可改善跨域稳定性。
3. 在 RAV、Fundus-AVSeg 和 mBRSET 等非 cIMT 数据集中，模型的血管表型、质量控制和机制关联可以被独立审计。

本文不能声称：

1. 已经完成独立队列上的 cIMT 临床确认性验证。
2. 视网膜表型可替代超声 cIMT 或可直接用于临床筛查。
3. mBRSET 的 224 px 图像或其系统性标签等价于独立的 cIMT 外部验证。

数据集角色必须在正文和图 1 中明确区分：China-Fundus-CIMT 是结局开发与内部患者级验证；RAV/Fundus-AVSeg 是解剖表型迁移审计；mBRSET 是低分辨率机制/临床代理验证；FIVES 和视盘数据是组件质量与失败模式审计。

## 2. 核心创新点

### 创新点 1：双读出而非单一像素预测

从每只眼同时提取：

- **质量读出（mass/soft-vessel readout）**：软血管概率、血管占据率、局部覆盖与连续性；
- **结构读出（structure/topology readout）**：artery–vein 分离、主干/分支拓扑、左右眼不一致、视盘到血管质量的几何关系。

二者在患者级汇聚时分别保留均值、离散度和左右眼差异，而不是提前压缩成一个黑箱分数。

### 创新点 2：双眼一致性与不确定性进入表型本身

双眼不是简单平均。模型显式计算 common signal、inter-eye discordance 和 confidence-weighted aggregation。低质量视野或视盘回退会降低该眼的贡献，并保留回退标志用于敏感性分析。

### 创新点 3：质量—重叠加权的跨域迁移

跨域评估同时使用预测质量和标注重叠质量。RAV/Fundus-AVSeg 中报告 vessel Dice/IoU、视盘成功率、有限值率与不确定性分层，并比较未加权、质量加权和质量+不确定性门控三种汇聚方式。

### 创新点 4：目标是“年龄/性别校正后的 cIMT 偏离”

内部临床建模不把 cIMT 绝对值和年龄混为一谈，而是构造年龄/性别基线后的 residual/deviation target。这样可以检验视网膜微血管信号是否携带超出基础人口学风险的增量信息。

### 创新点 5：标签盲的跨域审计链

外部 RAV、Fundus-AVSeg 和 mBRSET 的迁移分析不用于重新调参。所有权重、阈值和读出定义在内部锁定后固定执行，并记录失败原因、视盘回退、常数特征、缺失率和异常值。

## 3. 数据与分析角色

| 数据/模块 | 样本角色 | 主要问题 | 允许的结论 |
|---|---|---|---|
| China-Fundus-CIMT | 内部结局开发与患者级 nested CV | cIMT 偏离建模、双读出增量 | 内部方法学效能 |
| RAV | 外部解剖表型迁移 | 血管分割与形态域偏移 | 解剖读出可迁移性 |
| Fundus-AVSeg | 外部解剖表型迁移 | 标注协议和图像风格差异 | 低重叠域的失败模式 |
| mBRSET | 外部机制/临床代理 | 224 px、系统性标签、图像协议差异 | 机制关联和可用性线索 |
| FIVES/视盘组件 | 组件质量控制 | occupancy、视盘定位、回退 | 子模块可靠性 |

## 4. 论文总体脉络

### Introduction

1. cIMT 是结构性血管表型，但临床超声不易规模化。
2. 视网膜微血管提供无创窗口，但现有工作常把图像、分割质量和临床标签混合在一起。
3. 本文提出 RMDB 双读出：质量读出 + 结构读出，以患者级双眼不确定性门控为核心。
4. 本文的验证重点是“内部结局建模 + 跨域表型迁移 + 机制代理”，不把未获得的独立 cIMT 队列包装成确认性证据。

### Methods

1. 队列和数据角色；
2. 解剖预处理与 VascX/occupancy 读出；
3. 双眼患者级聚合；
4. cIMT residual/deviation 目标构造；
5. E0–E6 预先锁定模型族与 nested CV；
6. 质量—重叠加权与不确定性门控；
7. 外部标签盲迁移审计；
8. 统计分析、bootstrap、校准和失败模式登记。

### Results

1. 数据流和锁定协议；
2. 内部 cIMT 偏离建模；
3. 双读出增量与消融；
4. 外部解剖表型迁移；
5. mBRSET 机制代理验证；
6. 失败模式、回退和不确定性敏感性。

### Discussion

重点讨论“表型可迁移性”和“临床确认性证据”的边界，明确独立高分辨率 cIMT 队列是下一阶段，而不是本稿隐含完成的结果。

## 5. 主图与主表蓝图

### Figure 1. Study design and data-role map

左侧展示患者/双眼输入和真实数据集图片；中间展示 VascX logits、occupancy、视盘定位和双读出聚合；右侧按颜色区分内部结局开发、解剖外部迁移和机制代理验证。图中用灰色小字标注“internal outcome development”“external anatomy transport”“mechanism proxy—not cIMT confirmation”。

### Figure 2. Dual-readout module

A：单眼真实 RGB、血管软掩膜、occupancy 和视盘回退示例；B：质量读出分支；C：结构/拓扑分支；D：双眼 common/discordance/confidence 门控；E：患者级向量和 residual cIMT 输出。质量读出和结构读出必须使用不同主色，避免图 1 与图 2 视觉同质化。

### Figure 3. Internal cIMT-deviation modeling

A：cIMT 绝对值到年龄/性别校正 residual 的构造；B：E0–E6 模型族；C：患者级 nested CV；D：OOF calibration、AUROC/AUPRC/Brier 与 decision-curve；E：配对 bootstrap 增量森林图。

### Figure 4. Incremental value and ablation

比较 clinical-only、clinical+mass、clinical+structure、clinical+dual、clinical+dual+uncertainty。展示 ΔAUROC、ΔAUPRC、ΔBrier、校准斜率和 bootstrap 95% CI。不要只展示点估计。

### Figure 5. Cross-dataset phenotype transport

RAV 和 Fundus-AVSeg 使用真实图像/真实预测叠加。展示 vessel Dice/IoU、有限值率、视盘失败率、质量分层和 domain shift。mBRSET 单独作为机制代理面板，不与 cIMT 确认性混色。

### Figure 6. Failure modes and uncertainty

四类真实案例：视盘回退、低重叠血管、左右眼不一致、近常数特征。每个案例展示输入、软掩膜、结构读出、质量权重和最终是否降权。

### Figure 7. Mechanism-proxy validation in mBRSET

展示血管表型与 systemic_hypertension 等标签的内部患者级分析、无 DR 亚组和低事件探索性结果。标题中明确“mechanism proxy / not independent cIMT confirmation”。

### Table 1. Cohort and data-role summary

人数、眼数、图像分辨率、标签类型、是否有 cIMT、是否用于调参、是否属于外部迁移。

### Table 2. Main internal performance

E0–E6 的 OOF AUROC、AUPRC、Brier、校准指标及 95% CI。

### Table 3. Incremental-value and ablation results

临床、单读出、双读出、双读出+不确定性，以及 paired bootstrap Δ 指标。

### Table 4. External transport and quality audit

RAV/Fundus-AVSeg/mBRSET 的样本量、Dice/IoU、视盘失败、有限值率、缺失率、质量分层差异。

### Table 5. Failure modes and sensitivity analyses

视盘回退 189 例、低重叠图像、常数特征、左右眼缺失、去除低质量图像后的结果变化。

## 6. Supplementary 图表

- Supplementary Fig. 1：完整数据处理队列和文件完整性。
- Supplementary Fig. 2：所有特征的分布、常数率和异常率。
- Supplementary Fig. 3：bootstrap 配对增量完整森林图。
- Supplementary Fig. 4：不同质量阈值与不确定性门控阈值的敏感性。
- Supplementary Fig. 5：外部域按图像风格/分辨率分层。
- Supplementary Table 1：逐特征定义和单位。
- Supplementary Table 2：所有失败样本及自动修复记录。
- Supplementary Table 3：早期临床基线实验对 test artifact 的访问披露。

## 7. 结果解读规则

1. 只有配对 bootstrap 的 95% CI 不跨 0，且方向一致，才称为“支持增量”；否则写“点估计提示但证据不足”。
2. 外部 RAV/Fundus-AVSeg 只能支持表型/解剖读出迁移，不能支持 cIMT 临床效能。
3. mBRSET 只能支持机制代理或临床相关性线索，不能写成外部 cIMT 验证。
4. 任何视盘回退、低重叠和内部 CV 限制都在摘要、结果和讨论中重复说明。
5. 早期临床 baseline 曾访问 test artifact；因此不得写“test 从未打开”。正确表述是：锁定双读出开发、模型选择和主要迁移分析未使用 test 进行调参，但早期基线实验访问过该 artifact。

## 8. 投稿定位

优先考虑医学影像/眼科 AI/生物医学工程方法学期刊。若内部性能和跨域迁移结果稳定，可定位为中等偏上的方法学期刊稿；在没有独立高分辨率 cIMT 队列前，不宜包装成临床确认性高影响论文。标题、摘要和 cover letter 都应使用“transportability、mechanistic proxy、internal patient-level validation”等措辞，避免“external clinical validation”。

## 9. 下一步执行顺序

1. 从现有结果文件生成 Table 1–5 的数值草稿；
2. 统一 Figure 1–7 的真实图像来源和颜色语义；
3. 完成结果段与限制段，确保每个主张可追溯到一个结果文件；
4. 运行一次完全独立的复现检查，不改变任何锁定权重或阈值；
5. 若未来获得独立 cIMT 队列，只追加确认性 Figure 8/表 6，不重写当前主结论。
