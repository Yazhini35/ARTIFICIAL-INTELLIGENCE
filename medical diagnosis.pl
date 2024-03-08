start_diagnosis :-
    write('What are your symptoms? '), nl,
    read(Symptoms),
    diagnose(Symptoms, Disease),
    write('You may have '), write(Disease), nl.
diagnose([fever, cough, headache], 'Common Cold').
diagnose([fever, cough, sore_throat], 'Flu').
diagnose([rash, itchiness, sneezing], 'Allergies').
diagnose([chest_pain, shortness_of_breath, dizziness], 'Heart Attack').
diagnose(_, 'Unknown').

