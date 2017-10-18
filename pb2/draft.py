n_jack = int(input())
min, max = (input()).split()
max, min= int(max), int(min)
moy = float(input())
nb_eleve = int(input())

s = "Jack ! Viens ici !"

notes_str = (input()).split()


def fun():
    notes = []
    r_moy = 0
    bool_max = False
    bool_min = False
    for n in notes_str:
        note = int(n)
        r_moy += note
        notes.append(note)
        if note == max:
            bool_max=True
        if note == min:
            bool_min=True
            
        if note > max:
            print(s)
            return
        if note < min:
            print(s)
            return

    r_moy += n_jack


    if (not bool_max) or (not bool_min):
        print(s)
        return
    if len(notes) != nb_eleve:
        print(s)
        return
    

    if round(r_moy/(nb_eleve+1), 2) != moy:
        print(s)
        return

    elif n_jack > max:
        print(s)
        return
    elif n_jack < min:
        print(s)
        return

    print("RAS")

fun()
