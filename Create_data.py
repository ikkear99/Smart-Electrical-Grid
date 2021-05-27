import os, shutil
import pandas as pd
from sklearn import model_selection
import numpy as np

image_Set = "data/JPGImages"
Annotations = "data/Annotations" #.xml
csv_path = "Meta_data/grid_cell_detection.csv"

def segregate_data(df, img_path, labels_path, train_img_path, train_labels_path ):
    filenames = []
    for filename in df.filename:
        filenames.append(filename)

    filenames = set(filenames)
    for filename in filenames:
        yolo_list = []

        for _, row in df[df.filename == filename].iterrows():
            yolo_list.append([row.labels, row.x_center_norm, row.y_center_norm, row.w_norm, row.h_norm])

        yolo_list = np.array(yolo_list)

        txt_filename = os.path.join(train_labels_path, str(row.prev_filename.split('.')[0]) + ".txt")

        # Save the .img & .txt files to the corresponding train and validation folders
        np.savetxt(txt_filename, yolo_list, fmt=["%d", "%f", "%f", "%f", "%f"])

        shutil.copyfile(os.path.join(img_path, row.prev_filename), os.path.join(train_img_path, row.prev_filename))


if __name__ == '__main__':
    src_img_path = "data/JPGImages/"
    src_label_path = "data/Annotations/"

    train_img_path = "Meta_data/images/train"
    train_label_path = "Meta_data/labels/train"

    valid_img_path = "Meta_data/images/valid"
    valid_label_path = "Meta_data/labels/valid"

    df = pd.read_csv("Meta_data/grid_cell_detection.csv")

    df_train, df_valid = model_selection.train_test_split(df, test_size=0.2, random_state=21, shuffle=True)
    print(df_train.shape, df_valid.shape)

    segregate_data(df_train, src_img_path, src_label_path, train_img_path, train_label_path)
    segregate_data(df_valid, src_img_path, src_label_path, valid_img_path, valid_label_path)

    print("Number of Training images", len(os.listdir('Meta_data/images/train')))
    print("Number of Training labels", len(os.listdir("Meta_data/labels/train")))

    print("Number of valid images", len(os.listdir("Meta_data/images/valid")))
    print("Number of valid labels", len(os.listdir("Meta_data/labels/valid")))
