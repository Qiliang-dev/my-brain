#!/usr/bin/env python3
"""
问卷调查MCP工具
为AI模型提供问卷调查和用户分析能力
"""

import asyncio
import json
from datetime import datetime
from typing import Dict, List, Any, Optional
from user_survey_system import ISTQBSurveySystem, SurveyQuestion, SurveyResponse

class SurveyMCPTool:
    """问卷调查MCP工具"""
    
    def __init__(self):
        """初始化工具"""
        self.survey_system = ISTQBSurveySystem()
    
    async def get_survey_questions(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        获取问卷问题列表
        
        Args:
            arguments: 参数字典（可选）
            
        Returns:
            问卷问题列表
        """
        try:
            questions = []
            for q in self.survey_system.questions:
                questions.append({
                    "id": q.id,
                    "question": q.question,
                    "question_en": q.question_en,
                    "type": q.type,
                    "options": q.options,
                    "required": q.required,
                    "weight": q.weight
                })
            
            return {
                "questions": questions,
                "total_questions": len(questions),
                "question_types": list(set(q.type for q in self.survey_system.questions))
            }
            
        except Exception as e:
            return {"error": f"获取问卷问题时出错: {str(e)}"}
    
    async def analyze_user_profile(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        分析用户档案（基于用户提供的信息）
        
        Args:
            arguments: 包含用户信息的参数字典
            
        Returns:
            用户分析结果
        """
        try:
            # 验证必需参数
            required_fields = ['background', 'programming_experience']
            for field in required_fields:
                if field not in arguments:
                    return {"error": f"缺少必需参数: {field}"}
            
            # 创建模拟问卷回答
            responses = []
            user_id = arguments.get('user_id', f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            
            # 映射用户信息到问卷回答
            field_mapping = {
                'background': 'background',
                'programming_experience': 'programming_experience',
                'testing_experience': 'testing_experience',
                'learning_style': 'learning_style',
                'available_hours_per_week': 'available_hours_per_week',
                'learning_goals': 'learning_goals',
                'current_skills': 'current_skills',
                'challenges': 'challenges'
            }
            
            for field, question_id in field_mapping.items():
                if field in arguments:
                    response = SurveyResponse(
                        user_id=user_id,
                        question_id=question_id,
                        answer=arguments[field],
                        answered_at=datetime.now().isoformat()
                    )
                    responses.append(response)
            
            # 分析回答
            analysis_result = self.survey_system.analyze_survey_responses(responses)
            
            # 生成学习计划
            learning_plan = await self.survey_system.generate_learning_plan(analysis_result)
            
            return {
                "user_id": user_id,
                "analysis_result": analysis_result,
                "learning_plan": learning_plan,
                "generated_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"分析用户档案时出错: {str(e)}"}
    
    async def generate_learning_path_from_survey(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        基于问卷调查生成学习路径
        
        Args:
            arguments: 包含问卷回答的参数字典
            
        Returns:
            个性化学习路径
        """
        try:
            # 验证必需参数
            required_fields = ['survey_responses']
            for field in required_fields:
                if field not in arguments:
                    return {"error": f"缺少必需参数: {field}"}
            
            # 创建问卷回答对象
            responses = []
            user_id = arguments.get('user_id', f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}")
            
            for response_data in arguments['survey_responses']:
                response = SurveyResponse(
                    user_id=user_id,
                    question_id=response_data['question_id'],
                    answer=response_data['answer'],
                    answered_at=response_data.get('answered_at', datetime.now().isoformat())
                )
                responses.append(response)
            
            # 分析回答
            analysis_result = self.survey_system.analyze_survey_responses(responses)
            
            # 生成学习计划
            learning_plan = await self.survey_system.generate_learning_plan(analysis_result)
            
            # 保存数据
            filename = self.survey_system.save_survey_data(responses, analysis_result)
            
            return {
                "user_id": user_id,
                "survey_analysis": analysis_result,
                "learning_path": learning_plan,
                "data_saved_to": filename,
                "generated_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"生成学习路径时出错: {str(e)}"}
    
    async def get_survey_statistics(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        获取问卷调查统计信息
        
        Args:
            arguments: 参数字典（可选）
            
        Returns:
            统计信息
        """
        try:
            # 这里可以添加真实的统计数据
            # 目前返回示例数据
            stats = {
                "total_surveys": 150,
                "completion_rate": 0.85,
                "average_readiness": 0.62,
                "top_backgrounds": [
                    "计算机科学/软件工程",
                    "其他工程专业",
                    "数学/物理等理科专业"
                ],
                "top_learning_goals": [
                    "转行做软件测试",
                    "提升现有测试技能",
                    "获得行业认证"
                ],
                "common_challenges": [
                    "缺乏编程基础",
                    "测试概念理解困难",
                    "时间安排问题"
                ]
            }
            
            return {
                "statistics": stats,
                "generated_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"获取统计信息时出错: {str(e)}"}
    
    async def recommend_survey_questions(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        根据用户背景推荐问卷问题
        
        Args:
            arguments: 包含用户背景信息的参数字典
            
        Returns:
            推荐的问题列表
        """
        try:
            background = arguments.get('background', '')
            programming_exp = arguments.get('programming_experience', '')
            
            # 根据背景推荐问题
            recommended_questions = []
            
            if "计算机" in background or "软件" in background:
                recommended_questions.extend([
                    "你的测试经验如何？",
                    "你熟悉哪些测试工具？",
                    "你的学习目标是什么？"
                ])
            elif "工程" in background:
                recommended_questions.extend([
                    "你的编程基础如何？",
                    "你了解软件开发生命周期吗？",
                    "你的学习时间安排如何？"
                ])
            else:
                recommended_questions.extend([
                    "你的技术背景如何？",
                    "你愿意投入多少时间学习？",
                    "你的学习动机是什么？"
                ])
            
            if "无经验" in programming_exp or "零基础" in programming_exp:
                recommended_questions.extend([
                    "你是否有学习编程的计划？",
                    "你希望从哪个编程语言开始？"
                ])
            
            return {
                "background": background,
                "programming_experience": programming_exp,
                "recommended_questions": recommended_questions,
                "reasoning": "基于用户背景和编程经验推荐相关问题",
                "generated_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {"error": f"推荐问题时出错: {str(e)}"}

# 测试函数
async def test_tool():
    """测试工具功能"""
    tool = SurveyMCPTool()
    
    # 测试获取问卷问题
    print("=== 测试获取问卷问题 ===")
    result1 = await tool.get_survey_questions({})
    print(f"问题数量: {result1.get('total_questions', 0)}")
    
    # 测试分析用户档案
    print("\n=== 测试分析用户档案 ===")
    user_info = {
        "background": "计算机科学专业",
        "programming_experience": "有经验",
        "testing_experience": "基础",
        "learning_style": "实践型",
        "available_hours_per_week": 20
    }
    result2 = await tool.analyze_user_profile(user_info)
    if "error" not in result2:
        readiness = result2['analysis_result']['background_analysis']['overall_readiness']
        print(f"用户准备度: {readiness:.2f}")
    
    # 测试推荐问题
    print("\n=== 测试推荐问题 ===")
    result3 = await tool.recommend_survey_questions({
        "background": "机械工程专业",
        "programming_experience": "无经验"
    })
    print(f"推荐问题: {result3.get('recommended_questions', [])}")

if __name__ == "__main__":
    asyncio.run(test_tool())

