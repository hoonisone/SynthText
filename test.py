import h5py
from PIL import Image
# SynthText.h5 파일 열기
with h5py.File("./results/SynthText.h5", "r") as f:
    # 데이터셋 목록 출력
    print("Datasets in SynthText.h5:", list(f.keys()))

    # 데이터셋 내용 출력
    data = f["data"]
    for name in data:
        x = data[name]
        image = Image.fromarray(x[:])
        image.save("image.png")
