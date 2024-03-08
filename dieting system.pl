disease(high_blood_pressure,
    "High blood pressure, also known as hypertension, is a condition in which the blood pressure in the arteries is persistently elevated.",
    [avoid(salt), avoid(caffeine), avoid(alcohol), consume(whole_grains), consume(fruits), consume(vegetables), consume(low_fat_dairy_products)]).

disease(diabetes,
    "Diabetes is a chronic metabolic disorder characterized by high blood glucose levels due to insufficient insulin production or insulin resistance.",
    [limit(sugar), limit(carbohydrates), consume(lean_proteins), consume(healthy_fats), consume(whole_grains), consume(fruits), consume(vegetables)]).

disease(high_cholesterol,
    "High cholesterol is a condition in which there is an excess of cholesterol in the blood, leading to an increased risk of heart disease.",
    [limit(saturated_fats), limit(trans_fats), consume(omega_3_fatty_acids), consume(soluble_fiber), consume(whole_grains), consume(fruits), consume(vegetables)]).

suggest_diet(Disease) :-
    disease(Disease, Description, SuggestedDiet),
    write("You have "), write(Disease), nl,
    write("Description: "), write(Description), nl,
    write("Suggested Diet: "), nl,
    print_suggested_diet(SuggestedDiet).

print_suggested_diet([]) :- nl.
print_suggested_diet([H|T]) :-
    write("- "), print_diet_item(H), nl,
    print_suggested_diet(T).

print_diet_item(avoid(Item)) :-
    write("Avoid "), write(Item).
print_diet_item(limit(Item)) :-
    write("Limit "), write(Item).
print_diet_item(consume(Item)) :-
    write("Consume "), write(Item).

% Query Examples:

?- suggest_diet(high_blood_pressure).
?- suggest_diet(diabetes).
?- suggest_diet(high_cholesterol).
