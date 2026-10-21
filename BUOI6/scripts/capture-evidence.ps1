param()
$ErrorActionPreference = 'Stop'
$labRoot = Split-Path $PSScriptRoot -Parent
$evidence = Join-Path $labRoot 'evidence'
New-Item -ItemType Directory -Force (Join-Path $labRoot '.capture-temp') | Out-Null
Add-Type -AssemblyName System.Drawing
Add-Type -AssemblyName System.Windows.Forms
Add-Type @'
using System;
using System.Runtime.InteropServices;
public class LabWindow {
  [StructLayout(LayoutKind.Sequential)] public struct Rect { public int Left,Top,Right,Bottom; }
  [DllImport("user32.dll", CharSet=CharSet.Unicode)] public static extern IntPtr FindWindow(string cls,string title);
  [DllImport("user32.dll")] public static extern bool SetForegroundWindow(IntPtr h);
  [DllImport("user32.dll")] public static extern bool MoveWindow(IntPtr h,int x,int y,int w,int height,bool repaint);
  [DllImport("user32.dll")] public static extern bool GetWindowRect(IntPtr h,out Rect rect);
  [DllImport("user32.dll")] public static extern bool PostMessage(IntPtr h,uint msg,IntPtr wp,IntPtr lp);
  [DllImport("user32.dll")] public static extern bool SetProcessDPIAware();
}
'@
[LabWindow]::SetProcessDPIAware() | Out-Null
Get-Process -Name cmd -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowTitle -like 'BUOI6-*' } | ForEach-Object { [LabWindow]::PostMessage($_.MainWindowHandle,0x0010,[IntPtr]::Zero,[IntPtr]::Zero) | Out-Null }
$cases = [ordered]@{
 '01-environment' = @('hostname','ver','node --version','call npm.cmd --version','git remote -v')
 '02-tests' = @('call npm.cmd test')
 '03-security' = @('call npm.cmd run security','node scripts\audit.mjs')
 '04-build' = @('call npm.cmd run build','node scripts\checksums.mjs')
}
foreach ($item in $cases.GetEnumerator()) {
 $title = 'BUOI6-' + $item.Key
 $marker = Join-Path $env:TEMP ($title + '.done')
 if (Test-Path -LiteralPath $marker) { Remove-Item -LiteralPath $marker }
 $batch = Join-Path $env:TEMP ($title + '.cmd')
 $lines = @('@echo off',('title '+$title),'mode con: cols=140 lines=48','color 0F',('cd /d "'+$labRoot+'"'),'echo VO HOANG MINH MAN - MSSV 2387700042 - LAB 06','echo Captured from real Windows CMD.','echo %DATE% %TIME%','echo.')
 foreach ($command in $item.Value) {
   $lines += 'echo CMD^> ' + ($command -replace '>','^>')
   $lines += $command
   $lines += ('if errorlevel 1 (echo FAILED & echo FAILED > "'+$marker+'" & exit /b 1)')
 }
 $lines += 'echo.'
 $lines += 'echo ALL COMMANDS COMPLETED SUCCESSFULLY'
 $lines += 'title ' + $title
 $lines += 'echo OK > "'+$marker+'"'
 [IO.File]::WriteAllLines($batch,$lines,[Text.Encoding]::ASCII)
 Start-Process -FilePath "$env:WINDIR\System32\conhost.exe" -ArgumentList ('cmd.exe /d /k ""'+$batch+'""') -WindowStyle Normal | Out-Null
 $deadline = (Get-Date).AddSeconds(120)
 while (!(Test-Path -LiteralPath $marker)) {
   if ((Get-Date) -gt $deadline) { throw "CMD stage timed out: $title" }
   Start-Sleep -Milliseconds 250
 }
 if ((Get-Content -LiteralPath $marker) -match 'FAILED') { throw "CMD command failed: $title" }
 $consoleProcess = Get-Process -Name cmd -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowTitle -eq $title } | Sort-Object StartTime -Descending | Select-Object -First 1
 $window = if ($consoleProcess) { $consoleProcess.MainWindowHandle } else { [IntPtr]::Zero }
 if ($window -eq [IntPtr]::Zero) { throw "Cannot locate real console window: $title" }
 $bounds = [Windows.Forms.Screen]::PrimaryScreen.Bounds
 [LabWindow]::MoveWindow($window,10,10,[Math]::Min(1510,$bounds.Width-20),[Math]::Min(970,$bounds.Height-20),$true) | Out-Null
 [LabWindow]::SetForegroundWindow($window) | Out-Null
 Start-Sleep -Milliseconds 800
 $rect = New-Object LabWindow+Rect
 [LabWindow]::GetWindowRect($window,[ref]$rect) | Out-Null
 $bitmap = New-Object Drawing.Bitmap ($rect.Right-$rect.Left),($rect.Bottom-$rect.Top)
 $graphics = [Drawing.Graphics]::FromImage($bitmap)
 $graphics.CopyFromScreen($rect.Left,$rect.Top,0,0,$bitmap.Size)
 $output = Join-Path $evidence ($item.Key+'.png')
 $bitmap.Save($output,[Drawing.Imaging.ImageFormat]::Png)
 $graphics.Dispose()
 $bitmap.Dispose()
 [LabWindow]::PostMessage($window,0x0010,[IntPtr]::Zero,[IntPtr]::Zero) | Out-Null
 Write-Output "Captured real CMD window: $output"
}
Get-ChildItem $evidence -Filter '*.png' | Get-FileHash -Algorithm SHA256 | Select-Object Hash,Path | ConvertTo-Json | Set-Content -Encoding UTF8 (Join-Path $evidence 'sha256.json')
