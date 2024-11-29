# Visual Studio CodeとPythonのセットアップ手順

## A. VSCodeのインストールと日本語化

### 1. Visual Studio Code (VSCode) のインストール

1. [VSCode のダウンロードページ](https://code.visualstudio.com/)にアクセスします。
   <img src="./images/download_vscode.png" style="zoom:50%;" />

2. "Download for Windows"（もしくは使用している OS に対応するボタン）をクリックし、インストーラをダウンロードします。

3. ダウンロードしたインストーラを実行し、指示に従ってインストールを進めます。

   ![](./images/install_vscode_1.png)

   ![install_vscode_2](./images/install_vscode_2.png)

   ![install_vscode_3](./images/install_vscode_3.png)

4. インストールが完了したら、VSCode を起動します。

### 2. VSCode のユーザーインターフェースを日本語化

1. VSCode を起動したら、左側の拡張機能アイコン（四角形が組み合わさったようなマーク）をクリックします。

   <img src="./images/vscode_1_open_folder.png" style="zoom: 67%;" />

2. 検索ボックスに「Japanese Language Pack」と入力し、Microsoft の **Japanese Language Pack for Visual Studio Code** をインストールします。

   <img src="./images/vscode_2_japanese_language_pack.png" style="zoom: 67%;" />

3. "Change Language and Restart"をクリックして、言語を日本語に切り替えます。インストールが完了すると、VSCode のインターフェースが日本語に変更されます。

   <img src="./images/vscode_2a_enable_japanese_language_pack.png" style="zoom:67%;" />

## B. Pythonインストール + VSCode連携の設定

### 1. Python のインストール

1. [Python の公式サイト](https://www.python.org/downloads/)にアクセスします。

   <img src="./images/download_python.png" style="zoom:50%;" />

2. "Download Python" ボタンをクリックして最新バージョンをダウンロードします。

3. インストーラを実行し、"Add Python to PATH" にチェックを入れてから "Install Now" をクリックします。

   ![](./images/install_python.png)

4. インストールが完了したら、Macの場合は「ターミナル」アプリ、Windowsの場合は"PowerShell"を立ち上げて、 "python --version" と入力してエンターキーを押します。3.13 のようなバージョン番号が表示されていれば、インストールは成功です。

### 2. VSCode で Python 環境の設定

1. VSCode を起動したら、左側の拡張機能アイコン（四角形が組み合わさったようなマーク）をクリックします。

2. 検索ボックスに「Python」と入力し、Microsoft の **Python 拡張機能** をインストールします。

   <img src="./images/vscode_3_python_plugin.png" style="zoom:67%;" />

# C. 動作確認

### 1. 簡単な Python スクリプトの実行

1. VSCode で「新しいファイル」をメニューから選びます。

   <img src="./images/vscode_4_new_file.png" style="zoom:67%;" />

2. ファイルの種類として「Pythonファイル」を選択します。

   <img src="./images/vscode_5_new_python_file.png" style="zoom:67%;" />

3. 以下のコードを入力します：

   ```python
   print("こんにちは!")
   ```

   

   <img src="./images/vscode_6_python_code.png" style="zoom:67%;" />

4. ファイルを保存します (場所はどこでも大丈夫ですが、デスクトップなどわかりやすい場所がおすすめです)。

   <img src="./images/vscode_7_save_python_file.png" style="zoom:67%;" />

5. 右上の再生ボタンをクリックしてコードを実行します。

   <img src="./images/vscode_8_run_python_code.png" style="zoom:67%;" />

6. 実行結果のウィンドウに「こんにちは!」と表示されることを確認します。

   <img src="./images/vscode_9_python_code_output.png" style="zoom:67%;" />

### 2. トラブルシューティング

- Python が見つからないと表示された場合、Python のインストールパスが正しく設定されていることを確認してください。
- VSCode のターミナルが動作しない場合、拡張機能が正しくインストールされているか確認してください。

### 3. おすすめの追加拡張機能

- **Pylance**: 途中まで書くと、残りを補完してくれる拡張機能。
- **Pylint**: 間違いがないか、自動でチェックしてくれる拡張機能。
