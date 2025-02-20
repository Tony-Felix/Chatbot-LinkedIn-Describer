import google.generativeai as genai
import os
import time
import gradio as gr
from google.api_core.exceptions import InvalidArgument


genai.configure(api_key=os.environ["GEMINI_API"])

initial_prompt = (
    "Você é um assistente virtual que pode receber e processar arquivos de "
    "vários tipos, como imagens, áudios, e textos. "
    "Ao receber um arquivo, você deve analisá-lo e cria uma descrição de um "
    "post para o linkedin"
)

model = genai.GenerativeModel(
    "gemini-1.5-flash", system_instruction=initial_prompt
)

chat = model.start_chat()


def assemble_prompt(message):
    prompt = [message["text"]]
    uploaded_files = upload_files(message)
    prompt.extend(uploaded_files)
    return prompt


def upload_files(message):
    uploaded_files = []
    if message["files"]:
        for file_gradio_data in message["files"]:
            uploaded_file = genai.upload_file(file_gradio_data["path"])
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(5)
                uploaded_file = genai.get_file(uploaded_file.name)
            uploaded_files.append(uploaded_file)
    return uploaded_files


def gradio_wrapper(message, _history):
    prompt = assemble_prompt(message)
    try:
        response = chat.send_message(prompt)
    except InvalidArgument as e:
        response = chat.send_message(
            "Quando você receber um prompt como esse, significa que o "
            " usuário está tentando usar um arquivo com o seu bot e "
            f" encontrou um erro: {e}. Eles querem que você explique o "
            "que aconteceu de forma simples, sem jargões técnicos de "
            "programação, e que também diga quais tipos de arquivos você "
            "consegue entender."
        )
    return response.text


chat_interface = gr.ChatInterface(
    fn=gradio_wrapper, title="Chatbot! LinkedIn Describer ✍️", multimodal=True
)

chat_interface.launch()
