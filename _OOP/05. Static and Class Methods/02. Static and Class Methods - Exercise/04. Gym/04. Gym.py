from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
customer1 = Customer("Penka", "Slavqnska Street", "lolo.smith@gmail.com")
equipment = Equipment("Treadmill")
equipment1 = Equipment("SmithMachine")
trainer = Trainer("Peter")
trainer11 = Trainer("Ganio")
subscription = Subscription("14.05.2020", 1, 1, 1)
subscription1 = Subscription("124.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)
plan1 = ExercisePlan(1, 1, 20)
gym = Gym()
gym.add_customer(customer)
gym.add_customer(customer1)
gym.add_equipment(equipment)
gym.add_equipment(equipment1)
gym.add_trainer(trainer)
gym.add_trainer(trainer11)
gym.add_plan(plan)
gym.add_plan(plan1)
gym.add_subscription(subscription)
gym.add_subscription(subscription1)
# print(customer)
print(Customer.get_next_id())
# print(customer)
print(gym.subscription_info(2))
