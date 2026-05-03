<div align="center">
    <h2>
        <b>
            Slice and Method
        </b>
    </h2>
        My Computer Science Class, Programing in Python<br>Meeting 6: Assignment
</div>

---

### Base Theory
<div align="justify">
    In Python, strings are immutable text data types, meaning they cannot be modified directly but can generate new strings through manipulation. Key techniques include slicing to extract specific parts via indices and built-in methods like lower(), strip(), replace(), and split(). Mastering these tools is essential for effective data cleaning and preparation.
</div>

#### Assignment
<div align="justify">
    Write a program to clean up user input (remove spaces and lowercase letters),search and replace specific words in a sentence, (Optional) Perform a simple tokenization of a sentence into a list of words.
</div>

### Implementation
My first implementation here will be using:
| String Method | Explanation |
| :-- | :-- |
| ``stript()`` | for removing spaces between word. |
| ``lower()`` | for making the word in lowercases. |
| ``replace()`` | for replacing old word into the new one. |
| ``split()`` | for making the word into a list. |

| Slicing | Explanation |
| :-- | :-- |
| ``[-5:]`` | for taking the most behind of the word. |
| ``[:5]`` | for taking the most front of the word. |

---

### File Structure
```
Slicing-Method/
├── L6.py           # Fist implementation code
└── README.md       # Please Read For Better General Understanding
```

### How to run
- First, making virtual environtment for yourself and activate it.
    - On Windows (for me using git bash):
    ```bash
    py -m venv .venv && source .venv/Scripts/activate
    ```
    - On linux based OS (bash / zsh):
    ```bash
    python3 -m venv .venv && source .venv/bin/activate
    ```
- Second, run the code file.
    - On windows (for me using git bash):
    ```bash
    py L6.py
    ```
    - On linux based OS (bash / zsh):
    ```zsh
    python3 L6.py
    ```

---

<div align="center">
    <b>
        Made By Me. 😊
    </b>
</div>