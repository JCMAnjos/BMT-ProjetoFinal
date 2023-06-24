import openai
import pandas as pd

openai.api_key = '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'

#Função para classificar o comentário
def classificar_comentario(comentario):
    resposta = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Classifique o seguinte comentário sobre inteligência artificial como 'p' (positivo), 'n' (negativo) ou 'x' (irrelevante ou fora do assunto):\n\n{comentario}\n\nClassificação:",
        temperature=0.0,
        max_tokens=1,
        n=1,
        stop=None,
        timeout=15
    )
    classificacao = resposta.choices[0].text.strip().lower()
    return classificacao

#Ler o arquivo CSV
df = pd.read_csv('comentarios.csv', sep=';', index_col=0, header=0)

#Adicionar uma nova coluna ao DataFrame com a classificação feita
df['sentimento_GPT'] = df['comentario'].apply(classificar_comentario)

#Salvar o DataFrame com a coluna de classificação em um novo arquivo CSV
df.to_csv('comentarios_GPT_3classes.csv')

print("A classificação dos comentários foi concluída.")