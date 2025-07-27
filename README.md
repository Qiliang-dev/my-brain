# My Brain - 个人知识管理系统 / Personal Knowledge Management System

## 项目概述 / Project Overview
这是一个个人知识管理系统，用于组织和跟踪不同主题的学习进度和知识积累。系统采用主题分离的方式，每个学习项目都有独立的结构和进度跟踪。

This is a personal knowledge management system for organizing and tracking learning progress and knowledge accumulation across different topics. The system adopts a topic-separated approach, with each learning project having independent structure and progress tracking.

## 项目结构 / Project Structure

```
My_brain/
├── projects/                          # 学习项目目录 / Learning Projects Directory
│   ├── tax_learning/                  # 德国税务申报学习 / German Tax Declaration Learning
│   │   ├── 02_德国税务申报.md         # 税务申报基础知识 / Tax Declaration Basics
│   │   ├── 03_德国税务申报实务.md     # 税务申报实务操作 / Tax Declaration Practice
│   │   └── 学习进度_Learning_Progress.md # 学习进度记录 / Learning Progress Record
│   └── istqb_certification/           # ISTQB认证学习 / ISTQB Certification Learning
│       ├── 01_Testing_Fundamentals_测试基础.md # 测试基础 / Testing Fundamentals
│       └── 学习进度_Learning_Progress.md # 学习进度记录 / Learning Progress Record
├── docs/                              # 文档目录 / Documentation Directory
│   └── 学习指南.md                     # 学习指南 / Learning Guide
├── knowledge_base/                    # 通用知识库 / General Knowledge Base
│   ├── references/                    # 参考资料 / References
│   ├── summaries/                     # 知识总结 / Knowledge Summaries
│   │   └── 知识点总览.md              # 知识点总览 / Knowledge Overview
│   └── topics/                        # 主题知识 / Topic Knowledge
│       └── 01_基础概念.md             # 基础概念 / Basic Concepts
├── learning_records/                  # 学习记录 / Learning Records
│   ├── progress/                      # 进度记录 / Progress Records
│   │   └── 学习进度总览.md            # 学习进度总览 / Learning Progress Overview
│   └── qa_logs/                       # 问答记录 / Q&A Logs
│       └── 问答记录.md                # 问答记录 / Q&A Records
├── tools/                             # 工具目录 / Tools Directory
├── 02_V4_ISTQB_Foundation_Fundaments_of_testing_1.pptx # ISTQB课程PPT / ISTQB Course PPT
├── ppt_content.txt                    # PPT内容提取 / PPT Content Extraction
├── ppt_notes.txt                      # PPT注释提取 / PPT Notes Extraction
└── README.md                          # 项目说明 / Project Description
```

## 当前学习项目 / Current Learning Projects

### 1. 德国税务申报学习 / German Tax Declaration Learning
- **状态 / Status**: 进行中 / In Progress
- **完成度 / Completion**: 90%
- **重点内容 / Key Content**: 
  - 个人所得税申报 / Personal Income Tax Declaration
  - 各种费用申报 / Various Expense Declarations
  - Elster系统使用 / Elster System Usage
  - 多份工作申报 / Multiple Jobs Declaration

### 2. ISTQB Foundation 认证 / ISTQB Foundation Certification
- **状态 / Status**: 进行中 / In Progress
- **完成度 / Completion**: 15%
- **重点内容 / Key Content**:
  - 测试基础 / Testing Fundamentals
  - 测试生命周期 / Testing Throughout the Software Development Lifecycle
  - 静态测试 / Static Testing
  - 测试技术 / Test Techniques
  - 测试管理 / Test Management

## 学习特点 / Learning Features

### 主题分离 / Topic Separation
- 每个学习项目都有独立的结构 / Each learning project has independent structure
- 清晰的知识组织和进度跟踪 / Clear knowledge organization and progress tracking
- 便于管理和维护 / Easy to manage and maintain

### 双语标注 / Bilingual Annotation
- 所有内容都采用中英文双语标注 / All content uses Chinese-English bilingual annotation
- 便于中英文对照学习 / Facilitates Chinese-English comparative learning
- 提高语言能力 / Improves language skills

### 知识管理 / Knowledge Management
- 结构化的知识库 / Structured knowledge base
- 详细的进度记录 / Detailed progress records
- 完整的参考资料 / Complete reference materials

## 使用工具 / Tools Used

### 开发环境 / Development Environment
- **VSCode**: 主要开发和学习环境 / Main development and learning environment
- **PowerPoint Preview**: 用于查看PPT文件 / For viewing PPT files
- **Python脚本 / Python Scripts**: 提取PPT内容 / Extract PPT content

### 文档格式 / Document Format
- **Markdown**: 主要文档格式 / Main document format
- **双语标注**: 中英文对照 / Chinese-English bilingual annotation
- **结构化组织**: 清晰的层次结构 / Clear hierarchical structure

## 学习方法 / Learning Methods

### 内容提取 / Content Extraction
1. 使用Python脚本从PPT中提取文本和注释 / Use Python scripts to extract text and notes from PPT
2. 整理成结构化的Markdown文档 / Organize into structured Markdown documents
3. 添加中英文双语标注 / Add Chinese-English bilingual annotation

### 知识整理 / Knowledge Organization
1. 按主题分类组织内容 / Organize content by topic
2. 建立清晰的知识结构 / Establish clear knowledge structure
3. 记录学习进度和成果 / Record learning progress and outcomes

### 进度跟踪 / Progress Tracking
1. 详细记录学习进度 / Detailed learning progress records
2. 定期更新学习状态 / Regular learning status updates
3. 设定明确的学习目标 / Set clear learning goals

## 项目目标 / Project Goals

### 短期目标 / Short-term Goals
- 完成ISTQB Foundation认证 / Complete ISTQB Foundation certification
- 掌握德国税务申报实务 / Master German tax declaration practice
- 建立完整的知识管理体系 / Establish complete knowledge management system

### 长期目标 / Long-term Goals
- 获得ISTQB高级认证 / Obtain ISTQB Advanced certification
- 成为税务申报专家 / Become a tax declaration expert
- 建立个人知识库 / Establish personal knowledge base

## 贡献指南 / Contribution Guidelines

### 添加新项目 / Adding New Projects
1. 在`projects/`目录下创建新项目文件夹 / Create new project folder under `projects/` directory
2. 建立项目结构（知识库、进度记录等）/ Establish project structure (knowledge base, progress records, etc.)
3. 更新README文件 / Update README file

### 内容更新 / Content Updates
1. 保持双语标注格式 / Maintain bilingual annotation format
2. 及时更新进度记录 / Update progress records promptly
3. 保持文档结构清晰 / Keep document structure clear

## 许可证 / License
本项目仅供个人学习使用 / This project is for personal learning use only.

---

*最后更新 / Last Updated: 2025年1月10日 / January 10, 2025* 