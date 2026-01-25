import json
import os
import argparse
import re

def slugify(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    text = text.strip('-')
    return text

def main():
    parser = argparse.ArgumentParser(description='Batch generate social media content structure.')
    parser.add_argument('--schedule', required=True, help='Path to the schedule JSON file')
    args = parser.parse_args()

    if not os.path.exists(args.schedule):
        print(f"Error: Schedule file not found: {args.schedule}")
        return

    with open(args.schedule, 'r', encoding='utf-8') as f:
        data = json.load(f)

    tenant_id = data.get('tenant_id')
    week = data.get('week')
    posts = data.get('posts', [])

    base_output = os.path.join('.agent', 'skills', 'social-media-manager', 'output', tenant_id, week)
    
    print(f"Processing {len(posts)} posts for {tenant_id} - {week}...")

    for i, post in enumerate(posts):
        topic = post.get('topic', f'post-{i+1}')
        slug = slugify(topic)
        post_dir = os.path.join(base_output, slug)
        
        # Create directory
        os.makedirs(post_dir, exist_ok=True)
        print(f"Created: {post_dir}")

        # Create caption.txt
        content = post.get('content_plan', {})
        caption = content.get('caption_draft', '')
        title = content.get('title', '')
        visual_prompt = content.get('visual_prompt', '')
        
        caption_file = os.path.join(post_dir, 'caption.txt')
        with open(caption_file, 'w', encoding='utf-8') as f:
            f.write(f"TITLE: {title}\n\n")
            f.write(f"CAPTION:\n{caption}\n\n")
            f.write(f"VISUAL PROMPT:\n{visual_prompt}\n")
        
        print(f" - Saved caption.txt")

    print("Batch generation of structure completed.")
    print(f"Output location: {base_output}")

if __name__ == "__main__":
    main()
