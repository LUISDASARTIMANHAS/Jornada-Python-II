# input do chat (campo de mensagem)
# a cada mensagem que o usuário enviar:
    # mostrar a mensagem que o usuario enviou no chat
    # pegar a pergunta e enviar para uma IA responder
    # exibir a resposta da IA na tela


# Streamlit > apenas com Python criar o frontend e o
# a IA que vamos usar: OpenAI
# pip install openai streamlit
import streamlit as st

from gemini_client import gerar_resposta_gemini

# markdown
st.write("# Chatbot com IA")
# cria lista_mensagens caso não exista
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []


texto_user = st.chat_input("Digite sua mensagem")

# mostra mensagens anteriores
for mensagem in st.session_state["lista_mensagens"]:
    role= mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_user:
    # mostrar a mensagem que o usuario enviou no chat
    st.chat_message("user").write(texto_user)
    mensagem_usuario = {"role": "user", "content": texto_user}
    st.session_state["lista_mensagens"].append(mensagem_usuario)

    # pegar a pergunta e enviar para uma IA responder
    resposta_ia = gerar_resposta_gemini(st.session_state["lista_mensagens"])

    st.chat_message("assistant").write(resposta_ia)
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
