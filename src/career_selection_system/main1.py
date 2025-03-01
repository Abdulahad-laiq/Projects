from crewai.flow import Flow, start, listen
from career_selection_system.crews.dev_crew.dev_crew import DevCrew

class DevFlow(Flow):
    @start()
    def run_crew(self):
        output = DevCrew().crew().kickoff(
            inputs={
                "query": "help me in selecting the best career among the following options: medical, engineering, business.",
            }
        )
        return output.raw
    
def kickoff():
    obj = DevFlow()
    result = obj.kickoff()
    print(result)
    obj.plot()   
    
    
