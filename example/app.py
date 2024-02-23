# !pip install gradio
import gradio as gr

# 这是我们的 "Hello World" 函数，它接受一个字符串参数并返回一个新的字符串
def greet(name):
    return "Hello, " + name + "!"

# 创建一个 Gradio 接口，指定输入和输出的类型，以及要调用的函数
iface = gr.Interface(fn=greet, inputs="text", outputs="text")

# 启动应用，这将在本地启动一个服务器，并在默认的web浏览器中打开一个新的标签页
iface.launch(share=True)