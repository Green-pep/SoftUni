from typing import List
from battle.project import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, album: Album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album = next((a for a in self.albums if a.name == album_name), None)
        if album:
            if album.published:
                return "Album has been published. It cannot be removed."
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        return "\n".join(
            [f"Band {self.name}"] + [f"{a.details()}" for a in self.albums]
        )
