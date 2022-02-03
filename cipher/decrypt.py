def cipher_reverse(string: str, key: list[int]):
    """Reverses the Caesar cipher on the given string.

    Args
    ----
    string (str, required):
        The string to decrypt.
    key (int or list of int, required):
        The key to decrypt the string.

    Returns
    -------
    decrypted_msg (str): The decrypted message.
    """
    if isinstance(key, int):
        key = [key]
    decrypted_msg = ""
    l = len(key)
    for i, char in enumerate(string):
        decrypted_msg += chr(ord(char) - key[i % l])
    return decrypted_msg
