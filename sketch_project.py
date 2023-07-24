# This Is The Sketchpy inbuilt function
from sketchpy import library
my_pro=library.flag()
my_pro.draw()

# This Is The Sketchpy Project
from sketchpy import canvas
user = canvas.sketch_from_image(r"D:\virat kohli.jpg")
user.draw()


# this code is another type,this only for user want to sketch tha images.so,user can put the input.
# *note...>this code is not paint all kind of images

from sketchpy import canvas
out= canvas.sketch_from_image(input("Enter Input:"))
out.draw()




