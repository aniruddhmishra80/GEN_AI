from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

@tool #Decorator for creating tool
def grettings(name : str) -> str:
    """Generate a greating message for the user"""

    return f"hello {name} , Welcome to the AI world"

result = grettings.invoke({"name" : "Aniruddh"})
print(result)

print(grettings.name)
print(grettings.description)
print(grettings.name)