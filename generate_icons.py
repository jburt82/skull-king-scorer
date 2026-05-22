#!/usr/bin/env python3
"""
Generate app icons for Skull King Scorer PWA
Creates PNG icons at all required sizes for the manifest.json
"""

from PIL import Image, ImageDraw
import os

def create_skull_icon(size):
    """Create a skull icon at the specified size"""
    # Dark navy background
    img = Image.new('RGB', (size, size), color='#0a1628')
    draw = ImageDraw.Draw(img)

    center_x = size // 2
    center_y = size // 2

    # Scale proportions to size
    skull_radius = int(size * 0.30)
    jaw_radius = int(size * 0.22)
    eye_radius = int(size * 0.08)
    eye_offset_x = int(size * 0.12)
    eye_offset_y = int(size * 0.05)

    # Main skull (top)
    skull_top = center_y - int(size * 0.08)
    draw.ellipse(
        [center_x - skull_radius, skull_top - skull_radius,
         center_x + skull_radius, skull_top + skull_radius],
        fill='#c9a227'
    )

    # Jaw (bottom)
    jaw_top = center_y + int(size * 0.08)
    draw.ellipse(
        [center_x - jaw_radius, jaw_top - jaw_radius,
         center_x + jaw_radius, jaw_top + jaw_radius],
        fill='#c9a227'
    )

    # Left eye socket
    eye_left_x = center_x - eye_offset_x
    eye_top = skull_top - eye_offset_y
    draw.ellipse(
        [eye_left_x - eye_radius, eye_top - eye_radius,
         eye_left_x + eye_radius, eye_top + eye_radius],
        fill='#0a1628'
    )

    # Right eye socket
    eye_right_x = center_x + eye_offset_x
    draw.ellipse(
        [eye_right_x - eye_radius, eye_top - eye_radius,
         eye_right_x + eye_radius, eye_top + eye_radius],
        fill='#0a1628'
    )

    # Nose
    nose_size = int(size * 0.05)
    draw.ellipse(
        [center_x - nose_size, skull_top + int(size * 0.02) - nose_size,
         center_x + nose_size, skull_top + int(size * 0.02) + nose_size],
        fill='#0a1628'
    )

    return img

def main():
    """Generate icons for all required sizes"""
    # Required icon sizes from manifest.json
    sizes = [72, 96, 128, 144, 152, 192, 384, 512]

    # Create icons directory
    os.makedirs('icons', exist_ok=True)

    print("🏴‍☠️ Generating Skull King Scorer app icons...")
    print()

    for size in sizes:
        # Create icon
        icon = create_skull_icon(size)

        # Save icon
        filename = f'icons/icon-{size}x{size}.png'
        icon.save(filename)

        print(f"✓ Created {filename}")

    print()
    print("✅ All icons generated successfully!")
    print()
    print("Next steps:")
    print("1. Verify the icons folder contains 8 PNG files")
    print("2. Commit and deploy to Netlify, Vercel, or GitHub Pages")
    print("3. See DEPLOYMENT.md for detailed instructions")

if __name__ == '__main__':
    try:
        main()
    except ImportError:
        print("❌ Error: PIL (Pillow) is not installed")
        print()
        print("Install it with:")
        print("  pip install Pillow")
        print()
        print("Or use the online icon generator at:")
        print("  https://www.favicon-generator.org/")
