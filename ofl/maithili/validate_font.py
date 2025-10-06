#!/usr/bin/env python3
"""
Font Validation Script for Maithili Test Font
Checks basic font properties and character coverage
"""

import os
import sys

try:
    import fontforge
except ImportError:
    print("❌ FontForge Python module not found!")
    print("Install with: pip3 install fontforge-python")
    sys.exit(1)

def validate_font(font_path):
    """Validate font file and check character coverage"""
    
    if not os.path.exists(font_path):
        print(f"❌ Font file not found: {font_path}")
        return False
    
    try:
        font = fontforge.open(font_path)
        print(f"\n📁 Validating: {os.path.basename(font_path)}")
        print("=" * 50)
        
        # Basic font info
        print(f"✅ Font Name: {font.fontname}")
        print(f"✅ Family Name: {font.familyname}")
        print(f"✅ Full Name: {font.fullname}")
        print(f"✅ Version: {font.version}")
        print(f"✅ Weight: {font.weight}")
        print(f"✅ Encoding: {font.encoding}")
        print(f"✅ EM Size: {font.em}")
        print(f"✅ Ascent: {font.ascent}")
        print(f"✅ Descent: {font.descent}")
        
        # Character coverage
        print(f"\n📝 Character Coverage:")
        
        # Essential Maithili character ranges
        ranges_to_check = [
            (0x0905, 0x0914, "Devanagari Vowels"),
            (0x0915, 0x0939, "Devanagari Consonants"),
            (0x0966, 0x096F, "Devanagari Digits"),
        ]
        
        total_chars = 0
        present_chars = 0
        
        for start, end, name in ranges_to_check:
            range_present = 0
            range_total = end - start + 1
            
            for unicode_val in range(start, end + 1):
                if unicode_val in font:
                    range_present += 1
                    present_chars += 1
                total_chars += 1
            
            percentage = (range_present / range_total) * 100
            status = "✅" if percentage == 100 else "⚠️" if percentage > 0 else "❌"
            print(f"  {status} {name}: {range_present}/{range_total} ({percentage:.1f}%)")
        
        overall_percentage = (present_chars / total_chars) * 100
        print(f"\n📊 Overall Coverage: {present_chars}/{total_chars} ({overall_percentage:.1f}%)")
        
        # File size
        file_size = os.path.getsize(font_path)
        print(f"📦 File Size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
        
        # Check specific important characters
        important_chars = [
            (0x0905, "अ", "Devanagari Letter A"),
            (0x0915, "क", "Devanagari Letter KA"),
            (0x092E, "म", "Devanagari Letter MA"),
            (0x0939, "ह", "Devanagari Letter HA"),
            (0x0966, "०", "Devanagari Digit Zero"),
            (0x0967, "१", "Devanagari Digit One"),
        ]
        
        print(f"\n🔍 Key Character Check:")
        for unicode_val, char, description in important_chars:
            status = "✅" if unicode_val in font else "❌"
            print(f"  {status} U+{unicode_val:04X} ({char}) - {description}")
        
        font.close()
        print(f"\n✅ Validation completed successfully!")
        return True
        
    except Exception as e:
        print(f"❌ Error validating font: {e}")
        return False

def main():
    """Main function"""
    print("🔍 Maithili Font Validator")
    print("=" * 40)
    
    font_dir = "/Users/vikramkumar/Desktop/Google fonts project/fonts/ofl/maithili"
    
    fonts_to_check = [
        "MaithiliTest-Regular.ttf",
        "MaithiliTest-Bold.ttf"
    ]
    
    all_valid = True
    
    for font_file in fonts_to_check:
        font_path = os.path.join(font_dir, font_file)
        if not validate_font(font_path):
            all_valid = False
    
    print("\n" + "=" * 50)
    if all_valid:
        print("🎉 All fonts validated successfully!")
        print("\n📋 Next Steps:")
        print("1. Open test_font.html in browser to see visual results")
        print("2. Test with actual Maithili text")
        print("3. Get feedback from Maithili language community")
        print("4. Improve character designs based on feedback")
        print("5. Add more characters and OpenType features")
    else:
        print("⚠️ Some issues found. Please fix them before proceeding.")
    
    # Show sample test commands
    print(f"\n🧪 Test Commands:")
    print(f"Open test page: open test_font.html")
    print(f"Install fonts: cp *.ttf ~/Library/Fonts/")
    print(f"Test in TextEdit or other apps")

if __name__ == "__main__":
    main()
