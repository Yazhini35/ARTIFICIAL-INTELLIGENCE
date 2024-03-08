bird(canary).
bird(robin).
bird(ostrich).
bird(penguin).

can_fly(canary).
can_fly(robin).
cannot_fly(ostrich).
cannot_fly(penguin).

can_fly_bird(X) :-
  bird(X),
  can_fly(X),
  write(X), write(' can fly'), nl.

cannot_fly_bird(X) :-
  bird(X),
  cannot_fly(X),
  write(X), write(' cannot fly'), nl.

:- initialization(main).

main :-
  can_fly_bird(X),
  fail.
  
main :-
  cannot_fly_bird(Y),
  fail.
