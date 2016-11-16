from django.shortcuts import render

def index(request):
	return render(request, 'dninjas/index.html')


def indies(request, id):
	colors = {
		"orange": "dninja/images/orange_turt.jpg",
		"blue" : "dninja/images/blue_turt.jpeg",
		"red":"dninja/images/red_turt.jpeg",
		"purple":"dninja/images/purple_turt.png"
	}
	if id in colors:
		newcolor = colors[id]
	else:
		newcolor = "dninja/images/viggo.jpeg"

	context = {
		"id": id,
		"pic": newcolor
	}
	
	return render(request, 'dninjas/visitall.html', context)

def allturtles(request):
	newallcolors = "dninja/images/all_turt.jpeg"
	
	context = {
	
		"pic": newallcolors,
	}
	return render(request, 'dninjas/visitall.html', context)