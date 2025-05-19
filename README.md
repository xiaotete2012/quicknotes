# QuickNotes - 极简命令行笔记工具

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

## 目录
- [功能特性](#-功能特性)
- [安装指南](#-安装指南)
- [使用教程](#-使用教程)
- [开发部署](#-开发部署)
- [贡献说明](#-贡献说明)
- [开源协议](#-开源协议)

## ✨ 功能特性

```text
• 添加/删除/搜索笔记
• 支持标签分类 (--tag)
• 自动保存为JSON格式
• 毫秒级响应速度
• 纯离线本地存储

```
QuickNotes是一个简单高效的命令行笔记工具，让您可以快速记录、管理和检索笔记。支持标签分类、全文搜索，并以JSON格式安全存储您的所有笔记。

## 📦 安装指南

### 方法1：源码运行# 克隆仓库
git clone https://github.com/yourusername/quicknotes.git
cd quicknotes

# 安装依赖
pip install -r requirements.txt

# 运行示例
python quicknotes.py add "安装成功测试"
## 🚀 使用教程

### 基础命令
| 命令格式               | 示例                          | 说明                 |
|------------------------|-------------------------------|----------------------|
| add <内容>             | add "明天10点开会"            | 添加笔记             |
| add --tag=<标签>       | add "修复BUG" --tag=work      | 添加带标签的笔记     |
| list                   | list                          | 列出所有笔记         |
| delete <ID>            | delete 3                      | 删除指定ID的笔记     |
| search <关键词>        | search "会议"                 | 搜索笔记内容         |

### 高级用法# 组合使用标签和搜索
quicknotes add "阅读PEP8规范" --tag=study
quicknotes search --tag=study

# 导出笔记为Markdown
quicknotes list > notes.md
## 🛠️ 开发部署

### 项目结构quicknotes/
├── quicknotes.py     # 主程序
├── storage.py        # 数据存储逻辑
├── notes.ico         # 应用图标
└── requirements.txt  # 依赖配置
### 重新打包# 安装打包工具
pip install pyinstaller pillow

# 生成可执行文件
pyinstaller --onefile --clean --icon=notes.ico quicknotes.py

# 输出路径
ls dist/quicknotes*
## 🤝 贡献说明

### 开发流程
1. Fork 本仓库
2. 创建特性分支 (git checkout -b feat/awesome-feature)
3. 提交更改 (git commit -m 'Add amazing feature')
4. 推送到分支 (git push origin feat/awesome-feature)
5. 创建Pull Request

### 代码规范# 使用Google风格文档字符串
def add_note(content: str, tag: str = None) -> bool:
    """添加新笔记到数据库
    
    Args:
        content: 笔记文本内容
        tag: 可选标签分类
    
    Returns:
        是否添加成功
    """
## 📜 开源协议
本项目采用 MIT License，您可以：
- 自由使用、修改和分发代码
- 用于商业项目
- 保留原始许可证声明
THE SOFTWARE IS PROVIDED "AS IS"...
由 @xiaotete2012 创建并维护
    