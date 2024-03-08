color(red).
color(green).
color(yellow).
color(orange).
fruit(apple, red).
fruit(grape, green).
fruit(banana, yellow).
fruit(orange, orange).
get_fruit_color(Fruit, Color) :- fruit(Fruit, Color).
get_fruits_by_color(Color, Fruits) :-
    findall(Fruit, fruit(Fruit, Color), Fruits).
get_all_fruits(Fruits) :-
    findall(Fruit-Color, fruit(Fruit, Color), Fruits).
get_all_colors(Colors) :-
    findall(Color, color(Color), Colors).
