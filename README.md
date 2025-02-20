# Chatbot! LinkedIn Describer ✍️

## Descrição do Projeto

Este projeto consiste em um chatbot desenvolvido em Python que utiliza a API do Gemini para gerar descrições de posts para o LinkedIn a partir de arquivos de diversos tipos, como imagens, áudios e textos. O chatbot é integrado a uma interface gráfica através do Gradio, proporcionando uma experiência interativa e amigável para o usuário.

## Como Executar o Projeto

1.  **Clone este repositório:**

    ```bash
    git clone https://github.com/Tony-Felix/Chatbot-LinkedIn-Describer
    cd projeto-clonado
    ```

2.  **Crie um ambiente virtual (opcional, mas recomendado):**

    ```bash
    python3 -m venv .venv  # Cria o ambiente virtual
    source .venv/bin/activate  # Ativa o ambiente virtual (Linux/macOS)
    .venv\Scripts\activate  # Ativa o ambiente virtual (Windows)
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a chave da API do Gemini:**

    *   Faça login na sua conta do Google no navegador e acesse: <https://aistudio.google.com/app/apikey?hl=pt-br>
    *   Crie uma chave GEMINI\_API gratuita.
    *   Defina a chave da API como a variável de ambiente `GEMINI_API`:

        *   **Linux/macOS:**
            ```bash
            nano ~/.bashrc  # Ou ~/.zshrc, dependendo do seu shell
            ```
            Adicione a seguinte linha no final do arquivo:
            ```bash
            export GEMINI_API="SUA_CHAVE_DE_API_AQUI"
            ```
            Salve o arquivo e execute:
            ```bash
            source ~/.bashrc  # Ou source ~/.zshrc
            ```

        *   **Windows:**
            Abra o menu Iniciar, procure por "Variáveis de ambiente" e selecione "Editar as variáveis de ambiente do sistema". Clique em "Variáveis de Ambiente...", em "Variáveis do sistema", clique em "Novo..." e adicione `GEMINI_API` como nome de sua chave como valor.

        *   **Verifique se a variável foi criada:**
            ```bash
            echo $GEMINI_API
            ```

5.  **Execute o script:**

    ```bash
    python seu_script.py  # Substitua pelo nome do seu script principal
    ```

## Observações

*   Certifique-se de ter o Python instalado em seu sistema.
*   A chave de API do Gemini é necessária para o funcionamento do chatbot.
*   O Gradio irá gerar um link local para acessar a interface do chatbot.

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Autor

[Antônio Felix]