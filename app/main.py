class Car:
    def __init__(
        self,
        comfort_level: int,
        cleanliness_level: int,
        brand: str
    ) -> None:
        self.comfort_level = comfort_level
        self.cleanliness_level = cleanliness_level
        self.brand = brand


class CarWashStation:
    def __init__(
        self,
        distance_from_city_center: float,
        clean_threshold: int,
        average_rating: float,
        count_of_ratings: int
    ) -> None:
        self.distance_from_city_center = distance_from_city_center
        self.clean_threshold = clean_threshold
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def serve_cars(self, cars: list[Car]) -> float:
        income = 0.0
        for car in cars:
            if car.cleanliness_level < self.clean_threshold:
                income += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(income, 1)

    def calculate_washing_price(self, car: Car) -> float:
        price = (car.comfort_level
                 * (self.clean_threshold - car.cleanliness_level)
                 * self.average_rating) / self.distance_from_city_center
        return round(price, 1)

    def wash_single_car(self, car: Car) -> None:
        if self.clean_threshold > car.cleanliness_level:
            car.cleanliness_level = self.clean_threshold

    def rate_service(self, rating: int) -> None:
        total_rating_sum = self.average_rating * self.count_of_ratings
        self.count_of_ratings += 1
        self.average_rating = round((total_rating_sum + rating) / self.count_of_ratings, 1)
