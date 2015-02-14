def combine_regexes(regex_list):
    return '(%s)' % ')|('.join(regex_list)