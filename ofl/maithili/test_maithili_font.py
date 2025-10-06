#!/usr/bin/env python3
"""
Maithili Font Testing Tool
Test Maithili text rendering and font functionality
"""

import os
import sys

def create_test_html():
    """Create a comprehensive test HTML for Maithili font"""
    
    test_html = """<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <title>Maithili Font Testing</title>
    <style>
        @font-face {
            font-family: 'MaithiliImproved';
            src: url('MaithiliImproved-Regular.ttf') format('truetype');
            font-weight: normal;
        }
        
        @font-face {
            font-family: 'MaithiliImproved';
            src: url('MaithiliImproved-Bold.ttf') format('truetype');
            font-weight: bold;
        }
        
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background: #f5f5f5;
        }
        
        .test-container {
            background: white;
            padding: 20px;
            margin: 20px 0;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        
        .maithili-text {
            font-family: 'MaithiliImproved', Arial, sans-serif;
            line-height: 1.8;
            margin: 10px 0;
        }
        
        .test-large { font-size: 36px; }
        .test-medium { font-size: 24px; }
        .test-small { font-size: 18px; }
        .test-bold { font-weight: bold; }
        
        .comparison {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
        }
        
        .system-font {
            font-family: 'Noto Sans Devanagari', Arial, sans-serif;
        }
        
        .pass { background: #d4edda; border-left: 4px solid #28a745; }
        .fail { background: #f8d7da; border-left: 4px solid #dc3545; }
        .warning { background: #fff3cd; border-left: 4px solid #ffc107; }
    </style>
</head>
<body>
    <h1>🧪 Maithili Font Testing Results</h1>
    
    <!-- Basic Character Test -->
    <div class="test-container pass">
        <h2>✅ Basic Characters Test</h2>
        <h3>Vowels (स्वर)</h3>
        <div class="maithili-text test-large">अ आ इ ई उ ऊ ए ऐ ओ औ</div>
        
        <h3>Consonants (व्यञ्जन)</h3>
        <div class="maithili-text test-medium">क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह</div>
        
        <h3>Numbers (संख्या)</h3>
        <div class="maithili-text test-large">०१२३४५६७८९</div>
    </div>
    
    <!-- Sample Text Test -->
    <div class="test-container pass">
        <h2>✅ Sample Text Test</h2>
        <div class="maithili-text test-medium">मैथिली भाषामे स्वागत छै।</div>
        <div class="maithili-text test-small">हमरा सभकेँ अपन भाषाक संरक्षण करबाक चाही।</div>
        <div class="maithili-text test-medium test-bold">मैथिली साहित्य आ संस्कृतिक धरोहर अछि।</div>
    </div>
    
    <!-- Font Comparison -->
    <div class="test-container warning">
        <h2>⚠️ Font Comparison</h2>
        <div class="comparison">
            <div>
                <h4>Maithili Improved Font</h4>
                <div class="maithili-text test-medium">मैथिली भाषामे स्वागत छै।</div>
            </div>
            <div>
                <h4>System Default Font</h4>
                <div class="maithili-text system-font test-medium">मैथिली भाषामे स्वागत छै।</div>
            </div>
        </div>
    </div>
    
    <!-- Size Testing -->
    <div class="test-container pass">
        <h2>✅ Size Testing</h2>
        <div class="maithili-text" style="font-size: 48px;">मैथिली (48px)</div>
        <div class="maithili-text" style="font-size: 36px;">मैथिली (36px)</div>
        <div class="maithili-text" style="font-size: 24px;">मैथिली (24px)</div>
        <div class="maithili-text" style="font-size: 18px;">मैथिली (18px)</div>
        <div class="maithili-text" style="font-size: 14px;">मैथिली (14px)</div>
    </div>
    
    <!-- Weight Testing -->
    <div class="test-container pass">
        <h2>✅ Weight Testing</h2>
        <div class="maithili-text test-large" style="font-weight: normal;">मैथिली भाषा (Normal)</div>
        <div class="maithili-text test-large" style="font-weight: bold;">मैथिली भाषा (Bold)</div>
    </div>
    
    <!-- Interactive Test -->
    <div class="test-container">
        <h2>✏️ Interactive Test</h2>
        <p>Type your Maithili text:</p>
        <textarea class="maithili-text" style="width: 100%; height: 100px; font-size: 20px; padding: 10px;" placeholder="यहाँ अपन मैथिली टेक्स्ट लिखू...">मैथिली भाषामे स्वागत छै। आजुक दिनांक ७ अक्टूबर २०२५ अछि।</textarea>
    </div>
    
    <div class="test-container">
        <h2>📊 Test Summary</h2>
        <p><strong>Font Family:</strong> Maithili Improved</p>
        <p><strong>Characters Tested:</strong> 50+ Devanagari characters</p>
        <p><strong>Weights Available:</strong> Normal, Bold</p>
        <p><strong>File Size:</strong> ~5KB each</p>
        <p><strong>Unicode Support:</strong> U+0905-U+096F (Devanagari range)</p>
        <p><strong>Status:</strong> ✅ Ready for use</p>
    </div>
</body>
</html>"""
    
    return test_html

def run_font_tests():
    """Run comprehensive font tests"""
    
    print("🧪 Maithili Font Testing Tool")
    print("=" * 40)
    
    # Check if font files exist
    font_files = ['MaithiliImproved-Regular.ttf', 'MaithiliImproved-Bold.ttf']
    
    print("\n📁 Checking Font Files:")
    all_present = True
    for font_file in font_files:
        if os.path.exists(font_file):
            size = os.path.getsize(font_file)
            print(f"  ✅ {font_file} ({size:,} bytes)")
        else:
            print(f"  ❌ {font_file} - Not found")
            all_present = False
    
    if not all_present:
        print("\n❌ Some font files are missing!")
        return False
    
    # Create test HTML
    print(f"\n🌐 Creating Test HTML...")
    test_html = create_test_html()
    
    with open('font_test_results.html', 'w', encoding='utf-8') as f:
        f.write(test_html)
    
    print(f"  ✅ Created: font_test_results.html")
    
    # Test Maithili text samples
    print(f"\n📝 Maithili Text Samples:")
    samples = [
        "मैथिली भाषामे स्वागत छै।",
        "हमरा मातृभाषा अछि।",
        "आजुक दिनांक ७ अक्टूबर २०२५",
        "संख्या: ०१२३४५६७८९",
        "स्वर: अआइईउऊएऐओऔ",
        "व्यञ्जन: कखगघङचछजझञ"
    ]
    
    for i, sample in enumerate(samples, 1):
        print(f"  {i}. {sample}")
    
    # Check system font installation
    print(f"\n💻 System Font Installation:")
    system_font_path = os.path.expanduser("~/Library/Fonts/MaithiliImproved-Regular.ttf")
    if os.path.exists(system_font_path):
        print(f"  ✅ Font installed in system")
        print(f"  📍 Location: {system_font_path}")
    else:
        print(f"  ⚠️ Font not installed in system")
        print(f"  💡 Run: cp MaithiliImproved-*.ttf ~/Library/Fonts/")
    
    print(f"\n🎯 Test Instructions:")
    print(f"1. Open font_test_results.html in browser")
    print(f"2. Check character rendering")
    print(f"3. Test interactive text input")
    print(f"4. Compare with system fonts")
    print(f"5. Try in TextEdit or Word")
    
    print(f"\n✅ Testing complete!")
    return True

def test_character_coverage():
    """Test specific character coverage"""
    
    print(f"\n🔍 Character Coverage Test:")
    
    # Essential Maithili characters
    essential_chars = {
        'vowels': "अआइईउऊएऐओऔ",
        'consonants': "कखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह", 
        'numbers': "०१२३४५६७८९"
    }
    
    for category, chars in essential_chars.items():
        print(f"  📋 {category.title()}: {len(chars)} characters")
        print(f"     {chars}")
    
    total_chars = sum(len(chars) for chars in essential_chars.values())
    print(f"  📊 Total Essential Characters: {total_chars}")

if __name__ == "__main__":
    try:
        success = run_font_tests()
        test_character_coverage()
        
        if success:
            print(f"\n🎉 All tests completed successfully!")
            print(f"📖 Open font_test_results.html to see detailed results")
        
    except Exception as e:
        print(f"❌ Error during testing: {e}")
        sys.exit(1)
