from phi.agent import Agent 
from phi.model.groq import Groq 
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

def get_company_symbol(company: str) -> str:
    symbols = {
        "phidata":"PDT",
        "Infosys":"INFY",
        "Tesla":"TSLA",
        "Apple":"AAPL",
        "Microsoft":"MSFT",
        "Amazon":"AMZN",
        "Google":"GOOGL",
    }
    return symbols.get(company, "Unknown")

agent = Agent(
    model = Groq(id="llama-3.3-70b-versatile"),
    tools = [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True), get_company_symbol],
    show_tool_calls=True, 
    markdown=True,
    instructions=["Use tables inorder to display the data.", "If you do not know the company symbol use get_company_symbol tool, even if it is not a public company"],
    debug_mode=False
)

agent.print_response("Summarize and compare analyst recommendations and fundamentals for Tesla and Phidata")

