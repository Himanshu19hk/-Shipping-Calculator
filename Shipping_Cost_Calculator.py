def calculate_shipping(weight, distance, speed='standard'):
    base_rate = 5  # per kg per 100 km
    cost = (weight * distance * base_rate) / 100

    if speed == 'express':
        cost *= 1.5
        days = 1
    else:
        days = 3

    return round(cost, 2), days

if __name__ == "__main__":
    w = float(input("Enter weight (kg): "))
    d = float(input("Enter distance (km): "))
    s = input("Enter shipping speed (standard/express): ").strip().lower()

    final_cost, delivery_days = calculate_shipping(w, d, s)
    print(f"Shipping Cost: ${final_cost}")
    print(f"Estimated Delivery: {delivery_days} day(s)")
