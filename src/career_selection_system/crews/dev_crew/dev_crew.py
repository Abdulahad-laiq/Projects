from crewai import Crew, Agent, Task, Process
from crewai.project import CrewBase, crew, agent, task


@CrewBase
class DevCrew:
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # If you would lik to add tools to your crew, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def medical_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["medical_assistant"],
        )

    @agent
    def engineering_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["engineering_assistant"],
        )
    # To learn more about structured task outputs,
    @agent
    def business_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["business_assistant"],
        )
    # task dependencies, and task callbacks, check out the documentation:
    @agent
    def decision_maker_assistant(self) -> Agent:
        return Agent(
            config=self.agents_config["decision_maker_assistant"],
        )
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def write_medical_benefits(self) -> Task:
        return Task(
            config=self.tasks_config["write_medical_benefits"],
        )

    @task
    def write_engineering_benefits(self) -> Task:
        return Task(
            config=self.tasks_config["write_engineering_benefits"],
        )
    
    @task
    def write_business_benefits(self) -> Task:
        return Task(
            config=self.tasks_config["write_business_benefits"],
        )
    
    @task
    def select_best_career(self) -> Task:
        return Task(
            config=self.tasks_config["select_best_career"],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Research Crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
