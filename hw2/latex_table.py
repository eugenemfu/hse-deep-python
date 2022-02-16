def latex_table(table=[[1, 2], [3, '$\\alpha$'], [5, 6]]):
    width = len(table[0])
    res = "\\begin{center}\\begin{tabular}{|" + width * "c|" + "} \\hline "
    for row in table:
        assert len(row) == width
        for i, item in enumerate(row):
            if i > 0:
                res += ' & '
            res += str(item)
        res += " \\\\ \\hline "
    res += "\\end{tabular}\\end{center}"
    return res
    

if __name__ == "__main__":
    with open('artifacts/table.tex', 'w') as f:
        f.write(latex_table())
    