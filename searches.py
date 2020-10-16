import auctions


def search_for_s_grade(list_to_check):
    selected = []
    for item in list_to_check:
        if 'A' in item.grade:
            selected.append(auctions.auction(item.ID, item.model, item.gig, item.grade, item.count, item.price, item.link))
    return selected


def search_for_b_grade(list_to_check):
    selected = []
    for item in list_to_check:
        if 'B' in item.grade:
            selected.append(auctions.auction(item.ID, item.model, item.gig, item.grade, item.count, item.price, item.link))
    return selected


def search_for_c_grade(list_to_check):
    selected = []
    for item in list_to_check:
        if 'C' in item.grade:
            selected.append(auctions.auction(item.ID, item.model, item.gig, item.grade, item.count, item.price, item.link))
    return selected


def search_for_d_grade(list_to_check):
    selected = []
    for item in list_to_check:
        if 'D' in item.grade:
            selected.append(auctions.auction(item.ID, item.model, item.gig, item.grade, item.count, item.price, item.link))
    return selected
