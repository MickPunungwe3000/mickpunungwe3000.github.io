param(
    [switch]$Drafts,
    [string]$RubyBin
)
$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path $PSScriptRoot -Parent
$originalPath = $env:PATH
try {
    if ($RubyBin) {
        $rubyDirectory = (Resolve-Path -LiteralPath $RubyBin).Path
        if (-not (Test-Path -LiteralPath (Join-Path $rubyDirectory 'ruby.exe'))) {
            throw 'RubyBin must point to a directory containing ruby.exe.'
        }
        $env:PATH = $rubyDirectory + ';' + $env:PATH
    }
    if (-not (Get-Command bundle -ErrorAction SilentlyContinue)) {
        throw 'Install Ruby+Devkit and Bundler, or supply -RubyBin with your Ruby bin directory. See README.md.'
    }
    Push-Location -LiteralPath $projectRoot
    try {
        $config = '_config.yml'
        if ($Drafts) { $config = '_config.yml,_config.preview.yml' }
        & bundle exec jekyll serve --config $config --host 127.0.0.1
        if ($LASTEXITCODE -ne 0) { throw "Jekyll exited with code $LASTEXITCODE" }
    } finally {
        Pop-Location
    }
} finally {
    $env:PATH = $originalPath
}
