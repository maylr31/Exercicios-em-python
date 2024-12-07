import boto3
import json
import streamlit as st

# Configurar cliente do Amazon Bedrock
def configurar_bedrock():
    return boto3.client(
        "bedrock-runtime",  # Serviço correto para Bedrock Runtime
        region_name="us-east-2",  # Substitua pela sua região
    )

# Função para gerar resposta do modelo Claude
def gerar_resposta(client, mensagem_usuario):
    try:
        # Corpo da solicitação
        payload = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 200,
            "top_k": 250,
            "stopSequences": [],
            "temperature": 1,
            "top_p": 0.999,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": mensagem_usuario
                        }
                    ]
                }
            ]
        }

        # Enviar solicitação para o modelo
        response = client.invoke_model(
            modelId="anthropic.claude-3-5-haiku-20241022-v1:0",  # Substitua pelo modelo correto
            body=json.dumps(payload),
            contentType="application/json",
            accept="application/json",
        )
        # Ler a resposta
        resultado = json.loads(response["body"].read().decode("utf-8"))
        return resultado
    except Exception as e:
        return f"Erro ao conectar ao Amazon Bedrock: {e}"

# Interface do Streamlit
def main():
    st.title("Assistente com Claude no Amazon Bedrock 🤖")
    st.sidebar.header("Entrada do Usuário")

    # Entrada do usuário
    mensagem_usuario = st.sidebar.text_area(
        "Digite sua mensagem para o modelo",
        "Escreva algo aqui"
    )

    # Botão para enviar a mensagem
    if st.sidebar.button("Enviar"):
        st.write("Processando sua mensagem... Aguarde.")
        client = configurar_bedrock()
        resposta = gerar_resposta(client, mensagem_usuario)

        if isinstance(resposta, str) and resposta.startswith("Erro"):
            # Mostrar erro, caso exista
            st.error(resposta)
        else:
            # Mostrar a resposta gerada
            st.subheader("Resposta do Modelo")
            st.write(resposta)

    # Rodapé
    st.caption("Desenvolvido por Mayra e equipe.")

if __name__ == "__main__":
    main()


