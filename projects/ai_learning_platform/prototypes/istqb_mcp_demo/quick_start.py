#!/usr/bin/env python3
"""
ISTQB MCP工具快速启动脚本
无需配置，直接体验MCP工具功能
"""

import asyncio
import json
from datetime import datetime
from istqb_learning_tool import ISTQBLearningPathTool, UserProfile

class QuickStartDemo:
    """快速启动演示"""
    
    def __init__(self):
        """初始化演示"""
        self.tool = ISTQBLearningPathTool()
        print("🎯 ISTQB学习平台MCP工具快速演示")
        print("=" * 50)
    
    async def run_demo(self):
        """运行演示"""
        try:
            # 演示1：计算机专业用户
            await self.demo_computer_science_user()
            
            print("\n" + "=" * 50)
            
            # 演示2：非计算机专业用户
            await self.demo_non_computer_user()
            
            print("\n" + "=" * 50)
            
            # 演示3：有测试经验的用户
            await self.demo_experienced_user()
            
            print("\n" + "=" * 50)
            
            # 显示课程大纲
            await self.show_curriculum()
            
            print("\n🎉 演示完成！")
            print("\n💡 下一步操作:")
            print("1. 运行 'python test_client.py' 查看完整演示")
            print("2. 运行 'python mcp_server.py' 启动MCP服务器")
            print("3. 在AI模型中配置MCP工具")
            
        except Exception as e:
            print(f"❌ 演示过程中出错: {str(e)}")
    
    async def demo_computer_science_user(self):
        """演示计算机专业用户"""
        print("\n👤 演示用户1: 计算机科学专业，有编程经验")
        
        user = UserProfile(
            user_id="demo_cs_user",
            background="计算机科学专业",
            programming_experience="有经验",
            testing_experience="基础",
            learning_style="实践型",
            available_hours_per_week=20
        )
        
        print("🔍 分析用户背景...")
        background_analysis = self.tool._analyze_user_background(user)
        print(f"📊 准备度评分: {background_analysis['overall_readiness']:.2f}")
        
        print("📚 生成学习路径...")
        result = await self.tool.generate_istqb_learning_path(user)
        
        if "error" not in result:
            print(f"✅ 学习路径生成成功！")
            print(f"⏱️ 总学习时长: {result['estimated_total_hours']}小时")
            print(f"📅 预计完成时间: {result['time_schedule']['estimated_completion_date']}")
            print(f"🎯 推荐学习顺序:")
            for i, chapter in enumerate(result['learning_path'][:3], 1):
                print(f"   {i}. {chapter.title} ({chapter.difficulty}级)")
            
            print(f"💡 学习建议:")
            for i, advice in enumerate(result['learning_advice'][:2], 1):
                print(f"   {i}. {advice}")
        else:
            print(f"❌ 生成失败: {result['error']}")
    
    async def demo_non_computer_user(self):
        """演示非计算机专业用户"""
        print("\n👤 演示用户2: 机械工程专业，无编程经验")
        
        user = UserProfile(
            user_id="demo_me_user",
            background="机械工程专业",
            programming_experience="无经验",
            testing_experience="无经验",
            learning_style="视觉型",
            available_hours_per_week=15
        )
        
        print("🔍 分析用户背景...")
        background_analysis = self.tool._analyze_user_background(user)
        print(f"📊 准备度评分: {background_analysis['overall_readiness']:.2f}")
        
        print("📚 生成学习路径...")
        result = await self.tool.generate_istqb_learning_path(user)
        
        if "error" not in result:
            print(f"✅ 学习路径生成成功！")
            print(f"⏱️ 总学习时长: {result['estimated_total_hours']}小时")
            print(f"📅 预计完成时间: {result['time_schedule']['estimated_completion_date']}")
            print(f"🎯 推荐学习顺序:")
            for i, chapter in enumerate(result['learning_path'][:3], 1):
                print(f"   {i}. {chapter.title} ({chapter.difficulty}级)")
            
            print(f"💡 学习建议:")
            for i, advice in enumerate(result['learning_advice'][:2], 1):
                print(f"   {i}. {advice}")
        else:
            print(f"❌ 生成失败: {result['error']}")
    
    async def demo_experienced_user(self):
        """演示有测试经验的用户"""
        print("\n👤 演示用户3: 软件工程专业，有测试经验")
        
        user = UserProfile(
            user_id="demo_se_user",
            background="软件工程专业",
            programming_experience="有经验",
            testing_experience="有经验",
            learning_style="听觉型",
            available_hours_per_week=25
        )
        
        print("🔍 分析用户背景...")
        background_analysis = self.tool._analyze_user_background(user)
        print(f"📊 准备度评分: {background_analysis['overall_readiness']:.2f}")
        
        print("📚 生成学习路径...")
        result = await self.tool.generate_istqb_learning_path(user)
        
        if "error" not in result:
            print(f"✅ 学习路径生成成功！")
            print(f"⏱️ 总学习时长: {result['estimated_total_hours']}小时")
            print(f"📅 预计完成时间: {result['time_schedule']['estimated_completion_date']}")
            print(f"🎯 推荐学习顺序:")
            for i, chapter in enumerate(result['learning_path'][:3], 1):
                print(f"   {i}. {chapter.title} ({chapter.difficulty}级)")
            
            print(f"💡 学习建议:")
            for i, advice in enumerate(result['learning_advice'][:2], 1):
                print(f"   {i}. {advice}")
        else:
            print(f"❌ 生成失败: {result['error']}")
    
    async def show_curriculum(self):
        """显示课程大纲"""
        print("\n📖 ISTQB课程大纲")
        print("-" * 30)
        
        curriculum = self.tool.istqb_curriculum
        total_hours = sum(ch.estimated_hours for ch in curriculum.values())
        
        print(f"📚 总章节数: {len(curriculum)}")
        print(f"⏱️ 总学习时长: {total_hours}小时")
        print("\n📋 章节详情:")
        
        for chapter_id, chapter in curriculum.items():
            print(f"  {chapter_id}. {chapter.title} ({chapter.title_en})")
            print(f"     难度: {chapter.difficulty} | 时长: {chapter.estimated_hours}小时")
            print(f"     关键概念: {', '.join(chapter.key_concepts[:2])}...")
            print(f"     实践项目: {', '.join(chapter.practice_projects[:2])}...")
            print()
    
    def show_mcp_integration_info(self):
        """显示MCP集成信息"""
        print("\n🔧 MCP工具集成信息")
        print("-" * 30)
        print("可用工具:")
        print("1. generate_istqb_learning_path - 生成学习路径")
        print("2. assess_user_readiness - 评估用户准备度")
        print("3. get_istqb_curriculum - 获取课程大纲")
        print("\n配置示例:")
        print("在AI模型配置中添加:")
        print(json.dumps({
            "mcpServers": {
                "istqb_learning_platform": {
                    "command": "python",
                    "args": ["mcp_server.py"],
                    "cwd": "/path/to/istqb_mcp_demo"
                }
            }
        }, indent=2, ensure_ascii=False))

async def main():
    """主函数"""
    demo = QuickStartDemo()
    await demo.run_demo()
    
    # 显示MCP集成信息
    demo.show_mcp_integration_info()

if __name__ == "__main__":
    print("🚀 启动ISTQB MCP工具快速演示...")
    asyncio.run(main())
