# ============================================================
# Escopo 2 - Adicionar Tags + Corrigir quiz.css + tags.md
# ============================================================
$base = "d:\SourceCode\REPOS\github.io\ads_mod_01_fundamentos_da_computacao"
$enc = New-Object System.Text.UTF8Encoding($false)

# Mapa de tags por aula
$tagMap = @{
    "aula-01" = "tags:`n  - Computacao`n  - Bases-Numericas`n  - Introducao"
    "aula-02" = "tags:`n  - Bases-Numericas`n  - Binario`n  - Conversao"
    "aula-03" = "tags:`n  - Bases-Numericas`n  - Binario`n  - Conversao"
    "aula-04" = "tags:`n  - Bases-Numericas`n  - Octal`n  - Conversao"
    "aula-05" = "tags:`n  - Bases-Numericas`n  - Hexadecimal`n  - Conversao"
    "aula-06" = "tags:`n  - Bases-Numericas`n  - Hexadecimal`n  - Binario"
    "aula-07" = "tags:`n  - Aritmetica`n  - Binario`n  - Calculo"
    "aula-08" = "tags:`n  - Representacao`n  - Dados`n  - Hardware"
    "aula-09" = "tags:`n  - Logica-Digital`n  - Booleana`n  - Logica"
    "aula-10" = "tags:`n  - Logica-Digital`n  - Tabelas-Verdade`n  - Logica"
    "aula-11" = "tags:`n  - Logica-Digital`n  - Circuitos`n  - Hardware"
    "aula-12" = "tags:`n  - Hardware`n  - Arquitetura`n  - Computacao"
    "aula-13" = "tags:`n  - Hardware`n  - Memoria`n  - Armazenamento"
    "aula-14" = "tags:`n  - Software`n  - Sistemas-Operacionais`n  - SO"
    "aula-15" = "tags:`n  - Algoritmos`n  - Fluxogramas`n  - Logica"
    "aula-16" = "tags:`n  - Programacao`n  - Introducao`n  - Algoritmos"
}

Write-Host "=== Adicionando frontmatter de tags nas aulas ==="
$aulaDir = "$base\docs\aulas"
foreach ($key in $tagMap.Keys) {
    $path = "$aulaDir\$key.md"
    if (![System.IO.File]::Exists($path)) { Write-Host "AUSENTE: $path"; continue }

    $content = [System.IO.File]::ReadAllText($path, [System.Text.Encoding]::UTF8)

    # Verificar se ja tem frontmatter ---
    if ($content.StartsWith("---")) {
        Write-Host "SKIP (ja tem frontmatter): $key"
        continue
    }

    # Adicionar frontmatter com tags no inicio
    $tagBlock = $tagMap[$key]
    $newContent = "---`n$tagBlock`n---`n`n" + $content
    [System.IO.File]::WriteAllText($path, $newContent, $enc)
    Write-Host "OK: $key - tags adicionadas"
}

# --- Criar docs/tags.md ---
Write-Host ""
Write-Host "=== Criando docs/tags.md ==="
$tagsMd = @"
---
hide:
  - navigation
---

# Tags

Explore as aulas por tema:
"@
[System.IO.File]::WriteAllText("$base\docs\tags.md", $tagsMd, $enc)
Write-Host "OK: tags.md criado"

# --- Corrigir quiz.css: adicionar flex-shrink: 0 ---
Write-Host ""
Write-Host "=== Corrigindo quiz.css (flex-shrink: 0) ==="
$cssPath = "$base\docs\assets\css\quiz.css"
if ([System.IO.File]::Exists($cssPath)) {
    $css = [System.IO.File]::ReadAllText($cssPath, [System.Text.Encoding]::UTF8)
    $changed = $false

    # Adicionar flex-shrink em seletores de opcoes do quiz se nao existir
    if ($css -notmatch 'flex-shrink:\s*0') {
        # Inserir em .quiz-option ou similar
        $css = [System.Text.RegularExpressions.Regex]::Replace(
            $css,
            '(\.quiz-option[^{]*\{)',
            "`$1`n  flex-shrink: 0;"
        )
        # Inserir em input[type=radio] e input[type=checkbox] se existir
        $css = [System.Text.RegularExpressions.Regex]::Replace(
            $css,
            '(input\[type=[''"]?(radio|checkbox)[''"]?\][^{]*\{)',
            "`$1`n  flex-shrink: 0;"
        )
        $changed = $true
    }

    # Garantir que label do quiz nao quebre circulos
    $quizLabelFix = @"

/* Fix visual: garantir circulos perfeitos nos quizzes */
.quiz-option input[type="radio"],
.quiz-option input[type="checkbox"] {
  flex-shrink: 0;
  min-width: 1rem;
  min-height: 1rem;
}
"@
    if ($css -notmatch 'Fix visual: garantir circulos perfeitos') {
        $css += $quizLabelFix
        $changed = $true
    }

    if ($changed) {
        [System.IO.File]::WriteAllText($cssPath, $css, $enc)
        Write-Host "OK: quiz.css corrigido (flex-shrink adicionado)"
    }
    else {
        Write-Host "SKIP: quiz.css ja esta correto"
    }
}
else {
    Write-Host "ERRO: quiz.css nao encontrado em $cssPath"
}

Write-Host ""
Write-Host "Escopo 2 concluido."
