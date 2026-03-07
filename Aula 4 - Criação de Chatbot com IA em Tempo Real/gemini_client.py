from google import genai

# cria cliente uma vez
client = genai.Client()


def gerar_resposta_gemini(mensagens: list) -> str:
    """
    Envia o histórico de mensagens para o Gemini e retorna a resposta.

    @param mensagens list: Lista de mensagens no formato
    [{"role":"user","content":"texto"}]

    @return str: resposta gerada pela IA
    """

    # converte histórico para texto simples
    prompt = ""

    for msg in mensagens:
        if msg["role"] == "user":
            prompt += f"Usuário: {msg['content']}\na"
        else:
            prompt += f"Assistente: {msg['content']}\n"

    prompt += "Assistente:"

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    print(response)

    return response.text