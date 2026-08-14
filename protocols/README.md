# CIMT 双眼眼底预测基线

本目录是本研究自主编写的可复现实验基线，不复用原数据集仓库的训练代码。

## 固定实验约定

- **数据划分**：严格使用 `data_info.json` 的患者级 `group` 字段（1/2/3 对应 train/validation/test）。同一受试者的双眼永不跨集合。
- **主要终点**：`label`，即 CIMT 增厚（`thickness >= 0.9 mm`）。
- **次要终点**：连续 `thickness`（毫米）。
- **模型选择**：只依据 validation 集；test 集仅在最终模型确定后评估一次。
- **报告**：分类报告 AUROC、AUPRC、敏感度、特异度、F1、Brier；回归报告 MAE、RMSE、R²，并使用患者级 bootstrap 置信区间。

## 运行顺序

```bash
python scripts/audit_dataset.py
python scripts/train_clinical.py
python scripts/train.py --mode bilateral --backbone vit_small_patch14_dinov2.lvd142m --image-size 384 --freeze-encoder-epochs 3
python scripts/train.py --mode multimodal --backbone vit_small_patch14_dinov2.lvd142m --image-size 384 --freeze-encoder-epochs 3
```

第一次运行影像模型时需要下载公开的 DINOv2 权重。筛查阶段用 384×384 且先冻结编码器三轮；确认增益后再以 518×518 全量微调。若网络或权重不可用，先以 `resnet18` 完成管线验证。

## 基线定义

1. `clinical`：年龄、性别的逻辑回归/岭回归。
2. `single-eye`：单眼共享视觉编码器；推理时左右眼概率平均。
3. `bilateral`：左右眼共享视觉编码器，拼接双眼表征。
4. `multimodal`：双眼表征加训练集尺度的年龄、性别；不得对单个受试者的年龄和性别做样本内归一化。

后续血管分割、图拓扑和原型记忆模型都必须与这四个基线在相同划分、相同指标上比较。

## 每次正式运行必须输出

- `history.json`：每一 epoch 的验证集 AUROC、AUPRC、MAE、RMSE、R²及冻结状态。
- `best.pt`、`config.json`：最佳验证权重和完整可复现配置。
- `validation_report/`：患者级预测表、1000 次 bootstrap 95% CI、阈值、校准结果、年龄/性别亚组表现，以及 ROC、PR、校准、回归散点图。
- `test_report/`：仅在模型选择结束后生成；阈值固定为验证集 Youden 阈值，绝不在测试集调阈值。
