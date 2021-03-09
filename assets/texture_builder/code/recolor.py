import numpy
import os
from PIL import Image as img

#Global Vars:
PARENT_DIRECTORY = os.path.abspath(os.path.join(os.getcwd(), os.pardir,"kestral","assets","texture_builder"))
COLORING = {(255,0,0,255):0,
            (0,255,0,255):1,
            (0,0,255,255):2,
            (255,255,255,255):3,
            (191,0,0,255):4,
            (0,191,0,255):5,
            (0,0,191,255):6,
            (191,191,191,255):7,
            (127,0,0,255):8,
            (0,127,0,255):9,
            (0,0,127,255):10,
            (127,127,127,255):11,
            (63,0,0,255):12,
            (0,63,0,255):13,
            (0,0,63,255):14,
            (63,63,63,255):15}

def recolor(width,height,file,save_as,recolor_to):
	file_path = os.path.join(PARENT_DIRECTORY,file)
	save_path = os.path.join(PARENT_DIRECTORY,save_as)
	starting_image = img.open(file_path)
	pixels = starting_image.load()

	for y in range(height):
		for x in range(width):
			if pixels[x,y] != (0,0,0,0):
				starting_image.putpixel((x,y),recolor_to[COLORING[pixels[x,y]]])
	
	starting_image.save(save_path)

def layer(files,save_as):
	base = img.open(os.path.join(PARENT_DIRECTORY,files[0]))
	save_path = os.path.join(PARENT_DIRECTORY,save_as)

	for filen in range(len(files)-1):
		layer = img.open(os.path.join(PARENT_DIRECTORY,files[filen+1]))
		base.paste(layer,(0,0),layer)
	base.save(save_path)


recolor(8,8,os.path.join("designs","base","stone.png"),os.path.join("designs","intermediate","stone.png"),[(125,125,125),(132,132,132),(138,138,138),(148,148,148)])
recolor(8,8,os.path.join("designs","base","ore.png"),os.path.join("designs","intermediate","ore.png"),[(127,255,255),(191,255,255)])
layer([os.path.join("designs","intermediate","stone.png"),os.path.join("designs","intermediate","ore.png")],os.path.join("final_textures","diamond_ore.png"))