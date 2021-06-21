#!/usr/bin/python3

import os.path as p

pwd = p.abspath(p.dirname(__file__))

drop_html_from_input = True  # for non-web only, just pages for printing
work_location = "/var/www/html/"
index_file_name = "index.html"
printable_file_name = "printable.html"

first_print_column = [
    "About me",
    "Skills",
    "Education",
]
drop_first = 1
tab_replacement = "   "

cv = open(p.join(pwd, "cv.txt")).read()
cv = cv.split("\n")
if drop_html_from_input:
    work_location = "other"
    cv[0] = cv[0][3:]
    tmp = cv[-5:]
    cv = [
        e
        for e in cv
        if "<" not in e
        and "readable CV" not in e
    ]
    tmp = [e for e in tmp if "<" in e]
    cv += tmp
t1 = open(
    p.join(pwd, "html/read_template.html")
).read()
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
            ele.replace("\t", tab_replacement)
            + "\n"
        )
    except:
        cv_parse[group] = (
            ele.replace("\t", tab_replacement)
            + "\n"
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

contents = []
if not drop_html_from_input:
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

open(
    p.join(work_location, index_file_name), "w"
).write(t1)

t2 = t2.replace("{input1}", print_cv[1])
t2 = t2.replace("{input2}", print_cv[2])

# reduce whitespace to +readability
t2.replace("   ", "  ")
open(
    p.join(work_location, printable_file_name),
    "w",
).write(t2)

print("Done. Good luck!")
