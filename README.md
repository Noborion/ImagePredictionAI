# ImagePredictionAI

Projeto simples para detectar objetos em imagens e vídeos utilizando modelos YOLO treinados localmente com a biblioteca `ultralytics`.

**Resumo**
- Código principal em `app.py` que carrega um modelo em `model/` e executa detecções sobre um vídeo em `video/`.
- Modelos pesados (`*.pt`) e resultados de execução são mantidos em pastas separadas.

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
- `images/` - imagens de exemplo
- `results/`, `runs/` - diretórios de saída (incluir no `.gitignore` se desejar)

**O que deve conter um README**
1. Título e descrição curta do projeto
2. Pré-requisitos e instalação
3. Como usar / exemplos de execução
4. Estrutura do repositório
5. Configurações importantes (variáveis, caminhos, modelos)
6. Como contribuir / rodar testes
7. Licença
8. Contato/autor

**Notas**
- Recomenda-se não versionar arquivos de modelos grandes (`.pt`) e resultados (coloque-os no `.gitignore`).
- Para publicar no GitHub, crie um repositório remoto e execute `git remote add origin <URL>` seguido de `git push -u origin main`.

---

Autor: Alberto Tomaz — `arc.tomaz01@gmail.com`
