"""
auth spencer-maaaaan
desc takes a 2d array and returns a html table formatted string

NOTE this assumes that the arrays only contain strings!
"""
indent=20

def to_table(arrays):
    table=""

    for row in arrays:
        table+=" "*indent+"<tr>"

        for el in row:
            table+="<td>"+el+"</td>"

        table+="</tr>\n"

    return table