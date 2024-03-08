move_disk(1, Src, Dst, _) :-   
    write('Move disk from '),
    write(Src),
    write(' to '),
    write(Dst),
    nl.
move_disk(N, Src, Dst, Aux) :- 
    N > 1,
    N1 is N - 1,
    move_disk(N1, Src, Aux, Dst),
    write('Move disk from '),
    write(Src),
    write(' to '),
    write(Dst),
    nl,
    move_disk(N1, Aux, Dst, Src). % Move N-1 disks from Aux to Dst
solve_hanoi(N) :-
    move_disk(N, 'Source Tower', 'Destination Tower', 'Auxiliary Tower').
