import os

def mergeCAF(x,path):
    os.system("git fetch "+x)
    os.system("git merge --signoff --no-commit -X subtree="+path+" FETCH_HEAD")
    mas = path+": Merge "+tag
    os.system("git commit -s -m '"+mas+"'")

tag = input("Enter tag: ")
audio = "https://source.codeaurora.org/quic/la/platform/vendor/opensource/audio-kernel "+tag
camera = "https://source.codeaurora.org/quic/la/platform/vendor/opensource/camera-kernel/ "+tag
display = "https://source.codeaurora.org/quic/la/platform/vendor/opensource/display-drivers/ "+tag
video = "https://source.codeaurora.org/quic/la/platform/vendor/opensource/video-driver/ "+tag
qcacld = "https://source.codeaurora.org/quic/la/platform/vendor/qcom-opensource/wlan/qcacld-3.0/ "+tag
fwapi = "https://source.codeaurora.org/quic/la/platform/vendor/qcom-opensource/wlan/fw-api/ "+tag
qcacmn = "https://source.codeaurora.org/quic/la/platform/vendor/qcom-opensource/wlan/qca-wifi-host-cmn/ "+tag

mergeCAF(qcacld,"drivers/staging/qcacld-3.0")
mergeCAF(fwapi,"drivers/staging/fw-api")
mergeCAF(qcacmn,"drivers/staging/qca-wifi-host-cmn")
