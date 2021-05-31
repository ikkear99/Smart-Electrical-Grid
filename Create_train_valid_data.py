import os, shutil
import pandas as pd
import glob
import numpy as np
from sklearn import model_selection

def create(csv_path, img_path, img_save_path, label_save_path):
    df = pd.read_csv(csv_path)
    print(df.shape)
    filenames = []
    for filename in df.filename:
        filenames.append(filename)

    for filename in filenames:
        yolo_list = []

        for _, row in df[df.filename == filename].iterrows():
            yolo_list.append([row.labels, row.x_center_norm, row.y_center_norm, row.w_norm, row.h_norm])

        yolo_list = np.array(yolo_list)

        txt_filename = os.path.join(label_save_path, str(row.prev_filename.split('.')[0]) + ".txt")

        # Save the .img & .txt files to the corresponding train and validation folders
        np.savetxt(txt_filename, yolo_list, fmt=["%d", "%f", "%f", "%f", "%f"])
        shutil.copyfile(os.path.join(img_path, row.prev_filename), os.path.join(img_save_path, row.prev_filename))

def num_label(path):
    dem = 0
    txt_path = glob.glob(os.path.join(path, "*.txt"))
    for txt_File in txt_path:
        f = open(txt_File, 'r')
        while f.readline() != "":
            dem = dem + 1
    print(dem)


if __name__ == '__main__':

    data_csv_path = "Meta_data/grid_box_detection.csv"
    df = pd.read_csv(data_csv_path)
    df_train, df_valid = model_selection.train_test_split(df, test_size=0.1, random_state=13, shuffle=True)
    print(df_train.shape, df_valid.shape)

    train_csv_path = "Meta_data/train.csv"
    valid_csv_path = "Meta_data/valid.csv"

    df_train.to_csv(train_csv_path, index=False)
    df_valid.to_csv(valid_csv_path, index=False)

    train_img_path = "Meta_data/images/train"
    train_labels_path = "Meta_data/labels/train"

    valid_img_path = "Meta_data/images/valid"
    valid_labels_path = "Meta_data/labels/valid"

    img_path = "data/JPGImages"

    create(train_csv_path, img_path, train_img_path, train_labels_path)
    create(valid_csv_path, img_path, valid_img_path, valid_labels_path)

    print("Number of Training images", len(os.listdir('Meta_data/images/train')))
    print("Number of Training labels", len(os.listdir("Meta_data/labels/train")))

    print("Number of valid images", len(os.listdir("Meta_data/images/valid")))
    print("Number of valid labels", len(os.listdir("Meta_data/labels/valid")))

# (715, 16) (80, 16)
# (715, 16)
# (80, 16)
# Number of Training images 245
# Number of Training labels 245
# Number of valid images 69
# Number of valid labels 69