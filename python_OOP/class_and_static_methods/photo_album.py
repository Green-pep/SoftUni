import math


class PhotoAlbum:
    MAX_PHOTOS_ON_PAGE = 4

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls(math.ceil(photos_count / cls.MAX_PHOTOS_ON_PAGE))

    def add_photo(self,label: str):
        for photo, page in enumerate(self.photos, start=1):
            if len(page) < self.MAX_PHOTOS_ON_PAGE:
                page.append(label)
                return f"{label} photo added successfully on page {photo} slot {len(page)}"
        return "No more free slots"
    def display(self):
        sepa = 11 * "-" + "\n"
        result = sepa
        for page in self.photos:
            result += ' '.join(["[]" for _ in page]) + "\n" + sepa
        return result.strip()


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

