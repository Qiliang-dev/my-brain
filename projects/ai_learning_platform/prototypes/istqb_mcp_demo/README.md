# ISTQB学习平台MCP工具演示

## 🎯 项目概述

这是一个完整的MCP（Model Context Protocol）工具演示项目，展示了如何为转码人士定制ISTQB认证学习方案。通过MCP协议，AI模型可以调用这些工具来提供个性化的学习建议。

## 🚀 核心功能

### 1. 个性化学习路径生成
- 根据用户背景（专业、经验）定制学习计划
- 智能调整学习顺序和难度
- 提供时间安排和完成预估

### 2. 用户准备度评估
- 分析用户的技术背景和学习能力
- 评估学习ISTQB的准备程度
- 提供针对性的准备建议

### 3. 实践项目推荐
- 基于学习章节推荐相关项目
- 根据用户水平筛选项目难度
- 提供项目描述和预估时间

## 🛠️ 技术架构

```
istqb_mcp_demo/
├── istqb_learning_tool.py    # 核心学习路径生成工具
├── mcp_server.py             # MCP服务器实现
├── test_client.py            # 测试客户端（模拟AI调用）
├── config.json               # MCP配置文件
├── requirements.txt          # Python依赖
└── README.md                # 项目文档
```

## 📋 安装和配置

### 步骤1：安装依赖
```bash
# 创建虚拟环境
python -m venv istqb_env
source istqb_env/bin/activate  # Linux/Mac
# 或
istqb_env\Scripts\activate     # Windows

# 安装依赖
pip install -r requirements.txt
```

### 步骤2：配置MCP服务器
编辑 `config.json` 文件，修改路径配置：
```json
{
  "mcpServers": {
    "istqb_learning_platform": {
      "command": "python",
      "args": ["mcp_server.py"],
      "cwd": "/your/actual/path/to/istqb_mcp_demo"
    }
  }
}
```

### 步骤3：启动MCP服务器
```bash
cd istqb_mcp_demo
python mcp_server.py
```

## 🎮 使用方法

### 方法1：运行演示程序
```bash
python test_client.py
```
这将启动一个完整的演示，展示AI如何调用MCP工具为用户定制学习方案。

### 方法2：在AI模型中配置
1. 将 `config.json` 中的配置添加到你的AI模型配置中
2. 启动MCP服务器
3. AI模型就可以调用这些工具了

### 方法3：直接测试工具
```bash
# 测试学习路径生成工具
python -c "
import asyncio
from istqb_learning_tool import ISTQBLearningPathTool, UserProfile

async def test():
    tool = ISTQBLearningPathTool()
    user = UserProfile(
        user_id='test_user',
        background='计算机科学专业',
        programming_experience='有经验',
        testing_experience='基础',
        learning_style='实践型',
        available_hours_per_week=20
    )
    result = await tool.generate_istqb_learning_path(user)
    print(result)

asyncio.run(test())
"
```

## 🔧 MCP工具详解

### 1. `generate_istqb_learning_path`
**功能**: 生成个性化ISTQB学习路径

**参数**:
- `user_id`: 用户ID
- `background`: 用户背景（如：计算机科学专业）
- `programming_experience`: 编程经验（无经验/基础/有经验）
- `testing_experience`: 测试经验（无经验/基础/有经验）
- `learning_style`: 学习风格（视觉型/听觉型/实践型）
- `available_hours_per_week`: 每周可用学习时间
- `target_certification_date`: 目标认证日期（可选）

**返回**:
- 个性化学习路径
- 时间安排
- 学习建议
- 推荐实践项目
- 预估总时长和置信度

### 2. `assess_user_readiness`
**功能**: 评估用户学习准备度

**参数**:
- `background`: 用户背景
- `programming_experience`: 编程经验
- 其他参数可选

**返回**:
- 背景分析结果
- 准备建议
- 预估准备时间

### 3. `get_istqb_curriculum`
**功能**: 获取ISTQB课程大纲

**参数**: 无

**返回**:
- 完整课程大纲
- 章节信息
- 总学习时长

## 📊 演示场景

### 场景1：计算机专业转码人士
```
用户: "我是计算机科学专业的，有编程经验，想学习ISTQB认证"

AI响应: "我来帮你制定个性化的ISTQB学习方案。让我先评估一下你的学习准备度，然后为你生成最适合的学习路径。"

工具调用:
1. assess_user_readiness - 评估准备度
2. generate_istqb_learning_path - 生成学习路径

结果: 准备度0.8，推荐直接开始学习，预计12周完成
```

### 场景2：非计算机专业转码人士
```
用户: "我是机械工程专业的，没有编程经验，想转行做软件测试"

AI响应: "我理解你的转行需求。让我先评估一下你的准备度，然后为你制定一个从基础开始的学习计划。"

工具调用:
1. assess_user_readiness - 评估准备度
2. generate_istqb_learning_path - 生成学习路径

结果: 准备度0.3，建议先补充基础知识，预计需要1-2个月准备
```

## 🔍 技术特点

### 1. 智能路径生成
- 基于用户背景动态调整学习顺序
- 考虑前置依赖关系
- 根据可用时间优化安排

### 2. 个性化建议
- 针对不同学习风格提供建议
- 基于经验水平推荐项目
- 动态调整学习策略

### 3. 时间管理
- 智能计算学习时长
- 提供周计划安排
- 预估完成日期

## 🚀 扩展功能

### 1. 数据库集成
```python
# 可以轻松集成数据库
from database import DatabaseConnection
db = DatabaseConnection()
# 在工具中使用数据库存储用户信息和学习进度
```

### 2. 机器学习优化
```python
# 可以添加ML模型来优化推荐
from ml_model import LearningPathOptimizer
optimizer = LearningPathOptimizer()
# 使用ML模型优化学习路径
```

### 3. 实时进度跟踪
```python
# 添加进度跟踪功能
from progress_tracker import ProgressTracker
tracker = ProgressTracker()
# 实时更新学习进度
```

## 🐛 故障排除

### 常见问题1：MCP服务器启动失败
**症状**: 运行 `python mcp_server.py` 时出错
**解决**: 
- 检查Python版本（需要3.7+）
- 确认依赖已安装：`pip install mcp`
- 检查文件路径是否正确

### 常见问题2：工具调用失败
**症状**: AI模型无法调用MCP工具
**解决**:
- 确认MCP服务器正在运行
- 检查配置文件路径
- 验证工具注册是否成功

### 常见问题3：依赖导入错误
**症状**: `ModuleNotFoundError`
**解决**:
- 激活虚拟环境
- 重新安装依赖：`pip install -r requirements.txt`
- 检查PYTHONPATH设置

## 📚 学习资源

### 1. MCP协议学习
- [MCP官方文档](https://modelcontextprotocol.io/)
- [MCP Python库](https://github.com/modelcontextprotocol/python-sdk)

### 2. ISTQB认证
- [ISTQB官网](https://www.istqb.org/)
- [ISTQB学习指南](https://www.istqb.org/certifications/certified-tester-foundation-level)

### 3. 软件测试学习
- [软件测试基础](https://www.guru99.com/software-testing-introduction.html)
- [测试实践项目](https://github.com/topics/software-testing)

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目！

### 贡献方式
1. Fork项目
2. 创建功能分支
3. 提交更改
4. 创建Pull Request

### 代码规范
- 使用Python类型提示
- 添加详细的文档字符串
- 遵循PEP 8代码风格
- 编写单元测试

## 📄 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 📞 联系方式

如有问题或建议，请通过以下方式联系：
- 提交GitHub Issue
- 发送邮件至：[your-email@example.com]

---

**🎉 祝你学习愉快，早日获得ISTQB认证！**


