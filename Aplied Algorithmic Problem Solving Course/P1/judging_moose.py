"""
Moose Problem

Beskrivning:
Ett program för att avgöra om en älg är symmetrisk eller asymmetrisk baserat 
på storleken av dess horn, eller om det inte är en älg alls.

Indata:
- Två heltal L och R som representerar vänster respektive höger hornstorlek.

Utdata:
- En av följande strängar:
  - "Not a moose" om L och R är 0.
  - "Even X" om L och R är lika, där X är summan av hornen.
  - "Odd X" om hornen är olika stora, där X är dubbla storleken av det större hornet.

Lösningsstrategi:
- Om båda hornen är 0, returnera "Not a moose".
- Om hornen är lika, returnera "Even" med summan.
- Om hornen är olika, returnera "Odd" med dubbla det största hornets storlek.

Tidskomplexitet:
- Programmet utför endast ett fåtal jämförelser och beräkningar, vilket gör det O(1).

"""

def main():
    # Läs in vänster och höger hornstorlek
    input_values = input().split()
    L = int(input_values[0])
    R = int(input_values[1])

    # Avgör om det är en älg och vilken typ
    if L == 0 and R == 0:
        print("Not a moose")  # Ingen älg om båda hornen är 0
    elif L == R:
        print(f"Even {L + R}")  # Symmetrisk älg med lika horn
    else:
        print(f"Odd {2 * max(L, R)}")  # Asymmetrisk älg, ta det största hornet gånger två

if __name__ == "__main__":
    main()
