from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        expenses = 250_000
        oracle = {1: 1_500_000, 2: 800_000}
        honda = {8: 20_000, 10: 10_000}
        revenue = 0
        if race_pos in oracle:
            revenue = oracle[race_pos]
            revenue += honda[8]
        elif race_pos in honda:
            revenue = honda[race_pos]

        profit = revenue - expenses
        self.budget += profit

        return f"The revenue after the race is {profit}$. Current budget {self.budget}$"
