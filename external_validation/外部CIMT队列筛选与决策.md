# RMDB-C 外部 CIMT 队列筛选与决策

状态：2026-07-30 首轮可获取性审计完成  
原则：外部队列只做一次锁定评估；没有 CIMT 的眼底数据不得冒充外部结局验证。

## 1. 最终排序

| 优先级 | 队列 | 配对设计 | 预计可用规模 | 原始眼底图像 | CIMT | 当前判断 |
|---|---|---|---:|---|---|---|
| P1 | MESA Exam 5 | 同次检查的双眼、双视野眼底摄影 + 颈动脉超声 | 上限约 3429 人，实际交集待授权后联表 | 受控访问 | 有 | 主外部队列 |
| P2 | ARIC Visit 3 | 单眼 45° 眼底摄影 + CIMT | 文献分析集 8794 人 | 原始胶片已数字化，像素获取需单独确认 | 有 | 备用外部队列 |
| P3 | MESA Exam 2 + 邻近 CIMT | 双眼、双视野眼底摄影 + 非完全同期 CIMT | 眼底表约 5845 人 | 受控访问 | 有 | 时间差敏感性分析 |
| P4 | UK Biobank | 双眼眼底摄影 + CIMT/血管表型 | 大样本，具体交集需项目内查询 | 受控、付费/机构申请 | 有 | 第二独立人群，非近期主线 |

没有找到第二个可匿名直接下载、同时包含原始彩色眼底和患者级连续 CIMT
的开放数据集。BRSET、ODIR、Fundus-AVSeg 等可以验证测量层跨域性，但不能
验证 CIMT 结局。

## 2. 为什么选 MESA Exam 5

1. 同一检查轮次同时有眼底摄影和颈动脉 IMT，避免 Exam 2 与 Exam 1 之间的
   时间差。
2. MESA 官网列出的 Exam 5 可用量为：眼底摄影约 4350 人、US carotid IMT
   约 3429 人，因此患者级交集上限约 3429 人。
3. dbGaP 的 Exam 5 眼底表实际包含 4183 名受试者：
   - 右眼双视野完整 3959 人；
   - 左眼双视野完整 3958 人；
   - CRAE 3937 人；
   - CRVE 3967 人。
4. 人群包括 White、African-American、Hispanic 和 Chinese American，可同时
   检验跨族群和跨设备泛化。
5. 眼底协议为双眼、视盘中心 Field 1 与黄斑中心 Field 2，适合当前
   视盘标准化血管表型管线。

注意：以上人数来自公开组件表和 dbGaP 汇总，不是最终眼底-CIMT 联表人数。
只有获得受控数据后才能计算真实交集、缺失机制和纳入流程图。

## 3. 已实际完成的下载验证

已从 NCBI dbGaP 公共 FTP 成功下载并解析：

| 文件 | 大小 | SHA-256 |
|---|---:|---|
| `MESA_retinal_E2_data_dictionary.xml` | 70 KB | `e383d1db475fa9356fa5e3eb511f39db923e270b7fe28f54e61157a068b4935e` |
| `MESA_retinal_E2_variable_report.xml` | 365 KB | `80a144ad2561e59eac6fb3ac516f29f0adddebbeebc0139cae4f11caec5613bc` |
| `MESA_retinal_E5_data_dictionary.xml` | 74 KB | `385dd89ea5554754dd72c3010beb023e956cda22ce7ef68f6596146248bd133b` |
| `MESA_retinal_E5_variable_report.xml` | 375 KB | `1ea61084960003dc45bb24cbec65190be22e9f99e0a79cb9dc39f2ba3984b0bb` |

本地目录：
`source-data:/data/external/MESA_metadata`

公开 XML 下载可行；原始患者级表不能匿名下载，需要 dbGaP/BioLINCC 授权。
更重要的是，dbGaP distribution manifest 对 Exam 2/5 retinal photography
只列出 `data_dict.xml`、`var_report.xml` 和受控的 `HMB.txt.gz` 表，没有列出
JPEG/TIFF 等像素文件。BioLINCC 页面也明确列为 “Study Datasets Only”。
因此当前证据表明标准仓储申请主要提供表型表，不能假设批准后会自动得到原始
图像。端到端外部验证必须通过 MESA 合作路径单独申请归档的去标识眼底像素。

## 4. 两条并行获取路径

### 路径 A：MESA 合作申请（首选）

向 MESA Coordinating Center 提交研究/合作意向，明确请求：

- Exam 5 原始去标识眼底图像；
- 同期连续 CIMT 读数和质控变量；
- 年龄、性别、族群、中心、检查日期；
- 允许计算新的图像表型并发表外部验证结果。

该路径最有机会获得原始图像，也有利于正确解释不同 CIMT 扫描/读片协议。

### 路径 B：dbGaP/BioLINCC（并行）

- dbGaP 数据集：
  - Exam 2 `pht003376.v1.p3`
  - Exam 5 `pht003377.v1.p3`
- BioLINCC MESA accession：`HLB00640825a`

先申请患者级数据和已有 CRAE/CRVE。现有分发清单未显示像素文件，因此该路径
默认定位为：

1. 获得患者级 CIMT、CRAE/CRVE 和临床变量；
2. 复现“已有血管口径—CIMT”机制关系；
3. 为 MESA 合作路径提供样本量和联表可行性依据。

除非数据管理方书面确认并实际交付原始像素，否则不能声称完成 RMDB-C 端到端
外部验证。

## 5. 备用队列

### ARIC Visit 3

ARIC 文献报告，Visit 3 首次进行眼底摄影；排除无/不可分级图像、无 CIMT
及其他缺失后，已有 8794 人进入视网膜口径与系统因素分析。它的优点是样本大、
眼底和 CIMT 关联已有流行病学先验；缺点是单眼、胶片摄影、数字化年代久远，
且 BioLINCC 标准释放不保证包含像素。

只有在 ARIC 官方确认可提供去标识数字化眼底像素后，才进入 P2 执行。

### UK Biobank

已有 UK Biobank 项目把 retinal imaging 与 CIMT 联合用于心血管风险预测，
证明数据组合在库内存在。它适合后续做大样本第二外部验证，但申请成本、机构
资格和等待周期更高，不阻塞 MESA 主线。

## 6. 明确不做的事

- 不用只有高血压/糖尿病标签的眼底数据替代连续 CIMT 外部验证；
- 不把 MESA 已有 CRAE/CRVE 直接当作本模型自己从图像提取的表型；
- 不在 MESA 上重新选特征、阈值或模型；
- 不因外部队列 CIMT 分布不同而在全外部数据上重拟合预测头；
- 不在图像尚未确认可获得时承诺已完成端到端外部验证。
