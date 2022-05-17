# OCR GOV.BR

O Projeto consiste em coletar dados de documentos CNH e CRLV e disponibilizar via API atraves de JSON Content.

## Estrutura do Projeto

- `app` - Diretorio Base do Projeto
   - `controllers` - Onde estão configurados os metodos com as rotas, novas rotas devem ser adicionadas aqui
      - `cnh.py`
      - `crlv.py`
   - `properties` - arquivos de parametros com as informações sobre o processamento da imagem
      - `cnh.json`
      - `crlv.json`
   - `server` - Configurações referente a inicialização do server
      - `instance.py`
   - `App.py` - Script principal
   - `Configs.py` - Script referente a configuração de projeto
   - `ConvertImage.py` - Script com funções referente a tratamento de imagem
   - `ExtractImageData.py` - Script referente a coleta de dados da imagem
   - `Log.py` - Script com funções de log e monitoramento
   - `requirements.txt` - libs utilizadas no projeto, o arquivo é utilizado no processo de build 
- `libs` - libs externas
- `logs` - diretorio de logs
- `temp` - diretorio temporario utilizado no projeto


## External Libs
Contempla as tecnologias utilizadas no OCR, como:
 - Poopler (Versao 0.68.0)
 - Tesseract (Versao 2.0)

## Monitoramento
- Os Logs são armazenados na pasta logs do projeto

## Configuração de Properties
Os Properties devem seguir a seguinte estrutura visando tornar dinamico o processo

```
{
    "fields":{
        "cpf":{
            "points":[420,392,580,414],
            "psm":7,
            "threshold":0
        },
        "categoria":{
            "points":[648,560,710,582],
            "psm":10,
            "threshold":0
        },
        "validade":{
            "points":[420,608,550,627],
            "psm":7,
            "threshold":0   
        },
        "nome":{
            "points":[195,296,713,320],
            "psm":7,
            "threshold":200
        }
    }
}
```
- O nome do campo será retornado na API
- `points` - Pontos de corte da imagem, onde o texto esta localizado
- `psm` - Parametro para auxilio na extração da imagem
- `threshold` - Ajuste dos pixels da imagem, 0 significa que a imagem padrao deve ser considerada
- `parms` - Outros Parametros que podem ser necessarios durante o processamento (Nao Obrigatorio)

### How to Run
`python App.py`


### REST Request
O Projeto por padrao recebe requisições POST com o seguinte body (ContentType/JSON)
```
{
   "base64_file":"ARQUIVO NO FORMATO BASE64"
}
```
> `SWAGGER` - http://ip:5002/docs
