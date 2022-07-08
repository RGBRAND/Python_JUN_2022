# waf to calculate fine for a book based on the days late and book categoty 

from http.client import REQUEST_URI_TOO_LONG


def collect_fine(days):
    if days <= 3:
        return days * 10
    elif days <= 7:
        return days * 50
    elif days <= 9:
        return days * 100
    else:
        return 'more than 10 days fine is double'
if __name__ == '__main__':

    fine = collect_fine(12)
    print(f'you have to pay fine: {fine}')
