rshell rm /pyboard/* --recursive
rshell rsync ./src /pyboard
Write-Output 'Done.'