#!/usr/bin/env python3
"""
Maithili Font Generator - Testing Version
Creates a basic TTF font with essential Maithili characters
"""

import fontforge
import os

def create_maithili_font():
    """Create a basic Maithili font with essential characters"""
    
    # Create new font
    font = fontforge.font()
    
    # Set font properties
    font.fontname = "MaithiliTest"
    font.familyname = "Maithili Test"
    font.fullname = "Maithili Test Regular"
    font.copyright = "Copyright 2024 Maithili Test Font"
    font.version = "1.000"
    font.weight = "Regular"
    
    # Set encoding
    font.encoding = "unicode"
    
    # Set font metrics
    font.em = 1000
    font.ascent = 800
    font.descent = 200
    
    # Essential Maithili characters with their Unicode values
    characters = {
        # Vowels
        0x0905: "अ",  # DEVANAGARI LETTER A
        0x0906: "आ",  # DEVANAGARI LETTER AA
        0x0907: "इ",  # DEVANAGARI LETTER I
        0x0908: "ई",  # DEVANAGARI LETTER II
        0x0909: "उ",  # DEVANAGARI LETTER U
        0x090A: "ऊ",  # DEVANAGARI LETTER UU
        0x090F: "ए",  # DEVANAGARI LETTER E
        0x0910: "ऐ",  # DEVANAGARI LETTER AI
        0x0913: "ओ",  # DEVANAGARI LETTER O
        0x0914: "औ",  # DEVANAGARI LETTER AU
        
        # Basic Consonants
        0x0915: "क",  # DEVANAGARI LETTER KA
        0x0916: "ख",  # DEVANAGARI LETTER KHA
        0x0917: "ग",  # DEVANAGARI LETTER GA
        0x0918: "घ",  # DEVANAGARI LETTER GHA
        0x0919: "ङ",  # DEVANAGARI LETTER NGA
        0x091A: "च",  # DEVANAGARI LETTER CA
        0x091B: "छ",  # DEVANAGARI LETTER CHA
        0x091C: "ज",  # DEVANAGARI LETTER JA
        0x091D: "झ",  # DEVANAGARI LETTER JHA
        0x091E: "ञ",  # DEVANAGARI LETTER NYA
        0x091F: "ट",  # DEVANAGARI LETTER TTA
        0x0920: "ठ",  # DEVANAGARI LETTER TTHA
        0x0921: "ड",  # DEVANAGARI LETTER DDA
        0x0922: "ढ",  # DEVANAGARI LETTER DDHA
        0x0923: "ण",  # DEVANAGARI LETTER NNA
        0x0924: "त",  # DEVANAGARI LETTER TA
        0x0925: "थ",  # DEVANAGARI LETTER THA
        0x0926: "द",  # DEVANAGARI LETTER DA
        0x0927: "ध",  # DEVANAGARI LETTER DHA
        0x0928: "न",  # DEVANAGARI LETTER NA
        0x092A: "प",  # DEVANAGARI LETTER PA
        0x092B: "फ",  # DEVANAGARI LETTER PHA
        0x092C: "ब",  # DEVANAGARI LETTER BA
        0x092D: "भ",  # DEVANAGARI LETTER BHA
        0x092E: "म",  # DEVANAGARI LETTER MA
        0x092F: "य",  # DEVANAGARI LETTER YA
        0x0930: "र",  # DEVANAGARI LETTER RA
        0x0932: "ल",  # DEVANAGARI LETTER LA
        0x0935: "व",  # DEVANAGARI LETTER VA
        0x0936: "श",  # DEVANAGARI LETTER SHA
        0x0937: "ष",  # DEVANAGARI LETTER SSA
        0x0938: "स",  # DEVANAGARI LETTER SA
        0x0939: "ह",  # DEVANAGARI LETTER HA
        
        # Numbers
        0x0966: "०",  # DEVANAGARI DIGIT ZERO
        0x0967: "१",  # DEVANAGARI DIGIT ONE
        0x0968: "२",  # DEVANAGARI DIGIT TWO
        0x0969: "३",  # DEVANAGARI DIGIT THREE
        0x096A: "४",  # DEVANAGARI DIGIT FOUR
        0x096B: "५",  # DEVANAGARI DIGIT FIVE
        0x096C: "६",  # DEVANAGARI DIGIT SIX
        0x096D: "७",  # DEVANAGARI DIGIT SEVEN
        0x096E: "८",  # DEVANAGARI DIGIT EIGHT
        0x096F: "९",  # DEVANAGARI DIGIT NINE
        
        # Basic Latin for testing
        0x0041: "A",
        0x0042: "B",
        0x0043: "C",
        0x0020: " ",  # Space
    }
    
    print("Creating Maithili characters...")
    
    for unicode_val, char_name in characters.items():
        # Create glyph
        glyph = font.createChar(unicode_val)
        glyph.glyphname = f"uni{unicode_val:04X}"
        
        # Create simple rectangular shape for testing
        # In real font, these would be proper character designs
        pen = glyph.glyphPen()
        
        if unicode_val == 0x0020:  # Space character
            glyph.width = 250
        else:
            # Simple rectangular placeholder
            pen.moveTo((50, 50))
            pen.lineTo((50, 650))
            pen.lineTo((450, 650))
            pen.lineTo((450, 50))
            pen.closePath()
            
            # Add a smaller internal rectangle to make it look like a character
            pen.moveTo((100, 100))
            pen.lineTo((100, 600))
            pen.lineTo((400, 600))
            pen.lineTo((400, 100))
            pen.closePath()
            
            glyph.width = 500
        
        print(f"Created: {char_name} (U+{unicode_val:04X})")
    
    return font

def generate_font_files():
    """Generate TTF files"""
    
    print("\n🎨 Creating Maithili Test Font...")
    
    # Create the font
    font = create_maithili_font()
    
    # Output directory
    output_dir = "/Users/vikramkumar/Desktop/Google fonts project/fonts/ofl/maithili"
    
    # Generate TTF file
    ttf_path = os.path.join(output_dir, "MaithiliTest-Regular.ttf")
    font.generate(ttf_path)
    print(f"\n✅ Generated: {ttf_path}")
    
    # Also create a bold version (same design, just different name)
    font.fontname = "MaithiliTestBold"
    font.familyname = "Maithili Test"
    font.fullname = "Maithili Test Bold"
    font.weight = "Bold"
    
    ttf_bold_path = os.path.join(output_dir, "MaithiliTest-Bold.ttf")
    font.generate(ttf_bold_path)
    print(f"✅ Generated: {ttf_bold_path}")
    
    font.close()
    print("\n🎉 Font generation complete!")
    
    return ttf_path, ttf_bold_path

if __name__ == "__main__":
    try:
        regular_path, bold_path = generate_font_files()
        print(f"\n📁 Font files created:")
        print(f"   Regular: {regular_path}")
        print(f"   Bold: {bold_path}")
        print(f"\n🧪 Test these fonts with Maithili text:")
        print(f"   मैथिली भाषा")
        print(f"   अआइईउऊएऐओऔ")
        print(f"   कखगघङचछजझञ")
        print(f"   ०१२३४५६७८९")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure FontForge is properly installed.")
