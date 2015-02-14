def combine_regexes(regex_list):
    return r'(%s)' % ')|('.join(regex_list)