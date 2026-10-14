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
        
def total_minutes(rows, kind):
    total = 0.0

    for row in rows:
        if row["тип"] == kind:
            clean_val = row["минуты"].replace(",", ".")
            total = total + float(clean_val)
    return round(total , 1)
    
