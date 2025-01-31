# markdown_to_html_converter

このプロジェクトでは、Markdown ファイルを HTML に変換するためのスクリプト **`file_converter.py`** を提供しています。

---

## 使い方

```bash
python3 file_converter.py markdown input.md output.html
```

- **input.md** : 変換したい Markdown ファイル  
- **output.html** : 変換後の HTML ファイル

---

## 必要環境

- Python 3.6 以上
- [python-markdown](https://pypi.org/project/Markdown/)  
  ```bash
  pip install markdown
  ```
  上記コマンドでインストール可能です。

---

## 実行例

```bash
python3 file_converter.py markdown sample.md sample.html
```
`sample.html` が生成され、ブラウザで開くと Markdown が HTML に変換されています。

---

## ファイル構成

```
markdown_to_html_project/
├── file_converter.py
├── sample.md
└── README.md  ← このファイル
```
