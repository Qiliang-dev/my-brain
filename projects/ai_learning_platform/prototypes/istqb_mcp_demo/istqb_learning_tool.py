#!/usr/bin/env python3
"""
ISTQB学习路径生成工具
为转码人士定制ISTQB认证学习方案
"""

import asyncio
import json
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from dataclasses import dataclass

@dataclass
class ISTQBChapter:
    """ISTQB章节信息"""
    id: str
    title: str
    title_en: str
    difficulty: str  # beginner, intermediate, advanced
    estimated_hours: int
    prerequisites: List[str]
    key_concepts: List[str]
    practice_projects: List[str]

@dataclass
class UserProfile:
    """用户学习档案"""
    user_id: str
    background: str  # 转码背景
    programming_experience: str  # 编程经验
    testing_experience: str  # 测试经验
    learning_style: str  # 学习风格
    available_hours_per_week: int  # 每周可用学习时间
    target_certification_date: Optional[str] = None

class ISTQBLearningPathTool:
    """ISTQB学习路径生成工具"""
    
    def __init__(self):
        # 初始化ISTQB课程大纲
        self.istqb_curriculum = self._initialize_curriculum()
    
    def _initialize_curriculum(self) -> Dict[str, ISTQBChapter]:
        """初始化ISTQB课程大纲"""
        return {
            "01": ISTQBChapter(
                id="01",
                title="测试基础",
                title_en="Testing Fundamentals",
                difficulty="beginner",
                estimated_hours=20,
                prerequisites=[],
                key_concepts=["测试定义", "测试原则", "测试过程", "测试心理学"],
                practice_projects=["创建测试计划模板", "编写测试用例"]
            ),
            "02": ISTQBChapter(
                id="02",
                title="测试活动和角色",
                title_en="Testing Activities and Roles",
                difficulty="beginner",
                estimated_hours=16,
                prerequisites=["01"],
                key_concepts=["测试活动", "测试角色", "测试团队", "测试沟通"],
                practice_projects=["角色分配练习", "测试活动流程图"]
            ),
            "03": ISTQBChapter(
                id="03",
                title="静态测试",
                title_en="Static Testing",
                difficulty="intermediate",
                estimated_hours=18,
                prerequisites=["01", "02"],
                key_concepts=["静态分析", "评审过程", "检查清单", "静态测试工具"],
                practice_projects=["代码评审练习", "文档评审练习"]
            ),
            "04": ISTQBChapter(
                id="04",
                title="软件生命周期中的测试",
                title_en="Testing Throughout Software Lifecycle",
                difficulty="intermediate",
                estimated_hours=22,
                prerequisites=["01", "02", "03"],
                key_concepts=["V模型", "敏捷测试", "测试级别", "测试类型"],
                practice_projects=["V模型设计", "敏捷测试计划"]
            ),
            "05": ISTQBChapter(
                id="05",
                title="测试分析和设计",
                title_en="Test Analysis and Design",
                difficulty="advanced",
                estimated_hours=24,
                prerequisites=["01", "02", "03", "04"],
                key_concepts=["测试技术", "测试设计", "测试覆盖率", "测试数据"],
                practice_projects=["等价类划分", "边界值分析", "决策表测试"]
            ),
            "06": ISTQBChapter(
                id="06",
                title="测试管理",
                title_en="Test Management",
                difficulty="advanced",
                estimated_hours=20,
                prerequisites=["01", "02", "04"],
                key_concepts=["测试计划", "风险评估", "测试监控", "测试报告"],
                practice_projects=["测试计划编写", "风险评估矩阵"]
            ),
            "07": ISTQBChapter(
                id="07",
                title="测试工具",
                title_en="Test Tools",
                difficulty="intermediate",
                estimated_hours=16,
                prerequisites=["01", "02", "03"],
                key_concepts=["测试工具分类", "工具选择", "工具实施", "工具维护"],
                practice_projects=["工具评估报告", "工具使用练习"]
            )
        }
    
    async def generate_istqb_learning_path(self, user_profile: UserProfile) -> Dict[str, Any]:
        """
        为转码人士生成ISTQB学习路径
        
        Args:
            user_profile: 用户学习档案
            
        Returns:
            个性化学习路径
        """
        try:
            # 1. 分析用户背景和学习需求
            background_analysis = self._analyze_user_background(user_profile)
            
            # 2. 生成学习路径
            learning_path = self._generate_learning_path(user_profile, background_analysis)
            
            # 3. 计算学习时间安排
            time_schedule = self._calculate_time_schedule(learning_path, user_profile)
            
            # 4. 生成学习建议
            learning_advice = self._generate_learning_advice(user_profile, background_analysis)
            
            # 5. 推荐实践项目
            recommended_projects = self._recommend_practice_projects(learning_path, user_profile)
            
            return {
                "user_id": user_profile.user_id,
                "learning_path": learning_path,
                "time_schedule": time_schedule,
                "learning_advice": learning_advice,
                "recommended_projects": recommended_projects,
                "estimated_total_hours": sum(chapter.estimated_hours for chapter in learning_path),
                "confidence_score": self._calculate_confidence_score(user_profile),
                "generated_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "error": f"生成学习路径时出错: {str(e)}",
                "user_id": user_profile.user_id,
                "learning_path": [],
                "time_schedule": {},
                "learning_advice": [],
                "recommended_projects": [],
                "estimated_total_hours": 0,
                "confidence_score": 0.0,
                "generated_at": datetime.now().isoformat()
            }
    
    def _analyze_user_background(self, user_profile: UserProfile) -> Dict[str, Any]:
        """分析用户背景"""
        background_score = 0
        programming_score = 0
        testing_score = 0
        
        # 分析转码背景
        if "计算机" in user_profile.background or "软件" in user_profile.background:
            background_score += 2
        elif "工程" in user_profile.background or "科学" in user_profile.background:
            background_score += 1
        
        # 分析编程经验
        if user_profile.programming_experience == "有经验":
            programming_score += 2
        elif user_profile.programming_experience == "基础":
            programming_score += 1
        
        # 分析测试经验
        if user_profile.testing_experience == "有经验":
            testing_score += 2
        elif user_profile.testing_experience == "基础":
            testing_score += 1
        
        return {
            "background_score": background_score,
            "programming_score": programming_score,
            "testing_score": testing_score,
            "overall_readiness": (background_score + programming_score + testing_score) / 6.0
        }
    
    def _generate_learning_path(self, user_profile: UserProfile, background_analysis: Dict[str, Any]) -> List[ISTQBChapter]:
        """生成学习路径"""
        # 根据用户背景调整学习顺序
        if background_analysis["overall_readiness"] >= 0.7:
            # 有经验的用户，可以并行学习一些章节
            path = [
                self.istqb_curriculum["01"],  # 测试基础
                self.istqb_curriculum["02"],  # 测试活动和角色
                self.istqb_curriculum["03"],  # 静态测试
                self.istqb_curriculum["04"],  # 软件生命周期中的测试
                self.istqb_curriculum["05"],  # 测试分析和设计
                self.istqb_curriculum["06"],  # 测试管理
                self.istqb_curriculum["07"]   # 测试工具
            ]
        elif background_analysis["overall_readiness"] >= 0.4:
            # 中等经验的用户，按顺序学习
            path = [
                self.istqb_curriculum["01"],  # 测试基础
                self.istqb_curriculum["02"],  # 测试活动和角色
                self.istqb_curriculum["03"],  # 静态测试
                self.istqb_curriculum["04"],  # 软件生命周期中的测试
                self.istqb_curriculum["07"],  # 测试工具
                self.istqb_curriculum["05"],  # 测试分析和设计
                self.istqb_curriculum["06"]   # 测试管理
            ]
        else:
            # 初学者，需要更多基础章节
            path = [
                self.istqb_curriculum["01"],  # 测试基础
                self.istqb_curriculum["02"],  # 测试活动和角色
                self.istqb_curriculum["07"],  # 测试工具
                self.istqb_curriculum["03"],  # 静态测试
                self.istqb_curriculum["04"],  # 软件生命周期中的测试
                self.istqb_curriculum["05"],  # 测试分析和设计
                self.istqb_curriculum["06"]   # 测试管理
            ]
        
        return path
    
    def _calculate_time_schedule(self, learning_path: List[ISTQBChapter], user_profile: UserProfile) -> Dict[str, Any]:
        """计算学习时间安排"""
        total_hours = sum(chapter.estimated_hours for chapter in learning_path)
        weeks_needed = total_hours / user_profile.available_hours_per_week
        
        # 计算每周学习计划
        weekly_plan = {}
        current_week = 1
        remaining_hours = user_profile.available_hours_per_week
        
        for chapter in learning_path:
            chapter_weeks = []
            chapter_hours = chapter.estimated_hours
            
            while chapter_hours > 0:
                if remaining_hours >= chapter_hours:
                    # 本周可以完成
                    chapter_weeks.append({
                        "week": current_week,
                        "hours": chapter_hours,
                        "status": "complete"
                    })
                    remaining_hours -= chapter_hours
                    chapter_hours = 0
                else:
                    # 本周只能完成部分
                    chapter_weeks.append({
                        "week": current_week,
                        "hours": remaining_hours,
                        "status": "partial"
                    })
                    chapter_hours -= remaining_hours
                    current_week += 1
                    remaining_hours = user_profile.available_hours_per_week
            
            weekly_plan[chapter.id] = {
                "title": chapter.title,
                "weeks": chapter_weeks,
                "total_hours": chapter.estimated_hours
            }
        
        return {
            "total_weeks": current_week,
            "total_hours": total_hours,
            "weekly_plan": weekly_plan,
            "estimated_completion_date": self._estimate_completion_date(current_week)
        }
    
    def _estimate_completion_date(self, weeks_needed: int) -> str:
        """估算完成日期"""
        start_date = datetime.now()
        completion_date = start_date + timedelta(weeks=weeks_needed)
        return completion_date.strftime("%Y-%m-%d")
    
    def _generate_learning_advice(self, user_profile: UserProfile, background_analysis: Dict[str, Any]) -> List[str]:
        """生成学习建议"""
        advice = []
        
        if background_analysis["overall_readiness"] < 0.4:
            advice.extend([
                "建议先补充基础的软件工程知识",
                "多关注实际项目案例，理论结合实践",
                "建议参加一些测试相关的在线课程"
            ])
        elif background_analysis["overall_readiness"] < 0.7:
            advice.extend([
                "重点关注测试实践，多做练习项目",
                "建议加入测试学习社区，与他人交流",
                "定期复习已学内容，巩固基础"
            ])
        else:
            advice.extend([
                "可以尝试并行学习相关章节",
                "重点关注高级测试技术和工具",
                "建议参与开源测试项目，积累经验"
            ])
        
        # 根据学习风格给出建议
        if user_profile.learning_style == "视觉型":
            advice.append("多使用图表和流程图来理解测试概念")
        elif user_profile.learning_style == "听觉型":
            advice.append("建议听一些测试相关的播客和讲座")
        elif user_profile.learning_style == "实践型":
            advice.append("多做实际项目，理论结合实践")
        
        return advice
    
    def _recommend_practice_projects(self, learning_path: List[ISTQBChapter], user_profile: UserProfile) -> List[Dict[str, Any]]:
        """推荐实践项目"""
        projects = []
        
        for chapter in learning_path:
            for project in chapter.practice_projects:
                projects.append({
                    "chapter_id": chapter.id,
                    "chapter_title": chapter.title,
                    "project_name": project,
                    "difficulty": chapter.difficulty,
                    "estimated_hours": max(2, chapter.estimated_hours // 4),
                    "description": f"基于{chapter.title}章节的实践项目"
                })
        
        # 根据用户背景筛选项目
        if user_profile.programming_experience == "无经验":
            # 优先推荐基础项目
            projects = [p for p in projects if p["difficulty"] == "beginner"]
        
        return projects[:10]  # 返回前10个项目
    
    def _calculate_confidence_score(self, user_profile: UserProfile) -> float:
        """计算推荐置信度"""
        # 基于用户信息的完整性计算置信度
        confidence = 0.5  # 基础置信度
        
        if user_profile.background:
            confidence += 0.1
        if user_profile.programming_experience:
            confidence += 0.1
        if user_profile.testing_experience:
            confidence += 0.1
        if user_profile.learning_style:
            confidence += 0.1
        if user_profile.available_hours_per_week > 0:
            confidence += 0.1
        
        return min(confidence, 1.0)

# 测试函数
async def test_tool():
    """测试工具功能"""
    tool = ISTQBLearningPathTool()
    
    # 创建测试用户档案
    user_profile = UserProfile(
        user_id="test_user_001",
        background="计算机科学专业",
        programming_experience="有经验",
        testing_experience="基础",
        learning_style="实践型",
        available_hours_per_week=15,
        target_certification_date="2024-06-30"
    )
    
    # 生成学习路径
    result = await tool.generate_istqb_learning_path(user_profile)
    
    # 打印结果
    print("=== ISTQB学习路径生成结果 ===")
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    asyncio.run(test_tool())
