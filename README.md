# Logitech logi.bin Parser – Technical Assessment

This project is my solution for the **Logitech Innovation Team Technical Assessment**.  
It parses the provided `logi.bin` binary file, extracts all messages along with their sequence numbers, and presents them in a **clean, animated block-view format** using Python and the `rich` library.

The main goals of this solution are:
- Accurate parsing of the binary packet structure  
- Clean and maintainable code  
- A visually polished CLI with animations  
- Clear developer-friendly documentation  

---

## 📦 Binary File Format  
According to the assessment, the `logi.bin` file consists of *N* messages, each stored with this structure:

| Component        | Size     | Type         | Description                                      |
|------------------|----------|--------------|--------------------------------------------------|
| PAYLOAD_HEADER   | 4 bytes  | Int32 (LE)   | Length of message text in bytes                  |
| SEQUENCE_NUMBER  | 4 bytes  | Int32 (LE)   | Message ordering index                           |
| MESSAGE          | N bytes  | UTF-8 String | The actual text content of the message           |

Parsing steps:
1. Read 4 bytes → decode as Int32 LE → **message length**  
2. Read 4 bytes → decode as Int32 LE → **sequence number**  
3. Read *N* bytes → decode as **UTF-8 string**  
4. Convert into a `LogMessage` Python object  
5. Continue until end of file  

---

## 🧱 Project Structure

```
logitech-Technical-Assessment/
│
├── src/
│   ├── parser.py       # Binary parsing logic (LogMessage + parse_log_file)
│   ├── main.py         # CLI entry point, typing animation, block view
│   └── __init__.py
│
├── logi.bin            # Provided binary file (input)
├── requirements.txt    # Python dependencies (rich)
└── README.md           # Documentation
```

---

## ▶️ How to Run the Project

Before running the parser, install all dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Parser (Block View + Typing Animation)

Once dependencies are installed, run:

```bash
python -m src.main --input logi.bin
```

### What You’ll See:
- A progress bar while parsing  
- Each message displayed inside a clean **block section**  
- Multi-line formatting preserved  
- Line-by-line **typing animation**  
- Colored labels for readability  

---

## 🎬 Demo (Execution GIF)

Below is a short demonstration of the parser running:

![Image](https://github.com/user-attachments/assets/5c0240b9-8fac-4ec1-85b9-392255c9999e)

---

## 🧠 Design Decisions & Reasoning

### 1. Clean Separation of Concerns  
- `parser.py`
  Handles only binary parsing. No printing. No styling.
  This makes it reusable in tests, future UI/CLI tools, or even another language binding.
- `main.py`
  Manages CLI, animations, progress bar, and message rendering.
  Keeping UI logic separate makes the program easier to maintain and extend.

This keeps the project modular and easy to maintain.

### 2. Minimal Dependencies  
Only one external library is used:  
- `rich` → color, animation, panels, progress bars
All other components rely on Python’s standard library:
- `struct` for binary unpacking
- `os` / `argparse` for CLI
- `time` for animations

Everything else relies on Python’s standard library.

### 3. Block View Output  
Instead of raw printed messages, the output is presented in a:
-Colored block
- With preserved line breaks
- Clean separator before and after
- Human-readable label styling
- Multi-line support
- Responsiveness with typing animation

The design goal is to make the reviewer’s experience pleasant and effortless to read, similar to developer tools like:

- GitHub Actions logs
- Poetry / Pipenv output
- AWS CLI prettifiers

### 4. Typing Animation  
A lightweight typing animation (`typing_print()`) adds:
- Personality  
- Smooth readability  
- Modern CLI feel

This animation is intentionally subtle (0.05s delay), preserving clarity while adding polish.

### 5. Defensive Programming  
The code includes checks for:
- File not found
- Incomplete integer reads
- Sequence length mismatch
- Unexpected EOF
- Invalid UTF-8 decoding (handled via errors="replace")

This ensures the program behaves gracefully even with corrupted input, which is critical in low-level parsing tasks.

### 6. Professional Documentation  
This README includes:
- Overview  
- Binary specification  
- Project structure  
- Installation steps  
- Output preview  
- Engineering reasoning 

---

## ✔ Final Notes  
This solution was designed to be:
- Professional  
- Readable  
- Lightweight  
- Creative  
- Technically correct  

A clean, polished, and developer-friendly answer to the Logitech assessment.
