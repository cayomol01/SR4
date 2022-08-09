from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import flat, gourad

width = 1024
height = 800

rend = Renderer(width, height)

rend.active_shader = flat
rend.active_texture = Texture("model.bmp")

rend.glLoadModel("bull.obj",
                 translate = V3(width/2, height/2, 0),
                 rotate = V3(0, 180, 0),
                 scale= V3(15, 15, 15))
rend.glFinish("output.bmp")