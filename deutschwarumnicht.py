import urllib.request

audioformatstring = "http://radio-download.dw.com/Events/dwelle/deutschkurse/deutschwarumnicht/serie{0}/eng/DWN_Englisch_Serie{0}_Lektion{1:0>2}_dwdownload.mp3"

for series in range (1, 5):
    for ep in range(1, 26 + 1):
        print(audioformatstring.format(series, ep))
        urllib.request.urlretrieve(audioformatstring.format(series, ep), "DWM_S{0}E{1:0>2}.mp3".format(series, ep))
