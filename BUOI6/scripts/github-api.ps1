param([ValidateSet('status','pages','runs','enable-pages','dispatch')][string]$Action='status')
$ErrorActionPreference='Stop'
$env:GCM_INTERACTIVE='Never'
$credential = "protocol=https`nhost=github.com`n`n" | git credential fill 2>$null
$entry = $credential | Where-Object { $_ -like 'password=*' } | Select-Object -First 1
if (!$entry) { throw 'No stored GitHub credential available' }
$token = $entry.Substring(9)
$headers = @{Authorization="Bearer $token";Accept='application/vnd.github+json';'X-GitHub-Api-Version'='2022-11-28'}
$base='https://api.github.com/repos/Mikmankkk/TH_LTANTT_2387700042'
switch($Action){
 'status' { $repo=Invoke-RestMethod $base -Headers $headers; [pscustomobject]@{repository=$repo.full_name;default_branch=$repo.default_branch;push=$repo.permissions.push;has_pages=$repo.has_pages} | ConvertTo-Json }
 'pages' { Invoke-RestMethod "$base/pages" -Headers $headers | Select-Object html_url,status,build_type | ConvertTo-Json }
 'enable-pages' { try { $existing=Invoke-RestMethod "$base/pages" -Headers $headers; if($existing.build_type -eq 'workflow'){ $existing | Select-Object html_url,status,build_type | ConvertTo-Json } else { Invoke-RestMethod "$base/pages" -Headers $headers -Method Put -ContentType 'application/json' -Body '{"build_type":"workflow"}' | Select-Object html_url,status,build_type | ConvertTo-Json } } catch { if([int]$_.Exception.Response.StatusCode -eq 404){ Invoke-RestMethod "$base/pages" -Headers $headers -Method Post -ContentType 'application/json' -Body '{"build_type":"workflow"}' | Select-Object html_url,status,build_type | ConvertTo-Json } else { throw } } }
 'dispatch' { Invoke-RestMethod "$base/actions/workflows/buoi6.yml/dispatches" -Headers $headers -Method Post -ContentType 'application/json' -Body '{"ref":"main"}' }
 'runs' { $runs=Invoke-RestMethod "$base/actions/workflows/buoi6.yml/runs?per_page=3" -Headers $headers; $runs.workflow_runs | Select-Object id,head_sha,status,conclusion,html_url | ConvertTo-Json -Depth 4 }
}
