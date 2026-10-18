def read_rows(lines):
    column = None
    rows = []
    for lin in lines:
        variable = lin.strip()
        if variable == "":
            continue
            
        if column is None:
            column = []
            for name in variable.split(","):
                column.append(name.strip())
            continue
        meaning = []
        for value in variable.split(","):
            meaning.append(value.strip()) 
        if len(meaning) != len(column):
            continue
        result = dict(zip(column, meaning))
        rows.append(result)
        
    return rows


def count_types(rows):
    count = {}
    for line in rows:
        meaning = line['тип']
        if meaning in count:
            count[meaning] = count[meaning] + 1
        else:
            count[meaning] = 1
    return count


def total_minutes(rows, kind):
    total = 0.0
    
    for row in rows:
        if row["тип"] == kind:
            clean_val = row["минуты"].replace(",", ".")
            if clean_val.replace(".", "", 1).isdigit():
                total = total + float(clean_val)
    
    return round(total, 1)


def to_csv(counts):
    result = ["тип,количество"]
    for kind in sorted(counts.keys()):
        line = f"{kind},{counts[kind]}"
        result.append(line)
        
    final_text = "\n".join(result) + "\n"
    return final_text