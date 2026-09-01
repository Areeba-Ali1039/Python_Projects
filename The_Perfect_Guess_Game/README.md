<div align="center">

# 🎯 The Perfect Guess — Number Guessing Game

**A Classic Higher/Lower Guessing Game, Built in Python**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)]()
[![No Dependencies](https://img.shields.io/badge/Dependencies-None-00C853?style=for-the-badge)]()
[![CLI](https://img.shields.io/badge/Interface-Command_Line-black?style=for-the-badge)]()

*A single-file, zero-dependency Python script — pick a range, guess the number, see how many tries it takes*

[How to Run](#-how-to-run) · [Rules](#-rules) · [Logic](#-game-logic) · [Roadmap](#-roadmap)

</div>

---

## 📌 Overview

**The Perfect Guess** is a simple command-line game: the program secretly picks a random number within a range you choose, and you try to guess it. After every guess, the game tells you whether to go higher or lower, until you land on the exact number — then it reports how many guesses it took you.

No libraries beyond Python's standard `random` module, no setup, no build step — just run the script.

### ✨ Key Highlights

- 🎲 **Random Number Generation** — computer picks a hidden number using `random.randint`
- 🔁 **Higher / Lower Feedback Loop** — guides the player toward the correct answer
- 🛡️ **Input Validation** — invalid range inputs (below 1) are rejected and re-prompted instead of crashing
- 🔢 **Guess Counter** — tracks and reports how many attempts it took to win

---

## 📏 Rules

1. Choose an upper bound `n` for the guessing range.
2. The program picks a hidden number between `1` and `n`.
3. You guess a number.
4. The game responds with:
   - `"Lower number plz"` — your guess is too high
   - `"Higher number plz"` — your guess is too low
5. Repeat until you guess correctly — the game then reports your total number of guesses.

---

## ⚙️ Game Logic

The core of the game is a `while` loop that keeps running until the player's guess matches the computer's hidden number, paired with a simple comparison to decide which hint to print:

```python
computer = random.randint(1, n)
guess = -1
guesses = 0

while (computer != guess):
    guess = int(input("Guess a random Number : "))
    guesses += 1
    if (guess > computer):
        print("Lower number plz")
    elif (guess < computer):
        print("Higher number plz")
```

Input validation for the range follows the same `while`-over-`if` principle, so it keeps re-prompting no matter how many invalid values are entered in a row:

```python
n = int(input("Enter a number : "))
while (n < 1):
    print("Number should be greater than 1")
    n = int(input("Enter a number : "))
```

---

## 🚀 How to Run

```bash
python perfect_guess.py
```

Example session:

```
Enter a number : 100
Guess a random Number : 50
Lower number plz
Guess a random Number : 25
Higher number plz
Guess a random Number : 37
It took 3 guesses for you to guess it right
```

> Update the filename above if your script is saved under a different name.

---

## 📁 Project Structure

```
perfect-guess/
├── perfect_guess.py     # The game script
└── README.md            # This file
```

---

## 🧱 Concepts Covered

- `random` module (`random.randint`) for hidden-number generation
- `while` loops for both the main game loop and input validation
- Conditional logic (`if` / `elif`) for higher/lower comparison
- The `if` vs `while` distinction for robust input handling

---

## ⚠️ Known Limitations

- **No range check on the guess itself** — a guess wildly outside `1`–`n` still works, it just returns a hint
- **No replay loop** — the game ends after one round; running again requires restarting the script
- **Console-only** — no graphical interface

---

## 🔮 Roadmap

- [ ] Add a "play again?" loop without restarting the script
- [ ] Track and display best (fewest-guess) score across rounds
- [ ] Add a difficulty/attempt limit mode
- [ ] Validate that guesses fall within `1`–`n`

---

## 👤 Author

**Areeba Ali**


---

## 📄 License

Personal / educational project — free to use, adapt, and build on.

---

<div align="center">

**🎯 Guess high, guess low, guess right 🎯**

[Back to Top](#-the-perfect-guess--number-guessing-game)

</div>
