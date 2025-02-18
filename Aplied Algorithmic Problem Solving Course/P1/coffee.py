"""
Coffee Cup Combo

Beskrivning:
Jonna behöver dricka en kopp kaffe per föreläsning för att hålla sig vaken. 
Hon kan ta med sig maximalt två koppar kaffe från föregående föreläsning, 
och vissa föreläsningssalar har kaffemaskiner där hon kan fylla på.

Indata:
- En heltalsvariabel n (antal föreläsningar).
- En sträng av längd n där varje tecken är '1' (föreläsningssal har en kaffemaskin) eller '0' (ingen kaffemaskin).

Utdata:
- Ett heltal som representerar det maximala antalet föreläsningar där Jonna kan hålla sig vaken.

Lösningsstrategi:
- Iterera genom föreläsningssalarna.
- Om en kaffemaskin finns i salen ('1'), drick en kopp och fyll på reserv upp till max 2 koppar.
- Om ingen kaffemaskin finns ('0'), använd en reservkopp om möjligt.
- Räkna antalet föreläsningar Jonna kan hålla sig vaken.

Tidskomplexitet:
- Programmet gör en enkel iteration över n föreläsningar och utför endast O(1)-operationer per iteration.
- Därför är den totala tidskomplexiteten O(n).

"""

def main():
    # Läs in antalet föreläsningar och kaffemaskinernas placering
    n = int(input())
    coffee_halls = input()

    focused = 0  # Antal föreläsningar Jonna kan hålla sig vaken på
    coffee_reserves = 0  # Antal koppar kaffe hon har i reserv

    # Iterera genom föreläsningarna
    for i in range(n):
        if coffee_halls[i] == '1':
            # Jonna dricker direkt om det finns en maskin
            focused += 1
            # Om hon har 0 koppar, fyll på två
            if coffee_reserves == 0:
                coffee_reserves = 2
            # Om hon har 1 kopp, fyll på till max 2
            elif coffee_reserves < 2:
                coffee_reserves += 1
        elif coffee_halls[i] == '0':
            # Använd en reservkopp om det inte finns en kaffemaskin
            if coffee_reserves > 0:
                focused += 1
                coffee_reserves -= 1

    # Skriv ut det maximala antalet föreläsningar där Jonna kan hålla sig vaken
    print(focused)

if __name__ == "__main__":
    main()
