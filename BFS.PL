graph([    node(a, [b, c], [5, 6]),
    node(b, [d], [7]),
    node(c, [d, e], [4, 8]),
    node(d, [f], [9]),
    node(e, [f], [5]),
    node(f, [], [])
]).
node(Name, Neighbors, Costs):-
    member(Name, [a, b, c, d, e, f]),
    length(Neighbors, X),
    length(Costs, X).
min([X], X).
min([H|T], X):-
    min(T, X1),
    min(H, X1, X).

min(X, Y, X):-
    X =< Y.
min(X, Y, Y):-
    X > Y.

% Predicate to find the neighbor node with the lowest cost
minimum_neighbor(Node, Neighbors, Costs, MinimumNeighbor):-
    findall(Minimum, (
        nth0(Index, Neighbors, Neighbor),
        nth0(Index, Costs, Cost),
        h(Node, Neighbor, H),
        Minimum is Cost + H
    ), Minimums),
    min(Minimums, Minimum),
    nth0(Index2, Minimums, Minimum),
    nth0(Index2, Neighbors, MinimumNeighbor).

% Predicate to calculate the heuristic value between two nodes
h(a, d, 9).
h(a, e, 6).
h(a, f, 3).
h(b, d, 7).
h(b, e, 4).
h(b, f, 11).
h(c, d, 3).
h(c, e, 7).
h(c, f, 10).
h(d, d, 0).
h(d, e, 8).
h(d, f, 13).
h(e, d, 6).
h(e, e, 0).
h(e, f, 5).
h(f, d, 3).
h(f, e, 7).
h(f, f, 0).

% Predicate to implement the Best First Search algorithm
best_first_search(Start, Goal):-
    graph(Graph),
    best_first_search(Graph, [[Start]], Goal).

best_first_search(_, [[Goal|Path]|_], Goal):-
    reverse([Goal|Path], Path).

best_first_search(Graph, [Path|Paths], Goal):-
    extend_path(Graph, Path, ExtendedPaths),
    append(Paths, ExtendedPaths, NewPaths),
    sort_paths(NewPaths, SortedPaths),
    best_first_search(Graph, SortedPaths, Goal).

extend_path(_, [Goal|_], []):-
    goal(Goal).
extend_path(Graph, [Node|Path], ExtendedPaths):-
    findall([Neighbor, Node|Path], (
        node(Node, Neighbors, _),
        member(Neighbor, Neighbors),
        \+ member(Neighbor, Path),
        is_valid(Graph, Path, Neighbor)
    ), ExtendedPaths).

is_valid(Graph, Path, Node):-
    \+ member([_, Node|_], Path),
    \+ member(node(Node, _, _), Graph).

sort_paths(Paths, SortedPaths):-
    map_list_to_pairs(path_cost, Paths, Pairs),
    keysort(Pairs, SortedPairs),
    pairs_values(SortedPairs, SortedPaths).

path_cost([Node|Path], Cost):-
    reverse([Node|Path], ReversedPath),
    path_cost(ReversedPath, Cost).

path_cost([_], 0).
path_cost([Node1, Node2|Path], Cost):-
    node(Node1, Neighbors, Costs),
    nth0(Index, Neighbors, Node2),
    nth0(Index, Costs, Cost),
    path_cost([Node2|Path], RemainingCost),
    Cost is Cost + RemainingCost.
