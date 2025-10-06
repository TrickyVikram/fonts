#!/usr/bin/env python3
"""
मैथिली भाषा Font Testing Script
Test specific Maithili language features and text samples
"""

def create_maithili_test_samples():
    """Create comprehensive Maithili text samples for testing"""
    
    samples = {
        "basic_greeting": {
            "text": "मैथिली भाषामे स्वागत छै।",
            "translation": "Welcome to Maithili language.",
            "category": "Basic Greeting"
        },
        
        "self_introduction": {
            "text": "हमर नाम विक्रम अछि। हम मैथिली बाजैत छी।",
            "translation": "My name is Vikram. I speak Maithili.",
            "category": "Self Introduction"
        },
        
        "family": {
            "text": "हमर परिवारमे चारि गोटे अछि। माता, पिता, भाई आ हम।",
            "translation": "There are four people in my family. Mother, father, brother and me.",
            "category": "Family"
        },
        
        "daily_routine": {
            "text": "हम सबेरे उठैत छी। स्नान करैत छी। खाना खाइत छी।",
            "translation": "I wake up in the morning. I take a bath. I eat food.",
            "category": "Daily Routine"
        },
        
        "numbers_date": {
            "text": "आजुक दिनांक ७ अक्टूबर २०२५ अछि। समय दुपहर १२ बजे अछि।",
            "translation": "Today's date is 7 October 2025. The time is 12 noon.",
            "category": "Numbers & Date"
        },
        
        "weather": {
            "text": "आइ मौसम बड्ड नीक अछि। तापमान २५ डिग्री अछि।",
            "translation": "Today the weather is very nice. The temperature is 25 degrees.",
            "category": "Weather"
        },
        
        "education": {
            "text": "हम विद्यालयमे पढ़ैत छी। मैथिली हमर प्रिय विषय अछि।",
            "translation": "I study in school. Maithili is my favorite subject.",
            "category": "Education"
        },
        
        "culture": {
            "text": "मैथिली साहित्य बहुत समृद्ध अछि। हमरा अपन संस्कृति पर गर्व अछि।",
            "translation": "Maithili literature is very rich. We are proud of our culture.",
            "category": "Culture"
        },
        
        "poetry": {
            "text": "मैथिली भाषाक माधुर्य, हृदयमे बसल रहै छै।",
            "translation": "The sweetness of Maithili language resides in the heart.",
            "category": "Poetry"
        },
        
        "technology": {
            "text": "आजुक युगमे तकनीक बहुत महत्वपूर्ण अछि। कंप्यूटर सभक जीवन सरल बना देलक।",
            "translation": "Technology is very important in today's era. Computers have made everyone's life simple.",
            "category": "Technology"
        }
    }
    
    return samples

def create_interactive_maithili_tester():
    """Create an interactive HTML tester for Maithili"""
    
    samples = create_maithili_test_samples()
    
    html_content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>मैथिली भाषा Font Tester</title>
    <style>
        @font-face {{
            font-family: 'MaithiliImproved';
            src: url('MaithiliImproved-Regular.ttf') format('truetype');
            font-weight: normal;
        }}
        
        @font-face {{
            font-family: 'MaithiliImproved';
            src: url('MaithiliImproved-Bold.ttf') format('truetype');
            font-weight: bold;
        }}
        
        body {{
            font-family: system-ui, Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
            min-height: 100vh;
            color: #333;
        }}
        
        .container {{
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 40px;
            padding-bottom: 20px;
            border-bottom: 3px solid #1e3c72;
        }}
        
        .header h1 {{
            color: #1e3c72;
            font-size: 2.5em;
            margin: 0;
        }}
        
        .maithili-title {{
            font-family: 'MaithiliImproved', Arial, sans-serif;
            font-size: 36px;
            color: #2a5298;
            margin: 10px 0;
        }}
        
        .sample-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }}
        
        .sample-card {{
            background: #f8f9fa;
            border-radius: 10px;
            padding: 20px;
            border-left: 5px solid #1e3c72;
            transition: all 0.3s ease;
        }}
        
        .sample-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        }}
        
        .sample-category {{
            font-size: 12px;
            color: #1e3c72;
            font-weight: bold;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        
        .maithili-text {{
            font-family: 'MaithiliImproved', Arial, sans-serif;
            font-size: 22px;
            line-height: 1.6;
            color: #333;
            margin: 10px 0;
            padding: 15px;
            background: white;
            border-radius: 8px;
            border: 1px solid #e0e0e0;
        }}
        
        .translation {{
            font-size: 14px;
            color: #666;
            font-style: italic;
            margin-top: 10px;
        }}
        
        .interactive-section {{
            background: linear-gradient(45deg, #1e3c72, #2a5298);
            color: white;
            padding: 30px;
            border-radius: 15px;
            margin: 30px 0;
        }}
        
        .test-input {{
            width: 100%;
            padding: 15px;
            font-size: 20px;
            font-family: 'MaithiliImproved', Arial, sans-serif;
            border: none;
            border-radius: 8px;
            margin: 15px 0;
            min-height: 100px;
            resize: vertical;
        }}
        
        .controls {{
            display: flex;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }}
        
        .control {{
            background: rgba(255,255,255,0.2);
            padding: 10px 15px;
            border-radius: 25px;
            border: none;
            color: white;
            cursor: pointer;
            transition: all 0.3s ease;
        }}
        
        .control:hover {{
            background: rgba(255,255,255,0.3);
            transform: scale(1.05);
        }}
        
        .size-selector {{
            background: white;
            color: #333;
            padding: 8px 12px;
            border: none;
            border-radius: 5px;
        }}
        
        .stats-section {{
            background: #f8f9fa;
            padding: 25px;
            border-radius: 10px;
            margin: 30px 0;
        }}
        
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
            gap: 20px;
        }}
        
        .stat-item {{
            text-align: center;
            padding: 15px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        }}
        
        .stat-number {{
            font-size: 2em;
            font-weight: bold;
            color: #1e3c72;
        }}
        
        .character-showcase {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
            gap: 10px;
            margin: 20px 0;
        }}
        
        .char-display {{
            background: white;
            border: 2px solid #e0e0e0;
            border-radius: 8px;
            padding: 15px;
            text-align: center;
            font-family: 'MaithiliImproved', Arial, sans-serif;
            font-size: 24px;
            transition: all 0.3s ease;
        }}
        
        .char-display:hover {{
            border-color: #1e3c72;
            transform: scale(1.1);
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎨 मैथिली भाषा Font Tester</h1>
            <div class="maithili-title">मैथिली भाषामे स्वागत छै</div>
            <p>Comprehensive testing for Maithili language typography</p>
        </div>
        
        <!-- Statistics -->
        <div class="stats-section">
            <h2>📊 Font Statistics</h2>
            <div class="stats-grid">
                <div class="stat-item">
                    <div class="stat-number">53</div>
                    <div>Characters</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">10</div>
                    <div>Vowels</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">33</div>
                    <div>Consonants</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number">10</div>
                    <div>Numbers</div>
                </div>
            </div>
        </div>
        
        <!-- Character Showcase -->
        <div class="stats-section">
            <h2>🔤 Character Showcase</h2>
            <h3>Vowels (स्वर)</h3>
            <div class="character-showcase">
                <div class="char-display">अ</div>
                <div class="char-display">आ</div>
                <div class="char-display">इ</div>
                <div class="char-display">ई</div>
                <div class="char-display">उ</div>
                <div class="char-display">ऊ</div>
                <div class="char-display">ए</div>
                <div class="char-display">ऐ</div>
                <div class="char-display">ओ</div>
                <div class="char-display">औ</div>
            </div>
            
            <h3>Numbers (संख्या)</h3>
            <div class="character-showcase">
                <div class="char-display">०</div>
                <div class="char-display">१</div>
                <div class="char-display">२</div>
                <div class="char-display">३</div>
                <div class="char-display">४</div>
                <div class="char-display">५</div>
                <div class="char-display">६</div>
                <div class="char-display">७</div>
                <div class="char-display">८</div>
                <div class="char-display">९</div>
            </div>
        </div>
        
        <!-- Sample Texts -->
        <div class="stats-section">
            <h2>📝 Maithili Text Samples</h2>
            <div class="sample-grid">"""
    
    for key, sample in samples.items():
        html_content += f"""
                <div class="sample-card">
                    <div class="sample-category">{sample['category']}</div>
                    <div class="maithili-text">{sample['text']}</div>
                    <div class="translation">{sample['translation']}</div>
                </div>"""
    
    html_content += """
            </div>
        </div>
        
        <!-- Interactive Testing -->
        <div class="interactive-section">
            <h2 style="margin-top: 0;">✏️ Interactive Testing</h2>
            <p>Type or paste your own Maithili text:</p>
            
            <div class="controls">
                <button class="control" onclick="insertSample('मैथिली भाषामे स्वागत छै।')">Sample 1</button>
                <button class="control" onclick="insertSample('हमर नाम विक्रम अछि।')">Sample 2</button>
                <button class="control" onclick="insertSample('आजुक दिनांक ७ अक्टूबर २०२५')">Date</button>
                <button class="control" onclick="insertSample('अआइईउऊएऐओऔ')">Vowels</button>
                <button class="control" onclick="insertSample('०१२३४५६७८९')">Numbers</button>
                <select class="size-selector" onchange="changeFontSize(this.value)">
                    <option value="20">20px</option>
                    <option value="24" selected>24px</option>
                    <option value="28">28px</option>
                    <option value="32">32px</option>
                    <option value="36">36px</option>
                </select>
            </div>
            
            <textarea id="testInput" class="test-input" placeholder="यहाँ अपन मैथिली टेक्स्ट लिखू...">मैथिली भाषामे स्वागत छै! आजुक दिनांक ७ अक्टूबर २०२५ अछि।</textarea>
            
            <div id="livePreview" class="maithili-text" style="background: rgba(255,255,255,0.1); color: white; font-size: 24px;">
                मैथिली भाषामे स्वागत छै! आजुक दिनांक ७ अक्टूबर २०२५ अछि।
            </div>
        </div>
        
        <!-- Download Section -->
        <div class="stats-section">
            <h2>💾 Download Fonts</h2>
            <p>Download the Maithili font files for your projects:</p>
            <div style="text-align: center; margin: 20px 0;">
                <a href="MaithiliImproved-Regular.ttf" download style="display: inline-block; background: #1e3c72; color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; margin: 10px;">
                    📥 Download Regular Font
                </a>
                <a href="MaithiliImproved-Bold.ttf" download style="display: inline-block; background: #2a5298; color: white; padding: 15px 30px; text-decoration: none; border-radius: 8px; margin: 10px;">
                    📥 Download Bold Font
                </a>
            </div>
        </div>
    </div>
    
    <script>
        function insertSample(text) {
            const input = document.getElementById('testInput');
            input.value = text;
            updatePreview();
        }
        
        function changeFontSize(size) {
            const input = document.getElementById('testInput');
            const preview = document.getElementById('livePreview');
            input.style.fontSize = size + 'px';
            preview.style.fontSize = size + 'px';
        }
        
        function updatePreview() {
            const input = document.getElementById('testInput');
            const preview = document.getElementById('livePreview');
            preview.textContent = input.value || 'मैथिली भाषामे स्वागत छै!';
        }
        
        // Real-time preview
        document.getElementById('testInput').addEventListener('input', updatePreview);
        
        // Initialize
        updatePreview();
    </script>
</body>
</html>"""
    
    return html_content

def main():
    print("🎨 Creating Advanced Maithili Font Tester...")
    
    # Create the interactive tester
    html_content = create_interactive_maithili_tester()
    
    with open('maithili_language_tester.html', 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print("✅ Created: maithili_language_tester.html")
    
    # Show sample texts
    print(f"\n📝 Sample Maithili Texts Created:")
    samples = create_maithili_test_samples()
    
    for i, (key, sample) in enumerate(samples.items(), 1):
        print(f"  {i}. {sample['category']}: {sample['text']}")
    
    print(f"\n🧪 Testing Instructions:")
    print(f"1. Open maithili_language_tester.html in browser")
    print(f"2. Test all sample texts")
    print(f"3. Use interactive text input")
    print(f"4. Try different font sizes")
    print(f"5. Check character rendering")
    
    print(f"\n🎯 Maithili Text Features to Test:")
    print(f"  • Basic greetings and conversation")
    print(f"  • Numbers and dates") 
    print(f"  • Family and social contexts")
    print(f"  • Cultural and literary content")
    print(f"  • Modern technology terms")
    
    print(f"\n✅ Advanced Maithili tester ready!")

if __name__ == "__main__":
    main()
