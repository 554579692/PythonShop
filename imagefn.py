from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
# from skimage import img_as_float
# import matplotlib.pyplot as plt
# from skimage import io
import random
import numpy as np

import os
import cv2

def imageenhancebrightness(img_path,n,flag):  #亮度
    im = Image.open(img_path)
    n=n/100
    om = ImageEnhance.Brightness(im)
    if(flag==1):
        om.enhance(1+n).save("img/copy1.jpg")
    else:
        om.enhance(1+n).save("img/copy0.jpg")

def imageenhancecontrast(img_path,n,flag):    #对比度
    im = Image.open(img_path)
    n=n/120
    om = ImageEnhance.Contrast(im)
    if(flag==1):
        om.enhance(1+n).save("img/copy1.jpg")
    else:
        om.enhance(1+n).save("img/copy0.jpg")

def imageenhancesharpness(img_path,n,flag):    #锐度
    im = Image.open(img_path)
    n=n/50
    om = ImageEnhance.Sharpness(im)
    if(flag==1):
        om.enhance(1+n).save("img/copy1.jpg")
    else:
        om.enhance(1+n).save("img/copy0.jpg")

def imageenhancecolor(img_path,n,flag):    #色彩平衡
    im = Image.open(img_path)
    n=n/100
    om = ImageEnhance.Color(im)
    if(flag==1):
        om.enhance(1+n).save("img/copy1.jpg")
    else:
        om.enhance(1+n).save("img/copy0.jpg")

    def temperature(img_path,n,flag):
        im = Image.open(img_path)
        width = im.size[0]
        height = im.size[1]
        im = im.convert('RGB')
        array = []
        k=0
        for x in range(width):
            for y in range(height):
                r, g, b = im.getpixel((x,y))
                rgb = (r, g, b)
                array.append(rgb)
        for x in range(width):
            for y in range(height):
                im.putpixel((x, y), (int((array[k][0]+1.5*n)/2), int((array[k][1]+n)/2), int((array[k][2]+n)/2)))
                k +=1
        if (flag == 1):
            im.save("img/copy1.jpg")
        else:
            im.save("img/copy0.jpg")
def imageenhancesmoothness(img_path,n,flag):
    img = cv2.imread(img_path)
    img1 = cv2.bilateralFilter(src=img, d=0, sigmaColor=n, sigmaSpace=15)
    if(flag==1):
        cv2.imwrite("img/copy1.jpg",img1)
    else:
        cv2.imwrite("img/copy0.jpg",img1)

def imageenhancered(img_path,n,flag):
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k=0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x,y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            b = 255-int(array[k][0])
            if n>0:
                a = int((b/99)*n)
            if n<=0:
                a = int(((b-255)/99)*n)
            im.putpixel((x, y), (int(array[k][0]+a), int(array[k][1]), int(array[k][2])))
            k +=1
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")
def imageenhancegreen(img_path,n,flag):
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k=0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x,y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            b = 255-int(array[k][1])
            if n>0:
                a = int((b/99)*n)
            if n<=0:
                a = int(((b-255)/99)*n)
            im.putpixel((x, y), (int(array[k][0]), int(array[k][1]+a), int(array[k][2])))
            k +=1
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")

def imageenhanceblue(img_path,n,flag):
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k=0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x,y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            b = 255-int(array[k][2])
            if n>0:
                a = int((b/99)*n)
            if n<=0:
                a = int(((b-255)/99)*n)
            im.putpixel((x, y), (int(array[k][0]), int(array[k][1]), int(array[k][2]+a)))
            k +=1
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")


def default_1(img_path,flag):    #ins风格
    im = Image.open(img_path)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(0.5)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(1.5)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(5)
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")

def default_2(img_path,flag):    #浅白
    im = Image.open(img_path)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(0.8)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(0.8)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(2.0)
    if(flag==1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")


def default_3(img_path, flag):  # 日系
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 209) / 2), int((array[k][1] + 238) / 2), int((array[k][2] + 238) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if(flag==1):
        enh.enhance(2).save("img/copy1.jpg")
    else:
        enh.enhance(2).save("img/copy0.jpg")

def default_4(img_path, flag):  # 西柚
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 225) / 2), int((array[k][1] + 228) / 2), int((array[k][2] + 225) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(2).save("img/copy1.jpg")
    else:
        enh.enhance(2).save("img/copy0.jpg")


def default_5(img_path, flag):  #小森林
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 240) / 2), int((array[k][1] + 255) / 2), int((array[k][2] + 240) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(100)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(3).save("img/copy1.jpg")
    else:
        enh.enhance(3).save("img/copy0.jpg")


def default_6(img_path, flag):  # 氧气
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 240) / 2), int((array[k][1] + 248) / 2), int((array[k][2] + 255) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(1.8)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(1.5)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(2).save("img/copy1.jpg")
    else:
        enh.enhance(2).save("img/copy0.jpg")


def default_7(img_path, flag):  # 樱花
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 255) / 2), int((array[k][1] + 192) / 2), int((array[k][2] + 203) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")


def default_8(img_path, flag):  # 芝士
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 255) / 2), int((array[k][1] + 239) / 2), int((array[k][2] + 213) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(3)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")


def default_9(img_path, flag):  # 冰激凌
    im = Image.open(img_path)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(0.5)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(1.8)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(1)
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")


def default_10(img_path, flag):  # 复古
    im = Image.open(img_path)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(1.8)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(1.2)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(1)
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")


def default_11(img_path, flag):  # 果酱
    im = Image.open(img_path)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(0.8)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(1.8)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(1)
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")


def default_12(img_path, flag):  # 桔梗
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 255) / 2), int((array[k][1] + 218) / 2), int((array[k][2] + 185) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.8)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(1.8)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")


def default_13(img_path, flag):  # 白茶
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 238) / 2), int((array[k][1] + 210) / 2), int((array[k][2] + 238) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")


def default_14(img_path, flag):  # 珍珠
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 255) / 2), int((array[k][1] + 182) / 2), int((array[k][2] + 193) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(4)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")


def default_15(img_path, flag):  # 海盐
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 230) / 2), int((array[k][1] + 230) / 2), int((array[k][2] + 250) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")


def default_16(img_path, flag):  # 黄油
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 255) / 2), int((array[k][1] + 248) / 2), int((array[k][2] + 220) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(2).save("img/copy1.jpg")
    else:
        enh.enhance(2).save("img/copy0.jpg")


def default_17(img_path, flag):  # 质感
    im = Image.open(img_path)
    enh = ImageEnhance.Contrast(im)
    im = enh.enhance(0.9)
    enh = ImageEnhance.Color(im)
    im = enh.enhance(1.5)
    enh = ImageEnhance.Sharpness(im)
    im = enh.enhance(5)
    if (flag == 1):
        im.save("img/copy1.jpg")
    else:
        im.save("img/copy0.jpg")


def default_18(img_path, flag):  # 蜜桃
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 255) / 2), int((array[k][1] + 218) / 2), int((array[k][2] + 185) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(4)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1.2).save("img/copy1.jpg")
    else:
        enh.enhance(1.2).save("img/copy0.jpg")


def default_19(img_path, flag):  # 奶油
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 191) / 2), int((array[k][1] + 239) / 2), int((array[k][2] + 255) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.9)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(1).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")


def default_20(img_path, flag):  # 葡萄
    im = Image.open(img_path)
    width = im.size[0]
    height = im.size[1]
    im = im.convert('RGB')
    array = []
    k = 0
    for x in range(width):
        for y in range(height):
            r, g, b = im.getpixel((x, y))
            rgb = (r, g, b)
            array.append(rgb)
    for x in range(width):
        for y in range(height):
            im.putpixel((x, y),
                        (int((array[k][0] + 255) / 2), int((array[k][1] + 187) / 2), int((array[k][2] + 255) / 2)))
            k += 1
    enh = ImageEnhance.Brightness(im)
    enh.enhance(0.8)
    enh = ImageEnhance.Sharpness(im)
    enh.enhance(2)
    enh = ImageEnhance.Color(im)
    if (flag == 1):
        enh.enhance(4).save("img/copy1.jpg")
    else:
        enh.enhance(1).save("img/copy0.jpg")

def default_21(img_path, flag):  # 颜色交换
    im = Image.open(img_path)
    r,g,b=im.split()
    om=Image.merge("RGB",(b,g,r))
    if (flag == 1):
        om.save("img/copy1.jpg")
    else:
        om.save("img/copy0.jpg")

def default_22(img_path, flag):  #模糊
    im = Image.open(img_path)
    om = im.filter(ImageFilter.BLUR)
    if (flag == 1):
        om.save("img/copy1.jpg")
    else:
        om.save("img/copy0.jpg")

def default_23(img_path, flag):  #去色
    im = Image.open(img_path)
    om=im.convert('L')
    if (flag == 1):
        om.save("img/copy1.jpg")
    else:
        om.save("img/copy0.jpg")

def default_24(img_path, flag):  #提取边界
    im = Image.open(img_path)
    om = im.filter(ImageFilter.EMBOSS)
    if (flag == 1):
        om.save("img/copy1.jpg")
    else:
        om.save("img/copy0.jpg")

def default_25(img_path, flag):  #马赛克
    img = io.imread(img_path)
    img = img_as_float(img)
    img_out = img.copy()
    row, col, channel = img.shape
    half_patch = 10
    for i in range(half_patch, row - 1 - half_patch, half_patch):
        for j in range(half_patch, col - 1 - half_patch, half_patch):
            k1 = random.random() - 0.5
            k2 = random.random() - 0.5
            m = np.floor(k1 * (half_patch * 2 + 1))
            n = np.floor(k2 * (half_patch * 2 + 1))
            h = int((i + m) % row)
            w = int((j + n) % col)
            img_out[i - half_patch:i + half_patch, j - half_patch:j + half_patch, :] = \
                img[h, w, :]
    plt.figure(1)
    plt.imshow(img)
    plt.axis('off')
    plt.figure(2)
    plt.imshow(img_out)
    plt.axis('off')
    if (flag == 1):
        plt.savefig("img/copy1.jpg")
    else:
        plt.savefig("img/copy0.jpg")

