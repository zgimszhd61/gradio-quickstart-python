import os
import gradio as gr

def fetch_token(input):
    # 从环境变量获取 token
    token = os.getenv('AAAA_TOKEN', 'Token not found')
    return token

def main():
    # 创建 Gradio 接口
    interface = gr.Interface(
        fn=fetch_token,
        inputs="text",
        outputs="text",
        title="Display Environment Token",
        description="This app fetches and displays the token stored in an environment variable named 'AAAA_TOKEN'."
    )
    interface.launch()

if __name__ == "__main__":
    main()


