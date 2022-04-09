from point import Point

def possible_route(start_point, end_point):
  possible_x_plots = list(range(start_point.x+1, end_point.x+1)) if(start_point.x < end_point.x) else list(reversed(range(end_point.x, start_point.x)))
  possible_x_points = [Point([x, start_point.y]) for x in possible_x_plots]

  possible_y_plots = list(range(start_point.y+1, end_point.y+1)) if(start_point.y < end_point.y) else list(reversed(range(end_point.y, start_point.y)))
  possible_y_points = [Point([end_point.x, y]) for y in possible_y_plots]
  return possible_x_points + possible_y_points

def check_whether_collapse(monster_position, adventure_route):
  for route in adventure_route:
    if(route.x == monster_position.x and route.y == monster_position.y):
      return True
  return False

def find_collision(adventure_route, monster_route):
  while(monster_route and adventure_route):
    adventure_route = adventure_route[1:]
    is_collapsed = check_whether_collapse(monster_route[0], adventure_route)
    monster_route = monster_route[1:]
    if is_collapsed: return is_collapsed
  return False

dimentions = Point([int(i) for i in input("Dimensions of the dungeon(Row x Column): ").split()])

adventurer = Point([int(i) for i in input("Position of adventurer:").split()])

monster = Point([int(i) for i in input("Position of monster: ").split()])

trigger = Point([int(i) for i in input("Position of trigger: ").split()])

gold = Point([int(i) for i in input("Position of gold: ").split()])


possible_plots_for_adventure = possible_route(adventurer, gold)
possible_plots_for_monster = possible_route(monster, gold)


if(len(possible_plots_for_adventure) > len(possible_plots_for_monster) or find_collision(possible_plots_for_adventure, possible_plots_for_monster)):
  print("Only way is to use Triggers")
  adventurer_to_trigger = possible_route(adventurer, trigger)
  trigger_to_adventure = possible_route(trigger, gold)
  possible_plots_for_adventure = adventurer_to_trigger + trigger_to_adventure


print(f"Minimum number of steps: {len(possible_plots_for_adventure)}")
print("Path: {initial_path} -> {path}".format(initial_path = f"({adventurer.x}, {adventurer.y})", path = " -> ".join(list(map(lambda r: f"({r.x}, {r.y})",possible_plots_for_adventure)))))