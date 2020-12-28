# -*- coding: utf-8 -*-

if __name__ == "__main__":

    # 图片转numpy数组
    img_path = "/Users/yunba/Downloads/tupian/260820200206zip.jpg"
    # img_data = cv2.imread(img_path)

    # 以 二进制方式 进行图片读取
    with open(img_path,"rb") as f:
        img_bin = f.read() # 内容读取

    print(img_bin)

    # 将 图片的二进制内容 转成 真实图片
    # with open("img.jpg","wb") as f:
    #     f.write(img_bin) # img_bin里面保存着 以二进制方式读取的图片内容,当前目录会生成一张img.jpg的图片
