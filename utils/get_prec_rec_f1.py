from sklearn import metrics
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import os
import pandas as pd
import numpy as np


def calculate_model_ap_ar_af1(gt_path, gt_files, pred_path, obj_list=None, avg_typ='micro'):
    gt_dict = {}
    pred_dict = {}

    for fl in gt_files:
        gt_fl = os.path.join(gt_path, fl)
        pred_fl = os.path.join(pred_path, fl)

        if not os.path.exists(pred_fl):
            continue

        if obj_list:
            gt_data = pd.read_csv(gt_fl)

            gt_data = gt_data.transpose()
            gt_data.columns = [x__.lower() for x__ in gt_data.iloc[0]]
            gt_data = gt_data.reindex(columns=obj_list).iloc[1:].transpose().reset_index()

            pred_data = pd.read_csv(pred_fl)

            pred_data = pred_data.transpose()
            pred_data.columns = [x__.lower() for x__ in pred_data.iloc[0]]
            pred_data = pred_data.reindex(columns=obj_list).iloc[1:].transpose().reset_index()
            # print(gt_data)
            # print(pred_data)
        else:
            gt_data = pd.read_csv(gt_fl)
            gt_data.replace(-1, 1, inplace=True)
            pred_data = pd.read_csv(pred_fl)
            pred_data.replace(-1, 1, inplace=True)

        x = []
        for index, row in gt_data.iterrows():
            # if list(row)[0].strip().lower() in ["Sidewalk pits"]:
            #     continue
            if list(row)[0].strip().lower() in gt_dict.keys():
                gt_dict[list(row)[0].strip().lower()] += list(row)[1:]
            else:
                gt_dict[list(row)[0].strip().lower()] = list(row)[1:]

            x.append(len(list(row)[1:]))

        y = []
        for index, row in pred_data.iterrows():
            # if list(row)[0].strip().lower() in ["Sidewalk pits"]:
            #     continue
            if list(row)[0].strip().lower() in pred_dict.keys():
                pred_dict[list(row)[0].strip().lower()] += list(row)[1:]
            else:
                pred_dict[list(row)[0].strip().lower()] = list(row)[1:]
            y.append(len(list(row)[1:]))

        if x != y:
            print(len(x), len(y), fl)

    target_array = []
    pred_array = []

    label_names = []

    for key in gt_dict.keys():
        if key in pred_dict.keys():
            if obj_list:
                if key not in obj_list:
                    continue
            if len(gt_dict[key]) == len(pred_dict[key]):
                target_array.append(gt_dict[key])
                pred_array.append(pred_dict[key])
                label_names.append(key)
            else:
                print(len(gt_dict[key]), len(pred_dict[key]), key)

    target_array = np.array(target_array).T
    pred_array = np.array(pred_array).T

    # print(target_array.shape)

    # try:
    if pred_path.endswith('GT_N'):
        precs = precision_score(target_array, pred_array, average=avg_typ)
        recs = recall_score(target_array, pred_array, average=avg_typ)
        f1ss = f1_score(target_array, pred_array, average=avg_typ)
    else:
        precs = precision_score(target_array, pred_array, average=avg_typ)
        recs = recall_score(target_array, pred_array, average=avg_typ)
        f1ss = f1_score(target_array, pred_array, average=avg_typ)
    # except Exception as e:
    #     # ap = 0
    #     print(e)
    #     precs = 0.0
    #     recs = 0.0
    #     f1ss = 0.0

    frm_wise_pn_s = (2 * target_array) - pred_array

    return precs, recs, f1ss, frm_wise_pn_s