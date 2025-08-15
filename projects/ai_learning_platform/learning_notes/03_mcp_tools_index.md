# MCP工具索引 / MCP Tools Index

## 概述 / Overview

本文档是AI学习平台中所有MCP工具的完整索引，包含工具定义、参数说明、返回值、使用场景和实现细节。这些工具是实现用户定制化、记忆存储和任务分配等核心功能的基础。

## 工具分类 / Tools Classification

### 1. 用户定制化工具 / User Customization Tools

#### 1.1 get_personalized_path - 个性化路径生成

**工具名称**: `get_personalized_path`  
**功能描述**: 根据用户背景和进度生成个性化学习路径  
**工具类型**: 路径规划 / Path Planning  

**参数说明 / Parameters**:
```python
@mcp.tool("get_personalized_path")
async def get_personalized_path(
    user_id: str,           # 用户ID
    current_progress: dict,  # 当前学习进度
    learning_goals: list     # 学习目标列表
) -> dict:
```

**返回值 / Return Value**:
```python
{
    "path": recommended_path,           # 推荐的学习路径
    "confidence": confidence_score,     # 推荐置信度
    "estimated_duration": duration      # 预估学习时长
}
```

**使用场景 / Usage Scenarios**:
- 新用户注册后的初始路径规划
- 学习过程中的动态路径调整
- 基于学习效果的路径优化

**实现逻辑 / Implementation Logic**:
1. 分析用户学习历史
2. 评估当前技能水平
3. 生成推荐路径
4. 计算置信度和预估时长

#### 1.2 get_next_recommendation - 智能推荐系统

**工具名称**: `get_next_recommendation`  
**功能描述**: 获取下一个学习推荐  
**工具类型**: 智能推荐 / Intelligent Recommendation  

**参数说明 / Parameters**:
```python
@mcp.tool("get_next_recommendation")
async def get_next_recommendation(
    user_id: str,        # 用户ID
    current_node: str,    # 当前学习节点
    context: dict         # 上下文信息
) -> dict:
```

**返回值 / Return Value**:
```python
{
    "recommendations": [           # 推荐选项列表
        {
            "option": option,      # 推荐选项
            "score": score,        # 推荐分数
            "reason": reason       # 推荐理由
        }
    ],
    "best_option": best_option     # 最佳推荐选项
}
```

**使用场景 / Usage Scenarios**:
- 学习过程中的下一步推荐
- 多选项智能排序
- 个性化内容推荐

**实现逻辑 / Implementation Logic**:
1. 获取用户当前状态
2. 分析可用选项
3. 计算推荐分数
4. 排序并返回最佳推荐

### 2. 记忆存储工具 / Memory Storage Tools

#### 2.1 store_learning_memory - 学习记忆存储

**工具名称**: `store_learning_memory`  
**功能描述**: 存储学习记忆  
**工具类型**: 记忆管理 / Memory Management  

**参数说明 / Parameters**:
```python
@mcp.tool("store_learning_memory")
async def store_learning_memory(
    user_id: str,      # 用户ID
    memory_type: str,  # 记忆类型
    content: dict,     # 记忆内容
    context: dict      # 上下文信息
) -> str:
```

**返回值 / Return Value**:
```python
memory_id  # 存储的记忆ID
```

**使用场景 / Usage Scenarios**:
- 存储学习笔记和心得
- 记录问答和讨论内容
- 保存学习过程中的重要信息

**实现逻辑 / Implementation Logic**:
1. 生成记忆ID
2. 创建记忆记录
3. 存储到数据库
4. 生成向量嵌入
5. 返回记忆ID

#### 2.2 retrieve_memories - 记忆检索

**工具名称**: `retrieve_memories`  
**功能描述**: 检索相关记忆  
**工具类型**: 记忆检索 / Memory Retrieval  

**参数说明 / Parameters**:
```python
@mcp.tool("retrieve_memories")
async def retrieve_memories(
    user_id: str,           # 用户ID
    query: str,             # 查询内容
    memory_types: list = None,  # 记忆类型过滤
    limit: int = 10         # 返回结果数量限制
) -> list:
```

**返回值 / Return Value**:
```python
[
    {
        "memory_id": id,        # 记忆ID
        "content": content,     # 记忆内容
        "similarity": score,    # 相似度分数
        "tags": tags,          # 标签信息
        "created_at": time     # 创建时间
    }
]
```

**使用场景 / Usage Scenarios**:
- 基于自然语言的记忆搜索
- 相关学习内容检索
- 复习材料查找

**实现逻辑 / Implementation Logic**:
1. 生成查询向量
2. 向量相似度搜索
3. 返回相关记忆列表

#### 2.3 schedule_review - 复习调度

**工具名称**: `schedule_review`  
**功能描述**: 安排复习计划  
**工具类型**: 复习管理 / Review Management  

**参数说明 / Parameters**:
```python
@mcp.tool("schedule_review")
async def schedule_review(
    user_id: str,        # 用户ID
    memory_id: str,      # 记忆ID
    review_result: str   # 复习结果
) -> dict:
```

**返回值 / Return Value**:
```python
{
    "memory_id": memory_id,           # 记忆ID
    "new_strength": new_strength,     # 新的记忆强度
    "next_review": next_review,       # 下次复习时间
    "review_interval": interval       # 复习间隔
}
```

**使用场景 / Usage Scenarios**:
- 基于复习结果调整记忆强度
- 智能安排复习时间
- 间隔重复算法实现

**实现逻辑 / Implementation Logic**:
1. 获取当前记忆强度
2. 根据复习结果调整强度
3. 计算下次复习时间
4. 更新记忆记录

### 3. 任务分配工具 / Task Allocation Tools

#### 3.1 allocate_learning_task - 智能任务分配

**工具名称**: `allocate_learning_task`  
**功能描述**: 分配学习任务  
**工具类型**: 任务管理 / Task Management  

**参数说明 / Parameters**:
```python
@mcp.tool("allocate_learning_task")
async def allocate_learning_task(
    user_id: str,     # 用户ID
    course_id: str,   # 课程ID
    context: dict     # 上下文信息
) -> dict:
```

**返回值 / Return Value**:
```python
{
    "allocated_task": best_task,           # 分配的任务
    "reasoning": explanation,              # 分配理由
    "estimated_duration": duration,        # 预估时长
    "prerequisites": prerequisites         # 前置要求
}
```

**使用场景 / Usage Scenarios**:
- 智能分配学习任务
- 检查依赖关系
- 动态难度调整

**实现逻辑 / Implementation Logic**:
1. 获取用户当前状态
2. 检查依赖关系
3. 评估任务难度
4. 选择最佳任务

## 工具配置 / Tools Configuration

### MCP服务器配置

**基础配置 / Basic Configuration**:
```json
{
  "mcpServers": {
    "learning_platform": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {
        "DATABASE_URL": "postgresql://...",
        "OPENAI_API_KEY": "..."
      }
    },
    "memory_store": {
      "command": "python",
      "args": ["memory_server.py"],
      "env": {
        "VECTOR_DB_URL": "faiss://..."
      }
    }
  }
}
```

### 工具注册配置

**工具注册示例 / Tool Registration Example**:
```python
# 注册所有工具
tools = [
    get_personalized_path,
    get_next_recommendation,
    store_learning_memory,
    retrieve_memories,
    schedule_review,
    allocate_learning_task
]

# 注册到MCP服务器
for tool in tools:
    mcp.register_tool(tool)
```

## 工具使用流程 / Tools Usage Flow

### 1. 用户定制化流程 / User Customization Flow

```
用户注册/登录 → get_personalized_path → 生成初始路径
学习过程中 → get_next_recommendation → 动态推荐
学习效果评估 → 路径优化 → 更新个性化设置
```

### 2. 记忆存储流程 / Memory Storage Flow

```
学习内容 → store_learning_memory → 存储记忆
查询需求 → retrieve_memories → 检索相关记忆
复习安排 → schedule_review → 智能复习调度
```

### 3. 任务分配流程 / Task Allocation Flow

```
用户状态分析 → allocate_learning_task → 任务分配
依赖检查 → 难度评估 → 最佳任务选择
任务执行 → 进度更新 → 下一轮分配
```

## 工具扩展性 / Tools Extensibility

### 新增工具原则 / New Tool Principles

1. **功能单一**: 每个工具专注于一个特定功能
2. **参数清晰**: 参数类型和含义明确
3. **返回值规范**: 返回数据结构统一
4. **错误处理**: 完善的异常处理机制
5. **文档完整**: 详细的工具说明和使用示例

### 扩展方向 / Extension Directions

1. **学习分析工具**: 学习行为分析、效果评估
2. **内容管理工具**: 课程内容管理、资源推荐
3. **社交互动工具**: 用户交流、协作学习
4. **评估反馈工具**: 学习效果评估、用户反馈

## 工具测试 / Tools Testing

### 测试策略 / Testing Strategy

1. **单元测试**: 测试每个工具的核心逻辑
2. **集成测试**: 测试工具间的协作
3. **性能测试**: 测试工具的性能表现
4. **用户测试**: 测试工具的用户体验

### 测试工具 / Testing Tools

- **pytest**: 单元测试框架
- **pytest-asyncio**: 异步测试支持
- **httpx**: HTTP客户端测试
- **Playwright**: 端到端测试

## 工具监控 / Tools Monitoring

### 监控指标 / Monitoring Metrics

1. **调用频率**: 工具被调用的次数
2. **响应时间**: 工具执行的时间
3. **成功率**: 工具执行成功的比例
4. **错误率**: 工具执行失败的比例

### 监控工具 / Monitoring Tools

- **Prometheus**: 指标收集
- **Grafana**: 数据可视化
- **Jaeger**: 分布式追踪
- **ELK Stack**: 日志分析

## 总结 / Summary

本文档收录了AI学习平台中所有核心MCP工具，包括用户定制化、记忆存储和任务分配三大类工具。每个工具都有详细的参数说明、返回值定义、使用场景和实现逻辑，为开发团队提供了完整的工具参考。

通过这些MCP工具，我们实现了：
- **个性化学习**: 基于用户背景的智能路径规划
- **智能记忆**: 高效的记忆存储和检索系统
- **任务分配**: 智能的学习任务分配和管理

这些工具为AI学习平台提供了强大的功能基础，支持平台的持续扩展和优化。

---

**创建时间**: 2024-12-19  
**文档状态**: 工具索引完成  
**下次更新**: 根据工具开发进度更新

