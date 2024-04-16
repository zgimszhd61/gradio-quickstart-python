import gradio as gr

def process_file(uploaded_file, input_text):
    # 这里我们仅仅返回文件的名字和用户输入的文本作为示例
    return f"Received file: {uploaded_file.name}\nReceived text: {input_text}"

def main():
    # 创建一个文件输入界面
    file_input = gr.File(label="Upload your file")
    # 创建一个文本输入框
    text_input = gr.Textbox(label="Enter your text")
    
    # 创建一个输出界面，这里用Text表示输出文本
    output_component = gr.Textbox(label="Result")
    
    # 定义界面，连接输入、处理函数和输出
    interface = gr.Interface(fn=process_file,
                             inputs=[file_input, text_input],
                             outputs=output_component,
                             title="File and Text Upload Example",
                             description="Upload a file and enter some text to see both processed.")
    
    # 启动应用
    interface.launch()

if __name__ == "__main__":
    main()

