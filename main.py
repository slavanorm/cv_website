#!/usr/bin/python3

import os.path as p

pwd = p.abspath(p.dirname(__file__))

first_print_column=["About me", "Skills",
"Education"]
drop_first = 3
tab_replacement = "   "

cv = open(p.join(pwd, "cv.txt")).read()
cv = cv.split("\n")
t1 = open(p.join(pwd, "html/read_template.html")).read()
t2 = open(
    p.join(pwd, "html/print_template.html")
).read()

# toml-style -> dict
cv_parse = {}
group = ""
for ele in cv:
    if not ele.count("\t"):
        if len(ele.strip()):
            group = ele.strip()

    try:
        cv_parse[group] += (
            ele.replace("\t", tab_replacement) + "\n"
        )
    except:
        cv_parse[group] = (
            ele.replace("\t", tab_replacement) + "\n"
        )

# dict -> html
cv = ""
print_cv = {1: "", 2: ""}
i = 0
for k, v in cv_parse.items():
    cv += f"""<span id="{k}" class="section scrollspy">{v}</span>"""
    if v.strip() != "":
        i += 1
    if k in first_print_column:
        print_cv[1] += v
    elif i > drop_first:
        print_cv[2] += v

contents = [k for k in cv_parse.keys()]
contents = contents[drop_first:]
contents = [
    f"""<li><a href="#{ele}">{ele}</a></li>"""
    for ele in contents
]
contents = "".join(contents)

# html -> templates
t1 = t1.replace("{input}", cv)
t1 = t1.replace("{contents}", contents)

open("/var/www/html/index.html", "w").write(t1)

t2 = t2.replace("{input1}", print_cv[1])
t2 = t2.replace("{input2}", print_cv[2])

# reduce whitespace to +readability
t2.replace("   ", "  ")
open("/var/www/html/printable.html", "w").write(t2)

print("Done. Good luck!")
