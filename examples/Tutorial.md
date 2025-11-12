# 数据搜集格式

1. 图片放进文件夹

    每个图片都储存为.jpg，命名方式：代码类型_具体类型_id.jpg

    比如 matplotlib_bar_0001.jpg, latex_mathequation_0001.jpg

2. 储存成json

    json格式参考code_vqa_10.json（请仔细参照此文件的数据格式，该文件的图片命名不规范，请按照上面的方法进行图片命名）

    注意事项：json文件里面每个字典的id就是图片的名字；字典的"image"就是图片文件夹名称（文件夹名称为各自负责的数据类型，如matplotlib_images，latex_images）加图片名字（包括.jpg后缀）；字典的conversation是一问一答的格式，回答（python代码）要注意加上\```python\n 和 \n```

# GPT4的API使用

从官网和Github收集种子数据后（搜集完之后请先告知魏来），我们需要利用GPT4做数据扩充。请仔细阅读CodeLLaVA/datasets/gpt4.py。注意要修改和设计新的prompt（第十行的inputs），设计的prompt可以发给魏来看一下，以确保prompt的质量。GPT4生成的画图代码，以及画图代码画出的图片，请按照“数据搜集格式”的说明进行保存

至于GPT4-V（多模态GPT4）的使用，可以参考gpt4V_example.py