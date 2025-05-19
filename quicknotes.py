import argparse
from datetime import datetime
from storage import add_note, list_notes, delete_note, search_notes

def main():
    # 初始化命令行解析器
    parser = argparse.ArgumentParser(description="QuickNotes - 命令行笔记工具")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # 子命令：add
    parser_add = subparsers.add_parser("add", help="添加笔记")
    parser_add.add_argument("content", help="笔记内容")
    parser_add.add_argument("--tag", help="分类标签")

    # 子命令：list
    parser_list = subparsers.add_parser("list", help="列出所有笔记")

    # 子命令：delete
    parser_delete = subparsers.add_parser("delete", help="删除笔记")
    parser_delete.add_argument("note_id", type=int, help="要删除的笔记ID")

    # 子命令：search
    parser_search = subparsers.add_parser("search", help="搜索笔记")
    parser_search.add_argument("keyword", help="搜索关键词")

    args = parser.parse_args()

    # 执行对应操作
    if args.command == "add":
        add_note(args.content, args.tag)
        print(f"[OK] 笔记已添加")
    elif args.command == "list":
        list_notes()
    elif args.command == "delete":
        delete_note(args.note_id)
        print(f"[OK] 笔记 {args.note_id} 已删除")
    elif args.command == "search":
        search_notes(args.keyword)

if __name__ == "__main__":
    main()
