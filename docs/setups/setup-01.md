# Configuração do Ambiente (Windows)

Para desenvolver as aplicações de arquitetura de software e baixo nível requeridas neste curso, precisaremos instalar ferramentas que convertam o código `C/C++` que digitaremos em binários que o hardware possa executar nativamente.

## 1. O Compilador (MSYS2 / MinGW-w64)

No Windows, a maneira mais segura, moderna e madura de instalar o compilador `GCC/G++` nativo (utilizado historicamente em sistemas Unix) é baixar o ambiente do **MSYS2**.

### Passo a Passo de Instalação:

1. Acesse [msys2.org](https://www.msys2.org/).
2. Baixe o instalador mais recente (`msys2-x86_64-xxxxxxxx.exe`).
3. Instale no caminho padrão (`C:\msys64`).
4. Ao final da instalação, deixe a caixa **"Run MSYS2 now"** marcada e clique em **Finish**. O console do terminal do MSYS2 irá abrir.

### Baixando os Pacotes de Compilação
Dentro do terminal preto do MSYS2 que abriu, digite o seguinte comando e aperte `ENTER`:

```bash
pacman -S mingw-w64-ucrt-x86_64-gcc
```

O sistema perguntará se você quer baixar (`Proceed with installation? [Y/n]`). Digite `Y` e aperte `ENTER`.
O pacote GCC e G++ (C e C++) da biblioteca UCRT (*Universal C Runtime*) começará a ser baixado no seu computador.

Quando finalizar, instale também o GDB (Depurador nativo) com o comando:

```bash
pacman -S mingw-w64-ucrt-x86_64-gdb
```

### Configurando o PATH do Windows

Para que o seu Windows e o VS Code consigam achar os compiladores (`gcc`, `g++`, `gdb`), você precisa colocar o diretório de instalação deles na variável `PATH`.

1. No menu iniciar do Windows, procure por **Editar variáveis de ambiente do sistema**.
2. Na janela que abrir ("Propriedades do Sistema"), clique no botão **Variáveis de Ambiente...**.
3. Na seção "Variáveis do sistema" (a de baixo), procure a variável **Path**, selecione-a e clique em **Editar...**.
4. Clique em **Novo** e cole o seguinte caminho:
   `C:\msys64\ucrt64\bin`
5. Pressione OK em todas as janelas para salvar e sair.

> **Teste Rápido**: Abra o Prompt de Comando do Windows (cmd) e digite `g++ --version`. Se aparecer um texto da *Free Software Foundation*, parabéns! Seu compilador está vivo.

---

## 2. O Editor de Código (Visual Studio Code)

O Visual Studio Code é um super "bloco de notas" voltado a desenvolvedores. Vai ser a nossa ferramenta oficial.

### Instalação

1. Acesse [code.visualstudio.com](https://code.visualstudio.com/).
2. Baixe a versão para **Windows**.
3. Execute o instalador (sugerimos marcar as caixas de adicionar ações de contexto ao mouse "Abrir com o VS Code" caso não estejam marcadas).

### Extensões Recomendadas (Obrigatórias)

Abra o VS Code, clique no ícone de "Extensions" (quatro quadradinhos, sendo um solto) na barra lateral esquerda e procure os seguintes nomes:

1. **C/C++** (fabricante oficial: *Microsoft*): Traz sintaxe, autocompletar do código base e o depurador IntelliSense.
2. **Code Runner** (fabricante oficial: *Jun Han*): Essa extensão mostrará um botão de "*Play*" (▶️) no canto direito de cima no seu VS Code, permitindo você clicar nele e automaticamente compilar/rodar seus códigos em C/C++ sem precisar escrever comandos gigantescos via terminal de comando.

---

**🎉 Pronto! O seu Windows agora tem a alma de um ecossistema Unix nativo e está pronto para criar executáveis velozes!**
