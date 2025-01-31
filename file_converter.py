#!/usr/bin/env python3
import sys
import markdown

def convert_markdown_to_html(input_file, output_file):
    # 1. Markdownファイルを読み込む
    with open(input_file, 'r', encoding='utf-8') as f_in:
        md_text = f_in.read()

    # 2. Markdown -> HTML に変換
    html_text = markdown.markdown(md_text)

    # 3. HTMLを出力ファイルへ書き込む
    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(html_text)

def main():
    # コマンドライン引数を取得
    args = sys.argv
    if len(args) < 4:
        print("Usage: python3 file_converter.py markdown <input.md> <output.html>")
        sys.exit(1)
    
    command = args[1]
    input_file = args[2]
    output_file = args[3]

    # markdownコマンドの場合にMarkdown->HTML変換
    if command == "markdown":
        convert_markdown_to_html(input_file, output_file)
        print(f"Converted '{input_file}' to '{output_file}' as HTML.")
    else:
        print(f"Unknown command: {command}")
        sys.exit(1)

if __name__ == "__main__":
    main()
