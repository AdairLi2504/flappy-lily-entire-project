extends Node

export(PackedScene) var obstalce_scene
export(PackedScene) var ground_scene


# Called when the node enters the scene tree for the first time.
func _ready():
	new_game()

func new_game():
	for i in range(4):
		gen_ground(i*280)
	gen_obstalce(1120)
	$ScoreTimer.start()
	$LilyWhite.show()
	$LilyWhite.position.x = 360
	$LilyWhite.position.y = 540
	$LilyWhite.onGame = true
	
func gen_ground(pos_x:int):
	var ground = ground_scene.instance()
	ground.position.x = pos_x
	add_child(ground)

func gen_obstalce(pos_x:int):
	var obstalce = obstalce_scene.instance()
	obstalce.position.x = pos_x 
	add_child(obstalce)

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass

	
func terrain_go_out_window(node):
	var childernObstacle:Array 
	for i in get_children():
		if i.name.match("*Obstacle*"):
			childernObstacle.append(i)
	var lastNode
	if len(childernObstacle) == 0:
		lastNode = get_node("@Ground@4")
	else:
		lastNode = childernObstacle[len(childernObstacle)-1]
	gen_obstalce(lastNode.position.x+280)
