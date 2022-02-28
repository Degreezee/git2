from PIL import Image
new = Image.new(mode="RGBA", size=(4, 4), color="#aa1155")
new.show()
new.save("xxx.png")