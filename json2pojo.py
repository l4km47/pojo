import json

# some JSON:
x = ""

with open("input.json", "r") as inputfile:
    x = inputfile.read()
# parse x:
y = json.loads(x)


def _gettype(object):
    if type(object) is int:
        return "int"
    elif type(object) is str or str(type(object)) == "<class 'NoneType'>":
        return "String"
    elif type(object) is bool:
        return "boolean"
    elif type(object) is float:
        return "float"
    else:
        return "object"


# the result is a Python dictionary:
output = []
i = y[0]
with open("data.txt", "a") as outfile:

    for a in i:
        ff = '\r\n@SerializedName("{0}")\r\n@Expose\r\nprivate {1} {0};'

        aa = ff.format(a, _gettype(i[a]))

        bb = "\r\npublic {1} get{0}() {{\r\nreturn {0};\r\n}}\r\npublic void set{0}({1} x{0}) {{\r\n{0} = x{0};\r\n}}".format(
            a, _gettype(i[a])
        )

        # output.append(f"{aa}\r\n{bb}")
        outfile.write(aa)
        outfile.write(bb)
    outfile.close()
