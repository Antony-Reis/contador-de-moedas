from ultralytics import YOLO


def main():
    modelo = YOLO('yolov8n')

    modelo.train(
    data="data.yaml",
    epochs=250,
    batch=4,
    imgsz=640,
    device=0,
    patience=50,
    cache=False,
    pretrained=True,
    workers=0,
    project="contador-de-moedas\yolo_runs",
    name="moedas2"
    )



if __name__ == "__main__":
    main()