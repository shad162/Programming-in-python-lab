def display_resources(resources):
    print(f"\n{'ID':<5} | {'Resource Name':<20} | {'Category':<15} | {'Total':<8} | {'Available':<10}")
    print("-" * 68)
    for res in resources:
        print(f"{res['id']:<5} | {res['name']:<20} | {res['category']:<15} | {res['total']:<8} | {res['available']:<10}")


def search_by_category(resources, category):
    print(f"\n--- Resources in Category: '{category}' ---")
    filtered_resources = [res for res in resources if res['category'].lower() == category.lower()]
    
    if not filtered_resources:
        print("No resources found in this category.")
    else:
        display_resources(filtered_resources)


def find_unavailable(resources):
    print("\n--- Out of Stock / Unavailable Resources ---")
    unavailable_resources = [res for res in resources if res['available'] == 0]
    
    if not unavailable_resources:
        print("All resources are currently available!")
    else:
        display_resources(unavailable_resources)


if __name__ == "__main__":
    university_resources = [
        {"id": 101, "name": "Dell XPS Laptop", "category": "Laptops", "total": 15, "available": 4},
        {"id": 102, "name": "Epson 4K Projector", "category": "Projectors", "total": 8, "available": 0},
        {"id": 103, "name": "MacBook Pro", "category": "Laptops", "total": 10, "available": 7},
        {"id": 104, "name": "Digital Microscope", "category": "Lab Equipment", "total": 5, "available": 0},
        {"id": 105, "name": "Oscilloscope", "category": "Lab Equipment", "total": 4, "available": 2},
    ]

    print("1. Displaying All University Resources:")
    display_resources(university_resources)

    print("\n2. Testing Category Search:")
    search_by_category(university_resources, "Laptops")

    print("\n3. Testing Unavailable Resources Lookup:")
    find_unavailable(university_resources)
