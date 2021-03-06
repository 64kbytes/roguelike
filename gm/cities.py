class City(object):
	def create_dungeon(self, width, height):
		global PLAYER_XYZ
		
		rooms = []
		num_rooms = 0
	
		for r in range(self.max_rooms):
			#random width and height
			w = random.randint(self.room_min_size, self.room_max_size)
			h = random.randint(self.room_min_size, self.room_max_size)
			#random position without going out of the boundaries of the map
			x = random.randint(0, width - w - 1)
			y = random.randint(0, height - h - 1)

			#"Rect" class makes rectangles easier to work with
			new_room = Rect(x, y, w, h)

			#run through the other rooms and see if they intersect with this one
			failed = False
			for other_room in rooms:
				if new_room.intersect(other_room):
					failed = True
					break
		    
			if not failed:
				self.create_room(new_room)
				(new_x, new_y) = new_room.center()
				LIGHTS.append((new_x, new_y))
				if num_rooms == 0:
					PLAYER_XYZ = (new_x, new_y, 0)
				else:
					(prev_x, prev_y) = rooms[num_rooms-1].center()
					if random.randint(0, 1) == 1:
						self.create_h_tunnel(prev_x, new_x, prev_y)
						self.create_v_tunnel(prev_y, new_y, new_x)
					else:
						self.create_v_tunnel(prev_y, new_y, prev_x)
						self.create_h_tunnel(prev_x, new_x, new_y)
				rooms.append(new_room)
				num_rooms += 1
				
	def create_room(self, room):
		#go through the tiles in the rectangle and make them passable
		for y in range(room.y1 + 1, room.y2):
			for x in range(room.x1 + 1, room.x2):
				self.terrain[y][x].blocked = False
				self.terrain[y][x].block_sight = False
	
	def create_h_tunnel(self, x1, x2, y):
		#horizontal tunnel. min() and max() are used in case x1>x2
		for x in range(min(x1, x2), max(x1, x2) + 1):
			self.terrain[y][x].blocked = False
			self.terrain[y][x].block_sight = False
	
	def create_v_tunnel(self, y1, y2, x):
		#vertical tunnel
		for y in range(min(y1, y2), max(y1, y2) + 1):
			self.terrain[y][x].blocked = False
			self.terrain[y][x].block_sight = False
