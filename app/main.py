import bottle
import os
import random
import astar
import numpy as np

@bottle.route('/')
def static():
    return "the server is running"


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data.get('game_id')
    board_width = data.get('width')
    board_height = data.get('height')

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#0000FF',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url
    }


@bottle.post('/move')
def move():
	data = bottle.request.json
	
    # TODO: Do things with data
    
	directions = ['up', 'down', 'left', 'right']
	direction = random.choice(directions)
	createMap(data)
	print direction
	return {
        'move': direction,
        'taunt': 'battlesnake-python!'
    }

#Creates a map of the game board from data
#Call on each move
def createMap(data):
	map =[[0 for x in range(board_width)] for y in range(board_height)] 
	for snake in data['snakes']:
		for data in snake['data']['body']['data']:
			map[data.x, data.y] = WALL
			
	print np.matrix(map);
	return map
# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
