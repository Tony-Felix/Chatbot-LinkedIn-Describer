import gradio as gr
from gemini_api import gradio_wrapper

chat_interface = gr.ChatInterface(fn=gradio_wrapper, multimodal=True)

titulo = (
    """<div style='height: 50px; width: 100px;'> """
    """<h1 style="position: absolute; right: 47%;"> """
    """Chatbot! Criador de Posts ✍️</h1> """
    """</div>"""
)

paths = {
        "0.01": "pix_0.01.png",
        "0.10": "pix_0.10.png",
        "1.00": "pix_1.00.png",
        "10.00": "pix_10.00.png",
        "100.00": "pix_100.00.png"
    }


def exibir_qrcode(valor):
    chosen_img = paths.get(valor, "pix_1.00.png")

    return (
        gr.update(value=chosen_img, visible=True),  # mostra iamgem
        gr.update(visible=True)  # mostra botão fechar
    )


def ocultar_qrcode():
    return (
        gr.update(visible=False),  # Oculta imagem
        gr.update(visible=False),  # Oculta o botão de fechar
        gr.update(visible=False)  # Oculta o container com os botões
    )


def mostrar_opcoes():
    return (
        gr.update(visible=True),  # mostra os botões de valores de doação
        gr.update(visible=True)   # mostra botão fechar
    )


with open("styles.css", "r") as f:
    css = f.read()

# Criando a interface e botões em blocos
with gr.Blocks(css=css, fill_height=True) as demo:
    botoes = {}

    # Container para os botões de pagamento, inicialmente oculto
    with gr.Row(visible=False) as payment_options:
        for valor in paths.keys():
            botoes[valor] = gr.Button(valor, elem_classes=["botoes"], scale=1)

    # Linha que contém o botão principal e o título
    with gr.Row():
        button1 = gr.Button(value="Me pague um ☕", elem_id="botao1", scale=0)
        titulo_text = gr.HTML(titulo)

    qrcode_image = gr.Image(type="filepath", visible=False)
    button2 = gr.Button(
        value="Fechar", visible=False, elem_id="botao2"
    )

    # Configura o clique no botão para exibir as opções de pagamento
    button1.click(
        mostrar_opcoes,
        outputs=[payment_options, button2],
        queue=False
    )

    # envia o valor escolhido para a função exibir_qrcode()
    for valor, botao in botoes.items():
        botao.click(
            fn=lambda v=valor: exibir_qrcode(v),
            outputs=[qrcode_image, button2],
            queue=False
        )

    # Configuração do clique no botão de fechar para ocultar os elementos
    button2.click(
        ocultar_qrcode,
        outputs=[qrcode_image, button2, payment_options],
        queue=False
    )

    chat_interface.render()
