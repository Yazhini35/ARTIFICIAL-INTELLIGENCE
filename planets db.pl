planet(mercury, 0.39, 0.33).
planet(venus, 0.72, 4.87).
planet(earth, 1, 5.97).
planet(mars, 1.52, 0.641).
planet(jupiter, 5.20, 1898).
planet(saturn, 9.58, 568).
planet(uranus, 19.18, 86.8).
planet(neptune, 30.07, 102).
planet(pluto, 39.48, 0.0146).


smaller(X, Y) :-
    planet(X, DistanceX, _),
    planet(Y, DistanceY, _),
    DistanceX < DistanceY.

larger(X, Y) :-
    planet(X, DistanceX, _),
    planet(Y, DistanceY, _),
    DistanceX > DistanceY.

mass(X, Mass) :- planet(X, _, Mass).
