# 论文阅读 skills 的本地快照

这是本网站使用的本地版本快照（2026-11-04），不是上游仓库的自动镜像。

| 目录 | 上游 | 许可 | 本仓库版本 |
| --- | --- | --- | --- |
| `paper-deep-reader` | https://github.com/Linwei-Chen/paper-deep-reader-skill | MIT；保留 Linwei Chen 版权 | 包含此前本地增加的实现与训练深读规则；见包内 CHANGELOG |
| `paper-reading` | https://github.com/Agentchengfeng/paper-reading-skills | Apache-2.0；保留 LICENSE 和 NOTICE | 当前本地安装快照；不宣称对应某个已核验的上游 commit |

两个目录均保留 SKILL.md、references、scripts、已有 tests、agents 与原有许可文件。发布时排除了运行缓存和 Git 元数据，没有运行其中的测试。

## 安装到本地 agent

将选定目录复制到你的 agent 的 skills 目录，保持目录结构。例如使用默认 Codex 目录时：

```bash
mkdir -p "$HOME/.codex/skills"
cp -R -n skills/paper-deep-reader "$HOME/.codex/skills/"
cp -R -n skills/paper-reading "$HOME/.codex/skills/"
```

`-n` 不覆盖已有文件。如果已经安装旧版，先备份并自行选择合并或替换整个目录，避免把两个版本混成一份。使用自定义 skills 路径的环境应调整目标目录。安装后让 agent 重新加载技能。

## 使用与边界

给 agent 明确的论文链接和任务，并指定技能；例如：

> 使用 paper-deep-reader 深读这篇论文，重点说明预训练。每个问题接上作者的具体方案、计算例子、实验依据和解决边界；论文没解决的地方明确写出来。输出 report.md、来源记录与已检查的图表，再按网站流程发布。

技能是 agent 的阅读与写作指令；Python 脚本负责提取、校验、渲染，不会单独生成可信的论文分析。选择一个主技能即可，不需要机械叠加两套输出格式。

完整流程见 [工具链说明](../docs/paper-toolchain.md)。
