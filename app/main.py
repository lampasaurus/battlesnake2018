import bottle
import os
import random

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
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url
    }


@bottle.post('/move')
def move():
	data = bottle.request.json
	for snek in data['snakes']['data']:
		if snek['id'] == snake_id:
			my_snake = snek
			head = my_snake['body']['data'][0]
	print head
	# TODO: Do things with data
	
	directions = ['up', 'down', 'left', 'right']
	direction = random.choice(directions)
	print direction
	map = createMap(data)
	return {
		'move': direction,
		'taunt': 'battlesnake-python!'
	}

def createMap(data):
	map =[[0 for x in range(data['width'])] for y in range(data['height'])] 
	for snake in data['snakes']['data']:
		for coord in snake['body']['data']:
			map[coord['y']][coord['x']] = WALL
	return map

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '0.0.0.0'),
        port=os.getenv('PORT', '8080'),
        debug = True)
