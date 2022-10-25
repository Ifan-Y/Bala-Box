import os
import shutil


# img_dir = 'D:\\AI_space\\for_test\\new'  # 图片位置
# label_dir = 'D:\\AI_space\\for_test\\txt'  # 数据集位置
# save_dir = 'D:\\AI_space\\for_test'  # 保存位置
# img_suffix = '.PNG'  # 图片格式
# label_suffix = '.txt'  # 数据集格式

def replaces(img_dir, label_dir, save_dir, img_suffix, label_suffix, start_num):
    print(img_suffix)
    print("1")


def replace(img_dir, label_dir, save_dir, img_suffix, label_suffix, start_num):
    # start_num = 1  # 开始数字

    img_paths = []
    img_names = []
    label_names = []
    for file in os.listdir(img_dir):
        img_file_path = os.path.join(img_dir, file)
        if not os.path.isdir(img_file_path):
            if os.path.splitext(img_file_path)[1] == img_suffix:
                img_names.append(os.path.splitext(file)[0])
                img_paths.append(img_file_path)

    for file in os.listdir(label_dir):
        label_file_dir = os.path.join(label_dir, file)
        if not os.path.isdir(label_file_dir):
            if os.path.splitext(file)[1] == label_suffix:
                label_names.append(os.path.splitext(file)[0])

    same_names = list(set(img_names) & set(label_names))

    if not os.path.exists(f"{save_dir}\\the_new_"):
        os.mkdir(f"{save_dir}\\the_new_")
    if not os.path.exists(f"{save_dir}\\the_new_\\imgs"):
        os.mkdir(f"{save_dir}\\the_new_\\imgs")
    if not os.path.exists(f"{save_dir}\\the_new_\\labels"):
        os.mkdir(f"{save_dir}\\the_new_\\labels")

    for name in same_names:
        img_act_path = f"{img_dir}\\{name}{img_suffix}"
        label_act_path = f"{label_dir}\\{name}{label_suffix}"
        img_final_path = f"{save_dir}\\the_new_\\imgs\\{start_num}{img_suffix}"
        label_final_path = f"{save_dir}\\the_new_\\labels\\{start_num}{label_suffix}"

        shutil.copyfile(img_act_path, img_final_path)
        shutil.copyfile(label_act_path, label_final_path)

        start_num += 1

    return 1

    # a = f"{img_dir}\\{same_names[0]}{img_suffix}"
    # b = f"{save_dir}\\the_new_\\imgs\\{same_names[0]}{img_suffix}"
    # print(a)
    # print(b)
    # shutil.copyfile(a, b)



