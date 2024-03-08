male(john).
male(harry).
male(bob).
male(david).
male(james).

female(sarah).
female(lily).
female(emma).
female(rachel).

parent(john, harry).
parent(john, bob).
parent(sarah, harry).
parent(sarah, bob).
parent(harry, lily).
parent(harry, emma).
parent(emma, james).
parent(james, david).
parent(rachel, david).

father(X, Y) :- male(X), parent(X, Y).
mother(X, Y) :- female(X), parent(X, Y).
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X\=Y.
uncle(X, Y) :- sibling(X, Z), parent(Z, Y), male(X).
aunt(X, Y) :- sibling(X, Z), parent(Z, Y), female(X).
