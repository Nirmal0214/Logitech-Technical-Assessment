# Logitech logi.bin Parser – Technical Assessment

This project is my solution for the Logitech Innovation Team technical test. :contentReference[oaicite:0]{index=0}  
The goal is to:

- Parse the provided `logi.bin` binary file
- Extract every message and its sequence number
- Present the data **clearly and creatively** in the terminal

The application is written in Python and focuses on:
- Clean, readable, and maintainable code
- Correct binary parsing according to the given packet structure
- An animated, **block-style view** of each message using the `rich` library
- A small CLI with a pleasant developer experience

---

## Binary File Format  

According to the assessment, the `logi.bin` file contains *n* messages. Each message has the following packet structure: :contentReference[oaicite:1]{index=1}  

| Component        | Size     | Type         | Description                                      |
|-----------------|----------|-------------|--------------------------------------------------|
| PAYLOAD_HEADER  | 4 bytes  | Int32 (LE)  | Length of the message text in bytes             |
| SEQUENCE_NUMBER | 4 bytes  | Int32 (LE)  | Sequence number (ordering of the message)       |
| MESSAGE         | N bytes  | String      | UTF-8 encoded message text                      |

My parser loops over the file and, for each message:

1. Reads 4 bytes → interprets as a little-endian 32-bit integer → **message length**
2. Reads 4 bytes → interprets as a little-endian 32-bit integer → **sequence number**
3. Reads **N** bytes → decodes as UTF-8 → **message text**
4. Wraps the result in a small `LogMessage` data structure
5. Repeats until the end of the file


---

## 🧱 Project Structure

logitech-log-parser/
│
├── src/
│   ├── parser.py        # Binary parsing logic (LogMessage + parse_log_file)
│   ├── main.py          # CLI entry point, animations, and block view
│   └── __init__.py
│
├── logi.bin             # Provided binary file (input)
├── requirements.txt     # Python dependencies (rich, etc.)
└── README.md            # This file

---

## ▶️ Usage Instructions

### How to Run the Application

This project provides a command-line interface that reads the `logi.bin` file,
parses each binary message, and displays them in an animated block-view format.

### Step 1 — Install Dependencies

Before running the tool, install the required Python packages:

```bash
pip install -r requirements.txt

```

### Run the Parser

Use the -i or --input flag to point to your logi.bin file:

```bash
python -m src.main --input logi.bin

```
### What Happens When You Run the Program

A progress bar appears while parsing the binary file

Each message is displayed in a clean block view

Multi-line formatting is preserved

A typing animation prints each line naturally

Output uses Rich for colors and formatting

---

## 🎬 Demo (Execution GIF)

Below is a short demonstration of the parser running in the terminal:

![Execution Demo](assets/execution.gif)

---

## Design Decisions & Reasoning

This section explains the thought process behind the implementation, highlighting clarity, maintainability, and user-focused design.

---

### **1. Clean Separation of Concerns**
I intentionally separated the project into the following layers:

- **`parser.py`** → Handles binary parsing only  
- **`main.py`** → Handles CLI, animations, and user interaction  

This prevents mixing logic, keeps each component easy to test, and aligns with real-world software engineering practices.

---

### **2. Minimal Dependencies**
The solution uses only:
- Python's standard library  
- `rich` (for color, animation, and formatting)

This keeps the project lightweight and easy to run anywhere without complex setup.

---

### **3. Block View for Human-Friendly Output**
Instead of dumping raw parsed text, I chose a **well-structured Block View** for readability:

- Clear per-message section  
- Multi-line preserved  
- Colored labels  
- Clean separators around each block  

This gives a polished, professional output suitable for both engineers and reviewers.

---

### **4. Typing Animation for Better UX**
I added a simple typing effect (`typing_print()`) to give the CLI more personality.

- Not overwhelming  
- Easy to turn off  
- Applied only to message text (not UI labels)  

This balances professionalism and creativity without slowing execution.

---

### **5. Lightweight Progress Indicator**
Even though the parsing is fast, I added a subtle progress bar to:

- Enhance perceived responsiveness  
- Make the CLI feel “alive”  
- Provide immediate visual feedback  

This mirrors patterns used in real tools (package managers, CLI frameworks, etc.).

---

### **6. Defensive Programming**
The parser validates:

- File existence  
- Binary structure  
- Unexpected EOF  
- Message length mismatches  

This ensures reliability even if the file is corrupted.

---

### **7. Engineering Communication**
Throughout the code I added:

- Inline comments  
- Clear function names  
- Type hints  
- Docstrings  

These mimic real production-quality Python code and show attention to detail.

---

### **8. Professional Markdown Documentation**
The README is structured into:

1. Overview  
2. File Format Specification  
3. Project Structure  
4. How to Run  
5. Output Preview  
6. Design Decisions (this section)  

This mirrors documentation style seen in modern GitHub open-source repositories.

---
