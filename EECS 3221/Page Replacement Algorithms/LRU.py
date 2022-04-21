class Page:
    def __init__(self, page_number: int, loaded: int, last_ref: int, r: int, m: int):
        self.page_number = page_number
        self.loaded = loaded
        self.last_ref = last_ref
        self.r = r
        self.m = m


def lru(pte: list) -> None:
    pte.sort(key=lambda x: x.last_ref)
    print("Using the LRU Page Replacement Algorithm, Page Number {} has been chosen to be evicted.."
          .format(pte[0].page_number))


# Homework Question: Parameters

p0 = Page(0, 126, 280, 1, 0)
p1 = Page(1, 230, 265, 0, 1)
p2 = Page(2, 140, 270, 0, 0)
p3 = Page(3, 110, 285, 1, 1)

pages = [p0, p1, p2, p3]

lru(pages)
