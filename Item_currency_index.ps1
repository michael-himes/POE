function Read-MultiLineInput {
[CmdletBinding()]
param(
)
 
$inputstring = @()
$lineinput = $null
while($lineinput -ne "qq") {
    $lineinput = Read-Host
    if($lineinput -eq "qq") {
        Continue
    } else {
        $inputstring += $lineinput
 
    }
}
 
return $inputstring
 
}
 
 
Write-Host "### Enter multi-line input ###"
Write-Host "(Type `"qq`" on a new line when finished)" -ForegroundColor Green
$multilines = Read-MultiLineInput
$multilines -join "`n"

clear
$search=(($multilines) -split "\n+")[1]
Write-Host $search
$item= $search -replace " ", "+"

Invoke-WebRequest -Uri "https://poe.trade/search" -UseBasicParsing -Method "POST" -Headers @{"Cache-Control"="max-age=0"; "Origin"="https://poe.trade"; "Upgrade-Insecure-Requests"="1"; "Sec-Fetch-Dest"="document"; "Accept"="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"; "Sec-Fetch-Site"="same-origin"; "Sec-Fetch-Mode"="navigate"; "Sec-Fetch-User"="?1"; "Referer"="https://poe.trade/"; "Accept-Encoding"="gzip, deflate, br"; "Accept-Language"="en-US,en;q=0.9"; "Cookie"="_ga=GA1.2.1454003851.1584649422; __qca=P0-1838013029-1584649422698; __gads=ID=cddbdb8d500fcb86:T=1584649426:S=ALNI_MY2_uIdaxoqOeNrip3jgAR9xyA7Qw; league=Delirium; CRISPSUBNO=3c6f0bc0d631048ac3b3a4e2ffa2be34; _gid=GA1.2.53560309.1586720717"} -ContentType "application/x-www-form-urlencoded" -Body "league=Delirium&type=&base=&name=$item&dmg_min=&dmg_max=&aps_min=&aps_max=&crit_min=&crit_max=&dps_min=&dps_max=&edps_min=&edps_max=&pdps_min=&pdps_max=&armour_min=&armour_max=&evasion_min=&evasion_max=&shield_min=&shield_max=&block_min=&block_max=&sockets_min=&sockets_max=&link_min=&link_max=&sockets_r=&sockets_g=&sockets_b=&sockets_w=&linked_r=&linked_g=&linked_b=&linked_w=&rlevel_min=&rlevel_max=&rstr_min=&rstr_max=&rdex_min=&rdex_max=&rint_min=&rint_max=&mod_name=&mod_min=&mod_max=&mod_weight=&group_type=And&group_min=&group_max=&group_count=1&q_min=&q_max=&level_min=&level_max=&ilvl_min=&ilvl_max=&rarity=&progress_min=&progress_max=&sockets_a_min=&sockets_a_max=&map_series=&altart=&identified=&corrupted=&crafted=&enchanted=&fractured=&synthesised=&mirrored=&veiled=&shaper=&elder=&crusader=&redeemer=&hunter=&warlord=&seller=&thread=&online=x&capquality=x&buyout_min=&buyout_max=&buyout_currency=&has_buyout=&exact_currency=" | Select-Object -ExpandProperty RawContent | Out-File -FilePath $env:USERPROFILE\'Documents\My Games\Path of Exile\POE_Search'

$list = foreach ($buyout in (Select-String -Path $env:USERPROFILE\'Documents\My Games\Path of Exile\POE_Search' -Pattern data-buyout)){ (($buyout) -split "=+")[1] }
#Write-Host $list | group
$list | group
$sort = $list | Get-Unique

#foreach ( $item in $sort){ $item }
