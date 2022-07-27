import cv2
import os

def save_pic():
    # 得到存储的路径和源文件的路径
    save_path = r'F:\Dataset\color AR face images'
    images_path = r'F:\Dataset\color AR face images\color AR face images'

    # for i in range(100):
    # 新建100个文件夹用来存储，foder_name为文件路径＋后缀（顺序）
    #     foder_name = os.path.join(save_path, str(i+1))
    #     print(foder_name)
    #   创建文件夹
    #     os.mkdir(foder_name)

    for i in range(2600):
        # 得到每张图片的名字
        img_name = str(i+1) + '.bmp'
        # 图片的路径等于文件夹路径+文件名
        img_path = os.path.join(images_path, img_name)

        # print(img_name)
        # 将每一张图片以矩阵的形式存储到img中
        img = cv2.imread(img_path)
        # 得到存储路径
        img_save_path = os.path.join(save_path, str(i//26 + 1))
        print(img_save_path)
        # 每个小文件夹中的存储路劲
        img_save_path = os.path.join(img_save_path, str(i%26 + 1) + '.bmp')
        print(img_save_path)
        # 将图片放进文件夹中
        cv2.imwrite(img_save_path, img)

def select_pic():
    save_path = r'C:\Users\endless\Desktop\pic'

    # for i in range(100):
    #     foder_name = os.path.join(save_path, str(i+1))
    #     print(foder_name)
    #     os.mkdir(foder_name)
    for i in range(100):
        for j in range(4):
            images_path = r"F:\Dataset\color AR face images"
            images_path = os.path.join(images_path, str(i+1))
            img_name = str(j + 1) + '.bmp'
            img_path = os.path.join(images_path, img_name)
            img = cv2.imread(img_path)
            img_save_path = os.path.join(save_path, str(i+1))
            print(img_save_path)
            img_save_path = os.path.join(img_save_path, str(j+1) + '.bmp')
            print(img_save_path)
            cv2.imwrite(img_save_path, img)






if __name__ == '__main__':
    # save_pic()
    select_pic()