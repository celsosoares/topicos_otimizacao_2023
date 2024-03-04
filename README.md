# Run

É necessário ter instalado o alguma versão do [python3](https://www.python.org/downloads/).

Para executar o programa, escreva o seguinte comando:

```bash
python3 lec.py
```

# Build

O projeto utiliza a biblioteca [pyinstaller](https://pyinstaller.org/en/stable/installation.html) para converter um arquivo .py para um executável.

Para gerar a build do projeto, execute o seguinte comando após alguma modificação no código:

### build file
```bash
bash build.sh
```

### pyinstaller
```bash
pyinstaller --onefile lec.py
```

Isso irá gerar um novo executável em /dist/lec