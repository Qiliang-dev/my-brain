import zipfile
import xml.etree.ElementTree as ET

z = zipfile.ZipFile("06_V4_ISTQB_Test_Analysis_and_Design_01.pptx")
slides = [f for f in z.namelist() if f.startswith("ppt/slides/slide")]
slides.sort()

for i, slide in enumerate(slides):
    print(f"=== Slide {i+1} ===")
    try:
        xml_content = ET.fromstring(z.read(slide))
        texts = xml_content.findall(".//{http://schemas.openxmlformats.org/drawingml/2006/main}t")
        for text in texts:
            if text.text:
                print(text.text)
        print()
    except Exception as e:
        print(f"Error processing slide {i+1}: {e}")
        print()

z.close()
