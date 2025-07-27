# ISTQB Foundation - 测试基础 / Testing Fundamentals

## 概述 / Overview
- **课程 / Course**: ISTQB Foundation - Fundaments of testing 1
- **机构 / Organization**: Technica Engineering GmbH
- **日期 / Date**: 2025年1月10日 / January 10, 2025
- **考试结构 / Exam Structure**: 40题，总分40分，及格分数26分(65%)，考试时长60分钟(+25%非母语时间)
- **Exam Structure**: 40 questions, 40 total points, passing score 26 (65%), exam duration 60 minutes (+25% for non-native language)

## 主要内容 / Main Content

### 1. 什么是测试 / What is Testing

#### 测试定义 / Testing Definition
测试是一套活动，用于发现缺陷并评估软件制品的质量。这些被测试的制品被称为测试对象(test object)。

**English**: Testing is a set of activities to discover defects and evaluate the quality of software artifacts. These artifacts, when being tested, are known as test objects.

#### 测试活动包括 / Testing Activities Include
- 测试计划 (test planning)
- 需求分析 (requirement analysis)
- 设计 (designing)
- 实施/执行/分析测试 (implementing/executing/analyzing tests)
- 评审 (reviewing)
- 报告结果 (reporting results)
- 评估测试对象的质量 (evaluating the quality of a test object)

#### 测试类型 / Types of Testing
- **动态测试 (Dynamic testing)**: 涉及软件执行 / involves the execution of software
- **静态测试 (Static testing)**: 不涉及软件执行，包括评审和静态分析 / does not involve software execution, includes reviews and static analysis

### 2. 测试目标 / Objectives of Testing

#### 典型测试目标 / Typical Test Objectives
- 评估工作产品（如需求、用户故事、设计和代码） / Evaluating work products such as requirements, user stories, designs, and code
- 触发故障并发现缺陷 / Triggering failures and finding defects
- 确保测试对象的所需覆盖率 / Ensuring required coverage of a test object
- 降低软件质量不足的风险 / Reducing the level of risk of inadequate software quality
- 验证是否满足指定需求 / Verifying whether specified requirements have been fulfilled
- 验证测试对象是否符合合同、法律和监管要求 / Verifying that a test object complies with contractual, legal, and regulatory requirements
- 为利益相关者提供信息以做出明智决策 / Providing information to stakeholders to allow them to make informed decisions
- 建立对测试对象质量的信心 / Building confidence in the quality of the test object
- 验证测试对象是否完整并按利益相关者预期工作 / Validating whether the test object is complete and works as expected by the stakeholders

#### 不同测试级别的目标 / Different Objectives during Different Levels of Testing
- **组件测试 / Component Testing**: 尽可能多地发现故障，以便及早识别和修复底层缺陷 / finding as many failures as possible so that the underlying defects are identified and fixed early
- **验收测试 / Acceptance Testing**: 确认系统按预期工作并满足需求，为利益相关者提供发布风险信息 / confirming that the system works as expected and satisfies requirements, giving information to stakeholders about the risk of releasing the system

### 3. 测试与调试的区别 / Testing vs. Debugging

| 测试 (Testing) | 调试 (Debugging) |
|---|---|
| 执行/分析软件或硬件以识别缺陷 / Execution/analysis of software or hardware with the intent of identifying defects | 查找、分析和移除组件或系统中故障原因的过程 / The process of finding, analyzing and removing the causes of failures in a component or system |
| 不一定需要软件/硬件知识 / Software/hardware knowledge is not necessarily required | 必须理解编程语言才能进行调试过程 / Understanding of programming language is required to proceed with debugging |
| 质量保证活动 / Quality assurance activity | 缺陷修复活动 / Defect removal activity |

### 4. 为什么需要测试 / Why is Testing Necessary

#### 测试的必要性 / Necessity of Testing
- 减少开发不正确或不想要功能的风险 / reduces the risk of incorrect or unwanted features being developed
- 减少基本设计缺陷的风险，使测试能够在早期阶段识别 / reduce the risk of fundamental design defects and enable tests to be identified at an early stage
- 减少代码和测试本身中缺陷的风险 / reduce the risk of defects within the code and the tests themselves

#### 测试作为质量控制 / Testing as Quality Control
- 帮助在设定的范围、时间、质量和预算约束内实现商定的目标 / helps in achieving the agreed upon goals within the set scope, time, quality, and budget constraints
- 测试人员与开发人员密切合作可以增加各方对代码和如何测试的理解 / Having testers work closely with developers can increase each party's understanding of the code and how to test it
- 测试人员验证和验证软件可以在发布前检测可能被遗漏的故障 / Having testers verify and validate the software prior to release can detect failures that might otherwise have been missed

### 5. 质量保证与测试 / Quality Assurance vs Testing

#### 质量保证 (QA) / Quality Assurance
- 过程导向，公司导向 / Process focused, company focused
- 财务报告和利益相关者参与 / Financial reporting and stakeholder engagement
- 风险管理 / Risk management
- 项目团队技能评估和培训要求 / Project team skill assessment and training requirements
- 沟通和协作 / Communication and collaboration
- 方法论 / Methodologies
- 版本控制和分支策略 / Version control and branching strategy
- 设计标准和评审 / Design standards and reviews
- 编码标准、代码质量检查和评审 / Coding standards, code quality checks and reviews

#### 质量控制活动 / Quality Control Activities
- 走查 (Walkthroughs)
- 测试 (Testing)
- 检查 (Inspection)
- 评审 (Review)

#### 测试活动 / Testing Activities
- 测试计划 / Test planning
- 测试用例设计 / Test case design
- 测试执行 / Test execution
- 缺陷报告 / Defect reporting
- 测试报告 / Test reporting

### 6. 错误、缺陷和故障 / Errors, Defects, and Failures

#### 定义 / Definitions
- **错误 (Error)**: 产生不正确结果的人为行为。同义词：mistake / A human action that produces an incorrect result. Synonyms: mistake
- **缺陷 (Defect)**: 工作产品中的不完美或缺陷，不符合其需求或规格。同义词：bug, fault / An imperfection or deficiency in a work product where it does not meet its requirements or specifications. Synonyms: bug, fault
- **故障 (Failure)**: 组件或系统在指定限制内不执行所需功能的事件 / An event in which a component or system does not perform a required function within specified limits

#### 关系链 / Relationship Chain
```
[故障 Failures] ← [缺陷 Defects] ← [错误 Errors]
```

### 7. 七个测试原则 / Seven Testing Principles

1. **测试显示缺陷的存在，而不是它们的缺失 / Testing shows the presence of defects, not their absence**
   - 测试可以显示缺陷存在，但不能证明没有缺陷 / Testing can show that defects are present but cannot prove that there are no defects
   - 即使没有发现缺陷，测试也不是正确性的证明 / Even if no defects are found, testing is not a proof of correctness

2. **穷尽测试是不可能的 / Exhaustive testing is impossible**
   - 测试所有内容（所有输入和前置条件的组合）除了琐碎情况外都不可行 / Testing everything (all combinations of inputs and preconditions) is not feasible except for trivial cases
   - 应使用风险分析、测试技术和优先级来集中测试工作 / Risk analysis, test techniques, and priorities should be used to focus test efforts

3. **早期测试节省时间和金钱 / Early testing saves time and money**
   - 静态和动态测试活动应尽早开始 / Static and dynamic test activities should be started as early as possible
   - 早期测试有时被称为"左移"(shift left) / Early testing is sometimes referred to as "shift left"

4. **缺陷聚集在一起 / Defects cluster together**
   - 少数模块通常包含预发布测试中发现的大部分缺陷 / A small number of modules usually contains most of the defects discovered during pre-release testing
   - 预测的缺陷集群和实际观察到的缺陷集群是风险分析的重要输入 / Predicted defect clusters and actual observed defect clusters are important inputs into risk analysis

5. **警惕农药悖论 (pesticide paradox) / Beware of the pesticide paradox**
   - 如果重复相同的测试，最终这些测试不再发现任何新缺陷 / If the same tests are repeated over and over again, eventually these tests no longer find any new defects
   - 需要改变现有测试和测试数据，编写新测试 / Existing tests and test data may need changing, and new tests may need to be written

6. **测试依赖于上下文 / Testing is context dependent**
   - 在不同上下文中测试方式不同 / Testing is done differently in different contexts
   - 例如：安全关键工业控制软件与电子商务移动应用的测试方式不同 / For example, safety-critical industrial control software is tested differently from an e-commerce mobile app

7. **无错误谬论 (Absence-of-errors fallacy) / Absence-of-errors is a fallacy**
   - 期望软件验证将确保系统成功是一种谬论 / It is a fallacy to expect that software verification will ensure the success of a system
   - 彻底测试所有指定需求并修复所有发现的缺陷仍可能产生不符合用户需求和期望的系统 / Thoroughly testing all specified requirements and fixing all defects found could still produce a system that does not fulfill users' needs and expectations

## 考试题目示例 / Exam Question Examples

### 考试题1 / Exam Question 1
**问题 / Question**: 为什么需要测试？ / Why is testing necessary?
- A. 消除软件中的缺陷 / To eliminate the defects from the software
- B. 显示软件正确工作且无错误 / To show that the software works correctly without any errors
- C. 降低软件故障的风险 / To reduce the risk of software failure
- D. 证明软件完全功能且无错误 / To prove that the software is fully functional and error-free

**答案 / Answer**: C

### 考试题2 / Exam Question 2
**问题 / Question**: 以下哪项是测试的主要目标？ / Which of the following is a primary objective of testing?
- A. 为利益相关者提供信息 / To provide information for stakeholders
- B. 增加软件的复杂性 / To increase the complexity of the software
- C. 确保软件运行更快 / To ensure that the software runs faster
- D. 使软件开发更昂贵 / To make software development more expensive

**答案 / Answer**: A

### 考试题3 / Exam Question 3
**问题 / Question**: 哪个测试原则指出测试永远不能完全证明没有缺陷？ / Which testing principle states that testing can never completely prove that there are no defects?
- A. 穷尽测试是可能的 / Exhaustive testing is possible
- B. 无错误谬论 / Absence-of-errors fallacy
- C. 缺陷聚集 / Defect clustering
- D. 测试显示缺陷的存在 / Testing shows the presence of defects

**答案 / Answer**: D

### 考试题4 / Exam Question 4
**问题 / Question**: 以下哪项描述了软件缺陷的原因？ / Which of the following describes a cause of software defects?
- A. 只有有经验的开发人员才会犯错 / Only experienced developers make mistakes
- B. 缺陷只在测试阶段引入 / Defects are only introduced in the testing phase
- C. 开发过程中的复杂性和人为错误 / Complexity and human errors during development
- D. 测试可以移除软件中的所有缺陷 / Testing can remove all defects from software

**答案 / Answer**: C

## 重要概念 / Important Concepts

### 验证 vs 验证 (Verification vs Validation)

#### 验证 (Verification)
- **定义 / Definition**: 确认工作产品满足其规格的过程 / The process of confirming that a work product fulfills its specification
- **目的 / Purpose**: 确保产品按照需求和设计规格构建 / Ensures the product is built according to the requirements and design specifications
- **性质 / Nature**: 静态过程（评审、检查等）/ Static process (reviews, inspections, etc.)
- **时机 / Timing**: 在开发阶段进行 / Conducted during the development phases
- **问题 / Question**: "我们是否在正确构建产品？" / "Are we building the product right?"

#### 验证 (Validation)
- **定义 / Definition**: 通过检查确认工作产品符合利益相关者的需求 / Confirmation by examination that a work product matches a stakeholder's needs
- **目的 / Purpose**: 确保最终产品满足预期用途和用户需求 / Ensures the final product meets the intended use and user requirements
- **性质 / Nature**: 动态过程（产品的实际测试）/ Dynamic process (actual testing of the product)
- **时机 / Timing**: 在产品构建后进行 / Conducted after the product is built
- **问题 / Question**: "我们是否在构建正确的产品？" / "Are we building the right product?"

## 参考资料 / References
- ISTQB术语表 / ISTQB Glossary: https://glossary.istqb.org/en_US/search?term=&exact_matches_first=true
- V-Model: https://en.wikipedia.org/wiki/V-Model
- ASPICE: https://www.invensity.com/wp-content/uploads/2023/09/ASPICE-process-landscape.webp
- 测试目标 / Testing Objectives: https://senuri.medium.com/objectives-of-testing-4832858f6f7d
- 测试vs调试 / Testing vs Debugging: https://www.javatpoint.com/testing-vs-debugging
- 测试vs质量保证 / Testing vs Quality Assurance: 
  - https://www.triad.co.uk/news/testing-vs-qa/
  - https://blog.qatestlab.com/2011/04/07/what-is-the-difference-between-qa-and-testing/
- ISO 26262: https://model-engineers.com/en/iso-26262/ 