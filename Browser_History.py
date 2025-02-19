class BrowserHistory:
    def __init__(self, homepage):
        self.back_stack = []
        self.forward_stack = []
        self.current_page = homepage
        print("Starting at:", self.current_page)

    def visit(self, url):
        print(f"Visiting: {url}")
        self.back_stack.append(self.current_page)
        self.current_page = url
        self.forward_stack.clear()
        print(self.current_page)

    def back(self):
        if not self.back_stack:
            print("Ignored")
            return
        print(f"Going Back from: {self.current_page}")
        self.forward_stack.append(self.current_page)
        self.current_page = self.back_stack.pop()
        print(self.current_page)

    def forward(self):
        if not self.forward_stack:
            print("Ignored")
            return
        print(f"Going Forward from: {self.current_page}")
        self.back_stack.append(self.current_page)
        self.current_page = self.forward_stack.pop()
        print(self.current_page)

def main():
    browser = BrowserHistory("http://www.google.com/")  # Initial page
    while True:
        command = input("Enter command: ").strip()  # Prompt for input
        print(f"Received command: {command}")  # Debugging
        if command == "QUIT":
            break
        elif command.startswith("VISIT "):
            _, url = command.split(maxsplit=1)
            browser.visit(url)
        elif command == "BACK":
            browser.back()
        elif command == "FORWARD":
            browser.forward()
        else:
            print("Ignored")

if __name__ == "__main__":
    main()
