#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator


def insert_sort(lst, operator_=operator.gt):
    _lst = lst[:]
    N = len(_lst)
    for j in xrange(1, N):
        key = _lst[j]
        i = j - 1
        while i > -1 and operator_(_lst[i], key):
            _lst[i+1] = _lst[i]
            i -= 1
        _lst[i+1] = key
    return _lst


if __name__ == '__main__':
    org = [5, 2, 4, 6, 1, 3]
    print(operator.gt)
    print('from: {0}'.format(org))
    dst = insert_sort(org)
    print('  to: {0}'.format(dst))

    print(operator.lt)
    print('from: {0}'.format(org))
    dst = insert_sort(org, operator.lt)
    print('  to: {0}'.format(dst))