import os
import csv
import glob
import pandas as pd

img_width = 4056
img_height = 2280

classes = ["ong_noi", "khoa_neo", "tru_su"]

def data_set(AnnotationPath: str):
    dataList = []
    cnt = 0
    xml_path = glob.glob(os.path.join(AnnotationPath, "*.xml"))  #lay cac file co duoi .xml tu path ra
    for xml_File in xml_path:
        with open(xml_File, 'r') as fp:
            for p in fp:
                if '<filename>' in p:
                    fileName = p.split('>')[1].split('<')[0]
                if '<object>' in p:
                    d = [next(fp).split('>')[1].split('<')[0] for _ in range(9)]  # category

                    strType = d[0]
                    # bounding box
                    xmin = int(d[-4])  # xmin
                    ymin = int(d[-3])  # ymin
                    xmax = int(d[-2])  # xmax
                    ymax = int(d[-1])  # ymax
                    labels = classes.index(strType)

                    # convert yolo dataframe
                    width = xmax - xmin
                    height = ymax - ymin
                    x_center = int(xmin + width / 2)
                    y_center = int(ymin + height / 2)

                    # normalized data [0,1]
                    w_norm = width / img_width
                    h_norm = height / img_height
                    x_center_norm = x_center / img_width
                    y_center_norm = y_center / img_height
                    filename = str(cnt) + '.jpg'

                    dataList.append([os.path.join(fileName), filename, strType, xmin, ymin, xmax, ymax, labels, width,
                                      height, x_center, y_center, x_center_norm, y_center_norm, w_norm, h_norm])
        cnt += 1

    df = pd.DataFrame(dataList,columns=[ 'prev_filename', 'filename', 'strType', 'xmin', 'ymin', 'xmax', 'ymax',
                                         'labels', 'width', 'height', 'x_center', 'y_center', 'x_center_norm',
                                         'y_center_norm', 'w_norm', 'h_norm'])
    df.to_csv(r'Meta_data\grid_box_detection.csv', index= False)

if __name__ == '__main__':
    AnnotationPath = "data/Annotations"
    data_set(AnnotationPath)
    print("End program")