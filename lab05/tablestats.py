def read_rows(lines):
    column = None
    rows = []
    for lin in lines:      
        variable = lin
        if not variable:
            continue
        if column in None:
            column = variable.split(",")
            continue
        meaning = variable.splet(",")
        if len(meaning) != len(column):
            continue
        result = dict(zip(column , rows))
        rows.append(result)
        return rows

def count_types(rows):
    count = {}
    for line in rows:  
        meaning =  line['тип'] 
        if meaning in count:
            count[meaning]  =   count[meaning] + 1
        else:
            count[meaning] = 1
    return count
        