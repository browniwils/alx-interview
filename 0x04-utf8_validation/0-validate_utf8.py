#!/usr/bin/python3
"""Module for validating UTF-8 encodiing characters.
"""


def validUTF8(data):
    """Helper function to check if a given byte is a valid continuation byte.
    """

    def isContinuation(byte):
        """Check for byte continuation.
        """
        return (byte & 0b11000000) == 0b10000000

    # Iterate through each byte in the data
    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        num_bytes = 0
        mask = 0b10000000
        while mask & data[i]:
            num_bytes += 1
            mask >>= 1
        if num_bytes == 1 or num_bytes > 4:
            return False  # Updated condition for valid byte count

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes):
            i += 1
            if i >= len(data) or not isContinuation(data[i]):
                return False

        # Move to the next character
        i += 1

    return True
