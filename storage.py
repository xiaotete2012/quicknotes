import json
import os
from pathlib import Path
from datetime import datetime

def get_data_path():
    """获取数据文件路径"""
    home = Path.home()
    data_dir = home / ".quicknotes"
    data_dir.mkdir(exist_ok=True)
    return data_dir / "notes.json"

def load_notes():
    """加载所有笔记"""
    data_file = get_data_path()
    if not data_file.exists():
        return {"notes": []}
    with open(data_file, "r") as f:
        return json.load(f)

def save_notes(data):
    """保存笔记到文件"""
    with open(get_data_path(), "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def add_note(content, tag=None):
    """添加新笔记"""
    data = load_notes()
    data["notes"].append({
        "id": len(data["notes"]) + 1,
        "content": content,
        "tag": tag,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    save_notes(data)

def list_notes():
    """列出所有笔记"""
    data = load_notes()
    for note in data["notes"]:
        print(
            f"{note['id']}. [{note.get('tag', '')}] {note['content']} "
            f"(创建于 {note['created_at']})"
        )

def delete_note(note_id):
    """删除笔记"""
    data = load_notes()
    data["notes"] = [n for n in data["notes"] if n["id"] != note_id]
    save_notes(data)

def search_notes(keyword):
    """搜索笔记"""
    data = load_notes()
    results = [
        n for n in data["notes"]
        if keyword.lower() in n["content"].lower()
    ]
    for note in results:
        print(f"{note['id']}. {note['content']}")
