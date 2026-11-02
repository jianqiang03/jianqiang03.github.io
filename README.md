# 观行 · Observe & Act

jianqiang03 的个人研究笔记网站，关注机器人学习、数据与训练系统。

**[访问网站](https://jianqiang03.github.io/)** · **[阅读建站教程](docs/github-pages-guide.md)** · **[Dyna-2 深读](https://jianqiang03.github.io/notes/dyna-2/)**

## 本地运行

```bash
git clone https://github.com/jianqiang03/jianqiang03.github.io.git
cd jianqiang03.github.io
python -m http.server 8080 --bind 127.0.0.1
```

打开 http://localhost:8080/ 。无需安装 npm 依赖或运行构建命令。

## 文件入口

| 文件 | 用途 |
| --- | --- |
| [index.html](index.html) | 首页内容、导航和 SVG 插画 |
| [style.css](style.css) | 首页样式与响应式布局 |
| [notes/dyna-2/index.html](notes/dyna-2/index.html) | 论文页，CSS 与图片内嵌在 HTML 中 |
| [docs/github-pages-guide.md](docs/github-pages-guide.md) | 从制作、预览到发布和维护的中文教程 |
| [.nojekyll](.nojekyll) | 让 Pages 直接发布静态文件 |

## 发布与维护

GitHub Pages 从 `main` 分支的根目录发布。修改文件并推送后，查看仓库 Actions 中的 `pages-build-deployment` 结果，再检查线上页面。

建站教程包含 CLI 登录、首次发布、添加文章、论文页居中布局、图片加载优化与常见故障排查。

## 授权状态

仓库目前公开，尚未添加开源许可证。论文原图和其他第三方内容保留其来源及原作者权利。
