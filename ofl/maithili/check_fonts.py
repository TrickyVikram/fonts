#!/usr/bin/env python3
"""
Quick validation script for improved fonts
"""

import fontforge
import os

def check_improved_fonts():
    """Check the improved font files"""
    
    print("🔍 Checking Improved Maithili Fonts")
    print("=" * 40)
    
    font_dir = "/Users/vikramkumar/Desktop/Google fonts project/fonts/ofl/maithili"
    
    fonts = [
        "MaithiliImproved-Regular.ttf",
        "MaithiliImproved-Bold.ttf"
    ]
    
    for font_file in fonts:
        font_path = os.path.join(font_dir, font_file)
        
        if os.path.exists(font_path):
            font = fontforge.open(font_path)
            
            print(f"\n✅ {font_file}")
            print(f"   Font Name: {font.fontname}")
            print(f"   Family: {font.familyname}")
            print(f"   Weight: {font.weight}")
            print(f"   File Size: {os.path.getsize(font_path):,} bytes")
            
            # Check key characters
            test_chars = [0x0905, 0x0915, 0x0966, 0x0967]  # अ क ० १
            present = sum(1 for char in test_chars if char in font)
            print(f"   Key chars: {present}/{len(test_chars)} present")
            
            font.close()
        else:
            print(f"❌ {font_file} not found")
    
    print(f"\n🎨 Font Comparison:")
    print(f"📁 Files in directory:")
    for f in sorted(os.listdir(font_dir)):
        if f.endswith('.ttf'):
            size = os.path.getsize(os.path.join(font_dir, f))
            print(f"   {f}: {size:,} bytes")

if __name__ == "__main__":
    check_improved_fonts()
