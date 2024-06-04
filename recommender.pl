% Define os fatos e regras para determinar a recomendação baseada nas respostas do questionário

% Base de conhecimento de tecnologias recomendadas
technology(front_end, ["HTML", "CSS", "JavaScript", "React", "Vue.js"]).
technology(back_end, ["Node.js", "Python", "Java", "C#", "Ruby on Rails"]).
technology(dados, ["SQL", "Python", "R", "Pandas", "NumPy"]).

% Regra para determinar a recomendação
recommendation(Answers, Recommendation) :-
    nth0(2, Answers, "Sim"), nth0(3, Answers, "Sim"), Recommendation = dados;
    nth0(1, Answers, "Interfaces Visuais"), Recommendation = front_end;
    nth0(4, Answers, "Sim"), Recommendation = front_end;
    nth0(5, Answers, "Sim"), nth0(6, Answers, "Sim"), nth0(7, Answers, "Sim"), Recommendation = back_end;
    nth0(8, Answers, "Sim"), Recommendation = back_end.

% Regra para obter tecnologias recomendadas com base na recomendação
recommended_technologies(Recommendation, Technologies) :-
    technology(Recommendation, Technologies).
