def rail_fence_cipher_encrypt(message, key):
    depth, repeats = key

    message = message.lower()

    period = 2 * depth - 2
    encrypted_message = message

    for _ in range(repeats):
        encrypted_message_temp = ""
        for i in range(depth):
            j = i
            while j < len(encrypted_message):
                encrypted_message_temp += encrypted_message[j]
                if 0 < i < depth - 1:
                    next_j = j + period - 2 * i
                    if next_j < len(encrypted_message):
                        encrypted_message_temp += encrypted_message[next_j]
                j += period
        encrypted_message = encrypted_message_temp

    return encrypted_message