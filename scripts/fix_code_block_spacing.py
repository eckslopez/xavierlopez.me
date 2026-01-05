#!/usr/bin/env python3
"""
Add blank lines before and after code blocks in markdown files.
"""

from pathlib import Path


def fix_code_block_spacing(content):
    """Add blank lines before and after code blocks."""
    lines = content.split('\n')
    result = []
    in_frontmatter = False
    frontmatter_count = 0
    in_code_block = False

    for i, line in enumerate(lines):
        # Track YAML front matter
        if line.strip() == '---' and i < 30 and frontmatter_count < 2:
            frontmatter_count += 1
            if frontmatter_count == 1:
                in_frontmatter = True
            elif frontmatter_count == 2:
                in_frontmatter = False
            result.append(line)
            continue

        if in_frontmatter:
            result.append(line)
            continue

        # Check if current line is a code block marker
        is_code_marker = line.strip().startswith('```')

        if is_code_marker:
            if not in_code_block:
                # Opening code block - add blank line before if needed
                if result and result[-1].strip() != '':
                    result.append('')
                result.append(line)
                in_code_block = True
            else:
                # Closing code block
                result.append(line)
                # Add blank line after if needed
                if i + 1 < len(lines) and lines[i + 1].strip() != '':
                    result.append('')
                in_code_block = False
        else:
            result.append(line)

    return '\n'.join(result)


def process_posts():
    """Process all posts in _posts directory."""
    posts_dir = Path('_posts')

    if not posts_dir.exists():
        print(f"Directory {posts_dir} not found")
        return

    for post_file in sorted(posts_dir.glob('*.md')):
        print(f"Processing {post_file.name}...")

        with open(post_file, 'r', encoding='utf-8') as f:
            content = f.read()

        fixed_content = fix_code_block_spacing(content)

        if content != fixed_content:
            with open(post_file, 'w', encoding='utf-8') as f:
                f.write(fixed_content)
            print(f"  ✓ Updated {post_file.name}")
        else:
            print(f"  - No changes needed for {post_file.name}")


if __name__ == '__main__':
    process_posts()
