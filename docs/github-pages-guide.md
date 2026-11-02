# 从零制作一个「观行」这样的 GitHub Pages 网站

本文记录本站的实际结构与制作方法，适合制作个人主页、项目展示和论文阅读笔记。不需要数据库、付费服务器或前端构建工具。

## 1. 先理解网站由什么组成

本站采用静态 HTML + CSS：浏览器读取 HTML 组织内容，通过 CSS 排版。首页机器人插画是直接写在 HTML 中的 SVG，不需要外部图片服务。GitHub 保存源码，GitHub Pages 将站点文件发布到公网。

本仓库当前结构：

```text
jianqiang03.github.io/
├── index.html                 # 首页结构、文字、链接、SVG 插画
├── style.css                  # 首页颜色、字体、布局和移动端适配
├── .nojekyll                  # 使用静态文件，不经过 Jekyll 处理
├── notes/
│   └── dyna-2/
│       └── index.html         # 独立论文页，内含 CSS、图片和少量 JS
├── docs/
│   └── github-pages-guide.md  # 本教程，在 GitHub 中阅读
└── README.md                  # 仓库介绍与维护入口
```

这里没有 npm 安装或编译步骤。修改文件、预览、提交并推送，就是日常维护流程。也可以日后改用静态站点生成器，但当前内容规模还不需要。

## 2. 确定内容，再做视觉设计

本站首页按照四个问题组织：

1. 这是哪里？用「观行 / Observe & Act」和一句介绍交代主题。
2. 可以读什么？突出一篇已经完成的 Dyna-2 深读笔记。
3. 关注哪些方向？展示机器人学习、数据规模、训练系统三个主题。
4. 如何找到作者？链接到公开 GitHub 账号。

设计上使用米白底色、深绿色文字和少量橙色强调。首页采用双栏首屏，在手机上变为单栏；内容较少时不虚构项目经历、文章数量或个人履历。

修改首页主要编辑 `index.html`。颜色集中在 `style.css` 开头：

```css
:root {
  --paper: #f7f6ef;
  --ink: #233f31;
  --muted: #687568;
  --line: #d9ded1;
  --orange: #c46b40;
}
```

网页内容中的姓名、GitHub 链接、简介、文章标题需要一起检查。更改网站主题时，还应修改 `<title>` 和 `meta description`。

## 3. 在本地预览

维护本站，可以先克隆，然后进入目录：

```bash
git clone https://github.com/jianqiang03/jianqiang03.github.io.git
cd jianqiang03.github.io
python -m http.server 8080 --bind 127.0.0.1
```

在运行该命令的同一台电脑上打开 `http://localhost:8080/`。如果使用远程开发环境，需要通过开发工具转发端口。停止预览按 Ctrl+C。

建议使用 HTTP 预览，不只双击 HTML：例如 `notes/dyna-2/` 这种目录链接依赖 HTTP 服务返回目录中的 `index.html`，在 `file://` 下行为可能不同。

没有 Python 时，也可以使用编辑器的静态预览服务。网页本身不依赖 Python，它只是本地提供文件的工具。

## 4. 为自己的新网站创建 GitHub 仓库

维护本站时跳过本节，直接使用现有仓库，避免重复初始化。

个人根站点的仓库名应为 `<用户名>.github.io`。本站账号为 `jianqiang03`，所以仓库名是 `jianqiang03.github.io`，访问地址为 `https://jianqiang03.github.io/`。发布源可以选择 `main` 分支根目录。GitHub Free 的这类站点使用公开仓库。[官方建站说明](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

创建另一个新站点时，在 GitHub 新建对应名称的仓库，将你的站点文件放到根目录。可以在网页上传文件，也可以用 Git 推送。已有同名仓库时先检查内容，不要覆盖。

### 可选：用 GitHub CLI 创建并推送

先安装 Git 和 [GitHub CLI](https://cli.github.com/)，在实际执行发布的终端登录：

```bash
gh auth login --hostname github.com --git-protocol https --web
gh api user --jq .login
```

按照交互提示在浏览器完成设备授权。浏览器已登录，不代表另一个终端、容器或远程服务器中的 CLI 已登录；应以最后一条命令返回的账号为准。设备码过期时重新运行登录命令生成新码，不要反复提交旧码。无需把密码或 Token 写进网站文件。[CLI 登录说明](https://cli.github.com/manual/gh_auth_login)

以下命令只用于尚未初始化、尚未创建远程仓库的新站点目录。把 `YOUR_USERNAME` 替换为自己的 GitHub 用户名；个人信息通过你自己的 Git 配置设置。

```bash
git init -b main
git add index.html style.css .nojekyll notes
git commit -m "Create personal website"
gh repo create YOUR_USERNAME/YOUR_USERNAME.github.io --public --source . --remote origin --push
```

`git add` 中只列出实际存在且准备发布的文件。空的 `.nojekyll` 文件可以手动创建。创建仓库前也可以在 GitHub Settings → Emails 查看自己的 noreply 邮箱，并用仓库级 `git config user.email` 配置提交邮箱。

## 5. 开启 GitHub Pages

在仓库中进入 **Settings → Pages**，选择：

- Source：Deploy from a branch
- Branch：main
- Folder：/(root)

保存后到 Actions 查看 `pages-build-deployment` 的执行结果。即使仓库没有手写的 `.github/workflows`，GitHub 也会为分支发布执行部署任务。若 Pages 已自动开启，检查配置即可，不需要再次创建。[发布源说明](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

本站的入口是根目录的 `index.html`，而不是外层开发目录。上传时若把整个 `site/` 文件夹嵌套到根目录，发布源也必须相应调整；最简单的方法是把该文件夹里的站点文件放在仓库根目录。

## 6. 验证网站确实发布成功

构建通过只是第一步。还要打开以下页面确认访问和内容：

- 首页：`https://jianqiang03.github.io/`
- 论文页：`https://jianqiang03.github.io/notes/dyna-2/`
- 从首页点击文章，确认路由正确。
- 在论文页点击图片，确认能放大并用 Esc 关闭。
- 缩窄窗口到手机宽度，检查目录、表格和图片。

可以用 CLI 查看最近的部署：

```bash
gh run list --repo jianqiang03/jianqiang03.github.io --limit 3
```

本次页面验证覆盖 390、768、1024、1440 和 1920 像素宽度，重点检查横向溢出、标题换行、图表可读性和链接。无需为纯样式微调建立复杂测试系统，但要真实查看渲染结果。

## 7. 论文页怎么做，以及为什么曾经偏左

论文页与首页各自独立：首页 CSS 在 `style.css`；Dyna-2 页的 CSS 在 `notes/dyna-2/index.html` 的 `<style>` 中。因此修改首页样式不会自动改变论文页。

最初论文页采用固定左边距：

```css
/* 反例：超宽屏时容易让主体停留在左侧 */
main {
  max-width: 1090px;
  margin-left: 235px;
}
```

修正时把侧栏占用的空间从页面中预留，再让阅读区在剩余空间居中：

```css
body { padding-left: 248px; }
aside { position: fixed; width: 248px; }
main {
  width: 100%;
  max-width: 1240px;
  margin: 0 auto;
  padding: 64px clamp(28px, 4vw, 72px) 100px;
}
main > p {
  max-width: 880px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.95;
}
main > p:has(> img) { max-width: 1100px; }
@media (max-width: 950px) {
  body { padding-left: 0; }
  aside { position: relative; width: 100%; }
}
```

这是原理示例，完整断点和样式以页面源码为准。正文限制行长，避免一行横跨整块屏幕；图片和表格可以更宽。标题使用 `text-wrap: balance` 改善换行。手机将侧栏转换为顶部目录。

图片设置正确的 `width`、`height` 属性，再用 CSS 控制实际尺寸，可以提前预留纵横比，降低懒加载时的布局跳动。截图本身的留白需要在获取素材时处理，外层 CSS 居中不能消除图片像素里的留白。

目前论文图片内嵌为 Base64，优点是单个 HTML 可离线携带；缺点是文件较大、图片不能单独缓存。文章数量增长后，可以把图片移到每篇文章的 `assets/` 目录，改成普通相对路径。

## 8. 如何继续添加论文笔记

完整操作请看[新增论文解读：从论文链接到网站发布](adding-paper-notes.md)，含可复制的任务模板、核验要求和首页卡片示例。以下是简要说明。

为每篇文章建立独立目录，例如：

```text
notes/
├── dyna-2/index.html
└── another-paper/
    ├── index.html
    └── assets/
        └── architecture.png
```

制作新 HTML 时修改标题、正文、原文链接、图片说明和目录锚点，不要只替换页面大标题。文章内的图片路径可以写为 `assets/architecture.png`；两级目录下返回首页使用 `../../`。

随后在首页添加一个文章入口，例如：

```html
<a href="notes/another-paper/">
  <h3>新论文的标题</h3>
  <p>一句话说明这篇解读要回答的问题。</p>
</a>
```

同步调整首页文章数量。如果文章变多，再将目前单篇精选区扩展为文章列表，或增加分类和搜索。

论文深读也可以由 AI 辅助。本次尝试过 [paper-reading](https://github.com/techdou/paper-reading) 和 [paper-deep-reader](https://github.com/Linwei-Chen/paper-deep-reader-skill)，最终图文报告使用后者的六部分结构：总结、动机、方法、实验、贡献、结论。关键是逐图解释“观察到了什么、为什么支持结论、不能推出什么”，并核对原文，而不是只增加篇幅。

给 AI 的建站要求可以写成：

> 为我的个人研究笔记制作纯 HTML/CSS 网站，部署到 GitHub Pages。首页包含真实的个人介绍、关注方向和已有文章。使用相对链接，适配桌面与手机；论文页有目录、可放大的图表和来源链接。先完成本地预览与检查，再发布。不要编造履历、实验结果或文章。

[skills/github-pages](https://github.com/skills/github-pages) 是 GitHub 的教学课程，可用于学习 Pages；它和用于 AI 工作流的 `SKILL.md` 技能不是同一类东西。本网站采用手写静态 HTML，并未直接使用该课程的 Jekyll 模板。

## 9. 日常更新

在本地仓库目录中进行修改。多人或多台机器维护时，先确认工作区状态，再拉取远程更新。

```bash
git status
git pull --ff-only
# 编辑文件并进行本地预览
git diff --stat
git add index.html style.css notes docs README.md
git commit -m "Update website content"
git push origin main
```

只暂存本次准备发布的路径；有未完成内容时不要照抄整个 `git add` 列表。推送后等待部署成功并检查线上页面。若需要撤销已发布修改，优先使用 `git revert` 创建反向提交，再正常推送，避免覆盖共享历史。

## 10. 常见问题

| 现象 | 先检查什么 |
| --- | --- |
| 浏览器已登录，CLI 仍报未登录 | 在实际执行发布的环境运行 `gh api user --jq .login` |
| 授权码过期 | 重新发起 CLI 登录，使用新的一次性代码 |
| Pages 返回 404 | 仓库名称、发布分支、发布目录以及部署是否结束 |
| 首页正常，文章打不开 | 路径大小写、目录里的 index.html，以及是否使用了错误的绝对路径 |
| CSS 修改没出现在网页上 | 是否改对页面的样式文件、提交是否已部署、浏览器是否缓存旧资源 |
| 页面挤在左边 | 检查固定 margin-left 和 max-width 的组合，使用剩余空间居中布局 |
| 图片加载前页面跳动 | 是否提供与图片真实比例一致的 width、height |
| 图片看起来仍偏左 | 原始截图是否自带大量右侧空白；外层居中不等于画面主体居中 |

仓库当前公开，但尚未添加 LICENSE。教程不改变代码、文章或第三方图表的授权状态；引用论文内容时应保留来源，使用或转载第三方素材时另行确认许可。
