from PIL import Image
def image(img,frame)
    # img = Image.open("images/cat.png")
    # frame = Image.open("images/frame.png")

    resized_frame = frame.resize((img.width, img.height))

    img.paste(resized_frame, (0, 0), resized_frame)

    return img.save("images/out.png")

