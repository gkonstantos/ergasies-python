#13η Άσκηση.

# Συνάρτηση που ελέγχει αν η συγκεκριμένη τιμή της λίστας + το max μέχρι εκείνο το σημείο είναι μικρότερα το ακέραιου.
def check(listb,lim,currmax,begin,end):
    for i in range(end,begin,-1):
        if((listb[i]+currmax) <= lim):
            currmax+=listb[i]
            check(listb,lim,currmax,begin,i-1)
    return(currmax)


# Συνάρτηση που βρίσκει το μέγιστο άθροισμα μέσω ελέγχων και κλήσης της συνάρτησης check.

def maxDistance(listb,lim):
    listb.sort()
    fmax = 0
    currmax = 0

    if(sum(listb)<lim):
        return sum(listb)

    for begin in range(len(listb)):
        currmax = listb[begin]
        for end in range(len(listb)-1,begin,-1):
            if ((listb[end]+currmax)<=lim):
                currmax = check(listb,lim,currmax,begin,end)
                fmax= max(currmax,fmax)
    return fmax

# Ο χρήστηε ζητείται να εισάγει νούμερα, τα οποία χωρίζονται στη λίστα με βάση το κενό, καθώς και τον ακέραιο που λειτουργεί σαν όριο.

lista = input("please insert a list of numbers with a space between them: ")
lista=(lista.split())
for i in range(len(lista)):
    lista[i] = int(lista[i])
integer=int(input("please insert an integer: "))

print("the maximum sum is: ",maxDistance(lista,integer))