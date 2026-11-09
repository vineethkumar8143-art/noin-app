Add-Type -AssemblyName System.Drawing

function Optimize-Jpeg($srcPath, $destPath, $maxWidth, $quality) {
    $img = [System.Drawing.Image]::FromFile($srcPath)
    $newWidth = $maxWidth
    $newHeight = [int]($img.Height * ($maxWidth / $img.Width))
    $bmp = New-Object System.Drawing.Bitmap($newWidth, $newHeight)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
    $g.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
    $g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
    $g.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
    $g.DrawImage($img, 0, 0, $newWidth, $newHeight)

    $encoder = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.FormatDescription -eq "JPEG" }
    $encoderParams = New-Object System.Drawing.Imaging.EncoderParameters(1)
    $encoderParams.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, [long]$quality)

    $bmp.Save($destPath, $encoder, $encoderParams)
    $g.Dispose()
    $bmp.Dispose()
    $img.Dispose()
    
    $origSize = (Get-Item $srcPath).Length
    $newSize = (Get-Item $destPath).Length
    Write-Host "[OPT] $srcPath : $origSize bytes -> $destPath : $newSize bytes"
}

$assets = @("tacoma_trd.jpg", "classic_bronco.jpg", "civic_sport.jpg", "hero_garage.jpg")

foreach ($a in $assets) {
    $src = "d:\Project01\assets\$a"
    $dst = "d:\Project01\assets\opt_$a"
    Optimize-Jpeg -srcPath $src -destPath $dst -maxWidth 900 -quality 82
}
