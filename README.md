
# PDF Compare Assistant "Patapata"

A verification tool that automatically "flips" (Patapata) between PDF tabs for efficient comparison./PDFを「パタパタ」と自動でめくりながら比較する検版支援ツール。

 [日本語](#japanese) |English
  
<a id="english"></a>

A tool to automate PDF comparison verification process by automatically switching between multiple PDF tabs opened in Adobe Acrobat.

## About the Name "Patapata"

"Patapata" is an onomatopoeic Japanese word that mimics the sound of flipping pages or rapidly switching between documents. In the Japanese publishing and printing industry, the process of comparing documents by quickly switching between them is affectionately known as "Patapata" (from the "aori-kenpan" verification method). This tool automates this "Patapata" process.

## Features

- Automatically switches between multiple PDF tabs open in Adobe Acrobat.
- Alternately displays left and right PDFs for comparison.
- Automatically flips pages after a set interval.
- Operation can be stopped at any time with the Esc key.

## Requirements

- Python 3.6 or higher
- The following Python packages:
  - pyautogui
  - pygetwindow
  - keyboard

## Installation

```bash
# Install required packages
pip install pyautogui pygetwindow keyboard
```

## How to Use

1. Open the two PDF files you want to compare in separate tabs in Adobe Acrobat.
2. Run this script:

   ```bash
   python pdf_compare_assistant.py
   ```  

3. Click "はい（Yes）" on the confirmation dialog to start the comparison.  
4. To stop the process in the middle, press and hold the Esc key for about 2 seconds.
   **Note:** There will be a delay of several seconds between when you hold down the key and when the operation actually stops, during which several more pages may be processed.

## Compatible PDF Viewers

- This tool is designed for use with PDF files opened in tabs in Adobe Acrobat.
- It may work with other PDF viewers, but this has not been tested.
- If you want to try it with other PDF viewers (e.g., PDF-XChange Viewer), edit the commented-out section in the script as shown below:

 try:

 ```Python
        # Adobe Acrobatのウィンドウを取得
        acrobat_windows = gw.getWindowsWithTitle('Adobe Acrobat')
        # 別のPDFビューアを使用する場合は以下の行のコメントを外して編集してください。
        # acrobat_windows = gw.getWindowsWithTitle('PDF-XChange Viewer')
 ```

## Notes

- This tool is designed for use with PDF files opened in tabs in Adobe Acrobat.
- It may work with other PDF viewers, but this has not been tested.
- By editing the commented-out sections in the script, you can adapt it for other PDF viewers (e.g., PDF-XChange Viewer).

## Customization

You can customize the behavior by editing the following parts of the script:

- Change the value of `time.sleep(0.5)` to adjust the interval between tab switches.
- Change the window title to be activated to adapt to other PDF viewers.

## License

[MIT License](LICENSE)

## Author  

calico_blanket  

## Note from the Author  

I am not a professional developer or software engineer, just a middle-aged woman who is an IT enthusiast.
This tool was created as a personal project with significant help from Claude's Sonnet 3.5 and 3.7.
If you provide feedback, bug reports, or suggestions, I will sincerely work on improvements with the help of Sonnet and knowledgeable community members.
I would appreciate your cooperation in my learning and growth

---

*This tool was created to improve the efficiency of document comparison. It does not guarantee the quality of the verification process itself.*

 日本語| [English](#english)  

<a id="japanese"></a>

# PDF比較アシスタント「パタパタ」(PDF Compare Assistant "Patapata")

PDFの比較確認（あおり検版）を自動化するためのツールです。Adobe Acrobatで開いた複数のPDFタブを自動的に切り替えながら比較確認作業を効率化します。

「パタパタ」(Patapata)という名前は、日本の出版・印刷業界で使われる「あおり検版」の通称です。複数のPDFページをパタパタと素早く切り替えて比較することから、このような愛称で呼ばれています。このツールはそのパタパタという作業を自動化します。

## 機能

- Adobe Acrobatで開いた複数のPDFタブを自動的に切り替え
- 左右のPDFを交互に表示
- 一定時間後に自動でページ送り
- Escキーの長押し（約2秒間）で操作を中止可能

## 必要条件

- Python 3.6以上
- 以下のPythonパッケージ:
  - pyautogui
  - pygetwindow
  - keyboard

## インストール方法

```bash
# 必要なパッケージのインストール
pip install pyautogui pygetwindow keyboard
```

## 使用方法

1. Adobe Acrobatで比較したい2つのPDFファイルを別々のタブで開きます。
2. このスクリプトを実行します。:

   ```bash
   python pdf_compare_assistant.py
   ```

3. 確認ダイアログが表示されたら「はい」をクリックして比較を開始します。
4. 途中で中止したい場合はEscキーを2秒間程度長押しします。ただし、長押ししてから実際に動作が停止するまでに数秒かかり、その間にさらに数ページが処理される場合があります。

## 対象PDFビューワー

- このツールはAdobe Acrobatでタブ表示されているPDFファイルでの使用を想定しています。
- 他のPDFビューワーでも動作する可能性がありますが、テストは行っていません。
- 他のPDFビューワー（例：PDF-XChange Viewer）で試してみる場合は、スクリプト内のコメントアウトされた部分（下記）を編集してください。

```Python
try:
        # Adobe Acrobatのウィンドウを取得
        acrobat_windows = gw.getWindowsWithTitle('Adobe Acrobat')
        # 別のPDFビューアを使用する場合は以下の行のコメントを外して編集してください。
        # acrobat_windows = gw.getWindowsWithTitle('PDF-XChange Viewer')
 ```

## カスタマイズ

スクリプト内の以下の部分を編集することで、動作をカスタマイズできます:

- `time.sleep(0.5)` の値を変更すると、タブ切り替えの間隔を調整できます。
- アクティブにするウィンドウのタイトルを変更することで、他のPDFビューアにも対応できます。

## ライセンス

[MITライセンス](LICENSE)

### 貢献

貢献は歓迎します！Issue報告や改善のためのプルリクエストをお待ちしています。

## 作者

calico_blanket (猫柄毛布）
<https://x.com/calico_blanket>

## 作者から

私はプロのデベロッパーやソフトエンジニアではなく、単なる、おばちゃんのIT愛好家にすぎません。
このツールは個人的なプロジェクトとして、ClaudeのSonnet3.7の助けを大きく借りて作成しました。
フィードバック、バグ報告、および提案などをいただきましたら、Sonnetと有識者の皆様のお知恵をお借りして、真摯に改善に取り組みたいと思います。
私の学びと成長ににご協力いただけると幸いです。

---

*このツールは検版作業の効率化のために作成されました。実際の検版作業の品質保証を保証するものではありません。*
