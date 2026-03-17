# 图床快速参考指南

## 从 0 到 1 搭建 GitHub 免费图床

### 第一步：创建 GitHub 仓库

1. 登录 [GitHub](https://github.com)
2. 点击右上角「+」→「New repository」
3. 填写信息：
   - Repository name: `nia-picture-assets`（或你喜欢的名字）
   - Description: `AI PM 内容素材库`
   - 选择 **Public**（必须公开才能用 jsDelivr）
   - 勾选「Add a README file」
4. 点击「Create repository」

### 第二步：克隆仓库到本地

```bash
git clone https://github.com/你的用户名/nia-picture-assets.git
cd nia-picture-assets
```

### 第三步：上传图片

将图片放入对应分类目录：

```
nia-picture-assets/
├── xhs/          # 小红书配图
├── bilibili/     # B站配图
├── blog/         # 博客配图
├── notion/       # Notion配图
├── icons/        # 图标
├── screenshots/  # 截图
└── cover/        # 封面
```

### 第四步：提交上传

```bash
git add .
git commit -m "添加 xhs/cover-001.jpg"
git push
```

### 第五步：获取 CDN 链接

图片上传后，使用以下格式访问：

```
https://cdn.jsdelivr.net/gh/{用户名}/{仓库名}@{分支}/{图片路径}
```

**示例**：
```
原始路径: xhs/cover-001.jpg
用户名: yourname
仓库: nia-picture-assets
分支: main

完整链接:
https://cdn.jsdelivr.net/gh/yourname/nia-picture-assets@main/xhs/cover-001.jpg
```

---

## 链接格式速查

| 用途 | 格式 |
|------|------|
| **CDN 直链** | `https://cdn.jsdelivr.net/gh/{u}/{r}@{b}/{path}` |
| **Markdown** | `![描述](CDN链接)` |
| **HTML** | `<img src="CDN链接" alt="描述">` |

---

## 工具使用

### 使用 generate_links.py 生成链接

1. 修改 `config.json` 中的配置：
   ```json
   {
     "github_username": "你的用户名",
     "repo_name": "nia-picture-assets",
     "branch": "main"
   }
   ```

2. 运行脚本：
   ```bash
   python generate_links.py
   ```

3. 脚本会自动扫描所有图片并生成对应的 CDN 链接和 Markdown 格式。

---

## 常见问题

### Q: 图片上传后链接打不开？
A: 首次上传后，等待 2-5 分钟让 jsDelivr 刷新缓存。

### Q: 如何更新图片？
A: 直接在本地替换同名文件，然后重新 `git add . && git commit && git push`。

### Q: 单个文件大小有限制吗？
A: 建议不超过 5MB，大文件会影响加载速度。

### Q: 可以用其他 CDN 吗？
A: 可以，常见的免费 CDN 还有：
- `https://raw.githubusercontent.com/{u}/{r}/{b}/{path}`（直连 GitHub，较慢）
- `https://gcore.jsdelivr.net/gh/{u}/{r}@{b}/{path}`（备用节点）

---

## 推荐的图床组合

| 场景 | 推荐方案 |
|------|----------|
| 临时/随手传 | SM.MS (s.ee) |
| 长期/重要素材 | GitHub + jsDelivr（本方案） |
| 笔记/文档 | 路过图床 (imgchr) |

---

*本指南配合 nia-picture-assets 图床仓库使用*
