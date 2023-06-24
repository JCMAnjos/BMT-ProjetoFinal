import json
import pandas as pd

lista_total_coment = []

videoNum = 1
DB = "DB3"
continua_video = True
while continua_video:
    pgNum = 1
    continua_pg = True

    nomeArquivo = 'ArquivosJsonColetadosYoutube/Extraido_' + DB + '/video_' + str(videoNum) + '_pg_' + str(pgNum) + '.json'
    print("lendo arquivo: " + nomeArquivo)
    itemListJson = []
    try:
        arquivo = open(nomeArquivo,'r')
        itemListJson = json.loads(arquivo.read()).get('items')
        arquivo.close()
        for comment in itemListJson:
            lista_total_coment.append(comment.get('snippet').get('topLevelComment').get('snippet').get('textOriginal'))

    except(FileNotFoundError):
        print("Erro de leitura de arquivo")
        continua_video = False
        continua_pg = False

    


    pgNum = pgNum + 1
    while continua_pg:
        nomeArquivo = 'ArquivosJsonColetadosYoutube/video_' + str(videoNum) + '_pg_' + str(pgNum) + '.json'
        print("lendo arquivo: " + nomeArquivo)
        itemListJson = []
        try:
            arquivo = open(nomeArquivo,'r')
            itemListJson = json.loads(arquivo.read()).get('items')
            arquivo.close()

            for comment in itemListJson:
                lista_total_coment.append(comment.get('snippet').get('topLevelComment').get('snippet').get('textOriginal'))


        except(FileNotFoundError):
            print("Erro de leitura de arquivo")
            continua_pg = False
        pgNum = pgNum + 1
    videoNum = videoNum+1


df = pd.DataFrame(lista_total_coment)
df.columns = ['Comentario']
df.to_csv('Comentarios_extraídos/comentarios_' + DB + '.csv', sep=";")
