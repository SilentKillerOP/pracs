father(X,Y):- male(X),
    parent_of(X,Y).

grandfather(X,Z):- male(X),
    parent_of(X,Y),
    parent_of(Y,Z).

mother(X,Y):- female(X),
    parent_of(X,Y).

grandmother(X,Z):- female(X),
    parent_of(X,Y),
    parent_of(Y,Z).


brother(X,Y):- male(X),
    parent_of(P,X),
    parent_of(P,Y),
    X \= Y.

sister(X,Y):- female(X),
    parent_of(P,X),
    parent_of(P,Y),
    X \= Y.

is_successor(X,Y):-
    parent_of(Y,X).

is_successor(X,Z):-
    parent_of(Y,X),
    is_successor(Y,Z).

is_predecessor(X, Z):-
    parent_of(X, Y),
    is_predecessor(Y, Z).

is_predecessor(X, Y):-
    parent_of(X, Y).

uncle(X,Y):-
    parent_of(P,Y),
    brother(X,P).

aunt(X,Y):-
    parent_of(P,Y),
    sister(X,P).


parent_of(m,d).
parent_of(p,k).
parent_of(p,g).
parent_of(n,d).
parent_of(p,m).
male(p).
male(g).
male(m). 
female(n).
female(k).
