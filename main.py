my_dict = {
    "escalus":"King of Verona",
    "paris" : "Aik jawaan raees zadaah, Baadshaah ky khaandaan sy",

    "montague" : "(Romeo ky abba) One of the two wealthy families",
    "capulet" : " (Juliet ky abba) One of the two wealthy families ",

    "old man" : " capulet's(Juliet ky abba) relative ",
    "romeo" : "Montague gharaany ka larka",

    "mercutio" : "Baadshaah(Escalus) ka rishtedaar aur romeo ka dost",
    "benvolio" : " Montgue(romeo_ky_abba) ky bhai ka beta aur romeo ka dost ",
    "tybalt" : "Lady Capulet(Romeo ki amma) ky bhai ka beta",

    "friar lawrence" : "paadri",
    "balthazar" : "Romeo ka mulaazim",
    "sampson" : "Capulet(Juliet ky abba) ka naukar",
    "gregory" : "Capulet(Juliet ky abba) ka naukar",
    "antony" : "Capulet(Juliet ky abba) ka naukar",
    "poptan" : " Capulet(Juliet ky abba) ka naukar ",
    "peter" : "Capulet(Juliet ky abba) ka mulaazim (Ghar ky kaam kaaj message wagera handle karta hai)",
    "servingmen":"Capulet ghar ka aam mulaazim",

    "abraham" : "Montague(Romeo ky abba) ka mulaazim",
    "apothecary" : "Dawa farosh",
    "three musicians" : "Capulet ghar ki ek event per bulaye gaye saazinday",
    "page to paris" : "Paris(Baadshah ka beta) ka mulaazim",
    "officer" : "",

    "lady montague":"Romeo ki amma",
    "lady capulet":" Juliet ki amma ",
    "juliet":" Capulet gharaany ki larki ",
    "nurse":" Juliet ki daai ",
    # "chorus":"Narrator",
}

print(" x for exiting and list for list of all keys")
while True:
    user_inp = input( " Enter the name : " ).lower()
    dict_keys = my_dict.keys()
    if user_inp in my_dict:
        print(my_dict[user_inp])
    elif user_inp == "x":
        break
    elif user_inp == "list":
        print(dict_keys)
    else:
        print("Enter correct name")