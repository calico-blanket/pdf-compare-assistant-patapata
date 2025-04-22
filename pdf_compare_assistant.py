"""
PDF比較アシスタント (PDF Compare Assistant)
Adobe Acrobatで開いた複数のPDFタブを自動的に切り替えて比較確認を効率化するツール
"""

from tkinter import messagebox
import pyautogui
import pygetwindow as gw
import keyboard
import time

def switch_tabs_in_adobe(switch_interval=0.5):
    """
    Adobe Acrobatで開いたPDFタブを切り替えながら比較確認を行う
    
    Args:
        switch_interval (float): タブ切り替えの間隔（秒）
    """
    try:
        # Adobe Acrobatのウィンドウを取得
        acrobat_windows = gw.getWindowsWithTitle('Adobe Acrobat')
        # 別のPDFビューアを使用する場合は以下の行のコメントを外して編集してください
        # acrobat_windows = gw.getWindowsWithTitle('PDF-XChange Viewer')
        
        # PDFビューアが開かれていなかったらメッセージを出して終了
        if len(acrobat_windows) == 0:
            messagebox.showinfo("PDF表示の確認", "PDFが開いていません。終了します。")
            return

        # 確認ダイアログを表示
        start_review = messagebox.askyesno(
            "あおり検版の開始", 
            "あおり検版を開始します。\n\n開始後に、中止/終了するにはEscキーを約5秒間長押ししてください。\n停止信号検知後、実際の停止までに数秒かかることがあります。"
        )
        
        if not start_review:
            messagebox.showinfo("キャンセルのお知らせ", "あおり検版がキャンセルされました。")
            return

        # メイン処理ループ
        while True:
            # Adobe Acrobatのウィンドウをアクティブにする
            acrobat_windows[0].activate()
            
            # 左右のPDFを3回交互に切り替え
            for _ in range(3):
                # PDF左のページを表示
                pyautogui.hotkey('ctrl', 'tab')  # タブを切り替え
                time.sleep(switch_interval)
                
                # PDF右のページを表示
                pyautogui.hotkey('ctrl', 'tab')  # タブを切り替え
                time.sleep(switch_interval)
            
            # PDFの左のページを表示
            pyautogui.hotkey('ctrl', 'tab')  # タブを切り替え
            time.sleep(0.0)
            
            # 左のページをめくる
            pyautogui.press('pagedown')
            time.sleep(0.0)
            
            # PDF右に切り替え
            pyautogui.hotkey('ctrl', 'tab')  # タブを切り替え
            time.sleep(0.0)
            
            # 右のページをめくる
            pyautogui.press('pagedown')
            time.sleep(0.0)
            
            # Escキーが長押しされたらループを終了
            if keyboard.is_pressed('esc'):
                print("Escキーが長押しされたため、あおり検版を停止します。")
                messagebox.showinfo("処理の終了", "あおり検版を終了します。\n（Escキー検知から停止まで数秒かかることがあります）")
                break

    except Exception as e:
        # エラー発生時のメッセージ
        print(f"エラーが発生しました: {e}")
        messagebox.showinfo("エラー", f"処理中にエラーが発生しました: {e}")
    except KeyboardInterrupt:
        # 処理の中断時のメッセージ
        messagebox.showinfo("処理の終了", "あおり検版を終了します。")

if __name__ == "__main__":
    # デフォルトの切り替え間隔（秒）で実行
    switch_tabs_in_adobe(0.5)