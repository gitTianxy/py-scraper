# encoding=utf-8
"""
regex demo
-------------------------
I. match process：
    1.依次拿出表达式和文本中的字符比较，
    2.如果每一个字符都能匹配，则匹配成功；一旦有匹配不成功的字符则匹配失败。
    3.如果表达式中有量词或边界，这个过程会稍微有一些不同。
II. classification
    1. 贪婪: 尝试匹配尽可能多的字符(python default)
    2. 非贪婪: 匹配到最少的字符后即返回(what we normally use)
III. aim
    1. to retrieve target str from content
IV. CONTENT
    1. basic function of regex
        - start/end with: ^, $
        - number/word/letter: \d, \w, [A-Za-z]
        - define match count: {m,n}
        - define match range: [...]
        - build-in, special symbol
        - pattern group: (...)
        - control expression:
            - or: |
            - if-else: ?(condition)yes-pattern|no-pattern
            - not: (!...), [^...]
        - at, before, after match:
            - at: ...
            - before: (?<=pattern-before)pattern-at/(?<!pattern-not-before)pattern-at,
            - after: (?=pattern-after)pattern-at/(?!pattern-not-after)pattern-at
        - greedy/non-greedy math:
            - greedy: *, +, {m,}
            - non-greedy: ?, *?, +?, {m,}?
        - annotation: #
    2. use regex in python -- API function of 're' package
        - api-function:
            0. compile(regex-str): return compiled pattern
            1. match(regex-str, string[, mode]): match from the start of the string, return with one-possible-match
            2. search(regex-str, string[, mode]): match start from any position of the string, return with
            one-possible-match
            3.
            4.
        - two forms:
            1. re.api_function(regex-str/pattern, params)
            2. pattern = re.compile(regex-str); pattern.api_function(params)
        - match modes: only care 'i'--ignore bold-/small-case
"""

import re


def match(regex_str, target_str):
    """
    match start with pattern
    :param regex_str:
    :param target_str:
    :return:
    """
    res = re.match(regex_str, target_str)
    if res:
        print res.group()
    else:
        print '%s not match %s' % (target_str, regex_str)


def search(regex_str, target_str):
    """
    match contains pattern
    :param regex_str:
    :param target_str:
    :return:
    """
    res = re.search(regex_str, target_str)
    if res:
        print res.group()
    else:
        print '%s not in %s' % (target_str, regex_str)


def find_all(regex_str, taret_str):
    """
    pick out all the matches
    :param regex_str:
    :param taret_str:
    :return:
    """
    print re.findall(regex_str, taret_str)


def find_itr(regex_str, target_str):
    """
    return iterator of all the matches
    :param regex_str:
    :param target_str:
    :return:
    """
    print [m.group() for m in re.finditer(regex_str, target_str)]


def split(regex_str, target_str):
    """
    split string by the pattern
    :param regex_str:
    :param target_str:
    :return:
    """
    print re.split(regex_str, target_str)


def replace(regex_str, target_str, repl_str):
    """
    replace all the matches target_str with the 'repl_str'
    :param regex_str:
    :param target_str:
    :param repl_str:
    :param repl_count:
    :return: result string
    """
    print re.sub(regex_str, repl_str, target_str)


def replace_with_num(regex_str, target_str, repl_str):
    """
    replace all the matches target_str with the 'repl_str'
    :param regex_str:
    :param target_str:
    :param repl_str:
    :return: result dict
    """
    res = re.subn(regex_str, repl_str, target_str)
    print dict(repl_res=res[0], repl_count=res[1])


if __name__ == '__main__':
    match(r'hello', 'hello after')
    match(r'hello', 'before hello')
    match(r'hello', 'hello hello interval hello')
    search(r'hello', 'hello hello interval hello')
    find_all(r'hello', 'hello hello XXX hello')
    find_itr(r'hello', 'hello hello XXX hello')
    replace(r'hello', 'hello hello XXX hello', r'sorry')
    replace_with_num(r'hello', 'hello hello XXX hello', r'sorry')
