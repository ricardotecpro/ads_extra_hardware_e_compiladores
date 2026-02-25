# ============================================================
# Auditoria e Padronizacao das Aulas - ads_mod_01
# ============================================================
$base = "d:\SourceCode\REPOS\github.io\ads_mod_01_fundamentos_da_computacao"
$docsAulas = "$base\docs\aulas"

Write-Host "=== AUDITORIA DAS 16 AULAS ==="
Write-Host ("Aula | info | tip | warn | note | tabs | tags | chars")
Write-Host ("-" * 70)

$aulaData = @()
Get-ChildItem $docsAulas -Filter "aula-*.md" | Sort-Object Name | ForEach-Object {
    $content = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
    $hasInfo = $content -match '!!! info'
    $hasTip = $content -match '!!! tip'
    $hasWarning = $content -match '!!! warning'
    $hasNote = $content -match '!!! note'
    $hasTabs = $content -match '=== "'
    $hasTags = $content -match '^---' -and $content -match 'tags:'
    $chars = $content.Length

    $row = "$($_.Name) | $(if($hasInfo){'OK'}else{'--'}) | $(if($hasTip){'OK'}else{'--'}) | $(if($hasWarning){'OK'}else{'--'}) | $(if($hasNote){'OK'}else{'--'}) | $(if($hasTabs){'OK'}else{'--'}) | $(if($hasTags){'OK'}else{'NO-TAGS'}) | $chars"
    Write-Host $row
    $aulaData += [PSCustomObject]@{
        File = $_.FullName
        Name = $_.Name
        hasInfo = $hasInfo; hasTip = $hasTip; hasWarn = $hasWarning
        hasNote = $hasNote; hasTabs = $hasTabs; hasTags = $hasTags
    }
}

Write-Host ""
Write-Host "=== VERIFICAR LINKS QUEBRADOS exercicios/ e projetos/ ==="
@("exercicios", "projetos") | ForEach-Object {
    $dir = "$base\docs\$_"
    if ([System.IO.Directory]::Exists($dir)) {
        Get-ChildItem $dir -Filter "*.md" | ForEach-Object {
            $c = [System.IO.File]::ReadAllText($_.FullName, [System.Text.Encoding]::UTF8)
            $links = [System.Text.RegularExpressions.Regex]::Matches($c, '\[.*?\]\((\.\.?/[^)]+)\)')
            foreach ($lk in $links) {
                $target = $lk.Groups[1].Value -replace '/', '\'
                $resolved = [System.IO.Path]::GetFullPath("$([System.IO.Path]::GetDirectoryName($_.FullName))\$target")
                if (![System.IO.File]::Exists($resolved) -and ![System.IO.Directory]::Exists($resolved)) {
                    Write-Host "LINK QUEBRADO: $($_.Name) -> $($lk.Groups[1].Value)"
                }
            }
        }
    }
}
Write-Host "Verificacao concluida."
