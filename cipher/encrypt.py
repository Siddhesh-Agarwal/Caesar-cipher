def caesar_cipher(string: str, key: list[int]):
    """Encrypts a string using a Caesar cipher.

    Args
    ----
    string (str, required):
        The string to encrypt
    key (int or list of int, required):
        The key used to encrypt the string.

    Returns
    -------
    encrypted_msg (str): The encrypted message.
    """
    if isinstance(key, int):
        key = [key]
    encrypted_message = ""
    l = len(key)
    for i, char in enumerate(string):
        encrypted_message += chr(ord(char) + key[i % l])
    return encrypted_message
