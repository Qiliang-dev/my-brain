#!/usr/bin/env python3
"""
ISTQB学习平台MCP服务器
为AI模型提供ISTQB学习相关的工具调用能力
"""

import asyncio
import json
import logging
from typing import Dict, Any, Optional
from mcp import ServerSession, StdioServerTransport
from istqb_learning_tool import ISTQBLearningPathTool, UserProfile
from survey_mcp_tool import SurveyMCPTool

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ISTQBLearningMCPServer:
    """ISTQB学习平台MCP服务器"""
    
    def __init__(self):
        """初始化服务器"""
        self.istqb_tool = ISTQBLearningPathTool()
        self.survey_tool = SurveyMCPTool()
        logger.info("ISTQB学习平台MCP服务器初始化完成")
    
    async def handle_generate_istqb_path(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        处理生成ISTQB学习路径的请求
        
        Args:
            arguments: 包含用户信息的参数字典
            
        Returns:
            个性化学习路径结果
        """
        try:
            logger.info(f"收到生成ISTQB学习路径请求: {arguments}")
            
            # 验证必需参数
            required_fields = ['user_id', 'background', 'programming_experience', 
                             'testing_experience', 'learning_style', 'available_hours_per_week']
            
            for field in required_fields:
                if field not in arguments:
                    return {
                        "error": f"缺少必需参数: {field}",
                        "required_fields": required_fields
                    }
            
            # 创建用户档案
            user_profile = UserProfile(
                user_id=arguments['user_id'],
                background=arguments['background'],
                programming_experience=arguments['programming_experience'],
                testing_experience=arguments['testing_experience'],
                learning_style=arguments['learning_style'],
                available_hours_per_week=arguments['available_hours_per_week'],
                target_certification_date=arguments.get('target_certification_date')
            )
            
            # 生成学习路径
            result = await self.istqb_tool.generate_istqb_learning_path(user_profile)
            
            logger.info(f"成功生成学习路径: {result['user_id']}")
            return result
            
        except Exception as e:
            logger.error(f"生成学习路径时出错: {str(e)}")
            return {
                "error": f"生成学习路径时出错: {str(e)}",
                "user_id": arguments.get('user_id', 'unknown')
            }
    
    async def handle_get_istqb_curriculum(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        获取ISTQB课程大纲信息
        
        Args:
            arguments: 参数字典（可选）
            
        Returns:
            ISTQB课程大纲
        """
        try:
            logger.info("收到获取ISTQB课程大纲请求")
            
            curriculum_info = {}
            for chapter_id, chapter in self.istqb_tool.istqb_curriculum.items():
                curriculum_info[chapter_id] = {
                    "title": chapter.title,
                    "title_en": chapter.title_en,
                    "difficulty": chapter.difficulty,
                    "estimated_hours": chapter.estimated_hours,
                    "prerequisites": chapter.prerequisites,
                    "key_concepts": chapter.key_concepts,
                    "practice_projects": chapter.practice_projects
                }
            
            return {
                "curriculum": curriculum_info,
                "total_chapters": len(curriculum_info),
                "total_hours": sum(ch["estimated_hours"] for ch in curriculum_info.values())
            }
            
        except Exception as e:
            logger.error(f"获取课程大纲时出错: {str(e)}")
            return {"error": f"获取课程大纲时出错: {str(e)}"}
    
    async def handle_assess_user_readiness(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        评估用户学习准备度
        
        Args:
            arguments: 包含用户背景信息的参数字典
            
        Returns:
            用户准备度评估结果
        """
        try:
            logger.info(f"收到用户准备度评估请求: {arguments}")
            
            if 'background' not in arguments or 'programming_experience' not in arguments:
                return {"error": "缺少用户背景信息"}
            
            # 创建临时用户档案进行评估
            temp_profile = UserProfile(
                user_id=arguments.get('user_id', 'temp_user'),
                background=arguments['background'],
                programming_experience=arguments.get('programming_experience', '无经验'),
                testing_experience=arguments.get('testing_experience', '无经验'),
                learning_style=arguments.get('learning_style', '未知'),
                available_hours_per_week=arguments.get('available_hours_per_week', 0)
            )
            
            # 分析用户背景
            background_analysis = self.istqb_tool._analyze_user_background(temp_profile)
            
            # 生成建议
            recommendations = []
            if background_analysis['overall_readiness'] < 0.4:
                recommendations.append("建议先补充基础的软件工程和编程知识")
                recommendations.append("可以参加一些入门级的测试课程")
                recommendations.append("建议每周投入更多时间学习")
            elif background_analysis['overall_readiness'] < 0.7:
                recommendations.append("基础较好，可以开始ISTQB学习")
                recommendations.append("重点关注测试实践和项目练习")
                recommendations.append("建议加入测试学习社区")
            else:
                recommendations.append("准备度很好，可以直接开始ISTQB学习")
                recommendations.append("可以尝试并行学习相关章节")
                recommendations.append("建议参与实际测试项目")
            
            return {
                "user_id": arguments.get('user_id', 'temp_user'),
                "background_analysis": background_analysis,
                "recommendations": recommendations,
                "estimated_preparation_time": self._estimate_preparation_time(background_analysis['overall_readiness'])
            }
            
        except Exception as e:
            logger.error(f"评估用户准备度时出错: {str(e)}")
            return {"error": f"评估用户准备度时出错: {str(e)}"}
    
    def _estimate_preparation_time(self, readiness_score: float) -> str:
        """估算准备时间"""
        if readiness_score >= 0.7:
            return "无需额外准备，可直接开始"
        elif readiness_score >= 0.4:
            return "需要1-2周准备时间"
        else:
            return "需要1-2个月准备时间"
    
    async def handle_get_survey_questions(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """处理获取问卷问题的请求"""
        try:
            logger.info("收到获取问卷问题请求")
            return await self.survey_tool.get_survey_questions(arguments)
        except Exception as e:
            logger.error(f"获取问卷问题时出错: {str(e)}")
            return {"error": f"获取问卷问题时出错: {str(e)}"}
    
    async def handle_analyze_user_profile(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """处理分析用户档案的请求"""
        try:
            logger.info(f"收到分析用户档案请求: {arguments}")
            return await self.survey_tool.analyze_user_profile(arguments)
        except Exception as e:
            logger.error(f"分析用户档案时出错: {str(e)}")
            return {"error": f"分析用户档案时出错: {str(e)}"}
    
    async def handle_generate_learning_path_from_survey(self, arguments: Dict[str, Any]) -> Dict[str, Any]):
        """处理基于问卷生成学习路径的请求"""
        try:
            logger.info(f"收到基于问卷生成学习路径请求: {arguments}")
            return await self.survey_tool.generate_learning_path_from_survey(arguments)
        except Exception as e:
            logger.error(f"基于问卷生成学习路径时出错: {str(e)}")
            return {"error": f"基于问卷生成学习路径时出错: {str(e)}"}
    
    async def handle_get_survey_statistics(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """处理获取问卷统计信息的请求"""
        try:
            logger.info("收到获取问卷统计信息请求")
            return await self.survey_tool.get_survey_statistics(arguments)
        except Exception as e:
            logger.error(f"获取问卷统计信息时出错: {str(e)}")
            return {"error": f"获取问卷统计信息时出错: {str(e)}"}
    
    async def start(self):
        """启动MCP服务器"""
        transport = StdioServerTransport()
        
        async with ServerSession(transport) as session:
            logger.info("MCP服务器启动，开始注册工具...")
            
            # 注册工具
            await session.register_tool(
                "generate_istqb_learning_path",
                self.handle_generate_istqb_path,
                description="为转码人士生成个性化的ISTQB学习路径"
            )
            
            await session.register_tool(
                "get_istqb_curriculum",
                self.handle_get_istqb_curriculum,
                description="获取ISTQB课程大纲信息"
            )
            
            await session.register_tool(
                "assess_user_readiness",
                self.handle_assess_user_readiness,
                description="评估用户学习ISTQB的准备度"
            )
            
            # 注册问卷调查工具
            await session.register_tool(
                "get_survey_questions",
                self.handle_get_survey_questions,
                description="获取ISTQB学习问卷调查问题列表"
            )
            
            await session.register_tool(
                "analyze_user_profile",
                self.handle_analyze_user_profile,
                description="基于用户信息分析学习准备度并生成学习计划"
            )
            
            await session.register_tool(
                "generate_learning_path_from_survey",
                self.handle_generate_learning_path_from_survey,
                description="基于问卷调查生成个性化学习路径"
            )
            
            await session.register_tool(
                "get_survey_statistics",
                self.handle_get_survey_statistics,
                description="获取问卷调查统计信息"
            )
            
            logger.info("所有工具注册完成，等待AI模型调用...")
            
            # 运行服务器
            await session.run()

async def main():
    """主函数"""
    server = ISTQBLearningMCPServer()
    await server.start()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("服务器被用户中断")
    except Exception as e:
        logger.error(f"服务器运行出错: {str(e)}")
