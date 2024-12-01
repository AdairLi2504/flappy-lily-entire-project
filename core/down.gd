extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"


# Called when the node enters the scene tree for the first time.
func _ready():
	var random = RandomNumberGenerator.new()
	random.randomize()
	var textrue = load("res://asset/mushroom/mushroom"+str(random.randi_range(0,10))+".png")
	$mushroom.texture = textrue
	$mushroom.position.y = 295 - random.randi_range(0,5)*70

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
