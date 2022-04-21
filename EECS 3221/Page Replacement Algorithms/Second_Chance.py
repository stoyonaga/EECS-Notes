class Page:
    def __init__(self, page_number: int, loaded: int, last_ref: int, r: int, m: int):
        self.page_number = page_number
        self.loaded = loaded
        self.last_ref = last_ref
        self.r = r
        self.m = m


def second_chance(pte: list) -> None:
    pte.sort(key=lambda x: x.loaded)
    for page in pte:
        if page.r == 0:
            print("Using the Second Chance Page Replacement Algorithm, Page Number {} has been chosen to be evicted.."
                  .format(page.page_number))
            break
        elif page.r == 1:
            page.r = 0
            pte.append(page)
            print("Page {}'s reference bit has been reset and appended to the list again."
                  .format(page.page_number))
            del page


# Homework Question: Parameters

p0 = Page(0, 126, 280, 1, 0)
p1 = Page(1, 230, 265, 0, 1)
p2 = Page(2, 140, 270, 0, 0)
p3 = Page(3, 110, 285, 1, 1)

pages = [p0, p1, p2, p3]

second_chance(pages)
