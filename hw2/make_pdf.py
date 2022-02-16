import subprocess
from latex_table import *
from latex_picture import *
from hw1_package.main import generate_graph


def make_pdf(table=[[1, 2], [3, '$\\alpha$'], [5, 6]], picture="artifacts/picture.png", output='artifacts/document.tex'):
    res = "\\documentclass{article} \\usepackage[utf8]{inputenc} \\usepackage{graphicx} \\begin{document}"
    res += latex_table(table)
    generate_graph("../hw1/fib.py", picture)
    res += latex_picture(picture)
    res += "\\end{document}"
    with open(output, 'w') as f:
        f.write(res)
    print(subprocess.call(['pdflatex', '-output-directory', 'artifacts/', output], shell=False))


if __name__ == "__main__":
    make_pdf()