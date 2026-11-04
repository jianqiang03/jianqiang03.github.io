# 论文解读工具链：从原文到 GitHub Pages

## 1. 现在上传了什么

- `skills/paper-deep-reader/`：本地修改版深读技能，含引用规则、实现深读要求、PDF 图表工具、报告校验器及已有测试。
- `skills/paper-reading/`：另一套阅读技能，含 HTML 模板、校验脚本和本地交互 bridge。网站静态发布不依赖 bridge。
- `scripts/vla-pretraining/`：本次五篇论文的 PDF 下载/文本提取、固定版本官方代码下载、证据页渲染脚本。
- `scripts/render-paper-note.py`：把写好的 Markdown 渲染进现有网页外壳。
- `notes/`：正式报告、页面、图片与来源记录。

下载的完整 PDF、第三方仓库源码缓存和临时执行日志不作为本项目源码重新分发；使用下载脚本从原始来源获取。仓库没有模型权重、内部训练数据或访问凭据。

## 2. 环境

Python 3.10+，以及提供 `pdftotext` 的 Poppler（Ubuntu/Debian 包名为 `poppler-utils`）。在仓库根目录：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

依赖范围用于说明兼容需求，不是经过本次完整复现的锁定环境。技能安装见 [skills/README.md](../skills/README.md)。

## 3. 重建本次五篇论文的材料

```bash
python scripts/vla-pretraining/fetch_sources.py
python scripts/vla-pretraining/code_sources.py
python scripts/vla-pretraining/render_evidence_pages.py
```

第一条下载固定 arXiv v1、提取文本并生成 SHA-256 manifest；第二条按 `code-manifest.json` 的固定 commit 下载所读官方文件，不执行这些文件；第三条生成报告使用的四张证据页候选图。

材料保存到 `scripts/vla-pretraining/sources/`，候选图保存到 `rendered-pages/`，两者均被 Git 忽略。查看候选图，确认页码、图注、表格和可读性后，才复制到正式 note 的 assets。下载可受网络、上游可用性和限流影响。

与最初临时脚本相比，发布版增加输出目录创建，将代码获取改为固定 commit，补齐实际阅读的 MolmoAct2 文件，并将证据页渲染拆成单独脚本。没有执行下载脚本或已有测试来声称复现成功。

## 4. 阅读与写作依然是必需步骤

agent 需要结合原文、附录和已固定的代码逐项确认事实，再撰写 `report.md`。脚本不能替代这一过程。

每个承重问题按以下顺序完成：

1. 作者具体遇到什么问题？
2. 采用了什么方案？输入、变换、目标、mask 和梯度怎样变化？
3. 用一个样本/数值例子走通处理与执行。
4. 哪个实验支持其效果？
5. 哪部分作者没有解决？补充建议单独标注。

尤其不能提出采样频率或标定问题，随后只给一般性风险，而不交代作者有没有处理。也不能把合理的工程建议伪装成论文方案。

## 5. 渲染与新增页面

更新现有专题：

```bash
python scripts/render-paper-note.py vla-pretraining
```

这个脚本需要该 note 已有 `index.html` 外壳，并且 slug 已加入脚本的 `FOCUS` 字典；不是输入任意 PDF 就能生成新网页的命令。新增论文时按 [添加笔记流程](adding-paper-notes.md) 建立目录/外壳、调整标题描述与首页入口、填写报告和来源，再渲染。共享样式为 `notes/reading.css`。

技能里的校验器有各自输出契约。单篇六部分完整深读使用对应模式；专题定向报告不能因套用错误 schema 报错就改写事实或声称校验通过。检查本地引用、展示效果和事实证据是不同工作，HTML 成功渲染不证明论文分析正确。

## 6. 发布

审阅 `git diff`，只提交正式内容和必要工具。按 [GitHub Pages 建站说明](github-pages-guide.md) 推送到 main，查看 Pages 部署状态。上传 skill 时保留其 LICENSE、NOTICE 和修改说明；论文图片仍归原作者，不能套用技能代码的许可。

## 7. 复现程度

现有材料支持继续编辑、追溯来源和重建网页。它不保证模型自动写出完全相同的文字，也没有复现任何论文训练结果。上游 skill 的原始 commit 未在安装时完整记录，因此仅声明为本地快照；论文关联代码的 commit 则记录于 manifest。
