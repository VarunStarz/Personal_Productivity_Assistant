import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent

def discussProjectDeliverables(input: str):
    """Meeting notes: Discuss project X deliverables on Monday.

    Args:
        input (str): The activity name or the day of the week.

    Returns:
        Output based on the description.
    """
    return 'Meeting notes: Discuss project X deliverables on Monday'

def submitReport(input: str):
    """Reminder: Submit report by Friday.

    Args:
        input (str): The activity name or the day of the week.

    Returns:
        Output based on the description.
    """
    return 'Reminder: Submit report by Friday'

def techConference(input: str):
    """Upcoming event: Tech Conference next Wednesday.

    Args:
        input (str): The activity name or the day of the week.

    Returns:
        Output based on the description.
    """
    return 'Upcoming event: Tech Conference next Wednesday'

root_agent = Agent(
    name="assistant_agent",
    model="gemini-2.0-flash",
    description=(
        "Agent to answer questions about activities of an assistant."
    ),
    instruction=(
        "You are a helpful agent who can answer user questions about activities of an assistant."
    ),
    tools=[discussProjectDeliverables, submitReport, techConference]
)