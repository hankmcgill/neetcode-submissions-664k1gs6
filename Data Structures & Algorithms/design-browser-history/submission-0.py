class BrowserHistory:

    def __init__(self, homepage: str):
        self.sites = [homepage]
        self.curr_page = 0

    def visit(self, url: str) -> None:
        self.sites = self.sites[:self.curr_page + 1]
        self.sites.append(url)
        self.curr_page += 1

    def back(self, steps: int) -> str:
        self.curr_page = max(0, self.curr_page - steps)
        return self.sites[self.curr_page]

    def forward(self, steps: int) -> str:
        self.curr_page = min(len(self.sites) - 1, self.curr_page + steps)
        return self.sites[self.curr_page]