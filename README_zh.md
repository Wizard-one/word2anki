在 [Make_Anki_Package](https://github.com/tongfeima/Make_Anki_Package) 启发下制作的 Anki 卡片生成器。 

从文本文件中读取陌生的单词批量生成 Anki 卡片


# Preview

正面:

![正面](doc/img/front.png)

背面:

![背面](doc/img/back.png)


# Usage

在python环境中安装包
```python
pip install .
```

将陌生单词按行放到 `wordlist.txt` 中

命令行运行

```
python demo.py
```

在目录中会生成 `*.apkg` 文件, 使用 Anki 打开-导入

默认卡组名称为 English

# TODO

- 打包成可执行文件


# Reference

- [Anki document](https://docs.ankiweb.net/templates/fields.html#field-references)
- [百词斩API](https://github.com/lyc8503/baicizhan-word-meaning-API)
- [GenAnki](https://github.com/kerrickstaley/genanki)
- [FreeDictionaryAPI](https://github.com/meetDeveloper/freeDictionaryAPI)

# Copyright & license

