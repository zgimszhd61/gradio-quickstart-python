import gradio as gr

def process_file(uploaded_file):
    # 这里我们仅仅返回文件的名字作为示例
    return f"Received file: {uploaded_file.name}"

def main():
    # 创建一个文件输入界面
    file_input = gr.File(label="Upload your file")
    
    # 创建一个输出界面，这里用Text表示输出文本
    output_component = gr.Textbox(label="Result")
    
    # 定义界面，连接输入、处理函数和输出
    interface = gr.Interface(fn=process_file,
                             inputs=file_input,
                             outputs=output_component,
                             title="File Upload Example",
                             description="Upload a file and see its name.")
    
    # 启动应用
    interface.launch()

if __name__ == "__main__":
    main()

