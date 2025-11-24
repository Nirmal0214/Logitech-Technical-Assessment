from dataclasses import dataclass
from typing import List
import struct


@dataclass
class LogMessage:
    """
    A small container to hold a parsed message from the binary file.
    """
    sequence_number: int
    text: str


def parse_log_file(path: str) -> List[LogMessage]:
    """
    Parse the given binary file and return all messages.
    This function walks through the file sequentially and extracts
    every message until the end of the file is reached.
    """

    messages: List[LogMessage] = []

    # Open the binary file in "rb" mode to ensure raw bytes are read as-is.
    with open(path, "rb") as f:
        while True:
            # 1) Reads first 4 bytes: message length
            size_bytes = f.read(4)

            # If no bytes returned → clean end-of-file reached
            if not size_bytes:
                break

            if len(size_bytes) != 4:
                # Corrupted or incomplete message header
                raise ValueError("Unexpected end of file when reading message size")

            # Convert 4 bytes -> uint32
            message_len = struct.unpack("<I", size_bytes)[0]

            #2) Read the next 4 bytes: sequence number
            seq_bytes = f.read(4)
            if len(seq_bytes) != 4:
                raise ValueError("Unexpected end of file when reading sequence number")

            sequence_number = struct.unpack("<I", seq_bytes)[0]

            # 3) Read the next N bytes: message text
            message_bytes = f.read(message_len)
            if len(message_bytes) != message_len:
                raise ValueError("Unexpected end of file when reading message text")

            # Decode raw bytes to human-readable text
            text = message_bytes.decode("utf-8", errors="replace")

            # Store parsed message
            messages.append(
                LogMessage(sequence_number=sequence_number, text=text)
            )

    return messages
