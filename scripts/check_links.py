"""Kiểm link nội bộ và anchor trong các file markdown của repo.

Chạy: python scripts/check_links.py
Thoát mã 1 nếu có link trỏ tới file không tồn tại hoặc anchor không có.
Anchor được tạo theo kiểu GitHub: chữ thường, giữ dấu tiếng Việt, bỏ ký tự đặc biệt, khoảng trắng thành "-".
Link ngoài (http/https) do lychee kiểm trong CI.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP_DIRS = {".git", "node_modules", "local"}

CODE_BLOCK = re.compile(r"^(```|~~~).*?^\1", re.S | re.M)
INLINE_CODE = re.compile(r"`[^`\n]*`")
HEADING = re.compile(r"^#{1,6} +(.*?) *#*$", re.M)
LINK = re.compile(r"\]\(([^)\s]+)(?: \"[^\"]*\")?\)")


def slug(text: str) -> str:
    text = re.sub(r"`|\*\*|__", "", text).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text, flags=re.U)
    return text.replace(" ", "-")


def strip_code(text: str) -> str:
    return INLINE_CODE.sub("", CODE_BLOCK.sub("", text))


def markdown_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                yield os.path.normpath(os.path.join(dirpath, name))


def anchors_of(path: str, cache: dict) -> set:
    if path not in cache:
        with open(path, encoding="utf-8") as f:
            text = CODE_BLOCK.sub("", f.read())
        seen, result = {}, set()
        for heading in HEADING.findall(text):
            base = slug(heading)
            n = seen.get(base, 0)
            result.add(base if n == 0 else f"{base}-{n}")
            seen[base] = n + 1
        cache[path] = result
    return cache[path]


def main() -> int:
    cache, errors = {}, []
    for path in markdown_files():
        with open(path, encoding="utf-8") as f:
            text = strip_code(f.read())
        for target in LINK.findall(text):
            if re.match(r"^[a-z]+:", target) or target.startswith("<"):
                continue
            file_part, _, anchor = target.partition("#")
            dest = os.path.normpath(os.path.join(os.path.dirname(path), file_part)) if file_part else path
            rel = os.path.relpath(path, ROOT)
            if not os.path.exists(dest):
                errors.append(f"{rel}: không có file {target}")
            elif anchor and dest.endswith(".md") and anchor not in anchors_of(dest, cache):
                errors.append(f"{rel}: không có anchor {target}")
    for e in errors:
        print(e)
    print(f"{len(errors)} lỗi link nội bộ")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
