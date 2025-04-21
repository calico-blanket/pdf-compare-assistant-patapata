# pdf-compare-assistant-patapata
A verification tool that automatically "flips" (Patapata) between PDF tabs for efficient comparison./PDFを「パタパタ」と自動でめくりながら比較する検版支援ツール。

# PDF Compare Assistant "Patapata"

A tool to automate PDF comparison verification process by automatically switching between multiple PDF tabs opened in Adobe Acrobat.

## About the Name "Patapata"

"Patapata" is an onomatopoeic Japanese word that mimics the sound of flipping pages or rapidly switching between documents. In the Japanese publishing and printing industry, the process of comparing documents by quickly switching between them is affectionately known as "Patapata" (from the "aori-kenpan" verification method). This tool automates this "Patapata" process.

## Features

- Automatically switches between multiple PDF tabs open in Adobe Acrobat
- Alternately displays left and right PDFs for comparison
- Automatically flips pages after a set interval
- Operation can be stopped at any time with the Esc key

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

1. Open the two PDF files you want to compare in separate tabs in Adobe Acrobat
2. Run this script:

```bash
python pdf_compare_assistant.py
```

3. Click "Yes" on the confirmation dialog to start the comparison
4. Press and hold the Esc key to stop the process at any time

## Notes

- This tool is designed for use with PDF files opened in tabs in Adobe Acrobat
- It may work with other PDF viewers, but this has not been tested
- By editing the commented-out sections in the script, you can adapt it for other PDF viewers (e.g., PDF-XChange Viewer)

## Customization

You can customize the behavior by editing the following parts of the script:

- Change the value of `time.sleep(0.5)` to adjust the interval between tab switches
- Change the window title to be activated to adapt to other PDF viewers

## License

[MIT License](LICENSE)


## Author  

calico_blanket  

## Note from the Author  

I am not a professional developer or software engineer, just a middle-aged woman who is an IT enthusiast.
This tool was created as a personal project with significant help from Claude's Sonnet 3.5 and 3.7.
If you provide feedback, bug reports, or suggestions, I will sincerely work on improvements with the help of Sonnet and knowledgeable community members.
I would appreciate your cooperation in my learning and growth.

---

*This tool was created to improve the efficiency of document comparison. It does not guarantee the quality of the verification process itself.*
