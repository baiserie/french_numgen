import random
import time
import os
import fade

def clear_terminal():
   
    if os.name == 'nt':
        _ = os.system('cls')  
    else:
        _ = os.system('clear') 

def generate_french_number():
   
    random_digits = [str(random.randint(1, 9)) for _ in range(8)]
    
    
    prefix = random.choice(['06', '07'])
    
    #
    phone_number = f'+33 {prefix}{"".join(random_digits)}'
    
    return phone_number

def main():
    clear_terminal() 
    
    banner = """

  ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  
 ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒
▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒   V2 | c'est un outils gratuit | dev by opj
░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  
░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒
 ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░
  ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░
░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ 
      ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░     
                                                                              

                                                                          """
    faded_text = fade.purplepink(banner)
    print(faded_text)
    
    num_to_generate = int(input("Combien de numéros tu veux générer ? "))

    
    file_counter = 1

   
    if not os.path.exists("numero_gen"):
        os.makedirs("numero_gen")

    while True:
        
        while True:
            filename = f"num_gen({file_counter}).txt"
            if not os.path.exists(os.path.join("numero_gen", filename)):
                break
            file_counter += 1

        with open(os.path.join("numero_gen", filename), "w") as file:
            for _ in range(num_to_generate):
                phone_number = generate_french_number()
                file.write(phone_number + "\n")

        print(f"[HIT] Les numéros de téléphone ont été enregistrés dans '{filename}'.")
        print("[AUTHOR] dev by opj !\n")
        file_counter += 1
        time.sleep(1) 

        
        num_to_generate = int(input("Combien de numéros tu veux générer ? "))


if __name__ == "__main__":
    main()
