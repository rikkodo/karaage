# keras on osx

## ref

https://keimina.hatenablog.jp/entry/2019/12/27/001723
https://qiita.com/lindq_yu/items/0f7543bc1d426cb36f31

## 仮想環境

### 入手

```sh
brew install pyenv
# brew install pipenv  # うまく動かない(Lockに失敗するので諦めてvenvを用いる)
```

### セットアップ

```sh
# pyenv install X.X.X
# pyenv shell X.X.X  # 本来つけるべき
python -m venv ${VENV}
```

### 起動

```sh
. ${VENV}/bin/activate

PATH="${PWD}/env/bin:${PATH}"  # PATH通しておく (pyenvと仲が悪いかもしれない)
export KERAS_BACKEND=plaidml.keras.backend  # keras backend を設定しておく
```

### 終了

```sh
deactivate
```

## keras

### 入手

```sh
pip install plaidml-keras
${VENV}/bin/plaidml-setup
# experimental device -> y
# default device -> metal, radeon
# Save Settings -> y
```

### import

```python
# import os
# os.environ["KERAS_BACKEND"] = "plaidml.keras.backend"  # 環境変数で設定していない場合
import keras
```

## jupyter

### 入手

```sh
pip install notebook
```

### 起動

```sh
${VENV}/bin/jupyter notebook
```
