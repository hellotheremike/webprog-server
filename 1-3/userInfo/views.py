from django.http import HttpResponse
from PIL import Image, ImageDraw, ImageFont
from time import gmtime, strftime
import random

def index(request):
	INK = "#E01B6A", "#44A2C9", "#BEC944", "#E8BC43"
	today = strftime("%A, %d %b %Y %H:%M:%S", gmtime())
	image = Image.new("RGB", (300, 100), random.choice(INK))
	draw = ImageDraw.Draw(image)
	draw.text((50, 45), today)
	response = HttpResponse(mimetype="image/png")
	image.save(response, "PNG")
	return response