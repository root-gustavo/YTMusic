# Download Audio YouTube

## Usuário:

1. Descompacte a pasta `download_yt.zip`.
   
> **Atenção:** não remova ou exclua o arquivo `ffmpeg.exe`. 
> Ele é necessário para o funcionamento do programa.

**Aviso:** Pode colocar a pasta descompactada onde quiser.

2. Execute o arquivo `download_yt.exe`.

---

## Programador:

1. Baixe a versão do Python mais recente ou a que foi usada no projeto: **v3.13.6**.

2. Crie uma virtual environment (venv) na raiz do projeto:

```bash
python -m venv venv
```

3. Ative a venv:

```bash
venv\Scripts\activate
```
4. Baixe as dependencias do projeto:
```bash
pip install -r requirements.txt
```

> Ou use o comando correspondente ao seu terminal/sistema operacional.

5. Rode o comando para gerar o executável:

```bash
pyinstaller src/download_yt.spec
```

6. Quando o processo terminar, será criada uma pasta chamada `dist` na raiz do projeto.
   Dentro dela estará o arquivo `download_yt.exe`.

> **Observação:** Dentro de `src/ffmpeg` descompacte o arquivo `ffmpeg.exe`.
7. Crie uma pasta e coloque o `ffmpeg.exe` junto com o `download_yt.exe`.
   Dessa forma, ao executar o `download_yt.exe`, o programa funcionará corretamente.

**Aviso:** Pode colocar essa nova pasta descompactada onde quiser.
