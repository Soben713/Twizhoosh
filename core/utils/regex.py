def combine_regexes(regex_list):
    ret = ''
    for regex in regex_list:
        ret += regex + '|'
    return ret[:-1]