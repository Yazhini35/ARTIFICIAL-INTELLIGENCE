valid_age(john, 25).
valid_age(sarah, 18).
valid_permit(john).
not_valid_permit(sarah).
eligible(Person) :-
  valid_age(Person, Age),
  Age >= 18,
  valid_permit(Person).

eligible(Person) :-
  valid_age(Person, Age),
  Age >= 16,
  not_valid_permit(Person).

% Queries
?- eligible(john).
?- eligible(sarah).
