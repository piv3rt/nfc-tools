from mifare_1k_safe import protect

if __name__ == "__main__":
    assert protect(0xFFFFFF) == 0xFF77F7
    assert protect(0x000000) == 0x880080
    assert protect(0xFF0780) == 0xFF0780
    assert protect(0x07878F) == 0x8F0787
