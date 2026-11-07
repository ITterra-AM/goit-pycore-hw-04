def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            pcount = 0
            for line in file:
                parts = line.strip().split(",")
                total += int(parts[1])
                pcount += 1    
    except FileNotFoundError:
        print("File not found")
        return 0, 0
    except (ValueError, IndexError):
        print("Invalid data in file")
        return 0, 0
    average = total // pcount if pcount > 0 else 0
    return total, average


total, average = total_salary("people_salary.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")