# ISTQB Foundation - 测试分析和设计 / Test Analysis and Design

## 概述 / Overview
- **课程 / Course**: ISTQB Foundation - Test Analysis & Design
- **机构 / Organization**: Technica Engineering GmbH
- **日期 / Date**: 2025年2月21日 / February 21, 2025
- **章节 / Chapter**: 测试分析和设计 / Test Analysis and Design

## 学习目标 / Learning Objectives

### 4.1 测试技术概述 / Test Techniques Overview
#### FL-4.1.1 (K2) 区分黑盒、白盒和基于经验的测试技术 / Distinguish black-box, white-box and experience-based test techniques

### 4.2 黑盒测试技术 / Black-box Test Techniques
#### FL-4.2.1 (K3) 使用等价类划分来推导测试用例 / Use equivalence partitioning to derive test cases
#### FL-4.2.2 (K3) 使用边界值分析来推导测试用例 / Use boundary value analysis to derive test cases
#### FL-4.2.3 (K3) 使用决策表测试来推导测试用例 / Use decision table testing to derive test cases
#### FL-4.2.4 (K3) 使用状态转换测试来推导测试用例 / Use state transition testing to derive test cases

## 主要内容 / Main Content

### 1. 测试技术概述 / Test Techniques Overview

#### 测试技术选择因素 / Factors for Choosing Test Techniques
选择使用哪些测试技术时需要考虑的因素 / The choice of which test techniques to use depends on:

- **时间和预算 / Time and budget**
- **组件或系统复杂性 / Component or system complexity**
- **风险水平和类型 / Risk levels and types**
- **测试人员知识和技能 / Tester knowledge and skills**
- **生命周期模型 / Lifecycle model**
- **客户或合同要求 / Customer or contractual requirements**

#### 测试技术类别及其特征 / Categories of Test Techniques and Their Characteristics

1. **黑盒测试技术 (Black-box Test Techniques)** / Black-box Test Techniques
   - 基于功能规格说明 / Based on functional specifications
   - 不依赖内部结构 / Independent of internal structure
   - 从用户角度测试 / Testing from user perspective

2. **白盒测试技术 (White-box Test Techniques)** / White-box Test Techniques
   - 基于代码结构 / Based on code structure
   - 需要了解内部实现 / Requires knowledge of internal implementation
   - 关注代码覆盖率 / Focus on code coverage

3. **基于经验的测试技术 (Experience-based Test Techniques)** / Experience-based Test Techniques
   - 基于测试人员经验 / Based on tester experience
   - 包括探索性测试 / Includes exploratory testing
   - 利用领域知识 / Leverages domain knowledge

### 2. 黑盒测试技术 / Black-box Test Techniques

#### 2.1 等价类划分 (Equivalence Partitioning) / Equivalence Partitioning

**定义 / Definition**: 将数据划分为分区（也称为等价类）的技术 / Technique that divides data into partitions (also known as equivalence classes)

**原则 / Principles**:
- 对于与测试对象相关的任何数据元素 / For any data element related to the test object
- 如果需要，可以进一步细分 / Sub partitions if required
- 每个值必须属于且仅属于一个等价分区 / Each value must belong to one and only one equivalence partition

**等价分区类型 / Types of Equivalence Partitions**:
- **有效等价分区 (Valid equivalence partition)**: 符合规格说明的数据 / Data that conforms to specifications
- **无效等价分区 (Invalid equivalence partition)**: 不符合规格说明的数据 / Data that does not conform to specifications

#### 2.2 边界值分析 (Boundary Value Analysis) / Boundary Value Analysis

**定义 / Definition**: 边界值分析是等价类划分的扩展 / Boundary value analysis (BVA) is an extension of equivalence partitioning

**使用条件 / Usage Conditions**:
- 只能在分区有序时使用 / Can only be used when the partition is ordered
- 适用于数值或顺序数据 / Numeric or sequential data
- 分区的最小值和最大值是其边界值 / The minimum and maximum values of a partition are its boundary values

**边界值 vs 等价类 / Boundary vs. Equivalence**:
- 边界值分析专注于边界条件 / Boundary value analysis focuses on boundary conditions
- 等价类划分关注数据分组 / Equivalence partitioning focuses on data grouping

#### 2.3 决策表测试 (Decision Table Testing) / Decision Table Testing

**定义 / Definition**: 基于决策逻辑的测试技术 / Testing technique based on decision logic

**决策表设计步骤 / Decision Table Design Steps**:

**步骤1: 识别条件 / Step 1: Identify Conditions**
对于测试情况，有四个潜在条件 / For the situation under test, there are four potential conditions:
- ID是否有效？是或否？/ ID is valid— yes or no?
- 密码是否有效？是或否？/ Password is valid— yes or no?
- 是否有三次无效密码尝试？是或否？/ There have been three invalid password attempts— yes or no?
- 是否授予系统访问权限？是或否？/ Access to system is granted— yes or no?

**步骤2: 创建条件组合 / Step 2: Create Condition Combinations**
- 考虑所有可能的条件组合 / Consider all possible condition combinations
- 识别有效和无效的组合 / Identify valid and invalid combinations

**步骤3: 处理特殊情况 / Step 3: Handle Special Cases**
- 账户因3次无效密码尝试而被阻止 / Account was blocked due to 3 invalid PW attempts
- 但仍然尝试登录 / But you still try to login

**步骤4: 优化测试用例 / Step 4: Optimize Test Cases**
- 测试用例从十六个减少到仅五个 / Test cases reduction from sixteen down to just five
- 减少了近70% / A reduction of nearly 70 percent!

#### 2.4 状态转换测试 (State Transition Testing) / State Transition Testing

**定义 / Definition**: 基于系统状态变化的测试技术 / Testing technique based on system state changes

**特点 / Characteristics**:
- 关注系统状态转换 / Focus on system state transitions
- 测试状态转换的有效性 / Test validity of state transitions
- 验证状态转换的完整性 / Verify completeness of state transitions

### 3. 静态测试基础 / Static Testing Basics

#### 静态测试 vs 动态测试 / Static Testing vs Dynamic Testing

**静态测试 (Static Testing)** / Static Testing:
- 直接发现缺陷 / Finds defects directly
- 不涉及软件执行 / Does not involve software execution
- 包括评审和静态分析 / Includes reviews and static analysis

**动态测试 (Dynamic Testing)** / Dynamic Testing:
- 通过故障确定缺陷 / Determines defects through failures
- 涉及软件执行 / Involves software execution
- 需要后续分析 / Requires subsequent analysis

#### 评审类型 / Review Types

**评审类型包括 / Review types include**:
- 非正式评审 (Informal Review) / Informal Review
- 走查 (Walkthrough) / Walkthrough
- 技术评审 (Technical Review) / Technical Review
- 检查 (Inspection) / Inspection

#### 角色和职责 / Roles and Responsibilities

**评审中的角色 / Roles in Reviews**:
- 作者 (Author) / Author
- 评审者 (Reviewer) / Reviewer
- 记录员 (Recorder) / Recorder
- 主持人 (Moderator) / Moderator

### 4. 软件生命周期中的测试 - V模型 / Testing in Software Lifecycle - V-Model

#### V模型概述 / V-Model Overview
- 需求分析阶段对应验收测试 / Requirements analysis phase corresponds to acceptance testing
- 系统设计阶段对应系统测试 / System design phase corresponds to system testing
- 架构设计阶段对应集成测试 / Architecture design phase corresponds to integration testing
- 模块设计阶段对应组件测试 / Module design phase corresponds to component testing

## 考试题目示例 / Exam Question Examples

### 考试题1 / Exam Question 1
**问题 / Question**: 等价类划分的主要目的是什么？/ What is the main purpose of equivalence partitioning?
- A. 减少测试用例数量 / Reduce the number of test cases
- B. 增加测试覆盖率 / Increase test coverage
- C. 提高测试执行速度 / Improve test execution speed
- D. 简化测试设计 / Simplify test design

**答案 / Answer**: A

### 考试题2 / Exam Question 2
**问题 / Question**: 边界值分析可以用于哪种类型的数据？/ What type of data can boundary value analysis be used for?
- A. 任何类型的数据 / Any type of data
- B. 无序数据 / Unordered data
- C. 有序数据 / Ordered data
- D. 随机数据 / Random data

**答案 / Answer**: C

### 考试题3 / Exam Question 3
**问题 / Question**: 决策表测试的主要优势是什么？/ What is the main advantage of decision table testing?
- A. 减少测试时间 / Reduce testing time
- B. 系统化处理复杂决策逻辑 / Systematic handling of complex decision logic
- C. 提高测试自动化程度 / Improve test automation
- D. 降低测试成本 / Reduce testing costs

**答案 / Answer**: B

### 考试题4 / Exam Question 4
**问题 / Question**: 静态测试和动态测试的主要区别是什么？/ What is the main difference between static and dynamic testing?
- A. 静态测试更快 / Static testing is faster
- B. 静态测试直接发现缺陷，动态测试通过故障确定缺陷 / Static testing finds defects directly, while dynamic testing determines defects through failures
- C. 动态测试更准确 / Dynamic testing is more accurate
- D. 静态测试成本更低 / Static testing costs less

**答案 / Answer**: B

## 重要概念总结 / Key Concepts Summary

### 测试技术分类 / Test Technique Categories
- **黑盒测试技术**: 基于功能规格，不依赖内部结构 / Black-box: Based on functional specifications, independent of internal structure
- **白盒测试技术**: 基于代码结构，需要了解内部实现 / White-box: Based on code structure, requires knowledge of internal implementation
- **基于经验的测试技术**: 基于测试人员经验和领域知识 / Experience-based: Based on tester experience and domain knowledge

### 黑盒测试技术 / Black-box Test Techniques
- **等价类划分**: 将数据划分为有效和无效分区 / Equivalence partitioning: Divides data into valid and invalid partitions
- **边界值分析**: 专注于边界条件的测试 / Boundary value analysis: Focuses on boundary conditions
- **决策表测试**: 系统化处理复杂决策逻辑 / Decision table testing: Systematic handling of complex decision logic
- **状态转换测试**: 基于系统状态变化的测试 / State transition testing: Testing based on system state changes

### 静态测试 / Static Testing
- 直接发现缺陷，不涉及软件执行 / Finds defects directly, does not involve software execution
- 包括评审、走查、技术评审、检查等 / Includes reviews, walkthroughs, technical reviews, inspections
- 与动态测试互补 / Complementary to dynamic testing

## 参考资料 / References
- 等价类划分 / Equivalence Partitioning: 
  - https://en.wikipedia.org/wiki/Equivalence_partitioning/
  - https://www.educba.com/equivalence-partitioning/
  - https://www.imperva.com/learn/application-security/black-box-testing
- 边界值分析 / Boundary Value Analysis: https://bookdown.org/joshuah40/qa_code/testing-frameworks.html
- 边界 vs 等价类 / Boundary vs. Equivalence: https://www.semanticscholar.org/paper/A-Comparative-Analysis-On-Equivalence-class-And-Akshatha-Illango
- 决策表测试 / Decision Table Testing: https://www.stickyminds.com/article/using-decision-tables-clear-well-designed-testing
- 状态转换测试 / State Transition Testing: https://www.guru99.com/state-transition-testing.html
- V模型 / V-Model: https://www.invensity.com/wp-content/uploads/2023/09/ASPICE-process-landscape.webp
- 评审过程 / Review Process: https://www.qualitenpress.com/journals/peer-review-process/
- 单元测试 / Unit Testing: https://blog.autify.com/what-is-unit-testing/ 