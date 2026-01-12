# Script de ayuda para publicar el repositorio en GitHub
# Este script te guiará paso a paso

Write-Host "`n=== PUBLICAR REPOSITORIO EN GITHUB ===" -ForegroundColor Green
Write-Host "`nTu usuario de Git: florentz14" -ForegroundColor Cyan
Write-Host "`nINSTRUCCIONES:" -ForegroundColor Yellow
Write-Host "`n1. Ve a https://github.com/new en tu navegador" -ForegroundColor White
Write-Host "2. Configura el repositorio:" -ForegroundColor White
Write-Host "   - Repository name: python-lab" -ForegroundColor Gray
Write-Host "   - Description: Coleccion completa de algoritmos y estructuras de datos en Python" -ForegroundColor Gray
Write-Host "   - Visibilidad: Public o Private (tu eleccion)" -ForegroundColor Gray
Write-Host "   - NO marques 'Initialize with README'" -ForegroundColor Gray
Write-Host "   - NO agregues .gitignore ni licencia" -ForegroundColor Gray
Write-Host "3. Haz clic en 'Create repository'" -ForegroundColor White
Write-Host "`n4. Despues de crear el repositorio, ejecuta estos comandos:" -ForegroundColor Yellow
Write-Host "`n   git remote add origin https://github.com/florentz14/python-lab.git" -ForegroundColor Cyan
Write-Host "   git push -u origin main" -ForegroundColor Cyan
Write-Host "`nNOTA: Si GitHub te pide autenticacion, necesitaras un Personal Access Token" -ForegroundColor Yellow
Write-Host "      Obtener token: https://github.com/settings/tokens" -ForegroundColor Gray
Write-Host "`n" -ForegroundColor White
