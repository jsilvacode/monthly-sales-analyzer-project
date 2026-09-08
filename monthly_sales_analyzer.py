# Datos de ejemplo
sales_data = [
    {"day": 1, "product_a": 202, "product_b": 142, "product_c": 164},
    {"day": 2, "product_a": 206, "product_b": 121, "product_c": 338},
    {"day": 3, "product_a": 120, "product_b": 152, "product_c": 271},
    {"day": 4, "product_a": 174, "product_b": 137, "product_c": 266},
    {"day": 5, "product_a": 199, "product_b": 153, "product_c": 301},
    {"day": 6, "product_a": 230, "product_b": 199, "product_c": 202},
    {"day": 7, "product_a": 101, "product_b": 137, "product_c": 307},
    {"day": 8, "product_a": 137, "product_b": 179, "product_c": 341},
    {"day": 9, "product_a": 287, "product_b": 70, "product_c": 310},
    {"day": 10, "product_a": 157, "product_b": 71, "product_c": 238},
    {"day": 11, "product_a": 148, "product_b": 108, "product_c": 319},
    {"day": 12, "product_a": 287, "product_b": 64, "product_c": 339},
    {"day": 13, "product_a": 289, "product_b": 100, "product_c": 257},
    {"day": 14, "product_a": 154, "product_b": 113, "product_c": 280},
    {"day": 15, "product_a": 150, "product_b": 184, "product_c": 170},
    {"day": 16, "product_a": 172, "product_b": 67, "product_c": 281},
    {"day": 17, "product_a": 188, "product_b": 109, "product_c": 163},
    {"day": 18, "product_a": 108, "product_b": 139, "product_c": 202},
    {"day": 19, "product_a": 229, "product_b": 133, "product_c": 241},
    {"day": 20, "product_a": 210, "product_b": 57, "product_c": 324}
]


def total_sales_by_product(data, product_key):
    """Calcula las ventas totales de un producto específico."""
    total = 0

    for day in data:
        total += day[product_key]

    return total


def average_daily_sales(data, product_key):
    """Calcula el promedio diario de ventas de un producto específico."""
    total = total_sales_by_product(data, product_key)
    return total / len(data)


def best_selling_day(data):
    """Encuentra el día con el mayor total de ventas."""
    best_day = None
    highest_total = 0

    for day in data:
        daily_total = day["product_a"] + day["product_b"] + day["product_c"]

        if daily_total > highest_total:
            highest_total = daily_total
            best_day = day["day"]

    return best_day


def days_above_threshold(data, product_key, threshold):
    """Cuenta cuántos días las ventas de un producto superaron un umbral determinado."""
    count = 0

    for day in data:
        if day[product_key] > threshold:
            count += 1

    return count


def top_product(data):
    """Determina qué producto obtuvo el mayor total de ventas."""
    products = ["product_a", "product_b", "product_c"]
    top = None
    highest_total = 0

    for product in products:
        total = total_sales_by_product(data, product)

        if total > highest_total:
            highest_total = total
            top = product

    return top


# Pruebas de las funciones
print("Ventas totales del producto A:", total_sales_by_product(sales_data, "product_a"))
print("Promedio diario de ventas del producto B:", average_daily_sales(sales_data, "product_b"))
print("Día con el mayor total de ventas:", best_selling_day(sales_data))
print("Días en que el producto C superó las 300 ventas:", days_above_threshold(sales_data, "product_c", 300))
print("Producto con el mayor total de ventas:", top_product(sales_data))
