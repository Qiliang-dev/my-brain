# ISTQB Foundation 学习笔记 / ISTQB Foundation Study Notes

## 课程概述 / Course Overview
- **课程名称 / Course Name**: ISTQB Foundation - Fundaments of testing
- **机构 / Organization**: Technica Engineering GmbH
- **学习时间 / Study Period**: 2025年1月10日 - 2025年1月24日 / January 10, 2025 - January 24, 2025
- **考试要求 / Exam Requirements**: 40题，26分及格(65%)，60分钟 / 40 questions, 26 points to pass (65%), 60 minutes

## 学习内容总结 / Learning Content Summary

### 第一章：测试基础 / Chapter 1: Testing Fundamentals

#### 1.1 什么是测试？ / What is Testing?

**核心概念 / Core Concepts**:
- 测试是一套活动，用于发现缺陷并评估软件制品的质量 / Testing is a set of activities to discover defects and evaluate the quality of software artifacts
- 测试对象 (test object): 被测试的制品 / The work product to be tested

**测试活动 / Test Activities**:
- 测试计划 (test planning)
- 需求分析 (requirement analysis)
- 设计 (designing)
- 实施/执行/分析测试 (implementing/executing/analyzing tests)
- 评审 (reviewing)
- 报告结果 (reporting results)
- 评估测试对象的质量 (evaluating the quality of a test object)

**测试类型 / Types of Testing**:
- **动态测试 (Dynamic testing)**: 涉及软件执行 / involves the execution of software
- **静态测试 (Static testing)**: 不涉及软件执行，包括评审和静态分析 / does not involve software execution, includes reviews and static analysis

#### 1.2 为什么需要测试？ / Why is Testing Necessary?

**测试的必要性 / Necessity of Testing**:
- 减少开发不正确或不想要功能的风险 / reduces the risk of incorrect or unwanted features being developed
- 减少基本设计缺陷的风险，使测试能够在早期阶段识别 / reduce the risk of fundamental design defects and enable tests to be identified at an early stage
- 减少代码和测试本身中缺陷的风险 / reduce the risk of defects within the code and the tests themselves

#### 1.3 七个测试原则 / Seven Testing Principles

1. **测试显示缺陷的存在，而不是它们的缺失 / Testing shows the presence of defects, not their absence**
2. **穷尽测试是不可能的 / Exhaustive testing is impossible**
3. **早期测试节省时间和金钱 / Early testing saves time and money**
4. **缺陷聚集在一起 / Defects cluster together**
5. **警惕农药悖论 (pesticide paradox) / Beware of the pesticide paradox**
6. **测试依赖于上下文 / Testing is context dependent**
7. **无错误谬论 (Absence-of-errors fallacy) / Absence-of-errors is a fallacy**

#### 1.4 测试活动、测试制品和测试角色 / Test Activities, Testware and Test Roles

**测试活动 / Test Activities**:
1. 测试计划 (Test Planning)
2. 测试监控和控制 (Test Monitoring and Control)
3. 测试分析 (Test Analysis)
4. 测试设计 (Test Design)
5. 测试实施 (Test Implementation)
6. 测试执行 (Test Execution)
7. 测试完成 (Test Completion)

**测试制品 (Testware) / Test Work Products**:
- 测试计划 (Test Plans)
- 测试用例 (Test Cases)
- 测试数据 (Test Data)
- 测试脚本 (Test Scripts)
- 测试报告 (Test Reports)

**可追溯性 / Traceability**:
- **双向可追溯性 (Bidirectional Traceability)**: 正向和反向可追溯性 / Forward and backward traceability
- **水平和垂直可追溯性 (Horizontal and Vertical Traceability)**: 同一级别和不同级别制品之间的关系 / Relationships between items at same and different levels

**测试角色 / Testing Roles**:
1. **测试管理角色 (Test Management Role)**: 负责测试过程、团队领导和测试活动 / Responsible for test process, team leadership and test activities
2. **测试角色 (Testing Role)**: 负责测试的工程（技术）方面 / Responsible for engineering (technical) aspects of testing

#### 1.5 测试中的基本技能和良好实践 / Essential Skills and Good Practices in Testing

**基本技能 / Essential Skills**:
1. **测试知识 (Testing Knowledge)**: 提高测试有效性 / Increase effectiveness of testing
2. **细致、谨慎、好奇心、关注细节、有条理 (Thoroughness, Carefulness, Curiosity, Attention to Details, Being Methodical)**: 识别缺陷 / Identify defects
3. **良好的沟通技能、积极倾听、团队合作 (Good Communication Skills, Active Listening, Being a Team Player)**: 与利益相关者互动 / Interact with stakeholders
4. **分析思维、批判性思维、创造力 (Analytical Thinking, Critical Thinking, Creativity)**: 提高测试有效性 / Increase effectiveness of testing
5. **技术知识 (Technical Knowledge)**: 提高测试效率 / Increase efficiency of testing
6. **领域知识 (Domain Knowledge)**: 理解业务需求 / Understand business requirements

**良好实践 / Good Practices**:
- **全团队方法 (Whole Team Approach)**: 提高团队协作 / Improve team collaboration
- **测试独立性 (Independence of Testing)**: 客观的测试视角 / Objective testing perspective
- **票证乒乓 (Ticket Ping Pong)**: 测试人员与开发人员的协作过程 / Collaboration process between testers and developers

### 第二章：测试活动和角色 / Chapter 2: Testing Activities and Roles

#### 2.1 测试活动概述 / Test Activities Overview

**测试活动流程 / Test Activity Flow**:
1. **测试计划 (Test Planning)**: 确定测试目标和策略 / Determine test objectives and strategy
2. **测试监控和控制 (Test Monitoring and Control)**: 跟踪测试进度和调整计划 / Track test progress and adjust plans
3. **测试分析 (Test Analysis)**: 分析测试基础以确定测试条件 / Analyze test basis to determine test conditions
4. **测试设计 (Test Design)**: 设计测试用例和测试数据 / Design test cases and test data
5. **测试实施 (Test Implementation)**: 准备测试环境和测试脚本 / Prepare test environment and test scripts
6. **测试执行 (Test Execution)**: 执行测试用例并记录结果 / Execute test cases and record results
7. **测试完成 (Test Completion)**: 完成测试活动并归档测试制品 / Complete test activities and archive testware

#### 2.2 测试角色和职责 / Test Roles and Responsibilities

**测试管理角色 / Test Management Role**:
- 制定测试策略和计划 / Develop test strategy and plans
- 管理测试资源和预算 / Manage test resources and budget
- 协调测试团队活动 / Coordinate test team activities
- 报告测试状态和结果 / Report test status and results

**测试角色 / Testing Role**:
- 设计和执行测试用例 / Design and execute test cases
- 分析测试结果和缺陷 / Analyze test results and defects
- 维护测试环境和工具 / Maintain test environment and tools
- 提供测试技术建议 / Provide testing technical advice

### 第三章：软件生命周期中的测试 / Chapter 3: Testing Throughout Software Lifecycle

#### 3.1 测试驱动开发 (TDD) / Test-Driven Development

**TDD方法 / TDD Approach**:
- **测试优先方法 (Test First Approach)**: 先写测试，再写代码 / Write tests first, then code
- **ATDD (Acceptance Test-Driven Development)**: 验收测试驱动开发 / Acceptance test-driven development
- **BDD (Behavior-Driven Development)**: 行为驱动开发 / Behavior-driven development

#### 3.2 DevOps和测试 / DevOps and Testing

**DevOps集成 / DevOps Integration**:
- 持续集成和持续部署 (CI/CD) / Continuous Integration and Continuous Deployment
- 自动化测试在DevOps中的作用 / Role of automated testing in DevOps
- 测试左移策略 / Shift-left testing strategy

#### 3.3 V模型 / V-Model

**V模型概述 / V-Model Overview**:
- 需求分析阶段对应验收测试 / Requirements analysis phase corresponds to acceptance testing
- 系统设计阶段对应系统测试 / System design phase corresponds to system testing
- 架构设计阶段对应集成测试 / Architecture design phase corresponds to integration testing
- 模块设计阶段对应组件测试 / Module design phase corresponds to component testing

#### 3.4 测试级别和测试类型 / Test Levels and Test Types

**测试级别 / Test Levels**:
- 组件测试 (Component testing)
- 组件集成测试 (Component Integration testing)
- 系统测试 (System testing)
- 系统集成测试 (System integration testing)
- 验收测试 (Acceptance testing)

**测试类型 / Test Types**:
- 功能测试 (Functional testing)
- 非功能测试 (Non-functional testing)
- 黑盒测试 (Black-box testing)
- 白盒测试 (White-box testing)

#### 3.5 确认测试和回归测试 vs 维护测试 / Confirmation and Regression Testing vs Maintenance Testing

**确认测试 (Confirmation Testing)**:
- 验证缺陷修复是否有效 / Verify that defect fixes are effective
- 确保修复没有引入新问题 / Ensure fixes don't introduce new issues

**回归测试 (Regression Testing)**:
- 确保新变更没有破坏现有功能 / Ensure new changes don't break existing functionality
- 基于风险分析选择测试用例 / Select test cases based on risk analysis

**维护测试 (Maintenance Testing)**:
- 在软件发布后进行 / Conducted after software release
- 包括修改、退役和迁移测试 / Includes modification, retirement, and migration testing

### 第四章：静态测试 / Chapter 4: Static Testing

#### 4.1 静态测试概述 / Static Testing Overview

**静态测试 vs 动态测试 / Static Testing vs Dynamic Testing**:

**静态测试 (Static Testing)**:
- 不涉及软件执行 / Does not involve software execution
- 直接发现缺陷 / Finds defects directly
- 包括评审和静态分析 / Includes reviews and static analysis

**动态测试 (Dynamic Testing)**:
- 涉及软件执行 / Involves software execution
- 通过故障确定缺陷 / Determines defects through failures
- 需要后续分析 / Requires subsequent analysis

#### 4.2 评审类型 / Review Types

**评审类型包括 / Review types include**:
- **非正式评审 (Informal Review)**: 简单的文档检查 / Simple document review
- **走查 (Walkthrough)**: 作者引导的评审 / Author-led review
- **技术评审 (Technical Review)**: 同行评审 / Peer review
- **检查 (Inspection)**: 正式的评审过程 / Formal review process

#### 4.3 评审角色和职责 / Review Roles and Responsibilities

**评审中的角色 / Roles in Reviews**:
- **作者 (Author)**: 创建被评审的制品 / Creates the work product being reviewed
- **评审者 (Reviewer)**: 检查制品并识别问题 / Examines the work product and identifies issues
- **记录员 (Recorder)**: 记录评审会议的结果 / Records the results of the review meeting
- **主持人 (Moderator)**: 引导评审过程 / Facilitates the review process

### 第五章：测试分析和设计 / Chapter 5: Test Analysis and Design

#### 5.1 测试技术概述 / Test Techniques Overview

**测试技术选择因素 / Factors for Choosing Test Techniques**:
- **时间和预算 / Time and budget**: 可用的测试时间和资源
- **组件或系统复杂性 / Component or system complexity**: 系统的复杂程度
- **风险水平和类型 / Risk levels and types**: 需要关注的风险类型
- **测试人员知识和技能 / Tester knowledge and skills**: 测试团队的能力
- **生命周期模型 / Lifecycle model**: 使用的开发模型
- **客户或合同要求 / Customer or contractual requirements**: 外部要求

**测试技术类别 / Categories of Test Techniques**:

1. **黑盒测试技术 (Black-box Test Techniques)**:
   - 基于功能规格说明 / Based on functional specifications
   - 不依赖内部结构 / Independent of internal structure
   - 从用户角度测试 / Testing from user perspective

2. **白盒测试技术 (White-box Test Techniques)**:
   - 基于代码结构 / Based on code structure
   - 需要了解内部实现 / Requires knowledge of internal implementation
   - 关注代码覆盖率 / Focus on code coverage

3. **基于经验的测试技术 (Experience-based Test Techniques)**:
   - 基于测试人员经验 / Based on tester experience
   - 包括探索性测试 / Includes exploratory testing
   - 利用领域知识 / Leverages domain knowledge

#### 5.2 黑盒测试技术 / Black-box Test Techniques

**等价类划分 (Equivalence Partitioning)**:
- **定义**: 将数据划分为分区（也称为等价类）的技术
- **原则**: 每个值必须属于且仅属于一个等价分区
- **类型**: 有效等价分区和无效等价分区

**边界值分析 (Boundary Value Analysis)**:
- **定义**: 边界值分析是等价类划分的扩展
- **使用条件**: 只能在分区有序时使用
- **特点**: 专注于边界条件的测试

**决策表测试 (Decision Table Testing)**:
- **定义**: 基于决策逻辑的测试技术
- **步骤**: 识别条件、创建条件组合、处理特殊情况、优化测试用例

**状态转换测试 (State Transition Testing)**:
- **定义**: 基于系统状态变化的测试
- **应用**: 适用于有明确状态转换的系统

#### 5.3 白盒测试技术 / White-box Test Techniques

**语句覆盖 (Statement Coverage)**:
- 确保每个语句至少执行一次 / Ensure each statement is executed at least once

**分支覆盖 (Branch Coverage)**:
- 确保每个分支至少执行一次 / Ensure each branch is executed at least once

**路径覆盖 (Path Coverage)**:
- 确保每个可能的执行路径都被测试 / Ensure each possible execution path is tested

#### 5.4 基于经验的测试技术 / Experience-based Test Techniques

**探索性测试 (Exploratory Testing)**:
- 同时进行测试设计、执行和学习 / Simultaneous test design, execution, and learning
- 基于测试人员的经验和直觉 / Based on tester experience and intuition

**错误推测 (Error Guessing)**:
- 基于经验预测可能的错误 / Predict possible errors based on experience
- 识别常见的缺陷模式 / Identify common defect patterns

### 第六章：测试管理 / Chapter 6: Test Management

#### 6.1 测试管理概述 / Test Management Overview

**测试管理的目标 / Test Management Objectives**:
- 确保测试活动按计划进行 / Ensure test activities proceed according to plan
- 管理测试资源和风险 / Manage test resources and risks
- 提供测试状态和结果报告 / Provide test status and results reporting

#### 6.2 测试计划 / Test Planning

**测试计划内容 / Test Plan Content**:
- 测试目标和范围 / Test objectives and scope
- 测试策略和方法 / Test strategy and approach
- 测试资源和时间安排 / Test resources and schedule
- 风险评估和缓解措施 / Risk assessment and mitigation

#### 6.3 测试监控和控制 / Test Monitoring and Control

**测试监控指标 / Test Monitoring Metrics**:
- 测试进度 / Test progress
- 缺陷发现率 / Defect discovery rate
- 测试覆盖率 / Test coverage
- 测试执行效率 / Test execution efficiency

**测试控制活动 / Test Control Activities**:
- 调整测试计划 / Adjust test plans
- 重新分配资源 / Reallocate resources
- 修改测试策略 / Modify test strategy

#### 6.4 测试估算 / Test Estimation

**估算技术 / Estimation Techniques**:
- **专家判断 (Expert Judgment)**: 基于经验进行估算
- **类比估算 (Analogy-based Estimation)**: 基于类似项目进行估算
- **参数化估算 (Parametric Estimation)**: 使用数学模型进行估算

**估算因素 / Estimation Factors**:
- 项目规模和复杂性 / Project size and complexity
- 团队经验和技能 / Team experience and skills
- 可用资源和时间 / Available resources and time
- 质量要求和风险 / Quality requirements and risks

### 第七章：测试工具 / Chapter 7: Test Tools

#### 7.1 测试工具概述 / Test Tools Overview

**测试工具分类 / Test Tool Categories**:
- **测试管理工具 (Test Management Tools)**: 管理测试过程和制品
- **需求管理工具 (Requirements Management Tools)**: 管理需求和可追溯性
- **缺陷管理工具 (Defect Management Tools)**: 跟踪和管理缺陷
- **测试执行工具 (Test Execution Tools)**: 自动化测试执行
- **性能测试工具 (Performance Testing Tools)**: 测试系统性能
- **静态分析工具 (Static Analysis Tools)**: 分析代码质量

#### 7.2 工具选择和实施 / Tool Selection and Implementation

**工具选择标准 / Tool Selection Criteria**:
- 功能需求 / Functional requirements
- 技术兼容性 / Technical compatibility
- 成本效益 / Cost-effectiveness
- 学习曲线 / Learning curve
- 支持和维护 / Support and maintenance

**工具实施步骤 / Tool Implementation Steps**:
1. 评估组织需求 / Assess organizational needs
2. 选择候选工具 / Select candidate tools
3. 进行概念验证 / Conduct proof of concept
4. 制定实施计划 / Develop implementation plan
5. 培训用户 / Train users
6. 部署和监控 / Deploy and monitor

#### 7.3 工具使用的最佳实践 / Best Practices for Tool Usage

**工具使用原则 / Tool Usage Principles**:
- 工具应该支持而不是替代测试过程 / Tools should support, not replace, the test process
- 确保工具适合项目需求 / Ensure tools fit project needs
- 提供适当的培训和支持 / Provide adequate training and support
- 定期评估工具效果 / Regularly evaluate tool effectiveness

## 重要概念对比 / Important Concept Comparisons

### 测试 vs 调试 / Testing vs Debugging

| 测试 (Testing) | 调试 (Debugging) |
|---|---|
| 执行/分析软件或硬件以识别缺陷 / Execution/analysis of software or hardware with the intent of identifying defects | 查找、分析和移除组件或系统中故障原因的过程 / The process of finding, analyzing and removing the causes of failures in a component or system |
| 不一定需要软件/硬件知识 / Software/hardware knowledge is not necessarily required | 必须理解编程语言才能进行调试过程 / Understanding of programming language is required to proceed with debugging |
| 质量保证活动 / Quality assurance activity | 缺陷修复活动 / Defect removal activity |

### 验证 vs 验证 / Verification vs Validation

| 验证 (Verification) | 验证 (Validation) |
|---|---|
| 确认工作产品满足其规格的过程 / The process of confirming that a work product fulfills its specification | 通过检查确认工作产品符合利益相关者的需求 / Confirmation by examination that a work product matches a stakeholder's needs |
| 确保产品按照需求和设计规格构建 / Ensures the product is built according to the requirements and design specifications | 确保最终产品满足预期用途和用户需求 / Ensures the final product meets the intended use and user requirements |
| 静态过程（评审、检查等）/ Static process (reviews, inspections, etc.) | 动态过程（产品的实际测试）/ Dynamic process (actual testing of the product) |
| 在开发阶段进行 / Conducted during the development phases | 在产品构建后进行 / Conducted after the product is built |
| "我们是否在正确构建产品？" / "Are we building the product right?" | "我们是否在构建正确的产品？" / "Are we building the right product?" |

### 错误、缺陷和故障 / Errors, Defects, and Failures

**定义 / Definitions**:
- **错误 (Error)**: 产生不正确结果的人为行为。同义词：mistake / A human action that produces an incorrect result. Synonyms: mistake
- **缺陷 (Defect)**: 工作产品中的不完美或缺陷，不符合其需求或规格。同义词：bug, fault / An imperfection or deficiency in a work product where it does not meet its requirements or specifications. Synonyms: bug, fault
- **故障 (Failure)**: 组件或系统在指定限制内不执行所需功能的事件 / An event in which a component or system does not perform a required function within specified limits

**关系链 / Relationship Chain**:
```
[故障 Failures] ← [缺陷 Defects] ← [错误 Errors]
```

## 考试题目练习 / Exam Question Practice

### 第一章题目 / Chapter 1 Questions

1. **问题**: 为什么需要测试？ / Why is testing necessary?
   - **答案**: C. 降低软件故障的风险 / To reduce the risk of software failure

2. **问题**: 以下哪项是测试的主要目标？ / Which of the following is a primary objective of testing?
   - **答案**: A. 为利益相关者提供信息 / To provide information for stakeholders

3. **问题**: 哪个测试原则指出测试永远不能完全证明没有缺陷？ / Which testing principle states that testing can never completely prove that there are no defects?
   - **答案**: D. 测试显示缺陷的存在 / Testing shows the presence of defects

4. **问题**: 以下哪项描述了软件缺陷的原因？ / Which of the following describes a cause of software defects?
   - **答案**: C. 开发过程中的复杂性和人为错误 / Complexity and human errors during development

### 第二章题目 / Chapter 2 Questions

1. **问题**: 以下哪项是测试管理角色的主要职责？ / Which of the following is a main responsibility of the test management role?
   - **答案**: C. 制定测试计划 / Develop test plans

2. **问题**: 可追溯性的主要价值是什么？ / What is the main value of traceability?
   - **答案**: B. 支持覆盖评估 / Support coverage evaluation

### 第三章题目 / Chapter 3 Questions

1. **问题**: V模型中，哪个阶段对应系统测试？ / In the V-model, which phase corresponds to system testing?
   - **答案**: B. 系统设计阶段 / System design phase

2. **问题**: 以下哪项是回归测试的主要目的？ / What is the main purpose of regression testing?
   - **答案**: A. 确保新变更没有破坏现有功能 / Ensure new changes don't break existing functionality

### 第四章题目 / Chapter 4 Questions

1. **问题**: 静态测试和动态测试的主要区别是什么？ / What is the main difference between static and dynamic testing?
   - **答案**: B. 静态测试直接发现缺陷，动态测试通过故障确定缺陷 / Static testing finds defects directly, while dynamic testing determines defects through failures

2. **问题**: 以下哪种评审类型最正式？ / Which of the following review types is most formal?
   - **答案**: D. 检查 / Inspection

### 第五章题目 / Chapter 5 Questions

1. **问题**: 等价类划分的主要目的是什么？ / What is the main purpose of equivalence partitioning?
   - **答案**: A. 减少测试用例数量 / Reduce the number of test cases

2. **问题**: 边界值分析可以用于哪种类型的数据？ / What type of data can boundary value analysis be used for?
   - **答案**: C. 有序数据 / Ordered data

3. **问题**: 决策表测试的主要优势是什么？ / What is the main advantage of decision table testing?
   - **答案**: B. 系统化处理复杂决策逻辑 / Systematic handling of complex decision logic

### 第六章题目 / Chapter 6 Questions

1. **问题**: 测试估算的主要目的是什么？ / What is the main purpose of test estimation?
   - **答案**: C. 确定测试活动所需的资源和时间 / Determine resources and time needed for test activities

2. **问题**: 以下哪项是测试监控的重要指标？ / Which of the following is an important metric for test monitoring?
   - **答案**: A. 缺陷发现率 / Defect discovery rate

### 第七章题目 / Chapter 7 Questions

1. **问题**: 测试工具选择时最重要的考虑因素是什么？ / What is the most important consideration when selecting test tools?
   - **答案**: B. 工具是否适合项目需求 / Whether the tool fits project needs

2. **问题**: 工具实施的第一步应该是什么？ / What should be the first step in tool implementation?
   - **答案**: A. 评估组织需求 / Assess organizational needs

## 学习进度 / Learning Progress

### 已完成内容 / Completed Content
- ✅ **第一章：测试基础 (Chapter 1: Testing Fundamentals)** - 100% 完成
- ✅ **第二章：测试活动和角色 (Chapter 2: Testing Activities and Roles)** - 100% 完成
- ✅ **第三章：软件生命周期中的测试 (Chapter 3: Testing Throughout Software Lifecycle)** - 100% 完成
- ✅ **第四章：静态测试 (Chapter 4: Static Testing)** - 100% 完成
- ✅ **第五章：测试分析和设计 (Chapter 5: Test Analysis and Design)** - 100% 完成
- ✅ **第六章：测试管理 (Chapter 6: Test Management)** - 100% 完成
- ✅ **第七章：测试工具 (Chapter 7: Test Tools)** - 100% 完成

### 学习状态 / Learning Status
- 🎯 **所有章节内容已提取完成** / All chapter content has been extracted
- 📚 **PPT内容已整理到Markdown文件** / PPT content has been organized into Markdown files
- 🔄 **准备进行复习和练习** / Ready for review and practice

## 学习技巧 / Study Tips

### 记忆技巧 / Memory Techniques
1. **七个测试原则**: 使用首字母缩写记忆 / Use acronyms to remember the seven testing principles
2. **测试活动**: 按顺序记忆7个活动 / Remember the 7 activities in order
3. **概念对比**: 制作对比表格帮助记忆 / Create comparison tables to help memory
4. **测试技术**: 按类别记忆黑盒、白盒、基于经验的技术 / Remember test techniques by category: black-box, white-box, experience-based

### 复习策略 / Review Strategy
1. **每日复习**: 重点概念和原则 / Daily review of key concepts and principles
2. **每周总结**: 章节内容总结 / Weekly summary of chapter content
3. **模拟考试**: 定期进行题目练习 / Regular mock exam practice
4. **实践应用**: 将理论应用到实际项目中 / Apply theory to actual projects

## 重要资源 / Important Resources

### 官方资源 / Official Resources
- ISTQB术语表 / ISTQB Glossary: https://glossary.istqb.org/en_US/
- 官方学习材料 / Official learning materials
- 在线练习题库 / Online practice question banks

### 参考资料 / Reference Materials
- V-Model: https://en.wikipedia.org/wiki/V-Model
- ASPICE: https://www.invensity.com/wp-content/uploads/2023/09/ASPICE-process-landscape.webp
- 测试目标: https://senuri.medium.com/objectives-of-testing-4832858f6f7d
- 测试vs调试: https://www.javatpoint.com/testing-vs-debugging
- 测试vs质量保证: 
  - https://www.triad.co.uk/news/testing-vs-qa/
  - https://blog.qatestlab.com/2011/04/07/what-is-the-difference-between-qa-and-testing/
- ISO 26262: https://model-engineers.com/en/iso-26262/
- 测试时间估算: https://www.apriorit.com/qa-blog/197-testing-time-estimation
- 软件测试心理学: https://www.slideshare.net/HcmcStc/hoang-nguyen-the-psychology-in-software-testing
- 双向可追溯性: https://www.researchgate.net/figure/Bidirectional-traceability-and-consistency-requirements-of-Automotive-SPICE-v30-5_fig1_319061671
- 项目角色和职责: https://confluence.technica-engineering.net/display/SQA/Project+Roles+and+Responsibilities
- 等价类划分: https://en.wikipedia.org/wiki/Equivalence_partitioning/
- 边界值分析: https://bookdown.org/joshuah40/qa_code/testing-frameworks.html
- 决策表测试: https://www.stickyminds.com/article/using-decision-tables-clear-well-designed-testing
- 状态转换测试: https://www.guru99.com/state-transition-testing.html
- 评审过程: https://www.qualitenpress.com/journals/peer-review-process/
- 单元测试: https://blog.autify.com/what-is-unit-testing/

## 下一步计划 / Next Steps

### 短期目标 (1-2周) / Short-term Goals (1-2 weeks)
- [ ] 复习所有章节内容 / Review all chapter content
- [ ] 进行模拟考试练习 / Conduct mock exam practice
- [ ] 准备认证考试 / Prepare for certification exam
- [ ] 整理重点知识点 / Organize key knowledge points

### 中期目标 (1个月) / Medium-term Goals (1 month)
- [ ] 通过ISTQB Foundation认证 / Pass ISTQB Foundation certification
- [ ] 开始ISTQB高级认证学习 / Start ISTQB Advanced certification learning
- [ ] 应用测试知识到实际项目中 / Apply testing knowledge to actual projects

---

*最后更新 / Last Updated: 2025年1月27日 / January 27, 2025* 