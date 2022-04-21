import random
"""
Recall:
    - Class 0: Not Referenced, Not Modified
    - Class 1: Not Referenced, Modified (Case 3, when the system clears the R-bit)
    - Class 2: Referenced, Not Modified
    - Class 3: Referenced, Modified
"""


class Page:
    def __init__(self, page_number: int, loaded: int, last_ref: int, r: int, m: int):
        self.page_number = page_number
        self.loaded = loaded
        self.last_ref = last_ref
        self.r = r
        self.m = m


def page_nru(pte: list) -> None:
    page_class_0 = []
    page_class_1 = []
    page_class_2 = []
    page_class_3 = []

    class_list = [page_class_0, page_class_1, page_class_2, page_class_3]

    for page in pte:
        if page.r == 0 and page.m == 0:
            page_class_0.append(page)
        elif page.r == 0 and page.m == 1:
            page_class_1.append(page)
        elif page.r == 1 and page.m == 0:
            page_class_2.append(page)
        elif page.r == 1 and page.m == 1:
            page_class_3.append(page)
        else:
            raise "Error: Page has not properly been set.."
    print("===== Page Classification =====")

    print("Class 0 Pages: {}".format(",".join(str(page.page_number) for page in page_class_0)))
    print("Class 1 Pages: {}".format(",".join(str(page.page_number) for page in page_class_1)))
    print("Class 2 Pages: {}".format(",".join(str(page.page_number) for page in page_class_2)))
    print("Class 3 Pages: {}".format(",".join(str(page.page_number) for page in page_class_3)))

    for page_class in class_list:
        if len(page_class) > 0:
            candidate_idx = random.randint(0, len(page_class) - 1)
            print("\nUsing the NRU Page Replacement Algorithm, Page Number {} has been chosen to be evicted.."
                  .format(page_class[candidate_idx].page_number))
            del page_class[candidate_idx]
            break


# Homework Question: Parameters

p0 = Page(0, 126, 280, 1, 0)
p1 = Page(1, 230, 265, 0, 1)
p2 = Page(2, 140, 270, 0, 0)
p3 = Page(3, 110, 285, 1, 1)

pages = [p0, p1, p2, p3]

page_nru(pages)
