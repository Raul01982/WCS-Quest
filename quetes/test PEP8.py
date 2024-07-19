# test 1
# variable
# liste des reponses possibles
list_oui_non = ["o", "n"]
# dictionnaire qui contient les questions pour le joueur
dict_quest = {
    "start": "Bonjour Jack !\n Veux-tu jouer à notre quiz ? (o :oui, n :non)",
    "bad_res": "Sois attentif au details Jeck, tu seras Data Analyst !",
    "re_start": "Jeux terminé ! Veux-tu rejouer ?"

}
# premiere question pour lancer le jeu ou pas


def fn_quiz_res(key_dict_quest):
    return (input(dict_quest[key_dict_quest]).lower())


play_res = fn_quiz_res("start")

# tant que le joueur ne repond pas correctement
while play_res not in list_oui_non:
    play_res = fn_quiz_res("bad_res")
# le joueur ne veut pas jouer
if play_res == list_oui_non[1]:
    print("Looser Jack ! T'es mauvais !")
# jack se decide enfin a jouer
if play_res == list_oui_non[0]:
    print("Ok ! On joue !")
# coder le jeu :
# variable du jeu
questionnaire = {
    "Paris": "la capitale de la France ?",
    "Madrid": "la capitale de l'Espagne ?",
    "Berlin": "la capitale de l'Allemange ? "
    }
nb_point = 0

for key_question, value_question in questionnaire.items():
    print(f"question : {value_question} ")
    nb_essai = 2

    while nb_essai >= 0:
        if input(value_question).capitalize() == key_question:
            print("Bravo ! tu as bien repondu !")
            nb_point += 1
            break
        else:
            print(f"Recommence, il te reste {nb_essai} essai !")
            nb_essai -= 1
    if nb_essai < 0:
        print(f"tu as perdu !, tu as {nb_point} points !")
        break
    print(f"tu as {nb_point} points !")
print("le jeu est fin !")
# demande au joueur s'il veut rejouer
play_res = fn_quiz_res("re_start")
