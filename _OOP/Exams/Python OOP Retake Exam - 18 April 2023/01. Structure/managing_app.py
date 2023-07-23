from typing import List
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar
from project.route import Route


class ManagingApp:

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[CargoVan, PassengerCar] = []
        self.routes: List[Route] = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str) -> str:
        if any(user for user in self.users if user.driving_license_number == driving_license_number):
            return f"{driving_license_number} has already been registered to our platform."

        user = User(first_name, last_name, driving_license_number)
        self.users.append(user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in ['CargoVan', 'PassengerCar']:
            return f"Vehicle type {vehicle_type} is inaccessible."
        if any(x for x in self.vehicles if x.license_plate_number == license_plate_number):
            return f"{license_plate_number} belongs to another vehicle."

        vehicle = globals()[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):

        if any(route for route in self.routes if route.start_point == start_point and route.end_point == end_point and route.length == length):
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        if any(route for route in self.routes if route.start_point == start_point and route.end_point == end_point and route.length < length):
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        for route in self.routes:
            if route.start_point == start_point and route.end_point == end_point and route.length > length:
                route.is_locked = True

        route_id = len(self.routes) + 1
        route = Route(start_point, end_point, length, route_id)
        self.routes.append(route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = next(x for x in self.users if x.driving_license_number == driving_license_number)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = next(x for x in self.vehicles if x.license_plate_number == license_plate_number)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = next(x for x in self.routes if x.route_id == route_id)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle.drive(route.length)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return f"{vehicle.brand} {vehicle.model} License plate: {license_plate_number} Battery: {vehicle.battery_level}% Status: {'Damaged' if vehicle.is_damaged else 'OK'}"

    def repair_vehicles(self, count: int) -> str:
        damaged = [x for x in self.vehicles if x.is_damaged]
        sorted_vehicle = sorted(damaged, key=lambda x: (x.brand, x.model))
        repaired = 0

        for i in range(len(damaged)):
            if count == 0:
                break
            sorted_vehicle[repaired].is_damaged = False
            sorted_vehicle[repaired].recharge()
            repaired += 1
            count -= 1

        return f"{repaired} vehicles were successfully repaired!"

    def users_report(self):
        res = ["*** E-Drive-Rent ***"]
        users = sorted(self.users, key=lambda x: -x.rating)
        users_by_rating = [str(user) for user in users]
        res.extend(users_by_rating)
        return "\n".join(res)

