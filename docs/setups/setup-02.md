# Configuração do Ambiente (Linux)

Desenvolver em sistemas Linux é incrivelmente favorável se tratando de C/C++, visto que muito de sua arquitetura nativa é criada fundamentalmente em cima das mesmas bibliotecas padrão de C que usaremos no curso.

## 1. Instalando Compiladores Globais

Enquanto no Windows precisamos de *runners* emulando diretórios Unix, no Linux tudo geralmente é simples usando o utilitário nativo de instalação.

Abra o seu terminal (no Ubuntu, pop_OS!, Linux Mint ou outros baseados no sistema Debian) e atualize as fontes do seu sistema:

```bash
sudo apt update
```

Logo após, faça a requisição dos pacotes-marco de desenvolvimento nativo do sistema e comissione-os para o disco global da máquina:

```bash
sudo apt install build-essential gdb
```

> ℹ️  O pacote meta chamado **`build-essential`** já contêm o `gcc` (para compilarmos a linguagem C), o `g++` (para compilar a linguagem C++ orientada a objetos) e o `make`. O `gdb` anexado acima é a ferramenta responsável pelo debbuging (análise linha a linha de falhas de memória) destas linguagens.

> **Teste Rápido**: No próprio terminal digite `g++ --version`. Se aparecer um texto da *Free Software Foundation*, sucesso!

---

## 2. O Editor de Código (Visual Studio Code)

O uso de IDEs gigantescas como *Clion* são ótimas, mas o VS Code permanece sendo leve e excelente para as simulações pragmáticas da cadeira.

1. Baixe o pacote correspondente à sua arquitetura: `.deb` (Debian/Ubuntu) ou `.rpm` (Fedora) no site oficial [code.visualstudio.com](https://code.visualstudio.com/).
2. Instale usando o empacotador local. Exemplo via diretório de Downloads: `sudo dpkg -i ~/Downloads/code_*.deb`.

Ou de forma veloz caso possua o ecossistema Snap embutido com permissão clássica ativa:
```bash
sudo snap install code --classic
```

### Extensões Recomendadas (Obrigatórias)

Abra o seu VS Code recém instalado, procure pelo ícone de **Extensions** e pesquise:

1. **C/C++** (fabricante oficial: *Microsoft*): Traz sintaxe, autocompletar do código base (`IntelliSense`).
2. **Code Runner** (fabricante oficial: *Jun Han*): Instala um ícone de "*Play*" (▶️) no seu VS Code, permitindo você simplesmente apertar "Compilar e Rodar" sobre seu arquivo atual (`.cpp` ou `.c`), eliminando a necessidade de escrever `$ gcc app.c -o app` frequentemente nas implementações cotidianas deste curso.

---

**🎉 Pronto! O seu sistema Unix agora é oficialmente imbatível como emulador nativo para esta disciplina.**
