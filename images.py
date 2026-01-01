#!/usr/bin/env python3
"""
Generate images from prompts in images.md using OpenAI's DALL-E API.
Requires: OPENAI_API_KEY environment variable
"""

import os
import re
import requests
import time
from pathlib import Path

def get_openai_api_key():
    """Get API key from environment."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable not set")
    return api_key

def parse_prompts(filepath: str) -> list[dict]:
    """Parse images.md and extract numbered prompts."""
    with open(filepath, "r") as f:
        content = f.read()

    # Pattern to match sections like "## 1. Title Name" followed by **Prompt:** content
    pattern = r'## (\d+)\. ([^\n]+)\n\n\*\*Prompt:\*\* (.+?)(?=\n\n---|\n## Usage Notes|\Z)'
    matches = re.findall(pattern, content, re.DOTALL)

    prompts = []
    for num, title, prompt_text in matches:
        # Clean up the prompt text
        prompt_text = prompt_text.strip()
        # Create a safe filename from the title
        safe_title = re.sub(r'[^\w\s-]', '', title).strip().lower()
        safe_title = re.sub(r'[\s]+', '-', safe_title)
        filename = f"{num.zfill(2)}-{safe_title}.png"

        prompts.append({
            "number": int(num),
            "title": title,
            "prompt": prompt_text,
            "filename": filename
        })

    return prompts

def generate_image(api_key: str, prompt: str) -> bytes:
    """Call OpenAI API to generate image, return the image bytes."""
    import base64

    url = "https://api.openai.com/v1/images/generations"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # Truncate prompt if too long
    if len(prompt) > 32000:
        prompt = prompt[:31997] + "..."

    data = {
        "model": "gpt-image-1.5",
        "prompt": prompt,
        "n": 1,
        "size": "1536x1024",  # Landscape for diagrams/infographics
        "quality": "high"
    }

    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()

    result = response.json()

    # Handle both URL and base64 responses
    image_data = result["data"][0]
    if "b64_json" in image_data:
        return base64.b64decode(image_data["b64_json"])
    elif "url" in image_data:
        # Download image from URL
        img_response = requests.get(image_data["url"])
        img_response.raise_for_status()
        return img_response.content
    else:
        raise ValueError(f"Unexpected response format: {image_data.keys()}")

def save_image(image_bytes: bytes, filepath: str):
    """Save image bytes to file."""
    with open(filepath, "wb") as f:
        f.write(image_bytes)

def main():
    # Get API key
    api_key = get_openai_api_key()

    # Parse prompts from images.md
    script_dir = Path(__file__).parent
    prompts_file = script_dir / "images.md"

    if not prompts_file.exists():
        raise FileNotFoundError(f"Could not find {prompts_file}")

    prompts = parse_prompts(str(prompts_file))
    print(f"Found {len(prompts)} prompts to generate\n")

    # Create images directory
    output_dir = script_dir / "images"
    output_dir.mkdir(exist_ok=True)

    # Generate each image
    for i, item in enumerate(prompts):
        print(f"[{i+1}/{len(prompts)}] Generating: {item['title']}")

        output_path = output_dir / item["filename"]

        # Skip if already exists
        if output_path.exists():
            print(f"  Skipping (already exists): {item['filename']}")
            continue

        try:
            # Generate image
            image_bytes = generate_image(api_key, item["prompt"])
            print(f"  Generated, saving...")

            # Save to file
            save_image(image_bytes, str(output_path))
            print(f"  Saved: {item['filename']}")

            # Rate limiting - be nice to the API
            if i < len(prompts) - 1:
                print("  Waiting 12s (rate limit)...")
                time.sleep(12)

        except requests.exceptions.HTTPError as e:
            print(f"  ERROR: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"  Response: {e.response.text}")
            continue
        except Exception as e:
            print(f"  ERROR: {e}")
            continue

    print(f"\nDone! Images saved to: {output_dir}")

if __name__ == "__main__":
    main()
