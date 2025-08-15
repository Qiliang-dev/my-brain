import zipfile
import xml.etree.ElementTree as ET
import os
import re

def extract_ppt_content(ppt_file):
    """提取PPT文件中的文本内容"""
    content = []
    try:
        with zipfile.ZipFile(ppt_file, 'r') as z:
            slides = [f for f in z.namelist() if f.startswith("ppt/slides/slide")]
            slides.sort()
            
            for i, slide in enumerate(slides):
                slide_content = []
                try:
                    xml_content = ET.fromstring(z.read(slide))
                    texts = xml_content.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/main}t")
                    for text in texts:
                        if text.text and text.text.strip():
                            slide_content.append(text.text.strip())
                    if slide_content:
                        content.append(f"## Slide {i+1}")
                        content.extend(slide_content)
                        content.append("")
                except Exception as e:
                    print(f"Error processing slide {i+1} in {ppt_file}: {e}")
    except Exception as e:
        print(f"Error opening {ppt_file}: {e}")
    
    return content

def get_topic_name(ppt_file):
    """根据PPT文件名确定主题名称"""
    filename = os.path.basename(ppt_file)
    
    # 定义PPT文件到主题的映射
    topic_mapping = {
        "04_V4_ISTQB_Testing_Throughout_Software Development_Lifecycle.pptx": "04_Testing_Throughout_Software_Lifecycle_软件生命周期中的测试",
        "05_V4_ISTQB_Static_Testing.pptx": "05_Static_Testing_静态测试",
        "06_V4_ISTQB_Test_Analysis_and_Design_01.pptx": "06_Test_Analysis_and_Design_01_测试分析和设计_01",
        "07_V4_ISTQB_Test_Analysis_and_Design_02.pptx": "07_Test_Analysis_and_Design_02_测试分析和设计_02", 
        "08_V4_ISTQB_Test_Analysis_and_Design_03.pptx": "08_Test_Analysis_and_Design_03_测试分析和设计_03",
        "09_V4_ISTQB_Test_Management_01.pptx": "09_Test_Management_01_测试管理_01",
        "10_V4_ISTQB_Test_Management_02.pptx": "10_Test_Management_02_测试管理_02",
        "11_V4_ISTQB_Test_Tools.pptx": "11_Test_Tools_测试工具"
    }
    
    return topic_mapping.get(filename, filename.replace('.pptx', ''))

def create_markdown_content(topic_name, content):
    """创建Markdown格式的内容"""
    markdown_content = []
    markdown_content.append(f"# {topic_name}")
    markdown_content.append("")
    markdown_content.append("## 概述 / Overview")
    markdown_content.append(f"- **主题 / Topic**: {topic_name}")
    markdown_content.append("- **来源 / Source**: ISTQB Foundation V4")
    markdown_content.append("- **章节 / Chapter**: " + topic_name.split('_')[0] + "_" + "_".join(topic_name.split('_')[1:]))
    markdown_content.append("")
    markdown_content.append("## 主要内容 / Main Content")
    markdown_content.append("")
    
    # 添加提取的内容
    markdown_content.extend(content)
    
    return markdown_content

def main():
    """主函数：处理所有PPT文件"""
    # 获取当前目录下的所有PPT文件
    ppt_files = [f for f in os.listdir('.') if f.endswith('.pptx') and f.startswith(('04_', '05_', '06_', '07_', '08_', '09_', '10_', '11_'))]
    ppt_files.sort()
    
    print(f"找到 {len(ppt_files)} 个PPT文件需要处理:")
    for ppt in ppt_files:
        print(f"  - {ppt}")
    
    # 处理每个PPT文件
    for ppt_file in ppt_files:
        print(f"\n正在处理: {ppt_file}")
        
        # 提取内容
        content = extract_ppt_content(ppt_file)
        
        if content:
            # 获取主题名称
            topic_name = get_topic_name(ppt_file)
            
            # 创建Markdown内容
            markdown_content = create_markdown_content(topic_name, content)
            
            # 保存到文件
            output_file = f"projects/istqb_certification/{topic_name}.md"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(markdown_content))
            
            print(f"已保存到: {output_file}")
        else:
            print(f"警告: {ppt_file} 没有提取到内容")

if __name__ == "__main__":
    main()
