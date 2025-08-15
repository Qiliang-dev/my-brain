#!/usr/bin/env python3
"""
ISTQB学习平台用户问卷调查系统
通过标准化问卷收集用户信息，为AI提供结构化数据
"""

import json
import asyncio
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from istqb_learning_tool import ISTQBLearningPathTool, UserProfile

@dataclass
class SurveyQuestion:
    """问卷问题结构"""
    id: str
    question: str
    question_en: str
    type: str  # single_choice, multiple_choice, text, number, scale
    options: Optional[List[str]] = None
    required: bool = True
    weight: float = 1.0  # 问题权重，用于计算准备度

@dataclass
class SurveyResponse:
    """用户问卷回答"""
    user_id: str
    question_id: str
    answer: Any
    answered_at: str

@dataclass
class UserSurveyProfile:
    """用户问卷档案"""
    user_id: str
    survey_responses: List[SurveyResponse]
    completed_at: str
    analysis_result: Optional[Dict[str, Any]] = None

class ISTQBSurveySystem:
    """ISTQB学习问卷调查系统"""
    
    def __init__(self):
        """初始化问卷系统"""
        self.questions = self._initialize_survey_questions()
        self.istqb_tool = ISTQBLearningPathTool()
        
    def _initialize_survey_questions(self) -> List[SurveyQuestion]:
        """初始化问卷问题"""
        return [
            # 基础信息
            SurveyQuestion(
                id="background",
                question="你的专业背景是什么？",
                question_en="What is your educational background?",
                type="single_choice",
                options=[
                    "计算机科学/软件工程",
                    "其他工程专业（机械、电子、土木等）",
                    "数学/物理等理科专业",
                    "商科/文科专业",
                    "其他专业"
                ],
                weight=2.0
            ),
            
            SurveyQuestion(
                id="programming_experience",
                question="你的编程经验如何？",
                question_en="What is your programming experience?",
                type="single_choice",
                options=[
                    "有丰富经验（2年以上）",
                    "有经验（6个月-2年）",
                    "基础水平（3-6个月）",
                    "初学者（1-3个月）",
                    "完全零基础"
                ],
                weight=2.0
            ),
            
            SurveyQuestion(
                id="testing_experience",
                question="你有软件测试经验吗？",
                question_en="Do you have software testing experience?",
                type="single_choice",
                options=[
                    "有专业测试经验（1年以上）",
                    "有测试经验（6个月-1年）",
                    "有基础测试经验（1-6个月）",
                    "了解测试概念但无实践",
                    "完全不了解测试"
                ],
                weight=1.5
            ),
            
            SurveyQuestion(
                id="learning_style",
                question="你更喜欢哪种学习方式？",
                question_en="What is your preferred learning style?",
                type="single_choice",
                options=[
                    "视觉型（图表、视频、流程图）",
                    "听觉型（音频、讲座、讨论）",
                    "实践型（动手操作、项目练习）",
                    "阅读型（文档、书籍、文章）",
                    "混合型（多种方式结合）"
                ],
                weight=1.0
            ),
            
            SurveyQuestion(
                id="available_hours_per_week",
                question="你每周可以投入多少时间学习？",
                question_en="How many hours per week can you dedicate to learning?",
                type="single_choice",
                options=[
                    "25小时以上",
                    "20-25小时",
                    "15-20小时",
                    "10-15小时",
                    "5-10小时",
                    "5小时以下"
                ],
                weight=1.0
            ),
            
            SurveyQuestion(
                id="target_certification_date",
                question="你希望在什么时候获得ISTQB认证？",
                question_en="When do you want to obtain ISTQB certification?",
                type="single_choice",
                options=[
                    "3个月内",
                    "6个月内",
                    "1年内",
                    "1-2年内",
                    "不着急，慢慢来"
                ],
                weight=0.5
            ),
            
            SurveyQuestion(
                id="learning_goals",
                question="你学习ISTQB的主要目标是什么？（可多选）",
                question_en="What are your main goals for learning ISTQB? (Multiple choice)",
                type="multiple_choice",
                options=[
                    "转行做软件测试",
                    "提升现有测试技能",
                    "获得行业认证",
                    "了解测试理论",
                    "为工作晋升做准备",
                    "个人兴趣学习"
                ],
                weight=1.0
            ),
            
            SurveyQuestion(
                id="current_skills",
                question="你目前掌握哪些技能？（可多选）",
                question_en="What skills do you currently have? (Multiple choice)",
                type="multiple_choice",
                options=[
                    "Python编程",
                    "Java编程",
                    "JavaScript编程",
                    "SQL数据库",
                    "Linux系统",
                    "Git版本控制",
                    "敏捷开发",
                    "项目管理",
                    "英语读写",
                    "其他技能"
                ],
                weight=1.0
            ),
            
            SurveyQuestion(
                id="challenges",
                question="你认为学习ISTQB可能遇到的最大挑战是什么？",
                question_en="What do you think will be the biggest challenge in learning ISTQB?",
                type="single_choice",
                options=[
                    "缺乏编程基础",
                    "测试概念理解困难",
                    "时间安排问题",
                    "英语语言障碍",
                    "理论与实践结合",
                    "其他挑战"
                ],
                weight=0.8
            ),
            
            SurveyQuestion(
                id="additional_info",
                question="还有什么其他信息想要告诉我们吗？",
                question_en="Is there anything else you'd like to tell us?",
                type="text",
                required=False,
                weight=0.3
            )
        ]
    
    def display_survey(self) -> None:
        """显示问卷内容"""
        print("📋 ISTQB学习问卷调查")
        print("=" * 60)
        print("请认真回答以下问题，这将帮助我们为你制定个性化的学习计划。\n")
        
        for i, question in enumerate(self.questions, 1):
            print(f"{i}. {question.question}")
            if question.question_en:
                print(f"   ({question.question_en})")
            
            if question.type == "single_choice" and question.options:
                for j, option in enumerate(question.options, 1):
                    print(f"   {j}. {option}")
            elif question.type == "multiple_choice" and question.options:
                print("   （可多选，输入选项编号，用逗号分隔，如：1,3,5）")
                for j, option in enumerate(question.options, 1):
                    print(f"   {j}. {option}")
            elif question.type == "text":
                print("   （请直接输入文字）")
            elif question.type == "number":
                print("   （请输入数字）")
            elif question.type == "scale":
                print("   （1-5分，1分最低，5分最高）")
            
            if question.required:
                print("   * 必答题")
            print()
    
    def collect_survey_responses(self) -> List[SurveyResponse]:
        """收集用户问卷回答"""
        responses = []
        user_id = f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        print("🎯 开始填写问卷...\n")
        
        for question in self.questions:
            while True:
                try:
                    if question.type == "single_choice":
                        answer = self._collect_single_choice(question)
                    elif question.type == "multiple_choice":
                        answer = self._collect_multiple_choice(question)
                    elif question.type == "text":
                        answer = self._collect_text(question)
                    elif question.type == "number":
                        answer = self._collect_number(question)
                    elif question.type == "scale":
                        answer = self._collect_scale(question)
                    else:
                        answer = "未知类型"
                    
                    if answer is not None:
                        response = SurveyResponse(
                            user_id=user_id,
                            question_id=question.id,
                            answer=answer,
                            answered_at=datetime.now().isoformat()
                        )
                        responses.append(response)
                        break
                    else:
                        print("❌ 请提供有效答案")
                        
                except Exception as e:
                    print(f"❌ 输入有误，请重新输入: {str(e)}")
        
        return responses
    
    def _collect_single_choice(self, question: SurveyQuestion) -> Optional[str]:
        """收集单选题答案"""
        if not question.options:
            return None
        
        while True:
            try:
                choice = input(f"请选择 (1-{len(question.options)}): ").strip()
                if choice.lower() == 'q':
                    return None
                
                choice_num = int(choice)
                if 1 <= choice_num <= len(question.options):
                    return question.options[choice_num - 1]
                else:
                    print(f"请输入1-{len(question.options)}之间的数字")
            except ValueError:
                print("请输入有效的数字")
    
    def _collect_multiple_choice(self, question: SurveyQuestion) -> Optional[List[str]]:
        """收集多选题答案"""
        if not question.options:
            return None
        
        while True:
            try:
                choice = input(f"请选择 (如: 1,3,5): ").strip()
                if choice.lower() == 'q':
                    return None
                
                choice_nums = [int(x.strip()) for x in choice.split(',')]
                if all(1 <= num <= len(question.options) for num in choice_nums):
                    return [question.options[num - 1] for num in choice_nums]
                else:
                    print(f"请输入1-{len(question.options)}之间的数字")
            except ValueError:
                print("请输入有效的数字，用逗号分隔")
    
    def _collect_text(self, question: SurveyQuestion) -> Optional[str]:
        """收集文本答案"""
        answer = input("请输入: ").strip()
        if not answer and question.required:
            return None
        return answer if answer else "无"
    
    def _collect_number(self, question: SurveyQuestion) -> Optional[int]:
        """收集数字答案"""
        while True:
            try:
                answer = input("请输入数字: ").strip()
                if answer.lower() == 'q':
                    return None
                return int(answer)
            except ValueError:
                print("请输入有效的数字")
    
    def _collect_scale(self, question: SurveyQuestion) -> Optional[int]:
        """收集评分答案"""
        while True:
            try:
                answer = input("请评分 (1-5): ").strip()
                if answer.lower() == 'q':
                    return None
                
                score = int(answer)
                if 1 <= score <= 5:
                    return score
                else:
                    print("请输入1-5之间的数字")
            except ValueError:
                print("请输入有效的数字")
    
    def analyze_survey_responses(self, responses: List[SurveyResponse]) -> Dict[str, Any]:
        """分析问卷回答，生成用户档案"""
        # 创建回答字典
        answers = {r.question_id: r.answer for r in responses}
        
        # 分析背景
        background_score = self._analyze_background(answers.get('background', ''))
        programming_score = self._analyze_programming(answers.get('programming_experience', ''))
        testing_score = self._analyze_testing(answers.get('testing_experience', ''))
        
        # 计算总体准备度
        total_weight = sum(q.weight for q in self.questions if q.id in ['background', 'programming_experience', 'testing_experience'])
        overall_readiness = (background_score + programming_score + testing_score) / total_weight
        
        # 生成学习建议
        learning_advice = self._generate_learning_advice(answers, overall_readiness)
        
        # 分析学习目标
        learning_goals = answers.get('learning_goals', [])
        if isinstance(learning_goals, str):
            learning_goals = [learning_goals]
        
        # 分析当前技能
        current_skills = answers.get('current_skills', [])
        if isinstance(current_skills, str):
            current_skills = [current_skills]
        
        return {
            "background_analysis": {
                "background_score": background_score,
                "programming_score": programming_score,
                "testing_score": testing_score,
                "overall_readiness": overall_readiness
            },
            "learning_goals": learning_goals,
            "current_skills": current_skills,
            "learning_style": answers.get('learning_style', '未知'),
            "available_hours": self._parse_available_hours(answers.get('available_hours_per_week', '')),
            "target_date": answers.get('target_certification_date', '不着急'),
            "challenges": answers.get('challenges', '未知'),
            "learning_advice": learning_advice,
            "additional_info": answers.get('additional_info', '无')
        }
    
    def _analyze_background(self, background: str) -> float:
        """分析专业背景"""
        if "计算机" in background or "软件" in background:
            return 2.0
        elif "工程" in background:
            return 1.0
        elif "数学" in background or "物理" in background:
            return 1.5
        elif "商科" in background or "文科" in background:
            return 0.5
        else:
            return 0.5
    
    def _analyze_programming(self, experience: str) -> float:
        """分析编程经验"""
        if "丰富经验" in experience:
            return 2.0
        elif "有经验" in experience:
            return 1.5
        elif "基础水平" in experience:
            return 1.0
        elif "初学者" in experience:
            return 0.5
        else:
            return 0.0
    
    def _analyze_testing(self, experience: str) -> float:
        """分析测试经验"""
        if "专业测试经验" in experience:
            return 2.0
        elif "有测试经验" in experience:
            return 1.5
        elif "基础测试经验" in experience:
            return 1.0
        elif "了解测试概念" in experience:
            return 0.5
        else:
            return 0.0
    
    def _parse_available_hours(self, hours_str: str) -> int:
        """解析可用时间"""
        if "25小时以上" in hours_str:
            return 30
        elif "20-25小时" in hours_str:
            return 22
        elif "15-20小时" in hours_str:
            return 17
        elif "10-15小时" in hours_str:
            return 12
        elif "5-10小时" in hours_str:
            return 7
        else:
            return 5
    
    def _generate_learning_advice(self, answers: Dict[str, Any], readiness: float) -> List[str]:
        """生成学习建议"""
        advice = []
        
        if readiness < 0.4:
            advice.extend([
                "建议先补充基础的软件工程和编程知识",
                "可以参加一些入门级的测试课程",
                "建议每周投入更多时间学习"
            ])
        elif readiness < 0.7:
            advice.extend([
                "基础较好，可以开始ISTQB学习",
                "重点关注测试实践和项目练习",
                "建议加入测试学习社区"
            ])
        else:
            advice.extend([
                "准备度很好，可以直接开始ISTQB学习",
                "可以尝试并行学习相关章节",
                "建议参与实际测试项目"
            ])
        
        # 根据学习风格给出建议
        learning_style = answers.get('learning_style', '')
        if "视觉型" in learning_style:
            advice.append("多使用图表和流程图来理解测试概念")
        elif "听觉型" in learning_style:
            advice.append("建议听一些测试相关的播客和讲座")
        elif "实践型" in learning_style:
            advice.append("多做实际项目，理论结合实践")
        
        return advice
    
    async def generate_learning_plan(self, analysis_result: Dict[str, Any]) -> Dict[str, Any]:
        """基于问卷分析生成学习计划"""
        # 创建用户档案
        user_profile = UserProfile(
            user_id=analysis_result.get('user_id', 'survey_user'),
            background=analysis_result.get('background', '未知'),
            programming_experience=self._map_programming_experience(analysis_result.get('programming_score', 0)),
            testing_experience=self._map_testing_experience(analysis_result.get('testing_score', 0)),
            learning_style=analysis_result.get('learning_style', '未知'),
            available_hours_per_week=analysis_result.get('available_hours', 15)
        )
        
        # 生成学习路径
        learning_plan = await self.istqb_tool.generate_istqb_learning_path(user_profile)
        
        # 整合问卷分析结果
        learning_plan['survey_analysis'] = analysis_result
        
        return learning_plan
    
    def _map_programming_experience(self, score: float) -> str:
        """映射编程经验分数到描述"""
        if score >= 1.5:
            return "有经验"
        elif score >= 1.0:
            return "基础"
        else:
            return "无经验"
    
    def _map_testing_experience(self, score: float) -> str:
        """映射测试经验分数到描述"""
        if score >= 1.5:
            return "有经验"
        elif score >= 1.0:
            return "基础"
        else:
            return "无经验"
    
    def save_survey_data(self, responses: List[SurveyResponse], analysis_result: Dict[str, Any], filename: str = None) -> str:
        """保存问卷数据"""
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"survey_data_{timestamp}.json"
        
        data = {
            "survey_responses": [asdict(r) for r in responses],
            "analysis_result": analysis_result,
            "generated_at": datetime.now().isoformat()
        }
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        return filename
    
    async def run_survey(self) -> Dict[str, Any]:
        """运行完整的问卷调查流程"""
        print("🎯 ISTQB学习问卷调查系统")
        print("=" * 60)
        
        # 1. 显示问卷
        self.display_survey()
        
        # 2. 收集回答
        responses = self.collect_survey_responses()
        
        # 3. 分析回答
        print("\n🔍 正在分析你的回答...")
        analysis_result = self.analyze_survey_responses(responses)
        
        # 4. 生成学习计划
        print("📚 正在生成个性化学习计划...")
        learning_plan = await self.generate_learning_plan(analysis_result)
        
        # 5. 保存数据
        filename = self.save_survey_data(responses, analysis_result)
        print(f"💾 问卷数据已保存到: {filename}")
        
        return learning_plan

async def main():
    """主函数"""
    survey_system = ISTQBSurveySystem()
    
    try:
        # 运行问卷调查
        result = await survey_system.run_survey()
        
        # 显示结果
        print("\n" + "=" * 60)
        print("🎉 问卷调查完成！")
        print("=" * 60)
        
        print(f"📊 学习准备度: {result['survey_analysis']['background_analysis']['overall_readiness']:.2f}")
        print(f"⏱️ 总学习时长: {result['estimated_total_hours']}小时")
        print(f"📅 预计完成时间: {result['time_schedule']['estimated_completion_date']}")
        
        print("\n💡 个性化建议:")
        for i, advice in enumerate(result['survey_analysis']['learning_advice'][:3], 1):
            print(f"   {i}. {advice}")
        
        print("\n🚀 下一步:")
        print("1. 查看完整的学习计划")
        print("2. 开始按照计划学习")
        print("3. 定期更新学习进度")
        
    except Exception as e:
        print(f"❌ 问卷调查过程中出错: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())
