# Changelog

## Article workflow — 2026-11-05

- 根据用户确认的新版 π0.7 文章重建默认：导语、四主题章节、总结。
- 同步入口、模板、阅读协议、机制指导、质量清单与界面提示，移除六部分强制约束。
- 原图独立裁切并图文穿插，保留原始图注与证据边界。
- 增加不依赖标题措辞的资产校验入口，旧六部分校验器保留兼容用途。

## Local workflow rebuild — 2026-11-05

- 重写 skill 入口与报告模板，把样本路径、核心改动和训练到推理的机制叙事设为默认。
- 保留六部分网站兼容外框与证据资产契约，移除正文固定标签模板。
- 更新质量清单与界面提示；明确旧校验器措辞误报的人工复核和披露要求，未改校验代码。
- 重读用户指定知乎文章，只参考组织方法，未复制正文或图片。

## Local narrative update — 2026-11-04

- 根据用户指定的知乎 pi0.7 解读及连续讲解反馈，增加 mechanism-narrative 参考。
- 强化问题—作者方案闭合、训练与推理对照、参数语义、问题驱动实验；保留一手来源核验。
- 本地修改涉及 SKILL.md、report-template、quality-checklist 和新增参考；未修改校验器或测试。

## 4.0.0 — 2026-08-15

- 恢复六部分论文解读结构作为默认 `explain` 契约：一句话总结、背景与动机、核心方法、实验与结果、贡献与影响、结论。
- 将单轴受众默认值改为双轴模型：零背景入口 `entry_level: novice` 与博士级技术上限 `technical_ceiling: doctoral`。
- 要求每个承重术语、缩写、指标和前置概念首次出现时先做白话解释，再给精确定义与类比边界。
- 要求至少一个最小例子在形式化细节之前走完整条核心机制。
- 将 `key: true` 视觉对象定义为 `explain` 与 `audit` 中必须进入报告的内容，取消原先 2–4 张的默认数量。
- 要求每个编号视觉对象填写 `classification_reason`，防止通过批量标记“非关键”规避覆盖。
- 新增图文邻接：每个关键图表附近必须有阅读指导、具体观察、观察到主张的推理桥，以及不能由该图推出的内容。
- 恢复实验设计、可靠性、贡献、影响和基于证据缺口的未来方向，同时不恢复 v2 的固定字段账本式正文。
- 将视觉 manifest 升级至 schema v4，将 source map 升级至 schema v5。
- 扩展确定性校验与单元测试，覆盖六部分结构、术语入门、贯穿例子、推理桥、关键视觉全覆盖、图文交错和分层读者元数据。
- 新增 `agents/openai.yaml`，用于 Codex 技能发现与界面展示。

## 3.0.0 — 2026-08-15

- Separated reading depth from delivery density with `brief`, `explain`, `audit`, and `targeted` modes.
- Made `explain` the default for both “解读” and “精读”: deep internal reading now produces a compact four-question explanation instead of a mandatory six-section audit.
- Required a worked minimal example before formal terminology and equations.
- Moved full visual ledgers, claim audits, reproduction details, and review checklists into optional audit appendices.
- Added understanding-driven visual selection through `selected_for_report`, `report_role`, and `selection_reason`; helpful figures and tables are included without a rigid count cap.
- Added mode-aware length budgets and validator checks for structure, examples, evidence grades, boundaries, visual selection, and source-map delivery consistency.
- Upgraded visual manifests to schema v3 and source maps to schema v4.

## 2.1.0 — 2026-08-01

- Added explicit `visual` and `text-only` execution routes for models without image understanding.
- Added `inventory --text-only`, which emits page text, per-visual text cards, body-reference contexts, and a text evidence ledger without rendering PNG assets.
- Added A/B/C/D text evidence grades and strict rules against presenting caption/OCR inference as direct visual observation.
- Added `validate_report.py --text-only` checks for disclosure, text-review completion, source recording, unverified-crop handling, and source-map execution metadata.
- Upgraded the source-map template to schema v3 with visual capability and verification fields.
- Documented structured-source, PDF-text, OCR, user-description, and human/vision-model handoff paths.

## 2.0.0 — 2026-08-01

- Broadened the default audience from computer-vision Ph.D. readers to research-trained readers across disciplines.
- Added structured routing for domain, audience, goal, depth, and language.
- Added project-level `.paper-reader.yaml` preferences and an example configuration.
- Separated method, theory, empirical/observational, dataset, system, and review paper types from domain-specific evidence norms.
- Added domain lenses for AI/CS, biomedicine, physics/mathematics, chemistry/materials, engineering, social science, earth/environment, and humanities/qualitative research.
- Kept computer vision as a deeply supported optional lens.
- Generalized report, reading, quality, and source-map protocols from model/experiment language to methods, theory, observation, qualitative evidence, and other research designs.
- Extended PDF caption detection to Scheme, Plate, Box, Chart, supplementary visuals, and Extended Data visuals.
- Added multilingual elevator-pitch validation and reader-profile validation for source-map schema v2.

## 1.0.0 — 2026-07-31

- Initial open-source release with source-grounded deep reading, visual extraction, report validation, and computer-vision-focused review guidance.
