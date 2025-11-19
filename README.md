# ImagePredictionAI

Projeto simples para detectar objetos em imagens e vídeos utilizando modelos YOLO treinados localmente com a biblioteca `ultralytics`.

**Resumo**
- Código principal em `app.py` que carrega um modelo em `model/` e executa detecções sobre um vídeo ou imagem em `video/` ou `images/`.

**Pré-requisitos**
- Python 3.10+ (recomendado)
- Instalar dependências (ex.: `ultralytics`, `opencv-python`)

Exemplo de instalação rápida:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Como rodar**
- Ajuste o caminho do modelo em `app.py` se necessário.
- Execute `python app.py` para rodar a inferência no vídeo configurado.

**Estrutura do repositório**
- `app.py` - script principal para rodar predições
- `model/` - modelos treinados (`.pt`)
- `video/` - vídeos de entrada
- `images/` - imagens de entrada
- `results/`, `runs/` - diretórios de saída (incluir no `.gitignore` se desejar)
---

Autor: Alberto Tomaz — `arc.tomaz01@gmail.com`
