# RMDB 现有证据到论文图表映射表

本文当前不再以“等待独立 cIMT 队列”为主线，而以现有可审计结果构成方法学论文。下表是结果文件到主图/主表的固定映射，后续撰写不得用未完成的外部临床确认替换这些证据。

## A. 主要结果文件

| 证据层 | 文件 | 可支持的结果 | 主图/主表 |
|---|---|---|---|
| 内部患者级 nested CV | `artifacts/cimt_dual_readout_development/outer_cv/metrics.json` | E0–E6 特征族、2603 患者、5×3 nested CV、双眼患者级聚合 | Fig. 3；Table 2 |
| 年龄/性别正交化 | `artifacts/cimt_dual_readout_development/normative_e7/metrics.json` | residual/z 目标与双眼 common/discordance 特征 | Fig. 3；Supplementary Table 1 |
| 双重正交 | `artifacts/cimt_dual_readout_development/e8_double_orthogonal/metrics.json` | 5 seeds、25 outer folds、raw vs double-orthogonal/low-rank | Fig. 4；Table 3 |
| 双估计头不确定性 | `artifacts/e11_dual_head_full/metrics.json` | nested fusion 的 MAE、fold direction、paired bootstrap、coverage | Fig. 4/6；Table 3/5 |
| 重复性 | `artifacts/manuscript_completion/02_repeatability_extended/repeatability_extended.csv` | 重复图像/重复提取稳定性和 Bland–Altman | Fig. 6；Supplementary Table 2 |
| 负对照 | `artifacts/manuscript_completion/03_negative_controls/negative_control_summary.json` | 标签置换、随机双眼配对、特征残差负对照 | Fig. 4；Supplementary Fig. 3 |
| 校准与实用性 | `artifacts/manuscript_completion/04_calibration_utility/calibration_metrics.csv`、`decision_curves.csv` | OOF calibration、Brier、decision curve | Fig. 3；Supplementary Fig. 4 |
| 队列与模型证据表 | `artifacts/manuscript_completion/05_evidence_tables/` | participant flow、cohort characteristics、fair model comparison | Table 1/2 |
| 外部表型迁移 | `artifacts/external_phenotype_transport/metadata.json` 及同目录 CSV | RAV/Fundus-AVSeg 的特征漂移、域判别和相关结构 | Fig. 5；Table 4 |
| 质量—重叠加权迁移 | `artifacts/quality_overlap_transport/metadata.json` 及同目录 CSV | 质量分层、overlap weighting、不确定性门控 | Fig. 5/6；Table 4/5 |
| mBRSET 高血压代理 | `artifacts/mbrset_external/cv_hypertension/metrics.json` | 1276 患者、912 事件；clinical-only vs ocular/vascular/full 代理结果 | Fig. 7；Supplementary Table 4 |
| mBRSET 无 DR | `artifacts/mbrset_external/cv_hypertension_no_dr/metrics.json` | 882 患者、628 事件；机制结果敏感性分析 | Fig. 7；Table 5 |
| mBRSET 探索性结果 | `artifacts/mbrset_external/cv_vascular_disease/metrics.json`、`cv_diabetic_foot/metrics.json`、`cv_acute_myocardial_infarction/metrics.json` | 低事件率/异质性代理终点，明确 exploratory | Fig. 7；Supplementary Table 5 |

## B. 可直接写入结果段的关键数值

### 内部 cIMT 建模

- E8 双重正交：MAE `0.10960 ± 0.00008 mm`，R² `0.37581 ± 0.00038`；AUROC `0.54180 ± 0.00741`，AUPRC `0.27768 ± 0.00486`。
- E8B 相对 E8A 的 MAE paired bootstrap 差异为 `−0.000186 mm`，95% CI `−0.000307` 至 `−0.000064`。
- E11 nested fusion 相对均值头的 MAE差异为 `−0.001381 mm`，95% CI `−0.001859` 至 `−0.000898`；但 RMSE 差异 CI 跨 0，因此只声称 MAE 改善，不声称所有误差指标均改善。

### mBRSET 机制代理

- 高血压：M0 clinical AUROC `0.6599`，M1 clinical+ocular `0.6657`；M1 相对 M0 的 AUROC paired CI 跨 0，Brier 改善 CI 不跨 0。M2/M3 血管读出没有显示稳定增量，且总体 M3 相对 M0 的 AUROC 下降。
- 无 DR 高血压：M0 AUROC `0.6640`，M1 `0.6679`；血管读出增量 CI 多数跨 0，作为敏感性分析，不做强结论。
- vascular_disease、diabetic_foot、acute_myocardial_infarction 的事件数分别为 216、173、98，全部标记为探索性；这些结果用于展示代理终点异质性和失败模式，不作为临床有效性证据。

## C. 主图制作规则

1. Fig. 1 和 Fig. 2 不使用相同输入图。Fig. 1 展示真实队列和数据角色；Fig. 2 展示真实 RGB、软掩膜、occupancy、视盘回退和双眼聚合。
2. 所有外部图像来自项目本地 `data/external/RAV`、`data/external/Fundus-AVSeg` 或 `mBRSET_external/anatomy`；不使用网络示意图冒充数据。
3. 图中颜色语义固定：青色=质量读出，橙色=结构/拓扑读出，紫色=不确定性/降权，灰色=数据角色或不能支持的结论。
4. 每个外部面板都放置灰色注释：“anatomy transport”或“mechanism proxy—not independent cIMT confirmation”。

## D. 不能写进主结论的内容

- 不能写“模型已在独立 cIMT 外部队列验证”。
- 不能把 mBRSET 的 224 px 低分辨率和系统性标签称为 cIMT 验证。
- 不能把 RAV/Fundus-AVSeg 的 vessel Dice/IoU 当成临床预测性能。
- 不能省略早期临床基线实验曾访问 test artifact 的事实；正确披露见 `artifacts/manuscript_completion/01_access_audit/access_audit.json`。
