# ============================================================
# Correcao Global de Links Relativos - ads_mod_01
# ============================================================
$base = "d:\SourceCode\REPOS\github.io\ads_mod_01_fundamentos_da_computacao\docs"
$enc = New-Object System.Text.UTF8Encoding($false)

$targets = @("exercicios", "projetos", "quizzes", "slides")

foreach ($t in $targets) {
    $dir = "$base\$t"
    if (![System.IO.Directory]::Exists($dir)) { continue }
    
    Get-ChildItem $dir -Filter "*.md" | ForEach-Object {
        $content = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
        $orig = $content
        
        # Corrigir links para aulas: (aula-XX.md) -> (../aulas/aula-XX.md)
        $content = $content -replace '\(aula-(\d+)\.md\)', '(../aulas/aula-$1.md)'
        
        # Corrigir links para exercicios: (exercicio-XX) -> (../exercicios/exercicio-XX.md)
        $content = $content -replace '\(exercicio-(\d+)\)', '(../exercicios/exercicio-$1.md)'
        
        # Corrigir links para quizzes: (quiz-(\d+)) -> (../quizzes/quiz-$1.md)
        $content = $content -replace '\(quiz-(\d+)\)', '(../quizzes/quiz-$1.md)'

        # Corrigir links para slides: (slide-(\d+).html) -> (../slides/slide-$1.html)
        $content = $content -replace '\(slide-(\d+)\.html\)', '(../slides/slide-$1.html)'

        if ($content -ne $orig) {
            [System.IO.File]::WriteAllText($_.FullName, $content, $enc)
            Write-Host "FIXED: $($_.FullName)"
        }
    }
}

Write-Host "Correcao de links concluida."
