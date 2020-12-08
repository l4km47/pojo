import json

# some JSON:
input = ""

with open("input.json", "r") as inputfile:
    input = inputfile.read()
# parse x:
jasondata = json.loads(input)

#get data type as java
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
firstdataset = jsondata[0]
with open("data.txt", "a") as outfile:

    for a in firstdataset:
        variable_string = '\r\n@SerializedName("{0}")\r\n@Expose\r\nprivate {1} {0};'

        variable_formated = variable_string.format(a, _gettype(i[a]))

        prop_string = "\r\npublic {1} get{0}() {{\r\nreturn {0};\r\n}}\r\npublic void set{0}({1} x{0}) {{\r\n{0} = x{0};\r\n}}".format(
            a, _gettype(i[a])
        )

        # write output
        outfile.write(variable_formated)
        outfile.write(prop_string)
    outfile.close() #save and close
