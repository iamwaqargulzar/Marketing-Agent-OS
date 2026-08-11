[CmdletBinding()]
param(
    [ValidateSet('universal', 'codex', 'opencode', 'claude-code', 'pi', 'cursor', 'gemini', 'copilot', 'amp', 'cline', 'roo', 'windsurf', 'openclaw', 'hermes', 'all')]
    [string]$Agent = 'universal',
    [ValidateSet('project', 'user')]
    [string]$Scope = 'project',
    [string]$Project = (Get-Location).Path,
    [string[]]$Skill = @(),
    [switch]$Force,
    [switch]$DryRun,
    [switch]$List
)

$ErrorActionPreference = 'Stop'
$installer = Join-Path $PSScriptRoot 'scripts/install.py'
$arguments = @($installer, '--agent', $Agent, '--scope', $Scope, '--project', $Project)
foreach ($name in $Skill) { $arguments += @('--skill', $name) }
if ($Force) { $arguments += '--force' }
if ($DryRun) { $arguments += '--dry-run' }
if ($List) { $arguments += '--list' }

if (Get-Command py -ErrorAction SilentlyContinue) {
    & py -3 @arguments
    exit $LASTEXITCODE
}
if (Get-Command python3 -ErrorAction SilentlyContinue) {
    & python3 @arguments
    exit $LASTEXITCODE
}
if (Get-Command python -ErrorAction SilentlyContinue) {
    & python @arguments
    exit $LASTEXITCODE
}

Write-Error 'Marketing Agent OS requires Python 3.9+ for the local installer. Alternatively, install Node.js and run `npx skills add . --all` from this directory.'
