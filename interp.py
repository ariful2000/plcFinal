import regex as re

# to run this (terminal) = python mn.py "test.test"

def lexer(contents):
    rows = []
    ln = contents.split('\n')
    for line in ln:
        str_tm = ""
        tk = []
        ch = list(line)
        qc = 0
        for chr in ch:
            if chr == '"' or chr == "'":
                qc += 1
            if qc % 2 == 0:
                iq = False
            else:
                iq = True
            if chr == " " and iq == False:
                tk.append(str_tm)
                str_tm = ""
            else:
                str_tm += chr
        tk.append(str_tm)
        items = []
        for tkn in tk:
            if tkn[0] == '"' or tkn[0] == "'":
                if tkn[-1] == '"' or tkn[-1] == "'":
                    items.append(("string", tkn))
                else:
                    # Error
                    break
            elif re.match(r"[.a-zA-Z]+", tkn):
                items.append(("symbol", tkn))

        rows.append(items)
    return rows
def parser(file):
    contents = open(file, "r").read()
    tkns = lexer(contents)
    return tkns