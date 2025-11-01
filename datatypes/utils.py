def multi_pop(data: bytearray, count: int) -> bytes:
    return b''.join(data.pop(0).to_bytes(1, "big") for _ in range(count))