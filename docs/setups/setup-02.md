# Configuração do Ambiente (Linux)

Para este curso, usaremos ferramentas básicas que geralmente já vêm instaladas no Linux, mas vamos garantir que você tenha tudo pronto.

## 1. Navegador Web

Recomendamos **Firefox** ou **Chromium/Chrome**.
Para instalar no Ubuntu/Debian:
```bash
sudo apt update
sudo apt install firefox
# ou
sudo apt install chromium-browser
```

## 2. Visual Studio Code

É o editor recomendado.
1. Baixe o pacote `.deb` ou `.rpm` em [code.visualstudio.com](https://code.visualstudio.com/).
2. Instale via terminal: `sudo apt install ./nome-do-arquivo.deb`.

Ou instale via Snap:
```bash
sudo snap install code --classic
```

## 3. Python

O Python geralmente já vem instalado no Linux. Verifique:
```bash
python3 --version
```
Se não estiver instalado:
```bash
sudo apt install python3 python3-pip
```

---

**🎉 Pronto! Ambiente Linux configurado.**
