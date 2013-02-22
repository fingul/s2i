# coding=utf-8
import os
from PIL import Image, ImageDraw, ImageFont


def s2i(size,msg, fontsize=10):
    W, H = size#(100,100)
    #msg = "100"

    #http://nadiana.com/pil-tutorial-basic-advanced-drawing#Drawing_a_Rectangle
    im = Image.new("RGBA",(W,H))
    draw = ImageDraw.Draw(im)


    font = ImageFont.truetype("font/NanumGothic.ttf", fontsize)
    w, h = draw.textsize(msg,font=font)
    draw.text(((W-w)/2,(H-h)/2), msg, fill="black",font=font)
    border = 1
    draw_rect = (0, 0, W-border,H-border)
    draw.ellipse(draw_rect,outline="black")
    draw.rectangle(draw_rect,outline="black")
    return im

def main():
    p = '0.png'
    size = (100,100)

    msg = u'사랑해'#.encode('utf8')
    #msg = "7942"
    i = s2i(size,msg)
    i.save(p, "PNG")
    #os.startfile(p)

if __name__ == "__main__":
    main()