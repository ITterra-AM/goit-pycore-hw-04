def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            cats = []
            for line in file:
                parts = line.strip().split(",")
                if len(parts) < 3:
                    raise ValueError("Invalid data in file")
                cat_id = parts[0]
                name = parts[1]
                age = parts[2]
                cats.append({"id": cat_id, "name": name, "age": age})
    except FileNotFoundError:
        print("File not found")
        return []
    except (ValueError):
        print("Invalid data in file")
        return []
    return cats


cats_info = get_cats_info("cats_info.txt")
print(cats_info)