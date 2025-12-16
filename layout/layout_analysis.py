import layoutparser as lp
import cv2

def analyze_layout(image_path):
    image = cv2.imread(image_path)
    model = lp.Detectron2LayoutModel(
        config_path="lp://PubLayNet/faster_rcnn_R_50_FPN_3x/config",
        label_map={0:"Text",1:"Title",2:"List",3:"Table",4:"Figure"}
    )
    layout = model.detect(image)
    return layout
