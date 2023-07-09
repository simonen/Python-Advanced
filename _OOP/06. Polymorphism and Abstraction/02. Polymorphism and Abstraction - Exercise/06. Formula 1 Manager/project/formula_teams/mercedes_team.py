from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        expenses = 200_000
        petronas = {1: 1_000_000, 3: 500_000}
        teamviewer = {5: 100_000, 7: 50_000}
        revenue = 0
        if race_pos in petronas:
            revenue = petronas[race_pos]
            revenue += teamviewer[5]
        elif race_pos in teamviewer:
            revenue = teamviewer[race_pos]

        profit = revenue - expenses
        self.budget += profit

        return f"The revenue after the race is {profit}$. Current budget {self.budget}$"
