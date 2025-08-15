# ISTQB Foundation - 测试分析和设计 / Test Analysis and Design

## 概述 / Overview
- **课程 / Course**: ISTQB Foundation - Test Analysis and Design
- **机构 / Organization**: Technica Engineering GmbH
- **日期 / Date**: 2025年1月27日 / January 27, 2025
- **章节 / Chapter**: 测试分析和设计 / Test Analysis and Design

## 学习目标 / Learning Objectives

### 4.1 测试技术概述 / Test Techniques Overview
#### FL-4.1.1 (K2) 区分黑盒、白盒和基于经验的测试技术 / Distinguish black-box, white-box and experience-based test techniques

### 4.2 黑盒测试技术 / Black-box Test Techniques
#### FL-4.2.1 (K3) 使用等价类划分来推导测试用例 / Use equivalence partitioning to derive test cases
#### FL-4.2.2 (K3) 使用边界值分析来推导测试用例 / Use boundary value analysis to derive test cases
#### FL-4.2.3 (K3) 使用决策表测试来推导测试用例 / Use decision table testing to derive test cases
#### FL-4.2.4 (K3) 使用状态转换测试来推导测试用例 / Use state transition testing to derive test cases

### 4.3 白盒测试技术 / White-box Test Techniques
#### FL-4.3.1 (K3) 使用语句覆盖来推导测试用例 / Use statement coverage to derive test cases
#### FL-4.3.2 (K3) 使用分支覆盖来推导测试用例 / Use branch coverage to derive test cases
#### FL-4.3.3 (K3) 使用路径覆盖来推导测试用例 / Use path coverage to derive test cases

### 4.4 基于经验的测试技术 / Experience-based Test Techniques
#### FL-4.4.1 (K2) 解释探索性测试的特点 / Explain the characteristics of exploratory testing
#### FL-4.4.2 (K2) 解释错误推测的特点 / Explain the characteristics of error guessing

### 4.5 测试技术应用 / Test Technique Application
#### FL-4.5.1 (K2) 解释如何选择合适的测试技术 / Explain how to select appropriate test techniques
#### FL-4.5.2 (K2) 解释测试技术的优缺点 / Explain the advantages and disadvantages of test techniques

### 4.6 测试用例设计 / Test Case Design
#### FL-4.6.1 (K3) 设计有效的测试用例 / Design effective test cases
#### FL-4.6.2 (K2) 评估测试用例质量 / Evaluate test case quality

## 主要内容 / Main Content

### 1. 测试技术概述 / Test Techniques Overview

#### 1.1 测试技术选择因素 / Factors for Choosing Test Techniques

**定义 / Definition**: 测试技术选择需要考虑多个因素，以确保选择最适合的技术 / Test technique selection depends on multiple factors to ensure the most appropriate technique is chosen

**选择因素 / Selection Factors**:
- **时间和预算 / Time and budget**: 可用的测试时间和资源限制
- **组件或系统复杂性 / Component or system complexity**: 系统的复杂程度和规模
- **风险水平和类型 / Risk levels and types**: 需要关注的风险类型和严重程度
- **测试人员知识和技能 / Tester knowledge and skills**: 测试团队的技术能力和经验
- **生命周期模型 / Lifecycle model**: 使用的软件开发模型
- **客户或合同要求 / Customer or contractual requirements**: 外部利益相关者的要求

#### 1.2 测试技术分类 / Test Technique Categories

**黑盒测试技术 (Black-box Test Techniques)**:
- **定义**: 基于功能规格说明，不依赖内部结构的测试技术 / Test techniques based on functional specifications, independent of internal structure
- **特点**: 从用户角度测试、不需要编程知识 / Testing from user perspective, no programming knowledge required
- **适用场景**: 功能测试、验收测试 / Functional testing, acceptance testing
- **优势**: 客观、用户导向、易于理解 / Objective, user-oriented, easy to understand

**白盒测试技术 (White-box Test Techniques)**:
- **定义**: 基于代码结构，需要了解内部实现的测试技术 / Test techniques based on code structure, requiring knowledge of internal implementation
- **特点**: 关注代码覆盖率、需要编程知识 / Focus on code coverage, programming knowledge required
- **适用场景**: 单元测试、集成测试 / Unit testing, integration testing
- **优势**: 高覆盖率、发现深层缺陷 / High coverage, find deep defects

**基于经验的测试技术 (Experience-based Test Techniques)**:
- **定义**: 基于测试人员经验和领域知识的测试技术 / Test techniques based on tester experience and domain knowledge
- **特点**: 包括探索性测试、利用直觉和创造力 / Includes exploratory testing, leverages intuition and creativity
- **适用场景**: 复杂系统、新功能测试 / Complex systems, new feature testing
- **优势**: 灵活、适应性强、发现意外缺陷 / Flexible, adaptive, find unexpected defects

### 2. 黑盒测试技术 / Black-box Test Techniques

#### 2.1 等价类划分 (Equivalence Partitioning) / Equivalence Partitioning

**定义 / Definition**: 将数据划分为分区（也称为等价类）的技术，每个分区中的值在测试中表现相同 / Technique that divides data into partitions (equivalence classes) where values in each partition behave the same way in testing

**核心原则 / Core Principles**:
- 对于与测试对象相关的任何数据元素 / For any data element related to the test object
- 如果需要，可以进一步细分 / Sub-partitions if required
- 每个值必须属于且仅属于一个等价分区 / Each value must belong to one and only one equivalence partition

**等价分区类型 / Types of Equivalence Partitions**:

**有效等价分区 (Valid Equivalence Partition)**:
- **定义**: 符合规格说明的数据 / Data that conforms to specifications
- **特点**: 应该被系统正确处理 / Should be processed correctly by the system
- **测试目标**: 验证正常功能 / Verify normal functionality
- **示例**: 有效用户名、有效密码 / Valid username, valid password

**无效等价分区 (Invalid Equivalence Partition)**:
- **定义**: 不符合规格说明的数据 / Data that does not conform to specifications
- **特点**: 应该被系统拒绝或错误处理 / Should be rejected or error-handled by the system
- **测试目标**: 验证错误处理 / Verify error handling
- **示例**: 无效用户名、无效密码 / Invalid username, invalid password

#### 2.2 边界值分析 (Boundary Value Analysis) / Boundary Value Analysis

**定义 / Definition**: 边界值分析是等价类划分的扩展，专注于边界条件的测试 / Boundary value analysis (BVA) is an extension of equivalence partitioning, focusing on boundary conditions

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

#### 2.4 状态转换测试 (State Transition Testing) / State Transition Testing

**定义 / Definition**: 基于系统状态变化的测试技术，适用于有明确状态转换的系统 / Testing technique based on system state changes, applicable to systems with clear state transitions

**状态转换概念 / State Transition Concepts**:

**状态 (State)**:
- **定义**: 系统在特定时刻的条件或模式 / System condition or mode at a specific moment
- **特点**: 相对稳定、可识别 / Relatively stable, identifiable
- **示例**: 登录状态、文件打开状态 / Logged in state, file open state

**事件 (Event)**:
- **定义**: 触发状态转换的输入或操作 / Input or action that triggers state transition
- **特点**: 外部触发、可控制 / Externally triggered, controllable
- **示例**: 用户点击、系统超时 / User click, system timeout

### 3. 白盒测试技术 / White-box Test Techniques

#### 3.1 白盒测试概述 / White-box Testing Overview

**定义 / Definition**: 白盒测试是基于代码结构的测试技术，需要了解内部实现 / White-box testing is test techniques based on code structure, requiring knowledge of internal implementation

**核心特征 / Core Characteristics**:
- 基于代码结构 / Based on code structure
- 需要了解内部实现 / Requires knowledge of internal implementation
- 关注代码覆盖率 / Focus on code coverage
- 需要编程知识 / Requires programming knowledge

#### 3.2 代码覆盖率 / Code Coverage

**定义 / Definition**: 代码覆盖率是衡量测试执行代码程度的指标 / Code coverage is a metric that measures the extent to which tests execute code

**覆盖率类型 / Coverage Types**:

**语句覆盖 (Statement Coverage)**:
- **定义**: 确保每个语句至少执行一次 / Ensure each statement is executed at least once
- **目标**: 100%语句覆盖率 / 100% statement coverage
- **优势**: 简单、易于理解 / Simple, easy to understand
- **局限性**: 可能遗漏分支和路径 / May miss branches and paths

**分支覆盖 (Branch Coverage)**:
- **定义**: 确保每个分支至少执行一次 / Ensure each branch is executed at least once
- **目标**: 100%分支覆盖率 / 100% branch coverage
- **优势**: 比语句覆盖更全面 / More comprehensive than statement coverage
- **局限性**: 可能遗漏复杂路径 / May miss complex paths

**路径覆盖 (Path Coverage)**:
- **定义**: 确保每个可能的执行路径都被测试 / Ensure each possible execution path is tested
- **目标**: 100%路径覆盖率 / 100% path coverage
- **优势**: 最全面的覆盖率 / Most comprehensive coverage
- **局限性**: 路径数量可能非常大 / Number of paths can be very large

### 4. 基于经验的测试技术 / Experience-based Test Techniques

#### 4.1 基于经验的测试概述 / Experience-based Testing Overview

**定义 / Definition**: 基于经验的测试技术利用测试人员的经验、直觉和领域知识来设计测试 / Experience-based test techniques leverage tester experience, intuition, and domain knowledge to design tests

**核心特征 / Core Characteristics**:
- 基于测试人员经验 / Based on tester experience
- 利用直觉和创造力 / Leverages intuition and creativity
- 适应性强、灵活 / Adaptive and flexible
- 发现意外缺陷 / Find unexpected defects

#### 4.2 探索性测试 (Exploratory Testing) / Exploratory Testing

**定义 / Definition**: 探索性测试是同时进行测试设计、执行和学习的测试方法 / Exploratory testing is a testing approach that simultaneously performs test design, execution, and learning

**探索性测试特征 / Exploratory Testing Characteristics**:

**同时进行设计、执行和学习 / Simultaneous Design, Execution, and Learning**:
- **测试设计**: 在测试过程中设计测试用例 / Design test cases during testing
- **测试执行**: 立即执行设计的测试用例 / Execute designed test cases immediately
- **学习过程**: 从测试结果中学习并调整策略 / Learn from test results and adjust strategy

#### 4.3 错误推测 (Error Guessing) / Error Guessing

**定义 / Definition**: 错误推测是基于测试人员经验预测可能的错误和缺陷的测试技术 / Error guessing is a test technique based on tester experience to predict possible errors and defects

**错误推测原理 / Error Guessing Principles**:

**基于经验预测 / Experience-based Prediction**:
- **历史经验**: 基于以往项目中遇到的错误 / Based on errors encountered in previous projects
- **领域知识**: 利用特定领域的专业知识 / Leverage domain-specific expertise
- **直觉判断**: 基于直觉识别潜在问题 / Identify potential issues based on intuition

### 5. 测试技术应用策略 / Test Technique Application Strategy

#### 5.1 技术选择框架 / Technique Selection Framework

**选择标准 / Selection Criteria**:

**项目特征 / Project Characteristics**:
- **项目规模**: 大型项目可能需要更全面的技术组合 / Large projects may need comprehensive technique combinations
- **项目复杂度**: 复杂项目需要更严格的测试方法 / Complex projects need stricter testing approaches
- **项目风险**: 高风险项目需要更严格的验证 / High-risk projects need stricter verification
- **项目时间**: 时间限制影响技术选择的深度 / Time constraints affect depth of technique selection

#### 5.2 技术组合策略 / Technique Combination Strategy

**互补使用原则 / Complementary Usage Principles**:

**黑盒与白盒技术结合 / Combining Black-box and White-box Techniques**:
- **功能验证**: 使用黑盒技术验证功能正确性 / Use black-box techniques to verify functional correctness
- **结构验证**: 使用白盒技术验证代码结构 / Use white-box techniques to verify code structure
- **覆盖增强**: 结合使用提高测试覆盖率 / Combine to improve test coverage

### 6. 测试用例设计 / Test Case Design

#### 6.1 测试用例设计原则 / Test Case Design Principles

**设计原则 / Design Principles**:

**完整性原则 / Completeness Principle**:
- **覆盖全面**: 测试用例应该覆盖所有重要场景 / Test cases should cover all important scenarios
- **边界覆盖**: 包括边界条件和异常情况 / Include boundary conditions and exception cases
- **路径覆盖**: 覆盖所有重要的执行路径 / Cover all important execution paths

**有效性原则 / Effectiveness Principle**:
- **明确目标**: 每个测试用例都有明确的测试目标 / Each test case has clear testing objectives
- **可验证性**: 测试结果可以明确验证 / Test results can be clearly verified
- **可重复性**: 测试用例可以重复执行 / Test cases can be repeated

#### 6.2 测试用例设计步骤 / Test Case Design Steps

**步骤1: 需求分析 / Step 1: Requirements Analysis**:
- **理解需求**: 深入理解测试对象的需求 / Deeply understand test object requirements
- **识别功能**: 识别所有需要测试的功能 / Identify all functions that need testing
- **分析约束**: 分析测试的约束条件 / Analyze testing constraints

**步骤2: 技术选择 / Step 2: Technique Selection**:
- **选择技术**: 根据需求选择合适的测试技术 / Select appropriate test techniques based on requirements
- **技术组合**: 考虑技术的组合使用 / Consider combination of techniques
- **工具支持**: 选择支持工具和框架 / Select supporting tools and frameworks

**步骤3: 用例设计 / Step 3: Test Case Design**:
- **设计用例**: 使用选定的技术设计测试用例 / Design test cases using selected techniques
- **数据准备**: 准备测试数据和环境 / Prepare test data and environment
- **预期结果**: 定义预期的测试结果 / Define expected test results

## 考试题目示例 / Exam Question Examples

### 考试题1 / Exam Question 1
**问题 / Question**: 等价类划分的主要目的是什么？/ What is the main purpose of equivalence partitioning?
- A. 减少测试用例数量 / Reduce the number of test cases
- B. 增加测试覆盖率 / Increase test coverage
- C. 提高测试执行速度 / Improve test execution speed
- D. 简化测试设计 / Simplify test design

**答案 / Answer**: A. 减少测试用例数量 / Reduce the number of test cases

**解释 / Explanation**: 等价类划分通过将输入域划分为等价分区，从每个分区选择代表性值，从而减少测试用例数量，同时保持测试的有效性。

### 考试题2 / Exam Question 2
**问题 / Question**: 边界值分析可以用于哪种类型的数据？/ What type of data can boundary value analysis be used for?
- A. 任何类型的数据 / Any type of data
- B. 无序数据 / Unordered data
- C. 有序数据 / Ordered data
- D. 随机数据 / Random data

**答案 / Answer**: C. 有序数据 / Ordered data

**解释 / Explanation**: 边界值分析只能用于有序数据，因为它需要识别数据的最小值和最大值作为边界。

### 考试题3 / Exam Question 3
**问题 / Question**: 探索性测试的主要特点是什么？/ What is the main characteristic of exploratory testing?
- A. 使用预定义的测试脚本 / Use predefined test scripts
- B. 同时进行测试设计、执行和学习 / Simultaneous test design, execution, and learning
- C. 完全自动化执行 / Completely automated execution
- D. 基于详细的测试计划 / Based on detailed test plans

**答案 / Answer**: B. 同时进行测试设计、执行和学习 / Simultaneous test design, execution, and learning

**解释 / Explanation**: 探索性测试的核心特点是同时进行测试设计、执行和学习，测试人员根据测试结果实时调整测试策略。

### 考试题4 / Exam Question 4
**问题 / Question**: 语句覆盖的主要目标是什么？/ What is the main objective of statement coverage?
- A. 确保每个分支至少执行一次 / Ensure each branch is executed at least once
- B. 确保每个语句至少执行一次 / Ensure each statement is executed at least once
- C. 确保每个路径至少执行一次 / Ensure each path is executed at least once
- D. 确保每个函数至少调用一次 / Ensure each function is called at least once

**答案 / Answer**: B. 确保每个语句至少执行一次 / Ensure each statement is executed at least once

**解释 / Explanation**: 语句覆盖的目标是确保程序中的每个可执行语句至少被执行一次，这是最基本的代码覆盖率要求。

## 重要概念总结 / Key Concepts Summary

### 测试技术分类 / Test Technique Categories
- **黑盒测试技术**: 基于功能规格，不依赖内部结构 / Based on functional specifications, independent of internal structure
- **白盒测试技术**: 基于代码结构，需要了解内部实现 / Based on code structure, requires knowledge of internal implementation
- **基于经验的测试技术**: 基于测试人员经验和领域知识 / Based on tester experience and domain knowledge

### 黑盒测试技术 / Black-box Test Techniques
- **等价类划分**: 将数据划分为有效和无效分区 / Divides data into valid and invalid partitions
- **边界值分析**: 专注于边界条件的测试 / Focuses on boundary conditions
- **决策表测试**: 系统化处理复杂决策逻辑 / Systematic handling of complex decision logic
- **状态转换测试**: 基于系统状态变化的测试 / Testing based on system state changes

### 白盒测试技术 / White-box Test Techniques
- **语句覆盖**: 确保每个语句至少执行一次 / Ensure each statement is executed at least once
- **分支覆盖**: 确保每个分支至少执行一次 / Ensure each branch is executed at least once
- **路径覆盖**: 确保每个可能的执行路径都被测试 / Ensure each possible execution path is tested

### 基于经验的测试技术 / Experience-based Test Techniques
- **探索性测试**: 同时进行测试设计、执行和学习 / Simultaneous test design, execution, and learning
- **错误推测**: 基于经验预测可能的错误 / Predict possible errors based on experience

## 参考资料 / References
- 等价类划分: https://en.wikipedia.org/wiki/Equivalence_partitioning/
- 边界值分析: https://bookdown.org/joshuah40/qa_code/testing-frameworks.html
- 决策表测试: https://www.stickyminds.com/article/using-decision-tables-clear-well-designed-testing
- 状态转换测试: https://www.guru99.com/state-transition-testing.html
- 黑盒测试: https://www.imperva.com/learn/application-security/black-box-testing
- 白盒测试: https://www.guru99.com/white-box-testing.html
- 探索性测试: https://www.satisfice.com/exploratory-testing
- 错误推测: https://www.softwaretestinghelp.com/error-guessing-testing-technique/ 