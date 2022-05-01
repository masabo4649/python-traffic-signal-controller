# GPIOリモートコントローラー

- Raspberry PIのGPIOをWebブラウザ等からRESTで操作できるようにする。
- サーバー側に信号機の制御器のような自動制御の仕組みを組み込める
- GPIOがないマシンでもシミュレータで操作させることができる

## Getting Started

- Raspberry PIで、予め必要なpythonライブラリをインストールしておく。
  ```sh
  sudo apt-get install python3-numpy
  sudo apt-get install python3-imaging
  sudo apt-get install python3-pandas
  sudo apt-get install python3-matplotlib
  sudo apt-get install libopencv-dev
  sudo apt-get install python3-opencv
  sudo apt-get install libportaudio2
  ```

- ライブラリをインストールする
  ```sh
  python -m pip install -r requirement.txt
  ```
- `config.properties`でMockモードを設定する。GPIOが使えない環境で起動する場合、`True`にする必要がある。
  ```properties
  [mode]
  mock = True
  ```
- コントローラー単体で起動する場合
  ```sh
  python controller.py
  ```

- HTTPサーバーを起動する場合。`--reload`をつけた場合、ファイルを更新すると自動的に読み込むため、開発が容易になる。
  ```sh
  uvicorn main:app --reload
  ```
- Raspberry PIで動かす場合、他の端末からリクエストを受けられるように`--host`を設定する。
  ```sh
  uvicorn main:app --host 0.0.0.0
  ```


## 使用しているライブラリ、構成など
Raspberry PI Zeroに、REST APIを受けるサーバーを構成している。RESTで受けたリクエストによってGPIOの入出力を実行している。クライアント側はSPAのページからRESTリクエストを投げて、ボタン押下などのステータスの更新や、サーバー側で動いたステータスの同期をしている。

### Webクライアント側
- [Bootstrap v4 + jQuery](https://getbootstrap.com/docs/4.6/getting-started/introduction/) - ページのテンプレート
- [iOS Style Switches For Bootstrap 4 – Custom Switch](https://www.cssscript.com/ios-style-switches-bootstrap-4/)

### サーバー側
- Python 3.7.3
- [FastAPI](https://fastapi.tiangolo.com/) - PythonでRESTを実装
- [gpiozero](https://gpiozero.readthedocs.io/en/stable/index.html) - Raspberry PIのGPIOを操作するライブラリ
- [tkgpio](https://github.com/wallysalami/tkgpio) - gpiozeroをMock化してUIでシミュ-レートしてくれるツール


## 参考リンク
- [ラズパイ（Raspberry Pi）のGPIOを再確認！　まずは汎用入出力からマスターしよう](https://deviceplus.jp/raspberrypi/raspberrypi-gpio/)
- [RasPi＋FastAPIを使う](https://qiita.com/dev_greentea/items/3d3d34b26d14e22ab76d)
- [M1版とIntel版のHomebrewを併用するときpyenvがうまく動かない問題を解決する](https://qiita.com/tomtsutom0122/items/52487730001247fdc2c5)
