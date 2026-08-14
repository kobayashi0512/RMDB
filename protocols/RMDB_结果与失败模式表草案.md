# RMDB 结果与失败模式表草案

本文件是主文结果段和补充材料的写作底稿。数值均来自已存在的 JSON/CSV，不在此处重新调参。

## Table 1. 数据集角色与审计状态

| 队列 | 患者/图像 | 标签 | 分辨率/协议 | 用途 | 状态 |
|---|---:|---|---|---|---|
| China-Fundus-CIMT train | 2,603 / 5,206 | cIMT | 内部队列 | 结局开发、患者级 nested CV | 完成 |
| China-Fundus-CIMT frozen validation artifact | 200 | cIMT | 冻结预测 | 描述性/复现检查 | 已存在，不能称 pristine unopened |
| RAV | 206 / 206 | A/V mask | 外部公开 | 解剖读出迁移 | 完成 |
| Fundus-AVSeg | 100 / 100 | A/V annotation | 外部公开 | 低重叠域迁移 | 完成 |
| mBRSET mirror | 1,287 / 4,884（2,523 patient-eye rows） | hypertension 等代理标签 | 224 px | 机制代理、失败模式 | 完成；非 cIMT 确认 |
| FIVES/视盘组件 | 组件级 | vessel/disc | 多协议 | occupancy、视盘 QC | 完成 |

## Table 2. 内部模型族比较

现有 `fair_model_comparison.csv` 提供 E0–E6 的固定比较；应在正文注明其与 E7–E11 正交化/不确定性实验的目标定义不同，不把不同目标的 AUROC 直接横向合并。

| 特征族 | MAE (mm) | RMSE (mm) | R² | AUROC | AUPRC | Brier |
|---|---:|---:|---:|---:|---:|---:|
| E0 clinical | 0.11456 | 0.14755 | 0.35362 | 0.85205 | 0.93348 | 0.15583 |
| E1 legacy VascX | 0.11450 | 0.14762 | 0.35297 | 0.84731 | 0.93013 | 0.15747 |
| E2 mass/UDCT | 0.11468 | 0.14800 | 0.34967 | 0.85001 | 0.93365 | 0.15652 |
| E3 factorized | 0.11457 | 0.14789 | 0.35064 | 0.84860 | 0.93278 | 0.15830 |
| E4 dual readout | 0.11544 | 0.14865 | 0.34394 | 0.84438 | 0.92799 | 0.15945 |
| E5 without Zone B | 0.11512 | 0.14790 | 0.35050 | 0.84694 | 0.93061 | 0.15799 |
| E6 without uncertainty | 0.11502 | 0.14803 | 0.34937 | 0.84569 | 0.93144 | 0.15822 |

## Table 3. 重点正交化与不确定性结果

| 实验 | 关键结果 | 解读 |
|---|---|---|
| E8A raw mass | MAE 0.10977 mm；R² 0.37564 | 原始质量读出基线 |
| E8B double orthogonal | MAE 0.10960 mm；R² 0.37581 | 相对 E8A 的 MAE paired CI 不跨 0，但效应很小 |
| E8C low-rank | MAE 0.10964 mm | 与 E8B 差异 CI 跨 0，不能声称低秩更优 |
| E11 nested fusion | MAE 0.10827 mm；25/25 folds improved/equal | MAE paired CI 不跨 0，RMSE CI 跨 0 |
| E11 coverage | 0.7/0.8/0.9/1.0 coverage 均有报告 | 作为 selective prediction 敏感性，不当作临床阈值 |

## Table 4. 外部解剖表型迁移

| 队列 | 视盘检测率 | complete core | 主要解剖结果 | 解释 |
|---|---:|---:|---|---|
| RAV | 1.000 | 1.000 | vessel Dice/IoU 约 0.8645/0.7701 | 高重叠外部域，支持表型迁移 |
| Fundus-AVSeg | 1.000 | 1.000 | vessel Dice/IoU 约 0.5901/0.4628 | 标注/风格偏移，暴露低重叠失败模式 |
| mBRSET | 0.9606 | 1.000 | 4,884 图；视盘回退和重复视图需单独报告 | 机制代理，不是 cIMT 外部确认 |

## Table 5. mBRSET 代理终点结果

| 终点 | 患者 | 事件 | M0 AUROC | M1 AUROC | M3 AUROC | 主要判断 |
|---|---:|---:|---:|---:|---:|---|
| systemic hypertension | 1,276 | 912 | 0.6599 | 0.6657 | 0.6172 | ocular 轻微、血管读出无稳定增量 |
| hypertension, no DR | 882 | 628 | 0.6640 | 0.6679 | 0.6427 | 敏感性分析，增量 CI 多数跨 0 |
| vascular disease | 1,268 | 216 | 0.5564 | 0.5239 | 0.4920 | 探索性，未支持增量 |
| diabetic foot | 1,260 | 173 | 0.6055 | 0.6139 | 0.5904 | 探索性，主要体现终点异质性 |
| acute myocardial infarction | 1,266 | 98 | 0.5719 | 0.5858 | 0.5242 | 低事件数探索性，不作临床结论 |

## 失败模式与自动修复登记

| 失败模式 | 影响 | 处理 | 正文位置 |
|---|---|---|---|
| 视盘定位回退 | mBRSET 189 例回退，影响几何读出 | 保留回退标志；做 reliable-core/strict-disc 敏感性 | Fig. 6；Table 5 |
| 低重叠外部域 | Fundus-AVSeg Dice/IoU 明显低于 RAV | 不调参；按 overlap 分层报告 | Fig. 5 |
| 常数/近常数特征 | 可能造成伪增量或退化 | 预先审计，删除/标记并记录 | Supplementary Fig. 2 |
| 左右眼不一致 | 简单平均会放大噪声 | 显式保留 mean、absolute difference、within-eye std 和 confidence | Fig. 2/6 |
| test artifact 早期访问 | 影响“未打开 test”的绝对表述 | 公开披露；锁定双读出开发未用 test 调参 | Methods limitation |
| 无独立 cIMT 外部队列 | 无法支持确认性临床结论 | 改为 transportability + mechanism proxy 论文 | Abstract/Discussion |

## 结果写作的安全句式

- “The dual-readout representation was internally evaluated with patient-level nested cross-validation and transported label-blind to public anatomical datasets.”
- “mBRSET analyses were prespecified as mechanism-proxy analyses and should not be interpreted as independent cIMT confirmation.”
- “The observed gain was small; confidence intervals and failure-mode analyses are reported to avoid overinterpretation.”
