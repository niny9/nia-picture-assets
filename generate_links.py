#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
图床链接生成工具
帮助生成 GitHub + jsDelivr CDN 图片链接
"""

import os
import json
from pathlib import Path

# ============ 配置区域 - 请根据实际情况修改 ============
GITHUB_USERNAME = "niny9"  # 替换为你的 GitHub 用户名
REPO_NAME = "nia-picture-assets"  # 仓库名称
BRANCH = "main"  # 分支名称，通常是 main 或 master
# ====================================================

CDN_BASE_URL = f"https://cdn.jsdelivr.net/gh/{GITHUB_USERNAME}/{REPO_NAME}@{BRANCH}"

def get_image_path(category, filename):
    """获取图片的完整路径"""
    return f"{category}/{filename}"

def generate_cdn_link(category, filename):
    """生成 jsDelivr CDN 链接"""
    relative_path = get_image_path(category, filename)
    full_url = f"{CDN_BASE_URL}/{relative_path}"
    return full_url

def generate_markdown(category, filename, alt_text=None):
    """生成 Markdown 格式的链接"""
    if alt_text is None:
        alt_text = os.path.splitext(filename)[0]
    url = generate_cdn_link(category, filename)
    return f"![{alt_text}]({url})"

def generate_html(category, filename, alt_text=None):
    """生成 HTML 格式的链接"""
    if alt_text is None:
        alt_text = os.path.splitext(filename)[0]
    url = generate_cdn_link(category, filename)
    return f'<img src="{url}" alt="{alt_text}">'

def list_local_images(base_path="."):
    """列出当前目录下的所有图片"""
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"}
    images = []
    
    for root, dirs, files in os.walk(base_path):
        # 跳过 README.md 和隐藏目录
        dirs[:] = [d for d in dirs if not d.startswith('.')]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in image_extensions:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_path)
                images.append(rel_path)
    
    return sorted(images)

def generate_all_links(base_path="."):
    """生成所有图片的链接并输出"""
    images = list_local_images(base_path)
    
    print(f"{'='*60}")
    print(f"图床链接生成器")
    print(f"{'='*60}")
    print(f"GitHub 用户名: {GITHUB_USERNAME}")
    print(f"仓库名称: {REPO_NAME}")
    print(f"分支: {BRANCH}")
    print(f"{'='*60}\n")
    
    if not images:
        print("未找到图片文件，请先将图片放入对应分类目录。")
        print("\n目录结构:")
        print("  /xhs/          - 小红书封面和配图")
        print("  /bilibili/      - B 站视频封面和素材")
        print("  /blog/         - 博客文章配图")
        print("  /notion/       - Notion 文档配图")
        print("  /avatar/       - 头像和人物图片")
        print("  /icons/        - 图标和 UI 元素")
        print("  /screenshots/  - 产品截图")
        print("  /cover/        - 通用封面图")
        return
    
    print(f"找到 {len(images)} 张图片:\n")
    
    for img in images:
        print(f"文件: {img}")
        print(f"  CDN 链接: {generate_cdn_link('xhs', img) if '/' not in img else generate_cdn_link(*img.split('/', 1))}")
        print(f"  Markdown: {generate_markdown('xhs', img) if '/' not in img else generate_markdown(*img.split('/', 1))}")
        print()

def update_config(username, repo, branch="main"):
    """更新配置文件"""
    global GITHUB_USERNAME, REPO_NAME, BRANCH, CDN_BASE_URL
    
    GITHUB_USERNAME = username
    REPO_NAME = repo
    BRANCH = branch
    CDN_BASE_URL = f"https://cdn.jsdelivr.net/gh/{GITHUB_USERNAME}/{REPO_NAME}@{BRANCH}"
    
    # 保存到配置文件
    config = {
        "github_username": username,
        "repo_name": repo,
        "branch": branch
    }
    
    with open("config.json", "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    
    print(f"配置已更新: {config}")

def load_config():
    """加载配置文件"""
    config_path = Path("config.json")
    
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config.get("github_username"), config.get("repo_name"), config.get("branch")
    
    return None, None, None

if __name__ == "__main__":
    # 尝试加载配置
    saved_username, saved_repo, saved_branch = load_config()
    
    if saved_username and saved_repo:
        GITHUB_USERNAME = saved_username
        REPO_NAME = saved_repo
        BRANCH = saved_branch or "main"
        CDN_BASE_URL = f"https://cdn.jsdelivr.net/gh/{GITHUB_USERNAME}/{REPO_NAME}@{BRANCH}"
    
    # 生成所有图片的链接
    generate_all_links(".")
