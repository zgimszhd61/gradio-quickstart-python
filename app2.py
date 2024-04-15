import gradio as gr

def process_text_and_number(text, number):
    processed_text = f"输入的文本是: {text}"
    processed_number = number * 10
    return processed_text, processed_number

app = gr.Interface(
    fn=process_text_and_number,
    inputs=[
        gr.components.Textbox(lines=2, placeholder="请输入一些文本..."), 
        gr.components.Slider(minimum=1, maximum=100)
    ],
    outputs=[
        gr.components.Textbox(), 
        gr.components.Number(label="处理后的数字")
    ],
    title="文本和数字处理",
    description="这是一个简单的应用，用于展示如何处理文本和数字输入，并显示输出。"
)

app.launch()
