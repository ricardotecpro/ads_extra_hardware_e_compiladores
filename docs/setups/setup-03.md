# Configuração do Ambiente (macOS)

O macOS, devido à sua fundação **UNIX** (semelhante ao Linux), possui um ecossistema excelente e orgânico para desenvolvedores C/C++. No entanto, em vez do compilador livre GNU (`gcc`), a Apple dita e preza pelo uso de seu próprio compilador proprietário otimizado e veloz: o **Clang** (baseado em LLVM).

Neste manual, prepararemos seu Mac (seja arquitetura Intel, ou modernas frentes Apple Silicon M1/M2/M3) para compilar e rodar os nossos códigos ao longo de toda a matéria.

---

## 🛠️ 1. O Compilador Nativo (Apple Clang)

A Apple fornece todas as ferramentas fundamentais agrupadas num pacote oficial chamado "Command Line Tools do Xcode". Não é necessário baixar a IDE pesadíssima do Xcode inteira, bastam as ferramentas de terminal.

Abra o aplicativo nativo **Terminal** (ou seu de preferência como *iTerm2*) e insira o seguinte gatilho no prompt:

<div class="termy" markdown="1">

```console
$ xcode-select --install
```

</div>

> [!INFO]
> Uma janela em popup gráfico surgirá no seu OS perguntando se você deseja instalar as Ferramentas de Linha de Comando. Aceite e aguarde o download (costuma ter alguns GBs de depêndencias essenciais, como `make`, `clang` e as livrarias standard do `C`).

### Confirmando a Instalação
Após o término, para testar se a âncora do hardware já tem consciência do seu compilador C++, no próprio terminal, digite:

```bash
clang++ --version
```
*Se um bloco de texto contendo `Apple clang version...` surgir, a fundação está sólida!*

---

## 🍺 2. Homebrew (Opcional, mas Altamente Recomendado)

Diferente do Linux que usa `apt`, a forma mais civilizada de gerenciar pacotes binários e softwares no Mac é através do **Homebrew**. Ele é a salvação do leão de chácara em C/C++ frente a biblitecas adicionais de terceiros.

Caso ainda não possua, copie do site oficial [`brew.sh`](https://brew.sh/pt-br/) o comando para colar no seu terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

*(Leia as instruções pós-instalação no terminal caso seja um Mac M1/M2/M3 ARM, ele pedirá para adicionar o brew ao `$PATH` no seu `~/.zprofile`)*

---

## 💻 3. O Editor de Código (Visual Studio Code)

Use seu recém-instalado poder do Brew para baixar limpidamente a nossa IDE do curso:

```bash
brew install --cask visual-studio-code
```
Ou alternativamente, baixe via `.dmg` no site [code.visualstudio.com](https://code.visualstudio.com/).

### Extensões Obrigatórias no VS Code

Abra o seu VS Code recém instalado, procure pela aba quadrada de **Extensions** e pesquise:

1. **C/C++** (fabricante oficial: *Microsoft*): Traz sintaxe, debug visual na IDE (usando LLVM/lldb nativo do Mac) e autocompletar do código base (`IntelliSense`).
2. **Code Runner** (fabricante oficial: *Jun Han*): Instala um ícone de "*Play*" (▶️) super conveniente no topo direito da janela, permitindo compilar e enviar saída rodando do app num instante.

---

**🎉 A Magia UNIX Pronta!** Seu sistema macOS agora está perfeitamente alinhado em linha de comando UNIX e compilará códigos C/C++ na velocidade espetacular dos processadores da Apple sem interrupções.
