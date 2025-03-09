from datetime import datetime

def check_coupon(ent, corr, curr_d, exp_d):
    d1 = datetime.strptime(curr_d, '%B %d, %Y')
    d2 = datetime.strptime(exp_d, '%B %d, %Y')
    return ent is corr and d1 <= d2