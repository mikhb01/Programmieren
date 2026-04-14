def kasten(text, zeichen="*", wieviele=10):
    """Ein Kasten mit Text wird ausgegeben."""
    print(zeichen*wieviele)
    print(text)
    print(zeichen*wieviele)
kasten(wieviele=7, zeichen="/", text="Hallo Schrödinger")