father(john, jim).
father(john, ann).
father(jim, jenny).
father(jim, alice).

ancestor(X, Y) :- father(X, Y).
ancestor(X, Y) :- father(X, Z), ancestor(Z, Y).

infer(Fact) :-
    ancestor(X, Y), \+ Fact = ancestor(X, Y), assertz(Fact), !.
