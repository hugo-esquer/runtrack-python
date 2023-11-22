def time_to_text(nombre):
    nbr_heures = nombre // 60
    nbr_minutes = nombre % 60
    print(f"{nbr_heures} heures et {nbr_minutes} minutes")


time_to_text(25)
time_to_text(60)
time_to_text(678)
time_to_text(90)
time_to_text(456)
time_to_text(112)
time_to_text(169)