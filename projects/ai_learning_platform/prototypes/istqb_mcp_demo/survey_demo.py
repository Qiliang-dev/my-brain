#!/usr/bin/env python3
"""
问卷调查系统演示脚本
展示问卷调查 + AI分析的完整流程
"""

import asyncio
import json
from user_survey_system import ISTQBSurveySystem

class SurveyDemo:
    """问卷调查演示"""
    
    def __init__(self):
        """初始化演示"""
        self.survey_system = ISTQBSurveySystem()
    
    async def run_demo(self):
        """运行演示"""
        print("🎯 ISTQB学习平台问卷调查系统演示")
        print("=" * 60)
        print("本演示将展示：")
        print("1. 📋 标准化问卷调查")
        print("2. 🔍 AI智能分析用户背景")
        print("3. 📚 个性化学习路径生成")
        print("4. 💾 数据存储和管理")
        print("=" * 60)
        
        # 演示1：运行完整问卷调查
        print("\n🚀 演示1: 完整问卷调查流程")
        print("-" * 40)
        
        try:
            # 运行问卷调查
            result = await self.survey_system.run_survey()
            
            if "error" not in result:
                print("✅ 问卷调查完成！")
                self._display_results(result)
            else:
                print(f"❌ 问卷调查失败: {result['error']}")
                
        except Exception as e:
            print(f"❌ 演示过程中出错: {str(e)}")
        
        # 演示2：基于已有数据生成学习计划
        print("\n🚀 演示2: 基于用户信息生成学习计划")
        print("-" * 40)
        
        try:
            # 模拟用户信息
            user_info = {
                "background": "机械工程专业",
                "programming_experience": "无经验",
                "testing_experience": "无经验",
                "learning_style": "视觉型",
                "available_hours_per_week": 15,
                "learning_goals": ["转行做软件测试", "获得行业认证"],
                "current_skills": ["AutoCAD", "SolidWorks", "项目管理"],
                "challenges": "缺乏编程基础"
            }
            
            # 分析用户档案
            analysis_result = self.survey_system.analyze_survey_responses([])
            
            # 生成学习计划
            learning_plan = await self.survey_system.generate_learning_plan(analysis_result)
            
            print("✅ 基于用户信息生成学习计划成功！")
            self._display_results(learning_plan)
            
        except Exception as e:
            print(f"❌ 演示过程中出错: {str(e)}")
        
        # 演示3：展示问卷系统功能
        print("\n🚀 演示3: 问卷系统功能展示")
        print("-" * 40)
        
        try:
            # 显示问卷问题
            print("📋 问卷问题示例:")
            for i, question in enumerate(self.survey_system.questions[:3], 1):
                print(f"  {i}. {question.question}")
                if question.options:
                    for j, option in enumerate(question.options[:2], 1):
                        print(f"     {j}. {option}")
                    if len(question.options) > 2:
                        print(f"     ... 还有{len(question.options)-2}个选项")
                print()
            
            # 显示问题类型
            question_types = set(q.type for q in self.survey_system.questions)
            print(f"🔧 支持的问题类型: {', '.join(question_types)}")
            
            # 显示权重系统
            print(f"⚖️ 问题权重系统: 背景({self.survey_system.questions[0].weight}) + 编程({self.survey_system.questions[1].weight}) + 测试({self.survey_system.questions[2].weight})")
            
        except Exception as e:
            print(f"❌ 演示过程中出错: {str(e)}")
        
        print("\n" + "=" * 60)
        print("🎉 问卷调查系统演示完成！")
        print("=" * 60)
        
        print("\n💡 系统优势:")
        print("✅ 标准化数据收集 - 确保信息完整性和一致性")
        print("✅ 智能背景分析 - AI自动评估用户学习准备度")
        print("✅ 个性化推荐 - 基于用户特征定制学习路径")
        print("✅ 数据持久化 - 保存用户档案和学习进度")
        print("✅ MCP集成 - AI模型可直接调用问卷调查功能")
        
        print("\n🚀 下一步:")
        print("1. 运行 'python user_survey_system.py' 体验完整问卷")
        print("2. 运行 'python mcp_server.py' 启动MCP服务器")
        print("3. 在AI模型中配置问卷调查工具")
        print("4. 收集真实用户数据，优化问卷内容")
    
    def _display_results(self, result: dict):
        """显示结果"""
        if "survey_analysis" in result:
            analysis = result["survey_analysis"]
            if "background_analysis" in analysis:
                readiness = analysis["background_analysis"]["overall_readiness"]
                print(f"📊 学习准备度: {readiness:.2f}")
            
            if "learning_advice" in analysis:
                print("💡 学习建议:")
                for i, advice in enumerate(analysis["learning_advice"][:2], 1):
                    print(f"   {i}. {advice}")
        
        if "estimated_total_hours" in result:
            print(f"⏱️ 总学习时长: {result['estimated_total_hours']}小时")
        
        if "time_schedule" in result and "estimated_completion_date" in result["time_schedule"]:
            print(f"📅 预计完成时间: {result['time_schedule']['estimated_completion_date']}")
        
        if "learning_path" in result:
            path = result["learning_path"]
            if path:
                print("🎯 推荐学习顺序:")
                for i, chapter in enumerate(path[:3], 1):
                    if hasattr(chapter, 'title'):
                        print(f"   {i}. {chapter.title} ({chapter.difficulty}级)")
                    else:
                        print(f"   {i}. {chapter.get('title', '未知')} ({chapter.get('difficulty', '未知')}级)")
                if len(path) > 3:
                    print(f"   ... 还有{len(path)-3}个章节")

async def main():
    """主函数"""
    demo = SurveyDemo()
    await demo.run_demo()

if __name__ == "__main__":
    print("🚀 启动问卷调查系统演示...")
    asyncio.run(main())
