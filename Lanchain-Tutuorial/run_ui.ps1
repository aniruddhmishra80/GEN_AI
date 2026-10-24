$ErrorActionPreference = "Stop"
Set-Location $PSScriptRoot
& "$PSScriptRoot\.venv\Scripts\Activate.ps1"
streamlit run "Cinesage/UIcore.py"
